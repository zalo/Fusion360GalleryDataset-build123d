"""Batch 006 - passing/04_6to7ops
87 models bundled from Fusion360 Gallery reconstructions.
"""

from build123d import *
from build123d import Edge, BuildLine
from collections import Counter
from OCP.BRepBuilderAPI import BRepBuilderAPI_MakeEdge
from OCP.Geom import Geom_BSplineCurve
from OCP.TColStd import TColStd_Array1OfReal, TColStd_Array1OfInteger
from OCP.TColgp import TColgp_Array1OfPnt
from OCP.gp import gp_Pnt


# Description: This is a hexahedral (box-like) metal bracket or housing component with an irregular angular geometry, featuring multiple planar faces, internal recesses or cutouts, and a complex 3D structure designed for structural support or part mounting.
def model_31280_c8bd4b11_0010():
    """Model: Magnifier Holder"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.5293141653, perimeter: 9.3424777961
            with BuildLine():
                Line((-1.5, 0.6), (1.5, 0.6))
                Line((-1.5, -0.6), (-1.5, 0.6))
                Line((1.5, -0.6), (-1.5, -0.6))
                Line((1.5, 0.6), (1.5, -0.6))
            make_face()
            with BuildLine():
                CenterArc((1.1000000164, 0), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((1.1000000164, 0)):
                Circle(0.15)
        # OneSide extrude, distance=1.2
        extrude(amount=1.2)

        # Sketch1 -> Extrude2 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((1.1000000164, 0)):
                Circle(0.15)
        # OneSide extrude, distance=1.2
        extrude(amount=1.2, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(1.5, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((0, 0.6500000097)):
                Circle(0.15)
        # OneSide extrude, distance=-0.316
        extrude(amount=-0.316, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a elongated metal bracket or guide rail with a rectangular profile, featuring a left-side vertical flange, a long horizontal body with a central slot or channel running lengthwise, and a small rectangular cutout or hole on the right end.
def model_31360_a1accb4b_0008():
    """Model: 3-Connecting Rod H"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 5 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 2.3343362939, perimeter: 10.6566370614
            with BuildLine():
                Line((-4.1, 0.6), (0, 0.6))
                Line((-4.1, 0), (-4.1, 0.6))
                Line((0, 0), (-4.1, 0))
                Line((0, 0.6), (0, 0))
            make_face()
            with BuildLine():
                CenterArc((-0.3, 0.3), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 10 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-4.1, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))) as sk:
            # Profile area: 0.0600000009, perimeter: 1.4000000179
            with BuildLine():
                Line((0, 0), (-0.1, 0))
                Line((0, 0.6000000089), (0, 0))
                Line((-0.1, 0.6000000089), (0, 0.6000000089))
                Line((-0.1, 0), (-0.1, 0.6000000089))
            make_face()
            # Profile area: 0.0600000009, perimeter: 1.4000000179
            with BuildLine():
                Line((0.2, 0.6000000089), (0.3, 0.6000000089))
                Line((0.2, 0), (0.2, 0.6000000089))
                Line((0.3, 0), (0.2, 0))
                Line((0.3, 0.6000000089), (0.3, 0))
            make_face()
        # TwoSides extrude, along=0.35, against=-0.2
        extrude(amount=0.35, mode=Mode.ADD)
        extrude(sk.sketch, amount=-0.2, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -0.1), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.0176714587, perimeter: 0.471238898
            with Locations((4.3, 0.2999999911)):
                Circle(0.075)
        # OneSide extrude, distance=-0.4
        extrude(amount=-0.4, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a linear bearing or rail assembly featuring two parallel blue rectangular blocks connected by a central dark cylindrical or spherical joint mechanism, designed to allow linear motion along a horizontal axis while maintaining alignment.
def model_31462_84375249_0005():
    """Model: Salt Bar v3 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 19 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.3519248752, perimeter: 3.5037410321
            with BuildLine():
                Line((-0.249458822, 0.1000000015), (-0.7500000112, 0.1000000015))
                Line((-0.7500000112, 0.1000000015), (-0.7500000112, -0.1000000015))
                Line((-0.7500000112, -0.1000000015), (-0.2502335411, -0.1000000015))
                CenterArc((-0.2502335411, -0.2641952114), 0.1641952099, 49.1437719951, 40.8562280049)
                CenterArc((-0.2502335411, -0.2641952114), 0.1641952099, 43.9654961224, 5.1782758727)
                CenterArc((0, 0), 0.2, -131.3199816676, 82.8654331402)
                CenterArc((0.2763879712, -0.3067149737), 0.2128867878, 131.5743444578, 0.8968049337)
                CenterArc((0.2763879712, -0.3067149737), 0.2128867878, 103.8300767199, 27.7442677379)
                Line((0.2254988302, -0.1000000015), (0.7500000112, -0.1000000015))
                Line((0.7500000112, -0.1000000015), (0.7500000112, 0.1000000015))
                Line((0.7500000112, 0.1000000015), (0.2504609622, 0.1000000015))
                CenterArc((0.2504609622, 0.2646296135), 0.164629612, -131.0037230536, 41.0037230536)
                CenterArc((0.2504609622, 0.2646296135), 0.164629612, -135.844989367, 4.8412663134)
                CenterArc((0, 0), 0.2, 48.5679920724, 83.1012633799)
                CenterArc((-0.249458822, 0.2620564746), 0.1620564731, -48.7805077338, 4.7394128607)
                CenterArc((-0.249458822, 0.2620564746), 0.1620564731, -90, 41.2194922662)
            make_face()
        # OneSide extrude, distance=0.11
        extrude(amount=0.11)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.11, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0298341425, perimeter: 0.6122964082
            Circle(0.09745)
        # OneSide extrude, distance=-0.15
        extrude(amount=-0.15, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a parallel jaw gripper or clamp assembly featuring two opposing rectangular plates with dark cylindrical jaw elements and connecting structural members, designed to grip or hold objects between its parallel surfaces.
def model_31645_11901b20_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 13 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 16.4999998435, perimeter: 38
            with BuildLine():
                Line((-7.5, 0), (-7.5, 2.5))
                Line((7.5, 0), (-7.5, 0))
                Line((7.5, 2.5), (7.5, 0))
                Line((7, 2.5), (7.5, 2.5))
                Line((7, 1), (7, 2.5))
                Line((-7.0000001043, 1), (7, 1))
                Line((-7.0000001043, 2.5), (-7.0000001043, 1))
                Line((-7.5, 2.5), (-7.0000001043, 2.5))
            make_face()
        # Symmetric extrude, each_side=6
        extrude(amount=6, both=True)

        # Sketch2 -> Extrude2 (NewBody)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(-7.0000001043, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.2566370989, perimeter: 3.9738353655
            with Locations((-5.0000000745, 1.7000000253)):
                Circle(0.6324555415)
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch19 -> Extrude19 (NewBody)
        # Sketch on BRepFace
        # Sketch has 7 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 6), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 3.4427487444, perimeter: 36.7171269763
            with BuildLine():
                Line((-7.6894839381, 5.5), (-7.6894839381, 7.0895941524))
                Line((-7.6894839381, 5.5), (-7.5, 5.5))
                Line((-7.5, 5.5), (-7.5, 6.9000001028))
                Line((-7.5, 6.9000001028), (7.4935239529, 6.891289711))
                Line((7.4935239529, 6.891289711), (7.4927126798, 5.49481497))
                Line((7.4927126798, 5.49481497), (7.6821965859, 5.4947048905))
                Line((7.6831179384, 7.0806635376), (7.6821965859, 5.4947048905))
                Line((-7.6894839381, 7.0895941524), (7.6831179384, 7.0806635376))
            make_face()
        # OneSide extrude, distance=-12
        extrude(amount=-12)
    return part.part


# Description: This is a rectangular duct or channel with a long, slender box-like shape featuring vertical fluting or ribbing along its sides, designed for structural reinforcement and airflow management.
def model_31751_e37382e1_0003():
    """Model: Component4"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.0335228379, perimeter: 0.9295781322
            with BuildLine():
                Line((0.1199999973, 0.1599999964), (0.1138785781, 0.1436762119))
                Line((0.1554497691, 0.1599999964), (0.1199999973, 0.1599999964))
                Line((0.1554497691, 0.1599999964), (0.1856244144, 0.1955696409))
                Line((0.1856244144, 0.1955696409), (-0.0958367332, 0.4462914104))
                Line((-0.1591105906, 0.3752599537), (-0.0958367332, 0.4462914104))
                Line((0.1138785781, 0.1436762119), (-0.1591105906, 0.3752599537))
            make_face()
            # Profile area: 0.0007051868, perimeter: 0.1133652154
            with BuildLine():
                Line((0.1299999971, 0.1299999971), (0.1554497691, 0.1599999964))
                Line((0.1554497691, 0.1599999964), (0.1199999973, 0.1599999964))
                Line((0.1199999973, 0.1599999964), (0.1138785781, 0.1436762119))
                Line((0.1299999971, 0.1299999971), (0.1138785781, 0.1436762119))
            make_face()
        # OneSide extrude, distance=0.03
        extrude(amount=0.03)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0097132654, perimeter: 0.697141096
            with BuildLine():
                Line((0.1162663474, 0.378254782), (0.0933902224, 0.403935601))
                Line((0.0933902224, 0.403935601), (-0.1438038221, 0.1926463661))
                Line((-0.1438038221, 0.1926463661), (-0.1265301348, 0.1722842738))
                Line((-0.1265301348, 0.1722842738), (0.1162663474, 0.378254782))
            make_face()
        # OneSide extrude, distance=-0.01
        extrude(amount=-0.01, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(-0.03, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.0097132654, perimeter: 0.697141096
            with BuildLine():
                Line((0.1265301348, 0.1722842738), (0.1438038221, 0.1926463661))
                Line((0.1438038221, 0.1926463661), (-0.0933902224, 0.403935601))
                Line((-0.0933902224, 0.403935601), (-0.1162663474, 0.378254782))
                Line((-0.1162663474, 0.378254782), (0.1265301348, 0.1722842738))
            make_face()
        # OneSide extrude, distance=-0.01
        extrude(amount=-0.01, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a hexagonal or elongated box-shaped structural component with multiple triangular cutouts and openings along its sides, featuring a tapered end and a complex lattice-like internal structure for weight reduction.
def model_31962_e5291336_0001():
    """Model: Rectángulo"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 11.1973009183, perimeter: 19.1415926536
            with BuildLine():
                Line((-19.8875070658, 16.4020676831), (-19.8875070658, 14.5020676831))
                Line((-19.8875070658, 14.5020676831), (-13.7875070658, 14.5020676831))
                Line((-13.7875070658, 16.4020676831), (-13.7875070658, 14.5020676831))
                Line((-19.8875070658, 16.4020676831), (-13.7875070658, 16.4020676831))
            make_face()
            with BuildLine():
                CenterArc((-14.8375070658, 15.7020676831), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-18.8375070658, 15.7020676831), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.9
        extrude(amount=1.9)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 16.4020676831, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            with Locations((-0.95, 16.8375070658)):
                Circle(0.3)
        # OneSide extrude, distance=-3.5
        extrude(amount=-3.5, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 14.5020676831, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.6675884389, perimeter: 5.3407075111
            with BuildLine():
                CenterArc((0.95, 16.8375070658), 0.55, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0.95, 16.8375070658), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.8
        extrude(amount=-0.8, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a stepped cylindrical connector or adapter featuring a smaller-diameter shaft on the left transitioning to a larger-diameter hollow cylinder on the right, with internal ribbed or fluted surface patterns visible through the mesh rendering.
def model_31962_e5291336_0002():
    """Model: Tornillo"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.3848451001, perimeter: 2.1991148575
            with Locations((35, -3)):
                Circle(0.35)
        # OneSide extrude, distance=0.4
        extrude(amount=0.4)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((-35, -3)):
                Circle(0.2)
        # OneSide extrude, distance=0.6
        extrude(amount=0.6, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0.4, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0779422863, perimeter: 1.0392304845
            with BuildLine():
                Line((35.1252831757, -2.8804001426), (34.9590650731, -2.8317016585))
                Line((34.9590650731, -2.8317016585), (34.8337818974, -2.9513015158))
                Line((34.8337818974, -2.9513015158), (34.8747168243, -3.1195998574))
                Line((34.8747168243, -3.1195998574), (35.0409349269, -3.1682983415))
                Line((35.0409349269, -3.1682983415), (35.1662181026, -3.0486984842))
                Line((35.1662181026, -3.0486984842), (35.1252831757, -2.8804001426))
            make_face()
        # OneSide extrude, distance=-0.3
        extrude(amount=-0.3, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a flanged shaft coupling featuring a large circular flange with a central hub and cylindrical shaft extensions on both ends, designed to connect and transmit torque between two rotating shafts.
def model_31962_e5291336_0005():
    """Model: ISO"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.4536459792, perimeter: 2.3876104167
            with Locations((18.7538668244, 1.6063675667)):
                Circle(0.38)
        # OneSide extrude, distance=0.22
        extrude(amount=0.22)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.22, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((18.7538668244, 1.6063675667)):
                Circle(0.2)
        # OneSide extrude, distance=0.8
        extrude(amount=0.8, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.0541265877, perimeter: 0.8660254038
            with BuildLine():
                Line((-18.6141801408, 1.6427126318), (-18.7154992323, 1.7455123158))
                Line((-18.7154992323, 1.7455123158), (-18.8551859159, 1.7091672506))
                Line((-18.8551859159, 1.7091672506), (-18.893553508, 1.5700225015))
                Line((-18.893553508, 1.5700225015), (-18.7922344165, 1.4672228175))
                Line((-18.7922344165, 1.4672228175), (-18.6525477329, 1.5035678827))
                Line((-18.6525477329, 1.5035678827), (-18.6141801408, 1.6427126318))
            make_face()
        # OneSide extrude, distance=-0.3
        extrude(amount=-0.3, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a shaft with an integral flange, featuring a cylindrical shaft on the left and a larger circular disk-like flange on the right, with the flange appearing to have radial cooling fins or ribbed texture on its outer surface.
def model_31962_e5291336_0008():
    """Model: DIN (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.4536459792, perimeter: 2.3876104167
            with Locations((9, 1)):
                Circle(0.38)
        # OneSide extrude, distance=0.22
        extrude(amount=0.22)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((-9, 1)):
                Circle(0.2)
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0.22, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0541265877, perimeter: 0.8660254038
            with BuildLine():
                Line((9.1067768658, 1.0971186607), (8.9692812056, 1.1410308087))
                Line((8.9692812056, 1.1410308087), (8.8625043397, 1.043912148))
                Line((8.8625043397, 1.043912148), (8.8932231342, 0.9028813393))
                Line((8.8932231342, 0.9028813393), (9.0307187944, 0.8589691913))
                Line((9.0307187944, 0.8589691913), (9.1374956603, 0.956087852))
                Line((9.1374956603, 0.956087852), (9.1067768658, 1.0971186607))
            make_face()
        # OneSide extrude, distance=-0.3
        extrude(amount=-0.3, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical coupling or connector with two rounded end flanges and a central bore, featuring a large circular hole through one flange and longitudinal slots or grooves along the cylindrical body.
def model_31962_e5291336_0009():
    """Model: tubo"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.7671458676, perimeter: 4.7123889804
            with Locations((46, 1)):
                Circle(0.75)
        # OneSide extrude, distance=0.8
        extrude(amount=0.8)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.8, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.1309733553, perimeter: 3.7699111843
            with Locations((46, 1)):
                Circle(0.6)
        # OneSide extrude, distance=0.8
        extrude(amount=0.8, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            with Locations((-46, 1)):
                Circle(0.3)
        # OneSide extrude, distance=-3
        extrude(amount=-3, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical connector or coupling with a rounded rectangular profile, featuring two large circular openings or ports on opposite ends and a central rectangular slot or channel running through its length.
def model_31962_e5291336_0010():
    """Model: Tapón"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.3273228961, perimeter: 4.0840704497
            with Locations((5.6705302942, 1.4480542631)):
                Circle(0.65)
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(1.5, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            with Locations((5.6705302942, 1.4480542631)):
                Circle(0.4)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(1.8, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((5.6705302942, 1.4480542631)):
                Circle(0.2)
        # OneSide extrude, distance=-3.2
        extrude(amount=-3.2, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a shoulder bolt or step bolt featuring a large hexagonal or cylindrical head with internal geometry on the left, a reduced-diameter shaft in the middle, and a cylindrical extension on the right, designed for pivot or hinge applications.
def model_31962_e5291336_0018():
    """Model: ten ajuste"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.5674501731, perimeter: 2.6703537556
            with Locations((3.8000000566, 0.400000006)):
                Circle(0.425)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.5, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((3.8000000566, 0.400000006)):
                Circle(0.25)
        # OneSide extrude, distance=1.6
        extrude(amount=1.6, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.1385640646, perimeter: 1.3856406461
            with BuildLine():
                Line((-3.6360750072, 0.562671182), (-3.8589149028, 0.6232988511))
                Line((-3.8589149028, 0.6232988511), (-4.0228399522, 0.460627675))
                Line((-4.0228399522, 0.460627675), (-3.963925106, 0.2373288299))
                Line((-3.963925106, 0.2373288299), (-3.7410852104, 0.1767011608))
                Line((-3.7410852104, 0.1767011608), (-3.577160161, 0.3393723369))
                Line((-3.577160161, 0.3393723369), (-3.6360750072, 0.562671182))
            make_face()
        # OneSide extrude, distance=-0.3
        extrude(amount=-0.3, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a shaft coupler or connector with a large flanged end featuring a central hexagonal or polygonal hole, connected to a cylindrical shaft portion, designed to join two rotating components.
def model_31962_e5291336_0019():
    """Model: DIN 3_1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.3848451001, perimeter: 2.1991148575
            with Locations((17, -4)):
                Circle(0.35)
        # OneSide extrude, distance=0.4
        extrude(amount=0.4)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.4, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((17, -4)):
                Circle(0.2)
        # OneSide extrude, distance=0.8
        extrude(amount=0.8, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.0779422863, perimeter: 1.0392304845
            with BuildLine():
                Line((-16.9419957282, -3.8367961261), (-17.1123365649, -3.8681648902))
                Line((-17.1123365649, -3.8681648902), (-17.1703408367, -4.0313687641))
                Line((-17.1703408367, -4.0313687641), (-17.0580042718, -4.1632038739))
                Line((-17.0580042718, -4.1632038739), (-16.8876634351, -4.1318351098))
                Line((-16.8876634351, -4.1318351098), (-16.8296591633, -3.9686312359))
                Line((-16.8296591633, -3.9686312359), (-16.9419957282, -3.8367961261))
            make_face()
        # OneSide extrude, distance=-0.3
        extrude(amount=-0.3, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a complex geometric polyhedron or stellated solid featuring multiple intersecting triangular faces, internal voids, and a central aperture, with an overall faceted, angular shape resembling a three-dimensional star or geometric lattice structure.
def model_31962_e5291336_0020():
    """Model: L"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 8 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.5792080159, perimeter: 11.3147503476
            with BuildLine():
                Line((5.9457673475, -33.3371637864), (6.1934673475, -33.3371637864))
                CenterArc((6.1934673475, -33.1085637864), 0.2286, -90, 90)
                Line((6.4220673475, -33.1085637864), (6.4220673475, -30.4860637864))
                CenterArc((6.9046673475, -30.4860637864), 0.4826, 90, 90)
                Line((7.9457673475, -30.0034637864), (6.9046673475, -30.0034637864))
                Line((7.9457673475, -29.5271637864), (7.9457673475, -30.0034637864))
                Line((5.9457673475, -29.5271637864), (7.9457673475, -29.5271637864))
                Line((5.9457673475, -33.3371637864), (5.9457673475, -29.5271637864))
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 30.0034637864), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            with Locations((7.3457673475, 1)):
                Circle(0.3)
        # OneSide extrude, distance=-2.1
        extrude(amount=-2.1, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(6.4220673475, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            with Locations((-32.3371637864, 1)):
                Circle(0.3)
        # OneSide extrude, distance=-2
        extrude(amount=-2, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a plastic or composite bracket/enclosure with a curved, ergonomic shape featuring multiple ventilation holes and slots, designed for mounting or housing components with an organic, wave-like form that includes flanged edges and internal structural ribs.
def model_31962_e5291336_0039():
    """Model: L2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 11 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.0859676459, perimeter: 9.2447503476
            with BuildLine():
                Line((-15.9811725346, -6.0161259186), (-15.980740975, -6.2637255425))
                CenterArc((-15.7521413222, -6.2633270993), 0.2286, -179.9001350619, 90)
                Line((-13.764245898, -6.488462597), (-15.751742879, -6.491926752))
                CenterArc((-13.7634047401, -6.9710618639), 0.4826, 0.0998649381, 90)
                Line((-13.2796878801, -7.6114197321), (-13.2808054732, -6.9702207061))
                Line((-12.8033886036, -7.610589555), (-13.2796878801, -7.6114197321))
                Line((-12.8061773574, -6.0105919854), (-12.8033886036, -7.610589555))
                Line((-15.9811725346, -6.0161259186), (-12.8061773574, -6.0105919854))
            make_face()
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.0112673705, 0, 6.4644522391), x_dir=(0.999998481, 0, -0.0017429711), z_dir=(0.0017429711, 0, 0.999998481))):
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            with Locations((-14.9916341932, 0.75)):
                Circle(0.4)
        # OneSide extrude, distance=-4
        extrude(amount=-4, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-13.2929140016, 0, 0.0231692), x_dir=(0.0017429711, 0, 0.999998481), z_dir=(-0.999998481, 0, 0.0017429711))):
            # Profile area: 0.1186811408, perimeter: 1.3613392834
            with BuildLine():
                Line((6.9470620585, 0.9965817511), (6.9470620585, 0.5034182489))
                CenterArc((6.9882620585, 0.75), 0.25, -99.4856162627, 198.9712325255)
            make_face()
            # Profile area: 0.0776684001, perimeter: 1.195784048
            with BuildLine():
                CenterArc((6.9882620585, 0.75), 0.25, 99.4856162627, 161.0287674745)
                Line((6.9470620585, 0.9965817511), (6.9470620585, 0.5034182489))
            make_face()
        # Symmetric extrude, each_side=2.9
        extrude(amount=2.9, both=True, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical connector or adapter with a hollow central bore, featuring two opposing rectangular slots or cutouts on opposite sides of the barrel, and a mesh-textured flanged end that suggests a threaded or ribbed mounting surface.
def model_31962_e5291336_0040():
    """Model: taponico"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((6.6076214635, 5.1767684041)):
                Circle(0.5)
        # OneSide extrude, distance=0.15
        extrude(amount=0.15)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.5674501731, perimeter: 2.6703537556
            with Locations((-6.6076214635, 5.1767684041)):
                Circle(0.425)
        # OneSide extrude, distance=0.65
        extrude(amount=0.65, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -0.65), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((-6.6076214635, 5.1767684041)):
                Circle(0.2)
        # OneSide extrude, distance=-2.1
        extrude(amount=-2.1, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical electric motor or rotor component with a rounded dome-shaped top end, a uniform cylindrical body, and ventilation slots or cooling fins distributed across its surface for heat dissipation.
def model_31962_e5291336_0041():
    """Model: Tapón (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.9347424096, perimeter: 6.3051764558
            with BuildLine():
                CenterArc((4.5, 1), 0.65, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((4.5, 1), 0.3535, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.3925804866, perimeter: 2.2211060061
            with Locations((4.5, 1)):
                Circle(0.3535)
        # OneSide extrude, distance=1.4
        extrude(amount=1.4)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1.4), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.3925804866, perimeter: 2.2211060061
            with Locations((4.5, 1)):
                Circle(0.3535)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1.7), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((4.5, 1)):
                Circle(0.25)
        # OneSide extrude, distance=-3.5
        extrude(amount=-3.5, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a stepped shoulder bolt featuring a cylindrical shaft on the left transitioning to a larger diameter cylindrical head on the right, with what appears to be internal axial slots or grooves in the enlarged head section.
def model_31962_e5291336_0042():
    """Model: Component91"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.5674501731, perimeter: 2.6703537556
            with Locations((4, -4.5)):
                Circle(0.425)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((-4, -4.5)):
                Circle(0.25)
        # OneSide extrude, distance=1.2
        extrude(amount=1.2, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0.5, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0779422863, perimeter: 1.0392304845
            with BuildLine():
                Line((4.160980089, -4.4360827804), (4.0251361086, -4.3286285437))
                Line((4.0251361086, -4.3286285437), (3.8641560196, -4.3925457632))
                Line((3.8641560196, -4.3925457632), (3.839019911, -4.5639172196))
                Line((3.839019911, -4.5639172196), (3.9748638914, -4.6713714563))
                Line((3.9748638914, -4.6713714563), (4.1358439804, -4.6074542368))
                Line((4.1358439804, -4.6074542368), (4.160980089, -4.4360827804))
            make_face()
        # OneSide extrude, distance=-0.3
        extrude(amount=-0.3, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a dual-chamber cylindrical component featuring two coaxial rounded ends with central elongated slots or openings, radial fins or cooling ribs extending from the outer surfaces, and a mesh-like structural pattern typical of a heat exchanger or acoustic damping device.
def model_31962_e5291336_0045():
    """Model: Tope"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 2.8352873699, perimeter: 5.9690260418
            with Locations((16.8534140934, 1.608772341)):
                Circle(0.95)
        # OneSide extrude, distance=0.4
        extrude(amount=0.4)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.4, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.7671458676, perimeter: 4.7123889804
            with Locations((16.8534140934, 1.608772341)):
                Circle(0.75)
        # OneSide extrude, distance=0.7
        extrude(amount=0.7, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(1.1, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((16.8534140934, 1.608772341)):
                Circle(0.5)
        # OneSide extrude, distance=-2.1
        extrude(amount=-2.1, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a pipe fitting or connector with a cylindrical shaft and a rounded hexagonal (or octagonal) end cap, featuring what appears to be a small internal opening or port on the rounded end.
def model_31962_e5291336_0054():
    """Model: tornillillo"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.2375829444, perimeter: 1.7278759595
            with Locations((-22.241315822, -7.6088418125)):
                Circle(0.275)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((22.241315822, -7.6088418125)):
                Circle(0.15)
        # OneSide extrude, distance=2
        extrude(amount=2, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0.3, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0346410162, perimeter: 0.692820323
            with BuildLine():
                Line((-22.1519624491, -7.6819807767), (-22.1332989346, -7.5680290037))
                Line((-22.1332989346, -7.5680290037), (-22.2226523074, -7.4948900395))
                Line((-22.2226523074, -7.4948900395), (-22.3306691949, -7.5357028483))
                Line((-22.3306691949, -7.5357028483), (-22.3493327095, -7.6496546212))
                Line((-22.3493327095, -7.6496546212), (-22.2599793366, -7.7227935854))
                Line((-22.2599793366, -7.7227935854), (-22.1519624491, -7.6819807767))
            make_face()
        # OneSide extrude, distance=-0.3
        extrude(amount=-0.3, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a toroidal (donut-shaped) ring with a textured surface featuring a mesh or lattice pattern on its outer and inner surfaces, commonly used as a seal, gasket, or structural component.
def model_32219_e5edc7ce_0040():
    """Model: guma na kolo v2 (1)"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 7.0685834706, perimeter: 28.2743338823
            with BuildLine():
                CenterArc((0, 0), 2.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.6
        extrude(amount=0.6)

        # Sketch3 -> Extrude2 (NewBody)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 8.6393797974, perimeter: 34.5575191895
            with BuildLine():
                CenterArc((0, 0), 3, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 2.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)
    return part.part


# Description: This is a hollow cylindrical sleeve or tube with a slightly tapered top end and a flat circular cap or flange on the upper surface, featuring vertical ribbed or corrugated detailing along its curved sidewall.
def model_32219_e5edc7ce_0042():
    """Model: butelka v5"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 19.6349540849, perimeter: 15.7079632679
            Circle(2.5)
        # OneSide extrude, distance=10
        extrude(amount=10)

        # Sketch5 -> Extrude4 (Cut)
        # Sketch on YZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 17.3381253815, perimeter: 19.501695941
            with BuildLine():
                Line((3.5, -0.8393574139), (3.5, 1.5))
                Line((3.5, 1.5), (-3.9114905566, 1.5))
                Line((-3.9114905566, 1.5), (-3.9114905566, -0.8393574139))
                Line((-3.9114905566, -0.8393574139), (3.5, -0.8393574139))
            make_face()
        # Symmetric extrude, each_side=5.5
        extrude(amount=5.5, both=True, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a hammer head featuring a cylindrical striking face with a wide, flat striking surface on top, a tapered neck, and a rectangular handle socket below for attachment to a shaft.
def model_32219_e5edc7ce_0044():
    """Model: srodek od chamber v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 7.0685834706, perimeter: 9.4247779608
            Circle(1.5)
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            Circle(0.5)
        # OneSide extrude, distance=2
        extrude(amount=2, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -2, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            Circle(0.15)
        # OneSide extrude, distance=-3.4
        extrude(amount=-3.4, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a dual-chamber duct or manifold component with two symmetrical curved saddle-shaped sections connected by a central bridge, featuring mesh-textured top surfaces, vertical ribbing on the sides, and mounting holes on each chamber.
def model_32219_e5edc7ce_0049():
    """Model: otwieranie v6"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 19 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1400000104, perimeter: 1.8000000447
            with BuildLine():
                Line((0, -0.6), (-0.5000000075, -0.6))
                Line((-0.5000000075, -0.6), (-0.5000000075, -0.8000000119))
                Line((0.200000003, -0.8000000119), (-0.5000000075, -0.8000000119))
                Line((0.200000003, -0.6), (0.200000003, -0.8000000119))
                Line((0, -0.6), (0.200000003, -0.6))
            make_face()
            # Profile area: 0.2000000077, perimeter: 2.4000000536
            with BuildLine():
                Line((-0.5000000075, 0), (-0.5000000075, 0.2000000119))
                Line((-0.5000000075, 0.2000000119), (-0.7000000104, 0.2000000119))
                Line((-0.7000000104, 0.2000000119), (-0.7000000104, -0.8000000119))
                Line((-0.7000000104, -0.8000000119), (-0.5000000075, -0.8000000119))
                Line((-0.5000000075, -0.6), (-0.5000000075, -0.8000000119))
                Line((-0.5000000075, -0.6), (-0.5000000075, 0))
            make_face()
            # Profile area: 0.1400000104, perimeter: 1.8000000447
            with BuildLine():
                Line((0, 0), (0.200000003, 0))
                Line((0.200000003, 0), (0.200000003, 0.2000000119))
                Line((0.200000003, 0.2000000119), (-0.5000000075, 0.2000000119))
                Line((-0.5000000075, 0), (-0.5000000075, 0.2000000119))
                Line((0, 0), (-0.5000000075, 0))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -0.2000000119), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.0039269908, perimeter: 0.2570796327
            with BuildLine():
                Line((0, 0.2), (0, 0.3))
                CenterArc((0, 0.25), 0.05, 90, 180)
            make_face()
            # Profile area: 0.0039269908, perimeter: 0.2570796327
            with BuildLine():
                CenterArc((0, 0.25), 0.05, -90, 180)
                Line((0, 0.2), (0, 0.3))
            make_face()
        # OneSide extrude, distance=-1.15
        extrude(amount=-1.15, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude3 (Cut)
        # Sketch on XY construction plane
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.2880530498, perimeter: 4.0232017094
            with BuildLine():
                CenterArc((-0.3000000045, -0.5000000149), 0.6403124391, 108.2007600934, 20.4590477443)
                CenterArc((-0.3000000045, -0.5000000149), 0.6403124391, 128.6598078376, 339.5409522557)
            make_face()
            # Profile area: 1.2880530498, perimeter: 4.0232017094
            with BuildLine():
                CenterArc((-0.3000000045, 1.0000000149), 0.6403124391, -128.6598078376, 20.4590477443)
                CenterArc((-0.3000000045, 1.0000000149), 0.6403124391, -108.2007600934, 339.5409522557)
            make_face()
        # Symmetric extrude, each_side=2.3
        extrude(amount=2.3, both=True, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical mesh or perforated container with a curved, elongated oval shape, featuring a mesh side wall, solid base, and a small protruding tab or handle on the upper left edge.
def model_32220_1fd19c5e_0020():
    """Model: ZOOM v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.3455751685, perimeter: 6.9115038847
            with BuildLine():
                CenterArc((0, 0), 0.6, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.5000000075, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.4
        extrude(amount=0.4)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.4, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0209994466, perimeter: 0.6266037245
            with BuildLine():
                CenterArc((0, 0), 0.6, -99.5940683712, 19.5816281392)
                Line((-0.1000000015, -0.5916079781), (-0.1000000015, -0.7000000104))
                Line((-0.1000000015, -0.7000000104), (0.1040606095, -0.7000000104))
                Line((0.1040606095, -0.7000000104), (0.1040606095, -0.5909072597))
            make_face()
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.4, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0209994466, perimeter: 0.6266037245
            with BuildLine():
                Line((-0.1000000015, -0.7000000104), (0.1040606095, -0.7000000104))
                Line((0.1040606095, -0.7000000104), (0.1040606095, -0.5909072597))
                CenterArc((0, 0), 0.6, -99.5940683712, 19.5816281392)
                Line((-0.1000000015, -0.5916079781), (-0.1000000015, -0.7000000104))
            make_face()
        # OneSide extrude, distance=0.05
        extrude(amount=0.05, mode=Mode.ADD)
    return part.part


# Description: This is a housing or bracket component with a complex curved body, featuring multiple rectangular cutouts/windows on the main face, a angular flanged extension on the left side, and internal ribbing or structural reinforcement visible through the openings.
def model_32461_378772c5_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 12 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 92.878666057, perimeter: 44.1533904727
            with BuildLine():
                CenterArc((-8.4621346669, 11), 2.6584518026, -0.0000000001, 180)
                Line((-11.1205864695, 5.4717709795), (-11.1205864695, 11))
                CenterArc((-5.6488154899, 5.4717709795), 5.4717709795, -180, 90)
                Line((0, 0), (-5.6488154899, 0))
                Line((0, 0), (0, 5))
                Line((-4, 5), (0, 5))
                CenterArc((-4, 6.8036828643), 1.8036828643, -180, 90)
                Line((-5.8036828643, 11), (-5.8036828643, 6.8036828643))
            make_face()
        # Symmetric extrude, each_side=3
        extrude(amount=3, both=True)

        # Sketch3 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 11 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 5.8036828643), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 1.4842543339, perimeter: 4.8731995173
            with BuildLine():
                Line((0.634939945, 11), (0.634939945, 9.7822120165))
                Line((0.634939945, 9.7822120165), (1.8537517201, 9.7822120165))
                Line((1.8537517201, 9.7822120165), (1.8537517201, 11))
                Line((0.634939945, 11), (1.8537517201, 11))
            make_face()
            # Profile area: 5.0123417058, perimeter: 10.6625879098
            with BuildLine():
                Line((0.634939945, 11), (1.8537517201, 11))
                Line((1.8537517201, 11), (1.8537517201, 15.1124821798))
                Line((1.8537517201, 15.1124821798), (0.634939945, 15.1124821798))
                Line((0.634939945, 15.1124821798), (0.634939945, 11))
            make_face()
            # Profile area: 5.0123417058, perimeter: 10.6625879098
            with BuildLine():
                Line((-1.8537517201, 11), (-0.634939945, 11))
                Line((-0.634939945, 15.1124821798), (-0.634939945, 11))
                Line((-1.8537517201, 15.1124821798), (-0.634939945, 15.1124821798))
                Line((-1.8537517201, 11), (-1.8537517201, 15.1124821798))
            make_face()
            # Profile area: 1.4842543339, perimeter: 4.8731995173
            with BuildLine():
                Line((-1.8537517201, 9.7822120165), (-1.8537517201, 11))
                Line((-0.634939945, 9.7822120165), (-1.8537517201, 9.7822120165))
                Line((-0.634939945, 11), (-0.634939945, 9.7822120165))
                Line((-1.8537517201, 11), (-0.634939945, 11))
            make_face()
        # OneSide extrude, distance=-8.5
        extrude(amount=-8.5, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(3, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            with Locations((-8.587092769, 11)):
                Circle(1)
            # Profile area: 1.5707963268, perimeter: 5.1415926536
            with BuildLine():
                Line((-8.587092769, 8.0292369635), (-8.587092769, 6.0292369635))
                CenterArc((-8.587092769, 7.0292369635), 1, -90, 180.0000000001)
            make_face()
            # Profile area: 1.5707963268, perimeter: 5.1415926536
            with BuildLine():
                CenterArc((-8.587092769, 7.0292369635), 1, 90.0000000001, 179.9999999999)
                Line((-8.587092769, 8.0292369635), (-8.587092769, 6.0292369635))
            make_face()
            # Profile area: 1.4570196194, perimeter: 4.8093872436
            with BuildLine():
                CenterArc((-5.6488154899, 5.4717709795), 2.9382772791, -128.997580012, 38.997580012)
                Line((-5.6488154899, 2.5334937005), (-5.6389357778, 2.5334937005))
                CenterArc((-6.6249148402, 2.7003627766), 1, -9.605830149, 160.4058220108)
            make_face()
            # Profile area: 1.6845730342, perimeter: 5.4933530839
            with BuildLine():
                CenterArc((-6.6249148402, 2.7003627766), 1, 150.7999918618, 199.5941779892)
                Line((-5.6488154899, 2.5334937005), (-5.6389357778, 2.5334937005))
                CenterArc((-5.6488154899, 5.4717709795), 2.9382772791, -128.997580012, 38.997580012)
            make_face()
        # OneSide extrude, distance=-13.5
        extrude(amount=-13.5, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a hexagonal prism or truncated wedge-shaped connector block with a rectangular base body, featuring an angled pentagonal top surface and what appears to be mounting holes or slots on the front face.
def model_32666_4baa4ef5_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 62.5, perimeter: 35
            with BuildLine():
                Line((15, -2.5), (2.5, -2.5))
                Line((15, 2.5), (15, -2.5))
                Line((2.5, 2.5), (15, 2.5))
                Line((2.5, -2.5), (2.5, 2.5))
            make_face()
        # Symmetric extrude, each_side=2
        extrude(amount=2, both=True)

        # Sketch3 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 6.6186449516, perimeter: 16.8795863564
            with BuildLine():
                CenterArc((-3.9721856713, 2.9209731379), 2.4187328024, -169.9767970309, 117.4694651617)
                Line((-6.2971297554, -2.5), (-6.3540022021, 2.5))
                CenterArc((-3.955598427, -2.8701993655), 2.3706152223, 52.119459925, 118.8963612973)
                Line((-2.5, -0.9990901354), (-2.5, 1.0018749855))
            make_face()
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 2.5), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1.9500000581, perimeter: 13.6000002027
            with BuildLine():
                Line((12.0000001788, 0.200000003), (5.500000082, 0.200000003))
                Line((12.0000001788, 0.5000000075), (12.0000001788, 0.200000003))
                Line((5.500000082, 0.5000000075), (12.0000001788, 0.5000000075))
                Line((5.500000082, 0.200000003), (5.500000082, 0.5000000075))
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical shaft or axle with a hexagonal socket head, featuring a long slender body and a larger polygonal head at the base, commonly used as a fastener or drive component.
def model_32871_04ff3d41_0010():
    """Model: CT009"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 10 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.3873796605, perimeter: 2.7436342898
            with BuildLine():
                CenterArc((0, 0), 0.6, 104.4775121859, 151.0449756281)
                Line((-0.15, -0.5809475019), (-0.15, 0.5809475019))
            make_face()
            # Profile area: 0.3873796605, perimeter: 2.7436342898
            with BuildLine():
                Line((0.15, 0.5809475019), (0.15, -0.5809475019))
                CenterArc((0, 0), 0.6, -75.5224878141, 151.0449756281)
            make_face()
            # Profile area: 0.3523912677, perimeter: 2.9270063139
            with BuildLine():
                Line((-0.15, -0.5809475019), (-0.15, 0.5809475019))
                CenterArc((0, 0), 0.6, -104.4775121859, 14.4775121859)
                CenterArc((0, 0), 0.6, -90, 14.4775121859)
                Line((0.15, 0.5809475019), (0.15, -0.5809475019))
                Line((0, 0.5809475019), (0.15, 0.5809475019))
                Line((-0.15, 0.5809475019), (0, 0.5809475019))
            make_face()
        # OneSide extrude, distance=0.8
        extrude(amount=0.8)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 10 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0019113833, perimeter: 0.3206606512
            with BuildLine():
                Line((0, 0.5809475019), (0, 0.6))
                Line((0, 0.5809475019), (0.15, 0.5809475019))
                CenterArc((0, 0), 0.6, 75.5224878141, 14.4775121859)
            make_face()
            # Profile area: 0.0019113833, perimeter: 0.3206606512
            with BuildLine():
                Line((-0.15, 0.5809475019), (0, 0.5809475019))
                Line((0, 0.5809475019), (0, 0.6))
                CenterArc((0, 0), 0.6, 90, 14.4775121859)
            make_face()
        # OneSide extrude, distance=0.8
        extrude(amount=0.8, mode=Mode.ADD)

        # Sketch1 -> Extrude3 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 10 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0019113833, perimeter: 0.3206606512
            with BuildLine():
                Line((0, 0.5809475019), (0, 0.6))
                Line((0, 0.5809475019), (0.15, 0.5809475019))
                CenterArc((0, 0), 0.6, 75.5224878141, 14.4775121859)
            make_face()
            # Profile area: 0.0019113833, perimeter: 0.3206606512
            with BuildLine():
                Line((-0.15, 0.5809475019), (0, 0.5809475019))
                Line((0, 0.5809475019), (0, 0.6))
                CenterArc((0, 0), 0.6, 90, 14.4775121859)
            make_face()
            # Profile area: 0.3523912677, perimeter: 2.9270063139
            with BuildLine():
                Line((-0.15, -0.5809475019), (-0.15, 0.5809475019))
                CenterArc((0, 0), 0.6, -104.4775121859, 14.4775121859)
                CenterArc((0, 0), 0.6, -90, 14.4775121859)
                Line((0.15, 0.5809475019), (0.15, -0.5809475019))
                Line((0, 0.5809475019), (0.15, 0.5809475019))
                Line((-0.15, 0.5809475019), (0, 0.5809475019))
            make_face()
        # OneSide extrude, distance=0.15
        extrude(amount=0.15, mode=Mode.SUBTRACT)

        # Sketch2 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.8, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.3848451001, perimeter: 2.1991148575
            Circle(0.35)
        # OneSide extrude, distance=3.4
        extrude(amount=3.4, mode=Mode.ADD)
    return part.part


# Description: This is a knurled thumb screw or manual adjustment knob featuring a cylindrical shaft with a flange base that has a slot or keyway for tool insertion, and knurled surfaces for improved grip.
def model_33147_d7173b68_0009():
    """Model: Sruba silnik v1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.096211275, perimeter: 1.0995574288
            Circle(0.175)
        # OneSide extrude, distance=0.15
        extrude(amount=0.15)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.15, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.020106193, perimeter: 0.5026548246
            Circle(0.08)
        # OneSide extrude, distance=0.45
        extrude(amount=0.45, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.0345178015, perimeter: 0.8736465843
            with BuildLine():
                Line((-0.05, 0.1677050983), (-0.05, -0.1677050983))
                CenterArc((0, 0), 0.175, -106.601549599, 33.203099198)
                Line((0.05, -0.1677050983), (0.05, 0.1677050983))
                CenterArc((0, 0), 0.175, 73.398450401, 33.203099198)
            make_face()
        # OneSide extrude, distance=-0.1
        extrude(amount=-0.1, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical fastener or standoff with a threaded cylindrical body, a hexagonal or polygonal base flange at the bottom, and a textured grip surface at the top, designed for assembly or mounting applications.
def model_33147_d7173b68_0010():
    """Model: Sruba enkoder v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0176714587, perimeter: 0.471238898
            Circle(0.075)
        # OneSide extrude, distance=0.05
        extrude(amount=0.05)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.05, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0078539816, perimeter: 0.3141592654
            Circle(0.05)
        # OneSide extrude, distance=0.2582
        extrude(amount=0.2582, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.0029910873, perimeter: 0.3374408518
            with BuildLine():
                Line((-0.01, 0.0743303437), (-0.01, -0.0743303437))
                CenterArc((0, 0), 0.075, -97.6622556608, 15.3245113215)
                Line((0.01, -0.0743303437), (0.01, 0.0743303437))
                CenterArc((0, 0), 0.075, 82.3377443392, 15.3245113215)
            make_face()
        # OneSide extrude, distance=-0.025
        extrude(amount=-0.025, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a threaded connector or coupling with an angled cylindrical stem, featuring a knurled hexagonal base with a central threaded hole and an offset vertical cylindrical outlet.
def model_33147_d7173b68_0017():
    """Model: Sruba slupek v0 v1 (2)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            Circle(0.3)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0706858368, perimeter: 0.9424778101
            Circle(0.1500000022)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.0597210532, perimeter: 1.3841536517
            with BuildLine():
                Line((-0.05, 0.2958039892), (-0.05, -0.2958039892))
                CenterArc((0, 0), 0.3, -99.5940682269, 19.1881364537)
                Line((0.05, -0.2958039892), (0.05, 0.2958039892))
                CenterArc((0, 0), 0.3, 80.4059317731, 19.1881364537)
            make_face()
        # OneSide extrude, distance=-0.1
        extrude(amount=-0.1, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a bolt or fastener with a long cylindrical shaft and a hexagonal head at the base, designed for threaded fastening applications.
def model_33147_d7173b68_0019():
    """Model: Sruba enkoder  v1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            Circle(0.2)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            Circle(0.1)
        # OneSide extrude, distance=1.5
        extrude(amount=1.5, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.0395793371, perimeter: 0.9767408734
            with BuildLine():
                Line((-0.05, 0.1936491673), (-0.05, -0.1936491673))
                CenterArc((0, 0), 0.2, -104.4775121859, 28.9550243719)
                Line((0.05, -0.1936491673), (0.05, 0.1936491673))
                CenterArc((0, 0), 0.2, 75.5224878141, 28.9550243719)
            make_face()
        # OneSide extrude, distance=-0.1
        extrude(amount=-0.1, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a mechanical arm or lever assembly featuring a horizontal blue rectangular bar extending from a vertical grip/handle on the left, with two dark spherical knobs or wheels attached at the right end.
def model_33625_c9ff9be8_0001():
    """Model: Door closer v6"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            Circle(0.3)
        # OneSide extrude, distance=1.2
        extrude(amount=1.2)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 8 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1.2), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 6.8690366906, perimeter: 16.0945914843
            with BuildLine():
                Line((-0.5590169944, 0.5), (-6.3590169944, 0.5))
                Line((-6.3590169944, 0.5), (-6.3590169944, -1.7))
                Line((-6.3590169944, -1.7), (-5.3590169944, -1.7))
                Line((-5.3590169944, -1.7), (-5.3590169944, -0.5))
                Line((-5.3590169944, -0.5), (-0.5590169944, -0.5))
                CenterArc((0, 0), 0.75, 138.1896851042, 83.6206297915)
            make_face()
            # Profile area: 1.4844025288, perimeter: 6.5973445725
            with BuildLine():
                CenterArc((0, 0), 0.75, 138.1896851042, 83.6206297915)
                CenterArc((0, 0), 0.75, -138.1896851042, 276.3793702085)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            Circle(0.3)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 1.4844025288, perimeter: 6.5973445725
            with BuildLine():
                CenterArc((0, 0), 0.75, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            Circle(0.3)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3, mode=Mode.ADD)
    return part.part


# Description: This is a cable tie or zip tie, featuring an elongated shaft with a ratcheting head at one end that has prongs or teeth for securing and locking cables or bundles together.
def model_33625_c9ff9be8_0004():
    """Model: Stick v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 5 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 55.4014642033, perimeter: 63.2082993873
            with BuildLine():
                CenterArc((0, 0), 2.1213203436, -143.8957952865, 287.791590573)
                Line((-1.7139136501, 1.25), (-21.7139136501, 1.25))
                Line((-21.7139136501, 1.25), (-21.7139136501, -1.25))
                Line((-21.7139136501, -1.25), (-1.7139136501, -1.25))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.6, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=10
        extrude(amount=10, both=True)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.25, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 107.4226184016, perimeter: 45.4278273002
            with BuildLine():
                Line((-8, 1.7139136501), (8, 1.7139136501))
                Line((-8, -5), (-8, 1.7139136501))
                Line((8, -5), (-8, -5))
                Line((8, 1.7139136501), (8, -5))
            make_face()
            # Profile area: 276.5773815984, perimeter: 66.5721726998
            with BuildLine():
                Line((8, 19), (8, 1.7139136501))
                Line((-8, 19), (8, 19))
                Line((-8, 1.7139136501), (-8, 19))
                Line((-8, 1.7139136501), (8, 1.7139136501))
            make_face()
        # Symmetric extrude, each_side=10
        extrude(amount=10, both=True, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 6 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 21.7139136501), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 10, perimeter: 13
            with BuildLine():
                Line((-2, -1.25), (-2, 1.25))
                Line((-2, -1.25), (2, -1.25))
                Line((2, 1.25), (2, -1.25))
                Line((-2, 1.25), (2, 1.25))
            make_face()
        # OneSide extrude, distance=83
        extrude(amount=83, mode=Mode.ADD)
    return part.part


# Description: This is a bracket or mounting clamp with a curved, angular design featuring two perpendicular flanges connected by a ribbed structure, two circular mounting holes, and a slot opening for component attachment or alignment.
def model_33655_f8991a06_0002():
    """Model: pieza 3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 8 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.0411035704, perimeter: 20.811035704
            with BuildLine():
                Line((-1.5516555295, -1.8667804089), (-3.3021344974, -0.64108184))
                Line((-3.3021344974, -0.64108184), (-3.4168497847, -0.8049122489))
                Line((-1.6663708168, -2.0306108177), (-3.4168497847, -0.8049122489))
                CenterArc((-1.4369402422, -1.70295), 0.4, -125, 35)
                Line((-0.2, -2.10295), (-1.4369402422, -2.10295))
                CenterArc((-0.2, -1.70295), 0.4, -90, 90)
                Line((0.2, -1.70295), (0.2, 1.70295))
                CenterArc((-0.2, 1.70295), 0.4, 0, 90)
                Line((-0.2, 2.10295), (-2.5, 2.10295))
                Line((-2.5, 2.10295), (-2.5, 1.90295))
                Line((-0.2, 1.90295), (-2.5, 1.90295))
                CenterArc((-0.2, 1.70295), 0.2, 0, 90)
                Line((0, 1.70295), (0, -1.70295))
                CenterArc((-0.2, -1.70295), 0.2, -90, 90)
                Line((-0.2, -1.90295), (-1.4369402422, -1.90295))
                CenterArc((-1.4369402422, -1.70295), 0.2, -125, 35)
            make_face()
        # OneSide extrude, distance=2.5
        extrude(amount=2.5)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 16 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -2.10295), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.0953564806, perimeter: 1.6447401404
            with BuildLine():
                CenterArc((2, 1.25), 0.3, 164.4268496519, 31.1463006962)
                CenterArc((1.9, 0.6), 0.6, 54.1482155269, 54.2112444212)
                CenterArc((2, 1.25), 0.3, -33.0654748732, 33.0654748732)
                CenterArc((2, 1.25), 0.3, 0, 33.0654748732)
                CenterArc((1.9, 1.9), 0.6, -108.359459948, 54.2112444212)
            make_face()
            # Profile area: 0.0936934291, perimeter: 1.255505374
            with BuildLine():
                CenterArc((1.9, 1.9), 0.6, -108.359459948, 54.2112444212)
                CenterArc((2, 1.25), 0.3, 33.0654748732, 131.3613747787)
            make_face()
            # Profile area: 0.0772566612, perimeter: 2.1424777961
            with BuildLine():
                CenterArc((1.9, 1.9), 0.6, 0, 90)
                Line((2.5, 1.9), (2.5, 2.5))
                Line((1.9, 2.5), (2.5, 2.5))
            make_face()
            # Profile area: 0.0772566612, perimeter: 2.1424777961
            with BuildLine():
                CenterArc((1.9, 0.6), 0.6, -90, 90)
                Line((1.9, 0), (2.5, 0))
                Line((2.5, 0.6), (2.5, 0))
            make_face()
            # Profile area: 0.0936934291, perimeter: 1.255505374
            with BuildLine():
                CenterArc((2, 1.25), 0.3, -164.4268496519, 131.3613747787)
                CenterArc((1.9, 0.6), 0.6, 54.1482155269, 54.2112444212)
            make_face()
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 14 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-1.5022942161, 0, 2.1454984903), x_dir=(0.8191520443, 0, 0.5735764364), z_dir=(-0.5735764364, 0, 0.8191520443))):
            # Profile area: 0.0953564806, perimeter: 1.6447401404
            with BuildLine():
                CenterArc((-1.7372407869, 1.9), 0.6, -125.8517844731, 54.2112444212)
                CenterArc((-1.8372407869, 1.25), 0.3, 146.9345251268, 33.0654748732)
                CenterArc((-1.8372407869, 1.25), 0.3, 180, 33.0654748732)
                CenterArc((-1.7372407869, 0.6), 0.6, 71.640540052, 54.2112444212)
                CenterArc((-1.8372407869, 1.25), 0.3, -15.5731503481, 31.1463006962)
            make_face()
            # Profile area: 0.0772566612, perimeter: 2.1424777961
            with BuildLine():
                Line((-2.3372407869, 2.5), (-2.3372407869, 1.9))
                CenterArc((-1.7372407869, 1.9), 0.6, 171.3881787376, 8.6118212624)
                CenterArc((-1.7372407869, 1.9), 0.6, 90, 81.3881787376)
                Line((-2.3372407869, 2.5), (-1.7372407869, 2.5))
            make_face()
            # Profile area: 0.0936934291, perimeter: 1.255505374
            with BuildLine():
                CenterArc((-1.8372407869, 1.25), 0.3, 15.5731503481, 131.3613747787)
                CenterArc((-1.7372407869, 1.9), 0.6, -125.8517844731, 54.2112444212)
            make_face()
            # Profile area: 0.0772566612, perimeter: 2.1424777961
            with BuildLine():
                CenterArc((-1.7372407869, 0.6), 0.6, -180, 90)
                Line((-2.3372407869, 0.6), (-2.3372407869, 0))
                Line((-1.7372407869, 0), (-2.3372407869, 0))
            make_face()
            # Profile area: 0.0936934291, perimeter: 1.255505374
            with BuildLine():
                CenterArc((-1.7372407869, 0.6), 0.6, 71.640540052, 54.2112444212)
                CenterArc((-1.8372407869, 1.25), 0.3, -146.9345251268, 131.3613747787)
            make_face()
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a complex geometric component featuring an angular, faceted cubic structure with internal mesh-like cutouts, curved surface transitions, and interconnected hollow sections that create a lightweight, lattice-patterned design.
def model_33655_f8991a06_0004():
    """Model: pieza 4"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.64, perimeter: 3.2
            with BuildLine():
                Line((0.4, -0.4), (0.4, 0.4))
                Line((0.4, 0.4), (-0.4, 0.4))
                Line((-0.4, 0.4), (-0.4, -0.4))
                Line((-0.4, -0.4), (0.4, -0.4))
            make_face()
        # OneSide extrude, distance=0.8
        extrude(amount=0.8)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.8, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            Circle(0.2)
        # OneSide extrude, distance=-0.8
        extrude(amount=-0.8, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-0.4, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.0628318531, perimeter: 1.0283185307
            with BuildLine():
                Line((0, 0.2), (0, 0.6))
                CenterArc((0, 0.4), 0.2, -90, 180)
            make_face()
            # Profile area: 0.0628318531, perimeter: 1.0283185307
            with BuildLine():
                CenterArc((0, 0.4), 0.2, 90, 180)
                Line((0, 0.2), (0, 0.6))
            make_face()
        # OneSide extrude, distance=-0.8
        extrude(amount=-0.8, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a curved structural bracket or clamp with an elongated oval/loop shape, featuring mesh or perforated surfaces on the outer edges and a solid central band with a rectangular mounting flange on one end.
def model_34063_0ca1585e_0004():
    """Model: Outer Swashplate"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 7.3827427359, perimeter: 29.5309709437
            with BuildLine():
                CenterArc((0, 0), 2.6, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 2.1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.7
        extrude(amount=0.7)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 7.3827427359, perimeter: 29.5309709437
            with BuildLine():
                CenterArc((0, 0), 2.6, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 2.1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 3.6756634047, perimeter: 24.504422698
            with BuildLine():
                CenterArc((0, 0), 2.1, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.8, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2, mode=Mode.ADD)

        # Sketch7 -> Extrude4 (Join)
        # Sketch on XZ construction plane
        # Sketch has 14 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))) as sk:
            # Profile area: 0.09, perimeter: 1.2
            with BuildLine():
                Line((0.3, -3.45), (0, -3.45))
                Line((0, -3.45), (0, -3.75))
                Line((0, -3.75), (0.3, -3.75))
                Line((0.3, -3.75), (0.3, -3.45))
            make_face()
            # Profile area: 0.09, perimeter: 1.2
            with BuildLine():
                Line((0, -3.45), (0, -3.75))
                Line((0, -3.45), (-0.3, -3.45))
                Line((-0.3, -3.45), (-0.3, -3.75))
                Line((-0.3, -3.75), (0, -3.75))
            make_face()
            # Profile area: 0.7689465433, perimeter: 5.3283256686
            with BuildLine():
                CenterArc((0, 0), 2.6, -112.619864948, 45.2397298961)
                CenterArc((-1.4375, -3.45), 1.1375, 0, 67.380135052)
                Line((0, -3.45), (-0.3, -3.45))
                Line((0.3, -3.45), (0, -3.45))
                CenterArc((1.4375, -3.45), 1.1375, 112.619864948, 67.380135052)
            make_face()
        # TwoSides extrude, along=0.3, against=-0.2
        extrude(amount=0.3, mode=Mode.ADD)
        extrude(sk.sketch, amount=-0.2, mode=Mode.ADD)

        # Sketch7 -> Extrude5 (Join)
        # Sketch on XZ construction plane
        # Sketch has 14 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.09, perimeter: 1.2
            with BuildLine():
                Line((0.3, -3.45), (0, -3.45))
                Line((0, -3.45), (0, -3.75))
                Line((0, -3.75), (0.3, -3.75))
                Line((0.3, -3.75), (0.3, -3.45))
            make_face()
            # Profile area: 0.09, perimeter: 1.2
            with BuildLine():
                Line((0, -3.45), (0, -3.75))
                Line((0, -3.45), (-0.3, -3.45))
                Line((-0.3, -3.45), (-0.3, -3.75))
                Line((-0.3, -3.75), (0, -3.75))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)
    return part.part


# Description: This is a hydraulic cylinder or actuator with an elongated cylindrical barrel, angled end caps with mounting flanges, a central rod extending through both ends, and a lighter-colored central band indicating the piston rod seal area.
def model_34063_0ca1585e_0012():
    """Model: Lever Arm"""
    with BuildPart() as part:
        # Sketch1 -> Extrude3 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 17 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 2.7945218719, perimeter: 10.4889607203
            with BuildLine():
                Line((-1.4005153389, -2.5561666365), (0.2505153389, -0.6692744332))
                CenterArc((0.1, -0.5375735116), 0.2, -41.1859251657, 41.1859251657)
                Line((0.3, -0.5375735116), (0.3, 0.5))
                Line((0.3, 0.5), (-0.3, 0.5))
                Line((-0.3, 0.5), (-0.3, -0.3121324419))
                CenterArc((-0.5, -0.3121324419), 0.2, -41.1859251657, 41.1859251657)
                Line((-2.0005153389, -2.3307255668), (-0.3494846611, -0.4438333635))
                CenterArc((-1.85, -2.4624264884), 0.2, 138.8140748343, 41.1859251657)
                Line((-2.05, -2.4624264884), (-2.05, -3.5))
                Line((-2.05, -3.5), (-1.45, -3.5))
                Line((-1.45, -3.5), (-1.45, -2.6878675581))
                CenterArc((-1.25, -2.6878675581), 0.2, 138.8140748343, 41.1859251657)
            make_face()
        # Symmetric extrude, each_side=0.3
        extrude(amount=0.3, both=True)

        # Sketch3 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.0000000909, 0.5, 0.0000004325), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            Circle(0.1)
        # OneSide extrude, distance=0.4
        extrude(amount=0.4, mode=Mode.ADD)

        # Sketch4 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.0000000909, -3.5, 0.0000004325), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            with Locations((-1.7500000261, 0)):
                Circle(0.1)
        # OneSide extrude, distance=0.4
        extrude(amount=0.4, mode=Mode.ADD)
    return part.part


# Description: This is a flat, trapezoidal plate or base with a beveled or angled edge along one side, featuring internal triangulated structural ribs or support webbing across its upper surface.
def model_34231_e27353cb_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 54.6354020822, perimeter: 63.8761041673
            with BuildLine():
                Line((5, -5), (5, 5))
                Line((5, 5), (-5, 5))
                Line((-5, 5), (-5, -5))
                Line((-5, -5), (5, -5))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 3.8, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 17.0902640355, perimeter: 42.7256600888
            with BuildLine():
                CenterArc((0, 0), 3.8, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 28.2743338823, perimeter: 18.8495559215
            Circle(3)
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)
    return part.part


# Description: This is a long, narrow rectangular bar or channel with a hexagonal cross-section, featuring beveled or chamfered edges at both ends and a slightly curved or recessed top surface along its length.
def model_34317_e9c65aa6_0020():
    """Model: Beam v9"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 40.96, perimeter: 25.6
            with BuildLine():
                Line((2.9, -3.9), (-3.5, -3.9))
                Line((2.9, 2.5), (2.9, -3.9))
                Line((-3.5, 2.5), (2.9, 2.5))
                Line((-3.5, -3.9), (-3.5, 2.5))
            make_face()
        # OneSide extrude, distance=84.46
        extrude(amount=84.46)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(84.46, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 12.8, perimeter: 16.8
            with BuildLine():
                Line((-3.5, -1.9), (-3.5, -3.9))
                Line((-3.5, -3.9), (2.9, -3.9))
                Line((2.9, -3.9), (2.9, -1.9))
                Line((2.9, -1.9), (-3.5, -1.9))
            make_face()
        # OneSide extrude, distance=-92.5
        extrude(amount=-92.5, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(84.46, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 34.5218672282, perimeter: 23.5880835088
            with BuildLine():
                Line((2.9, -2.8940417544), (-3.5, -2.8940417544))
                Line((2.9, -2.8940417544), (2.9, 2.5))
                Line((2.9, 2.5), (-3.5, 2.5))
                Line((-3.5, 2.5), (-3.5, -2.8940417544))
            make_face()
            # Profile area: 12.5774460019, perimeter: 38.4341919182
            with BuildLine():
                Line((-3.5, 2.5), (-3.5, -2.8940417544))
                Line((2.9, 2.5), (-3.5, 2.5))
                Line((2.9, -2.8940417544), (2.9, 2.5))
                Line((3.7547093357, -2.8940417544), (2.9, -2.8940417544))
                Line((3.7547093357, 3.1990150332), (3.7547093357, -2.8940417544))
                Line((-3.9752880813, 3.1990150332), (3.7547093357, 3.1990150332))
                Line((-3.9752880813, -2.8940417544), (-3.9752880813, 3.1990150332))
                Line((-3.5, -2.8940417544), (-3.9752880813, -2.8940417544))
            make_face()
        # OneSide extrude, distance=-1.3504
        extrude(amount=-1.3504, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical sleeve or connector with flanged ends at top and bottom, featuring a hollow central bore and vertical ribbing along the shaft, designed for structural support or assembly coupling.
def model_34330_5eff1ee1_0000():
    """Model: Component7"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0004908739, perimeter: 0.0785398163
            Circle(0.0125)
        # OneSide extrude, distance=0.075
        extrude(amount=0.075)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.075, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0004712389, perimeter: 0.1884955592
            with BuildLine():
                CenterArc((0, 0), 0.0175, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.0125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0004908739, perimeter: 0.0785398163
            Circle(0.0125)
        # OneSide extrude, distance=0.01
        extrude(amount=0.01, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0009621128, perimeter: 0.1099557429
            Circle(0.0175)
        # OneSide extrude, distance=-0.01
        extrude(amount=-0.01, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical standoff or spacer with enlarged circular flanges at both ends and a hollow tubular body, designed to maintain separation between two surfaces while allowing for fastening or alignment.
def model_34330_5eff1ee1_0009():
    """Model: Component11"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0004908739, perimeter: 0.0785398163
            Circle(0.0125)
        # OneSide extrude, distance=0.05
        extrude(amount=0.05)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.05, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0004712389, perimeter: 0.1884955592
            with BuildLine():
                CenterArc((0, 0), 0.0175, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.0125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0004908739, perimeter: 0.0785398163
            Circle(0.0125)
        # OneSide extrude, distance=0.01
        extrude(amount=0.01, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0009621128, perimeter: 0.1099557429
            Circle(0.0175)
        # OneSide extrude, distance=-0.01
        extrude(amount=-0.01, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical socket head cap screw (or Allen bolt) featuring a long shaft with a hexagonal socket in the recessed head at the top.
def model_34570_2041f80b_0002():
    """Model: Pieza 9"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1021017612, perimeter: 4.0840704497
            with BuildLine():
                CenterArc((0, 0), 0.35, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            Circle(0.3)
        # OneSide extrude, distance=3.4
        extrude(amount=3.4)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 3.4, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.7461282552, perimeter: 5.9690260418
            with BuildLine():
                CenterArc((0, 0), 0.6, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.35, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.3848451001, perimeter: 2.1991148575
            Circle(0.35)
        # OneSide extrude, distance=0.8
        extrude(amount=0.8, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 10 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 4.2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0897650726, perimeter: 1.4909814874
            with BuildLine():
                Line((0, -0.075), (0, 0.075))
                Line((0, -0.075), (0.595294045, -0.075))
                CenterArc((0, 0), 0.6, -7.1807557815, 14.3615115629)
                Line((0.595294045, 0.075), (0, 0.075))
            make_face()
            # Profile area: 0.0897650726, perimeter: 1.4909814874
            with BuildLine():
                Line((0, -0.075), (0, 0.075))
                Line((0, 0.075), (-0.595294045, 0.075))
                CenterArc((0, 0), 0.6, 172.8192442185, 14.3615115629)
                Line((-0.595294045, -0.075), (0, -0.075))
            make_face()
        # OneSide extrude, distance=-0.15
        extrude(amount=-0.15, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical connector or manifold block with a elongated barrel shape featuring rounded ends, central control interfaces (buttons/indicators), and symmetrical ports or attachment points on both sides.
def model_34678_f709cdcc_0004():
    """Model: Pasador de la polea"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0593957361, perimeter: 0.8639379797
            with Locations((-6.6190805009, 0.8729407581)):
                Circle(0.1375)
        # OneSide extrude, distance=0.6
        extrude(amount=0.6)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.6, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0490873852, perimeter: 0.7853981634
            with Locations((-6.6190805009, 0.8729407581)):
                Circle(0.125)
        # OneSide extrude, distance=0.375
        extrude(amount=0.375, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.0490873852, perimeter: 0.7853981634
            with Locations((6.6190805009, 0.8729407581)):
                Circle(0.125)
        # OneSide extrude, distance=0.375
        extrude(amount=0.375, mode=Mode.ADD)
    return part.part


# Description: This is a universal joint (U-joint) or coupling assembly featuring a central cubic hub with cylindrical shafts extending from opposite ends and cross-shaped internal geometry for rotational power transmission.
def model_34678_f709cdcc_0006():
    """Model: Muñon de gancho"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2396146317, perimeter: 3.0306767333
            with BuildLine():
                Line((2.679377949, -4.53107717), (2.506172949, -4.2310773099))
                Line((2.506172949, -4.2310773099), (2.159762949, -4.2310773099))
                Line((2.159762949, -4.2310773099), (1.986557949, -4.53107717))
                Line((1.986557949, -4.53107717), (2.159762949, -4.8310770301))
                Line((2.159762949, -4.8310770301), (2.506172949, -4.8310770301))
                Line((2.506172949, -4.8310770301), (2.679377949, -4.53107717))
            make_face()
            with BuildLine():
                CenterArc((2.332967949, -4.53107717), 0.15155, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.425
        extrude(amount=0.425)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 4.8310770301), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0490873852, perimeter: 0.7853981634
            with Locations((2.332967949, 0.2125)):
                Circle(0.125)
        # OneSide extrude, distance=0.375
        extrude(amount=0.375, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 4.2310773099), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.0490873852, perimeter: 0.7853981634
            with Locations((-2.332967949, 0.2125)):
                Circle(0.125)
        # OneSide extrude, distance=0.375
        extrude(amount=0.375, mode=Mode.ADD)
    return part.part


# Description: This is a hexagonal or trapezoidal prismatic component with a dark blue finish, featuring an open top cavity with internal geometric webbing or structural ribs visible through the aperture.
def model_34708_7559c801_0001():
    """Model: Cuerpo"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 43110.6378796283, perimeter: 928.3377876035
            with BuildLine():
                Line((100, 50), (136.7594172365, 180))
                Line((100, 50), (450, 50))
                Line((450, 50), (450, 180))
                Line((450, 180), (136.7594172365, 180))
            make_face()
        # OneSide extrude, distance=-270
        extrude(amount=-270)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 180, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3915.0429834587, perimeter: 251.47102546
            with BuildLine():
                Line((-80, -258.9760954935), (-136.7594172365, -258.9760954935))
                Line((-80, -190), (-80, -258.9760954935))
                Line((-136.7594172365, -190), (-80, -190))
                Line((-136.7594172365, -258.9760954935), (-136.7594172365, -190))
            make_face()
            # Profile area: 1379.5219098697, perimeter: 177.952190987
            with BuildLine():
                Line((-450, -190), (-450, -258.9760954935))
                Line((-470, -190), (-450, -190))
                Line((-470, -258.9760954935), (-470, -190))
                Line((-450, -258.9760954935), (-470, -258.9760954935))
            make_face()
            # Profile area: 21606.1123491315, perimeter: 764.433356514
            with BuildLine():
                Line((-136.7594172365, -258.9760954935), (-450, -258.9760954935))
                Line((-136.7594172365, -258.9760954935), (-136.7594172365, -190))
                Line((-450, -190), (-136.7594172365, -190))
                Line((-450, -190), (-450, -258.9760954935))
            make_face()
        # OneSide extrude, distance=-75
        extrude(amount=-75, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -270), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 78.5398163397, perimeter: 31.4159265359
            with Locations((-400, 150)):
                Circle(5)
        # OneSide extrude, distance=-90
        extrude(amount=-90, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a circular filter or strainer component with a flat, disc-like shape featuring a fine mesh or perforated surface across its top, a raised outer flange around the rim, and a solid base structure.
def model_34710_08cd9b5c_0004():
    """Model: Component2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 706.8583470577, perimeter: 94.2477796077
            Circle(15)
        # OneSide extrude, distance=4
        extrude(amount=4)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 4, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 19.6349540849, perimeter: 15.7079632679
            Circle(2.5)
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 4, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((0, -9)):
                Circle(0.5)
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a dark gray plastic or composite bracket with a rectangular profile featuring a large central slot or cutout, angled side flanges, and mounting holes, designed as a structural support or mounting component.
def model_34769_44655d03_0002():
    """Model: Lateral 1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 21 constraints, 28 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 9.7349297528, perimeter: 28.3649837503
            with BuildLine():
                Line((1.5, 0), (4.9518, 0))
                Line((4.9518, 0), (6.7693081293, 0.1762868385))
                CenterArc((6.75, 0.3753526471), 0.2, -84.46, 84.46)
                Line((6.95, 1.6177128117), (6.95, 0.3753526471))
                CenterArc((6.75, 1.6177128117), 0.2, 0, 90)
                Line((6.75, 1.8177128117), (6.0737971308, 1.8177128117))
                CenterArc((6.0737971308, 2.5177128117), 0.7, -153.0073987728, 63.0073987728)
                Line((5.45, 2.45), (5.4500515315, 2.2000000053))
                Line((1.5, 2.45), (5.45, 2.45))
                Line((1.5, 0), (1.5, 2.45))
            make_face()
            with BuildLine():
                CenterArc((3.65, 1.7876), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((2.35, 1.2876), (5.15, 1.2876))
                CenterArc((5.15, 0.9876), 0.3, -90, 180)
                Line((5.15, 0.6876), (2.35, 0.6876))
                CenterArc((2.35, 0.9876), 0.3, 90, 180)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((2.05, 0.35), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((2.05, 1.8), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((6.6, 0.5), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((6.6, 1.4677128117), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.25
        extrude(amount=0.25)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.25), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.2120575041, perimeter: 2.8274333882
            with BuildLine():
                CenterArc((6.6, 1.4677128117), 0.3, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((6.6, 1.4677128117), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.2120575041, perimeter: 2.8274333882
            with BuildLine():
                CenterArc((6.6, 0.5), 0.3, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((6.6, 0.5), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.2120575041, perimeter: 2.8274333882
            with BuildLine():
                CenterArc((2.05, 1.8), 0.3, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((2.05, 1.8), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.2120575041, perimeter: 2.8274333882
            with BuildLine():
                CenterArc((2.05, 0.35), 0.3, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((2.05, 0.35), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.05
        extrude(amount=-0.05, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2.45, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.97644028, perimeter: 12.0734511514
            with BuildLine():
                Line((-1.5, 0.25), (-5.45, 0.25))
                Line((-1.5, 0.25), (-1.5, 1.3))
                Line((-1.5, 1.3), (-5.45, 1.3))
                Line((-5.45, 0.25), (-5.45, 1.3))
            make_face()
            with BuildLine():
                CenterArc((-4.85, 0.8), 0.165, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-2.1, 0.8), 0.165, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.25
        extrude(amount=-0.25, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical connector or coupling featuring a smaller diameter shaft on the left end and a larger diameter chamber/flange on the right end, with internal mesh geometry visible suggesting hollow or complex internal features.
def model_34769_44655d03_0004():
    """Model: TOPE"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            with Locations((-5.5, -0.5)):
                Circle(0.4)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((5.5, -0.5)):
                Circle(0.25)
        # OneSide extrude, distance=0.9
        extrude(amount=0.9, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.5, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((-5.5, -0.5)):
                Circle(0.15)
        # OneSide extrude, distance=-2.8
        extrude(amount=-2.8, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a ring-shaped bearing or bushing with a toroidal overall form, featuring a large central hole, mesh-textured surfaces, and concentric cylindrical walls with radial slots or openings.
def model_34769_44655d03_0006():
    """Model: Topecillo1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            with Locations((-1.0197598346, 0.3147675817)):
                Circle(0.4)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.1), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            with Locations((-1.0197598346, 0.3147675817)):
                Circle(0.3)
        # OneSide extrude, distance=0.25
        extrude(amount=0.25, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.35), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((-1.0197598346, 0.3147675817)):
                Circle(0.25)
        # OneSide extrude, distance=-1.1
        extrude(amount=-1.1, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cubic or hexahedral structural component with multiple internal cutouts, apertures, and geometric features including rectangular slots, triangular voids, and small circular holes distributed across its faces, creating a latticed or skeletal framework structure.
def model_34769_44655d03_0007():
    """Model: Pieza delantera"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 3 constraints, 9 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.3360269637, perimeter: 6.611894611
            with BuildLine():
                Line((8.1000001207, 2.2000000328), (8.1000001207, 0.5093000328))
                Line((8.9700001207, 0.5936845519), (8.1000001207, 0.5093000328))
                Line((8.9700001207, 2.2000000328), (8.9700001207, 0.5936845519))
                Line((8.1000001207, 2.2000000328), (8.9700001207, 2.2000000328))
            make_face()
            with BuildLine():
                CenterArc((8.6200001207, 1.8500000328), 0.125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((8.6200001207, 0.9000000328), 0.125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.6
        extrude(amount=1.6)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(8.1000001207, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((0.8, 1.3876000328)):
                Circle(0.25)
        # OneSide extrude, distance=-3
        extrude(amount=-3, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2.2000000328, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0490873852, perimeter: 0.7853981634
            with Locations((-8.3100001207, 0.8000000119)):
                Circle(0.125)
        # OneSide extrude, distance=-0.8
        extrude(amount=-0.8, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a curved mounting bracket or deflector panel with a saddle-shaped profile featuring a central concave depression, symmetrical curved flanges on either side, and a trapezoidal overall footprint designed for structural support or flow direction.
def model_34782_b461066c_0001():
    """Model: Back wood v3"""
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
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 4907.7403805166, perimeter: 380.4653628052
            with BuildLine():
                Line((-58.9662414014, 32.250155868), (-58.9662414014, -27.749844132))
                _nurbs_edge([(-58.9662414014, -27.749844132), (-57.5171316775, -27.705000843), (-54.7600855246, -27.5391630855), (-51.048050613, -27.061949379), (-46.9471485801, -25.9679533698), (-43.2084590917, -23.8463682629), (-40.7590434048, -21.0060176805), (-39.3942339507, -17.523166091), (-38.751507254, -13.5335840702), (-38.3043137152, -9.2400109223), (-37.4896664907, -4.8853511707), (-35.8168351869, -0.7320009432), (-32.9736551163, 2.9606297658), (-28.961167985, 5.9588441388), (-24.031672161, 8.0696438111), (-18.5764804347, 9.1528954349), (-13.0282150255, 9.1362878242), (-7.7665818373, 8.0269337429), (-3.0003802036, 5.9324171769), (1.2431681668, 3.0469537503), (5.0522998623, -0.3865581578), (8.5873649436, -4.1075269603), (12.0308673797, -7.8696500239), (15.535853432, -11.4760915898), (19.1901220394, -14.802073287), (23.0370068344, -17.7751643718), (27.0861006075, -20.3631424261), (31.3274338268, -22.5594598618), (35.7444275543, -24.369598856), (40.3258663594, -25.7985545479), (45.0641585435, -26.8512023798), (48.9767962601, -27.3954143739), (51.9789900194, -27.6372101658), (54.0104953268, -27.7246005622), (55.0337585986, -27.749844132)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0333333333, 0.0666666667, 0.1, 0.1333333333, 0.1666666667, 0.2, 0.2333333333, 0.2666666667, 0.3, 0.3333333333, 0.3666666667, 0.4, 0.4333333333, 0.4666666667, 0.5, 0.5333333333, 0.5666666667, 0.6, 0.6333333333, 0.6666666667, 0.7, 0.7333333333, 0.7666666667, 0.8, 0.8333333333, 0.8666666667, 0.9, 0.9333333333, 0.9666666667, 1, 1, 1, 1, 1, 1], 5)
                Line((55.0337585986, 32.250155868), (55.0337585986, -27.749844132))
                Line((-58.9662414014, 32.250155868), (55.0337585986, 32.250155868))
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-58.9662414014, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 1.7671458676, perimeter: 4.7123889804
            with Locations((1, 27.250155868)):
                Circle(0.75)
            # Profile area: 1.7671458676, perimeter: 4.7123889804
            with Locations((1, -22.749844132)):
                Circle(0.75)
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(55.0337585986, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.7671458676, perimeter: 4.7123889804
            with Locations((-1, 27.250155868)):
                Circle(0.75)
            # Profile area: 1.7671458676, perimeter: 4.7123889804
            with Locations((-1, -22.749844132)):
                Circle(0.75)
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a bracket or support arm featuring a tapered, ribbed cylindrical shaft on one end that connects to a flat rectangular mounting plate with three drilled holes on the other end.
def model_35149_f50fea8a_0006():
    """Model: Component10"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 9 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0479185273, perimeter: 1.2825213638
            with BuildLine():
                CenterArc((0.0512601583, 0.2968361507), 0.0156, 111.2225170723, 150.9735368115)
                CenterArc((0.0512601583, 0.2968361507), 0.0156, 109.7753129365, 1.4472041358)
                CenterArc((0.0425263648, 0.3201970912), 0.0093435035, -68.2928948595, 105.5276014022)
                CenterArc((0.0256441732, 0.306228128), 0.03125, 38.8969343683, 1.4174128255)
                CenterArc((0.0256441732, 0.306228128), 0.03125, 40.3143471938, 99.3713056124)
                CenterArc((0.01, 0.3207), 0.01, 144.9264430814, 35.0735569186)
                Line((0, 0), (0, 0.3207))
                Line((0, 0), (0.25, 0))
                Line((0.25, 0), (0.25, 0.05))
                Line((0.0491419309, 0.2813806303), (0.25, 0.05))
            make_face()
            with BuildLine():
                CenterArc((0.03744872, 0.2074982022), 0.0125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0.16244872, 0.0824982022), 0.0125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0.03744872, 0.0824982022), 0.0125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.0125
        extrude(amount=0.0125)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.003125, perimeter: 0.525
            with BuildLine():
                Line((0, 0.0125), (0, 0))
                Line((0, 0), (0.25, 0))
                Line((0.25, 0), (0.25, 0.0125))
                Line((0.25, 0.0125), (0, 0.0125))
            make_face()
        # OneSide extrude, distance=0.1
        extrude(amount=0.1, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -0.0125), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.0004908739, perimeter: 0.0785398163
            with Locations((-0.03752128, 0.0625254013)):
                Circle(0.0125)
            # Profile area: 0.0004908739, perimeter: 0.0785398163
            with Locations((-0.125062913, 0.0502362803)):
                Circle(0.0125)
            # Profile area: 0.0004908739, perimeter: 0.0785398163
            with Locations((-0.21252128, 0.0625254013)):
                Circle(0.0125)
        # TwoSides extrude (symmetric), distance=0.1
        extrude(amount=0.1, both=True, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a reinforced rubber or elastomer belt with an elliptical/oval torus shape, featuring a hollow center and a mesh or fabric reinforcement layer visible on the outer surface.
def model_35166_562b126c_0001():
    """Model: Tail Cap Button Retainer"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.3435217333, perimeter: 9.3462381444
            with BuildLine():
                CenterArc((0, 0), 0.8875, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.6, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)

        # Sketch3 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.3, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0176714587, perimeter: 0.471238898
            with Locations((0, 0.7)):
                Circle(0.075)
            # Profile area: 0.0176714587, perimeter: 0.471238898
            with Locations((0, -0.7)):
                Circle(0.075)
        # OneSide extrude, distance=-0.075
        extrude(amount=-0.075, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.408407045, perimeter: 8.1681408993
            with BuildLine():
                CenterArc((0, 0), 0.7, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.6, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.15
        extrude(amount=-0.15, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical shaft or rod with hexagonal ends, featuring a long, slender body and threaded or knurled sections at both ends for fastening or assembly purposes.
def model_35962_dbbd6e18_0005():
    """Model: toothed bar v5"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.8352873699, perimeter: 5.9690260418
            Circle(0.95)
        # OneSide extrude, distance=19
        extrude(amount=19)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 19, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))) as sk:
            # Profile area: 1.1309733553, perimeter: 3.7699111843
            Circle(0.6)
        # TwoSides extrude, along=3, against=-20.1
        extrude(amount=3, mode=Mode.ADD)
        extrude(sk.sketch, amount=-20.1, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on XY construction plane
        # Sketch has 160 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY) as sk:
            # Profile area: 0.1625000024, perimeter: 1.7094810191
            with BuildLine():
                Line((-0.956457199, 3.7010345186), (-0.956457199, 3.2010345186))
                Line((-0.956457199, 3.2010345186), (-0.4564571916, 3.3760345186))
                Line((-0.4564571916, 3.5260345186), (-0.4564571916, 3.3760345186))
                Line((-0.4564571916, 3.5260345186), (-0.956457199, 3.7010345186))
            make_face()
            # Profile area: 0.1625000024, perimeter: 1.7094810191
            with BuildLine():
                Line((-0.956457199, 13.7010345186), (-0.4564571916, 13.8760345186))
                Line((-0.4564571916, 14.0260345186), (-0.4564571916, 13.8760345186))
                Line((-0.4564571916, 14.0260345186), (-0.956457199, 14.2010345186))
                Line((-0.956457199, 14.2010345186), (-0.956457199, 13.7010345186))
            make_face()
            # Profile area: 0.1625000024, perimeter: 1.7094810191
            with BuildLine():
                Line((-0.956457199, 8.8010345186), (-0.956457199, 9.3010345186))
                Line((-0.956457199, 8.8010345186), (-0.4564571916, 8.9760345186))
                Line((-0.4564571916, 9.1260345186), (-0.4564571916, 8.9760345186))
                Line((-0.4564571916, 9.1260345186), (-0.956457199, 9.3010345186))
            make_face()
            # Profile area: 0.1625000024, perimeter: 1.7094810191
            with BuildLine():
                Line((-0.4564571916, 13.3260345186), (-0.956457199, 13.5010345186))
                Line((-0.956457199, 13.0010345186), (-0.956457199, 13.5010345186))
                Line((-0.956457199, 13.0010345186), (-0.4564571916, 13.1760345186))
                Line((-0.4564571916, 13.3260345186), (-0.4564571916, 13.1760345186))
            make_face()
            # Profile area: 0.1625000024, perimeter: 1.7094810191
            with BuildLine():
                Line((-0.956457199, 12.8010345186), (-0.956457199, 12.3010345186))
                Line((-0.956457199, 12.3010345186), (-0.4564571916, 12.4760345186))
                Line((-0.4564571916, 12.4760345186), (-0.4564571916, 12.6260345186))
                Line((-0.4564571916, 12.6260345186), (-0.956457199, 12.8010345186))
            make_face()
            # Profile area: 0.1625000024, perimeter: 1.7094810191
            with BuildLine():
                Line((-0.956457199, 10.9010345186), (-0.956457199, 11.4010345186))
                Line((-0.956457199, 10.9010345186), (-0.4564571916, 11.0760345186))
                Line((-0.4564571916, 11.2260345186), (-0.4564571916, 11.0760345186))
                Line((-0.4564571916, 11.2260345186), (-0.956457199, 11.4010345186))
            make_face()
            # Profile area: 0.1625000024, perimeter: 1.7094810191
            with BuildLine():
                Line((-0.956457199, 10.7010345186), (-0.956457199, 10.2010345186))
                Line((-0.956457199, 10.2010345186), (-0.4564571916, 10.3760345186))
                Line((-0.4564571916, 10.5260345186), (-0.4564571916, 10.3760345186))
                Line((-0.4564571916, 10.5260345186), (-0.956457199, 10.7010345186))
            make_face()
            # Profile area: 0.1625000024, perimeter: 1.7094810191
            with BuildLine():
                Line((-0.956457199, 5.1010345186), (-0.956457199, 4.6010345186))
                Line((-0.956457199, 4.6010345186), (-0.4564571916, 4.7760345186))
                Line((-0.4564571916, 4.9260345186), (-0.4564571916, 4.7760345186))
                Line((-0.4564571916, 4.9260345186), (-0.956457199, 5.1010345186))
            make_face()
            # Profile area: 0.1625000024, perimeter: 1.7094810191
            with BuildLine():
                Line((-0.4564571916, 15.4260345186), (-0.4564571916, 15.2760345186))
                Line((-0.4564571916, 15.4260345186), (-0.956457199, 15.6010345186))
                Line((-0.956457199, 15.6010345186), (-0.956457199, 15.1010345186))
                Line((-0.956457199, 15.1010345186), (-0.4564571916, 15.2760345186))
            make_face()
            # Profile area: 0.1625000024, perimeter: 1.7094810191
            with BuildLine():
                Line((-0.956457199, 4.4010345186), (-0.956457199, 3.9010345186))
                Line((-0.956457199, 3.9010345186), (-0.4564571916, 4.0760345186))
                Line((-0.4564571916, 4.2260345186), (-0.4564571916, 4.0760345186))
                Line((-0.4564571916, 4.2260345186), (-0.956457199, 4.4010345186))
            make_face()
            # Profile area: 0.1625000024, perimeter: 1.7094810191
            with BuildLine():
                Line((-0.4564571916, 15.9760345186), (-0.4564571916, 16.1260345186))
                Line((-0.4564571916, 16.1260345186), (-0.956457199, 16.3010345186))
                Line((-0.956457199, 15.8010345186), (-0.956457199, 16.3010345186))
                Line((-0.956457199, 15.8010345186), (-0.4564571916, 15.9760345186))
            make_face()
            # Profile area: 0.1625000024, perimeter: 1.7094810191
            with BuildLine():
                Line((-0.956457199, 8.1010345186), (-0.4564571916, 8.2760345186))
                Line((-0.4564571916, 8.4260345186), (-0.4564571916, 8.2760345186))
                Line((-0.4564571916, 8.4260345186), (-0.956457199, 8.6010345186))
                Line((-0.956457199, 8.6010345186), (-0.956457199, 8.1010345186))
            make_face()
            # Profile area: 0.1625000024, perimeter: 1.7094810191
            with BuildLine():
                Line((-0.956457199, 5.3010345186), (-0.956457199, 5.8010345186))
                Line((-0.956457199, 5.3010345186), (-0.4564571916, 5.4760345186))
                Line((-0.4564571916, 5.6260345186), (-0.4564571916, 5.4760345186))
                Line((-0.4564571916, 5.6260345186), (-0.956457199, 5.8010345186))
            make_face()
            # Profile area: 0.1625000024, perimeter: 1.7094810191
            with BuildLine():
                Line((-0.956457199, 17.0010345186), (-0.956457199, 16.5010345186))
                Line((-0.956457199, 16.5010345186), (-0.4564571916, 16.6760345186))
                Line((-0.4564571916, 16.6760345186), (-0.4564571916, 16.8260345186))
                Line((-0.4564571916, 16.8260345186), (-0.956457199, 17.0010345186))
            make_face()
            # Profile area: 0.1625000024, perimeter: 1.7094810191
            with BuildLine():
                Line((-0.4564571916, 7.7260345186), (-0.4564571916, 7.5760345186))
                Line((-0.4564571916, 7.7260345186), (-0.956457199, 7.9010345186))
                Line((-0.956457199, 7.9010345186), (-0.956457199, 7.4010345186))
                Line((-0.956457199, 7.4010345186), (-0.4564571916, 7.5760345186))
            make_face()
            # Profile area: 0.1625000024, perimeter: 1.7094810191
            with BuildLine():
                Line((-0.4564571916, 6.3260345186), (-0.956457199, 6.5010345186))
                Line((-0.956457199, 6.0010345186), (-0.956457199, 6.5010345186))
                Line((-0.956457199, 6.0010345186), (-0.4564571916, 6.1760345186))
                Line((-0.4564571916, 6.3260345186), (-0.4564571916, 6.1760345186))
            make_face()
            # Profile area: 0.1625000024, perimeter: 1.7094810191
            with BuildLine():
                Line((-0.956457199, 9.5010345186), (-0.956457199, 10.0010345186))
                Line((-0.956457199, 9.5010345186), (-0.4564571916, 9.6760345186))
                Line((-0.4564571916, 9.8260345186), (-0.4564571916, 9.6760345186))
                Line((-0.4564571916, 9.8260345186), (-0.956457199, 10.0010345186))
            make_face()
            # Profile area: 0.1625000024, perimeter: 1.7094810191
            with BuildLine():
                Line((-0.956457199, 7.2010345186), (-0.956457199, 6.7010345186))
                Line((-0.956457199, 6.7010345186), (-0.4564571916, 6.8760345186))
                Line((-0.4564571916, 6.8760345186), (-0.4564571916, 7.0260345186))
                Line((-0.4564571916, 7.0260345186), (-0.956457199, 7.2010345186))
            make_face()
            # Profile area: 0.1625000024, perimeter: 1.7094810191
            with BuildLine():
                Line((-0.4564571916, 11.7760345186), (-0.4564571916, 11.9260345186))
                Line((-0.4564571916, 11.9260345186), (-0.956457199, 12.1010345186))
                Line((-0.956457199, 11.6010345186), (-0.956457199, 12.1010345186))
                Line((-0.956457199, 11.6010345186), (-0.4564571916, 11.7760345186))
            make_face()
            # Profile area: 0.1625000024, perimeter: 1.7094810191
            with BuildLine():
                Line((-0.956457199, 14.9010345186), (-0.956457199, 14.4010345186))
                Line((-0.956457199, 14.4010345186), (-0.4564571916, 14.5760345186))
                Line((-0.4564571916, 14.7260345186), (-0.4564571916, 14.5760345186))
                Line((-0.4564571916, 14.7260345186), (-0.956457199, 14.9010345186))
            make_face()
        # TwoSides extrude, along=2, against=-1
        extrude(amount=2, mode=Mode.SUBTRACT)
        extrude(sk.sketch, amount=-1, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a flapped disc or grinding wheel with a circular disk shape featuring a central hole and a textured radial flap surface designed for abrasive finishing and grinding applications.
def model_36088_1ea9c8a9_0004():
    """Model: Clutch Plate 2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.4948008429, perimeter: 6.5973445725
            with BuildLine():
                CenterArc((0, 0), 0.6, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.45, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.1, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 4.1783182293, perimeter: 11.9380520836
            with BuildLine():
                CenterArc((0, 0), 1.3, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.6, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.4948008429, perimeter: 6.5973445725
            with BuildLine():
                CenterArc((0, 0), 0.6, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.45, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.15
        extrude(amount=0.15, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.25, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 2.167698931, perimeter: 14.4513262065
            with BuildLine():
                CenterArc((0, 0), 1.3, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.02
        extrude(amount=0.02, mode=Mode.ADD)
    return part.part


# Description: This is a toroidal (donut-shaped) component with a large central oval hole and radial fins or ridges covering its outer surface, likely designed as a heat exchanger or cooling device.
def model_36088_1ea9c8a9_0012():
    """Model: Clutch Plate 1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 2.167698931, perimeter: 14.4513262065
            with BuildLine():
                CenterArc((0, 0), 1.3, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.02
        extrude(amount=0.02)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.02, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 2.167698931, perimeter: 14.4513262065
            with BuildLine():
                CenterArc((0, 0), 1.3, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 2.5054201412, perimeter: 9.1106186954
            with BuildLine():
                CenterArc((0, 0), 1, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.45, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.15
        extrude(amount=0.15, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.17, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.4948008429, perimeter: 6.5973445725
            with BuildLine():
                CenterArc((0, 0), 0.6, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.45, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.36
        extrude(amount=0.36, mode=Mode.ADD)
    return part.part


# Description: This is a helicopter tail boom or fuselage fairing with a streamlined, curved aerodynamic shape featuring black composite material with blue striping accents and tapered ends for reduced drag.
def model_36163_04339590_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch90 -> Extrude15 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 20 constraints, 9 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.408850691, perimeter: 8.3847171155
            with BuildLine():
                CenterArc((-0.397261822, 0.8000000015), 0.8, -106.699244234, 16.699244234)
                Line((0, 0.0000000015), (-0.397261822, 0.0000000015))
                Line((0, 0.1000000015), (0, 0.0000000015))
                Line((0, 0.1000000015), (-0.397261822, 0.1000000015))
                CenterArc((-0.397261822, 0.8000000015), 0.7, -106.699244234, 16.699244234)
                Line((-0.5984053419, 0.1295216018), (-1.3499459715, 0.3549837907))
                CenterArc((-1.5510894914, -0.315494609), 0.7, 73.300755766, 25.2300098439)
                Line((-1.6549278084, 0.3767608381), (-3.3123583198, 0.1281462613))
                CenterArc((-3.4161966368, 0.8204017084), 0.7, -111.8014094864, 30.3321750963)
                Line((-3.6761701103, 0.1704680247), (-4.0000000596, 0.3000000045))
                Line((-4.0000000596, 0.1922967083), (-4.0000000596, 0.3000000045))
                Line((-3.7133091779, 0.0776203556), (-4.0000000596, 0.1922967083))
                CenterArc((-3.4161966368, 0.8204017084), 0.8, -111.8014094864, 30.3321750963)
                Line((-1.6400937631, 0.2778672028), (-3.2975242745, 0.0292526261))
                CenterArc((-1.5510894914, -0.315494609), 0.6, 73.300755766, 25.2300098439)
                Line((-0.6271401305, 0.0337389733), (-1.37868076, 0.2592011622))
            make_face()
        # OneSide extrude, distance=1.4
        extrude(amount=1.4)

        # Sketch91 -> Extrude16 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 28 constraints, 17 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.3017127901, perimeter: 4.2169809066
            with BuildLine():
                Line((0.7, -1.6975396106), (0.7, -1.2975089383))
                Line((0.7, -3.1975242745), (0.7, -1.6975396106))
                Line((0.7, -3.2975242745), (0.7, -3.1975242745))
                Line((0.7, -3.2975242745), (0.8, -3.2975242745))
                Line((0.8, -3.2975242745), (0.8997053781, -1.5086551616))
                CenterArc((0.7, -1.4975242745), 0.2000153361, -3.1901678578, 93.1901678578)
            make_face()
            # Profile area: 0.079521564, perimeter: 1.1568583471
            with BuildLine():
                Line((0.7, -1.025), (0.7, -0.575))
                CenterArc((0.7, -0.8), 0.225, -90, 180)
            make_face()
            # Profile area: 0.0078539816, perimeter: 0.3570796327
            with BuildLine():
                Line((0.7, -3.2975242745), (0.8, -3.2975242745))
                Line((0.7, -3.3975242745), (0.7, -3.2975242745))
                CenterArc((0.7, -3.2975242745), 0.1, -90, 90)
            make_face()
            # Profile area: 0.2612163097, perimeter: 2.426518996
            with BuildLine():
                Line((1.0191457196, -3.8213066854), (1.0752652664, -3.2975242745))
                CenterArc((0.8202838889, -3.8000000596), 0.2, -90, 83.8844961323)
                Line((0.8202838889, -4.0000000596), (1.4, -4.0000000596))
                Line((1.4, -4.0000000596), (1.4, -3.2975242745))
                Line((1.0752652664, -3.2975242745), (1.4, -3.2975242745))
            make_face()
            # Profile area: 0.5287829331, perimeter: 6.3799668125
            with BuildLine():
                Line((1.0752652664, -3.2975242745), (1.4, -3.2975242745))
                Line((1.4, -3.2975242745), (1.4, -0.3347524339))
                CenterArc((0.7, -0.3347524339), 0.7, -26.5650483596, 26.5650483596)
                Line((1.2926209706, -0.7147580852), (1.3260990491, -0.64780192))
                CenterArc((1.7398345771, -0.938364861), 0.5, 153.4349516404, 44.9999971825)
                Line((1.2518361095, -1.0555082882), (1.2654929281, -1.096478744))
                CenterArc((0.5877578008, -1.2768677244), 0.7, -6.1155038677, 24.5504526907)
                Line((1.0752652664, -3.2975242745), (1.2837742082, -1.3514409146))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.SUBTRACT)

        # Sketch92 -> Extrude17 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.1000000015, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0176714587, perimeter: 0.471238898
            with Locations((-0.3373, 0.197261822)):
                Circle(0.075)
            # Profile area: 0.0176714587, perimeter: 0.471238898
            with Locations((-1.0627, 0.197261822)):
                Circle(0.075)
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a rectangular vertical duct or channel with a trapezoidal top opening, featuring internal ribbing/fluting along its length and angled side panels, designed as an industrial air handling or structural component.
def model_36182_1c8d16f4_0004():
    """Model: nogi"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 18 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 216, perimeter: 150
            with BuildLine():
                Line((-1.5, 12), (-1.5, -12))
                Line((-1.5, -12), (-12, -12))
                Line((-12, -12), (-12, -15))
                Line((-12, -15), (12, -15))
                Line((12, -15), (12, -12))
                Line((12, -12), (1.5, -12))
                Line((1.5, -12), (1.5, 12))
                Line((12, 12), (1.5, 12))
                Line((12, 15), (12, 12))
                Line((-12, 15), (12, 15))
                Line((-12, 12), (-12, 15))
                Line((-1.5, 12), (-12, 12))
            make_face()
        # OneSide extrude, distance=100
        extrude(amount=100)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 7 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 100, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 616, perimeter: 266
            with BuildLine():
                Line((-13, 16), (-13, -16))
                Line((-13, -16), (13, -16))
                Line((13, -16), (13, 16))
                Line((13, 16), (-13, 16))
            make_face()
            with BuildLine():
                Line((12, -15), (12, -12))
                Line((-12, -15), (12, -15))
                Line((-12, -12), (-12, -15))
                Line((-1.5, -12), (-12, -12))
                Line((-1.5, 12), (-1.5, -12))
                Line((-12, 12), (-1.5, 12))
                Line((-12, 15), (-12, 12))
                Line((12, 15), (-12, 15))
                Line((12, 12), (12, 15))
                Line((1.5, 12), (12, 12))
                Line((1.5, -12), (1.5, 12))
                Line((12, -12), (1.5, -12))
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 216, perimeter: 150
            with BuildLine():
                Line((12, -12), (1.5, -12))
                Line((1.5, -12), (1.5, 12))
                Line((1.5, 12), (12, 12))
                Line((12, 12), (12, 15))
                Line((12, 15), (-12, 15))
                Line((-12, 15), (-12, 12))
                Line((-12, 12), (-1.5, 12))
                Line((-1.5, 12), (-1.5, -12))
                Line((-1.5, -12), (-12, -12))
                Line((-12, -12), (-12, -15))
                Line((-12, -15), (12, -15))
                Line((12, -15), (12, -12))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 8 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 616, perimeter: 266
            with BuildLine():
                Line((13, -16), (13, 16))
                Line((13, 16), (-13, 16))
                Line((-13, 16), (-13, -16))
                Line((-13, -16), (13, -16))
            make_face()
            with BuildLine():
                Line((-12, 15), (-12, 12))
                Line((12, 15), (-12, 15))
                Line((12, 12), (12, 15))
                Line((1.5, 12), (12, 12))
                Line((1.5, -12), (1.5, 12))
                Line((12, -12), (1.5, -12))
                Line((12, -15), (12, -12))
                Line((-12, -15), (12, -15))
                Line((-12, -12), (-12, -15))
                Line((-1.5, -12), (-12, -12))
                Line((-1.5, 12), (-1.5, -12))
                Line((-12, 12), (-1.5, 12))
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 216, perimeter: 150
            with BuildLine():
                Line((-12, 12), (-1.5, 12))
                Line((-1.5, 12), (-1.5, -12))
                Line((-1.5, -12), (-12, -12))
                Line((-12, -12), (-12, -15))
                Line((-12, -15), (12, -15))
                Line((12, -15), (12, -12))
                Line((12, -12), (1.5, -12))
                Line((1.5, -12), (1.5, 12))
                Line((1.5, 12), (12, 12))
                Line((12, 12), (12, 15))
                Line((12, 15), (-12, 15))
                Line((-12, 15), (-12, 12))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical housing or container with a flared, open top featuring internal ribbing and a rectangular access opening or slot on the side.
def model_36194_c9cfd107_0009():
    """Model: Component12"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0015067393, perimeter: 0.1376017582
            Circle(0.0219)
        # OneSide extrude, distance=0.075
        extrude(amount=0.075)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.075, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0004085373, perimeter: 0.1045062603
            with BuildLine():
                Line((-0.0047, 0.0213897172), (-0.0047, -0.0213897172))
                CenterArc((0, 0), 0.0219, -102.3927577003, 24.7855154005)
                Line((0.0047, 0.0213897172), (0.0047, -0.0213897172))
                CenterArc((0, 0), 0.0219, 77.6072422997, 24.7855154005)
            make_face()
        # OneSide extrude, distance=-0.025
        extrude(amount=-0.025, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0001227185, perimeter: 0.0392699082
            with Locations((0, 0.0625)):
                Circle(0.00625)
        # TwoSides extrude (symmetric), distance=0.1
        extrude(amount=0.1, both=True, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a ball joint or spherical connector featuring a cylindrical stem on one end and a large spherical socket or cup on the other end, with internal cavity structure visible through the mesh rendering.
def model_36436_362a4413_0000():
    """Model: Main Rod Connector Pin Screw v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            Circle(0.2)
        # OneSide extrude, distance=0.6
        extrude(amount=0.6)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on YZ construction plane
        # Sketch has 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 0.6361725124, perimeter: 2.8274333882
            with Locations((0, 1)):
                Circle(0.45)
        # Symmetric extrude, each_side=0.14
        extrude(amount=0.14, both=True, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 13 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.14, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 0.06255177, perimeter: 1.8247501246
            with BuildLine():
                CenterArc((0, 1), 0.45, 152.8993146518, 10.3092382337)
                Line((-0.4308131846, 1.13), (0.4308131846, 1.13))
                CenterArc((0, 1), 0.45, 16.7914471146, 10.3092382337)
                Line((-0.40059331, 1.205), (0.40059331, 1.205))
            make_face()
            # Profile area: 0.0674207481, perimeter: 1.9438875367
            with BuildLine():
                Line((-0.4482186966, 1.04), (0.4482186966, 1.04))
                CenterArc((0, 1), 0.45, 174.9003110858, 9.5605326121)
                Line((-0.4486368242, 0.965), (0.4486368242, 0.965))
                CenterArc((0, 1), 0.45, -4.4608436979, 9.5605326121)
            make_face()
        # OneSide extrude, distance=0.025
        extrude(amount=0.025, mode=Mode.ADD)
    return part.part


# Description: This is a flat sheet metal panel with a parallelogram shape featuring a small rectangular cutout or slot on the right edge and appears to have a slight bend or flange detail near the bottom right corner.
def model_36436_362a4413_0006():
    """Model: Platine v13"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 11 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 66.8115044408, perimeter: 37.1699111843
            with BuildLine():
                Line((-5, 3.35), (-5, -3.35))
                Line((-5, -3.35), (5, -3.35))
                Line((5, -3.35), (5, 3.35))
                Line((5, 3.35), (-5, 3.35))
            make_face()
            with BuildLine():
                CenterArc((-3.5733423482, 1.9722053021), 0.1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-1.5044424843, 1.7038542738), 0.1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-3.175144048, 0.8728317343), 0.1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1.8109911887, 0.3447861624), 0.1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0.5644573796, 1.3749078519), 0.1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-1.2534044255, -0.1919158944), 0.1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.15
        extrude(amount=0.15)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 8 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.15), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1.35, perimeter: 4.8
            with BuildLine():
                Line((-4.9, 2.35), (-4, 2.35))
                Line((-4.9, 0.85), (-4.9, 2.35))
                Line((-4, 0.85), (-4.9, 0.85))
                Line((-4, 2.35), (-4, 0.85))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 14 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(4.9, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 0.5371681469, perimeter: 4.4566370614
            with BuildLine():
                Line((-1.1, 0.35), (-2.1, 0.35))
                Line((-1.1, 0.95), (-1.1, 0.35))
                Line((-2.1, 0.95), (-1.1, 0.95))
                Line((-2.1, 0.35), (-2.1, 0.95))
            make_face()
            with BuildLine():
                CenterArc((-1.3312359852, 0.65), 0.1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-1.8687640148, 0.65), 0.1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.SUBTRACT)
    return part.part


# Description: A fastener consisting of a cylindrical shaft with a hexagonal head, featuring a threaded shaft for insertion into threaded holes or nuts.
def model_36436_362a4413_0025():
    """Model: Connector Screw v2 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            Circle(0.2)
        # OneSide extrude, distance=1.4
        extrude(amount=1.4)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on YZ construction plane
        # Sketch has 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 0.6361725124, perimeter: 2.8274333882
            with Locations((0, 1.8)):
                Circle(0.45)
        # Symmetric extrude, each_side=0.14
        extrude(amount=0.14, both=True, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 13 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.14, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 0.06255177, perimeter: 1.8247501246
            with BuildLine():
                CenterArc((0, 1.8), 0.45, 152.8993146518, 10.3092382337)
                Line((-0.4308131846, 1.93), (0.4308131846, 1.93))
                CenterArc((0, 1.8), 0.45, 16.7914471146, 10.3092382337)
                Line((-0.40059331, 2.005), (0.40059331, 2.005))
            make_face()
            # Profile area: 0.0664095875, perimeter: 1.9190266687
            with BuildLine():
                Line((-0.4482186966, 1.76), (0.4482186966, 1.76))
                CenterArc((0, 1.8), 0.45, -174.9003110858, 9.7068179977)
                Line((-0.4350574675, 1.685), (0.4350574675, 1.685))
                CenterArc((0, 1.8), 0.45, -14.8065069119, 9.7068179977)
            make_face()
        # OneSide extrude, distance=0.025
        extrude(amount=0.025, mode=Mode.ADD)
    return part.part


# Description: This is a ball joint or spherical connector featuring a cylindrical shaft on one end and a large spherical socket on the other, with internal cavity details visible through the mesh rendering.
def model_36436_362a4413_0033():
    """Model: Clamp Pin Screw v4 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            Circle(0.2)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on YZ construction plane
        # Sketch has 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 0.6361725124, perimeter: 2.8274333882
            with Locations((0, 0.9)):
                Circle(0.45)
        # Symmetric extrude, each_side=0.14
        extrude(amount=0.14, both=True, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 13 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.14, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 0.06255177, perimeter: 1.8247501246
            with BuildLine():
                CenterArc((0, 0.9), 0.45, 152.8993146518, 10.3092382337)
                Line((-0.4308131846, 1.03), (0.4308131846, 1.03))
                CenterArc((0, 0.9), 0.45, 16.7914471146, 10.3092382337)
                Line((-0.40059331, 1.105), (0.40059331, 1.105))
            make_face()
            # Profile area: 0.0674207481, perimeter: 1.9438875367
            with BuildLine():
                Line((-0.4482186966, 0.94), (0.4482186966, 0.94))
                CenterArc((0, 0.9), 0.45, 174.9003110858, 9.5605326121)
                Line((-0.4486368242, 0.865), (0.4486368242, 0.865))
                CenterArc((0, 0.9), 0.45, -4.4608436979, 9.5605326121)
            make_face()
        # OneSide extrude, distance=0.025
        extrude(amount=0.025, mode=Mode.ADD)
    return part.part


# Description: This is a U-shaped bracket or clamp with two parallel vertical arms connected by a top horizontal section, featuring a rectangular opening between the arms and a small protruding pin or attachment point on the upper surface.
def model_36665_6cd225dd_0005():
    """Model: Foot Connector Body"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 9 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.75, perimeter: 8
            with BuildLine():
                Line((7.5, 0.5), (6, 0.5))
                Line((6, 0.5), (6, -2))
                Line((6, -2), (7.5, -2))
                Line((7.5, -2), (7.5, 0.5))
            make_face()
            # Profile area: 3.75, perimeter: 8
            with BuildLine():
                Line((-2.5, 0.5), (-1, 0.5))
                Line((-2.5, -2), (-2.5, 0.5))
                Line((-1, -2), (-2.5, -2))
                Line((-1, 0.5), (-1, -2))
            make_face()
        # OneSide extrude, distance=12
        extrude(amount=12)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(6, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 3.75, perimeter: 8
            with BuildLine():
                Line((2, 10.5), (-0.5, 10.5))
                Line((2, 12), (2, 10.5))
                Line((-0.5, 12), (2, 12))
                Line((-0.5, 10.5), (-0.5, 12))
            make_face()
        # OneSide extrude, distance=7
        extrude(amount=7, mode=Mode.ADD)

        # Sketch5 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 12, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2513274123, perimeter: 5.0265482457
            with BuildLine():
                CenterArc((-2.5, 0.75), 0.45, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-2.5, 0.75), 0.35, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.8
        extrude(amount=1.8, mode=Mode.ADD)
    return part.part


# Description: This is a composite structural bracket or deflector with an angular, boomerang-like shape featuring a bent main body with a vertical flange on one end and a tapered, pointed extension on the opposite end.
def model_36667_6c4f7023_0000():
    """Model: 1_Cuerpo"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 8 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 124.1502031047, perimeter: 60.2411313831
            with BuildLine():
                Line((6.5, 8.6686763129), (6.5, 0))
                Line((15.4370973077, 10.568314988), (6.5, 8.6686763129))
                Line((18.5, 14.2185402752), (15.4370973077, 10.568314988))
                Line((0, 12.6), (18.5, 14.2185402752))
                Line((0, 0), (0, 12.6))
                Line((6.5, 0), (0, 0))
            make_face()
        # OneSide extrude, distance=2.25
        extrude(amount=2.25)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-1.0939835193, 12.504288844, 0), x_dir=(0, 0, 1), z_dir=(-0.0871557427, 0.9961946981, 0))):
            # Profile area: 2.0999092965, perimeter: 16.36528133
            with BuildLine():
                Line((2.25, 11.6688293532), (2.25, 19.6688293532))
                Line((1.9, 19.6688293532), (2.25, 19.6688293532))
                Line((1.9, 15.6693476591), (1.9, 19.6688293532))
                Line((2.25, 11.6688293532), (1.9, 15.6693476591))
            make_face()
        # OneSide extrude, distance=-6
        extrude(amount=-6, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 6.4561423577, perimeter: 12.154216119
            with BuildLine():
                Line((-17.6609003688, 13.2185402752), (-16.2761969389, 11.568314988))
                Line((-12.812687807, 11.2652972029), (-16.2761969389, 11.568314988))
                Line((-12.6799268784, 12.7827615615), (-12.812687807, 11.2652972029))
                Line((-17.6609003688, 13.2185402752), (-12.6799268784, 12.7827615615))
            make_face()
        # OneSide extrude, distance=-1.25
        extrude(amount=-1.25, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a skylight or roof window assembly with a trapezoidal shape, featuring a sloped glazed panel recessed into a dark frame base with angled side flanges and internal structural ribs for support and water drainage.
def model_37040_ecbcd25e_0003():
    """Model: podstawa wystająca v4"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 69.0215401605, perimeter: 138.043080321
            with BuildLine():
                Line((-7.2654252801, -10), (7.2654252801, -10))
                Line((7.2654252801, -10), (11.7557050458, 3.8196601125))
                Line((11.7557050458, 3.8196601125), (0, 12.360679775))
                Line((0, 12.360679775), (-11.7557050458, 3.8196601125))
                Line((-11.7557050458, 3.8196601125), (-7.2654252801, -10))
            make_face()
            with BuildLine():
                Line((-10.5801345413, 3.4376941013), (-6.538882752, -9))
                Line((0, 11.1246117975), (-10.5801345413, 3.4376941013))
                Line((10.5801345413, 3.4376941013), (0, 11.1246117975))
                Line((6.538882752, -9), (10.5801345413, 3.4376941013))
                Line((-6.538882752, -9), (6.538882752, -9))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=2
        extrude(amount=2)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 100.5898130023, perimeter: 154.7535584651
            with BuildLine():
                Line((-8.2099305665, 11.3), (-13.2839467018, -4.3162159271))
                Line((-13.2839467018, -4.3162159271), (0, -13.9675681457))
                Line((0, -13.9675681457), (13.2839467018, -4.3162159271))
                Line((13.2839467018, -4.3162159271), (8.2099305665, 11.3))
                Line((8.2099305665, 11.3), (-8.2099305665, 11.3))
            make_face()
            with BuildLine():
                Line((0, -12.360679775), (11.7557050458, -3.8196601125))
                Line((-11.7557050458, -3.8196601125), (0, -12.360679775))
                Line((-7.2654252801, 10), (-11.7557050458, -3.8196601125))
                Line((7.2654252801, 10), (-7.2654252801, 10))
                Line((11.7557050458, -3.8196601125), (7.2654252801, 10))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-1.5
        extrude(amount=-1.5, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 169.6113531629, perimeter: 147.4881331851
            with BuildLine():
                Line((-8.2099305665, 11.3), (8.2099305665, 11.3))
                Line((-13.2839467018, -4.3162159271), (-8.2099305665, 11.3))
                Line((0, -13.9675681457), (-13.2839467018, -4.3162159271))
                Line((13.2839467018, -4.3162159271), (0, -13.9675681457))
                Line((8.2099305665, 11.3), (13.2839467018, -4.3162159271))
            make_face()
            with BuildLine():
                Line((-10.5801345413, -3.4376941013), (-6.538882752, 9))
                Line((-6.538882752, 9), (6.538882752, 9))
                Line((6.538882752, 9), (10.5801345413, -3.4376941013))
                Line((10.5801345413, -3.4376941013), (0, -11.1246117975))
                Line((0, -11.1246117975), (-10.5801345413, -3.4376941013))
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 294.2497238422, perimeter: 65.3888275205
            with BuildLine():
                Line((0, -11.1246117975), (-10.5801345413, -3.4376941013))
                Line((10.5801345413, -3.4376941013), (0, -11.1246117975))
                Line((6.538882752, 9), (10.5801345413, -3.4376941013))
                Line((-6.538882752, 9), (6.538882752, 9))
                Line((-10.5801345413, -3.4376941013), (-6.538882752, 9))
            make_face()
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.ADD)
    return part.part


# Description: This is a rectangular box or enclosure with an open top, featuring angled side walls and a sloped roof-like top section, with internal structural geometry visible through transparent faces.
def model_37040_ecbcd25e_0010():
    """Model: uchwyt v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 4, perimeter: 8
            with BuildLine():
                Line((-2, 2), (0, 2))
                Line((-2, 0), (-2, 2))
                Line((0, 0), (-2, 0))
                Line((0, 2), (0, 0))
            make_face()
        # OneSide extrude, distance=0.4
        extrude(amount=0.4)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.4, perimeter: 4.4
            with BuildLine():
                Line((1.8, 0), (1.8, 2))
                Line((2, 0), (1.8, 0))
                Line((2, 0), (2, 2))
                Line((2, 2), (1.8, 2))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-1, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 1.6, perimeter: 5.6
            with BuildLine():
                Line((1, 2), (1.8, 2))
                Line((1, 0), (1, 2))
                Line((1.8, 0), (1, 0))
                Line((1.8, 2), (1.8, 0))
            make_face()
            # Profile area: 0.4, perimeter: 4.4
            with BuildLine():
                Line((1.8, 2), (1.8, 0))
                Line((2, 0), (1.8, 0))
                Line((2, 2), (2, 0))
                Line((1.8, 2), (2, 2))
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)
    return part.part


# Description: This is a rectangular hollow frame or bracket with a thin-walled, elongated parallelogram profile, featuring four corner joints and an open center cavity.
def model_37040_ecbcd25e_0022():
    """Model: ścianka szkielet 1 v11 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 11 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 55.9437746564, perimeter: 113.8875493128
            with BuildLine():
                Line((6.538882752, -9), (10.5801345413, 3.4376941013))
                Line((6.538882752, -9), (6.538882752, -10))
                Line((6.538882752, -10), (7.2654252801, -10))
                Line((7.2654252801, -10), (11.7557050458, 3.8196601125))
                Line((11.7557050458, 3.8196601125), (0, 12.360679775))
                Line((0, 12.360679775), (-11.7557050458, 3.8196601125))
                Line((-11.7557050458, 3.8196601125), (-7.2654252801, -10))
                Line((-7.2654252801, -10), (-6.538882752, -10))
                Line((-6.538882752, -9), (-6.538882752, -10))
                Line((-10.5801345413, 3.4376941013), (-6.538882752, -9))
                Line((0, 11.1246117975), (-10.5801345413, 3.4376941013))
                Line((10.5801345413, 3.4376941013), (0, 11.1246117975))
            make_face()
        # OneSide extrude, distance=40
        extrude(amount=40)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 10 constraints, 9 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(9.510565163, 0, 3.0901699437), x_dir=(0.3090169944, 0, -0.9510565163), z_dir=(0.9510565163, 0, 0.3090169944))):
            # Profile area: 394.5985307839, perimeter: 95.3306205265
            with BuildLine():
                Line((5.2654252801, 38), (-5.2654252801, 38))
                Line((-5.2654252801, 1), (-5.2654252801, 38))
                Line((5.5333744725, 1), (-5.2654252801, 1))
                Line((5.5333744725, 1), (5.2654252801, 38))
            make_face()
        # OneSide extrude, distance=-10
        extrude(amount=-10, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 40, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 41.7761953603, perimeter: 85.7884586981
            with BuildLine():
                Line((0, -12.360679775), (11.7557050458, -3.8196601125))
                Line((11.7557050458, -3.8196601125), (7.2654252801, 10))
                Line((7.2654252801, 10), (6.538882752, 10))
                Line((6.538882752, 10), (6.538882752, 9))
                Line((6.538882752, 9), (10.5801345413, -3.4376941013))
                Line((10.5801345413, -3.4376941013), (0, -11.1246117975))
                Line((0, -11.1246117975), (-10.5801345413, -3.4376941013))
                Line((-10.5801345413, -3.4376941013), (-11.7557050458, -3.8196601125))
                Line((-11.7557050458, -3.8196601125), (0, -12.360679775))
            make_face()
        # OneSide extrude, distance=-50
        extrude(amount=-50, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a twisted or braided cylindrical bundle composed of multiple elongated strands or cables wound together, featuring a helical twist pattern that creates a tapered, rope-like structure.
def model_37040_ecbcd25e_0031():
    """Model: ksztalt 2 v5"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 27 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.3401856736, perimeter: 4.9497264752
            with BuildLine():
                Line((8.4792674371, 18.358685952), (9.6092298732, 16.3318390932))
                Line((9.6092298732, 16.3318390932), (9.6561138851, 16.5547349233))
                Line((8.5698329177, 18.5032290467), (9.6561138851, 16.5547349233))
                Line((8.4792674371, 18.358685952), (8.5698329177, 18.5032290467))
            make_face()
            # Profile area: 0.1966943275, perimeter: 2.7960599436
            with BuildLine():
                Line((8.4806223203, 18.6632487195), (9.1147031935, 19.6752459068))
                Line((8.4806223203, 18.6632487195), (8.5698329177, 18.5032290467))
                Line((8.5698329177, 18.5032290467), (9.236638883, 19.5674556933))
                Line((9.236638883, 19.5674556933), (9.1147031935, 19.6752459068))
            make_face()
            # Profile area: 0.4734516078, perimeter: 5.834538665
            with BuildLine():
                Line((8.7171847363, 11.1971331805), (9.2513845187, 13.7368241996))
                Line((9.2513845187, 13.7368241996), (9.1266024633, 14.0373332943))
                Line((8.6013272377, 11.5400713763), (9.1266024633, 14.0373332943))
                Line((8.6013272377, 11.5400713763), (8.7171847363, 11.1971331805))
            make_face()
            # Profile area: 0.1601588668, perimeter: 2.8055820121
            with BuildLine():
                Line((11.1050299982, 22.5494200344), (11.6693751374, 23.4501185378))
                Line((11.6693751374, 23.4501185378), (11.6956864912, 23.7945119942))
                Line((11.2007811447, 23.0046398504), (11.6956864912, 23.7945119942))
                Line((11.1050299982, 22.5494200344), (11.2007811447, 23.0046398504))
            make_face()
            # Profile area: 0.0648555682, perimeter: 1.4986614684
            with BuildLine():
                Line((11.6956864912, 23.7945119942), (11.910155704, 24.1368062491))
                Line((11.6693751374, 23.4501185378), (11.6956864912, 23.7945119942))
                Line((11.6693751374, 23.4501185378), (11.8838443502, 23.7924127928))
                Line((11.8838443502, 23.7924127928), (11.910155704, 24.1368062491))
            make_face()
            # Profile area: 1.0649668788, perimeter: 11.9826315074
            with BuildLine():
                Line((11.6693751374, 23.4501185378), (11.8838443502, 23.7924127928))
                Line((11.2563594478, 18.0440910747), (11.6693751374, 23.4501185378))
                Line((11.4327639869, 17.8881508163), (11.2563594478, 18.0440910747))
                Line((11.4327639869, 17.8881508163), (11.8838443502, 23.7924127928))
            make_face()
            # Profile area: 0.6891332012, perimeter: 7.9157201709
            with BuildLine():
                Line((11.4140099582, 17.6426763781), (11.237605419, 17.7986166365))
                Line((10.9634214125, 14.2097789578), (11.237605419, 17.7986166365))
                Line((10.9634214125, 14.2097789578), (11.1290429798, 13.9126986809))
                Line((11.1290429798, 13.9126986809), (11.4140099582, 17.6426763781))
            make_face()
            # Profile area: 0.4335265898, perimeter: 6.3779726993
            with BuildLine():
                Line((11.1290429798, 13.9126986809), (12.5309, 11.3981465091))
                Line((11.1084157278, 13.6427053282), (11.1290429798, 13.9126986809))
                Line((11.1084157278, 13.6427053282), (12.5309, 11.0911534477))
                Line((12.5309, 11.3981465091), (12.5309, 11.0911534477))
            make_face()
            # Profile area: 0.7842997244, perimeter: 10.4672034039
            with BuildLine():
                Line((10.9177875889, 22.5529802995), (11.2007811447, 23.0046398504))
                Line((11.2007811447, 23.0046398504), (11.8832105194, 26.2490435573))
                Line((11.8832105194, 26.2490435573), (11.9904392893, 27.6525778284))
                Line((10.9177875889, 22.5529802995), (11.9904392893, 27.6525778284))
            make_face()
            # Profile area: 0.2643110983, perimeter: 5.6887309703
            with BuildLine():
                Line((11.8832105194, 26.2490435573), (11.9904392893, 27.6525778284))
                Line((11.8832105194, 26.2490435573), (12.1789440203, 27.6550188894))
                Line((12.1789440203, 27.6550188894), (12.2861727902, 29.0585531605))
                Line((11.9904392893, 27.6525778284), (12.2861727902, 29.0585531605))
            make_face()
            # Profile area: 0.5623883267, perimeter: 7.8308245114
            with BuildLine():
                Line((11.8832105194, 26.2490435573), (12.1789440203, 27.6550188894))
                Line((11.6956864912, 23.7945119942), (11.8832105194, 26.2490435573))
                Line((11.6956864912, 23.7945119942), (11.910155704, 24.1368062491))
                Line((11.910155704, 24.1368062491), (12.1789440203, 27.6550188894))
            make_face()
            # Profile area: 0.1916915832, perimeter: 3.0355857084
            with BuildLine():
                Line((11.910155704, 24.1368062491), (12.5309, 25.1275181727))
                Line((11.8838443502, 23.7924127928), (11.910155704, 24.1368062491))
                Line((11.8838443502, 23.7924127928), (12.5309, 24.8251178076))
                Line((12.5309, 25.1275181727), (12.5309, 24.8251178076))
            make_face()
            # Profile area: 0.2902269515, perimeter: 3.4646531388
            with BuildLine():
                Line((12.5309, 16.9174070109), (11.4327639869, 17.8881508163))
                Line((11.4140099582, 17.6426763781), (11.4327639869, 17.8881508163))
                Line((12.5309, 16.6553541552), (11.4140099582, 17.6426763781))
                Line((12.5309, 16.9174070109), (12.5309, 16.6553541552))
            make_face()
            # Profile area: 0.4803854945, perimeter: 6.611806358
            with BuildLine():
                Line((9.3423054078, 19.7361001523), (9.2203697182, 19.8438903658))
                Line((9.3423054078, 19.7361001523), (10.8220364425, 22.0977604835))
                Line((10.8220364425, 22.0977604835), (10.9177875889, 22.5529802995))
                Line((9.2203697182, 19.8438903658), (10.9177875889, 22.5529802995))
            make_face()
            # Profile area: 0.2666420758, perimeter: 5.200195573
            with BuildLine():
                Line((12.2861727902, 29.0585531605), (12.5309, 30.2220345345))
                Line((12.1789440203, 27.6550188894), (12.2861727902, 29.0585531605))
                Line((12.1789440203, 27.6550188894), (12.5309, 29.3282869629))
                Line((12.5309, 30.2220345345), (12.5309, 29.3282869629))
            make_face()
            # Profile area: 0.5685470533, perimeter: 8.2276251647
            with BuildLine():
                Line((6.4146266704, 22.0620928253), (8.3900568396, 18.5187056248))
                Line((8.3900568396, 18.5187056248), (8.4806223203, 18.6632487195))
                Line((6.7520791765, 21.7637874004), (8.4806223203, 18.6632487195))
                Line((6.7520791765, 21.7637874004), (6.4146266704, 22.0620928253))
            make_face()
            # Profile area: 0.6707200848, perimeter: 7.6228951071
            with BuildLine():
                Line((6.4640257837, 22.2804772439), (6.7520791765, 21.7637874004))
                Line((9.1147031935, 19.6752459068), (6.7520791765, 21.7637874004))
                Line((9.1147031935, 19.6752459068), (9.2203697182, 19.8438903658))
                Line((9.2203697182, 19.8438903658), (6.4640257837, 22.2804772439))
            make_face()
            # Profile area: 0.0273870344, perimeter: 0.7075581488
            with BuildLine():
                Line((8.3900568396, 18.5187056248), (8.4792674371, 18.358685952))
                Line((8.4792674371, 18.358685952), (8.5698329177, 18.5032290467))
                Line((8.4806223203, 18.6632487195), (8.5698329177, 18.5032290467))
                Line((8.3900568396, 18.5187056248), (8.4806223203, 18.6632487195))
            make_face()
            # Profile area: 0.9677154826, perimeter: 14.2090668036
            with BuildLine():
                Line((11.9904392893, 27.6525778284), (12.5309, 34.7267532603))
                Line((11.9904392893, 27.6525778284), (12.2861727902, 29.0585531605))
                Line((12.2861727902, 29.0585531605), (12.5309, 32.2618261839))
                Line((12.5309, 34.7267532603), (12.5309, 32.2618261839))
            make_face()
            # Profile area: 0.6436961571, perimeter: 7.3971105028
            with BuildLine():
                Line((9.1266024633, 14.0373332943), (9.1951984818, 14.3634522814))
                Line((9.1951984818, 14.3634522814), (7.9121047508, 17.4534906252))
                Line((7.789406773, 17.2576638566), (7.9121047508, 17.4534906252))
                Line((9.1266024633, 14.0373332943), (7.789406773, 17.2576638566))
            make_face()
            # Profile area: 0.0319535957, perimeter: 0.7235237789
            with BuildLine():
                Line((9.1147031935, 19.6752459068), (9.2203697182, 19.8438903658))
                Line((9.236638883, 19.5674556933), (9.1147031935, 19.6752459068))
                Line((9.236638883, 19.5674556933), (9.3423054078, 19.7361001523))
                Line((9.3423054078, 19.7361001523), (9.2203697182, 19.8438903658))
            make_face()
            # Profile area: 0.0884303929, perimeter: 2.0839202175
            with BuildLine():
                Line((6.4640257837, 22.2804772439), (6.1265732776, 22.5787826688))
                Line((6.1265732776, 22.5787826688), (6.4146266704, 22.0620928253))
                Line((6.7520791765, 21.7637874004), (6.4146266704, 22.0620928253))
                Line((6.4640257837, 22.2804772439), (6.7520791765, 21.7637874004))
            make_face()
            # Profile area: 0.1694400797, perimeter: 2.4907485541
            with BuildLine():
                Line((7.9121047508, 17.4534906252), (7.8365854313, 17.6353616665))
                Line((7.9121047508, 17.4534906252), (8.4792674371, 18.358685952))
                Line((8.3900568396, 18.5187056248), (8.4792674371, 18.358685952))
                Line((7.8365854313, 17.6353616665), (8.3900568396, 18.5187056248))
            make_face()
            # Profile area: 0.0855773546, perimeter: 1.9963483089
            with BuildLine():
                Line((10.8220364425, 22.0977604835), (10.9177875889, 22.5529802995))
                Line((10.8220364425, 22.0977604835), (11.1050299982, 22.5494200344))
                Line((11.1050299982, 22.5494200344), (11.2007811447, 23.0046398504))
                Line((10.9177875889, 22.5529802995), (11.2007811447, 23.0046398504))
            make_face()
            # Profile area: 0.2186010916, perimeter: 3.1272870345
            with BuildLine():
                Line((7.0619477771, 16.0966345798), (7.789406773, 17.2576638566))
                Line((7.789406773, 17.2576638566), (7.7138874535, 17.4395348979))
                Line((6.9955737792, 16.2931016136), (7.7138874535, 17.4395348979))
                Line((6.9955737792, 16.2931016136), (7.0619477771, 16.0966345798))
            make_face()
            # Profile area: 0.1570924514, perimeter: 2.6400924403
            with BuildLine():
                Line((6.4146266704, 22.0620928253), (5.7570909885, 22.6433493203))
                Line((6.1265732776, 22.5787826688), (6.4146266704, 22.0620928253))
                Line((6.1265732776, 22.5787826688), (5.5851718137, 23.0573774067))
                Line((5.7570909885, 22.6433493203), (5.5851718137, 23.0573774067))
            make_face()
            # Profile area: 0.2835141777, perimeter: 5.9182183343
            with BuildLine():
                Line((3.9842245304, 26.4215766324), (3.4846770467, 27.6246227093))
                Line((2.6793178282, 29.0692192286), (3.4846770467, 27.6246227093))
                Line((2.6793178282, 29.0692192286), (2.9425441027, 28.2900694559))
                Line((2.9425441027, 28.2900694559), (3.9842245304, 26.4215766324))
            make_face()
            # Profile area: 0.5407267047, perimeter: 8.9874803623
            with BuildLine():
                Line((4.7837086922, 24.9875183751), (6.1265732776, 22.5787826688))
                Line((6.4640257837, 22.2804772439), (6.1265732776, 22.5787826688))
                Line((4.2841612084, 26.190564452), (6.4640257837, 22.2804772439))
                Line((4.7837086922, 24.9875183751), (4.2841612084, 26.190564452))
            make_face()
            # Profile area: 0.5109899311, perimeter: 7.4961730202
            with BuildLine():
                Line((5.5851718137, 23.0573774067), (5.2628445291, 23.3423122519))
                Line((5.5851718137, 23.0573774067), (4.7837086922, 24.9875183751))
                Line((3.9842245304, 26.4215766324), (4.7837086922, 24.9875183751))
                Line((5.2628445291, 23.3423122519), (3.9842245304, 26.4215766324))
            make_face()
            # Profile area: 0.0371039133, perimeter: 0.8560354231
            with BuildLine():
                Line((7.789406773, 17.2576638566), (7.7138874535, 17.4395348979))
                Line((7.789406773, 17.2576638566), (7.9121047508, 17.4534906252))
                Line((7.9121047508, 17.4534906252), (7.8365854313, 17.6353616665))
                Line((7.7138874535, 17.4395348979), (7.8365854313, 17.6353616665))
            make_face()
            # Profile area: 1.251581914, perimeter: 17.7095186755
            with BuildLine():
                Line((3.4846770467, 27.6246227093), (1.7822688184, 31.7244842976))
                Line((3.4846770467, 27.6246227093), (4.2841612084, 26.190564452))
                Line((4.2841612084, 26.190564452), (0.8917637378, 34.360379336))
                Line((0.8917637378, 34.360379336), (1.7822688184, 31.7244842976))
            make_face()
            # Profile area: 1.0707312549, perimeter: 12.026998844
            with BuildLine():
                Line((7.7138874535, 17.4395348979), (5.4347637038, 22.9282841655))
                Line((7.7138874535, 17.4395348979), (7.8365854313, 17.6353616665))
                Line((7.8365854313, 17.6353616665), (5.7570909885, 22.6433493203))
                Line((5.7570909885, 22.6433493203), (5.4347637038, 22.9282841655))
            make_face()
            # Profile area: 0.2454360903, perimeter: 5.8889935697
            with BuildLine():
                Line((3.9842245304, 26.4215766324), (4.7837086922, 24.9875183751))
                Line((4.7837086922, 24.9875183751), (4.2841612084, 26.190564452))
                Line((3.4846770467, 27.6246227093), (4.2841612084, 26.190564452))
                Line((3.9842245304, 26.4215766324), (3.4846770467, 27.6246227093))
            make_face()
            # Profile area: 0.2483886317, perimeter: 3.3729103957
            with BuildLine():
                Line((4.3378325075, 24.1600157778), (4.46406174, 23.7863772497))
                Line((5.4347637038, 22.9282841655), (4.46406174, 23.7863772497))
                Line((5.4347637038, 22.9282841655), (5.2628445291, 23.3423122519))
                Line((5.2628445291, 23.3423122519), (4.3378325075, 24.1600157778))
            make_face()
            # Profile area: 0.0844667854, perimeter: 1.7570306126
            with BuildLine():
                Line((5.4347637038, 22.9282841655), (5.2628445291, 23.3423122519))
                Line((5.7570909885, 22.6433493203), (5.4347637038, 22.9282841655))
                Line((5.7570909885, 22.6433493203), (5.5851718137, 23.0573774067))
                Line((5.5851718137, 23.0573774067), (5.2628445291, 23.3423122519))
            make_face()
            # Profile area: 0.0415397726, perimeter: 0.8747502654
            with BuildLine():
                Line((10.2832045055, 18.6422997173), (10.1246877344, 18.7824273261))
                Line((10.2832045055, 18.6422997173), (10.329682699, 18.8632662067))
                Line((10.329682699, 18.8632662067), (10.1711659278, 19.0033938155))
                Line((10.1246877344, 18.7824273261), (10.1711659278, 19.0033938155))
            make_face()
            # Profile area: 0.4286284871, perimeter: 5.1517559056
            with BuildLine():
                Line((9.6561138851, 16.5547349233), (9.7926071061, 16.3099030179))
                Line((9.7926071061, 16.3099030179), (10.2832045055, 18.6422997173))
                Line((10.2832045055, 18.6422997173), (10.1246877344, 18.7824273261))
                Line((9.6561138851, 16.5547349233), (10.1246877344, 18.7824273261))
            make_face()
            # Profile area: 0.0781458751, perimeter: 1.6618627515
            with BuildLine():
                Line((10.8576128401, 10.359906799), (10.6985589079, 10.7429518856))
                Line((10.6668557894, 10.3279847708), (10.6985589079, 10.7429518856))
                Line((10.8259097217, 9.9449396842), (10.6668557894, 10.3279847708))
                Line((10.8259097217, 9.9449396842), (10.8576128401, 10.359906799))
            make_face()
            # Profile area: 0.2464708865, perimeter: 2.9826787786
            with BuildLine():
                Line((11.2563594478, 18.0440910747), (10.329682699, 18.8632662067))
                Line((10.2832045055, 18.6422997173), (10.329682699, 18.8632662067))
                Line((11.237605419, 17.7986166365), (10.2832045055, 18.6422997173))
                Line((11.237605419, 17.7986166365), (11.2563594478, 18.0440910747))
            make_face()
            # Profile area: 0.0419024718, perimeter: 1.0161642716
            with BuildLine():
                Line((9.6092298732, 16.3318390932), (9.7457230942, 16.0870071877))
                Line((9.7457230942, 16.0870071877), (9.7926071061, 16.3099030179))
                Line((9.6561138851, 16.5547349233), (9.7926071061, 16.3099030179))
                Line((9.6092298732, 16.3318390932), (9.6561138851, 16.5547349233))
            make_face()
            # Profile area: 0.686381818, perimeter: 8.0352998327
            with BuildLine():
                Line((10.6668557894, 10.3279847708), (10.6985589079, 10.7429518856))
                Line((10.6985589079, 10.7429518856), (9.3199805371, 14.0629431867))
                Line((9.2513845187, 13.7368241996), (9.3199805371, 14.0629431867))
                Line((10.6668557894, 10.3279847708), (9.2513845187, 13.7368241996))
            make_face()
            # Profile area: 0.7595991112, perimeter: 8.9853075664
            with BuildLine():
                Line((10.5150128773, 5.8755618833), (10.8259097217, 9.9449396842))
                Line((10.8259097217, 9.9449396842), (10.6668557894, 10.3279847708))
                Line((10.3614268054, 6.3301766561), (10.6668557894, 10.3279847708))
                Line((10.3614268054, 6.3301766561), (10.5150128773, 5.8755618833))
            make_face()
            # Profile area: 0.6373393538, perimeter: 7.6734593786
            with BuildLine():
                Line((10.1711659278, 19.0033938155), (10.8220364425, 22.0977604835))
                Line((10.329682699, 18.8632662067), (10.1711659278, 19.0033938155))
                Line((10.329682699, 18.8632662067), (11.1050299982, 22.5494200344))
                Line((10.8220364425, 22.0977604835), (11.1050299982, 22.5494200344))
            make_face()
            # Profile area: 0.2249605018, perimeter: 2.7163859286
            with BuildLine():
                Line((9.236638883, 19.5674556933), (9.3423054078, 19.7361001523))
                Line((10.1246877344, 18.7824273261), (9.236638883, 19.5674556933))
                Line((10.1246877344, 18.7824273261), (10.1711659278, 19.0033938155))
                Line((10.1711659278, 19.0033938155), (9.3423054078, 19.7361001523))
            make_face()
            # Profile area: 0.3752729636, perimeter: 4.6855094026
            with BuildLine():
                Line((9.3199805371, 14.0629431867), (9.7457230942, 16.0870071877))
                Line((9.6092298732, 16.3318390932), (9.7457230942, 16.0870071877))
                Line((9.1951984818, 14.3634522814), (9.6092298732, 16.3318390932))
                Line((9.3199805371, 14.0629431867), (9.1951984818, 14.3634522814))
            make_face()
            # Profile area: 0.050844672, perimeter: 1.2218167221
            with BuildLine():
                Line((10.9634214125, 14.2097789578), (11.1290429798, 13.9126986809))
                Line((10.9427941606, 13.939785605), (10.9634214125, 14.2097789578))
                Line((10.9427941606, 13.939785605), (11.1084157278, 13.6427053282))
                Line((11.1084157278, 13.6427053282), (11.1290429798, 13.9126986809))
            make_face()
            # Profile area: 0.610116458, perimeter: 7.2533981526
            with BuildLine():
                Line((10.9427941606, 13.939785605), (11.1084157278, 13.6427053282))
                Line((10.6985589079, 10.7429518856), (10.9427941606, 13.939785605))
                Line((10.8576128401, 10.359906799), (10.6985589079, 10.7429518856))
                Line((10.8576128401, 10.359906799), (11.1084157278, 13.6427053282))
            make_face()
            # Profile area: 0.829902295, perimeter: 9.716815739
            with BuildLine():
                Line((12.5309, 6.3301766561), (10.8576128401, 10.359906799))
                Line((10.8259097217, 9.9449396842), (10.8576128401, 10.359906799))
                Line((12.5309, 5.8388598177), (10.8259097217, 9.9449396842))
                Line((12.5309, 6.3301766561), (12.5309, 5.8388598177))
            make_face()
            # Profile area: 0.3634621898, perimeter: 5.3613536635
            with BuildLine():
                Line((9.7926071061, 16.3099030179), (10.9634214125, 14.2097789578))
                Line((9.7457230942, 16.0870071877), (9.7926071061, 16.3099030179))
                Line((9.7457230942, 16.0870071877), (10.9427941606, 13.939785605))
                Line((10.9427941606, 13.939785605), (10.9634214125, 14.2097789578))
            make_face()
            # Profile area: 0.0613075249, perimeter: 1.3172830394
            with BuildLine():
                Line((9.2513845187, 13.7368241996), (9.3199805371, 14.0629431867))
                Line((9.3199805371, 14.0629431867), (9.1951984818, 14.3634522814))
                Line((9.1266024633, 14.0373332943), (9.1951984818, 14.3634522814))
                Line((9.2513845187, 13.7368241996), (9.1266024633, 14.0373332943))
            make_face()
            # Profile area: 0.0462273132, perimeter: 0.9632762832
            with BuildLine():
                Line((11.4327639869, 17.8881508163), (11.2563594478, 18.0440910747))
                Line((11.237605419, 17.7986166365), (11.2563594478, 18.0440910747))
                Line((11.4140099582, 17.6426763781), (11.237605419, 17.7986166365))
                Line((11.4140099582, 17.6426763781), (11.4327639869, 17.8881508163))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


# Description: This is a solar panel or photovoltaic module with a rectangular flat plate body featuring a dark blue surface and an attached dark cylindrical connector or junction box protruding from one edge.
def model_37040_ecbcd25e_0035():
    """Model: zawias2 v1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2140209995, perimeter: 1.6399595115
            with BuildLine():
                CenterArc((0.075, -1.25), 0.2610076627, 106.699244234, 326.601511532)
                CenterArc((0.075, -1.25), 0.2610076627, 73.300755766, 33.398488468)
            make_face()
            # Profile area: 0.1488945059, perimeter: 2.3021449134
            with BuildLine():
                Line((0, -1), (0, 0))
                CenterArc((0.075, -1.25), 0.2610076627, 73.300755766, 33.398488468)
                Line((0.15, 0), (0.15, -1))
                Line((0, 0), (0.15, 0))
            make_face()
        # OneSide extrude, distance=3
        extrude(amount=3)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 7 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.2118100048, perimeter: 1.6356696717
            with BuildLine():
                Line((-0.0000000497, 1.4999999851), (0.1500000497, 1.4999999851))
                CenterArc((0.075, 1.25), 0.2610076627, 106.6992556176, 146.6014992084)
                Line((0.15, 1.0000000149), (0, 1.0000000149))
                CenterArc((0.075, 1.25), 0.2610076627, -73.3007548261, 146.6014992084)
            make_face()
            # Profile area: 0.0815949898, perimeter: 1.7678347201
            with BuildLine():
                CenterArc((0.075, 1.25), 0.2610076627, -73.3007548261, 146.6014992084)
                Line((0.4500000067, 1.0000000149), (0.15, 1.0000000149))
                Line((0.4500000067, 1.4999999851), (0.4500000067, 1.0000000149))
                Line((0.1500000497, 1.4999999851), (0.4500000067, 1.4999999851))
            make_face()
            # Profile area: 0.0815949898, perimeter: 1.7678347201
            with BuildLine():
                Line((-0.3000000067, 1.4999999851), (-0.0000000497, 1.4999999851))
                Line((-0.3000000067, 1.0000000149), (-0.3000000067, 1.4999999851))
                Line((0, 1.0000000149), (-0.3000000067, 1.0000000149))
                CenterArc((0.075, 1.25), 0.2610076627, 106.6992556176, 146.6014992084)
            make_face()
        # OneSide extrude, distance=-1.5
        extrude(amount=-1.5, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a hydraulic or pneumatic cylinder with a dark blue barrel body, threaded ports at both ends, and a rod extending from the bottom, designed for linear motion applications.
def model_37117_89aac9d4_0004():
    """Model: arm_noodles"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.3166921744, perimeter: 1.994911335
            with Locations((3.9384494537, -5.060330129)):
                Circle(0.3175)
        # OneSide extrude, distance=0.635
        extrude(amount=0.635)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.635, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.4736288256, perimeter: 5.550911335
            with BuildLine():
                Line((-4.3829494537, 5.504830129), (-4.3829494537, 4.615830129))
                Line((-4.3829494537, 4.615830129), (-3.4939494537, 4.615830129))
                Line((-3.4939494537, 4.615830129), (-3.4939494537, 5.504830129))
                Line((-3.4939494537, 5.504830129), (-4.3829494537, 5.504830129))
            make_face()
            with BuildLine():
                CenterArc((-3.9384494537, 5.060330129), 0.3175, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.3166921744, perimeter: 1.994911335
            with Locations((-3.9384494537, 5.060330129)):
                Circle(0.3175)
        # OneSide extrude, distance=8.89
        extrude(amount=8.89, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 9.525, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.3166921744, perimeter: 1.994911335
            with Locations((-3.9384494537, 5.060330129)):
                Circle(0.3175)
        # OneSide extrude, distance=0.635
        extrude(amount=0.635, mode=Mode.ADD)
    return part.part


# Description: This is a closed-loop conveyor or drive belt with an elliptical/oval shape, featuring a textured ribbed surface on both the inner and outer edges for grip and traction.
def model_37377_90529181_0005():
    """Model: obrecz kola v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 9.3933620342, perimeter: 187.8672406847
            with BuildLine():
                CenterArc((-5, 2.5), 15, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-5, 2.5), 14.9, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=2.7
        extrude(amount=2.7)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2.7, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 23.2085157284, perimeter: 185.6681258272
            with BuildLine():
                CenterArc((5, -2.5), 14.9, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((5, -2.5), 14.65, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 23.2085157284, perimeter: 185.6681258272
            with BuildLine():
                CenterArc((-5, -2.5), 14.9, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-5, -2.5), 14.65, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2, mode=Mode.ADD)
    return part.part


# Description: This is a horizontal mounting bracket or channel with an elongated rectangular profile, featuring a central slot or groove running its length, rounded end caps on both sides, and what appears to be mounting holes or attachment points along its surface.
def model_37517_f894f8bd_0001():
    """Model: Component3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0209817477, perimeter: 1.1141592654
            with BuildLine():
                CenterArc((0.4, -0.025), 0.025, -90, 180)
                Line((0, 0), (0.4, 0))
                CenterArc((0, -0.025), 0.025, 90, 180)
                Line((0.4, -0.05), (0, -0.05))
            make_face()
            with BuildLine():
                CenterArc((0.35, -0.025), 0.0125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0.4, -0.025), 0.0125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.025
        extrude(amount=0.025)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.025, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0031400227, perimeter: 0.2823427023
            with BuildLine():
                CenterArc((-0.1, 0.0252), 0.0132, 75.8588897661, 194.1411102339)
                Line((-0.1, 0.012), (0, 0.012))
                CenterArc((0, 0.025), 0.013, -90, 180)
                Line((-0.0967750969, 0.038), (0, 0.038))
            make_face()
        # OneSide extrude, distance=-0.009
        extrude(amount=-0.009, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.0031309292, perimeter: 0.281681409
            with BuildLine():
                CenterArc((0.1, 0.025), 0.013, -90, 180)
                Line((0.1, 0.038), (0, 0.038))
                CenterArc((0, 0.025), 0.013, 90, 180)
                Line((0.1, 0.012), (0, 0.012))
            make_face()
        # OneSide extrude, distance=-0.009
        extrude(amount=-0.009, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical suppressor or silencer tube with a elongated tubular body, featuring two small mounting holes or slots near the tapered bottom end for attachment purposes.
def model_37517_f894f8bd_0004():
    """Model: Component5"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0019634954, perimeter: 0.1570796327
            Circle(0.025)
        # OneSide extrude, distance=0.4
        extrude(amount=0.4)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on YZ construction plane
        # Sketch has 5 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.001875, perimeter: 0.2
            with BuildLine():
                Line((-0.0125, 0.075), (-0.0125, 0))
                Line((-0.0125, 0), (0.0125, 0))
                Line((0.0125, 0), (0.0125, 0.075))
                Line((0.0125, 0.075), (-0.0125, 0.075))
            make_face()
        # TwoSides extrude (symmetric), distance=0.1
        extrude(amount=0.1, both=True, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0004908739, perimeter: 0.0785398163
            with Locations((0, 0.025)):
                Circle(0.0125)
        # TwoSides extrude (symmetric), distance=0.1
        extrude(amount=0.1, both=True, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical spacer or sleeve with a knurled hexagonal flange at the top and vertical ribbing along its body, designed for fastening or alignment purposes in an assembly.
def model_37517_f894f8bd_0013():
    """Model: Component9"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0030679616, perimeter: 0.1963495408
            Circle(0.03125)
        # OneSide extrude, distance=0.1125
        extrude(amount=0.1125)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.1125, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0013499031, perimeter: 0.4319689899
            with BuildLine():
                CenterArc((0, 0), 0.0375, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.03125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0030679616, perimeter: 0.1963495408
            Circle(0.03125)
        # OneSide extrude, distance=0.0125
        extrude(amount=0.0125, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.0019634954, perimeter: 0.1570796327
            Circle(0.025)
        # OneSide extrude, distance=-0.15
        extrude(amount=-0.15, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a circular impeller or fan wheel with a flat face featuring multiple radial slots or vanes, a central hub, and a perforated or mesh-textured curved outer rim.
def model_37605_e35cc4df_0008():
    """Model: kolo"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 18.8495559215, perimeter: 18.8495559215
            with BuildLine():
                CenterArc((1.0000000149, 1.0000000149), 2.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((1.0000000149, 1.0000000149), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=2
        extrude(amount=2)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 32 constraints, 16 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 2), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.3142958784, perimeter: 3.5108205302
            with BuildLine():
                CenterArc((-1.0999999851, 1.0867218288), 0.1, 82.8749836511, 97.1250163489)
                Line((-1.1999999851, 1.0867218288), (-1.1999999851, 0.9132782666))
                CenterArc((-1.0999999851, 0.9132782666), 0.1, 180, 97.1250163489)
                Line((-1.0875965116, 0.8140504789), (0.4000000387, 1.0000000477))
                Line((-1.0875965116, 1.1859496165), (0.4000000387, 1.0000000477))
            make_face()
            # Profile area: 0.3142958784, perimeter: 3.5108205302
            with BuildLine():
                CenterArc((-0.4943133442, 2.554214826), 0.1, 37.8749836511, 97.1250163489)
                Line((-0.5650240223, 2.6249255041), (-0.6876671413, 2.5022823851))
                CenterArc((-0.6169564632, 2.431571707), 0.1, 135, 97.1250163489)
                Line((-0.6783505246, 2.3526364852), (0.5050252849, 1.4322330779))
                Line((-0.4153781225, 2.6156088874), (0.5050252849, 1.4322330779))
            make_face()
            # Profile area: 0.3142958784, perimeter: 3.5108205302
            with BuildLine():
                CenterArc((1.086721796, 3.1000000477), 0.1, -7.1250163489, 97.1250163489)
                Line((1.086721796, 3.2000000477), (0.9132782338, 3.2000000477))
                CenterArc((0.9132782338, 3.1000000477), 0.1, 90, 97.1250163489)
                Line((0.8140504461, 3.0875965742), (1.0000000149, 1.6000000238))
                Line((1.1859495837, 3.0875965742), (1.0000000149, 1.6000000238))
            make_face()
            # Profile area: 0.3142958784, perimeter: 3.5108205302
            with BuildLine():
                CenterArc((2.58056039, 2.3608610289), 0.1, -52.1250163489, 97.1250163489)
                Line((2.6512710681, 2.431571707), (2.5286279491, 2.554214826))
                CenterArc((2.4579172709, 2.4835041479), 0.1, 45, 97.1250163489)
                Line((2.3789820492, 2.5448982092), (1.4585786418, 1.3615223997))
                Line((2.6419544513, 2.2819258071), (1.4585786418, 1.3615223997))
            make_face()
            # Profile area: 0.3142958784, perimeter: 3.5108205302
            with BuildLine():
                CenterArc((3.1000000149, 0.9132782666), 0.1, -97.1250163489, 97.1250163489)
                Line((3.2000000149, 0.9132782666), (3.2000000149, 1.0867218288))
                CenterArc((3.1000000149, 1.0867218288), 0.1, 0, 97.1250163489)
                Line((3.0875965414, 1.1859496165), (1.5999999911, 1.0000000477))
                Line((3.0875965414, 0.8140504789), (1.5999999911, 1.0000000477))
            make_face()
            # Profile area: 0.3142958784, perimeter: 3.5108205302
            with BuildLine():
                CenterArc((2.4336532022, -0.5634030398), 0.1, -142.1250163489, 97.1250163489)
                Line((2.5043638803, -0.634113718), (2.6270069994, -0.5114705989))
                CenterArc((2.5562963212, -0.4407599208), 0.1, -45, 97.1250163489)
                Line((2.6176903826, -0.3618246991), (1.4343145731, 0.5585787083))
                Line((2.3547179805, -0.6247971012), (1.4343145731, 0.5585787083))
            make_face()
            # Profile area: 0.3142958784, perimeter: 3.5108205302
            with BuildLine():
                CenterArc((0.9132782338, -1.0999999523), 0.1, 172.8749836511, 97.1250163489)
                Line((0.9132782338, -1.1999999523), (1.086721796, -1.1999999523))
                CenterArc((1.086721796, -1.0999999523), 0.1, -90, 97.1250163489)
                Line((1.1859495837, -1.0875964789), (1.0000000149, 0.4000000715))
                Line((0.8140504461, -1.0875964789), (1.0000000149, 0.4000000715))
            make_face()
            # Profile area: 0.3142958784, perimeter: 3.5108205302
            with BuildLine():
                CenterArc((-0.5462457851, -0.4750744959), 0.1, 127.8749836511, 97.1250163489)
                Line((-0.6169564632, -0.545785174), (-0.4943133442, -0.668428293))
                CenterArc((-0.4236026661, -0.5977176149), 0.1, -135, 97.1250163489)
                Line((-0.3446674443, -0.6591116762), (0.575735963, 0.5242641333))
                Line((-0.6076398465, -0.3961392741), (0.575735963, 0.5242641333))
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 2.3561944902, perimeter: 9.4247779608
            with BuildLine():
                CenterArc((-1.0000000149, 1.0000000149), 1, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-1.0000000149, 1.0000000149), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a long shaft or rod with a hexagonal or polygonal head on one end and a tapered or beveled point on the opposite end, featuring a straight cylindrical body with minimal features.
def model_37605_e35cc4df_0014():
    """Model: spych"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            with Locations((-54.0000008047, 6.6000000983)):
                Circle(0.3)
        # OneSide extrude, distance=9
        extrude(amount=9)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 9), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.158557395, perimeter: 2.5103613041
            with BuildLine():
                Line((-54.0052268958, 6.8999545748), (-54.5000008121, 6.8999545748))
                Line((-54.5000008121, 6.8999545748), (-54.5000008121, 6.3000000939))
                Line((-54.5000008121, 6.3000000939), (-54.010808925, 6.300194854))
                CenterArc((-54.0000008047, 6.6000000983), 0.3, 90.9981603687, 176.9371939038)
            make_face()
        # OneSide extrude, distance=-0.6
        extrude(amount=-0.6, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.158557395, perimeter: 2.5103613041
            with BuildLine():
                Line((54.010808925, 6.300194854), (54.5000008121, 6.3000000939))
                Line((54.5000008121, 6.3000000939), (54.5000008121, 6.8999545748))
                Line((54.5000008121, 6.8999545748), (54.0052268958, 6.8999545748))
                CenterArc((54.0000008047, 6.6000000983), 0.3, -87.9353542725, 176.9371939038)
            make_face()
        # OneSide extrude, distance=-0.6
        extrude(amount=-0.6, mode=Mode.ADD)
    return part.part


# Description: This is a socket head cap screw featuring a cylindrical shaft with a hexagonal socket in the head and a threaded tip for fastening applications.
def model_37615_8399c412_0007():
    """Model: Component10"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.3848451001, perimeter: 2.1991148575
            Circle(0.35)
        # OneSide extrude, distance=3.4
        extrude(amount=3.4)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 3.4, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.7461282552, perimeter: 5.9690260418
            with BuildLine():
                CenterArc((0, 0), 0.6, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.35, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.3848451001, perimeter: 2.1991148575
            Circle(0.35)
        # OneSide extrude, distance=0.8
        extrude(amount=0.8, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 4.2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1795301452, perimeter: 2.6819629748
            with BuildLine():
                Line((0.595294045, -0.075), (-0.595294045, -0.075))
                CenterArc((0, 0), 0.6, -7.1807557815, 14.3615115629)
                Line((-0.595294045, 0.075), (0.595294045, 0.075))
                CenterArc((0, 0), 0.6, 172.8192442185, 14.3615115629)
            make_face()
        # OneSide extrude, distance=-0.15
        extrude(amount=-0.15, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical fastener or bolt with a square or rectangular head at the top, featuring a threaded or textured surface on the head and a smooth shaft below.
def model_37846_cde34fcd_0012():
    """Model: M2.5x8 v2 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0490873852, perimeter: 0.7853981634
            Circle(0.125)
        # OneSide extrude, distance=0.8
        extrude(amount=0.8)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.8, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1099557429, perimeter: 2.1991148575
            with BuildLine():
                CenterArc((0, 0), 0.225, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0490873852, perimeter: 0.7853981634
            Circle(0.125)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0233187696, perimeter: 0.9979903411
            with BuildLine():
                CenterArc((0, 0), 0.225, -95.6779884143, 13.2583491127)
                Line((0.0296812402, -0.2230336835), (0.0296812402, 0.2230336835))
                CenterArc((0, 0), 0.225, 82.4196393016, 13.2583491127)
                Line((-0.0222609301, -0.2238960718), (-0.0222609301, 0.2238960718))
            make_face()
        # OneSide extrude, distance=-0.1
        extrude(amount=-0.1, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical connector or coupling with a flanged head, featuring a long hollow shaft and a wider, textured cap at the top with angular cutouts or slots for gripping or alignment purposes.
def model_37846_cde34fcd_0035():
    """Model: M3x6 v2 (3)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            Circle(0.15)
        # OneSide extrude, distance=0.6
        extrude(amount=0.6)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.6, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2120575041, perimeter: 2.8274333882
            with BuildLine():
                CenterArc((0, 0), 0.3, 0, 360)
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
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.8, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0355592949, perimeter: 1.3130318945
            with BuildLine():
                Line((-0.0296812402, -0.2985280958), (-0.0296812402, 0.2985280958))
                CenterArc((0, 0), 0.3, -95.6779884143, 11.3559768286)
                Line((0.0296812402, -0.2985280958), (0.0296812402, 0.2985280958))
                CenterArc((0, 0), 0.3, 84.3220115857, 11.3559768286)
            make_face()
        # OneSide extrude, distance=-0.1
        extrude(amount=-0.1, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical connector or coupling with an angled flange head, featuring a hollow tubular body with a perpendicular flat-faced collar at the top that has slot or groove details.
def model_37846_cde34fcd_0060():
    """Model: M3x4 v4"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            Circle(0.15)
        # OneSide extrude, distance=0.4
        extrude(amount=0.4)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.4, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2120575041, perimeter: 2.8274333882
            with BuildLine():
                CenterArc((0, 0), 0.3, 0, 360)
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
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.6, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0355592949, perimeter: 1.3130318945
            with BuildLine():
                Line((-0.0296812402, -0.2985280958), (-0.0296812402, 0.2985280958))
                CenterArc((0, 0), 0.3, -95.6779884143, 11.3559768286)
                Line((0.0296812402, -0.2985280958), (0.0296812402, 0.2985280958))
                CenterArc((0, 0), 0.3, 84.3220115857, 11.3559768286)
            make_face()
        # OneSide extrude, distance=-0.1
        extrude(amount=-0.1, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a rectangular enclosure or chassis base plate with a trapezoidal top surface, featuring internal ribbing/bracing structures and mounting points at the corners and edges for assembly purposes.
def model_38196_ea48fa42_0006():
    """Model: Table"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.22, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 14.525, perimeter: 15.3
            with BuildLine():
                Line((-1.75, 1.825), (1.75, 1.825))
                Line((-1.75, -2.325), (-1.75, 1.825))
                Line((1.75, -2.325), (-1.75, -2.325))
                Line((1.75, 1.825), (1.75, -2.325))
            make_face()
            # Profile area: 1.225, perimeter: 7.7
            with BuildLine():
                Line((-1.75, -2.675), (-1.75, -2.325))
                Line((1.75, -2.675), (-1.75, -2.675))
                Line((1.75, -2.325), (1.75, -2.675))
                Line((1.75, -2.325), (-1.75, -2.325))
            make_face()
        # OneSide extrude, distance=0.425
        extrude(amount=0.425)

        # Sketch5 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 17 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.645, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0542971263, perimeter: 1.1684513021
            with BuildLine():
                Line((0, 1.825), (-0.19, 1.825))
                Line((-0.19, 1.39), (-0.19, 1.825))
                CenterArc((0, 1.39), 0.19, 90, 90)
                Line((0, 1.825), (0, 1.58))
            make_face()
            # Profile area: 0.0542971263, perimeter: 1.1684513021
            with BuildLine():
                Line((0, 1.825), (0, 1.58))
                CenterArc((0, 1.39), 0.19, 0, 90)
                Line((0.19, 1.39), (0.19, 1.825))
                Line((0.19, 1.825), (0, 1.825))
            make_face()
        # OneSide extrude, distance=-0.24
        extrude(amount=-0.24, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 17 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.645, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0056431051, perimeter: 0.5134539792
            with BuildLine():
                Line((0.19, -2.5), (0.19, -2.675))
                CenterArc((0, -2.5), 0.19, -67.0804578484, 67.0804578484)
                Line((0.0739932429, -2.675), (0.19, -2.675))
            make_face()
            # Profile area: 0.0056431051, perimeter: 0.5134539792
            with BuildLine():
                CenterArc((0, -2.5), 0.19, 180, 67.0804578484)
                Line((-0.19, -2.5), (-0.19, -2.675))
                Line((-0.19, -2.675), (-0.0739932429, -2.675))
            make_face()
        # OneSide extrude, distance=-0.24
        extrude(amount=-0.24, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical shaft or connector with a stepped diameter design, featuring a smaller diameter section on the left transitioning to a larger diameter section on the right, with a tapered or beveled transition between them.
def model_38196_ea48fa42_0012():
    """Model: Mitutoyo"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.096211275, perimeter: 1.0995574288
            Circle(0.175)
        # OneSide extrude, distance=0.756
        extrude(amount=0.756)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.756), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.1865320638, perimeter: 2.9845130209
            with BuildLine():
                CenterArc((0, 0), 0.3, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.175, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.096211275, perimeter: 1.0995574288
            Circle(0.175)
        # OneSide extrude, distance=0.7
        extrude(amount=0.7, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1.456), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0289811922, perimeter: 3.8641589639
            with BuildLine():
                CenterArc((0, 0), 0.315, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            Circle(0.3)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1, mode=Mode.ADD)
    return part.part


# Description: This is a elongated cylindrical rod or shaft with rounded ends and a smooth, curved profile, featuring two small holes or slots on its top surface.
def model_38484_56f24230_0001():
    """Model: BOLT_wheel_back_left"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            Circle(0.5)
        # OneSide extrude, distance=0.4
        extrude(amount=0.4)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.4, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            Circle(0.3)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0.7, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.5026548246, perimeter: 5.0265482457
            with BuildLine():
                CenterArc((0, 0), 0.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            Circle(0.3)
        # OneSide extrude, distance=5.3
        extrude(amount=5.3, mode=Mode.ADD)
    return part.part


# Description: This is a dumbbell consisting of two cylindrical weight plates connected by a shorter cylindrical bar handle in the middle, featuring a symmetric hourglass-like profile with textured grip surfaces on the plates.
def model_39197_8f65b459_0000():
    """Model: coil"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))) as sk:
            # Profile area: 4.573563142, perimeter: 7.5811008086
            Circle(1.2065696678)
        # TwoSides extrude, along=15.5, against=-1
        extrude(amount=15.5)
        extrude(sk.sketch, amount=-1)

        # Sketch3 -> Extrude2 (NewBody)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(15.5, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 27.6277615573, perimeter: 27.6971088729
            with BuildLine():
                CenterArc((0, 0), 3.2015621187, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.2065696678, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=4.5
        extrude(amount=4.5)

        # Sketch4 -> Extrude3 (NewBody)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(-1, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 27.6277615573, perimeter: 27.6971088729
            with BuildLine():
                CenterArc((0, 0), 3.2015621187, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.2065696678, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=4.5
        extrude(amount=4.5)
    return part.part


# Description: This is a disc brake rotor with an oval/elliptical shape, featuring a flat friction surface with radial cooling fins on the top face and a curved underside, designed for automotive braking applications.
def model_39306_ee445998_0002():
    """Model: Wheel v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 12.5663706144, perimeter: 12.5663706144
            Circle(2)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 0.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0706858368, perimeter: 0.9424778101
            with Locations((-1.5000000224, 0)):
                Circle(0.1500000022)
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.0549778731, perimeter: 2.1991148903
            with BuildLine():
                CenterArc((1.5000000224, 0), 0.200000003, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((1.5000000224, 0), 0.1500000022, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.1
        extrude(amount=-0.1, mode=Mode.SUBTRACT)
    return part.part


MODELS = {
    "model_31280_c8bd4b11_0010": {"func": model_31280_c8bd4b11_0010, "volume": 4.2160212929, "area": 18.4026905833},
    "model_31360_a1accb4b_0008": {"func": model_31360_a1accb4b_0008, "volume": 0.5293329717, "area": 8.1235619614},
    "model_31462_84375249_0005": {"func": model_31462_84375249_0005, "volume": 0.0354299806, "area": 1.0969455839},
    "model_31645_11901b20_0000": {"func": model_31645_11901b20_0000, "volume": 240.5696201543, "area": 942.9781304551},
    "model_31751_e37382e1_0003": {"func": model_31751_e37382e1_0003, "volume": 0.0008325754, "area": 0.1105141567},
    "model_31962_e5291336_0001": {"func": model_31962_e5291336_0001, "volume": 20.2035886499, "area": 63.0361938873},
    "model_31962_e5291336_0002": {"func": model_31962_e5291336_0002, "volume": 0.2059535778, "area": 2.7150875254},
    "model_31962_e5291336_0005": {"func": model_31962_e5291336_0005, "volume": 0.184095104, "area": 2.6976835203},
    "model_31962_e5291336_0008": {"func": model_31962_e5291336_0008, "volume": 0.2092278452, "area": 2.9490109326},
    "model_31962_e5291336_0009": {"func": model_31962_e5291336_0009, "volume": 1.8661060362, "area": 12.7705741368},
    "model_31962_e5291336_0010": {"func": model_31962_e5291336_0010, "volume": 1.9155861205, "area": 11.5453530019},
    "model_31962_e5291336_0018": {"func": model_31962_e5291336_0018, "volume": 0.5563151325, "area": 5.3990435406},
    "model_31962_e5291336_0019": {"func": model_31962_e5291336_0019, "volume": 0.231086319, "area": 2.9664149376},
    "model_31962_e5291336_0020": {"func": model_31962_e5291336_0020, "volume": 4.8890747271, "area": 28.4525520687},
    "model_31962_e5291336_0039": {"func": model_31962_e5291336_0039, "volume": 2.7951804331, "area": 18.6004591138},
    "model_31962_e5291336_0040": {"func": model_31962_e5291336_0040, "volume": 0.3861213721, "area": 4.5317474028},
    "model_31962_e5291336_0041": {"func": model_31962_e5291336_0041, "volume": 1.6422319811, "area": 11.3163308975},
    "model_31962_e5291336_0042": {"func": model_31962_e5291336_0042, "volume": 0.4959618496, "area": 4.6668019614},
    "model_31962_e5291336_0045": {"func": model_31962_e5291336_0045, "volume": 1.5071790756, "area": 13.2418130349},
    "model_31962_e5291336_0054": {"func": model_31962_e5291336_0054, "volume": 0.2022542479, "area": 3.0863303658},
    "model_32219_e5edc7ce_0040": {"func": model_32219_e5edc7ce_0040, "volume": 6.8329640216, "area": 58.7477826221},
    "model_32219_e5edc7ce_0042": {"func": model_32219_e5edc7ce_0042, "volume": 166.897109722, "area": 172.7875959474},
    "model_32219_e5edc7ce_0044": {"func": model_32219_e5edc7ce_0044, "volume": 8.4273222933, "area": 32.5311919279},
    "model_32219_e5edc7ce_0049": {"func": model_32219_e5edc7ce_0049, "volume": 0.1606954115, "area": 3.046300939},
    "model_32220_1fd19c5e_0020": {"func": model_32220_1fd19c5e_0020, "volume": 0.143479929, "area": 3.572378383},
    "model_32461_378772c5_0000": {"func": model_32461_378772c5_0000, "volume": 465.5370584994, "area": 574.0131732767},
    "model_32666_4baa4ef5_0000": {"func": model_32666_4baa4ef5_0000, "volume": 247.0806775358, "area": 274.1588280979},
    "model_32871_04ff3d41_0010": {"func": model_32871_04ff3d41_0010, "volume": 2.1598199193, "area": 13.0124697829},
    "model_33147_d7173b68_0009": {"func": model_33147_d7173b68_0009, "volume": 0.0200276979, "area": 0.6303502556},
    "model_33147_d7173b68_0010": {"func": model_33147_d7173b68_0010, "volume": 0.0028366938, "area": 0.146450832},
    "model_33147_d7173b68_0017": {"func": model_33147_d7173b68_0017, "volume": 0.0859194809, "area": 1.5119445273},
    "model_33147_d7173b68_0019": {"func": model_33147_d7173b68_0019, "volume": 0.0682986973, "area": 1.5023778672},
    "model_33625_c9ff9be8_0001": {"func": model_33625_c9ff9be8_0001, "volume": 3.4602905343, "area": 29.5021728276},
    "model_33625_c9ff9be8_0004": {"func": model_33625_c9ff9be8_0004, "volume": 1160.1624028172, "area": 1706.7147229153},
    "model_33655_f8991a06_0002": {"func": model_33655_f8991a06_0002, "volume": 4.9278562615, "area": 54.9087342297},
    "model_33655_f8991a06_0004": {"func": model_33655_f8991a06_0004, "volume": 0.3536047368, "area": 4.7079644737},
    "model_34063_0ca1585e_0004": {"func": model_34063_0ca1585e_0004, "volume": 7.980074415, "area": 52.3868371107},
    "model_34063_0ca1585e_0012": {"func": model_34063_0ca1585e_0012, "volume": 1.7018458644, "area": 12.3850750006},
    "model_34231_e27353cb_0000": {"func": model_34231_e27353cb_0000, "volume": 150, "area": 260},
    "model_34317_e9c65aa6_0020": {"func": model_34317_e9c65aa6_0020, "volume": 2340.366336, "area": 1851.48736},
    "model_34330_5eff1ee1_0000": {"func": model_34330_5eff1ee1_0000, "volume": 0.0000560578, "area": 0.0109563044},
    "model_34330_5eff1ee1_0009": {"func": model_34330_5eff1ee1_0009, "volume": 0.0000437859, "area": 0.008992809},
    "model_34570_2041f80b_0002": {"func": model_34570_2041f80b_0002, "volume": 2.1863225027, "area": 13.0669245813},
    "model_34678_f709cdcc_0004": {"func": model_34678_f709cdcc_0004, "volume": 0.0724529806, "area": 1.2262028826},
    "model_34678_f709cdcc_0006": {"func": model_34678_f709cdcc_0006, "volume": 0.1386517574, "area": 2.3563154975},
    "model_34708_7559c801_0001": {"func": model_34708_7559c801_0001, "volume": 9962907.5644894, "area": 376866.0719701822},
    "model_34710_08cd9b5c_0004": {"func": model_34710_08cd9b5c_0004, "volume": 2816.8305130249, "area": 1801.7033868337},
    "model_34769_44655d03_0002": {"func": model_34769_44655d03_0002, "volume": 3.3854310074, "area": 35.7458443503},
    "model_34769_44655d03_0004": {"func": model_34769_44655d03_0004, "volume": 0.3290818305, "area": 4.8537606498},
    "model_34769_44655d03_0006": {"func": model_34769_44655d03_0006, "volume": 0.0522289779, "area": 1.8849555922},
    "model_34769_44655d03_0007": {"func": model_34769_44655d03_0007, "volume": 1.9388157745, "area": 14.5797096399},
    "model_34782_b461066c_0001": {"func": model_34782_b461066c_0001, "volume": 9808.4042652522, "area": 10595.2531009701},
    "model_35149_f50fea8a_0006": {"func": model_35149_f50fea8a_0006, "volume": 0.0008540113, "area": 0.1578060717},
    "model_35166_562b126c_0001": {"func": model_35166_562b126c_0001, "volume": 0.3391447444, "area": 5.6558485242},
    "model_35962_dbbd6e18_0005": {"func": model_35962_dbbd6e18_0005, "volume": 55.0931000787, "area": 149.0579815325},
    "model_36088_1ea9c8a9_0004": {"func": model_36088_1ea9c8a9_0004, "volume": 0.7938019237, "area": 11.9443352689},
    "model_36088_1ea9c8a9_0012": {"func": model_36088_1ea9c8a9_0012, "volume": 0.9224501429, "area": 13.6596448578},
    "model_36163_04339590_0000": {"func": model_36163_04339590_0000, "volume": 0.4481141537, "area": 10.6922277384},
    "model_36182_1c8d16f4_0004": {"func": model_36182_1c8d16f4_0004, "volume": 23264, "area": 18128},
    "model_36194_c9cfd107_0009": {"func": model_36194_c9cfd107_0009, "volume": 0.0000986184, "area": 0.015818939},
    "model_36436_362a4413_0000": {"func": model_36436_362a4413_0000, "volume": 0.2529950545, "area": 2.9249191453},
    "model_36436_362a4413_0006": {"func": model_36436_362a4413_0006, "volume": 11.1031415927, "area": 146.2268140899},
    "model_36436_362a4413_0025": {"func": model_36436_362a4413_0025, "volume": 0.3535009913, "area": 3.9296069762},
    "model_36436_362a4413_0033": {"func": model_36436_362a4413_0033, "volume": 0.2404286525, "area": 2.7992554763},
    "model_36665_6cd225dd_0005": {"func": model_36665_6cd225dd_0005, "volume": 116.7023893421, "area": 264.5477868423},
    "model_36667_6c4f7023_0000": {"func": model_36667_6c4f7023_0000, "volume": 266.0017850378, "area": 389.0113975966},
    "model_37040_ecbcd25e_0003": {"func": model_37040_ecbcd25e_0003, "volume": 436.0526617456, "area": 1185.2814801879},
    "model_37040_ecbcd25e_0010": {"func": model_37040_ecbcd25e_0010, "volume": 2.4, "area": 20},
    "model_37040_ecbcd25e_0022": {"func": model_37040_ecbcd25e_0022, "volume": 172.1046410602, "area": 557.3177803392},
    "model_37040_ecbcd25e_0031": {"func": model_37040_ecbcd25e_0031, "volume": 9.8235599218, "area": 146.6965566487},
    "model_37040_ecbcd25e_0035": {"func": model_37040_ecbcd25e_0035, "volume": 0.7710315026, "area": 10.0857706209},
    "model_37117_89aac9d4_0004": {"func": model_37117_89aac9d4_0004, "volume": 7.4281527515, "area": 35.7270193955},
    "model_37377_90529181_0005": {"func": model_37377_90529181_0005, "volume": 34.6454837838, "area": 618.2340182999},
    "model_37517_f894f8bd_0001": {"func": model_37517_f894f8bd_0001, "volume": 0.0004681051, "area": 0.074893694},
    "model_37517_f894f8bd_0004": {"func": model_37517_f894f8bd_0004, "volume": 0.0006842839, "area": 0.0690316524},
    "model_37517_f894f8bd_0013": {"func": model_37517_f894f8bd_0013, "volume": 0.0001549321, "area": 0.0495782591},
    "model_37605_e35cc4df_0008": {"func": model_37605_e35cc4df_0008, "volume": 37.0238880034, "area": 82.5863328613},
    "model_37605_e35cc4df_0014": {"func": model_37605_e35cc4df_0014, "volume": 2.7349589234, "area": 18.9532917979},
    "model_37615_8399c412_0007": {"func": model_37615_8399c412_0007, "volume": 2.1863225027, "area": 13.0669245813},
    "model_37846_cde34fcd_0012": {"func": model_37846_cde34fcd_0012, "volume": 0.0687466568, "area": 1.3081209937},
    "model_37846_cde34fcd_0035": {"func": model_37846_cde34fcd_0035, "volume": 0.0954042391, "area": 1.6154837609},
    "model_37846_cde34fcd_0060": {"func": model_37846_cde34fcd_0060, "volume": 0.0812670722, "area": 1.4269882017},
    "model_38196_ea48fa42_0006": {"func": model_38196_ea48fa42_0006, "volume": 6.6649786889, "area": 38.6959480482},
    "model_38196_ea48fa42_0012": {"func": model_38196_ea48fa42_0012, "volume": 0.3018285142, "area": 2.9721037299},
    "model_38484_56f24230_0001": {"func": model_38484_56f24230_0001, "volume": 4.561592533, "area": 21.0486707791},
    "model_39197_8f65b459_0000": {"func": model_39197_8f65b459_0000, "volume": 324.1136458584, "area": 494.0203157116},
    "model_39306_ee445998_0002": {"func": model_39306_ee445998_0002, "volume": 6.2423446015, "area": 31.7772096943},
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
