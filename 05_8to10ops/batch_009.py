"""Batch 009 - passing/05_8to10ops
68 models bundled from Fusion360 Gallery reconstructions.
"""

from build123d import *
from build123d import Edge, BuildLine
from collections import Counter
from OCP.BRepBuilderAPI import BRepBuilderAPI_MakeEdge
from OCP.Geom import Geom_BSplineCurve
from OCP.TColStd import TColStd_Array1OfReal, TColStd_Array1OfInteger
from OCP.TColgp import TColgp_Array1OfPnt
from OCP.gp import gp_Pnt


# Description: A cylindrical mesh or perforated drum with a solid end cap and an open latticed side surface, appearing to be a filter or strainer component.
def model_52230_60438ea5_0003():
    """Model: knob"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 19.6349540849, perimeter: 15.7079632679
            with Locations((-25, 45)):
                Circle(2.5)
        # OneSide extrude, distance=4
        extrude(amount=4)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 7 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.0188481929, perimeter: 0.575675074
            with BuildLine():
                Line((24.900000371, 47.3999884901), (24.900000371, 47.4979992142))
                Line((25.0896070499, 47.3999884901), (24.900000371, 47.3999884901))
                Line((25.0896070499, 47.4983935992), (25.0896070499, 47.3999884901))
                CenterArc((25, 45), 2.5, 87.9459177152, 4.3465165503)
            make_face()
        # OneSide extrude, distance=-4
        extrude(amount=-4, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            with Locations((25, 45)):
                Circle(1)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -0.5), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((25, 45)):
                Circle(0.5)
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)
    return part.part


# Description: This is a bracket or mounting assembly with a roughly cubic/rectangular body featuring an internal cavity or channel, external flanges on opposing sides, and what appears to be mounting points or attachment features, designed for securing or housing a component within a larger assembly.
def model_52557_e6a00b06_0001():
    """Model: switch"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 15 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 23.7953981634, perimeter: 18.7415926536
            with BuildLine():
                CenterArc((-41.95, 3.05), 0.5, 180, 90)
                Line((-41.95, 2.55), (-38.05, 2.55))
                CenterArc((-38.05, 3.05), 0.5, -90, 90)
                Line((-37.55, 3.05), (-37.55, 6.95))
                CenterArc((-38.05, 6.95), 0.5, 0, 90)
                Line((-38.05, 7.45), (-41.95, 7.45))
                CenterArc((-41.95, 6.95), 0.5, 90, 90)
                Line((-42.45, 6.95), (-42.45, 3.05))
            make_face()
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(1.5, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 16, perimeter: 16
            with BuildLine():
                Line((-38, 3), (-42, 3))
                Line((-38, 7), (-38, 3))
                Line((-42, 7), (-38, 7))
                Line((-42, 3), (-42, 7))
            make_face()
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 15 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(1.5, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 5.15, perimeter: 39.4831853072
            with BuildLine():
                CenterArc((-42.2, 7.2), 0.5, 90, 90)
                Line((-42.7, 2.8), (-42.7, 7.2))
                CenterArc((-42.2, 2.8), 0.5, 180, 90)
                Line((-37.8, 2.3), (-42.2, 2.3))
                CenterArc((-37.8, 2.8), 0.5, -90, 90)
                Line((-37.3, 7.2), (-37.3, 2.8))
                CenterArc((-37.8, 7.2), 0.5, 0, 90)
                Line((-42.2, 7.7), (-37.8, 7.7))
            make_face()
            with BuildLine():
                CenterArc((-41.95, 6.95), 0.5, 90, 90)
                Line((-38.05, 7.45), (-41.95, 7.45))
                CenterArc((-38.05, 6.95), 0.5, 0, 90)
                Line((-37.55, 3.05), (-37.55, 6.95))
                CenterArc((-38.05, 3.05), 0.5, -90, 90)
                Line((-41.95, 2.55), (-38.05, 2.55))
                CenterArc((-41.95, 3.05), 0.5, 180, 90)
                Line((-42.45, 6.95), (-42.45, 3.05))
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 7.7953981634, perimeter: 34.7415926536
            with BuildLine():
                Line((-42.45, 6.95), (-42.45, 3.05))
                CenterArc((-41.95, 3.05), 0.5, 180, 90)
                Line((-41.95, 2.55), (-38.05, 2.55))
                CenterArc((-38.05, 3.05), 0.5, -90, 90)
                Line((-37.55, 3.05), (-37.55, 6.95))
                CenterArc((-38.05, 6.95), 0.5, 0, 90)
                Line((-38.05, 7.45), (-41.95, 7.45))
                CenterArc((-41.95, 6.95), 0.5, 90, 90)
            make_face()
            with BuildLine():
                Line((-42, 7), (-38, 7))
                Line((-38, 7), (-38, 3))
                Line((-38, 3), (-42, 3))
                Line((-42, 3), (-42, 7))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.5, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 2.5132741229, perimeter: 12.5663706144
            with BuildLine():
                CenterArc((-40, 5), 1.2, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-40, 5), 0.8, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.2
        extrude(amount=1.2, mode=Mode.ADD)
    return part.part


# Description: This is a blue anodized aluminum or composite housing/enclosure with a hexagonal or faceted geometric form, featuring a tapered design with multiple angular surfaces and what appears to be internal compartments or structural ribs.
def model_52557_e6a00b06_0002():
    """Model: Main housing"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 19 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 12.0581874002, perimeter: 122.340689839
            with BuildLine():
                CenterArc((7.0586088907, 15.5), 0.5, 7.1250163489, 82.8749836511)
                Line((7.0586088907, 16), (-7.0586088907, 16))
                CenterArc((-7.0586088907, 15.5), 0.5, 90, 82.8749836511)
                Line((-8.4224782909, 8.6201736729), (-7.5547478291, 15.5620173673))
                CenterArc((-3.4610889073, 8), 5, 172.8749836511, 14.2500326978)
                Line((-7.5547478291, 0.4379826327), (-8.4224782909, 7.3798263271))
                CenterArc((-7.0586088907, 0.5), 0.5, -172.8749836511, 82.8749836511)
                Line((-7.0586088907, 0), (7.0586088907, 0))
                CenterArc((7.0586088907, 0.5), 0.5, -90, 82.8749836511)
                Line((7.5547478291, 0.4379826327), (8.4224782909, 7.3798263271))
                CenterArc((3.4610889073, 8), 5, -7.1250163489, 14.2500326978)
                Line((7.5547478291, 15.5620173673), (8.4224782909, 8.6201736729))
            make_face()
            with BuildLine():
                Line((-7.3249997627, 15.8000002354), (7.324999771, 15.8000002354))
                Line((8.3000001237, 8), (7.324999771, 15.8000002354))
                Line((7.3250001095, 0.200000003), (8.3000001237, 8))
                Line((-7.3249997925, 0.200000003), (7.3250001095, 0.200000003))
                Line((-8.2999997921, 8), (-7.3249997925, 0.200000003))
                Line((-7.3249997627, 15.8000002354), (-8.2999997921, 8))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=41
        extrude(amount=41)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 15 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 16, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.1141848493, perimeter: 9.82644591
            with BuildLine():
                CenterArc((0.5, -1.5), 1, -180, 60)
                Line((0, -2.3660254038), (0, -1.75))
                Line((0, -1.75), (0, 1.75))
                Line((0, 1.75), (0, 2.3660254038))
                CenterArc((0.5, 1.5), 1, 120, 60)
                Line((-0.5, -1.5), (-0.5, 1.5))
            make_face()
            # Profile area: 4.2774078043, perimeter: 15.9208410124
            with BuildLine():
                CenterArc((0.5, -1.5), 1, -120, 30)
                Line((1, -2.5), (0.5, -2.5))
                CenterArc((1, -1.5), 1, -90, 90)
                Line((2, 1.5), (2, -1.5))
                CenterArc((1, 1.5), 1, 0, 90)
                Line((0.5, 2.5), (1, 2.5))
                CenterArc((0.5, 1.5), 1, 90, 30)
                Line((0, 1.75), (0, 2.3660254038))
                Line((1.5, 1.75), (0, 1.75))
                Line((1.5, -1.75), (1.5, 1.75))
                Line((0, -1.75), (1.5, -1.75))
                Line((0, -2.3660254038), (0, -1.75))
            make_face()
        # OneSide extrude, distance=0.3
        extrude(amount=0.3, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 16.3, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 6.3915926536, perimeter: 23.2831853072
            with BuildLine():
                Line((-0.5, 1.5), (-0.5, -1.5))
                CenterArc((0.5, -1.5), 1, 180, 90)
                Line((0.5, -2.5), (1, -2.5))
                CenterArc((1, -1.5), 1, -90, 90)
                Line((2, -1.5), (2, 1.5))
                CenterArc((1, 1.5), 1, 0, 90)
                Line((1, 2.5), (0.5, 2.5))
                CenterArc((0.5, 1.5), 1, 90, 90)
            make_face()
            with BuildLine():
                Line((0, 1.75), (1.5, 1.75))
                Line((1.5, 1.75), (1.5, -1.75))
                Line((1.5, -1.75), (0, -1.75))
                Line((0, -1.75), (0, 1.75))
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 5.25, perimeter: 10
            with BuildLine():
                Line((0, -1.75), (0, 1.75))
                Line((1.5, -1.75), (0, -1.75))
                Line((1.5, 1.75), (1.5, -1.75))
                Line((0, 1.75), (1.5, 1.75))
            make_face()
        # OneSide extrude, distance=0.3
        extrude(amount=0.3, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((3.5, 0)):
                Circle(0.15)
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((7.2, 0)):
                Circle(0.15)
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a rectangular base plate or mounting bracket with a trapezoidal profile, featuring a central rectangular boss or raised section on top and what appears to be a mounting hole or post, designed as a foundation or support component.
def model_52985_475fe7b2_0012():
    """Model: Foot (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 525, perimeter: 100
            with BuildLine():
                Line((-17.5, 7.5), (17.5, 7.5))
                Line((-17.5, -7.5), (-17.5, 7.5))
                Line((17.5, -7.5), (-17.5, -7.5))
                Line((17.5, 7.5), (17.5, -7.5))
            make_face()
        # OneSide extrude, distance=5
        extrude(amount=5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 8 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 78.5398163397, perimeter: 31.4159265359
            with BuildLine():
                CenterArc((10, 0), 5, 135, 180)
                CenterArc((10, 0), 5, -45, 180)
            make_face()
        # OneSide extrude, distance=6
        extrude(amount=6, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 7 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 11, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 29.1908909286, perimeter: 25.1182782678
            with BuildLine():
                Line((14.7754690554, -1.4815179042), (5.2245309446, -1.4815179042))
                CenterArc((10, 0), 5, -17.2357222545, 34.4714445091)
                Line((5.2245309446, 1.4815179042), (14.7754690554, 1.4815179042))
                CenterArc((10, 0), 5, 162.7642777455, 34.4714445091)
            make_face()
        # OneSide extrude, distance=-5
        extrude(amount=-5, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -1.4815179042), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 4.9087385212, perimeter: 7.853981634
            with Locations((-10, 8.5)):
                Circle(1.25)
        # Symmetric extrude, each_side=10
        extrude(amount=10, both=True, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a telescoping rod or tube assembly with a cylindrical main body and an adjustable upper section that can extend or retract, featuring a locking mechanism or collar in the middle where the two sections meet.
def model_52987_387431ac_0003():
    """Model: First step screw"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 23.7582944428, perimeter: 17.2787595947
            Circle(2.75)
        # OneSide extrude, distance=24.5
        extrude(amount=24.5)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 24.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 18.0327418316, perimeter: 25.7610597594
            with BuildLine():
                CenterArc((0, 0), 2.75, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.35, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-7.2
        extrude(amount=-7.2, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 14.6790916739, perimeter: 27.9601746169
            with BuildLine():
                CenterArc((0, 0), 2.75, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.7, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-15.6
        extrude(amount=-15.6, mode=Mode.SUBTRACT)

        # Sketch7 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, -0.0000000127), z_dir=(0, -1, 0))):
            # Profile area: 2.0106192983, perimeter: 5.0265482457
            Circle(0.8)
        # OneSide extrude, distance=-3.5
        extrude(amount=-3.5, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a tapered cylindrical pin or stylus with a pointed tip, featuring a gradually reducing diameter from a thicker rounded end to a sharp point.
def model_53075_6438cc56_0003():
    """Model: base back"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 13 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.92, perimeter: 19.2
            with BuildLine():
                Line((88.8, 11.2), (88.8, 13.8))
                Line((88.8, 13.8), (86.2, 13.8))
                Line((86.2, 13.8), (86.2, 11.2))
                Line((86.2, 11.2), (88.8, 11.2))
            make_face()
            with BuildLine():
                Line((86.4, 11.4), (88.6, 11.4))
                Line((86.4, 13.6), (86.4, 11.4))
                Line((88.6, 13.6), (86.4, 13.6))
                Line((88.6, 11.4), (88.6, 13.6))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=74
        extrude(amount=74)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 7 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 1.92, perimeter: 19.2
            with BuildLine():
                Line((-86.2, 11.2), (-88.8, 11.2))
                Line((-86.2, 13.8), (-86.2, 11.2))
                Line((-88.8, 13.8), (-86.2, 13.8))
                Line((-88.8, 11.2), (-88.8, 13.8))
            make_face()
            with BuildLine():
                Line((-86.4, 11.4), (-88.6, 11.4))
                Line((-88.6, 11.4), (-88.6, 13.6))
                Line((-88.6, 13.6), (-86.4, 13.6))
                Line((-86.4, 13.6), (-86.4, 11.4))
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 4.84, perimeter: 8.8
            with BuildLine():
                Line((-86.4, 13.6), (-86.4, 11.4))
                Line((-88.6, 13.6), (-86.4, 13.6))
                Line((-88.6, 11.4), (-88.6, 13.6))
                Line((-86.4, 11.4), (-88.6, 11.4))
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 7 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 74), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1.92, perimeter: 19.2
            with BuildLine():
                Line((88.8, 11.2), (86.2, 11.2))
                Line((88.8, 13.8), (88.8, 11.2))
                Line((86.2, 13.8), (88.8, 13.8))
                Line((86.2, 11.2), (86.2, 13.8))
            make_face()
            with BuildLine():
                Line((86.4, 13.6), (88.6, 13.6))
                Line((88.6, 13.6), (88.6, 11.4))
                Line((88.6, 11.4), (86.4, 11.4))
                Line((86.4, 11.4), (86.4, 13.6))
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 4.84, perimeter: 8.8
            with BuildLine():
                Line((86.4, 11.4), (86.4, 13.6))
                Line((88.6, 11.4), (86.4, 11.4))
                Line((88.6, 13.6), (88.6, 11.4))
                Line((86.4, 13.6), (88.6, 13.6))
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 13.8, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            with Locations((-87.5, 58.2)):
                Circle(0.4)
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            with Locations((-87.5, 11.2)):
                Circle(0.4)
        # OneSide extrude, distance=-10
        extrude(amount=-10, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(88.8, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((-72.7000010833, 13.1000001952)):
                Circle(0.5)
        # OneSide extrude, distance=-2.7
        extrude(amount=-2.7, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a curved blade or knife tool with an elongated handle featuring a sharp, downward-curved cutting edge on one end and a flat, slightly tapered shaft body with a pointed tip on the other end.
def model_53075_6438cc56_0005():
    """Model: basis prayer"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 13 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 2.56, perimeter: 25.6
            with BuildLine():
                Line((-33.5167323496, 0), (-36.9167323496, 0))
                Line((-33.5167323496, 3.4), (-33.5167323496, 0))
                Line((-36.9167323496, 3.4), (-33.5167323496, 3.4))
                Line((-36.9167323496, 0), (-36.9167323496, 3.4))
            make_face()
            with BuildLine():
                Line((-36.7167323496, 0.2), (-36.7167323496, 3.2))
                Line((-36.7167323496, 3.2), (-33.7167323496, 3.2))
                Line((-33.7167323496, 3.2), (-33.7167323496, 0.2))
                Line((-33.7167323496, 0.2), (-36.7167323496, 0.2))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-46
        extrude(amount=-46)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 3.4, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((15, 35.2167323496)):
                Circle(0.5)
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((10, 35.2167323496)):
                Circle(0.5)
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((5, 35.2167323496)):
                Circle(0.5)
        # OneSide extrude, distance=-5
        extrude(amount=-5, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 36.9167323496), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 5.95, perimeter: 11.7795491595
            with BuildLine():
                Line((-46, 3.4), (-42.5, 0))
                Line((-46, 3.4), (-46, 0))
                Line((-46, 0), (-42.5, 0))
            make_face()
        # OneSide extrude, distance=-4.5
        extrude(amount=-4.5, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-20.6341873163, -21.2410751785, 0), x_dir=(0, 0, 1), z_dir=(-0.6967856843, -0.7172793809, 0))):
            # Profile area: 114.4042232085, perimeter: 77.5856465647
            with BuildLine():
                Line((46.2167323496, 29.9241482663), (24.2167323496, 29.9241482663))
                Line((46.2167323496, 35.9241482663), (46.2167323496, 29.9241482663))
                Line((24.2167323496, 35.9241482663), (46.2167323496, 35.9241482663))
                Line((24.2167323496, 29.9241482663), (24.2167323496, 35.9241482663))
            make_face()
            with BuildLine():
                Line((36.9167323496, 30.4843736865), (36.9167323496, 35.363922846))
                Line((33.5167323496, 30.4843736865), (36.9167323496, 30.4843736865))
                Line((33.5167323496, 35.363922846), (33.5167323496, 30.4843736865))
                Line((36.9167323496, 35.363922846), (33.5167323496, 35.363922846))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((25.2167323496, 32.9241482663), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((45.2167323496, 32.9241482663), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 3.6740134848, perimeter: 31.170067424
            with BuildLine():
                Line((36.9167323496, 35.363922846), (33.5167323496, 35.363922846))
                Line((33.5167323496, 35.363922846), (33.5167323496, 30.4843736865))
                Line((33.5167323496, 30.4843736865), (36.9167323496, 30.4843736865))
                Line((36.9167323496, 30.4843736865), (36.9167323496, 35.363922846))
            make_face()
            with BuildLine():
                Line((33.7167323496, 35.0768905425), (36.7167323496, 35.0768905425))
                Line((36.7167323496, 35.0768905425), (36.7167323496, 30.77140599))
                Line((36.7167323496, 30.77140599), (33.7167323496, 30.77140599))
                Line((33.7167323496, 30.77140599), (33.7167323496, 35.0768905425))
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 12.9164536575, perimeter: 14.610969105
            with BuildLine():
                Line((33.7167323496, 30.77140599), (33.7167323496, 35.0768905425))
                Line((36.7167323496, 30.77140599), (33.7167323496, 30.77140599))
                Line((36.7167323496, 35.0768905425), (36.7167323496, 30.77140599))
                Line((33.7167323496, 35.0768905425), (36.7167323496, 35.0768905425))
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)
    return part.part


# Description: This is an L-shaped bracket or angle iron with a long horizontal arm and a shorter vertical arm, featuring a hexagonal hole or socket at the upper end and a rectangular slot or opening on the vertical section near the joint.
def model_53075_6438cc56_0011():
    """Model: grip barbell"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 13 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 2.72, perimeter: 27.2
            with BuildLine():
                Line((68.2, 121.8), (71.8, 121.8))
                Line((68.2, 118.2), (68.2, 121.8))
                Line((71.8, 118.2), (68.2, 118.2))
                Line((71.8, 121.8), (71.8, 118.2))
            make_face()
            with BuildLine():
                Line((68.4, 118.4), (71.6, 118.4))
                Line((68.4, 121.6), (68.4, 118.4))
                Line((71.6, 121.6), (68.4, 121.6))
                Line((71.6, 118.4), (71.6, 121.6))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=55
        extrude(amount=55)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 121.8, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.9087385212, perimeter: 7.853981634
            with Locations((-70, 35)):
                Circle(1.25)
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            with Locations((-69.2000010312, 54.0000008047)):
                Circle(0.4)
            # Profile area: 4.9087385212, perimeter: 7.853981634
            with Locations((-70, 25)):
                Circle(1.25)
            # Profile area: 4.9087385212, perimeter: 7.853981634
            with Locations((-70, 15)):
                Circle(1.25)
            # Profile area: 4.9087385212, perimeter: 7.853981634
            with Locations((-70, 5)):
                Circle(1.25)
        # OneSide extrude, distance=-10
        extrude(amount=-10, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(71.8, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            with Locations((-40, 120)):
                Circle(0.4)
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            with Locations((-30, 120)):
                Circle(0.4)
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            with Locations((-20, 120)):
                Circle(0.4)
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            with Locations((-10, 120)):
                Circle(0.4)
        # OneSide extrude, distance=-7
        extrude(amount=-7, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(68.2, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 4.9087385212, perimeter: 7.853981634
            with Locations((50, 120)):
                Circle(1.25)
        # OneSide extrude, distance=14
        extrude(amount=14, mode=Mode.ADD)
    return part.part


# Description: This is a blue plastic mounting bracket or handle with an angular, U-shaped design featuring two vertical flanges connected by a horizontal bar, and a rectangular slot or opening through the center for attachment or insertion purposes.
def model_53078_b592f2bd_0003():
    """Model: mangler"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 82.5353292432, perimeter: 40.2520916502
            with BuildLine():
                Line((71, 0), (79, 0))
                Line((79, 0), (76.8761372006, 13.274142496))
                CenterArc((75, 12.9739605439), 1.9, 9.0902769208, 161.8194461584)
                Line((73.1238627994, 13.274142496), (71, 0))
            make_face()
        # Symmetric extrude, each_side=12.5
        extrude(amount=12.5, both=True)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on XY construction plane
        # Sketch has 8 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 119.0414655442, perimeter: 59.6390316899
            with BuildLine():
                Line((72.6000010818, 9.0000001341), (71.9000010714, 9.0000001341))
                Line((71.9000010714, 9.0000001341), (69.5, -2))
                Line((69.5, -2), (81, -1))
                Line((81, -1), (79.3516565242, 9.302146724))
                Line((79.3516565242, 9.302146724), (77.654238009, 9.0000001341))
                Line((77.4000011533, 9.0000001341), (77.654238009, 9.0000001341))
                Line((77.4000011533, 9.0000001341), (76.7272906304, 13.2044409023))
                CenterArc((75.0000011176, 13.0000001937), 1.7393461601, 6.7500825167, 161.8194461584)
                Line((73.2727116047, 13.2044409023), (73.2951532938, 13.344701459))
                Line((72.6000010818, 9.0000001341), (73.2727116047, 13.2044409023))
            make_face()
            with BuildLine():
                CenterArc((77.1000011489, 2.3000000343), 0.3162277707, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((72.9000010863, 2.3000000343), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((75, 9.5), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((75.0000011176, 4.5000000671), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=11
        extrude(amount=11, both=True, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 11), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.7853981868, perimeter: 3.1415927004
            with Locations((-75.0000011176, 4.5000000671)):
                Circle(0.5000000075)
        # Symmetric extrude, each_side=24.5
        extrude(amount=24.5, both=True, mode=Mode.SUBTRACT)

        # Sketch6 -> Extrude6 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -12.5), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            with Locations((-77.5000011548, 1.0000000149)):
                Circle(0.4)
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            with Locations((-74.5000011101, 1.0000000149)):
                Circle(0.4)
        # OneSide extrude, distance=-29
        extrude(amount=-29, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a bracket or corner brace with an elongated rectangular profile, featuring a notched or slotted detail at one end for mounting or attachment purposes.
def model_53448_2f7c767c_0016():
    """Model: wing  v1 (2)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.9848829792, perimeter: 20.3275417017
            with BuildLine():
                Line((-4.9999258959, -0.103638967), (3.4761824312, -0.0974700673))
                Line((3.4761824312, -0.0974700673), (4.9683772229, -0.5948683312))
                Line((4.9683772229, -0.5948683312), (5, -0.5))
                Line((3.5, 0), (5, -0.5))
                Line((3.5, 0), (-4.9999258959, -0.0061862341))
                Line((-4.9999258959, -0.103638967), (-4.9999258959, -0.0061862341))
            make_face()
        # OneSide extrude, distance=50
        extrude(amount=50)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.0000727798, 0, 0.099999975), x_dir=(0.9999997352, 0, -0.0007277984), z_dir=(0.0007277984, 0, 0.9999997352))):
            # Profile area: 1.5085049189, perimeter: 7.3385114576
            with BuildLine():
                Line((1, 0), (0.2732220673, 1.2588163053))
                Line((-0.2732220673, 1.2588163053), (0.2732220673, 1.2588163053))
                Line((-0.2732220673, 1.2588163053), (-1, 0))
                Line((-1, 0), (1, 0))
            make_face()
            with BuildLine():
                CenterArc((0.555602997, 0.2565727293), 0.1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-0.5556025281, 0.256573), 0.1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0, 1.0022433053), 0.1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0.0001455597, 0, 0.1999999485), x_dir=(0.9999997352, 0, -0.0007277984), z_dir=(0.0007277984, 0, 0.9999997352))):
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            with Locations((0, 1.0022433053)):
                Circle(0.1)
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            with Locations((0.555602997, 0.2565727293)):
                Circle(0.1)
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            with Locations((-0.5556025281, 0.256573)):
                Circle(0.1)
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (NewBody)
        # Sketch on BRepFace
        # Sketch has 6 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.0001455597, 0, 0.1999999485), x_dir=(0.9999997352, 0, -0.0007277984), z_dir=(0.0007277984, 0, 0.9999997352))):
            # Profile area: 4.5085049413, perimeter: 10.3385114799
            with BuildLine():
                Line((1, 0), (-1, 0))
                Line((-1, 0), (-1.0000000084, -1.5))
                Line((-0.2732220897, -2.7588163134), (-1.0000000084, -1.5))
                Line((0.2732220448, -2.7588163195), (-0.2732220897, -2.7588163134))
                Line((0.9999999916, -1.5000000224), (0.2732220448, -2.7588163195))
                Line((1, 0), (0.9999999916, -1.5000000224))
            make_face()
            with BuildLine():
                CenterArc((-0.5556025394, -1.756573005), 0.1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-0.0000000196, -2.5022433165), 0.1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0.5556029857, -1.7565727467), 0.1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


# Description: This is a folded metal bracket or hinge assembly featuring two perpendicular rectangular panels with mesh or perforated surface patterns, connected by a bent section, and a flat base plate at the bottom.
def model_53456_0e487078_0000():
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
            # Profile area: 1.064530265, perimeter: 11.0312076794
            with BuildLine():
                _nurbs_edge([(-0.1065180406, 3.0366299557), (-0.1039397981, 2.8665059577), (-0.1038406989, 2.6774460387), (-0.1051019091, 2.484760605), (-0.1060759656, 2.3359459925), (-0.107631336, 2.1871627548), (-0.1074336753, 2.0734451151), (-0.107279392, 1.9846832638), (-0.1058034809, 1.9192388724), (-0.1052888592, 1.8717602517), (-0.1048078833, 1.8273857598), (-0.105980044, 1.7931260116), (-0.1075213541, 1.735989213), (-0.1090604535, 1.6789343619), (-0.1118571411, 1.6029144471), (-0.0969925602, 1.511906016), (-0.0854499266, 1.4412362153), (-0.061486242, 1.3586120194), (-0.0056020322, 1.2841778691), (0.0411986499, 1.2218423898), (0.1104942064, 1.1720517559), (0.1797582853, 1.1442068888), (0.2911399818, 1.0994303092), (0.3986653601, 1.0970498529), (0.4915159789, 1.0960442122), (0.594504472, 1.0949287707), (0.6792621015, 1.0979735108), (0.7458488447, 1.0970152931), (0.7999536125, 1.0962366974), (0.8462430834, 1.0934958948), (0.9057212493, 1.0935244826), (0.969278969, 1.0935550312), (1.0461921782, 1.0990975337), (1.117584085, 1.1030542701), (1.1491976327, 1.1048063801), (1.1793740154, 1.1058763926), (1.2029274446, 1.1054396337)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.09286533, 0.09286533, 0.09286533, 0.1645869845, 0.1645869845, 0.1645869845, 0.2205690366, 0.2205690366, 0.2205690366, 0.2728910098, 0.2728910098, 0.2728910098, 0.325137941, 0.325137941, 0.325137941, 0.36570869, 0.36570869, 0.36570869, 0.3996849908, 0.3996849908, 0.3996849908, 0.4543213635, 0.4543213635, 0.4543213635, 0.5149231964, 0.5149231964, 0.5149231964, 0.5641649514, 0.5641649514, 0.5641649514, 0.616784154, 0.616784154, 0.616784154, 0.6400848298, 0.6400848298, 0.6400848298, 0.6400848298], 3)
                _nurbs_edge([(1.2029274446, 1.1054396337), (1.2030927751, 1.0911490356), (1.202775446, 1.0744593312), (1.202109391, 1.0562865701), (1.1993523766, 0.9810637), (1.1923096931, 0.8844759287), (1.1914225199, 0.7982658879), (1.1900937633, 0.6691454929), (1.1959955833, 0.5599294298), (1.1956071984, 0.442005652), (1.1954365428, 0.3901901584), (1.1947073001, 0.3376755698), (1.1941691705, 0.288276353)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0.7404848672, 0.7404848672, 0.7404848672, 0.7404848672, 0.7546963876, 0.7546963876, 0.7546963876, 0.8135224159, 0.8135224159, 0.8135224159, 0.9016286263, 0.9016286263, 0.9016286263, 0.940342335, 0.940342335, 0.940342335, 0.940342335], 3)
                Line((1.1941691705, 0.288276353), (-0.0550227974, 0.288276353))
                Line((-0.0550227974, 0.288276353), (-0.0550227974, 0.08827635))
                Line((1.3942672613, 0.08827635), (-0.0550227974, 0.08827635))
                _nurbs_edge([(0.0934589987, 3.0396606234), (0.0936996613, 3.0237806247), (0.0941489714, 2.9918057548), (0.0947268913, 2.9431988371), (0.0953052934, 2.87709992), (0.0957117053, 2.7923804664), (0.0958131204, 2.7057298739), (0.0956333368, 2.617482154), (0.0952122284, 2.5281945565), (0.0946106127, 2.4387123777), (0.093912857, 2.3502091558), (0.0932351121, 2.2642882545), (0.0927124039, 2.182854779), (0.0924652259, 2.1077682075), (0.0925727293, 2.040560932), (0.0930410844, 1.9821175829), (0.0937786147, 1.9323976519), (0.0945563584, 1.890072574), (0.0950108013, 1.8524022531), (0.0948292952, 1.8161199629), (0.0938938264, 1.778105653), (0.0924722768, 1.7362711494), (0.0912730821, 1.6898666648), (0.0913630783, 1.6392026246), (0.0941153245, 1.585518789), (0.1011594483, 1.5308109612), (0.1142890226, 1.4776294154), (0.1351742534, 1.4286544143), (0.1650882164, 1.386286718), (0.2046584826, 1.3522743577), (0.2535312183, 1.3272197603), (0.3103745646, 1.3105495917), (0.3732102615, 1.3009300684), (0.4396551804, 1.2965628521), (0.5071969872, 1.2955204597), (0.573459643, 1.2960845785), (0.6364588132, 1.2970222049), (0.6947749774, 1.2975295642), (0.7477405734, 1.2972236716), (0.7956200767, 1.2961151113), (0.8398002399, 1.2945911382), (0.8829626513, 1.2933905186), (0.9282129276, 1.2933105153), (0.9781719698, 1.2948999865), (1.0341740803, 1.2981883281), (1.0951856454, 1.3023213619), (1.1582499259, 1.3057060068), (1.2194542224, 1.3063333452), (1.2747591907, 1.3020466536), (1.3208061854, 1.2908226882), (1.3559302343, 1.2710705972), (1.380258359, 1.2418278456), (1.3950411611, 1.2028774135), (1.4022155543, 1.1548727609), (1.4038492847, 1.099500781), (1.4019775881, 1.0390994633), (1.3984654968, 0.9762248507), (1.3948543095, 0.913218015), (1.3922318801, 0.8518143862), (1.3910472476, 0.7926258724), (1.3912114559, 0.7353121019), (1.3923025046, 0.6790054774), (1.3937425188, 0.6226676936), (1.394971361, 0.5654407228), (1.3956583581, 0.5070835245), (1.3957459573, 0.44802766), (1.3953472087, 0.3891019449), (1.3946829518, 0.3313454193), (1.3940071132, 0.2757975723), (1.3935269917, 0.2232667492), (1.3933603458, 0.174215426), (1.3935264097, 0.137945989), (1.3938279791, 0.1124484128), (1.3941077199, 0.0962074694), (1.3942672613, 0.08827635)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0142857143, 0.0285714286, 0.0428571429, 0.0571428571, 0.0714285714, 0.0857142857, 0.1, 0.1142857143, 0.1285714286, 0.1428571429, 0.1571428571, 0.1714285714, 0.1857142857, 0.2, 0.2142857143, 0.2285714286, 0.2428571429, 0.2571428571, 0.2714285714, 0.2857142857, 0.3, 0.3142857143, 0.3285714286, 0.3428571429, 0.3571428571, 0.3714285714, 0.3857142857, 0.4, 0.4142857143, 0.4285714286, 0.4428571429, 0.4571428571, 0.4714285714, 0.4857142857, 0.5, 0.5142857143, 0.5285714286, 0.5428571429, 0.5571428571, 0.5714285714, 0.5857142857, 0.6, 0.6142857143, 0.6285714286, 0.6428571429, 0.6571428571, 0.6714285714, 0.6857142857, 0.7, 0.7142857143, 0.7285714286, 0.7428571429, 0.7571428571, 0.7714285714, 0.7857142857, 0.8, 0.8142857143, 0.8285714286, 0.8428571429, 0.8571428571, 0.8714285714, 0.8857142857, 0.9, 0.9142857143, 0.9285714286, 0.9428571429, 0.9571428571, 0.9714285714, 0.9857142857, 1, 1, 1, 1, 1, 1], 5)
                Line((-0.1065180406, 3.0366299557), (0.0934589987, 3.0396606234))
            make_face()
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)
    return part.part


# Description: This is a T-shaped toggle clamp or latch mechanism featuring a flat rectangular head with mounting holes and a long cylindrical stem that angles downward, designed for quick-release fastening or positioning applications.
def model_53471_1b48c608_0001():
    """Model: middle hydraulic actuator 2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 139.2699081699, perimeter: 45.7079632679
            with BuildLine():
                CenterArc((50, -80), 5, -90, 180)
                Line((50, -75), (40, -75))
                Line((40, -75), (40, -85))
                Line((40, -85), (50, -85))
            make_face()
        # OneSide extrude, distance=8
        extrude(amount=8)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(8, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 78.5398163397, perimeter: 31.4159265359
            with BuildLine():
                CenterArc((50, -80), 5, 90, 180)
                CenterArc((50, -80), 5, -90, 180)
            make_face()
        # OneSide extrude, distance=16
        extrude(amount=16, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 78.5398163397, perimeter: 31.4159265359
            with BuildLine():
                CenterArc((-50, -80), 5, 90, 180)
                CenterArc((-50, -80), 5, -90, 180)
            make_face()
        # OneSide extrude, distance=16
        extrude(amount=16, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -40), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 50.2654824574, perimeter: 25.1327412287
            with BuildLine():
                CenterArc((4, -80), 4, 0, 180)
                CenterArc((4, -80), 4, 180, 180)
            make_face()
        # OneSide extrude, distance=50
        extrude(amount=50, mode=Mode.ADD)

        # Sketch5 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 10), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 103.6725575685, perimeter: 69.115038379
            with BuildLine():
                CenterArc((4, -80), 7, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((4, -80), 4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 50.2654824574, perimeter: 25.1327412287
            with Locations((4, -80)):
                Circle(4)
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)
    return part.part


# Description: This is a connector or coupling component with a cylindrical lower section featuring a protruding collar/flange, and a rectangular upper section, designed to join two parts together at an angle.
def model_53846_89405f98_0010():
    """Model: sprzaczka v4"""
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
        # OneSide extrude, distance=2
        extrude(amount=2, mode=Mode.ADD)

        # Sketch7 -> Extrude6 (Cut)
        # Sketch on XY construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.2922466566, perimeter: 1.9163715187
            with Locations((0, 1.4000000209)):
                Circle(0.305)
        # Symmetric extrude, each_side=0.7
        extrude(amount=0.7, both=True, mode=Mode.SUBTRACT)

        # Sketch9 -> Extrude7 (Cut)
        # Sketch on YZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            with Locations((0, 1.4000000209)):
                Circle(0.1)
        # OneSide extrude, distance=0.65
        extrude(amount=0.65, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a shovel or spade with a flat, squared blade attached to a cylindrical handle, featuring a pointed tip at the bottom of the blade for digging into soil.
def model_53927_ef5208b9_0004():
    """Model: hook"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 3.225341539, perimeter: 7.32961189
            with BuildLine():
                Line((75, 0), (76.5, 0))
                Line((76.5, 0), (76.5000011399, 1.0000000149))
                CenterArc((74.9300012441, 0.9300000503), 1.5715596291, 2.5528970265, 78.2897660388)
                Line((75.1000011191, 2.5000000373), (75.1801088473, 2.4815302159))
                Line((75, 2.5), (75.1000011191, 2.5000000373))
                Line((75, 0), (75, 2.5))
            make_face()
        # Symmetric extrude, each_side=0.6
        extrude(amount=0.6, both=True)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.2827454539, perimeter: 1.8849626422
            with Locations((0, -75.3000011221)):
                Circle(0.3000011221)
        # OneSide extrude, distance=-4.5
        extrude(amount=-4.5, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.2211053797, perimeter: 2.2958636591
            with BuildLine():
                Line((0.5196145944, -75), (-0.5196145944, -75))
                CenterArc((0, -75.3000011221), 0.6, 30.0001237246, 119.9997525508)
            make_face()
            # Profile area: 0.9098679756, perimeter: 3.5525059031
            with BuildLine():
                CenterArc((0, -75.3000011221), 0.6, 149.9998762754, 30.0001237246)
                CenterArc((0, -75.3000011221), 0.6, 180, 180)
                CenterArc((0, -75.3000011221), 0.6, 0, 30.0001237246)
                Line((0.5196145944, -75), (-0.5196145944, -75))
            make_face()
        # OneSide extrude, distance=-2.5
        extrude(amount=-2.5, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on YZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            with Locations((75.900001131, 1.0000000149)):
                Circle(0.4)
        # Symmetric extrude, each_side=0.7
        extrude(amount=0.7, both=True, mode=Mode.ADD)

        # Sketch5 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-0.7, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((-75.900001131, 1.0000000149)):
                Circle(0.2)
        # OneSide extrude, distance=-1.7
        extrude(amount=-1.7, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a dark gray polymer or composite enclosure/housing with an octagonal or rounded polygonal base shape, featuring two rectangular ventilation slots or openings with mesh inserts on the top and sides for airflow.
def model_53927_ef5208b9_0009():
    """Model: switch housing"""
    with BuildPart() as part:
        # Sketch1 -> Extrude3 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 28 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 10.6047908023, perimeter: 12.6301603038
            with BuildLine():
                CenterArc((-64.2500009313, -0.1817808725), 0.75, 180, 70.4268741696)
                Line((-63.9556874308, -1.0824226018), (-64.5012581821, -0.8884418902))
                CenterArc((-62.9841593946, 1.65), 2.9, -109.5731258304, 19.5731258304)
                Line((-62.0158424681, -1.25), (-62.9841593946, -1.25))
                CenterArc((-62.0158424681, 1.65), 2.9, -90, 19.5731258304)
                Line((-60.4987436806, -0.8884418902), (-61.0443144319, -1.0824226018))
                CenterArc((-60.7500009313, -0.1817808725), 0.75, -70.4268741696, 70.4268741696)
                Line((-60.0000009313, 0.1817808725), (-60.0000009313, -0.1817808725))
                CenterArc((-60.7500009313, 0.1817808725), 0.75, 0, 70.4268741696)
                Line((-61.0443144319, 1.0824226018), (-60.4987436806, 0.8884418902))
                CenterArc((-62.0158424681, -1.65), 2.9, 70.4268741696, 19.5731258304)
                Line((-62.9841593946, 1.25), (-62.0158424681, 1.25))
                CenterArc((-62.9841593946, -1.65), 2.9, 90, 19.5731258304)
                Line((-64.5012581821, 0.8884418902), (-63.9556874308, 1.0824226018))
                CenterArc((-64.2500009313, 0.1817808725), 0.75, 109.5731258304, 70.4268741696)
                Line((-65.0000009313, -0.1817808725), (-65.0000009313, 0.1817808725))
            make_face()
        # OneSide extrude, distance=-1.5
        extrude(amount=-1.5)

        # Sketch3 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 23 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.25, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 22.7693142392, perimeter: 30.7586989278
            with BuildLine():
                CenterArc((62.589614118, -0.75), 3.060153963, 0, 360)
            make_face()
            with BuildLine():
                Line((63.1641878559, -1.5), (62.9841593946, -1.5))
                Line((62.9841593946, -1.5), (62.0158424681, -1.5))
                Line((62.0158424681, -1.5), (61.7372822339, -1.5))
                CenterArc((61.7372822339, 3.85), 5.35, -102.5288077091, 12.5288077091)
                Line((60.5767042846, -1.372600772), (60.3523822253, -1.3227514255))
                CenterArc((60.4500009313, -0.8834672484), 0.45, -180, 77.4711922908)
                Line((60.0000009313, -0.6643604995), (60.0000009313, -0.8834672484))
                CenterArc((60.4500009313, -0.6643604995), 0.45, 103.7362683056, 76.2637316944)
                Line((60.3431470406, -0.2272309466), (60.6467564416, -0.1530153152))
                CenterArc((61.9171304756, -5.35), 5.35, 90, 13.7362683056)
                Line((62.0158424681, 0), (61.9171304756, 0))
                Line((62.9841593946, 0), (62.0158424681, 0))
                Line((63.1641878005, 0), (62.9841593946, 0))
                CenterArc((63.1641878005, -5.35), 5.35, 76.8280288376, 13.1719711624)
                Line((64.3833167628, -0.1407558539), (64.6525444889, -0.2037637125))
                CenterArc((64.5500009313, -0.6419244351), 0.45, 0, 76.8280288376)
                Line((65.0000009313, -0.8580755766), (65.0000009313, -0.6419244351))
                CenterArc((64.5500009313, -0.8580755766), 0.45, -76.828028567, 76.828028567)
                Line((64.652544491, -1.2962362987), (64.3833168428, -1.3592441403))
                CenterArc((63.1641878559, 3.85), 5.35, -90, 13.171971433)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-3.2
        extrude(amount=-3.2, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 8 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-60.0000009313, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0510270027, perimeter: 2.507814784
            with BuildLine():
                CenterArc((0.7749999827, 0.1), 0.15, 0, 180)
                Line((0.6249999827, -0.1), (0.6249999827, 0.1))
                CenterArc((0.7749999827, -0.1), 0.15, 180, 180)
                Line((0.9249999827, 0.1), (0.9249999827, -0.1))
            make_face()
            with BuildLine():
                Line((0.6643604995, 0.1817808725), (0.6643604995, -0.1817808725))
                Line((0.8834672484, 0.1817808725), (0.6643604995, 0.1817808725))
                Line((0.8834672484, -0.1817808725), (0.8834672484, 0.1817808725))
                Line((0.6643604995, -0.1817808725), (0.8834672484, -0.1817808725))
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.079658832, perimeter: 1.1653369879
            with BuildLine():
                Line((0.6643604995, -0.1817808725), (0.8834672484, -0.1817808725))
                Line((0.8834672484, -0.1817808725), (0.8834672484, 0.1817808725))
                Line((0.8834672484, 0.1817808725), (0.6643604995, 0.1817808725))
                Line((0.6643604995, 0.1817808725), (0.6643604995, -0.1817808725))
            make_face()
        # OneSide extrude, distance=-5.7
        extrude(amount=-5.7, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude6 (Cut)
        # Sketch on BRepFace
        # Sketch has 15 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.6492582383, perimeter: 3.1611713011
            with BuildLine():
                Line((-61.4507040904, -0.5008134435), (-61.9171304756, -0.5008134435))
                CenterArc((-61.4507040904, -0.3008134435), 0.2, -90, 90)
                Line((-61.2507040904, 0.2991865565), (-61.2507040904, -0.3008134435))
                CenterArc((-61.4507040904, 0.2991865565), 0.2, 0, 90)
                Line((-61.9171304756, 0.4991865565), (-61.4507040904, 0.4991865565))
                Line((-61.9171304756, -0.5008134435), (-61.9171304756, 0.4991865565))
            make_face()
            # Profile area: 1.2470573249, perimeter: 4.4941146497
            with BuildLine():
                Line((-61.9171304756, -0.5008134435), (-63.1641878005, -0.5008134435))
                Line((-61.9171304756, -0.5008134435), (-61.9171304756, 0.4991865565))
                Line((-63.1641878005, 0.4991865565), (-61.9171304756, 0.4991865565))
                Line((-63.1641878005, 0.4991865565), (-63.1641878005, -0.5008134435))
            make_face()
            # Profile area: 0.569348143, perimeter: 3.0013511106
            with BuildLine():
                Line((-63.1641878005, 0.4991865565), (-63.1641878005, -0.5008134435))
                Line((-63.5507040904, 0.4991865565), (-63.1641878005, 0.4991865565))
                CenterArc((-63.5507040904, 0.2991865565), 0.2, 90, 90)
                Line((-63.7507040904, -0.3008134435), (-63.7507040904, 0.2991865565))
                CenterArc((-63.5507040904, -0.3008134435), 0.2, -180, 90)
                Line((-63.1641878005, -0.5008134435), (-63.5507040904, -0.5008134435))
            make_face()
        # OneSide extrude, distance=-0.9
        extrude(amount=-0.9, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a black plastic or composite chair back with curved ergonomic shaping, featuring a mesh or perforated texture panel, a cylindrical mounting post, and two horizontal support legs extending downward.
def model_53927_ef5208b9_0011():
    """Model: plug"""
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
        # Sketch has 2 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 4.2376784604, perimeter: 11.7179037139
            with BuildLine():
                Line((-60.75, 0), (-59, 0))
                Line((-59, 0), (-59, 1))
                _nurbs_edge([(-60.25, 4.5), (-60.2523108531, 4.4367890409), (-60.2565785123, 4.3116219173), (-60.261917805, 4.1276355504), (-60.2668975192, 3.8899043286), (-60.2692053092, 3.6056707285), (-60.266709237, 3.3346694291), (-60.257734432, 3.0770206475), (-60.2396247919, 2.8324779838), (-60.2083869418, 2.6000924576), (-60.1590623925, 2.3783364639), (-60.0865225216, 2.1654549496), (-59.9861319068, 1.9596940903), (-59.8546527703, 1.7595625889), (-59.6908690013, 1.5640075974), (-59.4947238519, 1.3723276992), (-59.3123713074, 1.2217584558), (-59.161595044, 1.1103088425), (-59.054895388, 1.03666097), (-59, 1)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0666666667, 0.1333333333, 0.2, 0.2666666667, 0.3333333333, 0.4, 0.4666666667, 0.5333333333, 0.6, 0.6666666667, 0.7333333333, 0.8, 0.8666666667, 0.9333333333, 1, 1, 1, 1, 1, 1], 5)
                Line((-60.75, 4.5), (-60.25, 4.5))
                Line((-60.75, 0), (-60.75, 4.5))
            make_face()
            # Profile area: 4.2376474097, perimeter: 11.7178842054
            with BuildLine():
                Line((-62.5, 0), (-60.75, 0))
                Line((-60.75, 0), (-60.75, 4.5))
                Line((-60.75, 4.5), (-61.25, 4.5))
                _nurbs_edge([(-61.25, 4.5), (-61.2476728734, 4.4365841671), (-61.24337497, 4.3110311482), (-61.2379972186, 4.1265374927), (-61.2329801406, 3.8882740539), (-61.2306489248, 3.6036190527), (-61.2331440085, 3.3324402581), (-61.2421377539, 3.0748484129), (-61.2602810155, 2.8305730861), (-61.2915584454, 2.5986166477), (-61.3409226515, 2.3773796504), (-61.4134974885, 2.1650277695), (-61.513915009, 1.9597309987), (-61.645410363, 1.7599387558), (-61.8091981951, 1.5645649739), (-62.0053346924, 1.3728921593), (-62.1876701011, 1.2221856806), (-62.3384278475, 1.1105532833), (-62.4451126591, 1.0367483224), (-62.5, 1)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0666666667, 0.1333333333, 0.2, 0.2666666667, 0.3333333333, 0.4, 0.4666666667, 0.5333333333, 0.6, 0.6666666667, 0.7333333333, 0.8, 0.8666666667, 0.9333333333, 1, 1, 1, 1, 1, 1], 5)
                Line((-62.5, 0), (-62.5, 1))
            make_face()
        # OneSide extrude, distance=-1.4
        extrude(amount=-1.4)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 62.5), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1.7400000617, perimeter: 8.702264647
            with BuildLine():
                Line((-1.0000000149, 5.0000000745), (-1.4, 1))
                Line((-1.0000000149, 5.0000000745), (-1.9000000283, 4.70000007))
                Line((-1.9000000283, 4.70000007), (-1.4, 1))
            make_face()
            # Profile area: 3.0005231987, perimeter: 9.1391752575
            with BuildLine():
                Line((0, 1), (1.2000000179, 4.0000000596))
                Line((1.2000000179, 4.0000000596), (-0.4, 5.0008719184))
                Line((-0.4, 5.0008719184), (0, 1))
            make_face()
        # OneSide extrude, distance=-4.2
        extrude(amount=-4.2, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 8 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 4.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1306858347, perimeter: 1.3424777961
            with BuildLine():
                CenterArc((0.701138393, 60.6499724312), 0.15, 180, 180)
                Line((0.851138393, 60.8499724312), (0.851138393, 60.6499724312))
                CenterArc((0.701138393, 60.8499724312), 0.15, 0, 180)
                Line((0.551138393, 60.6499724312), (0.551138393, 60.8499724312))
            make_face()
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((-0.701138393, 59.7499724312)):
                Circle(0.15)
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((-0.701138393, 61.7499724312)):
                Circle(0.15)
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)

        # Sketch5 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -1, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.096211275, perimeter: 1.0995574288
            with Locations((-0.7000000104, 61.7500009201)):
                Circle(0.175)
            # Profile area: 0.0255254403, perimeter: 2.0420352248
            with BuildLine():
                CenterArc((-0.701138393, 59.7499724312), 0.175, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-0.701138393, 59.7499724312), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((-0.701138393, 59.7499724312)):
                Circle(0.15)
        # OneSide extrude, distance=0.8
        extrude(amount=0.8, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical or oval-shaped housing/container with a ribbed or textured outer surface, featuring a recessed top opening and reinforcing ribs along its sides for structural rigidity.
def model_54187_3f75c385_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 50.2654824574, perimeter: 25.1327412287
            Circle(4)
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 9.6211275016, perimeter: 10.9955742876
            Circle(1.75)
        # OneSide extrude, distance=-2
        extrude(amount=-2, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 18.8495559215, perimeter: 37.6991118431
            with BuildLine():
                CenterArc((0, 0), 3.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 2.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.9
        extrude(amount=-0.9, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 0.6, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.731824773, perimeter: 3.0325535975
            with Locations((0, -3)):
                Circle(0.4826458952)
        # OneSide extrude, distance=-1.5
        extrude(amount=-1.5, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a tactical pen featuring an elongated cylindrical body with a pointed tip, a textured grip section, and a blue-accented clip or attachment mechanism near the top.
def model_54285_76f37095_0003():
    """Model: Screwdriver-"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 0.1256637099, perimeter: 1.2566370802
            with Locations((0.5000000075, 0.5000000075)):
                Circle(0.200000003)
        # OneSide extrude, distance=3.5
        extrude(amount=3.5)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on YZ construction plane
        # Sketch has 25 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0336399011, perimeter: 1.1144641308
            with BuildLine():
                Line((-1.4997412312, 0.6000000075), (-1.4997412312, 0.7000000104))
                Line((-2.0003672086, 0.7000000104), (-1.4997412312, 0.7000000104))
                CenterArc((-1.4997412312, 1.9031318177), 1.3031318102, -112.5923096523, 22.5923096523)
            make_face()
            # Profile area: 0.1499741276, perimeter: 3.1994824684
            with BuildLine():
                Line((0, 0.7000000104), (0, 0.6000000075))
                Line((-1.4997412312, 0.7000000104), (0, 0.7000000104))
                Line((-1.4997412312, 0.6000000075), (-1.4997412312, 0.7000000104))
                Line((0, 0.6000000075), (-1.4997412312, 0.6000000075))
            make_face()
            # Profile area: 0.0336399011, perimeter: 1.1144641308
            with BuildLine():
                Line((-2.0003672086, 0.3000000045), (-1.4997412312, 0.3000000045))
                Line((-1.4997412312, 0.4000000075), (-1.4997412312, 0.3000000045))
                CenterArc((-1.4997412312, -0.9031318028), 1.3031318102, 90, 22.5923096523)
            make_face()
            # Profile area: 0.1499741276, perimeter: 3.1994824684
            with BuildLine():
                Line((-1.4997412312, 0.4000000075), (-1.4997412312, 0.3000000045))
                Line((-1.4997412312, 0.3000000045), (0, 0.3000000045))
                Line((0, 0.3000000045), (0, 0.4000000075))
                Line((0, 0.4000000075), (-1.4997412312, 0.4000000075))
            make_face()
        # OneSide extrude, distance=0.9
        extrude(amount=0.9, mode=Mode.SUBTRACT)

        # Sketch2 -> Extrude3 (Cut)
        # Sketch on YZ construction plane
        # Sketch has 25 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.079589036, perimeter: 1.4233324682
            with BuildLine():
                Line((-3.5, 0.4800000075), (-3.5, 0.3000000045))
                Line((-3.5, 0.3000000045), (-2.899369843, 0.3000000045))
                CenterArc((-3.4001955783, -0.3067400302), 0.7867400376, 50.4624702975, 39.5375297025)
                Line((-3.5, 0.4800000075), (-3.4001955783, 0.4800000075))
            make_face()
            # Profile area: 0.079589036, perimeter: 1.4233324682
            with BuildLine():
                Line((-3.5, 0.5200000075), (-3.4001955783, 0.5200000075))
                CenterArc((-3.4001955783, 1.3067400451), 0.7867400376, -90, 39.5375297025)
                Line((-3.5, 0.7000000104), (-2.899369843, 0.7000000104))
                Line((-3.5, 0.5200000075), (-3.5, 0.7000000104))
            make_face()
        # OneSide extrude, distance=0.9
        extrude(amount=0.9, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 11 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.6000000075, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.1999115215, perimeter: 5.2849556709
            with BuildLine():
                CenterArc((-0.6000000089, -1.1000000164), 0.400000006, -90, 90)
                Line((-0.200000003, -1.1000000164), (-0.200000003, -0.5000000075))
                Line((-0.200000003, -0.5000000075), (0, -0.5000000075))
                Line((0, -0.5000000075), (0, 0))
                Line((0, 0), (-0.3267949233, 0))
                Line((-0.3267949233, 0), (-0.6732050916, 0))
                Line((-0.6732050916, 0), (-1.0000000149, 0))
                Line((-1.0000000149, 0), (-1.0000000149, -1.1000000164))
                CenterArc((-0.6000000089, -1.1000000164), 0.400000006, 180, 90)
            make_face()
            with BuildLine():
                CenterArc((-0.5500000082, -1.1000000164), 0.1000000015, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0314159275, perimeter: 0.6283185401
            with Locations((-0.5500000082, -1.1000000164)):
                Circle(0.1000000015)
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2, mode=Mode.ADD)

        # Sketch4 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 11 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.6000000075, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0314159275, perimeter: 0.6283185401
            with Locations((-0.5500000082, -1.1000000164)):
                Circle(0.1000000015)
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a simple bracket or support arm featuring a long, horizontal rectangular body with a slight upward bend at the left end, designed to provide structural support or mounting capability.
def model_54383_13d47b0e_0001():
    """Model: frame degrees right"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 8 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 2.2799974889, perimeter: 15.1999977171
            with BuildLine():
                Line((-75.8000011295, 0.8000000119), (-75.8000011295, 3))
                Line((-75.8000011295, 3), (-78, 3))
                Line((-78, 3), (-78, 0.8000000119))
                Line((-78, 0.8000000119), (-75.8000011295, 0.8000000119))
            make_face()
            with BuildLine():
                Line((-77.7, 1.1), (-76.1, 1.1))
                Line((-77.7, 2.7), (-77.7, 1.1))
                Line((-76.1, 2.7), (-77.7, 2.7))
                Line((-76.1, 1.1), (-76.1, 2.7))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=71
        extrude(amount=71)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 78), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.5654866776, perimeter: 6.0548667765
            with BuildLine():
                CenterArc((0, 1.900000006), 0.8, 90, 180)
                Line((0, 2.900000006), (0, 2.700000006))
                CenterArc((0, 1.900000006), 1, 90, 180)
                Line((0, 1.100000006), (0, 0.900000006))
            make_face()
            # Profile area: 0.5654866776, perimeter: 6.0548667765
            with BuildLine():
                Line((0, 1.100000006), (0, 0.900000006))
                CenterArc((0, 1.900000006), 1, -90, 180)
                Line((0, 2.900000006), (0, 2.700000006))
                CenterArc((0, 1.900000006), 0.8, -90, 180)
            make_face()
        # OneSide extrude, distance=-8
        extrude(amount=-8, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 78), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1.0053096491, perimeter: 4.1132741229
            with BuildLine():
                CenterArc((0, 1.900000006), 0.8, 90, 180)
                Line((0, 2.700000006), (0, 1.100000006))
            make_face()
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2, mode=Mode.ADD)

        # Sketch7 -> Extrude11 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 3, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            with Locations((-10.435889882, 76.9000005648)):
                Circle(0.4)
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            with Locations((-29.435889882, 76.9000005648)):
                Circle(0.4)
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a linear actuator or hydraulic cylinder consisting of a dark gray cylindrical rod with a blue/navy rectangular housing sleeve mounted around its middle section, designed to provide linear motion or force along its axis.
def model_54383_13d47b0e_0004():
    """Model: pedal coupler"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            with Locations((75, 0)):
                Circle(1)
        # Symmetric extrude, each_side=11
        extrude(amount=11, both=True)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 16.237976321, perimeter: 15
            with BuildLine():
                Line((77.1650635095, 1.25), (75, 2.5))
                Line((75, 2.5), (72.8349364905, 1.25))
                Line((72.8349364905, 1.25), (72.8349364905, -1.25))
                Line((72.8349364905, -1.25), (75, -2.5))
                Line((75, -2.5), (77.1650635095, -1.25))
                Line((77.1650635095, -1.25), (77.1650635095, 1.25))
            make_face()
        # Symmetric extrude, each_side=5
        extrude(amount=5, both=True, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 11, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.6141829007, perimeter: 3.8264420127
            with BuildLine():
                CenterArc((-75, 0), 1, 120.0000744319, 119.9998511362)
                Line((-75.500001125, -0.8660247542), (-75.500001125, 0.8660247542))
            make_face()
        # OneSide extrude, distance=-3
        extrude(amount=-3, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -11, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.6141829007, perimeter: 3.8264420127
            with BuildLine():
                Line((75.500001125, -0.8660247542), (75.500001125, 0.8660247542))
                CenterArc((75, 0), 1, -59.9999255681, 119.9998511362)
            make_face()
        # OneSide extrude, distance=-3
        extrude(amount=-3, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a large circular fan impeller or turbine wheel with a predominantly disc-shaped body featuring multiple radial blades arranged in a fan pattern, along with a protruding cylindrical hub or mounting boss on one side.
def model_54383_13d47b0e_0008():
    """Model: computer"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 15 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 258.6429588259, perimeter: 58.5840079481
            with BuildLine():
                CenterArc((104, 51.3243955371), 12, 180, 53.6680474496)
                CenterArc((100, 59.3865933057), 18, -99.9479114474, 19.8958228949)
                CenterArc((96, 51.3243955371), 12, -53.6680474496, 53.6680474496)
                Line((108, 54.3241759643), (108, 51.3243955371))
                CenterArc((98, 54.3241759643), 10, 0, 21.8014094864)
                Line((107.2543311884, 58.1141720291), (107.2847669089, 58.0380827279))
                CenterArc((104.4689011157, 57), 3, 21.8014094864, 68.1985905136)
                Line((95.5310988843, 60), (104.4689011157, 60))
                CenterArc((95.5310988843, 57), 3, 90, 68.1985905136)
                Line((92.7152330911, 58.0380827279), (92.7456688116, 58.1141720291))
                CenterArc((102, 54.3241759643), 10, 158.1985905136, 21.8014094864)
                Line((92, 51.3243955371), (92, 54.3241759643))
            make_face()
        # OneSide extrude, distance=-3
        extrude(amount=-3)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 14 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 24.920757685, perimeter: 28.2849004506
            with BuildLine():
                CenterArc((96.5358983849, 49.5), 0.5, 8.2132107017, 81.7867892983)
                Line((96.5358983849, 50), (95.527864045, 50))
                CenterArc((95.527864045, 49.5), 0.5, 90, 96.3793702084)
                CenterArc((100, 50), 5, -173.6206297916, 167.2412595831)
                CenterArc((104.472135955, 49.5), 0.5, -6.3793702084, 96.3793702084)
                Line((104.472135955, 50), (103.4641016151, 50))
                CenterArc((103.4641016151, 49.5), 0.5, 90, 81.7867892983)
                CenterArc((100, 50), 3, -171.7867892983, 163.5735785965)
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 20 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 66.5170876295, perimeter: 31.7943741798
            with BuildLine():
                CenterArc((103.75, 53.0247548784), 1.25, -78.690067526, 78.690067526)
                Line((105, 53.0247548784), (105, 55.75))
                CenterArc((103.75, 55.75), 1.25, 0, 90)
                Line((103.75, 57), (96.25, 57))
                CenterArc((96.25, 55.75), 1.25, 90, 90)
                Line((95, 55.75), (95, 53.0247548784))
                CenterArc((96.25, 53.0247548784), 1.25, 180, 78.690067526)
                Line((96.0048548311, 51.7990290338), (96.3990227174, 51.7201954565))
                CenterArc((96.1538775485, 50.4944696119), 1.25, 7.4879740872, 71.2020934387)
                CenterArc((100, 51), 2.6292033828, -172.5120259128, 165.0240518255)
                CenterArc((103.8461224515, 50.4944696119), 1.25, 101.309932474, 71.2020934387)
                Line((103.6009772826, 51.7201954565), (103.9951451689, 51.7990290338))
            make_face()
        # OneSide extrude, distance=-0.1
        extrude(amount=-0.1, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-0.1, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 18, perimeter: 18
            with BuildLine():
                Line((103, 53), (103, 56))
                Line((103, 56), (97, 56))
                Line((97, 56), (97, 53))
                Line((97, 53), (103, 53))
            make_face()
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-3, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            with Locations((-97.0606601718, 51.9393398282)):
                Circle(0.4)
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            with Locations((-102.9393398282, 51.9393398282)):
                Circle(0.4)
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            with Locations((-102.9393398282, 46.0606601718)):
                Circle(0.4)
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            with Locations((-97.0606601718, 46.0606601718)):
                Circle(0.4)
        # OneSide extrude, distance=-2
        extrude(amount=-2, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a sheet metal bracket or frame assembly with an angular, Z-shaped profile featuring two large rectangular openings and reinforcing ribs along the edges for structural support.
def model_54509_e0930519_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 20 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 10.7247345129, perimeter: 44.6287889419
            with BuildLine():
                CenterArc((8.6420810432, 5.5), 1.5, 8.7461622626, 81.2538377374)
                Line((8.6420810432, 7), (2.3579189568, 7))
                CenterArc((2.3579189568, 5.5), 1.5, 90, 81.2538377374)
                Line((0.8753614103, 5.7280857764), (0.0539719821, 0.3890544931))
                CenterArc((-0.4402138667, 0.4650830852), 0.5, -73.4479220898, 64.7017598272)
                Line((-0.2977705026, -0.014197509), (-0.2500000037, 0))
                Line((-0.2500000037, 0), (0.5, 0))
                Line((1.3695472591, 5.6520571843), (0.5, 0))
                CenterArc((2.3579189568, 5.5), 1, 90, 81.2538377374)
                Line((8.6420810432, 6.5), (2.3579189568, 6.5))
                CenterArc((8.6420810432, 5.5), 1, 8.7461622626, 81.2538377374)
                Line((9.6304527409, 5.6520571843), (10.5, 0))
                Line((11.2500001676, 0), (10.5, 0))
                Line((11.2977705772, -0.0141974734), (11.2500001676, 0))
                CenterArc((11.4402138574, 0.4650831458), 0.5, -171.2538377374, 64.7017698527)
                Line((10.1246385897, 5.7280857764), (10.9460280086, 0.3890545537))
            make_face()
        # OneSide extrude, distance=-10
        extrude(amount=-10)

        # Sketch4 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-0.0057465425, 0.0008840835, 0), x_dir=(0, 0, 1), z_dir=(-0.9883716977, 0.1520571843, 0))):
            # Profile area: 39.6166101922, perimeter: 26.8036911538
            with BuildLine():
                Line((-9.5, 5.2945828543), (-9.5, 0.8927372774))
                Line((-9.5, 0.8927372774), (-0.5, 0.8927372774))
                Line((-0.5, 0.8927372774), (-0.5, 5.2945828543))
                Line((-0.5, 5.2945828543), (-9.5, 5.2945828543))
            make_face()
        # OneSide extrude, distance=-2.5
        extrude(amount=-2.5, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(10.7514112824, 1.6540632742, 0), x_dir=(0, 0, -1), z_dir=(0.9883716977, 0.1520571843, 0))):
            # Profile area: 39.6166096406, perimeter: 26.8036910312
            with BuildLine():
                Line((0.5, 3.6219538275), (0.5, -0.7798916881))
                Line((0.5, -0.7798916881), (9.5, -0.7798916881))
                Line((9.5, -0.7798916881), (9.5, 3.6219538275))
                Line((9.5, 3.6219538275), (0.5, 3.6219538275))
            make_face()
        # OneSide extrude, distance=-1.5
        extrude(amount=-1.5, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a trapezoidal structural bracket or enclosure with an angular, wedge-like geometry featuring multiple flat faces, internal ribbing/bracing, ventilation slots, and mounting flanges designed for reinforcement and component housing.
def model_54597_893331b6_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 15 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 24.5, perimeter: 51
            with BuildLine():
                Line((0, 6.5), (0, 1.5))
                Line((0, 1.5), (8.5, 1.5))
                Line((14, 1.5), (8.5, 1.5))
                Line((14, 1.5), (14, 2.5))
                Line((14, 2.5), (1, 2.5))
                Line((1, 5.5), (1, 2.5))
                Line((7.5, 5.5), (1, 5.5))
                Line((7.5, 6.5), (7.5, 5.5))
                Line((0, 6.5), (7.5, 6.5))
            make_face()
        # OneSide extrude, distance=6
        extrude(amount=6)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 6.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((-7, 5.5)):
                Circle(0.25)
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((-7, 0.5)):
                Circle(0.25)
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((-0.5, 5.5)):
                Circle(0.25)
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((-0.5, 0.5)):
                Circle(0.25)
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (NewBody)
        # Sketch on BRepFace
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 7.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 32.4484304654, perimeter: 22.9149485731
            with BuildLine():
                CenterArc((-0.5, 5.5), 0.25, 180, 90)
                Line((-7.0486452042, 5.5), (-0.75, 5.5))
                Line((-7.0486452042, 0.5375204585), (-7.0486452042, 5.5))
                Line((-0.5, 0.5375204585), (-7.0486452042, 0.5375204585))
                Line((-0.5, 5.25), (-0.5, 0.5375204585))
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.9087385212, perimeter: 7.853981634
            with Locations((-11, 3)):
                Circle(1.25)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3, mode=Mode.ADD)

        # Sketch5 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2.8, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((-11, 3)):
                Circle(0.25)
        # OneSide extrude, distance=3
        extrude(amount=3, mode=Mode.ADD)
    return part.part


# Description: This is a symmetrical dual-wing aerospace component with a central hexagonal body featuring two opposing trapezoidal wings or fins with blue striped ribbing patterns, designed for aerodynamic stabilization or control purposes.
def model_54637_d8b47586_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch2 -> Extrude2 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 17 constraints, 12 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 391.7734457254, perimeter: 267.1822971503
            with BuildLine():
                Line((69.4337552479, 4.2278974592), (96.1837552479, 4.2278974592))
                Line((96.1837552479, 4.2278974592), (96.1837552479, 7.2278974592))
                Line((96.1837552479, 7.2278974592), (69.4337552479, 7.2278974592))
                CenterArc((69.4337552479, 2.2278974592), 5, 90, 90)
                Line((64.4337552479, 2.2278974592), (64.4337552479, -11.5721025408))
                CenterArc((62.4337552479, -11.5721025408), 2, -90, 90)
                Line((34.9337552479, -13.5721025408), (62.4337552479, -13.5721025408))
                CenterArc((34.9337552479, -11.5721025408), 2, -180, 90)
                Line((32.9337552479, 2.2278974592), (32.9337552479, -11.5721025408))
                CenterArc((27.9337552479, 2.2278974592), 5, 0, 90)
                Line((1.1837552479, 7.2278974592), (27.9337552479, 7.2278974592))
                Line((1.1837552479, 7.2278974592), (1.1837552479, 4.2278974592))
                Line((1.1837552479, 4.2278974592), (27.9337552479, 4.2278974592))
                CenterArc((27.9337552479, 2.2278974592), 2, 0, 90)
                Line((29.9337552479, 2.2278974592), (29.9337552479, -11.5721025408))
                CenterArc((34.9337552479, -11.5721025408), 5, 180, 90)
                Line((34.9337552479, -16.5721025408), (62.4337552479, -16.5721025408))
                CenterArc((62.4337552479, -11.5721025408), 5, -90, 90)
                Line((67.4337552479, -11.5721025408), (67.4337552479, 2.2278974592))
                CenterArc((69.4337552479, 2.2278974592), 2, 90, 90)
            make_face()
        # OneSide extrude, distance=30
        extrude(amount=30)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -13.5721025408, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 157.0796326795, perimeter: 125.6637061436
            with BuildLine():
                CenterArc((-48.6837552479, 15), 11.25, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-48.6837552479, 15), 8.75, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=14
        extrude(amount=14, mode=Mode.ADD)

        # Sketch3 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -13.5721025408, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 44.1786466911, perimeter: 23.5619449019
            with Locations((-48.6837552479, 15)):
                Circle(3.75)
        # OneSide extrude, distance=-120
        extrude(amount=-120, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 7.2278974592, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 19.6349540849, perimeter: 15.7079632679
            with Locations((-14.5587552479, 15)):
                Circle(2.5)
            # Profile area: 19.6349540849, perimeter: 15.7079632679
            with Locations((-82.8087552479, 15)):
                Circle(2.5)
        # OneSide extrude, distance=-82.5
        extrude(amount=-82.5, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a seatpost (or seat tube extension), characterized by a long cylindrical shaft with a clamp mechanism at the top for securing a bicycle saddle, featuring a sleek dark finish with blue accent details.
def model_54659_e1303e28_0003():
    """Model: Arm 2 v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 22 constraints, 14 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 35.5000698928, perimeter: 49.9613802868
            with BuildLine():
                CenterArc((2.749181639, 14.9446311536), 0.5, -94, 115)
                Line((3.2159718522, 15.1238151283), (1.5436178799, 19.480446174))
                CenterArc((1.0768276666, 19.3012621993), 0.5, 21, 133.7075610734)
                Line((-0.442483363, 17.2563431311), (0.6247581974, 19.5148814752))
                CenterArc((0.1, 17), 0.6, 154.7075610734, 25.2924389266)
                Line((-0.5, 0), (-0.5, 17))
                CenterArc((0, 0), 0.5, -180, 176)
                Line((0.4987820251, -0.0348782369), (1.4753726575, 13.9310184668))
                CenterArc((2.0739110877, 13.8891645825), 0.6, 86, 90)
                Line((2.7143034021, 14.4458491284), (2.1157649719, 14.4877030127))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((2.749181639, 14.9446311536), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1.0768276666, 19.3012621993), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0.069841539, 2), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0.1, 17), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=1
        extrude(amount=1, both=True)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on XY construction plane
        # Sketch has 11 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.8307219313, perimeter: 5.2300788286
            with BuildLine():
                CenterArc((2.749181639, 14.9446311536), 0.5, -94, 115)
                Line((3.0009510825, 15.6839633842), (3.2159718522, 15.1238151283))
                Line((2.5341608693, 15.5047794095), (3.0009510825, 15.6839633842))
                CenterArc((2.749181639, 14.9446311536), 0.6, 111, 121.4426864488)
                Line((2.7143034021, 14.4458491284), (2.3834488047, 14.4689847576))
            make_face()
            with BuildLine():
                CenterArc((2.749181639, 14.9446311536), 0.2424100331, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.1846082283, perimeter: 1.523107158
            with Locations((2.749181639, 14.9446311536)):
                Circle(0.2424100331)
        # Symmetric extrude, each_side=0.5
        extrude(amount=0.5, both=True, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 9 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 3.7747462102, perimeter: 9.2425162566
            with BuildLine():
                CenterArc((-0.5, 17.1346241737), 1.7, -90.0000000001, 154.7075610736)
                Line((0.2263055381, 18.6716603688), (-0.442483363, 17.2563431311))
                CenterArc((0.1, 17), 0.6, 154.7075610734, 25.2924389266)
                Line((-0.5, 15.4346241737), (-0.5, 17))
            make_face()
            with BuildLine():
                CenterArc((0.1, 17), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.25
        extrude(amount=-0.25, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude4 (Cut)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.6414821615, perimeter: 5.9690260418
            with BuildLine():
                CenterArc((1.0768276666, 19.3012621993), 0.75, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((1.0768276666, 19.3012621993), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=0.5
        extrude(amount=0.5, both=True, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a toroidal (doughnut-shaped) ring with a smooth outer surface and textured mesh pattern on the inner and outer edges, featuring a large central void and radial ribbed or finned sections along its circumference.
def model_54747_8e62bef9_0011():
    """Model: TYERS v1"""
    with BuildPart() as part:
        # Sketch3 -> Extrude2 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            Circle(1)
        # Symmetric extrude, each_side=0.2
        extrude(amount=0.2, both=True)

        # Sketch6 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.2), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1.1309733553, perimeter: 3.7699111843
            Circle(0.6)
        # Symmetric extrude, each_side=5
        extrude(amount=5, both=True, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a hook-shaped bracket or stand with a cylindrical vertical shaft and a curved hook at the top, featuring circular flanged bases at both the bottom and top for mounting or stability.
def model_54753_f93827fa_0000():
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
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 19.6349540849, perimeter: 15.7079632679
            Circle(2.5)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            Circle(1)
        # OneSide extrude, distance=5.5
        extrude(amount=5.5, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 7 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 6, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.1290583059, perimeter: 4.253404033
            with BuildLine():
                Line((0.5520290099, -0.5113219983), (-0.5520290099, -0.5113219983))
                Line((0.5520290099, 0.5113219983), (0.5520290099, -0.5113219983))
                Line((-0.5520290099, 0.5113219983), (0.5520290099, 0.5113219983))
                Line((-0.5520290099, -0.5113219983), (-0.5520290099, 0.5113219983))
            make_face()
        # OneSide extrude, distance=1.5
        extrude(amount=1.5, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.5520290099, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 3.7824071037, perimeter: 9.7855143248
            with BuildLine():
                Line((0.5113219983, 7.5), (-0.5113219983, 7.5))
                _nurbs_edge([(0.249300953, 8.0993183885), (0.2584350686, 8.089314946), (0.2763623242, 8.0691344137), (0.3022303066, 8.038342687), (0.3346412614, 7.9962279372), (0.3714543875, 7.9416999279), (0.4042394367, 7.8851205571), (0.4326726936, 7.8263249677), (0.4565866172, 7.7652278367), (0.4761709883, 7.7019258131), (0.4917570492, 7.6365875871), (0.5012919669, 7.5828228559), (0.5068980471, 7.5417124368), (0.509959935, 7.5139614824), (0.5113219983, 7.5)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1, 1, 1, 1, 1], 5)
                _nurbs_edge([(0.249300953, 8.0993183885), (0.037096152, 8.3686374101), (-0.201113184, 8.6084285762), (-0.4842987213, 8.8077004151), (-0.7237633038, 8.9762067173), (-0.9991507243, 9.1136277443), (-1.2955560551, 9.1951509969), (-1.577732874, 9.272760843), (-1.8720859382, 9.2975277897), (-2.1536988188, 9.2812696495), (-2.5492981309, 9.2584308182), (-2.9232295085, 9.1627535492), (-3.2924471555, 9.0246317251), (-3.3637900009, 8.9979428492), (-3.4350047965, 8.969517921), (-3.5062279788, 8.9393855764)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.25, 0.25, 0.25, 0.4614025533, 0.4614025533, 0.4614025533, 0.6626570309, 0.6626570309, 0.6626570309, 0.945371844, 0.945371844, 0.945371844, 1, 1, 1, 1], 3)
                Line((-3.5062279788, 8.9393855764), (-3.1289201809, 8.0475511576))
                _nurbs_edge([(-0.5113219983, 7.5), (-0.5508314035, 7.550143231), (-0.6309873923, 7.6469593154), (-0.7546328893, 7.7817723728), (-0.9264290109, 7.9403578672), (-1.1535039797, 8.1009622837), (-1.393956247, 8.2207426022), (-1.648793287, 8.296624269), (-1.9184080772, 8.3274080169), (-2.2020446538, 8.3154008544), (-2.4985715799, 8.2640556376), (-2.7452232142, 8.1942012282), (-2.9351737362, 8.1266682862), (-3.0639765006, 8.0750268375), (-3.1289201809, 8.0475511576)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1, 1, 1, 1, 1], 5)
            make_face()
        # OneSide extrude, distance=-1.1
        extrude(amount=-1.1, mode=Mode.ADD)
    return part.part


# Description: This is a curved blade or fin-like component with a tapered, elongated shape that narrows toward the pointed bottom end, featuring a slightly twisted profile along its length.
def model_54765_38755dca_0000():
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
        # Sketch17 -> Extrude9 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))) as sk:
            # Profile area: 11.6311298651, perimeter: 28.0791928465
            with BuildLine():
                _nurbs_edge([(-6, 15), (-6.0398971042, 14.8747240274), (-6.1197341038, 14.6255136287), (-6.2396179447, 14.2557226206), (-6.3997219349, 13.770776087), (-6.5997624406, 13.1781683923), (-6.7981248378, 12.5987041862), (-6.9915738053, 12.0309926957), (-7.1746511507, 11.4721936755), (-7.3389743308, 10.9173949394), (-7.4744830894, 10.3604574137), (-7.5708653047, 9.7949408845), (-7.6188804008, 9.2149293724), (-7.6121231244, 8.6160632674), (-7.548050168, 7.9961520605), (-7.4263259802, 7.3543429273), (-7.2835459166, 6.8233736503), (-7.1514344954, 6.4154357201), (-7.0523184854, 6.1391926618), (-7, 6)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0666666667, 0.1333333333, 0.2, 0.2666666667, 0.3333333333, 0.4, 0.4666666667, 0.5333333333, 0.6, 0.6666666667, 0.7333333333, 0.8, 0.8666666667, 0.9333333333, 1, 1, 1, 1, 1, 1], 5)
                Line((-6, 17), (-6, 15))
                _nurbs_edge([(-7, 3.5), (-7.1062018464, 3.6587585584), (-7.3097244277, 3.97818954), (-7.5883647999, 4.4630776711), (-7.9062123719, 5.1211614251), (-8.2120405639, 5.9633878151), (-8.4244434125, 6.8253721307), (-8.5427795283, 7.7066893655), (-8.5695381291, 8.6058345191), (-8.511434942, 9.5199431243), (-8.377361039, 10.445469809), (-8.1771385672, 11.3786604572), (-7.9203088544, 12.3160215023), (-7.6150551865, 13.2548370683), (-7.2675732462, 14.1934189075), (-6.8823039118, 15.1307890097), (-6.5461109088, 15.8793605495), (-6.2788799852, 16.4399890652), (-6.094069429, 16.8133885105), (-6, 17)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0666666667, 0.1333333333, 0.2, 0.2666666667, 0.3333333333, 0.4, 0.4666666667, 0.5333333333, 0.6, 0.6666666667, 0.7333333333, 0.8, 0.8666666667, 0.9333333333, 1, 1, 1, 1, 1, 1], 5)
                Line((-7, 6), (-7, 3.5))
            make_face()
        # TwoSides offset extrude, full=3, trim=2
        extrude(amount=3)
        extrude(sk.sketch, amount=2, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a modular solar panel array consisting of four connected trapezoidal/rectangular photovoltaic panels arranged in a linear configuration with articulated joints, featuring a segmented geometric surface design typical of space-based solar arrays.
def model_54812_5f7b7aba_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 18.75, perimeter: 20
            with BuildLine():
                Line((0, 2.5), (0, 0))
                Line((0, 0), (7.5, 0))
                Line((7.5, 0), (7.5, 2.5))
                Line((7.5, 2.5), (0, 2.5))
            make_face()
        # OneSide extrude, distance=4
        extrude(amount=4)

        # Sketch2 -> Extrude2 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 18.8351787218, perimeter: 20.0681429774
            with BuildLine():
                Line((10, 2.5), (10, 0))
                Line((10, 0), (17.5340714887, 0))
                Line((17.5340714887, 0), (17.5340714887, 2.5))
                Line((17.5340714887, 2.5), (10, 2.5))
            make_face()
        # OneSide extrude, distance=4
        extrude(amount=4)

        # Sketch3 -> Extrude3 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 7.4716538037, perimeter: 16.9433076073
            with BuildLine():
                Line((7.4716538037, -2), (0, -2))
                Line((7.4716538037, -1), (7.4716538037, -2))
                Line((0, -1), (7.4716538037, -1))
                Line((0, -2), (0, -1))
            make_face()
        # OneSide extrude, distance=4
        extrude(amount=4)

        # Sketch4 -> Extrude4 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 3.1563538442, perimeter: 15.8416943584
            with BuildLine():
                Line((-9.5, 0.4208471792), (-2, 0.4208471792))
                Line((-9.5, 0), (-9.5, 0.4208471792))
                Line((-2, 0), (-9.5, 0))
                Line((-2, 0.4208471792), (-2, 0))
            make_face()
        # OneSide extrude, distance=4.2
        extrude(amount=4.2)
    return part.part


# Description: This is a thumb screw or knob assembly featuring a cylindrical shaft perpendicular to a wide, flat circular base with radial knurled or textured grooves for grip, designed for manual hand operation.
def model_54965_75ba8fee_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch3 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1635664.7237031229, perimeter: 4533.6926581857
            Circle(721.5595970097)
        # OneSide extrude, distance=300
        extrude(amount=300)

        # Sketch4 -> Extrude2 (Join)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 300, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 144044.2552050989, perimeter: 1345.4045844194
            Circle(214.1277900688)
        # OneSide extrude, distance=1200
        extrude(amount=1200, mode=Mode.ADD)
    return part.part


# Description: This is a shaft or spindle assembly featuring a cylindrical shaft on the left that transitions to a larger circular disk or flange on the right, with a textured or mesh-like surface pattern visible on the disk portion.
def model_55026_4a1cbcd7_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 19.6349540849, perimeter: 15.7079632679
            Circle(2.5)
        # OneSide extrude, distance=7
        extrude(amount=7)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(7, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 30.6305283725, perimeter: 40.8407044967
            with BuildLine():
                CenterArc((0, 0), 4, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 2.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 19.6349540849, perimeter: 15.7079632679
            Circle(2.5)
        # OneSide extrude, distance=2
        extrude(amount=2, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 4.9087385212, perimeter: 7.853981634
            Circle(1.25)
        # OneSide extrude, distance=5
        extrude(amount=5, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(9, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 9.6211275016, perimeter: 10.9955742876
            Circle(1.75)
        # OneSide extrude, distance=-7
        extrude(amount=-7, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a shaft coupling or connector featuring a cylindrical shaft on the left end and a larger flanged disk on the right end, with a central axial hole running through the entire component for shaft insertion.
def model_55028_329486a0_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 19.6349540849, perimeter: 15.7079632679
            with Locations((0, -2.5)):
                Circle(2.5)
        # OneSide extrude, distance=7
        extrude(amount=7)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(7, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 31.4159265359, perimeter: 41.0362929814
            with BuildLine():
                CenterArc((0, -2.5), 4.0311288741, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, -2.5), 2.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 19.6349540849, perimeter: 15.7079632679
            with Locations((0, -2.5)):
                Circle(2.5)
        # OneSide extrude, distance=2
        extrude(amount=2, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 4.9087385212, perimeter: 7.853981634
            with Locations((0, -2.5)):
                Circle(1.25)
        # OneSide extrude, distance=5
        extrude(amount=5, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(9, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 9.6211275016, perimeter: 10.9955742876
            with Locations((0, -2.5)):
                Circle(1.75)
        # OneSide extrude, distance=-7.5
        extrude(amount=-7.5, mode=Mode.SUBTRACT)
    return part.part


# Description: A tilted rectangular box or frame structure with a hollow rectangular opening in the upper portion and internal triangulated wireframe geometry, featuring a solid base and open top design.
def model_55113_1c22a134_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 130, perimeter: 46
            with BuildLine():
                Line((5, -8), (-5, -8))
                Line((5, 5), (5, -8))
                Line((-5, 5), (5, 5))
                Line((-5, -8), (-5, 5))
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(2, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 50, perimeter: 30
            with BuildLine():
                Line((5, 0), (-5, 0))
                Line((5, 5), (5, 0))
                Line((-5, 5), (5, 5))
                Line((-5, 0), (-5, 5))
            make_face()
        # OneSide extrude, distance=-1.8
        extrude(amount=-1.8, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 13.2258340488, perimeter: 21.9553823386
            with BuildLine():
                Line((-1.7776910322, 4.8000000715), (-1.7776910322, -4.8000000715))
                Line((-1.7776910322, -4.8000000715), (-0.400000006, -4.8000000715))
                Line((-0.400000006, -4.8000000715), (-0.400000006, 4.8000000715))
                Line((-0.400000006, 4.8000000715), (-1.7776910322, 4.8000000715))
            make_face()
        # OneSide extrude, distance=-7.5
        extrude(amount=-7.5, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0.2, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 8, perimeter: 12
            with BuildLine():
                Line((2, 1), (-2, 1))
                Line((2, 3), (2, 1))
                Line((-2, 3), (2, 3))
                Line((-2, 1), (-2, 3))
            make_face()
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a bracket or mounting clamp featuring a rectangular body with two parallel extended flanges or arms that extend outward, designed to hold or secure cylindrical components or cables between its legs.
def model_55228_41934c1f_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 55, perimeter: 32
            with BuildLine():
                Line((-6.5, 5), (-6.5, 0))
                Line((-6.5, 0), (4.5, 0))
                Line((4.5, 0), (4.5, 5))
                Line((4.5, 5), (-6.5, 5))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.5, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.5437645683, perimeter: 2.6140289004
            with Locations((-5.6724856991, 4.2565541279)):
                Circle(0.4160356209)
            # Profile area: 0.5437645683, perimeter: 2.6140289004
            with Locations((-5.6724856991, 0.7434458721)):
                Circle(0.4160356209)
            # Profile area: 0.5438021564, perimeter: 2.6141192471
            with Locations((3.5795043798, 0.7434458721)):
                Circle(0.41605)
            # Profile area: 0.5438021564, perimeter: 2.6141192471
            with Locations((3.5795043798, 4.2565541279)):
                Circle(0.41605)
        # OneSide extrude, distance=7
        extrude(amount=7, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (NewBody)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.2827433388, perimeter: 5.6548667765
            with BuildLine():
                CenterArc((-10.7641802028, 1.561287384), 0.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-10.7641802028, 1.561287384), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            with Locations((-10.7641802028, 1.561287384)):
                Circle(0.4)
        # OneSide extrude, distance=1.8
        extrude(amount=1.8)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-1.8, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            with Locations((-10.7641802028, 1.561287384)):
                Circle(0.4)
        # OneSide extrude, distance=-1.6
        extrude(amount=-1.6, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical dowel pin or spacer with a slightly rounded end, featuring a smooth, uniform tubular body with what appears to be subtle surface texturing or markings along its length.
def model_55233_19fac79a_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 19.6349540849, perimeter: 15.7079632679
            Circle(2.5)
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1.5), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 3.7022924975, perimeter: 32.8329301197
            with BuildLine():
                CenterArc((0, 0), 2.7255231247, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 2.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 19.6349540849, perimeter: 15.7079632679
            Circle(2.5)
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)

        # Sketch2 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1.5), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 3.7022924975, perimeter: 32.8329301197
            with BuildLine():
                CenterArc((0, 0), 2.7255231247, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 2.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 19.6349540849, perimeter: 15.7079632679
            Circle(2.5)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)

        # Sketch3 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 2.5), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 19.6349540849, perimeter: 15.7079632679
            Circle(2.5)
        # OneSide extrude, distance=15
        extrude(amount=15, mode=Mode.ADD)
    return part.part


# Description: This is a double-ended open-face wrench with two opposing jaw pairs of different sizes at each end, connected by a long handle with vertical ribbing and blue metallic accents for grip and structural reinforcement.
def model_55236_e0bbfb4e_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 25 constraints, 10 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 36.0528244905, perimeter: 43.0874926439
            with BuildLine():
                CenterArc((2.8440271521, 8.8901124344), 0.2, -39.2526507709, 125.7490607534)
                CenterArc((2.7380986083, 7.1599751172), 1.9333770487, 86.4964099825, 93.4319935629)
                CenterArc((0.3047234595, 7.1630158494), 0.5, -56.6307800196, 56.559183565)
                Line((-5.1800219378, 2.9520191208), (0.5797395444, 6.7454441154))
                CenterArc((-5.4550380227, 3.3695908548), 0.5, -100.7529510882, 44.1221710685)
                CenterArc((-6, 0.5), 2.420879188, 79.2470489118, 84.8247936058)
                CenterArc((-7.9432906815, 1.0545935626), 0.4, 164.0718425176, 109.9297561394)
                CenterArc((-7.9230532323, 0.7653005526), 0.11, -85.9984013439, 16.7578029847)
                CenterArc((-22.4162879858, 39.0006016025), 41, -69.2405983592, 2.3335340948)
                CenterArc((-6, 0.5), 0.8544004256, -48.4143972335, 161.5073329687)
                CenterArc((10.1649479863, -17.7162366227), 23.5, 131.5856027662, 4.1350319754)
                CenterArc((-6.5809872607, -1.3863329884), 0.11, 135.7206347416, 21.9455985225)
                CenterArc((-6.3127413414, -1.4965333821), 0.4, 157.666233263, 103.4311741576)
                CenterArc((-6, 0.5), 2.420879188, -98.9025925793, 97.4826322749)
                CenterArc((-3.0800177626, 0.4276193119), 0.5, 128.8169433389, 49.7630963566)
                Line((-3.3934348863, 0.8171956286), (1.9749637557, 5.1361133588))
                CenterArc((2.2883808795, 4.746537042), 0.5, 79.4446173338, 49.3723260051)
                CenterArc((2.7380986083, 7.1599751172), 1.954980525, -100.5553826662, 97.4467559542)
                CenterArc((4.4904967087, 7.0648040035), 0.2, -3.108626712, 125.6178240307)
                Line((3.2289671296, 6.4979983687), (4.3830097116, 7.2334650406))
                CenterArc((2.7380986083, 7.1599751172), 0.8241147497, 131.2008682311, 175.3567793145)
                Line((2.9988998264, 8.7635642034), (2.1952535125, 7.7800431156))
            make_face()
        # Symmetric extrude, each_side=0.5
        extrude(amount=0.5, both=True)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 12 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-0.5, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 8.7148728993, perimeter: 14.1701487034
            with BuildLine():
                CenterArc((-0.5700435916, 4.9328130043), 0.25, 138.8754637543, 92.7611143885)
                Line((3.4521603101, 1.4301912568), (-0.7252054258, 4.7367905433))
                CenterArc((3.619735091, 1.6418955146), 0.27, -128.3634218572, 94.9942018768)
                Line((4.5197177462, 2.5175072737), (3.8452238274, 1.4933868288))
                CenterArc((4.3109318791, 2.6550153162), 0.25, -33.3692199804, 90)
                Line((4.4484399216, 2.8638011832), (0.0868011835, 5.7364113525))
                CenterArc((-0.050706859, 5.5276254855), 0.25, 56.6307800196, 82.2446837347)
                Line((-0.7583640441, 5.0972374769), (-0.2390273115, 5.692049958))
            make_face()
        # Symmetric extrude, each_side=-0.1
        extrude(amount=-0.1, both=True, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0.5, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 8.7148728993, perimeter: 14.1701487034
            with BuildLine():
                CenterArc((-3.619735091, 1.6418955146), 0.27, -146.6307800196, 94.9942018768)
                Line((0.7252054258, 4.7367905433), (-3.4521603101, 1.4301912568))
                CenterArc((0.5700435916, 4.9328130043), 0.25, -51.6365781428, 92.7611143885)
                Line((0.7583640441, 5.0972374769), (0.2390273115, 5.692049958))
                CenterArc((0.050706859, 5.5276254855), 0.25, 41.1245362457, 82.2446837347)
                Line((-4.4484399216, 2.8638011832), (-0.0868011835, 5.7364113525))
                CenterArc((-4.3109318791, 2.6550153162), 0.25, 123.3692199804, 90)
                Line((-3.8452238274, 1.4933868288), (-4.5197177462, 2.5175072737))
            make_face()
        # Symmetric extrude, each_side=-0.1
        extrude(amount=-0.1, both=True, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical shaft or axle with a central spherical joint or ball connector, featuring two elongated tubular sections connected through a rounded hub in the middle, commonly used in mechanical linkages or suspension systems.
def model_55323_716f61f1_0000():
    """Model: socket"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -2.5), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.3848451001, perimeter: 2.1991148575
            Circle(0.35)
        # Symmetric extrude, each_side=2
        extrude(amount=2, both=True)

        # Sketch2 -> Extrude2 (NewBody)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -2.5), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.6283185307, perimeter: 6.2831853072
            with BuildLine():
                CenterArc((0, 0), 0.6, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -4.5), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.3848451001, perimeter: 2.1991148575
            Circle(0.35)
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2, perimeter: 2.4
            with BuildLine():
                Line((0.0999999985, 1.1000000313), (-0.1000000015, 1.1000000313))
                Line((0.0999999985, 2.1000000313), (0.0999999985, 1.1000000313))
                Line((-0.1000000015, 2.1000000313), (0.0999999985, 2.1000000313))
                Line((-0.1000000015, 1.1000000313), (-0.1000000015, 2.1000000313))
            make_face()
        # Symmetric extrude, each_side=1.1
        extrude(amount=1.1, both=True, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a dual-channel connector or coupler featuring two parallel cylindrical bores with an elongated rectangular body, blue internal detailing or markings, and a compact, streamlined profile designed for fluid or pneumatic connections.
def model_55336_6181655b_0000():
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
        # Sketch has 7 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.7197512162, perimeter: 7.9017320276
            with BuildLine():
                CenterArc((2.0000000298, -1.2000000179), 0.5, 113.6623995324, 141.0572466177)
                CenterArc((1.6468361512, 0.4831743586), 1.2346643474, -158.3554327103, 75.4500150492)
                CenterArc((0, 0), 0.5, -94.8222482213, 98.0062430886)
                CenterArc((0.885435032, -1.2374620518), 1.186026825, 141.4436294497, 78.5994548165)
                CenterArc((0, -2.5000000373), 0.5, -3.0646076847, 95.6484575112)
                CenterArc((1.7379207088, -3.0029320292), 1.3270214577, 84.3647035795, 74.6057393524)
            make_face()
            # Profile area: 0.7829513368, perimeter: 3.1401085371
            with BuildLine():
                CenterArc((2.0000000298, -1.2000000179), 0.5, 113.6623995324, 141.0572466177)
                CenterArc((1.7379207088, -3.0029320292), 1.3270214577, 79.0938016279, 5.2709019516)
                CenterArc((2.0000000298, -1.2000000179), 0.5, -91.2611409426, 181.2985587217)
                CenterArc((1.6468361512, 0.4831743586), 1.2346643474, -82.9054176611, 9.5106526338)
            make_face()
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with BuildLine():
                CenterArc((0, 0), 0.5, 3.1839948673, 261.9937569114)
                CenterArc((0, 0), 0.5, -94.8222482213, 98.0062430886)
            make_face()
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with BuildLine():
                CenterArc((0, -2.5000000373), 0.5, 92.5838498264, 264.3515424888)
                CenterArc((0, -2.5000000373), 0.5, -3.0646076847, 95.6484575112)
            make_face()
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2513274198, perimeter: 1.7771532017
            with Locations((2.0000000298, -1.2000000179)):
                Circle(0.2828427167)
            # Profile area: 0.319770962, perimeter: 2.0045848499
            with Locations((0, -2.5)):
                Circle(0.3190395877)
            # Profile area: 0.2513274198, perimeter: 1.7771532017
            Circle(0.2828427167)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0176714587, perimeter: 0.471238898
            with BuildLine():
                CenterArc((-3.5000000522, 0), 0.075, 99.5372158788, 295.9228714666)
                CenterArc((-3.5000000522, 0), 0.075, 35.4600873454, 64.0771285334)
            make_face()
        # OneSide extrude, distance=0.05
        extrude(amount=0.05)

        # Sketch4 -> Extrude4 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))) as sk:
            # Profile area: 0.0089991642, perimeter: 0.477778756
            with BuildLine():
                CenterArc((-3.5000000522, 0), 0.075, -19.7995417263, 65.6929536388)
                _nurbs_edge([(-3.4294337913, -0.0254047796), (-3.4154109112, -0.0248465023), (-3.3886334049, -0.0236394449), (-3.3522718506, -0.0215573544), (-3.3115248587, -0.0182292573), (-3.274347737, -0.0130874617), (-3.2521167562, -0.0068791071), (-3.2459897629, 0.0004784303), (-3.2564840426, 0.0090220643), (-3.2828118485, 0.0186955811), (-3.3237234557, 0.0294098001), (-3.3671352198, 0.0387434786), (-3.4053169216, 0.0461449869), (-3.4332295317, 0.0512547391), (-3.4478003998, 0.0538534706)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1, 1, 1, 1, 1], 5)
            make_face()
        # TwoSides offset extrude, full=0.03, trim=0.01
        extrude(amount=0.03)
        extrude(sk.sketch, amount=0.01, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a complex molded or cast component with an irregular, asymmetrical shape featuring multiple recessed slots, angled surfaces, and a curved left side, designed with both flat and contoured faces for structural or mechanical assembly purposes.
def model_55348_bf8fb35c_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 200, perimeter: 60
            with BuildLine():
                Line((-5.7991522439, -6.2967370182), (-5.7991522439, 3.7032629818))
                Line((-5.7991522439, 3.7032629818), (-25.7991522439, 3.7032629818))
                Line((-25.7991522439, 3.7032629818), (-25.7991522439, -6.2967370182))
                Line((-25.7991522439, -6.2967370182), (-5.7991522439, -6.2967370182))
            make_face()
        # OneSide extrude, distance=25
        extrude(amount=25)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 3.7032629818, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 157.4146971156, perimeter: 51.2208774355
            with BuildLine():
                Line((-20.3903993558, 20.1160123624), (-5.0241361251, 20.1160123624))
                Line((-20.3903993558, 9.8718368753), (-20.3903993558, 20.1160123624))
                Line((-5.0241361251, 9.8718368753), (-20.3903993558, 9.8718368753))
                Line((-5.0241361251, 20.1160123624), (-5.0241361251, 9.8718368753))
            make_face()
        # OneSide extrude, distance=10
        extrude(amount=10, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 24.7078213053, perimeter: 24.9595104443
            with BuildLine():
                Line((9.8718368753, 3.7032629818), (5.7991522439, 3.7032629818))
                Line((9.8718368753, 13.7032629818), (9.8718368753, 3.7032629818))
                CenterArc((29.9756600438, -0.3137281887), 24.5079527392, 145.1146299117, 25.4517045144)
            make_face()
        # OneSide extrude, distance=-25
        extrude(amount=-25, mode=Mode.ADD)
    return part.part


# Description: This is a complex multi-faceted 3D component with an irregular polyhedron shape, featuring angular surfaces, internal cavities or slots, and a stepped geometric profile suggesting it may be a structural bracket, connector, or specialized mechanical part with interlocking geometric features.
def model_55476_1473d91f_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 36, perimeter: 26
            with BuildLine():
                Line((10, 1), (1, 1))
                Line((10, 5), (10, 1))
                Line((1, 5), (10, 5))
                Line((1, 1), (1, 5))
            make_face()
        # OneSide extrude, distance=5
        extrude(amount=5)

        # Sketch6 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 5), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 5, perimeter: 9
            with BuildLine():
                Line((6, 2.5), (3.5, 2.5))
                Line((6, 4.5), (6, 2.5))
                Line((3.5, 4.5), (6, 4.5))
                Line((3.5, 2.5), (3.5, 4.5))
            make_face()
        # OneSide extrude, distance=6
        extrude(amount=6, mode=Mode.ADD)
    return part.part


# Description: This is a pneumatic or hydraulic actuator cylinder with a cylindrical barrel body, a central rod extending upward, and a flanged base with mounting holes for attachment.
def model_55481_a0e762b2_0000():
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
        # Sketch3 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 262.4096966005, perimeter: 57.4241891565
            Circle(9.1393435573)
        # OneSide extrude, distance=7.5
        extrude(amount=7.5)

        # Sketch4 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 7.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 10.9533820727, perimeter: 11.7321889947
            Circle(1.8672358718)
        # OneSide extrude, distance=30
        extrude(amount=30, mode=Mode.ADD)

        # Sketch5 -> Extrude3 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 13.6489913668, perimeter: 19.1720944261
            with BuildLine():
                Line((7.9371328819, 0), (5, 0))
                _nurbs_edge([(7.9371328819, 0), (8.0278850763, -0.7307049081), (8.1920506759, -2.1060511606), (8.3862838435, -3.9108854168), (8.5404647263, -5.7971582769), (8.5562886569, -7.2765757186), (8.3963606545, -7.8822472578), (8.0698374361, -7.6575193015), (7.5982444818, -6.7057267539), (7.0226724722, -5.2253765631), (6.3986203149, -3.4850934061), (5.828698543, -1.8976464442), (5.43067232, -0.8745671944), (5.1843096886, -0.3304360129), (5.0502272639, -0.0831797665), (5, 0)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0666666667, 0.1333333333, 0.2, 0.2666666667, 0.3333333333, 0.4, 0.4666666667, 0.5333333333, 0.6, 0.6666666667, 0.7110024727, 0.7110024727, 0.7110024727, 0.7110024727, 0.7110024727, 0.7110024727], 5)
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2)
    return part.part


# Description: This is a rectangular duct or channel bracket with a hollow, box-like structure featuring two internal vertical dividers/webs and multiple rectangular openings or ports on its sides for fluid or cable routing.
def model_55521_d587e636_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 9 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 28.5, perimeter: 34
            with BuildLine():
                Line((-14, 0), (-10.5, 0))
                Line((-10.5, 0), (-10.5, 2.5))
                Line((-10.5, 2.5), (-6.5, 2.5))
                Line((-6.5, 2.5), (-6.5, 0))
                Line((-6.5, 0), (-3, 0))
                Line((-3, 0), (-3, 3.5))
                Line((-3, 3.5), (-14, 3.5))
                Line((-14, 3.5), (-14, 0))
            make_face()
            # Profile area: 27.5, perimeter: 27
            with BuildLine():
                Line((-3, 3.5), (-14, 3.5))
                Line((-3, 6), (-3, 3.5))
                Line((-3, 6), (-14, 6))
                Line((-14, 6), (-14, 3.5))
            make_face()
        # Symmetric extrude, each_side=3
        extrude(amount=3, both=True)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 6, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 22, perimeter: 26
            with BuildLine():
                Line((14, 3), (3, 3))
                Line((3, 3), (3, 1))
                Line((3, 1), (14, 1))
                Line((14, 1), (14, 3))
            make_face()
        # OneSide extrude, distance=-4
        extrude(amount=-4, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 6, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            with Locations((12, -1)):
                Circle(1)
        # OneSide extrude, distance=-10
        extrude(amount=-10, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on XZ construction plane
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            with Locations((-5, 1)):
                Circle(1)
        # OneSide extrude, distance=19.5
        extrude(amount=19.5, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a lathe tool holder or turning insert with an elongated rectangular body, a tapered/angled cutting end, and a mounting slot or cavity on the underside for securing to a machine tool.
def model_55546_670606b4_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 8 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 13.75, perimeter: 16
            with BuildLine():
                Line((0, 1), (0, -4.5))
                Line((0, -4.5), (2.5, -4.5))
                Line((2.5, -4.5), (2.5, 1))
                Line((2.5, 1), (0, 1))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 4.5), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1.1271889092, perimeter: 5.0705855132
            with BuildLine():
                Line((2.2456423407, 0.1738042359), (0.2853644361, 0.1738042359))
                Line((2.2456423407, 0.7488190879), (2.2456423407, 0.1738042359))
                Line((0.2853644361, 0.7488190879), (2.2456423407, 0.7488190879))
                Line((0.2853644361, 0.1738042359), (0.2853644361, 0.7488190879))
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 6.5), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.3600000107, perimeter: 4.0000000596
            with BuildLine():
                Line((2.2000000328, 0.5000000075), (0.400000006, 0.5000000075))
                Line((2.2000000328, 0.7000000104), (2.2000000328, 0.5000000075))
                Line((0.400000006, 0.7000000104), (2.2000000328, 0.7000000104))
                Line((0.400000006, 0.5000000075), (0.400000006, 0.7000000104))
            make_face()
        # OneSide extrude, distance=-2
        extrude(amount=-2, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 8 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.7488190879, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1200000036, perimeter: 1.4000000209
            with BuildLine():
                Line((-0.9000000134, 5.500000082), (-0.6000000089, 5.500000082))
                Line((-0.9000000134, 5.100000076), (-0.9000000134, 5.500000082))
                Line((-0.6000000089, 5.100000076), (-0.9000000134, 5.100000076))
                Line((-0.6000000089, 5.500000082), (-0.6000000089, 5.100000076))
            make_face()
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.7488190879, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1200000036, perimeter: 1.4000000209
            with BuildLine():
                Line((-1.9000000283, 5.500000082), (-1.6000000238, 5.500000082))
                Line((-1.9000000283, 5.100000076), (-1.9000000283, 5.500000082))
                Line((-1.6000000238, 5.100000076), (-1.9000000283, 5.100000076))
                Line((-1.6000000238, 5.500000082), (-1.6000000238, 5.100000076))
            make_face()
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical capsule or rounded rectangular tube with two hemispherical ends and a central cylindrical body, featuring a highly detailed mesh surface pattern typical of finite element analysis visualization.
def model_55594_791079ce_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch8 -> Extrude4 (NewBody)
        # Sketch on YZ construction plane
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.1309733553, perimeter: 3.7699111843
            with Locations((-1.6000000238, 0)):
                Circle(0.6)
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)
    return part.part


# Description: This is a butterfly net consisting of a circular mesh net head mounted on a long handle, used for catching insects and small flying creatures.
def model_55611_69142616_0000():
    """Model: starter grip"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.1309733553, perimeter: 3.7699111843
            with Locations((20, -15)):
                Circle(0.6)
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1963495408, perimeter: 7.853981634
            with BuildLine():
                CenterArc((-20, 15), 0.65, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-20, 15), 0.6, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 1.1309733553, perimeter: 3.7699111843
            with Locations((-20, 15)):
                Circle(0.6)
        # OneSide extrude, distance=1.5
        extrude(amount=1.5, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.8994866864, perimeter: 10.0474053363
            with BuildLine():
                Line((-19.9817699503, 14.3502556924), (-16.9911800193, 14.3922013294))
                CenterArc((-17.0002950442, 15.0420734832), 0.6499360738, -89.1964293179, 180)
                Line((-17.009410069, 15.691945637), (-20, 15.65))
                CenterArc((-20, 15), 0.65, -88.3928586349, 178.3928586349)
            make_face()
            # Profile area: 3.8994866864, perimeter: 10.0474053363
            with BuildLine():
                CenterArc((-20, 15), 0.65, 91.6071413651, 178.3928586349)
                Line((-20.0182300497, 15.6497443076), (-23.0088199807, 15.6077986706))
                CenterArc((-22.9997049558, 14.9579265168), 0.6499360738, 90.8035706821, 180)
                Line((-22.990589931, 14.308054363), (-20, 14.35))
            make_face()
            # Profile area: 1.3273213421, perimeter: 4.0840692542
            with BuildLine():
                CenterArc((-20, 15), 0.65, 91.6071413651, 178.3928586349)
                Line((-20, 14.35), (-19.9817699503, 14.3502556924))
                CenterArc((-20, 15), 0.65, -88.3928586349, 178.3928586349)
                Line((-20, 15.65), (-20.0182300497, 15.6497443076))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 11 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0.2233954804, 0, 15.9273841595), x_dir=(0.9999016519, 0, -0.0140244944), z_dir=(0.0140244944, 0, 0.9999016519))):
            # Profile area: 0.3374547018, perimeter: 6.3636933863
            with BuildLine():
                CenterArc((19.7805745045, -10.0309750916), 13.5309769497, 77.159511061, 12.8104621955)
                Line((22.7876656229, 3.1616266313), (22.7876656229, 3.5))
                Line((22.7876656229, 3.5), (19.7876656229, 3.5))
            make_face()
            # Profile area: 0.302927995, perimeter: 8.2974693851
            with BuildLine():
                CenterArc((19.7805745045, -10.0309750916), 13.5309769497, 89.9699732564, 0.0300267436)
                Line((22.7876656229, 3.5), (19.7876656229, 3.5))
                Line((22.7876656229, 3.1616266313), (22.7876656229, 3.5))
                CenterArc((19.7805745045, -10.0309750916), 13.5309769497, 74.3755273891, 2.7839836719)
                Line((23.5000003502, 3.0000000447), (23.4248886204, 3))
                Line((23.5, 3.5000018581), (23.5000003502, 3.0000000447))
                Line((19.7805745045, 3.5000018581), (23.5, 3.5000018581))
            make_face()
            # Profile area: 0.5882794605, perimeter: 9.4169044278
            with BuildLine():
                CenterArc((19.7805745045, -10.0309750916), 13.5309769497, 90, 0.0300267436)
                Line((19.7805745045, 3.5000018581), (15.5, 3.5000018581))
                Line((15.5, 3.5000018581), (15.5, 3))
                Line((16.1362603886, 3), (15.5, 3))
                CenterArc((19.7805745045, -10.0309750916), 13.5309769497, 102.7789026837, 2.8455699272)
                Line((16.7876656229, 3.5), (16.7876656229, 3.1648512804))
                Line((19.7734833861, 3.5), (16.7876656229, 3.5))
            make_face()
            # Profile area: 0.3326786959, perimeter: 6.3317422842
            with BuildLine():
                Line((19.7734833861, 3.5), (16.7876656229, 3.5))
                Line((16.7876656229, 3.5), (16.7876656229, 3.1648512804))
                CenterArc((19.7805745045, -10.0309750916), 13.5309769497, 90.0300267436, 12.7488759401)
            make_face()
        # OneSide extrude, distance=-2
        extrude(amount=-2, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((20, 15)):
                Circle(0.2)
        # OneSide extrude, distance=6
        extrude(amount=6, mode=Mode.ADD)
    return part.part


# Description: This is a boat hull with an elongated, oval-shaped cross-section featuring a curved bottom, flared sides, an open top deck with internal ribbing and structural supports, and a pointed bow and stern design.
def model_55611_69142616_0009():
    """Model: deflector"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 19 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))) as sk:
            # Profile area: 566.0382606414, perimeter: 90.1058814529
            with BuildLine():
                CenterArc((-9.8498737342, 89.4643354119), 5, 180, 41.4096221093)
                CenterArc((5.1501262658, 102.6930919672), 25, -138.5903778907, 78.5903778907)
                CenterArc((15.1501262658, 85.3725838915), 5, -60, 60)
                Line((20.1501262658, 85.3725838915), (20.1501262658, 90.0717275579))
                CenterArc((15.1501262658, 90.0717275579), 5, 0, 59.1481140139)
                CenterArc((5.6501262658, 74.1680919672), 23.525, 59.1481140139, 30.8518859861)
                Line((5.6501262658, 97.6930919672), (-0.3498737342, 97.6930919672))
                CenterArc((-0.3498737342, 74.1680919672), 23.525, 90, 30.8518859861)
                CenterArc((-9.8498737342, 90.0717275579), 5, 120.8518859861, 59.1481140139)
                Line((-14.8498737342, 89.4643354119), (-14.8498737342, 90.0717275579))
            make_face()
        # TwoSides offset extrude, full=15, trim=5
        extrude(amount=15)
        extrude(sk.sketch, amount=5, mode=Mode.SUBTRACT)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-14.8498737342, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 18.4560898852, perimeter: 27.3209314725
            with BuildLine():
                Line((-89.4643354119, 14.5015447331), (-89.4643354119, 15))
                CenterArc((-97.6930919672, -53.1715056561), 68.1715056561, 72.939078841, 10.1280319569)
                Line((-77.692366132, 15), (-77.692366132, 12))
                Line((-77.692366132, 15), (-89.4643354119, 15))
            make_face()
            # Profile area: 1.0843291712, perimeter: 15.6860568701
            with BuildLine():
                Line((-90.0717275579, 15), (-90.0717275579, 14.5726379134))
                Line((-90.0717275579, 15), (-97.6930919672, 15))
                CenterArc((-97.6930919672, -53.1715056561), 68.1715056561, 83.5810894454, 6.4189105546)
            make_face()
            # Profile area: 0.2808875249, perimeter: 2.14475015
            with BuildLine():
                CenterArc((-97.6930919672, -53.1715056561), 68.1715056561, 83.0671107979, 0.5139786475)
                Line((-89.4643354119, 14.5015447331), (-89.4643354119, 15))
                Line((-89.4643354119, 15), (-90.0717275579, 15))
                Line((-90.0717275579, 15), (-90.0717275579, 14.5726379134))
            make_face()
        # OneSide extrude, distance=-42
        extrude(amount=-42, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -97.6930919672), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 64.0447092379, perimeter: 77.7691022502
            with BuildLine():
                Line((0.3498737342, 14.9281338021), (0.3498737342, 15))
                CenterArc((-2.6501262658, -47.4954924209), 62.4956727368, 73.7386381832, 13.5099165817)
                Line((15, 16), (14.8498737342, 12.5))
                Line((-20.1501262658, 16), (15, 16))
                Line((-20.1501262658, 12.5), (-20.1501262658, 16))
                CenterArc((-2.6501262658, -47.4954924209), 62.4956727368, 92.7514452351, 13.5099165817)
                Line((-5.6501262658, 15), (-5.6501262658, 14.9281338021))
                Line((-2.8002525317, 15), (-5.6501262658, 15))
                CenterArc((-2.6501262658, -47.4954924209), 62.4956727368, 89.8623647155, 0.2752705691)
                Line((0.3498737342, 15), (-2.5, 15))
            make_face()
        # OneSide extrude, distance=-22.5
        extrude(amount=-22.5, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 16 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 5, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 537.1545757674, perimeter: 88.0680844426
            with BuildLine():
                Line((17.4578185735, -93.9349588754), (17.4578185735, -94.5151808835))
                CenterArc((15.1501262658, -90.0717275579), 4.5, -59.1481140139, 59.1481140139)
                Line((19.6501262658, -90.0717275579), (19.6501262658, -85.3725838915))
                CenterArc((15.1501262658, -85.3725838915), 4.5, 0, 60)
                CenterArc((5.1501262658, -102.6930919672), 24.5, 60, 78.5903778907)
                CenterArc((-9.8498737342, -89.4643354119), 4.5, 138.5903778907, 41.4096221093)
                Line((-14.3498737342, -89.4643354119), (-14.3498737342, -90.0717275579))
                CenterArc((-9.8498737342, -90.0717275579), 4.5, 180, 59.1481140139)
                Line((-12.1575660418, -93.9349588754), (-12.1575660418, -94.5151808835))
                CenterArc((-0.3498737342, -74.1680919672), 23.525, -120.1271761313, 30.1271761313)
                Line((-0.3498737342, -97.6930919672), (5.6501262658, -97.6930919672))
                CenterArc((5.6501262658, -74.1680919672), 23.525, -90, 30.1271761313)
            make_face()
        # OneSide extrude, distance=-7
        extrude(amount=-7, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(20.1501262658, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 7.1761181929, perimeter: 12.9721948731
            with BuildLine():
                CenterArc((79.1803398461, 29.2061477223), 24.2776660199, -75.2229021294, 11.8779258124)
                Line((85.3725838915, 5.7314553696), (85.3725838915, 5))
                Line((90.0717275579, 5), (85.3725838915, 5))
                Line((90.0717275579, 5), (90.0717275579, 7.5086192666))
            make_face()
            # Profile area: 1.2922327226, perimeter: 9.4590635508
            with BuildLine():
                Line((85.3725838915, 5.7314553696), (85.3725838915, 5))
                CenterArc((79.1803398461, 29.2061477223), 24.2776660199, -85.601046012, 10.3781438827)
                Line((85.3725838915, 5), (81.0424568726, 5))
            make_face()
            # Profile area: 38.7847709185, perimeter: 28.3899984436
            with BuildLine():
                Line((90.0717275579, 5), (90.0717275579, 7.5086192666))
                Line((97.6930919672, 5), (90.0717275579, 5))
                Line((97.6930919672, 13.5), (97.6930919672, 5))
                CenterArc((79.1803398461, 29.2061477223), 24.2776660199, -63.3449763169, 23.0338309173)
            make_face()
        # OneSide extrude, distance=-38
        extrude(amount=-38, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a satellite or spacecraft component featuring a boxy, rectangular main body with protruding solar panels, antennas, and communication equipment mounted on top, characterized by angular faceted surfaces and external mounting brackets.
def model_55634_3b61fa4d_0000():
    """Model: servo"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.76, perimeter: 7
            with BuildLine():
                Line((6.2, -7.3), (5, -7.3))
                Line((6.2, -5), (6.2, -7.3))
                Line((5, -5), (6.2, -5))
                Line((5, -7.3), (5, -5))
            make_face()
        # OneSide extrude, distance=2.4
        extrude(amount=2.4)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 7.3), x_dir=(1, 0, 0), z_dir=(0, 0, 1))) as sk:
            # Profile area: 0.372, perimeter: 3.02
            with BuildLine():
                Line((5, 2.26), (6.2, 2.26))
                Line((5, 1.95), (5, 2.26))
                Line((6.2, 1.95), (5, 1.95))
                Line((6.2, 2.26), (6.2, 1.95))
            make_face()
        # TwoSides extrude, along=0.45, against=-2.75
        extrude(amount=0.45, mode=Mode.ADD)
        extrude(sk.sketch, amount=-2.75, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 8 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2.4, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.4948008429, perimeter: 6.5973445725
            with BuildLine():
                CenterArc((-5.6, 5.6), 0.6, 0, 180)
                CenterArc((-5.6, 5.6), 0.6, 180, 90)
                CenterArc((-5.6, 5.6), 0.6, -90, 90)
            make_face()
            with BuildLine():
                CenterArc((-5.6, 5.6), 0.45, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.5105088062, perimeter: 4.0840704497
            with BuildLine():
                CenterArc((-5.6, 5.6), 0.45, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-5.6, 5.6), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((-5.6, 5.6)):
                Circle(0.2)
        # OneSide extrude, distance=0.45
        extrude(amount=0.45, mode=Mode.ADD)

        # Sketch3 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 8 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2.4, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.5105088062, perimeter: 4.0840704497
            with BuildLine():
                CenterArc((-5.6, 5.6), 0.45, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-5.6, 5.6), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.6
        extrude(amount=0.6, mode=Mode.ADD)

        # Sketch3 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 8 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2.4, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((-5.6, 5.6)):
                Circle(0.2)
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)

        # Sketch3 -> Extrude6 (Cut)
        # Sketch on BRepFace
        # Sketch has 8 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2.4, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((-5.6, 7.65)):
                Circle(0.15)
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((-5.6, 4.65)):
                Circle(0.15)
        # OneSide extrude, distance=-1.1
        extrude(amount=-1.1, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a metal angle bracket or corner brace with an L-shaped profile, featuring two perpendicular arms connected at a joint with a mounting hole at the apex for fastening.
def model_55636_6180bfce_0006():
    """Model: pata 1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 12 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 11.3978196423, perimeter: 16.0127813655
            with BuildLine():
                CenterArc((-26.6242861563, 55.4260897529), 3.8797709054, 95.8343781637, 59.1656218363)
                Line((-30.1405527398, 57.0657517889), (-26.6249504897, 57.0973905833))
                Line((-23.0575169787, 56.9527789525), (-26.6249504897, 57.0973905833))
                CenterArc((-26.6242861563, 55.4260897529), 3.8797709054, 23.172445223, 57.567951379)
                CenterArc((-26.6242861563, 55.4260897529), 3.8797709054, 80.740396602, 15.0939815617)
            make_face()
            # Profile area: 199.5877966876, perimeter: 132.9108020596
            with BuildLine():
                Line((0, 0), (-26.6249504897, 57.0973905833))
                Line((0, 0), (3.5, 0))
                Line((3.5, 0), (-23.0575169787, 56.9527789525))
                Line((-23.0575169787, 56.9527789525), (-26.6249504897, 57.0973905833))
            make_face()
            # Profile area: 4.2856069925, perimeter: 10.4996949551
            with BuildLine():
                CenterArc((-26.6242861563, 55.4260897529), 3.8797709054, 80.740396602, 15.0939815617)
                Line((-26, 63.5), (-26, 59.2553049562))
                Line((-27.0186773596, 63.5), (-26, 63.5))
                Line((-27.0186773596, 59.2857630366), (-27.0186773596, 63.5))
            make_face()
            # Profile area: 199.8375942736, perimeter: 132.9831308718
            with BuildLine():
                Line((-56.7508102858, -0.0001296752), (-30.1405527398, 57.0657517889))
                Line((-53.2508107597, -0.0019510303), (-56.7508102858, -0.0001296752))
                Line((-26.6249504897, 57.0973905833), (-53.2508107597, -0.0019510303))
                Line((-30.1405527398, 57.0657517889), (-26.6249504897, 57.0973905833))
            make_face()
        # OneSide extrude, distance=-4
        extrude(amount=-4)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 8 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(-27.0186773596, 0, -0.0000000024), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 8.0000000034, perimeter: 12.0000000017
            with BuildLine():
                Line((0.0000000024, 63.5000000009), (-3.9999999976, 63.5000000009))
                Line((-3.9999999976, 63.5000000009), (-3.9999999976, 61.5))
                Line((-3.9999999976, 61.5), (-3.5, 61.5))
                Line((-3.5, 61.5), (-0.5, 61.5))
                Line((-0.5, 61.5), (0.0000000024, 61.5))
                Line((0.0000000024, 61.5), (0.0000000024, 63.5000000009))
            make_face()
            # Profile area: 6.6427108877, perimeter: 10.4284739251
            with BuildLine():
                Line((-3.5, 61.5), (-3.5, 59.2857630374))
                Line((-3.5, 59.2857630374), (-0.5, 59.2857630374))
                Line((-0.5, 59.2857630374), (-0.5, 61.5))
                Line((-3.5, 61.5), (-0.5, 61.5))
            make_face()
            # Profile area: 11.8389597869, perimeter: 23.3539443389
            with BuildLine():
                Line((0.0000000024, 61.5), (0.0000000024, 63.5000000009))
                Line((0.0000000024, 61.5), (1.5, 61.5))
                Line((1.5, 61.5), (1, 64.5))
                Line((1, 64.5), (-5.7259731936, 64.5))
                Line((-5.7259731936, 64.5), (-5, 61.5))
                Line((-5, 61.5), (-3.9999999976, 61.5))
                Line((-3.9999999976, 63.5000000009), (-3.9999999976, 61.5))
                Line((0.0000000024, 63.5000000009), (-3.9999999976, 63.5000000009))
            make_face()
        # OneSide extrude, distance=-1.5
        extrude(amount=-1.5, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0.0000000033, 0, -3.5000000024), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.8497124459, perimeter: 3.2770921723
            with BuildLine():
                CenterArc((-26.5, 61), 0.5230921818, 17.0880222627, 55.8239566998)
                Line((-26.3462943375, 61.5), (-26.6537056625, 61.5))
                CenterArc((-26.5, 61), 0.5230921818, 107.0880210375, 65.4627575404)
                Line((-27.0186773629, 61.0678175778), (-27.0186773629, 60.9321824222))
                CenterArc((-26.5, 61), 0.5230921818, -172.5507785779, 155.4627563151)
                Line((-26.0000000033, 60.8462943268), (-26.0000000033, 61.1537056732))
            make_face()
        # OneSide extrude, distance=3
        extrude(amount=3, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0.0000000033, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.3301734544, perimeter: 2.6416681572
            with BuildLine():
                Line((-26.624950493, 57.0973905842), (-26.2320816898, 56.254880717))
                Line((-27.0168431784, 56.2569740081), (-26.624950493, 57.0973905842))
                Line((-27.0168431784, 56.2569740081), (-26.2320816898, 56.254880717))
            make_face()
        # OneSide extrude, distance=-4
        extrude(amount=-4, mode=Mode.ADD)

        # Sketch5 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-0.00000013, -0.0000007447, 0), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            with Locations((-14.6450006956, 35.7090016961)):
                Circle(1)
        # OneSide extrude, distance=-4.5
        extrude(amount=-4.5, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a rectangular panel or plate with a recessed central surface and reinforcing ribs or flanges along its edges, featuring a trapezoidal or tapered overall geometry.
def model_55742_8008d3fe_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 181.5039860791, perimeter: 54.0693640947
            with BuildLine():
                Line((3.1749887294, -7.1193946843), (-9.2402986337, -7.1193946843))
                Line((3.1749887294, 7.5), (3.1749887294, -7.1193946843))
                Line((-9.2402986337, 7.5), (3.1749887294, 7.5))
                Line((-9.2402986337, -7.1193946843), (-9.2402986337, 7.5))
            make_face()
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(1.5, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 138.1234270237, perimeter: 47.1692935215
            with BuildLine():
                Line((2.3129071915, -6.1929320009), (-8.5122224731, -6.1929320009))
                Line((2.3129071915, 6.5665850952), (2.3129071915, -6.1929320009))
                Line((-8.5122224731, 6.5665850952), (2.3129071915, 6.5665850952))
                Line((-8.5122224731, -6.1929320009), (-8.5122224731, 6.5665850952))
            make_face()
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.SUBTRACT)

        # Sketch12 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 7.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 5.8451606255, perimeter: 24.3806425019
            with BuildLine():
                Line((-1, 9), (-0.5, 9))
                Line((-1, -2.6903212509), (-1, 9))
                Line((-0.5, -2.6903212509), (-1, -2.6903212509))
                Line((-0.5, 9), (-0.5, -2.6903212509))
            make_face()
        # OneSide extrude, distance=-14.5
        extrude(amount=-14.5, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a bevel gear featuring a large conical wheel with radial teeth meshed with a perpendicular shaft, designed to transmit rotational motion between perpendicular axes.
def model_56065_00bbe5da_0014():
    """Model: Cylinder_Cover v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 16.6190251375, perimeter: 14.4513262065
            Circle(2.3)
        # Symmetric extrude, each_side=0.25
        extrude(amount=0.25, both=True)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 0, 0.25), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 2.0106192983, perimeter: 5.0265482457
            Circle(0.8)
        # OneSide extrude, distance=2.7
        extrude(amount=2.7, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 0, 2.95), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            Circle(0.25)
        # OneSide extrude, distance=-9.5
        extrude(amount=-9.5, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.25), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.3848451001, perimeter: 2.1991148575
            with Locations((0, 1.5)):
                Circle(0.35)
        # OneSide extrude, distance=-2.3
        extrude(amount=-2.3, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a 3D CAD model of a rectangular platform or frame structure supported by four cylindrical legs with a distinctive angular or sloped top surface featuring geometric faceting.
def model_56356_95c9f867_0001():
    """Model: Untitled"""
    with BuildPart() as part:
        # escritorio -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 10 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 3791.3960836975, perimeter: 494.1720783261
            with BuildLine():
                Line((100, 52.086039163), (0, 52.086039163))
                Line((100, 0), (100, 52.086039163))
                Line((110, 0), (100, 0))
                Line((110, 75), (110, 0))
                Line((-10, 75), (110, 75))
                Line((-10, 0), (-10, 75))
                Line((0, 0), (-10, 0))
                Line((0, 52.086039163), (0, 0))
            make_face()
        # Symmetric extrude, each_side=40
        extrude(amount=40, both=True)

        # Sketch2 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(110, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 2000, perimeter: 180
            with BuildLine():
                Line((20, 0), (20, 50))
                Line((20, 50), (-20, 50))
                Line((-20, 50), (-20, 0))
                Line((-20, 0), (20, 0))
            make_face()
        # OneSide extrude, distance=-145
        extrude(amount=-145, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -40), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 700, perimeter: 160
            with BuildLine():
                Line((-15, 55), (-85, 55))
                Line((-15, 65), (-15, 55))
                Line((-85, 65), (-15, 65))
                Line((-85, 55), (-85, 65))
            make_face()
        # OneSide extrude, distance=-30
        extrude(amount=-30, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude5 (NewBody)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -40), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 684.5442452543, perimeter: 159.2123788006
            with BuildLine():
                Line((-15.100000225, 55.1000008211), (-84.8987963248, 55.1000008211))
                Line((-15.100000225, 64.9073941216), (-15.100000225, 55.1000008211))
                Line((-84.8987963248, 64.9073941216), (-15.100000225, 64.9073941216))
                Line((-84.8987963248, 55.1000008211), (-84.8987963248, 64.9073941216))
            make_face()
        # OneSide extrude, distance=28
        extrude(amount=28)
    return part.part


# Description: This is a curved shoulder harness or carrying strap with textured grip surfaces on both arms, designed to distribute weight evenly across the shoulders with a U-shaped profile and reinforced attachment points at each end.
def model_56489_241ed182_0012():
    """Model: Rotation_Rim"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 15 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 13.3724351372, perimeter: 89.7495655067
            with BuildLine():
                CenterArc((0, 0), 11.5, -79.2987345596, 79.2987345596)
                Line((-2.1354156504, -11.3), (2.1354156504, -11.3))
                CenterArc((0, 0), 11.5, 180, 79.2987345596)
                Line((-11.5, 0), (-11.5, 4))
                Line((-11.8, 4), (-11.5, 4))
                Line((-11.8, 0), (-11.8, 4))
                CenterArc((0, 0), 11.8, 180, 79.4360350953)
                Line((-2.1633307653, -11.6), (2.1633307653, -11.6))
                CenterArc((0, 0), 11.8, -79.4360350953, 79.4360350953)
                Line((11.8, 0), (11.8, 4))
                Line((11.8, 4), (11.5, 4))
                Line((11.5, 0), (11.5, 4))
            make_face()
        # Symmetric extrude, each_side=1
        extrude(amount=1, both=True)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -11.3, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.77437052, perimeter: 4.7592739892
            with BuildLine():
                Line((1.1180339887, 1), (-1.1180339887, 1))
                CenterArc((0, 0), 1.5, 41.8103148958, 96.3793702084)
            make_face()
            # Profile area: 0.77437052, perimeter: 4.7592739892
            with BuildLine():
                CenterArc((0, 0), 1.5, -138.1896851042, 96.3793702084)
                Line((-1.1180339887, -1), (1.1180339887, -1))
            make_face()
        # OneSide extrude, distance=-0.3
        extrude(amount=-0.3, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -11.3, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            Circle(0.4)
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on YZ construction plane
        # Sketch has 3 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            with Locations((0, 3)):
                Circle(0.3)
            # Profile area: 0.2146018366, perimeter: 3.5707963268
            with BuildLine():
                Line((0, 4), (-1, 4))
                Line((-1, 3), (-1, 4))
                CenterArc((0, 3), 1, 90, 90)
            make_face()
            # Profile area: 0.2146018366, perimeter: 3.5707963268
            with BuildLine():
                Line((1, 4), (0, 4))
                CenterArc((0, 3), 1, 0, 90)
                Line((1, 4), (1, 3))
            make_face()
        # Symmetric extrude, each_side=11.8
        extrude(amount=11.8, both=True, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a stepped bracket or angular support component with a complex geometric form featuring multiple recessed rectangular openings, angular projections, and interconnected flanges designed for mounting or structural support applications.
def model_56713_c077e606_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 3600, perimeter: 520
            with BuildLine():
                Line((-50, 60), (-50, 0))
                Line((50, 60), (-50, 60))
                Line((50, 0), (50, 60))
                Line((60, 0), (50, 0))
                Line((60, 80), (60, 0))
                Line((-60, 80), (60, 80))
                Line((-60, 0), (-60, 80))
                Line((-50, 0), (-60, 0))
            make_face()
        # Symmetric extrude, each_side=35
        extrude(amount=35, both=True)

        # Sketch4 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 35), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 640, perimeter: 176
            with BuildLine():
                Line((-35, 73), (-35, 65))
                Line((-35, 65), (45, 65))
                Line((45, 65), (45, 73))
                Line((45, 73), (-35, 73))
            make_face()
        # OneSide extrude, distance=-30
        extrude(amount=-30, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude3 (NewBody)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 35), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 553, perimeter: 172
            with BuildLine():
                Line((-34.5, 72.5), (44.5, 72.5))
                Line((-34.5, 65.5), (-34.5, 72.5))
                Line((44.5, 65.5), (-34.5, 65.5))
                Line((44.5, 72.5), (44.5, 65.5))
            make_face()
        # OneSide extrude, distance=30
        extrude(amount=30)
    return part.part


# Description: This is a plastic or composite bracket/mount component with a roughly L-shaped or angled profile, featuring a large vertical flange, a horizontal base, and what appears to be slots or mounting features on the left side for attachment or alignment purposes.
def model_56719_6e59eeff_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 23 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 4.6930103603, perimeter: 21.4857687485
            with BuildLine():
                CenterArc((-3.9558146445, 1.6430413573), 0.13, 39.6187008882, 90)
                Line((-4.1049143624, 1.6883776386), (-4.0387124524, 1.743181027))
                CenterArc((-4.0220165546, 1.5882379688), 0.13, 129.6187008882, 90)
                Line((-3.9385727827, 1.2835733172), (-4.1221562243, 1.505340161))
                Line((-4.4715352816, 1.0270847632), (-3.9385727827, 1.2835733172))
                Line((-5.5689338035, 3.3073902564), (-4.4715352816, 1.0270847632))
                CenterArc((-5.7501707944, 3.220169835), 0.201132416, 25.6992165921, 179.9999987926)
                Line((-4.667837804, 0.5073530494), (-5.9314077871, 3.1329494175))
                Line((-8.1545366023, 0.5073530494), (-4.667837804, 0.5073530494))
                CenterArc((-8.1545366023, 0.3773530494), 0.13, 90, 90)
                Line((-8.2845366023, 0.3773530494), (-8.2845366023, 0))
                Line((-8.2845366023, 0), (-2.4306126329, 0))
                Line((-2.4306126329, 0), (-2.44893528, 0.3501515646))
                CenterArc((-2.5787576621, 0.3433582502), 0.13, 2.9954277852, 87.0045722148)
                Line((-4.2050540321, 0.4733582502), (-2.5787576621, 0.4733582502))
                Line((-4.2050540321, 0.7598648753), (-4.2050540321, 0.4733582502))
                Line((-3.3833114384, 1.1553290402), (-4.2050540321, 0.7598648753))
                Line((-3.8556749748, 1.7259391652), (-3.3833114384, 1.1553290402))
            make_face()
        # OneSide extrude, distance=10.16
        extrude(amount=10.16)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.5073530494, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.7697930453, perimeter: 11.0420465173
            with BuildLine():
                CenterArc((-2.4011923715, 7.0866467174), 1.0389757725, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-2.4113687644, 7.0753370799), 0.7184205126, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=7.62
        extrude(amount=7.62, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.5073530494, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.7210134686, perimeter: 11.6922262581
            with BuildLine():
                CenterArc((-5.2285427554, 7.0570460898), 1.0776307689, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-5.2285427554, 7.0570460898), 0.7832448358, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=5.08
        extrude(amount=5.08, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 0.5073530494, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.6721347878, perimeter: 11.9738169036
            with BuildLine():
                CenterArc((-8.2808020466, 7.0553504422), 1.0924953438, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-8.2897856557, 7.0784040952), 0.8131968041, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=3.81
        extrude(amount=3.81, mode=Mode.ADD)
    return part.part


# Description: Four identical rectangular solar panels arranged in a 2x2 grid configuration, each featuring a textured photovoltaic surface with a slight trapezoidal shape and parallel grid lines representing solar cells.
def model_57098_95ef41bb_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 24000, perimeter: 1280.888691452
            with BuildLine():
                Line((600, 0), (600, 40))
                CenterArc((300, -4455), 4505, 86.181695134, 7.636609732)
                Line((0, 0), (0, 40))
                CenterArc((300, -4495), 4505, 86.181695134, 7.636609732)
            make_face()
        # OneSide extrude, distance=960
        extrude(amount=960)

        # Sketch3 -> Extrude2 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 23982.15091208, perimeter: 1280.892662328
            with BuildLine():
                Line((0, 1500), (0, 1460))
                CenterArc((300, 5955), 4505, -93.818304866, 7.636609732)
                Line((600, 1500), (600, 1460))
                CenterArc((300, 5975), 4485.0445928664, -93.8353190971, 7.6706381943)
            make_face()
        # OneSide extrude, distance=960
        extrude(amount=960)

        # Sketch5 -> Extrude3 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 24000, perimeter: 1280.888691452
            with BuildLine():
                Line((5600, 0), (5600, 40))
                CenterArc((5300, -4455), 4505, 86.181695134, 7.636609732)
                Line((5000, 0), (5000, 40))
                CenterArc((5300, -4495), 4505, 86.181695134, 7.636609732)
            make_face()

        # Sketch7 -> Extrude3 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 24000, perimeter: 1280.888691452
            with BuildLine():
                CenterArc((5300, 5995), 4505, -93.818304866, 7.636609732)
                Line((5000, 1500), (5000, 1460))
                CenterArc((5300, 5955), 4505, -93.818304866, 7.636609732)
                Line((5600, 1500), (5600, 1460))
            make_face()
        # OneSide extrude, distance=960
        extrude(amount=960)
    return part.part


# Description: This is a simple barbell/dumbbell consisting of a straight cylindrical bar (shown in blue) with two spherical or rounded square weights (shown in dark gray) attached at each end.
def model_57104_f2f9baa4_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.3544094003, perimeter: 14.193242244
            with BuildLine():
                Line((8.5500001274, -0.0500000007), (12.550000187, -0.0500000007))
                Line((12.550000187, -0.0500000007), (12.550000187, 0))
                CenterArc((13.0000001937, 0), 0.4500000067, 0, 180)
                Line((13.5000002012, 0), (13.4500002004, 0))
                CenterArc((13.0000001937, 0), 0.5000000075, 0, 180)
                Line((12.5000001863, 0), (8.6000001281, 0))
                CenterArc((8.05000012, -0.0500000007), 0.5522680591, 5.1944289077, 169.6111421845)
                Line((7.5500001125, 0), (7.5000001118, 0))
                CenterArc((8.05000012, -0.0527777786), 0.5027777853, 6.0255750084, 167.9488499833)
                CenterArc((8.3131580186, -0.0250000004), 0.2381578983, -6.0255750084, 12.0511500167)
            make_face()
        # OneSide extrude, distance=0.8
        extrude(amount=0.8)

        # Sketch4 -> Extrude2 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.3848451001, perimeter: 2.1991148575
            with Locations((8.05000012, -0.0741354967)):
                Circle(0.35)
            # Profile area: 0.3848536209, perimeter: 2.1991392027
            with Locations((12.9983544044, -0.0500000007)):
                Circle(0.3500038747)
        # OneSide extrude, distance=0.7
        extrude(amount=0.7)
    return part.part


# Description: This is a elongated parallelogram-shaped duct or channel with a tapered wedge profile, featuring a dark gray top surface, blue side surfaces, and a hollow interior cavity running along its length.
def model_57152_368e7c40_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 25 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 113.054296049, perimeter: 64.9745680348
            with BuildLine():
                Line((-1.8217080391, 1.2751516294), (-1.9880357561, 1.3916155506))
                CenterArc((-5.6302461269, -3.8099999306), 6.35, 55, 34.9999998095)
                Line((-5.6302461058, 2.5400000694), (-6.3851796361, 2.5400000719))
                CenterArc((-6.3851796615, -5.0799999281), 7.62, 89.9999998095, 39.8055730813)
                Line((-15.24, -2.54), (-11.2633849707, 0.7738460693))
                Line((-15.24, -2.54), (15.24, -2.54))
                Line((15.24, -2.54), (11.2620290082, 0.7743204792))
                CenterArc((6.3843930982, -5.0799999706), 7.62, 50.2, 39.7999998095)
                Line((6.3843931235, 2.5400000294), (5.6290403872, 2.540000032))
                CenterArc((5.6290403661, -3.809999968), 6.35, 89.9999998095, 35.0000001905)
                Line((1.8205023317, 1.2751516294), (1.9868299953, 1.3916155132))
                CenterArc((-0.0006028537, 3.87595937), 3.175, -125, 70)
            make_face()
        # OneSide extrude, distance=101.6
        extrude(amount=101.6)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 9.1088701487, perimeter: 23.302366516
            with BuildLine():
                CenterArc((0.0006028537, 3.87595937), 3.175, -125, 70)
                Line((1.9880357561, 1.3916155506), (1.8217080391, 1.2751516294))
                CenterArc((5.6302461269, -3.8099999306), 6.35, 90.0000001905, 34.9999998095)
                Line((5.6302461058, 2.54), (-5.6290403872, 2.54))
                CenterArc((-5.6290403661, -3.809999968), 6.35, 55, 35.0000001905)
                Line((-1.8205023317, 1.2751516294), (-1.9868299953, 1.3916155132))
            make_face()
        # OneSide extrude, distance=-21.59
        extrude(amount=-21.59, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(101.6, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 9.1088701487, perimeter: 23.302366516
            with BuildLine():
                CenterArc((-0.0006028537, 3.87595937), 3.175, -125, 70)
                Line((1.9868299953, 1.3916155132), (1.8205023317, 1.2751516294))
                CenterArc((5.6290403661, -3.809999968), 6.35, 89.9999998095, 35.0000001905)
                Line((5.6290403872, 2.54), (-5.6302461058, 2.54))
                CenterArc((-5.6302461269, -3.8099999306), 6.35, 55, 34.9999998095)
                Line((-1.8217080391, 1.2751516294), (-1.9880357561, 1.3916155506))
            make_face()
        # OneSide extrude, distance=-21.59
        extrude(amount=-21.59, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.2667686977, perimeter: 3.9898226701
            with Locations((57.1499991417, 0)):
                Circle(0.635)
            # Profile area: 1.2667686977, perimeter: 3.9898226701
            with Locations((44.4499993324, 0)):
                Circle(0.635)
            # Profile area: 1.2667686977, perimeter: 3.9898226701
            with Locations((76.1999988556, 0)):
                Circle(0.635)
            # Profile area: 1.2667686977, perimeter: 3.9898226701
            with Locations((68.57999897, 0)):
                Circle(0.635)
            # Profile area: 1.2667686977, perimeter: 3.9898226701
            with Locations((25.3999996185, 0)):
                Circle(0.635)
            # Profile area: 1.2667686977, perimeter: 3.9898226701
            with Locations((31.7499995232, 0)):
                Circle(0.635)
        # OneSide extrude, distance=10.16
        extrude(amount=10.16, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a rectangular storage container or bin with an open top, featuring internal shelving or dividers, angled side walls, and a dark blue/navy finish with a trapezoidal profile when viewed from above.
def model_57865_0744a6ab_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 16 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 10.5, perimeter: 43
            with BuildLine():
                Line((-3.5, 2), (4.5, 2))
                Line((4.5, 2), (4.5, -3.5))
                Line((4.5, -3.5), (4.5, -4))
                Line((5, -4), (4.5, -4))
                Line((5, 2.5), (5, -4))
                Line((-4, 2.5), (5, 2.5))
                Line((-4, -4), (-4, 2.5))
                Line((-3.5, -4), (-4, -4))
                Line((-3.5, -3.5), (-3.5, -4))
                Line((-3.5, -3.5), (-3.5, 2))
            make_face()
        # OneSide extrude, distance=4
        extrude(amount=4)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 16 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 12.5, perimeter: 50
            with BuildLine():
                Line((-3.5, -3.5), (-3.5, 2))
                Line((4.5, -3.5), (-3.5, -3.5))
                Line((4.5, 2), (4.5, -3.5))
                Line((-3.5, 2), (4.5, 2))
            make_face()
            with BuildLine():
                Line((-3, -3), (-3, 1.5))
                Line((-3, 1.5), (4, 1.5))
                Line((4, 1.5), (4, -3))
                Line((4, -3), (-3, -3))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)

        # Sketch1 -> Extrude3 (Join)
        # Sketch on XZ construction plane
        # Sketch has 16 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 31.5, perimeter: 23
            with BuildLine():
                Line((4, -3), (-3, -3))
                Line((4, 1.5), (4, -3))
                Line((-3, 1.5), (4, 1.5))
                Line((-3, -3), (-3, 1.5))
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2, mode=Mode.ADD)

        # Sketch4 -> Extrude6 (Cut)
        # Sketch on BRepFace
        # Sketch has 12 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -2), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.4492571252, perimeter: 5.319146185
            with BuildLine():
                Line((-0.5217034915, 3.318723416), (-3, 3.318723416))
                Line((-0.5217034915, 3.5), (-0.5217034915, 3.318723416))
                Line((-3, 3.5), (-0.5217034915, 3.5))
                Line((-3, 3.318723416), (-3, 3.5))
            make_face()
            # Profile area: 0.484727533, perimeter: 5.9015621151
            with BuildLine():
                Line((2.2544751366, 2.7599956418), (-0.5217034915, 2.7599956418))
                Line((2.2544751366, 2.9345980712), (2.2544751366, 2.7599956418))
                Line((-0.5217034915, 2.9345980712), (2.2544751366, 2.9345980712))
                Line((-0.5217034915, 2.7599956418), (-0.5217034915, 2.9345980712))
            make_face()
            # Profile area: 0.4426568415, perimeter: 4.6444246231
            with BuildLine():
                Line((2.0798727071, 3.5282463313), (2.0798727071, 3.318723416))
                Line((2.0798727071, 3.318723416), (4.1925621034, 3.318723416))
                Line((4.1925621034, 3.318723416), (4.1925621034, 3.5282463313))
                Line((4.1925621034, 3.5282463313), (2.0798727071, 3.5282463313))
            make_face()
        # OneSide extrude, distance=-0.1
        extrude(amount=-0.1, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude7 (Join)
        # Sketch on BRepFace
        # Sketch has 13 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 5.9265602884, perimeter: 9.7412482307
            with BuildLine():
                Line((-0.6293758847, -0.5), (-3, -0.5))
                Line((-0.6293758847, -0.5), (-0.6293758847, 2))
                Line((-3, 2), (-0.6293758847, 2))
                Line((-3, -0.5), (-3, 2))
            make_face()
            # Profile area: 5.8975620817, perimeter: 9.7180496654
            with BuildLine():
                Line((-0.3590248327, 2), (-0.3590248327, -0.5))
                Line((2, -0.5), (-0.3590248327, -0.5))
                Line((2, 2), (2, -0.5))
                Line((-0.3590248327, 2), (2, 2))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)
    return part.part


# Description: This is a flat rectangular mounting plate with a parallelogram shape, featuring four circular mounting holes (one in each corner) and a recessed central panel.
def model_60701_72ac971f_0003():
    """Model: Untitled v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 7 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 18, perimeter: 18
            with BuildLine():
                Line((-3, 1.5), (3, 1.5))
                Line((-3, -1.5), (-3, 1.5))
                Line((3, -1.5), (-3, -1.5))
                Line((3, 1.5), (3, -1.5))
            make_face()
        # OneSide extrude, distance=0.25
        extrude(amount=0.25)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.25), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            with Locations((-2.5000000373, 1.0000000149)):
                Circle(0.3)
        # OneSide extrude, distance=-0.9
        extrude(amount=-0.9, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.25), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            with Locations((2.5000000373, 1.0000000149)):
                Circle(0.3)
        # OneSide extrude, distance=-0.6
        extrude(amount=-0.6, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.25), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            with Locations((-2.5000000373, -1.0000000149)):
                Circle(0.3)
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.25), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            with Locations((2.5000000373, -1.0000000149)):
                Circle(0.3)
        # OneSide extrude, distance=-1.1
        extrude(amount=-1.1, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical sleeve or tube with a dark blue finish, featuring a tapered/angled top end, reinforcing ribs or structural lines along its body, and a flanged base at the bottom.
def model_60716_dcd9370c_0002():
    """Model: base v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 180, perimeter: 72
            with BuildLine():
                Line((0, 30), (0, 0))
                Line((0, 0), (6, 0))
                Line((6, 0), (6, 30))
                Line((6, 30), (0, 30))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(1, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            with Locations((4.5, 7.5)):
                Circle(0.3)
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            with Locations((1.5, 7.5)):
                Circle(0.3)
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            with Locations((1.5, 2.5)):
                Circle(0.3)
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            with Locations((4.5, 2.5)):
                Circle(0.3)
        # OneSide extrude, distance=-3
        extrude(amount=-3, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 10 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 30, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.5, perimeter: 7
            with BuildLine():
                Line((0, 0), (-1, 0))
                Line((0, 2.5), (0, 0))
                Line((-1, 2.5), (0, 2.5))
                Line((-1, 0), (-1, 2.5))
            make_face()
            # Profile area: 2.5, perimeter: 7
            with BuildLine():
                Line((-1, -8.5), (0, -8.5))
                Line((0, -8.5), (0, -6))
                Line((0, -6), (-1, -6))
                Line((-1, -6), (-1, -8.5))
            make_face()
        # OneSide extrude, distance=-30
        extrude(amount=-30, mode=Mode.ADD)

        # Sketch6 -> Extrude7 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 2.5), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 5, perimeter: 14.2495086728
            with BuildLine():
                CenterArc((-4.6666666667, 0), 5.6666666667, -61.9275130641, 61.9275130641)
                Line((0, 0), (1, 0))
                CenterArc((-5.6666666667, 0), 5.6666666667, -61.9275130641, 61.9275130641)
                Line((-2, -5), (-3, -5))
            make_face()
            # Profile area: 5, perimeter: 14.2495086728
            with BuildLine():
                Line((1, 30), (0, 30))
                CenterArc((-4.6666666667, 30), 5.6666666667, 0, 61.9275130641)
                Line((-2, 35), (-3, 35))
                CenterArc((-5.6666666667, 30), 5.6666666667, 0, 61.9275130641)
            make_face()
        # OneSide extrude, distance=-11
        extrude(amount=-11, mode=Mode.ADD)
    return part.part


# Description: This is a stamped or formed metal bracket with an angular L-shaped profile, featuring two perpendicular arms with beveled edges and a reinforcing rib or flange running along the inner corner for structural rigidity.
def model_60753_80b955c8_0004():
    """Model: ch1 v2 v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 7 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 26.7716842186, perimeter: 56.73888611
            with BuildLine():
                Line((0, 7), (0, 9))
                Line((0, 9), (-1, 9))
                Line((-1, 9), (-1, 7))
                Line((-1, 7), (-5.0682913245, -3.7840673913))
                Line((-5.0682913245, -3.7840673913), (10, -3.7840673913))
                Line((10, -3.7840673913), (10, -2.7761817733))
                Line((-3.6880662974, -2.7761817733), (10, -2.7761817733))
                Line((0, 7), (-3.6880662974, -2.7761817733))
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2)

        # Sketch13 -> Extrude5 (Cut)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 13.9583269682, perimeter: 15.4077653401
            with BuildLine():
                Line((-5.2366998875, -6.3484183479), (-7.5, -2))
                Line((-2.5928838639, -4.6786398066), (-5.2366998875, -6.3484183479))
                Line((-5.0759173248, -0.7471701603), (-2.5928838639, -4.6786398066))
                Line((-7.5, -2), (-5.0759173248, -0.7471701603))
            make_face()
        # OneSide extrude, distance=4.5
        extrude(amount=4.5, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a blue anodized aluminum bracket or support arm featuring two perpendicular platforms connected by angular ribs, designed to mount or support components at right angles with reinforced structural webbing.
def model_60865_19bbdeb4_0029():
    """Model: Leg v1 (3)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 4 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.4034314575, perimeter: 14.5171572875
            with BuildLine():
                Line((-1.1549605046, 0.0139966921), (-1.1549605046, -0.1860033079))
                Line((-1.1549605046, -0.1860033079), (1.7621967829, -0.1860033079))
                Line((1.7621967829, -0.1860033079), (4.5320452639, -2.9558517888))
                Line((4.5320452639, -2.9558517888), (4.8148879763, -2.9558517888))
                Line((4.8148879763, -2.9558517888), (1.8450394954, 0.0139966921))
                Line((-1.1549605046, 0.0139966921), (1.8450394954, 0.0139966921))
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2)

        # Sketch2 -> Extrude2 (NewBody)
        # Sketch on BRepFace
        # Sketch has 6 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -2.9558517888, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 6.1943145983, perimeter: 14.9656854428
            with BuildLine():
                Line((3.3734666201, 2.3000000045), (5.9734666201, 2.3000000045))
                Line((3.3734666201, -0.3000000045), (3.3734666201, 2.3000000045))
                Line((5.9734666201, -0.3000000045), (3.3734666201, -0.3000000045))
                Line((5.9734666201, 2.3000000045), (5.9734666201, -0.3000000045))
            make_face()
            with BuildLine():
                Line((4.8148879763, 2), (4.5320452639, 2))
                Line((4.8148879763, 0), (4.8148879763, 2))
                Line((4.5320452639, 0), (4.8148879763, 0))
                Line((4.5320452639, 2), (4.5320452639, 0))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -3.4558517888, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 1.6999989307, perimeter: 5.6999989307
            with BuildLine():
                Line((4.8148879763, 2), (4.8148879763, 0))
                Line((5.6648874417, 0), (4.8148879763, 0))
                Line((5.6648874417, 2), (5.6648874417, 0))
                Line((4.8148879763, 2), (5.6648874417, 2))
            make_face()
            # Profile area: 1.7343156444, perimeter: 5.7343156444
            with BuildLine():
                Line((3.6648874417, 2), (4.5320452639, 2))
                Line((3.6648874417, 0), (3.6648874417, 2))
                Line((4.5320452639, 0), (3.6648874417, 0))
                Line((4.5320452639, 0), (4.5320452639, 2))
            make_face()
        # OneSide extrude, distance=-0.3
        extrude(amount=-0.3, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.0139966921, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((-0.3450394954, 1)):
                Circle(0.5)
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a complex stamped or cast metal bracket with an irregular, angular geometry featuring multiple internal and external cutouts, slots, and flanges designed to mount or connect components at various angles.
def model_60870_1b9e95c9_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 60, perimeter: 32
            with BuildLine():
                Line((10, -6), (0, -6))
                Line((10, 0), (10, -6))
                Line((0, 0), (10, 0))
                Line((0, -6), (0, 0))
            make_face()
        # OneSide extrude, distance=8
        extrude(amount=8)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(10, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 4, perimeter: 10
            with BuildLine():
                Line((-5, 1), (-1, 1))
                Line((-5, 0), (-5, 1))
                Line((-1, 0), (-5, 0))
                Line((-1, 1), (-1, 0))
            make_face()
        # OneSide extrude, distance=-13.5
        extrude(amount=-13.5, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 8, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 10, perimeter: 14
            with BuildLine():
                Line((-2.5, 1.5), (-7.5, 1.5))
                Line((-2.5, 3.5), (-2.5, 1.5))
                Line((-7.5, 3.5), (-2.5, 3.5))
                Line((-7.5, 1.5), (-7.5, 3.5))
            make_face()
        # OneSide extrude, distance=-3.5
        extrude(amount=-3.5, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(10, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 12.5, perimeter: 15
            with BuildLine():
                Line((-6, 3), (-3.5, 3))
                Line((-3.5, 3), (-3.5, 8))
                Line((-3.5, 8), (-6, 8))
                Line((-6, 8), (-6, 3))
            make_face()
        # OneSide extrude, distance=-15.5
        extrude(amount=-15.5, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 3, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 7.5, perimeter: 11
            with BuildLine():
                Line((-6.5, 3.5), (-6.5, 6))
                Line((-3.5, 3.5), (-6.5, 3.5))
                Line((-3.5, 6), (-3.5, 3.5))
                Line((-6.5, 6), (-3.5, 6))
            make_face()
        # OneSide extrude, distance=-4
        extrude(amount=-4, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a hexagonal metal enclosure or junction box with an irregular, angular geometry featuring multiple faceted surfaces, internal structural supports or framework visible through cutouts, and a compact, three-dimensional prismatic shape designed for housing or mounting purposes.
def model_60972_b4c697a4_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 31 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 15.5475685434, perimeter: 28.4024648269
            with BuildLine():
                Line((-3.8171547924, 0.8711774884), (3.7064232499, 0.8711774884))
                Line((3.7064232499, 0.8711774884), (3.7064232499, -0.9994178343))
                Line((3.7064232499, -0.9994178343), (4.3744603504, -1))
                Line((4.3744603504, 2.269599965), (4.3744603504, -1))
                Line((-4.6865765511, 2.269599965), (4.3744603504, 2.269599965))
                Line((-4.6865765511, -1), (-4.6865765511, 2.269599965))
                Line((-4.6865765511, -1), (-3.8171547924, -0.9994178343))
                Line((-3.8171547924, -0.9994178343), (-3.8171547924, 0.8711774884))
            make_face()
        # OneSide extrude, distance=3
        extrude(amount=3)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 31 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.0850835103, perimeter: 38.7592939667
            with BuildLine():
                Line((-3.8171547924, -0.9994178343), (-3.8171547924, 0.8711774884))
                Line((3.7064232499, -0.9994178343), (-3.8171547924, -0.9994178343))
                Line((3.7064232499, 0.8711774884), (3.7064232499, -0.9994178343))
                Line((-3.8171547924, 0.8711774884), (3.7064232499, 0.8711774884))
            make_face()
            with BuildLine():
                Line((0.1650218684, -0.9335381201), (0.1650218684, 0.7039868652))
                Line((0.1650218684, 0.7039868652), (3.4024402987, 0.7039868652))
                Line((3.4024402987, 0.7039868652), (3.4024402987, -0.9335381201))
                Line((3.4024402987, -0.9335381201), (0.1650218684, -0.9335381201))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((-3.5283709887, -0.9335381201), (-3.5283709887, 0.7039868652))
                Line((-3.5283709887, 0.7039868652), (-0.0553657712, 0.7039868652))
                Line((-0.0553657712, 0.7039868652), (-0.0553657712, -0.9335381201))
                Line((-0.0553657712, -0.9335381201), (-3.5283709887, -0.9335381201))
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 5.3013535675, perimeter: 9.7498868312
            with BuildLine():
                Line((3.4024402987, -0.9335381201), (0.1650218684, -0.9335381201))
                Line((3.4024402987, 0.7039868652), (3.4024402987, -0.9335381201))
                Line((0.1650218684, 0.7039868652), (3.4024402987, 0.7039868652))
                Line((0.1650218684, -0.9335381201), (0.1650218684, 0.7039868652))
            make_face()
            # Profile area: 5.6871328177, perimeter: 10.2210604056
            with BuildLine():
                Line((-0.0553657712, -0.9335381201), (-3.5283709887, -0.9335381201))
                Line((-0.0553657712, 0.7039868652), (-0.0553657712, -0.9335381201))
                Line((-3.5283709887, 0.7039868652), (-0.0553657712, 0.7039868652))
                Line((-3.5283709887, -0.9335381201), (-3.5283709887, 0.7039868652))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)

        # Sketch1 -> Extrude3 (Join)
        # Sketch on XZ construction plane
        # Sketch has 31 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 5.6871328177, perimeter: 10.2210604056
            with BuildLine():
                Line((-0.0553657712, -0.9335381201), (-3.5283709887, -0.9335381201))
                Line((-0.0553657712, 0.7039868652), (-0.0553657712, -0.9335381201))
                Line((-3.5283709887, 0.7039868652), (-0.0553657712, 0.7039868652))
                Line((-3.5283709887, -0.9335381201), (-3.5283709887, 0.7039868652))
            make_face()
            # Profile area: 5.3013535675, perimeter: 9.7498868312
            with BuildLine():
                Line((3.4024402987, -0.9335381201), (0.1650218684, -0.9335381201))
                Line((3.4024402987, 0.7039868652), (3.4024402987, -0.9335381201))
                Line((0.1650218684, 0.7039868652), (3.4024402987, 0.7039868652))
                Line((0.1650218684, -0.9335381201), (0.1650218684, 0.7039868652))
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2, mode=Mode.ADD)

        # Sketch1 -> Extrude4 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 31 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 12.1384912454, perimeter: 22.3701947787
            with BuildLine():
                Line((-0.3432882756, -7.7520102701), (-0.3432882756, -7.1843707185))
                Line((-0.3432882756, -7.1843707185), (-0.579736362, -7.1843707185))
                Line((-0.579736362, -7.1843707185), (-2.6164221351, -7.1843707185))
                Line((-2.6164221351, -7.1843707185), (-2.6164221351, -3.7949608126))
                Line((-0.579736362, -3.7949608126), (-2.6164221351, -3.7949608126))
                Line((-0.3432882756, -3.7949608126), (-0.579736362, -3.7949608126))
                Line((-0.3432882756, -3.1833350158), (-0.3432882756, -3.7949608126))
                Line((-4.6865765511, -3.1833350158), (-0.3432882756, -3.1833350158))
                Line((-4.6865765511, -7.7520102701), (-4.6865765511, -3.1833350158))
                Line((-0.3432882756, -7.7520102701), (-4.6865765511, -7.7520102701))
            make_face()
        # OneSide extrude, distance=3
        extrude(amount=3)

        # Sketch1 -> Extrude5 (Join)
        # Sketch on XZ construction plane
        # Sketch has 31 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.567967363, perimeter: 20.4230958734
            with BuildLine():
                Line((-0.579736362, -3.7949608126), (-2.6164221351, -3.7949608126))
                Line((-2.6164221351, -7.1843707185), (-2.6164221351, -3.7949608126))
                Line((-0.579736362, -7.1843707185), (-2.6164221351, -7.1843707185))
                Line((-0.579736362, -3.7949608126), (-0.579736362, -7.1843707185))
            make_face()
            with BuildLine():
                Line((-2.5, -7.0171800954), (-2.5, -4))
                Line((-2.5, -4), (-0.7317278376, -4))
                Line((-0.7317278376, -4), (-0.7317278376, -7.0171800954))
                Line((-0.7317278376, -7.0171800954), (-2.5, -7.0171800954))
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 5.3351955714, perimeter: 9.5709045154
            with BuildLine():
                Line((-0.7317278376, -7.0171800954), (-2.5, -7.0171800954))
                Line((-0.7317278376, -4), (-0.7317278376, -7.0171800954))
                Line((-2.5, -4), (-0.7317278376, -4))
                Line((-2.5, -7.0171800954), (-2.5, -4))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)

        # Sketch1 -> Extrude6 (Join)
        # Sketch on XZ construction plane
        # Sketch has 31 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 5.3351955714, perimeter: 9.5709045154
            with BuildLine():
                Line((-0.7317278376, -7.0171800954), (-2.5, -7.0171800954))
                Line((-0.7317278376, -4), (-0.7317278376, -7.0171800954))
                Line((-2.5, -4), (-0.7317278376, -4))
                Line((-2.5, -7.0171800954), (-2.5, -4))
            make_face()
        # OneSide extrude, distance=1.9
        extrude(amount=1.9, mode=Mode.ADD)

        # Sketch1 -> Extrude7 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 31 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 6.2831853072, perimeter: 8.8857658763
            with Locations((2.2604760023, -3.1431393069)):
                Circle(1.4142135624)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch1 -> Extrude8 (Join)
        # Sketch on XZ construction plane
        # Sketch has 31 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((2.1612577625, -4.0884818835)):
                Circle(0.2)
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((1.5522917872, -2.7232414057)):
                Circle(0.2)
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((3.0953696683, -2.7232414057)):
                Circle(0.2)
        # OneSide extrude, distance=1.4
        extrude(amount=1.4, mode=Mode.ADD)
    return part.part


# Description: This is a complex multi-directional connector or bracket assembly featuring an irregular polyhedron shape with multiple protruding rectangular flanges, triangular faces, and integrated mounting holes, designed for 3D spatial assembly with intersecting geometric planes.
def model_61082_9b58978f_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 68, perimeter: 40
            with BuildLine():
                Line((4, 5), (-4, 5))
                Line((-4, 5), (-4, -5))
                Line((-4, -5), (-3, -5))
                Line((-3, -5), (-3, -3))
                Line((-3, -3), (3, -3))
                Line((3, -3), (3, -5))
                Line((3, -5), (4, -5))
                Line((4, -5), (4, 5))
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 16, perimeter: 16
            with BuildLine():
                Line((2, -4), (-2, -4))
                Line((2, 0), (2, -4))
                Line((-2, 0), (2, 0))
                Line((-2, -4), (-2, 0))
            make_face()
        # OneSide extrude, distance=3
        extrude(amount=3, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 15, perimeter: 16.3245553203
            with BuildLine():
                Line((2, 0), (3, 3))
                Line((3, 3), (-3, 3))
                Line((-2, 0), (-3, 3))
                Line((2, 0), (-2, 0))
            make_face()
        # OneSide extrude, distance=-2.9
        extrude(amount=-2.9, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 0, 3), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 2.7024185502, perimeter: 5.827485998
            with Locations((-0.0741297747, 3.55)):
                Circle(0.9274732024)
        # OneSide extrude, distance=-7
        extrude(amount=-7, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 8, perimeter: 12.94427191
            with BuildLine():
                Line((2, -4), (0, 0))
                Line((0, 0), (-2, -4))
                Line((-2, -4), (2, -4))
            make_face()
        # OneSide extrude, distance=-3
        extrude(amount=-3, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical socket head cap screw or hex socket screw featuring a long, uniform shaft with a recessed hexagonal socket at the top and a rounded end at the bottom.
def model_61270_6fc99e6c_0003():
    """Model: Screw Rod v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.7671458676, perimeter: 4.7123889804
            Circle(0.75)
        # OneSide extrude, distance=7.5
        extrude(amount=7.5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 7.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.7567475535, perimeter: 12.252211349
            with BuildLine():
                CenterArc((0, 0), 1.2, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.75, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 1.7671458676, perimeter: 4.7123889804
            Circle(0.75)
        # OneSide extrude, distance=2.2
        extrude(amount=2.2, mode=Mode.ADD)

        # Sketch5 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 1.1309733553, perimeter: 3.7699111843
            Circle(0.6)
        # OneSide extrude, distance=0.15
        extrude(amount=0.15, mode=Mode.ADD)

        # Sketch6 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -0.15, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            Circle(0.4)
        # OneSide extrude, distance=0.35
        extrude(amount=0.35, mode=Mode.ADD)
    return part.part


# Description: This is a hollow cubic or box-shaped housing with an open interior featuring internal walls, triangular cutouts or slots on multiple sides, and a complex internal structure with various geometric divisions and openings.
def model_61273_bf8abea3_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 42.5, perimeter: 27
            with BuildLine():
                Line((8.5, -5), (0, -5))
                Line((8.5, 0), (8.5, -5))
                Line((0, 0), (8.5, 0))
                Line((0, -5), (0, 0))
            make_face()
        # OneSide extrude, distance=8
        extrude(amount=8)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 8, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 26.0191430479, perimeter: 21.0095715239
            with BuildLine():
                Line((-7.504785762, 5), (-1, 5))
                Line((-7.504785762, 1), (-7.504785762, 5))
                Line((-1, 1), (-7.504785762, 1))
                Line((-1, 5), (-1, 1))
            make_face()
        # OneSide extrude, distance=-7
        extrude(amount=-7, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 20.3146609344, perimeter: 18.6705126135
            with BuildLine():
                Line((-7.1753275071, 4.7344653148), (-1.2944015157, 4.7344653148))
                Line((-7.1753275071, 1.2801349995), (-7.1753275071, 4.7344653148))
                Line((-1.2944015157, 1.2801349995), (-7.1753275071, 1.2801349995))
                Line((-1.2944015157, 4.7344653148), (-1.2944015157, 1.2801349995))
            make_face()
        # OneSide extrude, distance=3
        extrude(amount=3, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 9.2239819286, perimeter: 13.1610915151
            with BuildLine():
                Line((6.5559401685, 4.9753944109), (2, 4.9753944109))
                Line((6.5559401685, 7), (6.5559401685, 4.9753944109))
                Line((2, 7), (6.5559401685, 7))
                Line((2, 4.9753944109), (2, 7))
            make_face()
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a booster seat or child car seat with a contoured backrest, a reclined seating surface with blue padding, and rounded armrest/side supports, designed for automotive use.
def model_61899_93eee6e5_0000():
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
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 16.5371462776, perimeter: 39.0852240314
            with BuildLine():
                CenterArc((-6.8182424448, 3.2346506215), 2.441312701, 18.2702306741, 59.5485735748)
                CenterArc((-6.4936807548, 5.1622952688), 0.4967121049, 67.4398616576, 129.8473570798)
                CenterArc((-6.6355353184, 5.1070724838), 0.3450175008, -164.4691149434, 148.9382298868)
                CenterArc((-6.9679549398, 3.6387871352), 1.5281111433, 11.4847391572, 52.7253491206)
                CenterArc((-1.2564539404, 5.2256891049), 4.4048672186, -163.0709069376, 56.672677308)
                Line((9.9565070978, 1), (-2.5, 1))
                Line((9.9565070978, 1.8965447547), (9.9565070978, 1))
                Line((-2.3188172515, 1.8965447547), (9.9565070978, 1.8965447547))
                CenterArc((-1.2191660399, 5.219449458), 3.5001326338, -159.6104601165, 51.2994946414)
            make_face()
        # OneSide extrude, distance=-7
        extrude(amount=-7)

        # Sketch2 -> Extrude2 (NewBody)
        # Sketch on BRepFace
        # Sketch has 7 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 17.2266740321, perimeter: 40.0991357383
            with BuildLine():
                CenterArc((-1.2191660399, 5.219449458), 3.5001326338, -159.6104601165, 51.2994946414)
                Line((9.9565070978, 1.8965447547), (-2.3188172515, 1.8965447547))
                Line((9.9565070978, 2.7965447547), (9.9565070978, 1.8965447547))
                Line((9.9565070978, 2.7965447547), (-2.162682077, 2.7965447547))
                CenterArc((-1.2191660399, 5.219449458), 2.6001326338, -159.2992416943, 48.0225444607)
                CenterArc((-6.8182424448, 3.2346506215), 3.341312701, 18.5989574606, 58.0699231487)
                CenterArc((-6.4936807548, 5.1622952688), 1.3967121049, 71.3836345335, 76.0446561349)
                Line((-6.9586685572, 5.3369642666), (-7.6707156343, 5.9142218587))
                CenterArc((-6.4936807548, 5.1622952688), 0.4967121049, 67.4398616576, 91.971845673)
                CenterArc((-6.8182424448, 3.2346506215), 2.441312701, 18.2702306741, 59.5485735748)
            make_face()
        # OneSide extrude, distance=-6.85
        extrude(amount=-6.85)

        # Sketch6 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -7), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 39.7749850644, perimeter: 40.2469223131
            with BuildLine():
                Line((-9.9565070978, 1.8965447547), (-9.9565070978, 2.2892533156))
                Line((2.3188172515, 1.8965447547), (-9.9565070978, 1.8965447547))
                CenterArc((1.2191660399, 5.219449458), 3.5001326338, -71.6890345248, 51.2994946414)
                CenterArc((6.8182424448, 3.2346506215), 2.441312701, 102.1811957511, 59.5485735748)
                CenterArc((6.4936807548, 5.1622952688), 0.4967121049, -17.2872187374, 129.8473570798)
                _nurbs_edge([(-9.9565070978, 2.2892533156), (-9.857592349, 2.3823659749), (-9.6560558661, 2.5608216392), (-9.342630184, 2.8051961712), (-8.9024647258, 3.0843635072), (-8.315412614, 3.3559278044), (-7.6925318031, 3.5517202846), (-7.0360314788, 3.6753546686), (-6.3497598501, 3.7331983175), (-5.639650852, 3.7351358768), (-4.9141936584, 3.6953733827), (-4.1848702192, 3.6331858271), (-3.4648989299, 3.5706529277), (-2.7680259607, 3.5304811977), (-2.1072958834, 3.5337851962), (-1.4938420783, 3.5979128615), (-0.9356277071, 3.7341617982), (-0.4362680042, 3.9456894478), (0.0064039464, 4.2248398165), (0.3993298427, 4.5560259632), (0.7529154872, 4.9192476927), (1.0798388085, 5.2934986774), (1.3938397848, 5.6598929492), (1.7084833326, 6.0056863921), (2.036098269, 6.3251197839), (2.3869905265, 6.6161450421), (2.7685377266, 6.8780764396), (3.1844092171, 7.1091426877), (3.6334963758, 7.3034376764), (4.1097666983, 7.4505229894), (4.6032523271, 7.5383594277), (5.1007089047, 7.5554092985), (5.5864399511, 7.4930051571), (6.0429248055, 7.3477957954), (6.4518695567, 7.1236155217), (6.7963135448, 6.831113348), (7.0627297859, 6.4879971737), (7.2427907818, 6.1186697647), (7.3361668121, 5.7551357572), (7.3492479933, 5.4332687739), (7.2907249796, 5.1856585363), (7.192507018, 5.0652096352), (7.0910308008, 5.0217339973), (7.0110375389, 5.0135695361), (6.9679549398, 5.0146913643)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.025, 0.05, 0.075, 0.1, 0.125, 0.15, 0.175, 0.2, 0.225, 0.25, 0.275, 0.3, 0.325, 0.35, 0.375, 0.4, 0.425, 0.45, 0.475, 0.5, 0.525, 0.55, 0.575, 0.6, 0.625, 0.65, 0.675, 0.7, 0.725, 0.75, 0.775, 0.8, 0.825, 0.85, 0.875, 0.9, 0.925, 0.95, 0.975, 1, 1, 1, 1, 1, 1], 5)
            make_face()
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.ADD)

        # Sketch7 -> Extrude6 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(9.9565070978, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 9.1696099816, perimeter: 14.500109739
            with BuildLine():
                Line((6.5, 2.7965447547), (0, 2.7965447547))
                CenterArc((3.25, 1.1131853243), 3.6600818258, 27.3822027074, 125.2355945852)
            make_face()
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2, mode=Mode.ADD)
    return part.part


MODELS = {
    "model_52230_60438ea5_0003": {"func": model_52230_60438ea5_0003, "volume": 80.8206180585, "area": 109.1327299632},
    "model_52557_e6a00b06_0001": {"func": model_52557_e6a00b06_0001, "volume": 25.2981058252, "area": 124.4311485751},
    "model_52557_e6a00b06_0002": {"func": model_52557_e6a00b06_0002, "volume": 499.7673646655, "area": 5070.2036327768},
    "model_52985_475fe7b2_0012": {"func": model_52985_475fe7b2_0012, "volume": 2916.1283882395, "area": 1838.2361519692},
    "model_52987_387431ac_0003": {"func": model_52987_387431ac_0003, "volume": 216.2114750035, "area": 322.1860345889},
    "model_53075_6438cc56_0003": {"func": model_53075_6438cc56_0003, "volume": 144.067716875, "area": 1444.2644251095},
    "model_53075_6438cc56_0005": {"func": model_53075_6438cc56_0005, "volume": 138.5364602741, "area": 1400.2258100896},
    "model_53075_6438cc56_0011": {"func": model_53075_6438cc56_0011, "volume": 209.4630480142, "area": 1540.3957489045},
    "model_53078_b592f2bd_0003": {"func": model_53078_b592f2bd_0003, "volume": 318.8422232401, "area": 1229.666522025},
    "model_53448_2f7c767c_0016": {"func": model_53448_2f7c767c_0016, "volume": 49.836665246, "area": 1029.1267616876},
    "model_53456_0e487078_0000": {"func": model_53456_0e487078_0000, "volume": 1.5968693121, "area": 18.6758447413},
    "model_53471_1b48c608_0001": {"func": model_53471_1b48c608_0001, "volume": 6294.6455511285, "area": 3157.4776453552},
    "model_53846_89405f98_0010": {"func": model_53846_89405f98_0010, "volume": 0.4603328039, "area": 4.8260854002},
    "model_53927_ef5208b9_0004": {"func": model_53927_ef5208b9_0004, "volume": 4.9967125154, "area": 22.3466968437},
    "model_53927_ef5208b9_0009": {"func": model_53927_ef5208b9_0009, "volume": 12.0524223473, "area": 45.7481562198},
    "model_53927_ef5208b9_0011": {"func": model_53927_ef5208b9_0011, "volume": 10.7459294317, "area": 38.3948877932},
    "model_54187_3f75c385_0000": {"func": model_54187_3f75c385_0000, "volume": 43.5628372406, "area": 169.7662664574},
    "model_54285_76f37095_0003": {"func": model_54285_76f37095_0003, "volume": 0.5459492002, "area": 7.4132822323},
    "model_54383_13d47b0e_0001": {"func": model_54383_13d47b0e_0001, "volume": 170.2261844443, "area": 1166.9978964099},
    "model_54383_13d47b0e_0004": {"func": model_54383_13d47b0e_0004, "volume": 196.3937776486, "area": 255.7001183536},
    "model_54383_13d47b0e_0008": {"func": model_54383_13d47b0e_0008, "volume": 766.6400806552, "area": 725.5805519871},
    "model_54509_e0930519_0000": {"func": model_54509_e0930519_0000, "volume": 67.6307352129, "area": 336.074609872},
    "model_54597_893331b6_0000": {"func": model_54597_893331b6_0000, "volume": 156.3367544354, "area": 437.8316194231},
    "model_54637_d8b47586_0000": {"func": model_54637_d8b47586_0000, "volume": 13701.9725646915, "area": 10556.3441965603},
    "model_54659_e1303e28_0003": {"func": model_54659_e1303e28_0003, "volume": 68.0835280601, "area": 171.5922039275},
    "model_54747_8e62bef9_0011": {"func": model_54747_8e62bef9_0011, "volume": 0.8042477193, "area": 8.0424771932},
    "model_54753_f93827fa_0000": {"func": model_54753_f93827fa_0000, "volume": 32.9507054342, "area": 104.1409652941},
    "model_54765_38755dca_0000": {"func": model_54765_38755dca_0000, "volume": 11.6311205427, "area": 51.3418026108},
    "model_54812_5f7b7aba_0000": {"func": model_54812_5f7b7aba_0000, "volume": 193.4840162474, "area": 391.0072913838},
    "model_54965_75ba8fee_0000": {"func": model_54965_75ba8fee_0000, "volume": 663552523.3570554256, "area": 6245922.746165175},
    "model_55026_4a1cbcd7_0000": {"func": model_55026_4a1cbcd7_0000, "volume": 195.1714436043, "area": 376.9911184308},
    "model_55028_329486a0_0000": {"func": model_55028_329486a0_0000, "volume": 191.9316761803, "area": 384.4508788707},
    "model_55113_1c22a134_0000": {"func": model_55113_1c22a134_0000, "volume": 69.2062446337, "area": 485.0653675392},
    "model_55228_41934c1f_0000": {"func": model_55228_41934c1f_0000, "volume": 43.3354031199, "area": 210.4409757639},
    "model_55233_19fac79a_0000": {"func": model_55233_19fac79a_0000, "volume": 347.3139889839, "area": 322.9808539379},
    "model_55236_e0bbfb4e_0000": {"func": model_55236_e0bbfb4e_0000, "volume": 34.3098499106, "area": 118.0271713655},
    "model_55323_716f61f1_0000": {"func": model_55323_716f61f1_0000, "volume": 1.3345503502, "area": 12.1919971411},
    "model_55336_6181655b_0000": {"func": model_55336_6181655b_0000, "volume": 1.2763854798, "area": 13.7012330748},
    "model_55348_bf8fb35c_0000": {"func": model_55348_bf8fb35c_0000, "volume": 7191.8425037873, "area": 2574.6526818873},
    "model_55476_1473d91f_0000": {"func": model_55476_1473d91f_0000, "volume": 210, "area": 256},
    "model_55481_a0e762b2_0000": {"func": model_55481_a0e762b2_0000, "volume": 2323.9721427247, "area": 1373.1086015224},
    "model_55521_d587e636_0000": {"func": model_55521_d587e636_0000, "volume": 214.3008881569, "area": 374.8318530718},
    "model_55546_670606b4_0000": {"func": model_55546_670606b4_0000, "volume": 15.2726612181, "area": 61.2978645503},
    "model_55594_791079ce_0000": {"func": model_55594_791079ce_0000, "volume": 1.6964600329, "area": 7.916813487},
    "model_55611_69142616_0000": {"func": model_55611_69142616_0000, "volume": 11.5953920759, "area": 48.7444741183},
    "model_55611_69142616_0009": {"func": model_55611_69142616_0009, "volume": 1189.1563168248, "area": 1934.4939980861},
    "model_55634_3b61fa4d_0000": {"func": model_55634_3b61fa4d_0000, "volume": 7.5744052489, "area": 27.698722594},
    "model_55636_6180bfce_0006": {"func": model_55636_6180bfce_0006, "volume": 1636.8225328566, "area": 1929.481974832},
    "model_55742_8008d3fe_0000": {"func": model_55742_8008d3fe_0000, "volume": 118.4394365375, "area": 544.9691272905},
    "model_56065_00bbe5da_0014": {"func": model_56065_00bbe5da_0014, "volume": 12.9174435934, "area": 58.9991100344},
    "model_56356_95c9f867_0001": {"func": model_56356_95c9f867_0001, "volume": 261478.9255629177, "area": 51743.5935304037},
    "model_56489_241ed182_0012": {"func": model_56489_241ed182_0012, "volume": 26.6315279319, "area": 207.0305796756},
    "model_56713_c077e606_0000": {"func": model_56713_c077e606_0000, "volume": 249390, "area": 55146},
    "model_56719_6e59eeff_0000": {"func": model_56719_6e59eeff_0000, "volume": 76.2803900656, "area": 416.8385774617},
    "model_57098_95ef41bb_0000": {"func": model_57098_95ef41bb_0000, "volume": 92142864.8755969405, "area": 5110580.6890408779},
    "model_57104_f2f9baa4_0000": {"func": model_57104_f2f9baa4_0000, "volume": 0.822316625, "area": 16.68158788},
    "model_57152_368e7c40_0000": {"func": model_57152_368e7c40_0000, "volume": 11874.1885401784, "area": 6847.6234762563},
    "model_57865_0744a6ab_0000": {"func": model_57865_0744a6ab_0000, "volume": 123.2743970351, "area": 304.3161622404},
    "model_60701_72ac971f_0003": {"func": model_60701_72ac971f_0003, "volume": 4.2172566612, "area": 40.1230088816},
    "model_60716_dcd9370c_0002": {"func": model_60716_dcd9370c_0002, "volume": 438.8690266447, "area": 1036.7670664596},
    "model_60753_80b955c8_0004": {"func": model_60753_80b955c8_0004, "volume": 49.9256269123, "area": 160.014162377},
    "model_60865_19bbdeb4_0029": {"func": model_60865_19bbdeb4_0029, "volume": 4.716646209, "area": 51.8004659845},
    "model_60870_1b9e95c9_0000": {"func": model_60870_1b9e95c9_0000, "volume": 262, "area": 368},
    "model_60972_b4c697a4_0000": {"func": model_60972_b4c697a4_0000, "volume": 123.4924130435, "area": 292.6804746552},
    "model_61082_9b58978f_0000": {"func": model_61082_9b58978f_0000, "volume": 193.244852478, "area": 348.6149189681},
    "model_61270_6fc99e6c_0003": {"func": model_61270_6fc99e6c_0003, "volume": 23.5517347258, "area": 62.4234460268},
    "model_61273_bf8abea3_0000": {"func": model_61273_bf8abea3_0000, "volume": 214.1979905039, "area": 419.5920835981},
    "model_61899_93eee6e5_0000": {"func": model_61899_93eee6e5_0000, "volume": 249.5688899574, "area": 423.7921847854},
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
