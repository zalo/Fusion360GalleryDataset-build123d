"""Batch 009 - passing/03_4to5ops
124 models bundled from Fusion360 Gallery reconstructions.
"""

from build123d import *
from build123d import Edge, BuildLine
from collections import Counter
from OCP.BRepBuilderAPI import BRepBuilderAPI_MakeEdge
from OCP.Geom import Geom_BSplineCurve
from OCP.TColStd import TColStd_Array1OfReal, TColStd_Array1OfInteger
from OCP.TColgp import TColgp_Array1OfPnt
from OCP.gp import gp_Pnt


# Description: This is a flat, elongated parallelogram-shaped plate or panel with a beveled leading edge and a slight three-dimensional depth, featuring a smooth upper surface with minimal features.
def model_34782_b461066c_0003():
    """Model: Keyboard v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 491.279812005, perimeter: 105.0385333414
            with BuildLine():
                Line((18, -5), (-22.3411293816, -5))
                Line((18, 7.1781372891), (18, -5))
                Line((-22.3411293816, 7.1781372891), (18, 7.1781372891))
                Line((-22.3411293816, -5), (-22.3411293816, 7.1781372891))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.2634623244, perimeter: 6.0961249026
            with BuildLine():
                Line((19.2326400824, -4.7192974663), (21, -4.7192974663))
                Line((19.2326400824, -6), (19.2326400824, -4.7192974663))
                Line((21, -6), (19.2326400824, -6))
                Line((21, -4.7192974663), (21, -6))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)
    return part.part


# Description: This is a flat, rectangular metal plate with a parallelogram shape, featuring a small elongated slot or hole near the center and a slight 3D perspective that suggests a thin, beveled edge or flange along one side.
def model_34782_b461066c_0010():
    """Model: Table2 support 2 v4"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 850, perimeter: 134
            with BuildLine():
                Line((-30, 17), (-30, 0))
                Line((-30, 0), (20, 0))
                Line((20, 0), (20, 17))
                Line((20, 17), (-30, 17))
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 2), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 15.9043128088, perimeter: 14.1371669412
            with Locations((-15, 7.5147444422)):
                Circle(2.25)
        # OneSide extrude, distance=-19
        extrude(amount=-19, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical dowel pin or shaft with a rounded head on one end and a slightly tapered or chamfered tip on the other end, featuring a smooth cylindrical body.
def model_34785_dc3b83fa_0022():
    """Model: teleskopowy wysuw2 v6"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 95.0331777711, perimeter: 34.5575191895
            Circle(5.5)
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch3 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 63.6172512352, perimeter: 28.2743338823
            Circle(4.5)
        # OneSide extrude, distance=54.5
        extrude(amount=54.5, mode=Mode.ADD)
    return part.part


# Description: This is a handle or lever consisting of a cylindrical shaft with a rounded knob or grip head on one end, designed for manual operation or control.
def model_34785_dc3b83fa_0028():
    """Model: sworzen1 v4"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 78.5398163397, perimeter: 31.4159265359
            Circle(5)
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(1.5, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 28.2743338823, perimeter: 18.8495559215
            Circle(3)
        # OneSide extrude, distance=43.5
        extrude(amount=43.5, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical fastener or dowel pin featuring a larger flange or head at one end and a long, slender shaft with subtle surface markings or text.
def model_34785_dc3b83fa_0033():
    """Model: sworzen3 v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 63.6172512352, perimeter: 28.2743338823
            Circle(4.5)
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 28.2743338823, perimeter: 18.8495559215
            Circle(3)
        # OneSide extrude, distance=26
        extrude(amount=26, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical fastener or dowel pin with a flat circular head at one end and a long smooth shaft, featuring what appears to be a small textured or knurled surface on the head for grip or identification.
def model_34785_dc3b83fa_0034():
    """Model: sworzen2 v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 63.6172512352, perimeter: 28.2743338823
            Circle(4.5)
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 28.2743338823, perimeter: 18.8495559215
            Circle(3)
        # OneSide extrude, distance=23
        extrude(amount=23, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical connector or sleeve with a smooth, hollow tubular body and a slightly textured or ribbed rim at the top end.
def model_34785_dc3b83fa_0035():
    """Model: zacisk v1 (4)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.3823007676, perimeter: 13.8230076758
            with BuildLine():
                CenterArc((0, 0), 1.2, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=5
        extrude(amount=5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 1.1309733553, perimeter: 11.3097335529
            with BuildLine():
                CenterArc((0, 0), 1, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.8, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2, mode=Mode.ADD)
    return part.part


# Description: This is a dark blue rectangular plate or flat bar with a slightly trapezoidal profile, featuring what appears to be a subtle curved or angled surface detail running along its length.
def model_34917_61633e20_0004():
    """Model: internal mesh v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 742, perimeter: 134
            with BuildLine():
                Line((-53, 14), (0, 14))
                Line((-53, 0), (-53, 14))
                Line((0, 0), (-53, 0))
                Line((0, 14), (0, 0))
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.2, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1, perimeter: 4
            with BuildLine():
                Line((-51, 12), (-52, 12))
                Line((-51, 13), (-51, 12))
                Line((-52, 13), (-51, 13))
                Line((-52, 12), (-52, 13))
            make_face()
        # OneSide extrude, distance=-0.3
        extrude(amount=-0.3, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical capsule or rounded rectangular bar with hemispherical ends, featuring circular holes or indentations on both rounded ends and horizontal slot details along its length.
def model_34917_61633e20_0007():
    """Model: horizontal pipe v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 6.157521601, perimeter: 8.7964594301
            Circle(1.4)
        # OneSide extrude, distance=10
        extrude(amount=10)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(10, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 5.3092915846, perimeter: 8.1681408993
            Circle(1.3)
        # OneSide extrude, distance=-13.5
        extrude(amount=-13.5, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a rectangular connector or housing block with a hollow central cavity, featuring four downward-extending leg-like protrusions at the base and a ribbed or finned top surface for heat dissipation.
def model_35132_35c342c8_0005():
    """Model: head"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 11 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 2.4021957543, perimeter: 8.645885432
            with BuildLine():
                Line((-1.2500000075, 3.5000000522), (-1.2500000075, 1.7000000522))
                Line((-1.2500000075, 1.7000000522), (-1.0000000149, 0))
                Line((-0.6500000075, 0), (-1.0000000149, 0))
                Line((-0.6500000097, 1.1), (-0.6500000075, 0))
                Line((-0.5000000075, 1.1), (-0.6500000097, 1.1))
                Line((-0.5000000075, 1.1), (-0.5000000075, 3.8))
                CenterArc((-0.5000000075, 2.7124998631), 1.0875001369, 90, 43.6028121033)
            make_face()
            # Profile area: 2.4021957588, perimeter: 8.64588543
            with BuildLine():
                Line((-0.5000000075, 1.1), (-0.5000000075, 3.8))
                Line((-0.3500000075, 1.1), (-0.5000000075, 1.1))
                Line((-0.3500000075, 0), (-0.3500000075, 1.1))
                Line((0, 0), (-0.3500000075, 0))
                Line((0.2499999925, 1.7000000253), (0, 0))
                Line((0.2499999925, 3.5000000522), (0.2499999925, 1.7000000253))
                CenterArc((-0.5000000075, 2.7124998631), 1.0875001369, 46.3971878967, 43.6028121033)
            make_face()
        # OneSide extrude, distance=1.1
        extrude(amount=1.1)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 9 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1.2500000075), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.449999986, perimeter: 3.1999999762
            with BuildLine():
                Line((0.4, 2.2), (0.4, 2.7000000402))
                Line((0.4, 2.2), (0.25, 2.2))
                Line((0.25, 2.2), (0.25, 1.7000000522))
                Line((0.25, 1.7000000522), (0.85, 1.7000000522))
                Line((0.85, 1.7000000522), (0.85, 2.2))
                Line((0.85, 2.2), (0.7000000104, 2.2))
                Line((0.7000000104, 2.7000000402), (0.7000000104, 2.2))
                Line((0.4, 2.7000000402), (0.7000000104, 2.7000000402))
            make_face()
            # Profile area: 1.0200000313, perimeter: 4.6000001043
            with BuildLine():
                Line((0.25, 1.7000000522), (0.25, 0))
                Line((0.25, 0), (0.85, 0))
                Line((0.85, 0), (0.85, 1.7000000522))
                Line((0.25, 1.7000000522), (0.85, 1.7000000522))
            make_face()
        # OneSide extrude, distance=-1.8
        extrude(amount=-1.8, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a spherical or dodecahedral geometric structure with a central cylindrical hub and radial fin or blade-like extensions protruding from the core, resembling a turbine rotor, impeller, or geometric art piece with symmetrical polyhedral geometry.
def model_35132_35c342c8_0010():
    """Model: tuerca1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.4702282018, perimeter: 2.472135955
            with BuildLine():
                Line((0.37148053, -0.1483314391), (0.3877210942, 0.0983481221))
                Line((0.3877210942, 0.0983481221), (0.2558653786, 0.3074620433))
                Line((0.2558653786, 0.3074620433), (0.0262777848, 0.3991359142))
                Line((0.0262777848, 0.3991359142), (-0.2133470295, 0.3383534321))
                Line((-0.2133470295, 0.3383534321), (-0.37148053, 0.1483314391))
                Line((-0.37148053, 0.1483314391), (-0.3877210942, -0.0983481221))
                Line((-0.3877210942, -0.0983481221), (-0.2558653786, -0.3074620433))
                Line((-0.2558653786, -0.3074620433), (-0.0262777848, -0.3991359142))
                Line((-0.0262777848, -0.3991359142), (0.2133470295, -0.3383534321))
                Line((0.2133470295, -0.3383534321), (0.37148053, -0.1483314391))
            make_face()
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)

        # Sketch2 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.0883572934, perimeter: 1.4137166941
            with BuildLine():
                CenterArc((0, 0), 0.175, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.05, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1, mode=Mode.ADD)

        # Sketch2 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.0078539816, perimeter: 0.3141592654
            Circle(0.05)
        # OneSide extrude, distance=-0.4
        extrude(amount=-0.4, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a long, slender rectangular extrusion or bar with a hexagonal cross-section, featuring a flat top surface and angled side facets, with subtle surface markings or grooves along its length.
def model_35145_a3d7363c_0000():
    """Model: Seat structure"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 14 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.96, perimeter: 19.2
            with BuildLine():
                Line((1.25, -1.25), (1.25, 1.25))
                Line((1.25, 1.25), (-1.25, 1.25))
                Line((-1.25, 1.25), (-1.25, -1.25))
                Line((-1.25, -1.25), (1.25, -1.25))
            make_face()
            with BuildLine():
                Line((-1.15, -1.15), (1.15, -1.15))
                Line((-1.15, 1.15), (-1.15, -1.15))
                Line((1.15, 1.15), (-1.15, 1.15))
                Line((1.15, -1.15), (1.15, 1.15))
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=14
        extrude(amount=14, both=True)
    return part.part


# Description: This is a pipe wrench or adjustable wrench featuring an elongated handle with a rounded grip section on the left end and a tapered head on the right, with horizontal slot details visible along the shaft.
def model_35145_a3d7363c_0011():
    """Model: Translational support"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 12 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 4.1233403578, perimeter: 10.9955742876
            with BuildLine():
                CenterArc((0, 0), 1.25, 90, 180)
                CenterArc((0, 0), 1.25, -90, 180)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=4.5
        extrude(amount=4.5, both=True)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        # Sketch has 12 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 58.8412614788, perimeter: 58.853981634
            with BuildLine():
                CenterArc((25.5, 0), 1.25, 90, 180)
                Line((0, 1.25), (25.5, 1.25))
                CenterArc((0, 0), 1.25, -90, 180)
                Line((0, -1.25), (25.5, -1.25))
            make_face()
        # Symmetric extrude, each_side=2
        extrude(amount=2, both=True, mode=Mode.ADD)

        # Sketch1 -> Extrude3 (Join)
        # Sketch on XY construction plane
        # Sketch has 12 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 4.1233403578, perimeter: 10.9955742876
            with BuildLine():
                CenterArc((25.5, 0), 1.25, 90, 180)
                CenterArc((25.5, 0), 1.25, -90, 180)
            make_face()
            with BuildLine():
                CenterArc((25.5, 0), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=2
        extrude(amount=2, both=True, mode=Mode.ADD)
    return part.part


# Description: This is a sheet metal box or container with an open top, featuring a trapezoidal footprint, angled side walls, and internal ribbing or bracing elements for structural reinforcement.
def model_35145_a3d7363c_0015():
    """Model: Translational piece"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 14 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 3.36, perimeter: 33.6
            with BuildLine():
                Line((2.2, -2.2), (2.2, 2.2))
                Line((2.2, 2.2), (-2.2, 2.2))
                Line((-2.2, 2.2), (-2.2, -2.2))
                Line((-2.2, -2.2), (2.2, -2.2))
            make_face()
            with BuildLine():
                Line((-2, -2), (2, -2))
                Line((-2, 2), (-2, -2))
                Line((2, 2), (-2, 2))
                Line((2, -2), (2, 2))
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=5
        extrude(amount=5, both=True)

        # Sketch2 -> Extrude2 (NewBody)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 2.2), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 16, perimeter: 16
            with BuildLine():
                Line((2, 2.2), (-2, 2.2))
                Line((2, 2.2), (2, 6.2))
                Line((2, 6.2), (-2, 6.2))
                Line((-2, 6.2), (-2, 2.2))
            make_face()
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2)
    return part.part


# Description: This is a cylindrical fastener or spacer with a textured grip surface on the main barrel and a solid, flat circular head on one end, featuring a small central hole or recess.
def model_35154_61b67282_0003():
    """Model: Bolt"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((0.7292071126, 0.0041554735)):
                Circle(0.2)
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.1119192383, perimeter: 2.9845130209
            with BuildLine():
                CenterArc((0.7292071126, 0.0041554735), 0.275, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0.7292071126, 0.0041554735), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((0.7292071126, 0.0041554735)):
                Circle(0.2)
        # OneSide extrude, distance=0.15
        extrude(amount=0.15, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical roller or spacer with a smooth, rounded body and slightly tapered or beveled ends, appearing to be a simple tubular component used for spacing, alignment, or as a mechanical roller.
def model_35166_562b126c_0009():
    """Model: 18650 Battery"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.615866758, perimeter: 5.7334065928
            Circle(0.9125)
        # OneSide extrude, distance=6.5
        extrude(amount=6.5)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 6.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.1857827237, perimeter: 8.0581851565
            with BuildLine():
                CenterArc((0, 0), 0.9125, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.37, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.02
        extrude(amount=-0.02, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a toroidal ring or torus-shaped component with two opposing elliptical cutouts and a textured mesh surface, featuring a hollow center and curved profile typical of a rotational or bearing-type part.
def model_35580_2ab34839_0006():
    """Model: Handlebar_21"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1832.6567563472, perimeter: 409.6042854737
            with BuildLine():
                CenterArc((170, 110), 31.6227766017, 0, 360)
            make_face()
            with BuildLine():
                Line((165, 105), (175, 105))
                Line((175, 105), (180, 110))
                Line((180, 110), (195, 110))
                CenterArc((170, 110), 25, 180, 180)
                Line((160, 110), (145, 110))
                Line((165, 105), (160, 110))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((165, 115), (155, 130))
                CenterArc((170, 110), 25, 53.1301023542, 73.7397952917)
                Line((175, 115), (185, 130))
                Line((165, 115), (175, 115))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=10
        extrude(amount=10)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 50.2654824574, perimeter: 25.1327412287
            with Locations((-170, 110)):
                Circle(4)
        # OneSide extrude, distance=15
        extrude(amount=15, mode=Mode.ADD)
    return part.part


# Description: This is a 3D parallelogram-shaped shelf or bracket with three horizontal rectangular tiers, featuring dark gray structural frames with blue-shaded support shelves and angled side supports.
def model_35580_2ab34839_0008():
    """Model: Ladder_25"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 15.9043128088, perimeter: 14.1371669412
            with Locations((-45, -60)):
                Circle(2.25)
            # Profile area: 15.9043128088, perimeter: 14.1371669412
            with Locations((45, -60)):
                Circle(2.25)
        # OneSide extrude, distance=10
        extrude(amount=10)

        # Sketch2 -> Extrude2 (NewBody)
        # Sketch on BRepFace
        # Sketch has 18 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 10), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 15.8997036308, perimeter: 14.1361415189
            with BuildLine():
                Line((44.8215583601, -62.2429129678), (45.1787899365, -62.2428852308))
                CenterArc((45, -60), 2.25, -85.4423466909, 80.0949217911)
                Line((47.2402077751, -59.7903118404), (47.2402077751, -60.2096881596))
                CenterArc((45, -60), 2.25, 5.3474248998, 82.5003705568)
                Line((44.9155779945, -57.7515843523), (45.0844970009, -57.7515871694))
                CenterArc((45, -60), 2.25, 92.1502934558, 173.3009506156)
            make_face()
            # Profile area: 388.6968283696, perimeter: 193.5266587607
            with BuildLine():
                CenterArc((-45, -60), 2.25, -89.4215539606, 178.9231653351)
                Line((-44.977284863, -62.2498853354), (44.8215583601, -62.2429129678))
                CenterArc((45, -60), 2.25, 92.1502934558, 173.3009506156)
                Line((-44.9804285713, -57.7500851218), (44.9155779945, -57.7515843523))
            make_face()
            # Profile area: 15.9043128088, perimeter: 14.1371669412
            with BuildLine():
                CenterArc((-45, -60), 2.25, 89.5016113745, 90.4983886255)
                CenterArc((-45, -60), 2.25, 180, 90.5784460394)
                CenterArc((-45, -60), 2.25, -89.4215539606, 178.9231653351)
            make_face()
            # Profile area: 1105.0014335666, perimeter: 505.6472822951
            with BuildLine():
                CenterArc((-45, -60), 2.25, 180, 90.5784460394)
                Line((-47.25, -60), (-47.25, -100))
                Line((47.2402077751, -100), (-47.25, -100))
                Line((47.2402077751, -60.2096881596), (47.2402077751, -100))
                CenterArc((45, -60), 2.25, -85.4423466909, 80.0949217911)
                CenterArc((45, -60), 2.25, -94.5487559286, 9.1064092377)
                Line((44.8276054473, -74.7334242629), (44.8215583601, -62.2429129678))
                Line((-44.9760039569, -74.7334242629), (44.8276054473, -74.7334242629))
                Line((-44.9760039569, -74.7334242629), (-44.977284863, -62.2498853354))
            make_face()
            with BuildLine():
                Line((44.8302932759, -80.2852465459), (-44.9758845202, -80.2852465459))
                Line((44.8375319961, -95.2371254794), (44.8302932759, -80.2852465459))
                Line((-44.9747230507, -95.2440988884), (44.8375319961, -95.2371254794))
                Line((-44.9758845202, -80.2852465459), (-44.9747230507, -95.2440988884))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=5
        extrude(amount=5)
    return part.part


# Description: This is a pergola or patio shade structure consisting of a rectangular frame with three vertical support posts and a slatted roof panel system featuring parallel cross-beams for partial sun coverage.
def model_35580_2ab34839_0009():
    """Model: Chair_24"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 50.2654824574, perimeter: 25.1327412287
            with Locations((-30, 0)):
                Circle(4)
            # Profile area: 50.2654824574, perimeter: 25.1327412287
            with Locations((-30, -50)):
                Circle(4)
            # Profile area: 50.2654824574, perimeter: 25.1327412287
            with Locations((30, -50)):
                Circle(4)
            # Profile area: 50.2654824574, perimeter: 25.1327412287
            with Locations((30, 0)):
                Circle(4)
        # OneSide extrude, distance=50
        extrude(amount=50)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 50, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 5549.7345175426, perimeter: 325.1327412287
            with BuildLine():
                Line((-40, 60), (40, 60))
                Line((-40, -10), (-40, 60))
                Line((40, -10), (-40, -10))
                Line((40, 60), (40, -10))
            make_face()
            with BuildLine():
                CenterArc((30, 50), 4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 50.2654824574, perimeter: 25.1327412287
            with Locations((30, 50)):
                Circle(4)
        # OneSide extrude, distance=7
        extrude(amount=7, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical connector or adapter with an angled circular opening at the top and a polygonal base flange with triangular support features at the bottom.
def model_35962_dbbd6e18_0002():
    """Model: short screw v6"""
    with BuildPart() as part:
        # Sketch4 -> Extrude2 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0908426513, perimeter: 2.9886878948
            with BuildLine():
                Line((-0.1443375694, -0.2500000037), (0.1443375694, -0.2500000037))
                Line((0.1443375694, -0.2500000037), (0.2886751389, 0))
                Line((0.2886751389, 0), (0.1443375694, 0.2500000037))
                Line((0.1443375694, 0.2500000037), (-0.1443375694, 0.2500000037))
                Line((-0.1443375694, 0.2500000037), (-0.2886751389, 0))
                Line((-0.2886751389, 0), (-0.1443375694, -0.2500000037))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)

        # Sketch5 -> Extrude3 (Join)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            Circle(0.2)
        # OneSide extrude, distance=0.6
        extrude(amount=0.6, mode=Mode.ADD)
    return part.part


# Description: This is a hex bolt or fastener featuring a long cylindrical shaft with a hexagonal head at the base, used for securing components together.
def model_35962_dbbd6e18_0009():
    """Model: short screw v6 (3)"""
    with BuildPart() as part:
        # Sketch4 -> Extrude2 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0908426513, perimeter: 2.9886878948
            with BuildLine():
                Line((-0.1443375694, -0.2500000037), (0.1443375694, -0.2500000037))
                Line((0.1443375694, -0.2500000037), (0.2886751389, 0))
                Line((0.2886751389, 0), (0.1443375694, 0.2500000037))
                Line((0.1443375694, 0.2500000037), (-0.1443375694, 0.2500000037))
                Line((-0.1443375694, 0.2500000037), (-0.2886751389, 0))
                Line((-0.2886751389, 0), (-0.1443375694, -0.2500000037))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)

        # Sketch5 -> Extrude3 (Join)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            Circle(0.2)
        # OneSide extrude, distance=2.8
        extrude(amount=2.8, mode=Mode.ADD)
    return part.part


# Description: This is a cable tie or strapping band with an elongated loop shape, featuring a textured webbing material and a tapered locking mechanism at one end for securing and bundling cables or components.
def model_35962_dbbd6e18_0011():
    """Model: cover v4"""
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
        # Sketch has 17 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 9.8505239603, perimeter: 48.2666188849
            with BuildLine():
                _nurbs_edge([(6.3689331224, 4.2111213873), (6.3771702722, 4.2531856104), (6.3956149612, 4.3406314554), (6.4276755697, 4.4727145766), (6.4788400118, 4.6479121542), (6.5565022552, 4.8634273512), (6.6489899373, 5.0769802512), (6.7546602011, 5.2842976693), (6.8730573532, 5.4845541076), (7.0036987552, 5.6769569181), (7.1460932976, 5.8607529763), (7.2997596126, 6.0352355904), (7.4641920924, 6.1997386035), (7.6388266368, 6.3536307617), (7.8230060691, 6.4963103501), (8.015945169, 6.627200098), (8.2166952609, 6.7457423566), (8.4242276643, 6.8514182568), (8.6375168292, 6.94376719), (8.8556233426, 7.02240666), (9.0777769865, 7.0870525526), (9.3034600338, 7.1375398735), (9.5323574507, 7.1737925612), (9.7179174327, 7.1913935188), (9.8584350524, 7.1981869236), (9.9527120238, 7.1998700195), (10.000000149, 7.2000001073)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0.5615626937, 0.5615626937, 0.5615626937, 0.5615626937, 0.5615626937, 0.5615626937, 0.58, 0.6, 0.62, 0.64, 0.66, 0.68, 0.7, 0.72, 0.74, 0.76, 0.78, 0.8, 0.82, 0.84, 0.86, 0.88, 0.9, 0.92, 0.94, 0.96, 0.98, 1, 1, 1, 1, 1, 1], 5)
                _nurbs_edge([(6.3689331224, 2.7888785955), (6.368234953, 2.7924439011), (6.3586619684, 2.8416504585), (6.3418191279, 2.9368082148), (6.3214842549, 3.0785397517), (6.3036480788, 3.2674605456), (6.2963523363, 3.500000149), (6.3036480993, 3.7325397513), (6.3214842857, 3.9214604805), (6.3418191586, 4.0631919537), (6.3586619916, 4.1583496474), (6.368234965, 4.2075561432), (6.3689331224, 4.2111213873)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0.4384372793, 0.4384372793, 0.4384372793, 0.4384372793, 0.4384372793, 0.4384372793, 0.44, 0.46, 0.48, 0.5, 0.52, 0.54, 0.56, 0.5615626937, 0.5615626937, 0.5615626937, 0.5615626937, 0.5615626937, 0.5615626937], 5)
                _nurbs_edge([(9.9999999478, -0.1999999061), (9.9527118297, -0.1998698095), (9.8584348715, -0.1981866971), (9.7179172681, -0.1913932716), (9.5323573011, -0.1737922945), (9.3034598918, -0.1375395955), (9.0777768416, -0.0870522757), (8.8556231857, -0.022406395), (8.6375166537, 0.0562330551), (8.4242274669, 0.1485819646), (8.2166950425, 0.2542578419), (8.0159449344, 0.3728000829), (7.8230058262, 0.5036898221), (7.6388263949, 0.6463694122), (7.4641918603, 0.8002615815), (7.2997593969, 0.964764612), (7.1460931021, 1.1392472462), (7.0036985807, 1.3230433234), (6.8730571984, 1.5154461493), (6.7546600639, 1.7157025985), (6.6489898157, 1.9230200236), (6.5565021484, 2.1365729282), (6.4788399407, 2.3520880696), (6.4276755248, 2.5272855887), (6.3956149354, 2.6593686498), (6.3771702605, 2.7468144338), (6.3689331224, 2.7888785955)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.02, 0.04, 0.06, 0.08, 0.1, 0.12, 0.14, 0.16, 0.18, 0.2, 0.22, 0.24, 0.26, 0.28, 0.3, 0.32, 0.34, 0.36, 0.38, 0.4, 0.42, 0.4384372793, 0.4384372793, 0.4384372793, 0.4384372793, 0.4384372793, 0.4384372793], 5)
                Line((13.6258440438, -0.2), (9.9999999478, -0.1999999061))
                Line((13.6258440438, 7.2000001073), (13.6258440438, -0.2))
                Line((10.000000149, 7.2000001073), (13.6258440438, 7.2000001073))
            make_face()
            with BuildLine():
                CenterArc((10, 3.5), 3.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.7098475127, perimeter: 3.7481120191
            with BuildLine():
                _nurbs_edge([(6.3689331224, 2.7888785955), (6.3420978665, 2.8025045965), (6.2890350451, 2.8298211855), (6.2112639024, 2.8709898294), (6.1112299337, 2.9262704633), (5.9925808554, 2.9960251458), (5.8810466466, 3.0664335858), (5.7779632731, 3.1374824571), (5.6854452017, 3.2091373044), (5.6066057167, 3.2813328656), (5.5456299965, 3.3539653285), (5.5067473871, 3.426903959), (5.4933013015, 3.5000000439), (5.5067473804, 3.5730961294), (5.545629984, 3.6460347614), (5.6066056998, 3.7186672252), (5.6854451821, 3.7908627853), (5.7779632526, 3.8625176279), (5.881046627, 3.9335664899), (5.9925808383, 4.0039749153), (6.1112299206, 4.0737295777), (6.2112638938, 4.1290101911), (6.2890350405, 4.1701788171), (6.342097865, 4.1974953931), (6.3689331224, 4.2111213873)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1, 1, 1, 1, 1, 1], 5)
                _nurbs_edge([(6.3689331224, 2.7888785955), (6.368234953, 2.7924439011), (6.3586619684, 2.8416504585), (6.3418191279, 2.9368082148), (6.3214842549, 3.0785397517), (6.3036480788, 3.2674605456), (6.2963523363, 3.500000149), (6.3036480993, 3.7325397513), (6.3214842857, 3.9214604805), (6.3418191586, 4.0631919537), (6.3586619916, 4.1583496474), (6.368234965, 4.2075561432), (6.3689331224, 4.2111213873)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0.4384372793, 0.4384372793, 0.4384372793, 0.4384372793, 0.4384372793, 0.4384372793, 0.44, 0.46, 0.48, 0.5, 0.52, 0.54, 0.56, 0.5615626937, 0.5615626937, 0.5615626937, 0.5615626937, 0.5615626937, 0.5615626937], 5)
            make_face()
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.167698931, perimeter: 43.3539786195
            with BuildLine():
                CenterArc((10, 3.5), 3.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((10, 3.5), 3.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.2
        extrude(amount=1.2, mode=Mode.ADD)
    return part.part


# Description: This is a ring or bushing assembly with a toroidal (doughnut) overall shape, featuring a hollow central bore and concentric cylindrical surfaces with parallel grooves or ridges running axially along its interior and exterior walls.
def model_35968_5488b3e5_0007():
    """Model: tuleja (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.4535674394, perimeter: 12.0951317163
            with BuildLine():
                CenterArc((0, 0), 1, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.925, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 3.926990817, perimeter: 15.7079632679
            with BuildLine():
                CenterArc((0, 0), 1.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.65
        extrude(amount=-0.65)

        # Sketch1 -> Extrude2 (Cut)
        # Sketch on YZ construction plane
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.4535674394, perimeter: 12.0951317163
            with BuildLine():
                CenterArc((0, 0), 1, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.925, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-2.5
        extrude(amount=-2.5, mode=Mode.SUBTRACT)

        # Sketch1 -> Extrude3 (Join)
        # Sketch on YZ construction plane
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.4535674394, perimeter: 12.0951317163
            with BuildLine():
                CenterArc((0, 0), 1, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.925, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-1.75
        extrude(amount=-1.75, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical housing or bracket with a rectangular flange extending from one side, featuring multiple mounting holes and a curved body designed for mechanical assembly or component mounting.
def model_35968_5488b3e5_0009():
    """Model: zacisk"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.401982251, perimeter: 29.5067177191
            with BuildLine():
                Line((-0.200000003, -5.500000082), (-0.7000000104, -5.500000082))
                Line((-0.7000000104, -5.500000082), (-0.7000000104, -7.1265006044))
                CenterArc((0, -9), 2, 110.4873154337, 319.0253691326)
                Line((0.7000000104, -5.500000082), (0.7000000104, -7.1265006044))
                Line((0.200000003, -5.500000082), (0.7000000104, -5.500000082))
                Line((0.200000003, -5.500000082), (0.200000003, -7.2614661353))
                CenterArc((0, -9), 1.75, 96.5624279669, 346.8751440663)
                Line((-0.200000003, -5.500000082), (-0.200000003, -7.2614661353))
            make_face()
        # OneSide extrude, distance=4
        extrude(amount=4)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-0.7000000104, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.6361725124, perimeter: 2.8274333882
            with Locations((6.3000000939, 3.0000000447)):
                Circle(0.45)
            # Profile area: 0.6361725124, perimeter: 2.8274333882
            with Locations((6.3000000939, 1.0000000149)):
                Circle(0.45)
        # OneSide extrude, distance=-6
        extrude(amount=-6, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical sleeve or tube with a long, uniform circular cross-section and rounded ends, featuring a smooth exterior surface suitable for mechanical assembly or connection applications.
def model_35968_5488b3e5_0010():
    """Model: podest"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.4296456416, perimeter: 29.5309709437
            with BuildLine():
                CenterArc((0, 0), 2.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 2.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=18
        extrude(amount=18)
    return part.part


# Description: This is a cylindrical pressure vessel or hydraulic tube with hemispherical end caps, featuring internal passages or channels running longitudinally through its body and connection ports on both rounded ends.
def model_36088_1ea9c8a9_0006():
    """Model: Engine Shaft"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            Circle(0.15)
        # OneSide extrude, distance=1.015
        extrude(amount=1.015)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(1.015, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0020237743, perimeter: 0.306360742
            with BuildLine():
                CenterArc((0, 0), 0.15, 150.0735651334, 59.8528697332)
                Line((-0.13, 0.0748331477), (-0.13, -0.0748331477))
            make_face()
        # OneSide extrude, distance=-0.83
        extrude(amount=-0.83, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a simple cylindrical rod or shaft with rounded ends, featuring a straight, elongated tubular shape with no holes, slots, or flanges.
def model_36088_1ea9c8a9_0013():
    """Model: Lifter"""
    with BuildPart() as part:
        # Sketch4 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            Circle(0.2)
        # Symmetric extrude, each_side=4.45
        extrude(amount=4.45, both=True)

        # Sketch5 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 8 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-4.45, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.008153738, perimeter: 0.5347517693
            with BuildLine():
                CenterArc((0, 0), 0.2, 140.1310115967, 79.7379768067)
                Line((-0.1535024454, -0.1282068612), (-0.1535024454, 0.1282068612))
            make_face()
            # Profile area: 0.008153738, perimeter: 0.5347517693
            with BuildLine():
                Line((0.1535024454, 0.1282068612), (0.1535024454, -0.1282068612))
                CenterArc((0, 0), 0.2, -39.8689884033, 79.7379768067)
            make_face()
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical ring or collar with an elliptical/oval cross-section, featuring a solid lower band and an open-lattice or mesh upper surface with internal ribbing and support structures.
def model_36194_c9cfd107_0010():
    """Model: Component4"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0075183025, perimeter: 0.4002389041
            with BuildLine():
                CenterArc((0, 0), 0.05, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.0094, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-0.0313, 0), 0.0043, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.025
        extrude(amount=0.025)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on YZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0000899202, perimeter: 0.0336150414
            with Locations((0, 0.0125)):
                Circle(0.00535)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a boat hull or ship hull component featuring a tapered, wedge-like shape with a curved bottom surface, a flat deck area, and internal structural ribbing or framing visible through transparent surfaces.
def model_36194_c9cfd107_0018():
    """Model: Component1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0072224089, perimeter: 0.4090619419
            with BuildLine():
                Line((0, 0.1), (0, 0))
                Line((0, 0), (0.075, 0))
                Line((0.075, 0), (0.075, 0.1))
                Line((0.075, 0.1), (0, 0.1))
            make_face()
            with BuildLine():
                CenterArc((0.0187, 0.05), 0.0094, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.025
        extrude(amount=0.025)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.075, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.000058088, perimeter: 0.0270176968
            with Locations((0.0188, 0.0125)):
                Circle(0.0043)
            # Profile area: 0.000058088, perimeter: 0.0270176968
            with Locations((0.0812, 0.0125)):
                Circle(0.0043)
        # OneSide extrude, distance=-0.0375
        extrude(amount=-0.0375, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a horizontal support bracket or trim piece with a rectangular base featuring a central rectangular cutout/slot and angled end flanges on both sides.
def model_36268_3c96c142_0005():
    """Model: front trim v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 14 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 12.838684, perimeter: 42.164
            with BuildLine():
                Line((-6.985, 0.635), (6.985, 0.635))
                Line((-6.985, -0.635), (-6.985, 0.635))
                Line((6.985, -0.635), (-6.985, -0.635))
                Line((6.985, 0.635), (6.985, -0.635))
            make_face()
            with BuildLine():
                Line((-2.413, -0.508), (2.413, -0.508))
                Line((-2.413, 0.508), (-2.413, -0.508))
                Line((2.413, 0.508), (-2.413, 0.508))
                Line((2.413, -0.508), (2.413, 0.508))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.3175
        extrude(amount=0.3175)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 1.548384, perimeter: 24.384
            with BuildLine():
                Line((-2.54, 0.635), (-2.54, -0.635))
                Line((-2.54, -0.635), (2.54, -0.635))
                Line((2.54, -0.635), (2.54, 0.635))
                Line((2.54, 0.635), (-2.54, 0.635))
            make_face()
            with BuildLine():
                Line((2.413, -0.508), (-2.413, -0.508))
                Line((-2.413, -0.508), (-2.413, 0.508))
                Line((-2.413, 0.508), (2.413, 0.508))
                Line((2.413, 0.508), (2.413, -0.508))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.15875
        extrude(amount=-0.15875, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical connector or coupling piece featuring two opposing curved flanges or wing-like extensions with mesh-textured surfaces, rounded ends, and what appears to be central holes or passages running through its length.
def model_36413_fb06800c_0001():
    """Model: Clamp Base Spacer v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            Circle(1)
        # Symmetric extrude, each_side=1
        extrude(amount=1, both=True)

        # Sketch3 -> Extrude2 (Cut)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            Circle(0.5)
        # Symmetric extrude, each_side=1.4
        extrude(amount=1.4, both=True, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a hexagonal or multi-sided prismatic part with an irregular stepped geometry, featuring alternating face heights that create a tiered or staggered profile, with lighter blue-shaded upper surfaces and darker navy side faces.
def model_36413_fb06800c_0008():
    """Model: Clamp Foot v2 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 4, perimeter: 8
            with BuildLine():
                Line((1, -1), (1, 1))
                Line((1, 1), (-1, 1))
                Line((-1, 1), (-1, -1))
                Line((-1, -1), (1, -1))
            make_face()
        # Symmetric extrude, each_side=1
        extrude(amount=1, both=True)

        # Sketch3 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(1, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0225, perimeter: 0.7242640687
            with BuildLine():
                Line((0, 0.85), (-0.15, 1))
                Line((0, 0.85), (0.15, 1))
                Line((0.15, 1), (-0.15, 1))
            make_face()
        # OneSide extrude, distance=-2.4
        extrude(amount=-2.4, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a plastic bracket or connector with an angular, asymmetrical shape featuring a vertical mounting flange on the left, a central horizontal bridge, and a curved cylindrical housing on the right with two circular mounting holes and internal slots for component assembly.
def model_36451_1a7f9437_0007():
    """Model: Bracket"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 61 constraints, 17 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 77.2858068798, perimeter: 85.984690109
            with BuildLine():
                CenterArc((15.4, -2), 1, 89.9999975453, 88.3530130674)
                CenterArc((15.4, 0), 1, -89.9999975453, 179.9999950905)
                CenterArc((15.4, 2), 1, -178.3530106126, 88.3530130674)
                Line((14.4004131202, 1.971258571), (14.3404758003, 4.0557950975))
                CenterArc((12.4, 4), 1.9412777814, 1.6469893874, 178.3530106126)
                Line((10.4587222186, 4), (10.4587222186, 3))
                CenterArc((9.2587222186, 3), 1.2, -90, 90)
                Line((9.2587222186, 1.8), (3.4, 1.8))
                CenterArc((3.4, 2.8), 1, 180, 90)
                Line((2.4, 2.8), (2.4, 3.3))
                CenterArc((1.9, 3.3), 0.5, 0, 90)
                Line((1.9, 3.8), (0, 3.8))
                Line((0, 3.8), (0, -3.8))
                Line((1.9, -3.8), (0, -3.8))
                CenterArc((1.9, -3.3), 0.5, -90, 90)
                Line((2.4, -2.8), (2.4, -3.3))
                CenterArc((3.4, -2.8), 1, 90, 90)
                Line((9.2587222186, -1.8), (3.4, -1.8))
                CenterArc((9.2587222186, -3), 1.2, 0, 90)
                Line((10.4587222186, -4), (10.4587222186, -3))
                CenterArc((12.4, -4), 1.9412777814, 180, 178.3530106126)
                Line((14.4004131202, -1.971258571), (14.3404758003, -4.0557950975))
            make_face()
            with BuildLine():
                CenterArc((15.4, 0), 0.8, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((9.4, 0), 0.8, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((12.4, -4), 1.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((12.4, 4), 1.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=2
        extrude(amount=2)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            with Locations((1, 2.6)):
                Circle(0.4)
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            with Locations((1, -2.6)):
                Circle(0.4)
        # OneSide extrude, distance=-2
        extrude(amount=-2, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical connector or adapter with a geometric faceted base, featuring a tall hollow cylinder mounted on an angled, multi-faced polygonal pedestal or mounting block with triangular surface facets.
def model_36735_f4ef1c35_0012():
    """Model: Screw v2 (10)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1385640687, perimeter: 1.3856406667
            with BuildLine():
                Line((0.200000003, -0.1154700556), (0.200000003, 0.1154700556))
                Line((0.200000003, 0.1154700556), (0, 0.2309401111))
                Line((0, 0.2309401111), (-0.200000003, 0.1154700556))
                Line((-0.200000003, 0.1154700556), (-0.200000003, -0.1154700556))
                Line((-0.200000003, -0.1154700556), (0, -0.2309401111))
                Line((0, -0.2309401111), (0.200000003, -0.1154700556))
            make_face()
        # OneSide extrude, distance=-0.1
        extrude(amount=-0.1)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0358963641, perimeter: 0.6716301177
            Circle(0.1068932532)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)
    return part.part


# Description: A cylindrical roller or pin with rounded ends, featuring a smooth, uniform body with a slight dark finish.
def model_36851_2c8f1bb6_0008():
    """Model: sruby resory"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(6.2074098587, 2.6799402237, 120), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1.4635829324, perimeter: 4.5033320997
            with BuildLine():
                Line((-50.375277675, -50.65), (-49.624722325, -50.65))
                Line((-49.624722325, -50.65), (-49.2494446501, -50))
                Line((-49.2494446501, -50), (-49.624722325, -49.35))
                Line((-49.624722325, -49.35), (-50.375277675, -49.35))
                Line((-50.375277675, -49.35), (-50.7505553499, -50))
                Line((-50.7505553499, -50), (-50.375277675, -50.65))
            make_face()
        # OneSide extrude, distance=0.4
        extrude(amount=0.4)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 0, 120.4), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((-50, -50)):
                Circle(0.5)
        # OneSide extrude, distance=4.5
        extrude(amount=4.5, mode=Mode.ADD)
    return part.part


# Description: This is a socket head cap screw (or hex socket bolt) featuring a cylindrical shaft with a hexagonal socket head at one end and a conical tip at the other.
def model_36851_2c8f1bb6_0013():
    """Model: sruba kola"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.0478907386, perimeter: 3.8105117767
            with BuildLine():
                Line((20.3175431944, -4.4500003155), (19.6824578983, -4.4499996845))
                Line((19.6824578983, -4.4499996845), (19.3649147039, -4.9999993691))
                Line((19.3649147039, -4.9999993691), (19.6824568056, -5.5499996845))
                Line((19.6824568056, -5.5499996845), (20.3175421017, -5.5500003155))
                Line((20.3175421017, -5.5500003155), (20.6350852961, -5.0000006309))
                Line((20.6350852961, -5.0000006309), (20.3175431944, -4.4500003155))
            make_face()
        # OneSide extrude, distance=0.4
        extrude(amount=0.4)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.4), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            with Locations((20.000000298, -5.0000000745)):
                Circle(0.4)
        # OneSide extrude, distance=2.5
        extrude(amount=2.5, mode=Mode.ADD)
    return part.part


# Description: A cylindrical roller or pin with a slightly tapered end and smooth curved surfaces, appearing to be a mechanical component used for alignment, support, or rolling applications.
def model_36851_2c8f1bb6_0019():
    """Model: sruba zaczep"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(6.2074099856, 4, 7.2268907777), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.4635829324, perimeter: 4.5033320997
            with BuildLine():
                Line((265.375277675, 95.65), (264.624722325, 95.65))
                Line((264.624722325, 95.65), (264.2494446501, 95))
                Line((264.2494446501, 95), (264.624722325, 94.35))
                Line((264.624722325, 94.35), (265.375277675, 94.35))
                Line((265.375277675, 94.35), (265.7505553499, 95))
                Line((265.7505553499, 95), (265.375277675, 95.65))
            make_face()
        # OneSide extrude, distance=0.4
        extrude(amount=0.4)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 4.4, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((265, 95)):
                Circle(0.5)
        # OneSide extrude, distance=5.2
        extrude(amount=5.2, mode=Mode.ADD)
    return part.part


# Description: This is a flat, thin metallic parallelogram plate with a simple planar geometry and no holes, slots, or additional features—just a basic four-sided geometric form with beveled or angled edges.
def model_36953_bdaf025b_0004():
    """Model: pojemnik na lalke podloga"""
    with BuildPart() as part:
        # Sketch9 -> Extrude2 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 846.84824, perimeter: 116.8728
            with BuildLine():
                Line((39.1, 1.8364), (39.1, -30))
                Line((12.5, 1.8364), (39.1, 1.8364))
                Line((12.5, -30), (12.5, 1.8364))
                Line((39.1, -30), (12.5, -30))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


# Description: This is a hexagonal or polygonal container with an open top and a protruding cylindrical straw or tube, featuring a geometric faceted body with angled surfaces and a drinking vessel-like form.
def model_37040_ecbcd25e_0013():
    """Model: swieczka3 v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 20.25, perimeter: 18
            with BuildLine():
                Line((4.5, -4.5), (0, -4.5))
                Line((4.5, 0), (4.5, -4.5))
                Line((0, 0), (4.5, 0))
                Line((0, -4.5), (0, 0))
            make_face()
        # OneSide extrude, distance=6
        extrude(amount=6)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 6, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((-2.4000000358, 2.1000000313)):
                Circle(0.15)
        # OneSide extrude, distance=1.5
        extrude(amount=1.5, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical wireless speaker or portable audio device with a slightly tapered body, featuring a small antenna or protrusion at the top and textured surface details along its sides.
def model_37040_ecbcd25e_0034():
    """Model: swieczka2 v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 28.2743338823, perimeter: 18.8495559215
            Circle(3)
        # OneSide extrude, distance=15
        extrude(amount=15)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 15, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            Circle(0.15)
        # OneSide extrude, distance=2
        extrude(amount=2, mode=Mode.ADD)
    return part.part


# Description: This is a lightweight structural bracket or frame component with an elongated diamond-shaped profile, featuring two large rectangular cutouts for weight reduction and black reinforced edges or flanges along its perimeter.
def model_37117_89aac9d4_0002():
    """Model: base_plate"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 91 constraints, 11 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 130.1346491424, perimeter: 112.3273363813
            with BuildLine():
                CenterArc((-7.6683401327, -10.1904687978), 9.1988228613, 0.0024287443, 25.4843445845)
                CenterArc((-7.6683401327, -10.1896889296), 9.1988228613, -25.4867733288, 25.4843445845)
                Line((0.635296001, -20.3500788637), (0.635296001, -14.1479674686))
                Line((9.525296001, -20.3500788637), (0.635296001, -20.3500788637))
                CenterArc((9.525296001, -19.7150788637), 0.635, -90, 90)
                Line((10.160296001, -15.2700788637), (10.160296001, -19.7150788637))
                CenterArc((17.8289321347, -10.1896889296), 9.1988228613, -179.9975712557, 33.5216212947)
                CenterArc((17.8289321347, -10.1904687978), 9.1988228613, 146.475949961, 33.5216212947)
                Line((10.160296001, -0.6650788637), (10.160296001, -5.1100788637))
                CenterArc((9.525296001, -0.6650788637), 0.635, 0, 90)
                Line((0.635296001, -0.0300788637), (9.525296001, -0.0300788637))
                Line((0.635296001, -6.2321902587), (0.635296001, -0.0300788637))
            make_face()
            with BuildLine():
                Line((8.255296001, -1.0619538637), (6.985296001, -1.0619538637))
                CenterArc((8.255296001, -1.3000788637), 0.238125, -90, 180)
                Line((6.985296001, -1.5382038637), (8.255296001, -1.5382038637))
                CenterArc((6.985296001, -1.3000788637), 0.238125, 90, 180)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((8.255296001, -19.3182038637), (6.985296001, -19.3182038637))
                CenterArc((6.985296001, -19.0800788637), 0.238125, 90, 180)
                Line((6.985296001, -18.8419538637), (8.255296001, -18.8419538637))
                CenterArc((8.255296001, -19.0800788637), 0.238125, -90, 180)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((7.2912774109, -3.2050788637), (2.8693145911, -3.2050788637))
                CenterArc((7.2912774109, -3.9942130584), 0.7891341947, -17.490801295, 107.490801295)
                Line((8.0439261566, -4.2313894543), (7.0986590337, -7.2310729228))
                CenterArc((6.5273032226, -7.0510259715), 0.5990528922, -90, 72.5091987038)
                Line((3.6332887794, -7.6500788637), (6.5273032226, -7.6500788637))
                CenterArc((3.6332887794, -7.0510259715), 0.5990528921, -162.5091987038, 72.5091987038)
                Line((2.1166658455, -4.2313894543), (3.0619329683, -7.2310729228))
                CenterArc((2.8693145911, -3.9942130584), 0.7891341947, 90, 107.490801295)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((3.175296001, -1.5382038637), (1.905296001, -1.5382038637))
                CenterArc((1.905296001, -1.3000788637), 0.238125, 90, 180)
                Line((1.905296001, -1.0619538637), (3.175296001, -1.0619538637))
                CenterArc((3.175296001, -1.3000788637), 0.238125, -90, 180)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((2.8693145911, -17.1750788637), (7.2912774109, -17.1750788637))
                CenterArc((2.8693145911, -16.3859446689), 0.7891341947, 162.5091987042, 107.4908012958)
                Line((2.1166658454, -16.148768273), (3.0619329683, -13.1490848044))
                CenterArc((3.6332887794, -13.3291317558), 0.5990528922, 90, 72.5091987006)
                Line((3.6332887794, -12.7300788637), (6.5273032226, -12.7300788637))
                CenterArc((6.5273032226, -13.3291317558), 0.5990528922, 17.4908012994, 72.5091987006)
                Line((8.0439261566, -16.148768273), (7.0986590337, -13.1490848044))
                CenterArc((7.2912774109, -16.3859446689), 0.7891341947, -90, 107.4908012958)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((3.175296001, -18.8419538637), (1.905296001, -18.8419538637))
                CenterArc((3.175296001, -19.0800788637), 0.238125, -90, 180)
                Line((1.905296001, -19.3182038637), (3.175296001, -19.3182038637))
                CenterArc((1.905296001, -19.0800788637), 0.238125, 90, 180)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 3.4805612899, perimeter: 33.255246023
            with BuildLine():
                Line((0.635296001, -6.2321902587), (0.635296001, -0.0300788637))
                CenterArc((0.635, -0.6650787947), 0.635, 89.9732919543, 90.0267080457)
                Line((0, -0.6650787947), (0, -14.9860004783))
                Line((0.000296001, -15.2700788637), (0, -14.9860004783))
                Line((0.000296001, -5.1100788637), (0.000296001, -15.2700788637))
                CenterArc((-7.6683401327, -10.1904687978), 9.1988228613, 25.4867733288, 8.0372767102)
            make_face()
            # Profile area: 3.4776379633, perimeter: 13.5034027248
            with BuildLine():
                CenterArc((-7.6683401327, -10.1896889296), 9.1988228613, -33.524050039, 8.0372767102)
                Line((0.000296001, -15.2700788637), (0, -14.9860004783))
                Line((0, -14.9860004783), (0, -19.7150788637))
                CenterArc((0.635, -19.7150788637), 0.635, -180, 90)
                Line((0.635, -20.3500788637), (0.635296001, -20.3500788637))
                Line((0.635296001, -20.3500788637), (0.635296001, -14.1479674686))
            make_face()
        # OneSide extrude, distance=0.47625
        extrude(amount=0.47625)

        # Sketch1 (1) -> Extrude1 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.47625, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 11.2800740695, perimeter: 47.3065428855
            with BuildLine():
                Line((0, 3.9949008027), (0, 16.3852568557))
                EllipticalCenterArc((0, 10.1900788292), 6.1951780265, 2.2432457357, 180, 0, -90)
            make_face()
            with BuildLine():
                Line((-0.000296001, 15.2700788637), (-0.000296001, 5.1100788637))
                CenterArc((7.6683401327, 10.1904687978), 9.1988228613, -179.9975712557, 33.5216212947)
                CenterArc((7.6683401327, 10.1896889296), 9.1988228613, 146.475949961, 33.5216212947)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 21.829838301, perimeter: 26.3827673008
            with BuildLine():
                EllipticalCenterArc((0, 10.1900788292), 6.1951780265, 2.2432457357, 180, 0, -90)
                Line((0, 3.9949008027), (0, 16.3852568557))
            make_face()
            # Profile area: 10.5497642315, perimeter: 20.9237755846
            with BuildLine():
                CenterArc((7.6683401327, 10.1896889296), 9.1988228613, 146.475949961, 33.5216212947)
                CenterArc((7.6683401327, 10.1904687978), 9.1988228613, -179.9975712557, 33.5216212947)
                Line((-0.000296001, 15.2700788637), (-0.000296001, 5.1100788637))
            make_face()
        # OneSide extrude, distance=-2.54
        extrude(amount=-2.54, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical linear actuator or pneumatic cylinder with a long slender body, a slightly tapered upper end, and a protruding rod or connector at the bottom.
def model_37117_89aac9d4_0006():
    """Model: arm_soup"""
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
        # OneSide extrude, distance=6.35
        extrude(amount=6.35, mode=Mode.ADD)
    return part.part


# Description: A long, rectangular steel bar or rail with a uniform cross-section, featuring tapered or beveled ends and what appears to be a central slot or groove running along its length.
def model_37377_90529181_0014():
    """Model: KORYTO v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 262.5, perimeter: 181
            with BuildLine():
                Line((81.5, 1), (-6, 1))
                Line((81.5, 4), (81.5, 1))
                Line((-6, 4), (81.5, 4))
                Line((-6, 1), (-6, 4))
            make_face()
        # OneSide extrude, distance=2.3
        extrude(amount=2.3)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 9 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2.3, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 131.25, perimeter: 178
            with BuildLine():
                Line((-81.5, -1.75), (6, -1.75))
                Line((-81.5, -3.25), (-81.5, -1.75))
                Line((6, -3.25), (-81.5, -3.25))
                Line((6, -3.25), (6, -1.75))
            make_face()
        # OneSide extrude, distance=-0.4
        extrude(amount=-0.4, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a black extruded aluminum or composite channel with a long, rectangular profile featuring a closed U-shaped or box-like cross-section and angled end caps.
def model_37520_18f4b548_0002():
    """Model: mocowanie prawe"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(69.1243240282, 0, -0.0000002369), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 638.5, perimeter: 149
            with BuildLine():
                Line((143.3692592035, -26.5814849801), (143.3692592035, -28.0814849801))
                Line((163.3692592035, -26.5814849801), (143.3692592035, -26.5814849801))
                Line((163.3692592035, -18.5814849801), (163.3692592035, -26.5814849801))
                Line((143.3692592035, -18.5814849801), (163.3692592035, -18.5814849801))
                Line((143.3692592035, -17.0814849801), (143.3692592035, -18.5814849801))
                Line((143.3692592035, -17.0814849801), (99.8692592035, -17.0814849801))
                Line((99.8692592035, -17.0814849801), (99.8692592035, -28.0814849801))
                Line((99.8692592035, -28.0814849801), (143.3692592035, -28.0814849801))
            make_face()
            # Profile area: 76.5, perimeter: 105
            with BuildLine():
                Line((164.8692592035, -28.0814849801), (164.8692592035, -17.0814849801))
                Line((164.8692592035, -17.0814849801), (143.3692592035, -17.0814849801))
                Line((143.3692592035, -17.0814849801), (143.3692592035, -18.5814849801))
                Line((143.3692592035, -18.5814849801), (163.3692592035, -18.5814849801))
                Line((163.3692592035, -18.5814849801), (163.3692592035, -26.5814849801))
                Line((163.3692592035, -26.5814849801), (143.3692592035, -26.5814849801))
                Line((143.3692592035, -26.5814849801), (143.3692592035, -28.0814849801))
                Line((143.3692592035, -28.0814849801), (164.8692592035, -28.0814849801))
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2)

        # Sketch3 -> Extrude2 (Join)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, -17.0814849801, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 318.853690488, perimeter: 215.1982977362
            with BuildLine():
                Line((-67.1243240282, 160.8692589667), (-67.1243240282, 164.8692589667))
                Line((-67.1243240282, 160.8692589667), (-54, 160.8692589667))
                Line((-54, 160.8692589667), (-54, 112.281164805))
                Line((-54, 112.281164805), (-67.1243240282, 104.516821655))
                Line((-67.1243240282, 99.8692589667), (-67.1243240282, 104.516821655))
                Line((-67.1243240282, 99.8692589667), (-50, 110))
                Line((-50, 110), (-50, 164.8692589667))
                Line((-67.1243240282, 164.8692589667), (-50, 164.8692589667))
            make_face()
            with BuildLine():
                CenterArc((-52, 157), 1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-52, 162), 1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-52, 140), 1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-52, 130), 1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-52, 117), 1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-52, 112), 1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-2
        extrude(amount=-2, mode=Mode.ADD)
    return part.part


# Description: This is a metal channel or C-channel beam with a hollow rectangular cross-section, featuring two parallel flanges connected by a central web, designed for structural support applications.
def model_37599_faf701a1_0005():
    """Model: podst"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))) as sk:
            # Profile area: 43.3342561034, perimeter: 54.3814777688
            with BuildLine():
                Line((-7.3, -20), (-7.3, 5.4907388844))
                Line((-7.3, 5.4907388844), (-9, 5.4907388844))
                Line((-9, 5.4907388844), (-9, -20))
                Line((-9, -20), (-7.3, -20))
            make_face()
        # TwoSides extrude, along=7.5, against=-5
        extrude(amount=7.5)
        extrude(sk.sketch, amount=-5)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 5.4907388844, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 11.25, perimeter: 18
            with BuildLine():
                Line((-5, 9), (2.5, 9))
                Line((-5, 7.5), (-5, 9))
                Line((2.5, 7.5), (-5, 7.5))
                Line((2.5, 9), (2.5, 7.5))
            make_face()
        # OneSide extrude, distance=-33.5
        extrude(amount=-33.5, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a stunt scooter or trick scooter deck with an elongated, slightly curved platform featuring blue accent stripes and a vertical handlebar post extending upward from the rear.
def model_37599_faf701a1_0010():
    """Model: ramiona"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 7.0705920679, perimeter: 13.4498146545
            with BuildLine():
                CenterArc((0, 0), 1.5, -40.4278323536, 80.8556647072)
                Line((6, -0.5), (1.1418350744, -0.9727346312))
                CenterArc((6, 0), 0.5, -90, 180)
                Line((6, 0.5), (1.1418350744, 0.9727346312))
            make_face()
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((-6, 0)):
                Circle(0.15)
        # OneSide extrude, distance=1.8
        extrude(amount=1.8, mode=Mode.ADD)
    return part.part


# Description: This is a tape dispenser head featuring a cylindrical roller housing with a mesh/perforated curved surface, a flat rectangular tape guide slot extending from the front, and an internal cylindrical core for holding and dispensing tape.
def model_37605_e35cc4df_0002():
    """Model: swiatla"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            with Locations((18, 3)):
                Circle(0.4)
        # OneSide extrude, distance=0.4
        extrude(amount=0.4)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.0408413192, perimeter: 0.8275474702
            with BuildLine():
                CenterArc((-18, 3), 0.4, -104.4775520862, 28.9550248128)
                Line((-18.1000002697, 2.4000000358), (-18.1000002697, 2.612701735))
                Line((-17.9000002667, 2.4000000358), (-18.1000002697, 2.4000000358))
                Line((-17.9000002667, 2.6127015965), (-17.9000002667, 2.4000000358))
            make_face()
            # Profile area: 0.099158685, perimeter: 1.376740971
            with BuildLine():
                Line((-17.9000002667, 3.1000000462), (-17.9000002667, 2.6127015965))
                Line((-18.1000002697, 3.1000000462), (-17.9000002667, 3.1000000462))
                Line((-18.1000002697, 2.612701735), (-18.1000002697, 3.1000000462))
                CenterArc((-18, 3), 0.4, -104.4775520862, 28.9550248128)
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)
    return part.part


# Description: This is a curved ducting or manifold component with a rounded cylindrical body, a rectangular flanged outlet port on the upper right, and internal ribbed reinforcement structures visible through transparent sections.
def model_37605_e35cc4df_0012():
    """Model: lycha"""
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
            # Profile area: 16.9058154308, perimeter: 17.9995663127
            with BuildLine():
                Line((-61.6754928955, 13.9152668364), (-62.0797659994, 12.3761685693))
                _nurbs_edge([(-62.0797659994, 12.3761685693), (-62.0489218963, 12.307029352), (-61.9860970665, 12.1717572258), (-61.8884504928, 11.977868164), (-61.7514139317, 11.7374329758), (-61.5679327417, 11.4672330142), (-61.3700040001, 11.2274775186), (-61.1533818761, 11.0180545315), (-60.9107271525, 10.8382896476), (-60.6327769251, 10.6874790126), (-60.3115413334, 10.566228196), (-59.9428045747, 10.4774738096), (-59.5292809736, 10.4278404769), (-59.0826310967, 10.4282902941), (-58.6200113075, 10.4913174309), (-58.1614264472, 10.6286343011), (-57.7267382892, 10.8485412081), (-57.333015259, 11.1535940846), (-56.9912576726, 11.5375095122), (-56.7047773479, 11.9840373547), (-56.4715066921, 12.4705753423), (-56.2854715842, 12.9707853686), (-56.1385030866, 13.4574853642), (-56.0218464771, 13.9055136474), (-55.927662373, 14.2943416435), (-55.85087625, 14.6115693512), (-55.8013382328, 14.8036633879), (-55.7704479423, 14.9123681702), (-55.7526323609, 14.9691644068), (-55.7444189683, 14.9936439141)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.04, 0.08, 0.12, 0.16, 0.2, 0.24, 0.28, 0.32, 0.36, 0.4, 0.44, 0.48, 0.52, 0.56, 0.6, 0.64, 0.68, 0.72, 0.76, 0.8, 0.84, 0.88, 0.92, 0.96, 1, 1, 1, 1, 1, 1], 5)
                Line((-56.6512360563, 13.9152668364), (-55.7444189683, 14.9936439141))
                Line((-61.6754928955, 13.9152668364), (-56.6512360563, 13.9152668364))
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 4.2731489313, perimeter: 14.282484267
            with BuildLine():
                CenterArc((-63, 15), 1, 0, 199.9856499891)
                Line((-63.9397782519, 14.6582152181), (-63.9397782519, 13.4496040074))
                Line((-63.9397782519, 13.4496040074), (-62.0797659994, 12.3761685693))
                Line((-61.6754928955, 13.9152668364), (-62.0797659994, 12.3761685693))
                Line((-62, 15), (-61.6754928955, 13.9152668364))
            make_face()
            with BuildLine():
                CenterArc((-63, 15), 0.75, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)

        # Sketch1 -> Extrude3 (Join)
        # Sketch on XY construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 16.9058154308, perimeter: 17.9995663127
            with BuildLine():
                Line((-61.6754928955, 13.9152668364), (-62.0797659994, 12.3761685693))
                _nurbs_edge([(-62.0797659994, 12.3761685693), (-62.0489218963, 12.307029352), (-61.9860970665, 12.1717572258), (-61.8884504928, 11.977868164), (-61.7514139317, 11.7374329758), (-61.5679327417, 11.4672330142), (-61.3700040001, 11.2274775186), (-61.1533818761, 11.0180545315), (-60.9107271525, 10.8382896476), (-60.6327769251, 10.6874790126), (-60.3115413334, 10.566228196), (-59.9428045747, 10.4774738096), (-59.5292809736, 10.4278404769), (-59.0826310967, 10.4282902941), (-58.6200113075, 10.4913174309), (-58.1614264472, 10.6286343011), (-57.7267382892, 10.8485412081), (-57.333015259, 11.1535940846), (-56.9912576726, 11.5375095122), (-56.7047773479, 11.9840373547), (-56.4715066921, 12.4705753423), (-56.2854715842, 12.9707853686), (-56.1385030866, 13.4574853642), (-56.0218464771, 13.9055136474), (-55.927662373, 14.2943416435), (-55.85087625, 14.6115693512), (-55.8013382328, 14.8036633879), (-55.7704479423, 14.9123681702), (-55.7526323609, 14.9691644068), (-55.7444189683, 14.9936439141)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.04, 0.08, 0.12, 0.16, 0.2, 0.24, 0.28, 0.32, 0.36, 0.4, 0.44, 0.48, 0.52, 0.56, 0.6, 0.64, 0.68, 0.72, 0.76, 0.8, 0.84, 0.88, 0.92, 0.96, 1, 1, 1, 1, 1, 1], 5)
                Line((-56.6512360563, 13.9152668364), (-55.7444189683, 14.9936439141))
                Line((-61.6754928955, 13.9152668364), (-56.6512360563, 13.9152668364))
            make_face()
        # OneSide extrude, distance=-2
        extrude(amount=-2, mode=Mode.ADD)

        # Sketch1 -> Extrude4 (Join)
        # Sketch on XY construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 4.2731489313, perimeter: 14.282484267
            with BuildLine():
                CenterArc((-63, 15), 1, 0, 199.9856499891)
                Line((-63.9397782519, 14.6582152181), (-63.9397782519, 13.4496040074))
                Line((-63.9397782519, 13.4496040074), (-62.0797659994, 12.3761685693))
                Line((-61.6754928955, 13.9152668364), (-62.0797659994, 12.3761685693))
                Line((-62, 15), (-61.6754928955, 13.9152668364))
            make_face()
            with BuildLine():
                CenterArc((-63, 15), 0.75, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.ADD)
    return part.part


# Description: This is a black metal mounting bracket or support rail featuring an elongated tubular body with perpendicular flanges at each end and a central support lug, designed to attach or suspend components.
def model_37605_e35cc4df_0015():
    """Model: belka swiatla"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 9 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 2.0999999982, perimeter: 14.6000002563
            with BuildLine():
                Line((16.7000002488, 3.8), (11.3000001684, 3.8))
                Line((11.3000001684, 3.8), (11.3000001684, 4.3000000641))
                Line((11.3000001684, 4.3000000641), (11, 4.3000000641))
                Line((11, 4.3000000641), (11, 3.5))
                Line((11, 3.5), (17, 3.5))
                Line((17, 4.3000000641), (17, 3.5))
                Line((16.7000002488, 4.3000000641), (17, 4.3000000641))
                Line((16.7000002488, 3.8), (16.7000002488, 4.3000000641))
            make_face()
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.0039269908, perimeter: 0.2570796327
            with BuildLine():
                CenterArc((-12.5, 3.6649981594), 0.05, 180, 180)
                Line((-12.45, 3.6649981594), (-12.55, 3.6649981594))
            make_face()
            # Profile area: 0.0039269908, perimeter: 0.2570796327
            with BuildLine():
                Line((-12.45, 3.6649981594), (-12.55, 3.6649981594))
                CenterArc((-12.5, 3.6649981594), 0.05, 0, 180)
            make_face()
            # Profile area: 0.0039269908, perimeter: 0.2570796327
            with BuildLine():
                CenterArc((-15.5, 3.6649981594), 0.05, 180, 180)
                Line((-15.55, 3.6649981594), (-15.45, 3.6649981594))
            make_face()
            # Profile area: 0.0039269908, perimeter: 0.2570796327
            with BuildLine():
                Line((-15.55, 3.6649981594), (-15.45, 3.6649981594))
                CenterArc((-15.5, 3.6649981594), 0.05, 0, 180)
            make_face()
        # OneSide extrude, distance=0.6
        extrude(amount=0.6, mode=Mode.ADD)
    return part.part


# Description: This is a bolt or fastener with a long cylindrical shaft and a hexagonal head at the top, designed for threaded fastening applications.
def model_37615_8399c412_0008():
    """Model: Component7"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.3848451001, perimeter: 2.1991148575
            Circle(0.35)
        # OneSide extrude, distance=-5.2
        extrude(amount=-5.2)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.6630456385, perimeter: 6.0096266342
            with BuildLine():
                Line((-0.55, 0.3175426481), (-0.55, -0.3175426481))
                Line((-0.55, -0.3175426481), (0, -0.6350852961))
                Line((0, -0.6350852961), (0.55, -0.3175426481))
                Line((0.55, -0.3175426481), (0.55, 0.3175426481))
                Line((0.55, 0.3175426481), (0, 0.6350852961))
                Line((0, 0.6350852961), (-0.55, 0.3175426481))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.35, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.3848451001, perimeter: 2.1991148575
            Circle(0.35)
        # OneSide extrude, distance=0.55
        extrude(amount=0.55, mode=Mode.ADD)
    return part.part


# Description: A rectangular box-shaped bracket or enclosure with two circular holes on the front face, angled side panels, and internal structural ribs for reinforcement.
def model_37615_8399c412_0012():
    """Model: Component5"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 8 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.28, perimeter: 8.8
            with BuildLine():
                Line((0, -3.4), (0, 0))
                Line((0, -3.4), (1, -3.4))
                Line((1, -3.4), (1, -2.8))
                Line((1, -2.8), (0.6, -2.8))
                Line((0.6, 0), (0.6, -2.8))
                Line((0, 0), (0.6, 0))
            make_face()
        # OneSide extrude, distance=3.6
        extrude(amount=3.6)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            with Locations((1.0000157235, 2.6999612716)):
                Circle(0.4)
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            with Locations((1.0000157235, 0.9000387284)):
                Circle(0.4)
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a flexible coupling hub featuring a circular disk face with multiple bolt holes around its perimeter, a central bore, and a textured rim flange for torsional power transmission between shafts.
def model_37683_e2cca100_0001():
    """Model: LID4"""
    with BuildPart() as part:
        # Sketch2 -> Extrude2 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 5 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 2.7017696821, perimeter: 8.1681408993
            with BuildLine():
                CenterArc((0, 0), 0.95, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0.8), 0.1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0, -0.8), 0.1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0, 0), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.0000000105, 0, 0.2), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.3141592654, perimeter: 3.1415926536
            with BuildLine():
                CenterArc((-0.0000000105, 0), 0.35, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-0.0000000105, 0), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)
    return part.part


# Description: This is a parallelogram-shaped panel or bracket with a slanted rectangular form, featuring a vertical slot or channel running along one of its narrower sides.
def model_37683_e2cca100_0011():
    """Model: plate1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.9500000182, perimeter: 5.6000000242
            with BuildLine():
                Line((0, 0), (-1.3, 0))
                Line((-1.3000000242, -1.5), (-1.3, 0))
                Line((0, -1.5), (-1.3000000242, -1.5))
                Line((0, 0), (0, -1.5))
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.6361725124, perimeter: 2.8274333882
            with Locations((0.65, -0.55)):
                Circle(0.45)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)
    return part.part


# Description: This is a rectangular channel or U-shaped bracket with two parallel vertical walls connected by a base, featuring a central vertical divider or web that creates two separate compartments, with open top edges and a tapered or angled upper section.
def model_37846_cde34fcd_0000():
    """Model: Karetka v4"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 20 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.0284947126, perimeter: 9.4994406193
            with BuildLine():
                Line((1.89, 0.87), (0.8, 0.87))
                Line((1.89, 0.87), (1.89, 0))
                Line((1.89, 0), (2.69, 0))
                Line((2.69, 0), (2.69, 0.0559556362))
                Line((2.69, 0.0559556362), (2.12, 0.87))
                Line((2.12, 0.87), (2.12, 1.58))
                Line((2.12, 1.58), (0.57, 1.58))
                Line((0.57, 0.87), (0.57, 1.58))
                Line((0, 0.0559556362), (0.57, 0.87))
                Line((0, 0), (0, 0.0559556362))
                Line((0.8, 0), (0, 0))
                Line((0.8, 0.87), (0.8, 0))
            make_face()
        # OneSide extrude, distance=5
        extrude(amount=5)
    return part.part


# Description: This is a mushroom-shaped fastener or connector featuring a wide, curved circular head with a mesh/textured surface and a cylindrical stem, designed for assembly or mounting applications.
def model_37846_cde34fcd_0024():
    """Model: M2x3s v2 (1)"""
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
            # Profile area: 0.2513274123, perimeter: 2.5132741229
            with BuildLine():
                CenterArc((0, 0), 0.3, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            Circle(0.1)
        # OneSide extrude, distance=0.13
        extrude(amount=0.13, mode=Mode.ADD)
    return part.part


# Description: This is a bracket or mounting clamp featuring a rectangular main body with an extended arm or lever that projects from one side, designed to grip or hold cylindrical objects through a slot or opening mechanism.
def model_37846_cde34fcd_0046():
    """Model: Mocowanie glowicy v4"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 16 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.09, perimeter: 6.3
            with BuildLine():
                Line((3.45, -0.95), (3.45, -1.9))
                Line((1.25, -0.95), (3.45, -0.95))
                Line((1.25, -1.9), (1.25, -0.95))
                Line((3.45, -1.9), (1.25, -1.9))
            make_face()
            # Profile area: 2.93, perimeter: 11.9
            with BuildLine():
                Line((3.45, -0.3), (3.45, -0.95))
                Line((5, -0.3), (3.45, -0.3))
                Line((5, 0), (5, -0.3))
                Line((0, 0), (5, 0))
                Line((0, -0.3), (0, 0))
                Line((1.25, -0.3), (0, -0.3))
                Line((1.25, -0.95), (1.25, -0.3))
                Line((1.25, -0.95), (3.45, -0.95))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 16 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.09, perimeter: 6.3
            with BuildLine():
                Line((3.45, -0.95), (3.45, -1.9))
                Line((1.25, -0.95), (3.45, -0.95))
                Line((1.25, -1.9), (1.25, -0.95))
                Line((3.45, -1.9), (1.25, -1.9))
            make_face()
        # OneSide extrude, distance=2.7
        extrude(amount=2.7, mode=Mode.ADD)
    return part.part


# Description: This is a elongated hexagonal prism featuring beveled or chamfered edges along its length, creating a refined geometric form with faceted surfaces in light and dark blue shading.
def model_38196_ea48fa42_0007():
    """Model: Left"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 4 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.9670874172, perimeter: 4.2176379319
            with BuildLine():
                Line((-1.75, 0.35), (-1.2842334805, 0.35))
                Line((-1.15, 0.5417052776), (-1.2842334805, 0.35))
                Line((-0.4965, 1.475), (-1.15, 0.5417052776))
                Line((-1.75, 1.475), (-0.4965, 1.475))
                Line((-1.75, 0.35), (-1.75, 1.475))
            make_face()
            # Profile area: 0.0128666333, perimeter: 0.5599676895
            with BuildLine():
                Line((-1.2842334805, 0.35), (-1.15, 0.35))
                Line((-1.15, 0.35), (-1.15, 0.5417052776))
                Line((-1.15, 0.5417052776), (-1.2842334805, 0.35))
            make_face()
        # Symmetric extrude, each_side=2.325
        extrude(amount=2.325, both=True)
    return part.part


# Description: This is a cylindrical roller or spacer with a smooth dark surface and a slightly textured or knurled band around its middle section, featuring rounded ends and a uniform tubular shape.
def model_38196_ea48fa42_0009():
    """Model: Bar"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -2.325), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0176714587, perimeter: 0.471238898
            with Locations((0, 0.88)):
                Circle(0.075)
        # OneSide extrude, distance=-0.1
        extrude(amount=-0.1)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -2.325), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.1343816258, perimeter: 1.8535396656
            with BuildLine():
                CenterArc((0, 0.88), 0.22, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0.88), 0.075, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0176714587, perimeter: 0.471238898
            with Locations((0, 0.88)):
                Circle(0.075)
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)
    return part.part


# Description: This is a horseshoe-shaped magnetic core or transformer component featuring a curved, toroidal design with a central rectangular opening and layered/laminated construction visible on its surface.
def model_38276_c9ef069a_0007():
    """Model: Piece 6"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 10 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 25.6544855632, perimeter: 31.5923332641
            with BuildLine():
                CenterArc((-9.4, 2.5), 3, -108.2766895168, 0.6045303651)
                CenterArc((-7.8, -2.5), 3.3, 139.5366567888, 7.8112512456)
                CenterArc((-7.8, -2.5), 3.3, 147.3479080344, 32.6520919656)
                Line((-8.8670001642, -2.5), (-11.1, -2.5))
                CenterArc((-5.5670005077, -2.4984941484), 3.3, 128.477323578, 51.5488215559)
                CenterArc((-9.4, 2.5), 3, -53.6126500295, 233.6126500295)
                Line((-12.4, 2.5), (-12.3852809601, 2.203187619))
                Line((-12.3852809601, 2.203187619), (-12.3243863301, 0.9752352401))
                CenterArc((-11.825, 1), 0.5, -177.1610059931, 177.1610059931)
                Line((-11.325, 1), (-11.25, 2.5))
                CenterArc((-10, 2.5), 1.25, -32.652104007, 212.652104007)
                Line((-10.3408184839, -0.3486594357), (-8.9475473777, 1.8255791538))
            make_face()
        # OneSide extrude, distance=1.4
        extrude(amount=1.4)
    return part.part


# Description: This is a dark metal bracket or mounting clamp with an elongated, angled shape featuring two oval holes for fastening and a curved flange at the base for structural support.
def model_38287_88ec74de_0010():
    """Model: RamieStojaka v1 v2 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 47.2511064281, perimeter: 45.4203522483
            with BuildLine():
                Line((2.5, 5), (2.5, -5))
                CenterArc((0, 5), 2.5, 0, 180)
                Line((-2.5, -5), (-2.5, 5))
                Line((2.5, -5), (-2.5, -5))
            make_face()
            with BuildLine():
                CenterArc((0, 5), 2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on YZ construction plane
        # Sketch has 9 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 38.3318510837, perimeter: 50.2202254389
            with BuildLine():
                Line((6.8248983845, 11.3860231396), (2.6317121127, 0.4107407963))
                CenterArc((4.7230745113, 12.1890402042), 2.25, -20.909719689, 165.9400262439)
                Line((2.8793000358, 13.4786121035), (-2.0486383061, 6.4328576659))
                CenterArc((0, 5), 2.5, 0, 145.0303065548)
                Line((2.5, -0.30305215), (2.5, 5))
                CenterArc((4.5, -0.30305215), 2, 159.090280311, 20.909719689)
            make_face()
            with BuildLine():
                CenterArc((4.7230745113, 12.1890402042), 1.75, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)
    return part.part


# Description: This is a paraglider wing featuring an elliptical planform shape with internal structural ribs and suspension lines, designed to generate lift through airfoil geometry with a reinforced leading edge and perimeter trim.
def model_38287_88ec74de_0036():
    """Model: opór v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 9.6211275016, perimeter: 10.9955742876
            Circle(1.75)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.9452431127, perimeter: 23.5619449019
            with BuildLine():
                CenterArc((0, 0), 2, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.75, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.3
        extrude(amount=-0.3, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical tube or pipe with a uniform hollow circular cross-section, featuring a slightly textured or threaded rim at the top end and a smooth tapered or beveled edge at the bottom.
def model_38287_88ec74de_0079():
    """Model: Krótkisil v2 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.7671458676, perimeter: 14.1371669412
            with BuildLine():
                CenterArc((0, 0), 1.25, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=10
        extrude(amount=10)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 10, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.9087385212, perimeter: 7.853981634
            Circle(1.25)
        # OneSide extrude, distance=0.25
        extrude(amount=0.25, mode=Mode.ADD)
    return part.part


# Description: This is a thin, elongated triangular or crescent-shaped blade or fin with a curved upper edge and pointed ends, featuring a smooth aerodynamic profile typical of a spoiler, winglet, or deflector component.
def model_38288_740bfe5a_0002():
    """Model: Left Plate v5"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 3 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 688.8121281786, perimeter: 142.2489224804
            with BuildLine():
                CenterArc((30.5772212843, 22.4691328593), 24.9820854656, 120.2351093771, 25.1101341535)
                CenterArc((-1.526316555, 43.1619390423), 13.2501427003, -83.3852739371, 54.0711309035)
                Line((0, 0), (0, 30))
                CenterArc((21.2882177343, -7.6921451562), 22.6353111622, 126.7878097547, 33.3457071609)
                CenterArc((-19.5898675551, 47.2849710602), 45.8739449319, -53.4440630533, 17.2350606707)
                CenterArc((39.8278439407, 1.4738675892), 29.1899265988, 113.2949318506, 26.8357441926)
                Line((28.2842712475, 28.2842712475), (28.2842712475, 58.2842712475))
                CenterArc((8.1950545615, 61.9716747945), 20.4248273426, -61.3192855949, 50.9183410682)
            make_face()
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1.5), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((5, 20)):
                Circle(0.5)
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((25, 40)):
                Circle(0.5)
        # OneSide extrude, distance=-18
        extrude(amount=-18, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical container or vessel with a protruding nozzle or spout at the top, featuring a textured or ribbed surface pattern and an open top rim.
def model_38675_6e07d74b_0000():
    """Model: motor v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 7.0685834706, perimeter: 9.4247779608
            Circle(1.5)
        # OneSide extrude, distance=4
        extrude(amount=4)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 4, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            Circle(0.25)
        # OneSide extrude, distance=1.5
        extrude(amount=1.5, mode=Mode.ADD)
    return part.part


# Description: This is a hammer featuring a dark gray cylindrical head with a flat striking surface and a long handle, designed for striking or driving applications.
def model_38675_6e07d74b_0003():
    """Model: rubber hold v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            Circle(0.25)
        # OneSide extrude, distance=2.5
        extrude(amount=2.5)

        # Sketch2 -> Extrude2 (NewBody)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 2.9452432064, perimeter: 7.8539817276
            with BuildLine():
                CenterArc((0, 0), 1.0000000149, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


# Description: This is a bracket or mounting plate featuring a large rectangular body with two protruding rectangular flanges or tabs extending from its lower right side, designed for fastening or alignment purposes.
def model_38675_6e07d74b_0005():
    """Model: charger v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 20, perimeter: 18
            with BuildLine():
                Line((2, -2.5), (2, 2.5))
                Line((2, 2.5), (-2, 2.5))
                Line((-2, 2.5), (-2, -2.5))
                Line((-2, -2.5), (2, -2.5))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 18 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.200000006, perimeter: 2.4000000358
            with BuildLine():
                Line((0.1000000015, 1.0000000149), (0.1000000015, 2.0000000298))
                Line((0.1000000015, 2.0000000298), (-0.1000000015, 2.0000000298))
                Line((-0.1000000015, 2.0000000298), (-0.1000000015, 1.0000000149))
                Line((-0.1000000015, 1.0000000149), (0.1000000015, 1.0000000149))
            make_face()
            # Profile area: 0.4000000119, perimeter: 2.8000000417
            with BuildLine():
                Line((-0.5000000075, -1.2000000179), (-1.5000000224, -1.2000000179))
                Line((-0.5000000075, -0.8000000119), (-0.5000000075, -1.2000000179))
                Line((-1.5000000224, -0.8000000119), (-0.5000000075, -0.8000000119))
                Line((-1.5000000224, -1.2000000179), (-1.5000000224, -0.8000000119))
            make_face()
            # Profile area: 0.4000000119, perimeter: 2.8000000417
            with BuildLine():
                Line((1.5000000224, -1.2000000179), (1.5000000224, -0.8000000119))
                Line((1.5000000224, -0.8000000119), (0.5000000075, -0.8000000119))
                Line((0.5000000075, -0.8000000119), (0.5000000075, -1.2000000179))
                Line((0.5000000075, -1.2000000179), (1.5000000224, -1.2000000179))
            make_face()
        # OneSide extrude, distance=2.5
        extrude(amount=2.5, mode=Mode.ADD)
    return part.part


# Description: This is a curved ducting or air intake component with a bulbous, teardrop-like shape featuring a flat rectangular opening on one end, curved side walls with mesh or perforated sections, and a tapered bottom designed for aerodynamic flow direction.
def model_38739_f321c899_0009():
    """Model: Foot Rest v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 8 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 78.6163830947, perimeter: 34.2843793452
            with BuildLine():
                CenterArc((-1.27, 0.635), 4.445, 180, 90)
                Line((1.27, -3.81), (-1.27, -3.81))
                CenterArc((1.27, 0.635), 4.445, -90, 90)
                Line((5.715, 3.81), (5.715, 0.635))
                Line((-5.715, 3.81), (5.715, 3.81))
                Line((-5.715, 0.635), (-5.715, 3.81))
            make_face()
        # OneSide extrude, distance=0.635
        extrude(amount=0.635)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 11 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0.635, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 2.8771708029, perimeter: 45.5637764234
            with BuildLine():
                Line((-5.715, 3.81), (-5.715, 0.635))
                CenterArc((-1.27, 0.635), 4.445, 180, 90)
                Line((-1.27, -3.81), (1.27, -3.81))
                CenterArc((1.27, 0.635), 4.445, -90, 90)
                Line((5.715, 0.635), (5.715, 3.81))
                Line((5.715, 3.81), (5.588, 3.81))
                Line((5.588, 0.635), (5.588, 3.81))
                CenterArc((1.27, 0.635), 4.318, -90, 90)
                Line((-1.27, -3.683), (1.27, -3.683))
                CenterArc((-1.27, 0.635), 4.318, 180, 90)
                Line((-5.588, 3.81), (-5.588, 0.635))
                Line((-5.588, 3.81), (-5.715, 3.81))
            make_face()
        # OneSide extrude, distance=1.778
        extrude(amount=1.778, mode=Mode.ADD)
    return part.part


# Description: This is an Allen wrench (hex key) featuring a long cylindrical shaft with a blue hexagonal head at one end, used for tightening or loosening hexagonal socket screws and bolts.
def model_38740_c9ed5246_0000():
    """Model: Component8"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 2.3571208807, perimeter: 5.715
            with BuildLine():
                Line((0.47625, 0.8248891971), (0.9525, 0))
                Line((-0.47625, 0.8248891971), (0.47625, 0.8248891971))
                Line((-0.9525, 0), (-0.47625, 0.8248891971))
                Line((-0.47625, -0.8248891971), (-0.9525, 0))
                Line((0.47625, -0.8248891971), (-0.47625, -0.8248891971))
                Line((0.9525, 0), (0.47625, -0.8248891971))
            make_face()
        # OneSide extrude, distance=0.79502
        extrude(amount=0.79502)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 1.2667686977, perimeter: 3.9898226701
            Circle(0.635)
        # OneSide extrude, distance=7.62
        extrude(amount=7.62, mode=Mode.ADD)
    return part.part


# Description: This is a screw fastener (likely a cap screw or bolt) featuring a hexagonal head on one end and a cylindrical threaded shaft with a tapered tip on the other.
def model_38740_c9ed5246_0005():
    """Model: Component9"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 2.3571208807, perimeter: 5.715
            with BuildLine():
                Line((0.47625, 0.8248891971), (0.9525, 0))
                Line((-0.47625, 0.8248891971), (0.47625, 0.8248891971))
                Line((-0.9525, 0), (-0.47625, 0.8248891971))
                Line((-0.47625, -0.8248891971), (-0.9525, 0))
                Line((0.47625, -0.8248891971), (-0.47625, -0.8248891971))
                Line((0.9525, 0), (0.47625, -0.8248891971))
            make_face()
        # OneSide extrude, distance=0.635
        extrude(amount=0.635)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 1.2667686977, perimeter: 3.9898226701
            Circle(0.635)
        # OneSide extrude, distance=3.175
        extrude(amount=3.175, mode=Mode.ADD)
    return part.part


# Description: A spinning top toy with a cylindrical body, four flat sides, a pointed base, and a perpendicular stem or handle extending from the top for spinning.
def model_38924_16a41517_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> 押し出し1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 8 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((-5, -5)):
                Circle(0.5)
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch2 -> 押し出し2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            with Locations((5, 5)):
                Circle(0.1)
        # OneSide extrude, distance=0.7
        extrude(amount=0.7, mode=Mode.ADD)
    return part.part


# Description: This is a hexagonal prism or extruded hexagonal tube with a hollow interior channel running along its length, featuring slanted faces and a light blue top surface.
def model_39109_816b707e_0007():
    """Model: paluchy czesc 1 v8 (2)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0063, perimeter: 0.33
            with BuildLine():
                Line((-4.895, 3.94), (-5, 3.94))
                Line((-4.895, 4), (-4.895, 3.94))
                Line((-5, 4), (-4.895, 4))
                Line((-5, 3.94), (-5, 4))
            make_face()
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)
    return part.part


# Description: This is a bent or angled bracket or connector with two parallel rectangular flanges connected by a curved or angled cylindrical section, featuring multiple horizontal slots or ribs along the curved transition area.
def model_39109_816b707e_0009():
    """Model: paluchy czesc 2 v5 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 8 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.004, perimeter: 0.28
            with BuildLine():
                Line((-5.5, 3.5), (-5.4, 3.5))
                Line((-5.5, 3.46), (-5.5, 3.5))
                Line((-5.4, 3.46), (-5.5, 3.46))
                Line((-5.4, 3.5), (-5.4, 3.46))
            make_face()
            # Profile area: 0.0040000124, perimeter: 0.2800003862
            with BuildLine():
                Line((-5.28, 3.5), (-5.1799998842, 3.5))
                Line((-5.28, 3.4599999227), (-5.28, 3.5))
                Line((-5.1799998842, 3.4599999227), (-5.28, 3.4599999227))
                Line((-5.1799998842, 3.5), (-5.1799998842, 3.4599999227))
            make_face()
        # OneSide extrude, distance=0.25
        extrude(amount=0.25)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 5.5), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0012795597, perimeter: 0.1363647716
            with BuildLine():
                CenterArc((0.2399999946, 3.4799999222), 0.025, 126.8696005316, 106.2602047104)
                Line((0.2249998909, 3.46), (0.25, 3.46))
                Line((0.25, 3.46), (0.25, 3.5))
                Line((0.25, 3.5), (0.2250000983, 3.5))
            make_face()
            # Profile area: 0.0006839357, perimeter: 0.2007148825
            with BuildLine():
                Line((0.25, 3.5), (0.2250000983, 3.5))
                Line((0.25, 3.46), (0.25, 3.5))
                Line((0.2249998909, 3.46), (0.25, 3.46))
                CenterArc((0.2399999946, 3.4799999222), 0.025, -126.870194758, 253.7397952896)
            make_face()
        # OneSide extrude, distance=-0.33
        extrude(amount=-0.33, mode=Mode.ADD)

        # Sketch2 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 5.5), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0012795597, perimeter: 0.1363647716
            with BuildLine():
                CenterArc((0.2399999946, 3.4799999222), 0.025, 126.8696005316, 106.2602047104)
                Line((0.2249998909, 3.46), (0.25, 3.46))
                Line((0.25, 3.46), (0.25, 3.5))
                Line((0.25, 3.5), (0.2250000983, 3.5))
            make_face()
            # Profile area: 0.0006839357, perimeter: 0.2007148825
            with BuildLine():
                Line((0.25, 3.5), (0.2250000983, 3.5))
                Line((0.25, 3.46), (0.25, 3.5))
                Line((0.2249998909, 3.46), (0.25, 3.46))
                CenterArc((0.2399999946, 3.4799999222), 0.025, -126.870194758, 253.7397952896)
            make_face()
        # OneSide extrude, distance=0.01
        extrude(amount=0.01, mode=Mode.ADD)
    return part.part


# Description: This is a sheet metal bracket or mounting component with an angular, bent configuration featuring a main flat body with an attached perpendicular flange on the left side and a sloped top surface with internal ribbing or structural reinforcement.
def model_39109_816b707e_0010():
    """Model: czolo v8"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.3775000113, perimeter: 3.2161790325
            with BuildLine():
                Line((-1.8000000268, 1.5000000224), (-1.5500000231, 1.2500000186))
                Line((-1.5500000231, 1.2500000186), (-1.8000000268, 1.0000000149))
                Line((-1.8000000268, 1.0000000149), (-0.7000000104, 1.1000000164))
                Line((-0.7000000104, 1.1000000164), (-0.7000000104, 1.4000000209))
                Line((-0.7000000104, 1.4000000209), (-1.8000000268, 1.5000000224))
            make_face()
        # OneSide extrude, distance=0.4
        extrude(amount=0.4)

        # Sketch7 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.4, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0003, perimeter: 0.0921110235
            with BuildLine():
                Line((1.5299999658, -1.3999999687), (1.5499999654, -1.429999968))
                Line((1.519999966, -1.3999999687), (1.5299999658, -1.3999999687))
                Line((1.5399999656, -1.429999968), (1.519999966, -1.3999999687))
                Line((1.5499999654, -1.429999968), (1.5399999656, -1.429999968))
            make_face()
            # Profile area: 0.0003, perimeter: 0.0921110235
            with BuildLine():
                Line((1.5399999656, -1.0699999761), (1.519999966, -1.0999999754))
                Line((1.519999966, -1.0999999754), (1.5299999658, -1.0999999754))
                Line((1.5299999658, -1.0999999754), (1.5499999654, -1.0699999761))
                Line((1.5499999654, -1.0699999761), (1.5399999656, -1.0699999761))
            make_face()
        # OneSide extrude, distance=-0.1
        extrude(amount=-0.1, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a pentahedron or irregular polyhedron with a complex geometric shape featuring multiple triangular and quadrilateral faces in varying shades of blue and dark gray, displaying an asymmetrical structure with no apparent holes, slots, or flanges.
def model_39109_816b707e_0012():
    """Model: potylica v9"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0624999786, perimeter: 1.20710666
            with BuildLine():
                Line((-6, 3), (-6, 2.5))
                Line((-5.7500000857, 2.750000041), (-6, 2.5))
                Line((-6, 3), (-5.7500000857, 2.750000041))
            make_face()
        # OneSide extrude, distance=0.45
        extrude(amount=0.45)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(-6, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.225, perimeter: 1.9
            with BuildLine():
                Line((-3, 0.45), (-3, 0))
                Line((-3, 0), (-2.5, 0))
                Line((-2.5, 0), (-2.5, 0.45))
                Line((-2.5, 0.45), (-3, 0.45))
            make_face()
        # OneSide extrude, distance=0.6
        extrude(amount=0.6, mode=Mode.ADD)
    return part.part


# Description: This is a blind rivet nut (threaded insert) featuring a cylindrical body with a knurled or textured flange at the base and a hexagonal or ridged top opening designed for threaded fastening into sheet metal or composite materials.
def model_39306_ee445998_0003():
    """Model: Axle v4"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            Circle(0.5)
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.9817477042, perimeter: 7.853981634
            with BuildLine():
                CenterArc((0, 0), 0.75, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical bolt or fastener with a rounded head at one end and a threaded shaft, featuring a simple tubular body with minimal surface features.
def model_39306_ee445998_0004():
    """Model: Pin v6"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1256637099, perimeter: 1.2566370802
            Circle(0.200000003)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0706858315, perimeter: 0.942477775
            Circle(0.1499999966)
        # OneSide extrude, distance=1.5
        extrude(amount=1.5, mode=Mode.ADD)
    return part.part


# Description: This is an angled bracket or mounting arm featuring a curved cylindrical body transitioning to a rectangular flanged section, with internal ribbing/reinforcement details and a blue-highlighted surface indicating a key functional or mounting face.
def model_39389_d641313f_0005():
    """Model: Arm Head Suport"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 14 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 77.9283217062, perimeter: 47.9333209857
            with BuildLine():
                CenterArc((-6, 10), 1.25, 12.5640271897, 158.7599495194)
                Line((-8.7268901648, 0.4162151239), (-7.2356963734, 10.1885589369))
                CenterArc((-6, 0), 2.758471497, 171.3217166954, 148.5456000553)
                Line((-3.891, -1.7779644633), (-3.891, -1.778))
                CenterArc((-0.067, -5), 5.0004488799, 90.7677174972, 49.1153797441)
                CenterArc((-0.067, -5), 5.0004488799, 89.2322825028, 1.5354349944)
                Line((0, 0), (0, 6))
                CenterArc((0.167, 10.997), 4.9997897956, -169.9718845757, 78.0577690562)
                CenterArc((0.167, 10.997), 4.9997897956, -171.6613612402, 1.6894766645)
            make_face()
            with BuildLine():
                CenterArc((-6, 0), 0.8, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-6, 10), 0.8, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 5.9999598997, perimeter: 14.0000040098
            with BuildLine():
                Line((0, -6), (1, -6))
                Line((1, -6), (1, 0))
                Line((1, 0), (0.134, 0))
                CenterArc((0.067, 5), 5.0004488799, -90.7677174972, 1.5354349944)
                Line((0, 0), (0, -6))
            make_face()
        # OneSide extrude, distance=3.5
        extrude(amount=3.5, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical tube or pipe with a uniform circular cross-section, featuring slightly rounded or beveled edges at both ends and a subtle 3D perspective that emphasizes its elongated, hollow tubular form.
def model_39389_d641313f_0036():
    """Model: Hydraulic Body (2)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.3379421944, perimeter: 26.7035375555
            with BuildLine():
                CenterArc((0, 0), 2.25, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=23
        extrude(amount=23)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 12.5663706144, perimeter: 12.5663706144
            Circle(2)
        # OneSide extrude, distance=2
        extrude(amount=2, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical manifold block with a rounded rectangular (capsule) shape, featuring multiple internal passages and ports visible through the blue flow visualization, along with curved end caps and what appears to be mounting or connection points on the sides.
def model_39390_61cd2601_0010():
    """Model: Clamp Base Support (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.1865320638, perimeter: 2.9845130209
            with BuildLine():
                CenterArc((0, 0), 0.3, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.175, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.4064435496, perimeter: 3.6128315516
            with BuildLine():
                CenterArc((0, 0), 0.4, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.175, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.ADD)
    return part.part


# Description: This is a hexagonal box or container with an open top and internal geometric lattice structure, featuring a hollow interior with triangulated bracing framework visible through the transparent sections.
def model_39637_ca6a9a60_0009():
    """Model: Component2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.409570499, perimeter: 32.4450262021
            with BuildLine():
                Line((0, 2.2), (0, -2.2))
                Line((0, -2.2), (3, -2.2))
                Line((3, -2.2), (3, -2.1))
                Line((2, 0), (3, -2.1))
                Line((2, 0), (3, 2.1))
                Line((3, 2.2), (3, 2.1))
                Line((0, 2.2), (3, 2.2))
            make_face()
            with BuildLine():
                Line((0.1, 2.1), (2.8892409205, 2.1))
                Line((2.0082885395, 0.25), (2.8892409205, 2.1))
                Line((0.1, 0.25), (2.0082885395, 0.25))
                Line((0.1, 0.25), (0.1, 2.1))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((0.1, -0.25), (2.0082885395, -0.25))
                Line((2.0082885395, -0.25), (2.8892409205, -2.1))
                Line((0.1, -2.1), (2.8892409205, -2.1))
                Line((0.1, -0.25), (0.1, -2.1))
            make_face(mode=Mode.SUBTRACT)
        # TwoSides extrude (symmetric), distance=1.5
        extrude(amount=1.5, both=True)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.3452147505, perimeter: 8.5965724311
            with BuildLine():
                Line((0.1, 0.25), (0.1, 2.1))
                Line((0.1, 0.25), (2.0082885395, 0.25))
                Line((2.0082885395, 0.25), (2.8892409205, 2.1))
                Line((0.1, 2.1), (2.8892409205, 2.1))
            make_face()
            # Profile area: 4.3452147505, perimeter: 8.5965724311
            with BuildLine():
                Line((0.1, -0.25), (0.1, -2.1))
                Line((0.1, -2.1), (2.8892409205, -2.1))
                Line((2.0082885395, -0.25), (2.8892409205, -2.1))
                Line((0.1, -0.25), (2.0082885395, -0.25))
            make_face()
        # TwoSides extrude (symmetric), distance=0.5
        extrude(amount=0.5, both=True, mode=Mode.ADD)

        # Sketch2 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            Circle(0.4)
        # OneSide extrude, distance=-0.05
        extrude(amount=-0.05, mode=Mode.SUBTRACT)
    return part.part


# Description: A rectangular housing or duct component with a cylindrical bore running through its length and triangular/tapered end sections, featuring mesh or perforated side panels.
def model_39708_228f26be_0003():
    """Model: bearing3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 83.612736, perimeter: 36.576
            with BuildLine():
                Line((4.572, -4.572), (4.572, 4.572))
                Line((4.572, 4.572), (-4.572, 4.572))
                Line((-4.572, 4.572), (-4.572, -4.572))
                Line((-4.572, -4.572), (4.572, -4.572))
            make_face()
        # OneSide extrude, distance=18.288
        extrude(amount=18.288)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 18.288), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 36.9389752262, perimeter: 21.5450424183
            Circle(3.429)
        # OneSide extrude, distance=-28.6512
        extrude(amount=-28.6512, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical sleeve or bushing with a hollow center bore, featuring two circular holes positioned on opposite sides of its body and a slot or opening along the top edge.
def model_39708_228f26be_0005():
    """Model: steering column cap5"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 145.9317575872, perimeter: 95.7557452649
            with BuildLine():
                CenterArc((0, 0), 9.144000113, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 6.0960000753, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=12.192
        extrude(amount=12.192)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 29.1863515174, perimeter: 19.151149053
            with Locations((0, 6.0960000753)):
                Circle(3.0480000377)
        # TwoSides extrude (symmetric), distance=10.9728
        extrude(amount=10.9728, both=True, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a tapered hexagonal punch or drift pin with a long, slender shaft that gradually narrows from a larger hexagonal head to a pointed tip, featuring a dark metallic finish.
def model_39708_228f26be_0006():
    """Model: side rails 8"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(60.96, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1514.7474216554, perimeter: 353.3515718055
            with BuildLine():
                Line((85.3441602582, 12.192), (85.3556940813, 21.1194168082))
                Line((85.3556940813, 21.1194168082), (-82.2841660108, 21.3360000074))
                Line((-82.2841660108, 21.3360000074), (-82.2959796498, 12.192))
                Line((-82.2959796498, 12.192), (85.3441602582, 12.192))
            make_face()
        # OneSide extrude, distance=-6.096
        extrude(amount=-6.096)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 21.2296571108, -0.0274277672), x_dir=(-1, 0, 0), z_dir=(0, 0.9999991654, -0.0012919542))):
            # Profile area: 7.296587699, perimeter: 9.5755744081
            with Locations((-57.9120018482, -76.2000024319)):
                Circle(1.524)
            # Profile area: 7.296587699, perimeter: 9.5755744081
            with Locations((-57.9120018482, 0)):
                Circle(1.524)
            # Profile area: 7.296587699, perimeter: 9.5755744081
            with Locations((-57.9120018482, 73.1520023346)):
                Circle(1.524)
        # OneSide extrude, distance=-24.384
        extrude(amount=-24.384, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a blind rivet nut (threaded insert) with a cylindrical body, open top end with a serrated or knurled flange rim, and a closed bottom end designed for installation into sheet metal or composite materials.
def model_39708_228f26be_0009():
    """Model: spike 9 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 7.296587699, perimeter: 9.5755744081
            Circle(1.524)
        # OneSide extrude, distance=6.096
        extrude(amount=6.096)

        # Sketch4 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 3.2104988473, perimeter: 21.0662638399
            with BuildLine():
                CenterArc((0, 0), 1.8288000226, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.524, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 7.296587699, perimeter: 9.5755744081
            Circle(1.524)
        # OneSide extrude, distance=0.3048
        extrude(amount=0.3048, mode=Mode.ADD)
    return part.part


# Description: This is a sheet metal bracket or enclosure with a trapezoidal/wedge shape, featuring multiple bent flanges, a rectangular opening or slot on the bottom face, and angular surfaces that suggest it's designed for mounting or structural support applications.
def model_39792_60786b6c_0004():
    """Model: Handle_3 v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.6600342485, perimeter: 7.7447139427
            with BuildLine():
                Line((-1.4180331377, 0.45), (-1.5680331377, 0.023443557))
                Line((-1.4180331377, -0.4031128859), (-1.5680331377, 0.023443557))
                Line((1.55, -0.4031128859), (-1.4180331377, -0.4031128859))
                Line((1.55, -0.4031128859), (1.7, 0.023443557))
                Line((1.55, 0.45), (1.7, 0.023443557))
                Line((-1.4180331377, 0.45), (1.55, 0.45))
            make_face()
        # OneSide extrude, distance=1.7
        extrude(amount=1.7)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            Circle(0.15)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1, mode=Mode.ADD)
    return part.part


# Description: This is a curved air intake or duct component with a cylindrical base transitioning into an elongated, curved upper section featuring a mesh or perforated pattern with blue striping, designed to direct and filter airflow.
def model_39792_60786b6c_0005():
    """Model: Eccentric_Lever v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.7509273598, perimeter: 6.0451332804
            with BuildLine():
                CenterArc((0.6378389348, 1.2657724899), 1.1174710631, -117.0445086142, 0.6007792763)
                CenterArc((0, 0), 0.3000000045, 64.3748694422, 235.222901793)
                CenterArc((0.4110424125, 1.6691002135), 1.9477743335, -97.7562585945, 45.4739369172)
                CenterArc((1.5000000224, 0.3000000045), 0.200000003, -59.124615832, 216.4073934876)
                CenterArc((0.6378389348, 1.2657724899), 1.1174710631, -116.4437293379, 63.7761041688)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.200000003, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.1256637099, perimeter: 1.2566370802
            Circle(0.200000003)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.1256637099, perimeter: 1.2566370802
            Circle(0.200000003)
        # OneSide extrude, distance=0.4
        extrude(amount=0.4, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical cap or bucket-shaped container with a curved, flared top rim that widens outward and a tapered cylindrical body, featuring a mesh or wireframe rendering that highlights its hollow interior structure.
def model_39792_60786b6c_0006():
    """Model: Line Roller v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            Circle(0.3)
        # OneSide extrude, distance=0.4
        extrude(amount=0.4)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.4, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.3534291735, perimeter: 4.7123889804
            with BuildLine():
                CenterArc((0, 0), 0.45, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            Circle(0.3)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)
    return part.part


# Description: This is a hexagonal or polyhedron-shaped block with a complex geometric form featuring multiple flat faces, angular edges, and internal geometric subdivisions visible through transparent faceting.
def model_39793_5193d5ab_0010():
    """Model: Window v6"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 69.3547, perimeter: 33.9725
            with BuildLine():
                Line((0, 6.82625), (0, 0))
                Line((0, 0), (10.16, 0))
                Line((10.16, 0), (10.16, 6.82625))
                Line((10.16, 6.82625), (0, 6.82625))
            make_face()
        # OneSide extrude, distance=7.3025
        extrude(amount=7.3025)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 62.09665, perimeter: 31.75
            with BuildLine():
                Line((10.00125, 0.15875), (1.11125, 0.15875))
                Line((10.00125, 7.14375), (10.00125, 0.15875))
                Line((1.11125, 7.14375), (10.00125, 7.14375))
                Line((1.11125, 0.15875), (1.11125, 7.14375))
            make_face()
        # OneSide extrude, distance=-6.19125
        extrude(amount=-6.19125, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical disk or pulley with a flat circular face and a textured or knurled curved edge band around its perimeter, featuring a smooth, dark finished surface.
def model_39793_5193d5ab_0012():
    """Model: Top Headlight v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.9793260902, perimeter: 4.9872783376
            Circle(0.79375)
        # OneSide extrude, distance=0.0635
        extrude(amount=0.0635)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.0635), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1.4844945677, perimeter: 7.4809175064
            with BuildLine():
                CenterArc((0, 0), 0.79375, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.396875, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.4948315226, perimeter: 2.4936391688
            Circle(0.396875)
        # OneSide extrude, distance=0.3175
        extrude(amount=0.3175, mode=Mode.ADD)
    return part.part


# Description: This is a torus-shaped coupling or connector featuring a cylindrical shaft passing through its center, with textured or ribbed surfaces on the inner and outer edges, designed to join or couple two components together.
def model_39793_5193d5ab_0015():
    """Model: Steering Wheel v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0791730436, perimeter: 0.9974556675
            Circle(0.15875)
        # OneSide extrude, distance=0.9525
        extrude(amount=0.9525)

        # Sketch2 -> Extrude2 (NewBody)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.9525), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.2177258699, perimeter: 5.4860061713
            with BuildLine():
                CenterArc((0, 0), 0.47625, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.396875, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.15875
        extrude(amount=-0.15875)
    return part.part


# Description: This is a flat, parallelogram-shaped plate or base component with a central rectangular slot or cutout running lengthwise through its body, featuring beveled or angled edges along its perimeter.
def model_39795_7d4d7d57_0005():
    """Model: Top base"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 6 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 17.78, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 138.1045576719, perimeter: 52.7049991941
            with BuildLine():
                Line((-14.2874997902, -1.2700000405), (-0.9524999809, -1.2700000405))
                Line((-14.2874997902, -11.7474998283), (-14.2874997902, -1.2700000405))
                Line((-0.9524999809, -11.7474998283), (-14.2874997902, -11.7474998283))
                Line((-0.9524999809, -1.2700000405), (-0.9524999809, -11.7474998283))
            make_face()
            with BuildLine():
                Line((-2.5399999809, -11.4299998283), (-1.2699999809, -11.4299998283))
                Line((-2.5399999809, -10.1599998283), (-2.5399999809, -11.4299998283))
                Line((-1.2699999809, -10.1599998283), (-2.5399999809, -10.1599998283))
                Line((-1.2699999809, -11.4299998283), (-1.2699999809, -10.1599998283))
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 1.6129, perimeter: 5.08
            with BuildLine():
                Line((-1.2699999809, -11.4299998283), (-1.2699999809, -10.1599998283))
                Line((-1.2699999809, -10.1599998283), (-2.5399999809, -10.1599998283))
                Line((-2.5399999809, -10.1599998283), (-2.5399999809, -11.4299998283))
                Line((-2.5399999809, -11.4299998283), (-1.2699999809, -11.4299998283))
            make_face()
        # OneSide extrude, distance=1.27
        extrude(amount=1.27)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 19.05, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 9.6774003088, perimeter: 13.9700003242
            with BuildLine():
                Line((-10.1600003242, -4.4450000405), (-5.0800001621, -4.4450000405))
                Line((-10.1600003242, -6.3500000405), (-10.1600003242, -4.4450000405))
                Line((-5.0800001621, -6.3500000405), (-10.1600003242, -6.3500000405))
                Line((-5.0800001621, -4.4450000405), (-5.0800001621, -6.3500000405))
            make_face()
        # OneSide extrude, distance=-4.064
        extrude(amount=-4.064, mode=Mode.SUBTRACT)
    return part.part


# Description: This is an elongated oval or boat-shaped enclosure with a curved top surface featuring internal ribbing or structural reinforcements, a flat bottom base, and tapered ends.
def model_39819_c4b9cef8_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 706.8583470577, perimeter: 94.2477796077
            Circle(15)
        # OneSide extrude, distance=5
        extrude(amount=5)
    return part.part


# Description: This is a hexagonal prism or elongated hexagonal tube with a hollow interior channel running lengthwise through its center, featuring a beveled or chamfered edge on the top surface.
def model_39932_7b9150e8_0002():
    """Model: Drawer"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 80.8264721673, perimeter: 538.8168535198
            with BuildLine():
                Line((-30.48, -46.292121234), (-73.2, -46.292121234))
                Line((-30.48, 46.292121426), (-30.48, -46.292121234))
                Line((-73.2, 46.292121426), (-30.48, 46.292121426))
                Line((-73.2, -46.292121234), (-73.2, 46.292121426))
            make_face()
            with BuildLine():
                Line((-30.78001464, -45.992106594), (-72.89998536, -45.992106594))
                Line((-72.89998536, -45.992106594), (-72.89998536, 45.992106786))
                Line((-72.89998536, 45.992106786), (-30.78001464, 45.992106786))
                Line((-30.78001464, 45.992106786), (-30.78001464, -45.992106594))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=22.86
        extrude(amount=22.86)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3874.3723742652, perimeter: 268.2083681999
            with BuildLine():
                Line((-30.78001464, 45.992106786), (-30.78001464, -45.992106594))
                Line((-72.89998536, 45.992106786), (-30.78001464, 45.992106786))
                Line((-72.89998536, -45.992106594), (-72.89998536, 45.992106786))
                Line((-30.78001464, -45.992106594), (-72.89998536, -45.992106594))
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)
    return part.part


# Description: This is a pry bar (or crowbar) consisting of a long, straight cylindrical metal shaft with a flat, angled wedge-shaped head at one end for leveraging and prying applications.
def model_40052_42bdc982_0006():
    """Model: GearBeam"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 7.0685834706, perimeter: 9.4247779608
            Circle(1.5)
        # OneSide extrude, distance=50
        extrude(amount=50)

        # Sketch3 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 50, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 56.9314165294, perimeter: 41.4247779608
            with BuildLine():
                Line((-4, 4), (-4, -4))
                Line((-4, -4), (4, -4))
                Line((4, -4), (4, 4))
                Line((4, 4), (-4, 4))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 7.0685834706, perimeter: 9.4247779608
            Circle(1.5)
        # OneSide extrude, distance=1.2
        extrude(amount=1.2, mode=Mode.ADD)
    return part.part


# Description: This is a tapered cylindrical duct or sleeve component with a hexagonal top opening, featuring a curved, cone-like shape that narrows toward the bottom with ribbed or reinforcement patterns along its surface.
def model_40052_42bdc982_0021():
    """Model: Break"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 10 constraints, 9 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 185.4317371309, perimeter: 74.1885066846
            with BuildLine():
                Line((-2.5, -14.5), (-2.5, 2.5))
                Line((-2.5, -14.5), (-2.5549853157, -14.8118372215))
                CenterArc((6.3082844614, -16.3746708205), 9, 170, 90.6410923504)
                CenterArc((39, -20.390018814), 34.5, 154.5832163376, 33.5230925672)
                Line((2.5, -2.5), (7.8392685907, -5.5826281581))
                Line((2.5, 2.5), (2.5, -2.5))
                Line((2.5, 2.5), (-2.5, 2.5))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=2.4
        extrude(amount=2.4, both=True)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(2.4, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))) as sk:
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            Circle(1)
        # TwoSides extrude, along=-13.5, against=2
        extrude(amount=-13.5, mode=Mode.ADD)
        extrude(sk.sketch, amount=2, mode=Mode.ADD)
    return part.part


# Description: This is a solar panel mounting bracket with a rectangular base platform featuring triangular support struts, angled mounting rails, and a vertical post for securing and tilting photovoltaic panels.
def model_40061_d07e8764_0003():
    """Model: Base"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 38 constraints, 16 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1143.5397259067, perimeter: 163.3628179867
            with BuildLine():
                CenterArc((0, 0), 20, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 6, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=14
        extrude(amount=14)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 38 constraints, 16 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 7695.4536505968, perimeter: 559.0707812546
            with BuildLine():
                Line((-50, 45), (50, 45))
                Line((-50, -45), (-50, 45))
                Line((50, -45), (-50, -45))
                Line((50, 45), (50, -45))
            make_face()
            with BuildLine():
                CenterArc((35, -35), 1.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-35, -35), 1.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-35, 35), 1.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((35, 35), 1.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((43.28, 0), 2.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0, 0), 20, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 7.0685834706, perimeter: 9.4247779608
            with Locations((35, -35)):
                Circle(1.5)
            # Profile area: 7.0685834706, perimeter: 9.4247779608
            with Locations((-35, -35)):
                Circle(1.5)
            # Profile area: 7.0685834706, perimeter: 9.4247779608
            with Locations((-35, 35)):
                Circle(1.5)
            # Profile area: 7.0685834706, perimeter: 9.4247779608
            with Locations((35, 35)):
                Circle(1.5)
            # Profile area: 12.5663706144, perimeter: 25.1327412287
            with BuildLine():
                CenterArc((43.28, 0), 2.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((43.28, 0), 1.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 5.5815778498, perimeter: 13.9340216976
            with BuildLine():
                CenterArc((43.28, 0), 1.5, 0, 360)
            make_face()
            with BuildLine():
                Line((42.73, -0.5099019514), (42.73, 0.5099019514))
                CenterArc((43.28, 0), 0.75, 42.8334280661, 94.3331438679)
                Line((43.83, 0.5099019514), (43.83, -0.5099019514))
                CenterArc((43.28, 0), 0.75, -137.1665719339, 94.3331438679)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 1.4870056208, perimeter: 4.5092437368
            with BuildLine():
                CenterArc((43.28, 0), 0.75, -137.1665719339, 94.3331438679)
                Line((43.83, 0.5099019514), (43.83, -0.5099019514))
                CenterArc((43.28, 0), 0.75, 42.8334280661, 94.3331438679)
                Line((42.73, -0.5099019514), (42.73, 0.5099019514))
            make_face()
            # Profile area: 1143.5397259067, perimeter: 163.3628179867
            with BuildLine():
                CenterArc((0, 0), 20, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 6, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 113.0973355292, perimeter: 37.6991118431
            Circle(6)
        # OneSide extrude, distance=-7
        extrude(amount=-7, mode=Mode.ADD)

        # Sketch1 -> Extrude3 (Join)
        # Sketch on XZ construction plane
        # Sketch has 38 constraints, 16 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 12.5663706144, perimeter: 25.1327412287
            with BuildLine():
                CenterArc((43.28, 0), 2.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((43.28, 0), 1.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=12
        extrude(amount=12, mode=Mode.ADD)

        # Sketch1 -> Extrude4 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 38 constraints, 16 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 7.0685834706, perimeter: 9.4247779608
            with Locations((-35, 35)):
                Circle(1.5)
            # Profile area: 7.0685834706, perimeter: 9.4247779608
            with Locations((35, 35)):
                Circle(1.5)
            # Profile area: 7.0685834706, perimeter: 9.4247779608
            with Locations((35, -35)):
                Circle(1.5)
            # Profile area: 7.0685834706, perimeter: 9.4247779608
            with Locations((-35, -35)):
                Circle(1.5)
        # OneSide extrude, distance=-7
        extrude(amount=-7, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a circular disc with a central rectangular slot, featuring a textured or knurled edge around its circumference, commonly used as a pulley, gear, or mechanical component.
def model_40061_d07e8764_0004():
    """Model: Gear_3"""
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
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 4833.5764483563, perimeter: 316.898208614
            with BuildLine():
                CenterArc((0, 0), 40.25, -0.3480696452, 0.6961392905)
                CenterArc((0, 0), 40.25, 0.3480696452, 359.3038607095)
            make_face()
            with BuildLine():
                Line((8, 8), (-8, 8))
                Line((8, -8), (8, 8))
                Line((-8, -8), (8, -8))
                Line((-8, 8), (-8, -8))
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 256, perimeter: 64
            with BuildLine():
                Line((-8, 8), (-8, -8))
                Line((-8, -8), (8, -8))
                Line((8, -8), (8, 8))
                Line((8, 8), (-8, 8))
            make_face()
        # OneSide extrude, distance=5
        extrude(amount=5)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.1487569303, perimeter: 1.6131469447
            with BuildLine():
                _nurbs_edge([(40.249257286, -0.2445156898), (40.3016150895, -0.2268724917), (40.4524457775, -0.1748973717), (40.6020935494, -0.1196080118), (40.6999146301, -0.0834667123)], [1, 1, 1, 1, 1], [2.2553031059, 2.2553031059, 2.2553031059, 2.2553031059, 2.4210486798, 2.7338876972, 2.7338876972, 2.7338876972, 2.7338876972], 3)
                CenterArc((-0.1030164174, 0), 40.8030164174, -0.1172044153, 0.2344088306)
                _nurbs_edge([(40.249257286, 0.2445156898), (40.3016150895, 0.2268724917), (40.4524457775, 0.1748973717), (40.6020935494, 0.1196080118), (40.6999146301, 0.0834667123)], [1, 1, 1, 1, 1], [2.2553031059, 2.2553031059, 2.2553031059, 2.2553031059, 2.4210486798, 2.7338876972, 2.7338876972, 2.7338876972, 2.7338876972], 3)
                CenterArc((0, 0), 40.25, -0.3480696452, 0.6961392905)
            make_face()
        # OneSide extrude, distance=5
        extrude(amount=5, mode=Mode.ADD)

        # Sketch1 -> Extrude3 (Cut)
        # Sketch on XY construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 256, perimeter: 64
            with BuildLine():
                Line((-8, 8), (-8, -8))
                Line((-8, -8), (8, -8))
                Line((8, -8), (8, 8))
                Line((8, 8), (-8, 8))
            make_face()
        # OneSide extrude, distance=5
        extrude(amount=5, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical electric motor or actuator housing with a rounded dome-shaped top, a central axial hole through its length, and internal cooling fins or ribbed surfaces visible through the mesh rendering.
def model_40061_d07e8764_0019():
    """Model: Gear_4"""
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
        # Sketch has 13 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 17.3704042824, perimeter: 19.9030477394
            with BuildLine():
                CenterArc((0, 0), 2.45, 4.1761540728, 351.6476918544)
                CenterArc((0, 0), 2.45, -4.1761540728, 8.3523081456)
            make_face()
            with BuildLine():
                Line((0.55, 0.5099019514), (0.55, -0.5099019514))
                CenterArc((0, 0), 0.75, -137.1665719339, 94.3331438679)
                Line((-0.55, -0.5099019514), (-0.55, 0.5099019514))
                CenterArc((0, 0), 0.75, 42.8334280661, 94.3331438679)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 1.4870056208, perimeter: 4.5092437368
            with BuildLine():
                CenterArc((0, 0), 0.75, 42.8334280661, 94.3331438679)
                Line((-0.55, -0.5099019514), (-0.55, 0.5099019514))
                CenterArc((0, 0), 0.75, -137.1665719339, 94.3331438679)
                Line((0.55, 0.5099019514), (0.55, -0.5099019514))
            make_face()
        # OneSide extrude, distance=5
        extrude(amount=5)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        # Sketch has 13 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.1360641504, perimeter: 1.4543300688
            with BuildLine():
                Line((2.443494936, 0.1784166404), (2.5303976008, 0.1847620113))
                CenterArc((0, 0), 2.45, -4.1761540728, 8.3523081456)
                Line((2.443494936, -0.1784166404), (2.5303976008, -0.1847620113))
                _nurbs_edge([(2.5303976008, -0.1847620113), (2.5439412821, -0.1844456542), (2.5712495475, -0.1838077801), (2.6120691758, -0.1772522639), (2.6530556489, -0.1685608637), (2.6941265145, -0.157404667), (2.7352408746, -0.1442082723), (2.7763622979, -0.1290769261), (2.8174393346, -0.1121028541), (2.8584982784, -0.0934795598), (2.8854949425, -0.0798066986), (2.899087462, -0.0729225653)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0405977583, 0.0818576824, 0.1237561845, 0.1662906776, 0.2094601392, 0.2532639854, 0.2977018121, 0.3427733073, 0.3884782139, 0.3884782139, 0.3884782139, 0.3884782139], 3)
                CenterArc((-0.0141435345, 0), 2.9141435345, -1.4339003369, 2.8678006738)
                _nurbs_edge([(2.5303976008, 0.1847620113), (2.5439412821, 0.1844456542), (2.5712495475, 0.1838077801), (2.6120691758, 0.1772522639), (2.6530556489, 0.1685608637), (2.6941265145, 0.157404667), (2.7352408746, 0.1442082723), (2.7763622979, 0.1290769261), (2.8174393346, 0.1121028541), (2.8584982784, 0.0934795598), (2.8854949425, 0.0798066986), (2.899087462, 0.0729225653)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0405977583, 0.0818576824, 0.1237561845, 0.1662906776, 0.2094601392, 0.2532639854, 0.2977018121, 0.3427733073, 0.3884782139, 0.3884782139, 0.3884782139, 0.3884782139], 3)
            make_face()
        # OneSide extrude, distance=5
        extrude(amount=5, mode=Mode.ADD)

        # Sketch1 -> Extrude3 (Cut)
        # Sketch on XY construction plane
        # Sketch has 13 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.4870056208, perimeter: 4.5092437368
            with BuildLine():
                CenterArc((0, 0), 0.75, 42.8334280661, 94.3331438679)
                Line((-0.55, -0.5099019514), (-0.55, 0.5099019514))
                CenterArc((0, 0), 0.75, -137.1665719339, 94.3331438679)
                Line((0.55, 0.5099019514), (0.55, -0.5099019514))
            make_face()
        # OneSide extrude, distance=5
        extrude(amount=5, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a torus-shaped (donut-like) pulley or wheel with a central axial hole and multiple radial cutouts or slots around its circumference for lightweighting and ventilation.
def model_40061_d07e8764_0020():
    """Model: Gear_1"""
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
        # Sketch has 13 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 38.1138816044, perimeter: 30.7496220414
            with BuildLine():
                CenterArc((0, 0), 3.6785714286, -2.4220320426, 4.8440640852)
                CenterArc((0, 0), 3.6785714286, 2.4220320426, 355.1559359148)
            make_face()
            with BuildLine():
                Line((1, 0.75), (1, -0.75))
                CenterArc((0, 0), 1.25, -143.1301023542, 106.2602047083)
                Line((-1, -0.75), (-1, 0.75))
                CenterArc((0, 0), 1.25, 36.8698976458, 106.2602047083)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 4.3977975563, perimeter: 7.63647609
            with BuildLine():
                CenterArc((0, 0), 1.25, 36.8698976458, 106.2602047083)
                Line((-1, -0.75), (-1, 0.75))
                CenterArc((0, 0), 1.25, -143.1301023542, 106.2602047083)
                Line((1, 0.75), (1, -0.75))
            make_face()
        # OneSide extrude, distance=3
        extrude(amount=3)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        # Sketch has 13 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0732243673, perimeter: 1.1033870158
            with BuildLine():
                _nurbs_edge([(3.6752851905, -0.1554558584), (3.6851875041, -0.1541939359), (3.7091934719, -0.1503181764), (3.7472015655, -0.1427701424), (3.7893286401, -0.1322974663), (3.8314751316, -0.1200924497), (3.8736208931, -0.106257311), (3.9157349107, -0.090880525), (3.9578436891, -0.0741366241), (3.9856406093, -0.061913884), (3.9996120589, -0.0557704193)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0.0544141688, 0.0544141688, 0.0544141688, 0.0544141688, 0.0843621313, 0.127273794, 0.1706650799, 0.2145354051, 0.2588844823, 0.3037121388, 0.3490182571, 0.3948027492, 0.3948027492, 0.3948027492, 0.3948027492], 3)
                CenterArc((-0.0089716937, 0), 4.0089716937, -0.7970903682, 1.5941807363)
                _nurbs_edge([(3.6752851905, 0.1554558584), (3.6851875041, 0.1541939359), (3.7091934719, 0.1503181764), (3.7472015655, 0.1427701424), (3.7893286401, 0.1322974663), (3.8314751316, 0.1200924497), (3.8736208931, 0.106257311), (3.9157349107, 0.090880525), (3.9578436891, 0.0741366241), (3.9856406093, 0.061913884), (3.9996120589, 0.0557704193)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0.0544141688, 0.0544141688, 0.0544141688, 0.0544141688, 0.0843621313, 0.127273794, 0.1706650799, 0.2145354051, 0.2588844823, 0.3037121388, 0.3490182571, 0.3948027492, 0.3948027492, 0.3948027492, 0.3948027492], 3)
                CenterArc((0, 0), 3.6785714286, -2.4220320426, 4.8440640852)
            make_face()
        # OneSide extrude, distance=3
        extrude(amount=3, mode=Mode.ADD)

        # Sketch1 -> Extrude3 (Cut)
        # Sketch on XY construction plane
        # Sketch has 13 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 4.3977975563, perimeter: 7.63647609
            with BuildLine():
                CenterArc((0, 0), 1.25, 36.8698976458, 106.2602047083)
                Line((-1, -0.75), (-1, 0.75))
                CenterArc((0, 0), 1.25, -143.1301023542, 106.2602047083)
                Line((1, 0.75), (1, -0.75))
            make_face()
        # OneSide extrude, distance=3
        extrude(amount=3, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical sleeve or spacer with two opposing rectangular slots or windows cut through its walls and a small protruding tab or key feature on one end.
def model_40061_d07e8764_0021():
    """Model: Gear_2"""
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
        # Sketch has 13 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 2.36384966, perimeter: 11.4656274698
            with BuildLine():
                CenterArc((0, 0), 1.1071428571, 5.8236408384, 348.3527183231)
                CenterArc((0, 0), 1.1071428571, -5.8236408384, 11.6472816769)
            make_face()
            with BuildLine():
                Line((-0.55, 0.5099019514), (-0.55, -0.5099019514))
                CenterArc((0, 0), 0.75, 42.8334280661, 94.3331438679)
                Line((0.55, -0.5099019514), (0.55, 0.5099019514))
                CenterArc((0, 0), 0.75, -137.1665719339, 94.3331438679)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 1.4870056208, perimeter: 4.5092437368
            with BuildLine():
                CenterArc((0, 0), 0.75, -137.1665719339, 94.3331438679)
                Line((0.55, -0.5099019514), (0.55, 0.5099019514))
                CenterArc((0, 0), 0.75, 42.8334280661, 94.3331438679)
                Line((-0.55, 0.5099019514), (-0.55, -0.5099019514))
            make_face()
        # OneSide extrude, distance=3
        extrude(amount=3)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        # Sketch has 13 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0678802242, perimeter: 1.0325949813
            with BuildLine():
                Line((1.1014288123, 0.1123382282), (1.201875706, 0.1225831264))
                CenterArc((0, 0), 1.1071428571, -5.8236408384, 11.6472816769)
                Line((1.1014288123, -0.1123382282), (1.201875706, -0.1225831264))
                _nurbs_edge([(1.201875706, -0.1225831264), (1.2028936304, -0.1226152602), (1.2049301556, -0.1226660704), (1.2079869725, -0.1227019129), (1.2120667898, -0.1226688939), (1.217173313, -0.1224932152), (1.2222865026, -0.1221846394), (1.2274061629, -0.1217466419), (1.232531945, -0.1211855585), (1.237663303, -0.1205110728), (1.2427994647, -0.1197345197), (1.2479393901, -0.118867413), (1.2530817532, -0.1179199974), (1.2582248657, -0.1168995428), (1.2633667731, -0.115809549), (1.2685057229, -0.1146511594), (1.2736406026, -0.1134241774), (1.2787713027, -0.1121281499), (1.2838993286, -0.1107636364), (1.289027554, -0.1093326401), (1.2941588237, -0.1078378073), (1.2992947227, -0.1062819001), (1.3044345215, -0.1046672327), (1.3095734386, -0.102994954), (1.314703541, -0.1012650726), (1.3198170574, -0.099477207), (1.3249092968, -0.0976311822), (1.3299811516, -0.09572759), (1.3350432415, -0.0937686226), (1.340113126, -0.0917576961), (1.3452077565, -0.0896982273), (1.350336746, -0.0875925732), (1.3554965616, -0.0854410986), (1.3606610945, -0.0832406976), (1.3657886505, -0.0809858239), (1.3708384761, -0.0786709828), (1.375785204, -0.0762929024), (1.3806323633, -0.0738525699), (1.3854309806, -0.0713580317), (1.3902736176, -0.0688235108), (1.3952750115, -0.0662665165), (1.4005563511, -0.0637055016), (1.4062293946, -0.0611574947), (1.412377331, -0.058635252), (1.4190530868, -0.0561469942), (1.4262876797, -0.0536976301), (1.4325338234, -0.0517711322), (1.4374780669, -0.0503451433), (1.4408895264, -0.0494028699), (1.4426240807, -0.0489338297)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0222222222, 0.0444444444, 0.0666666667, 0.0888888889, 0.1111111111, 0.1333333333, 0.1555555556, 0.1777777778, 0.2, 0.2222222222, 0.2444444444, 0.2666666667, 0.2888888889, 0.3111111111, 0.3333333333, 0.3555555556, 0.3777777778, 0.4, 0.4222222222, 0.4444444444, 0.4666666667, 0.4888888889, 0.5111111111, 0.5333333333, 0.5555555556, 0.5777777778, 0.6, 0.6222222222, 0.6444444444, 0.6666666667, 0.6888888889, 0.7111111111, 0.7333333333, 0.7555555556, 0.7777777778, 0.8, 0.8222222222, 0.8444444444, 0.8666666667, 0.8888888889, 0.9111111111, 0.9333333333, 0.9555555556, 0.9777777778, 1, 1, 1, 1, 1, 1], 5)
                CenterArc((0, 0), 1.4434537602, -1.9427288205, 3.8854576409)
                _nurbs_edge([(1.201875706, 0.1225831264), (1.2028936304, 0.1226152602), (1.2049301556, 0.1226660704), (1.2079869725, 0.1227019129), (1.2120667898, 0.1226688939), (1.217173313, 0.1224932152), (1.2222865026, 0.1221846394), (1.2274061629, 0.1217466419), (1.232531945, 0.1211855585), (1.237663303, 0.1205110728), (1.2427994647, 0.1197345197), (1.2479393901, 0.118867413), (1.2530817532, 0.1179199974), (1.2582248657, 0.1168995428), (1.2633667731, 0.115809549), (1.2685057229, 0.1146511594), (1.2736406026, 0.1134241774), (1.2787713027, 0.1121281499), (1.2838993286, 0.1107636364), (1.289027554, 0.1093326401), (1.2941588237, 0.1078378073), (1.2992947227, 0.1062819001), (1.3044345215, 0.1046672327), (1.3095734386, 0.102994954), (1.314703541, 0.1012650726), (1.3198170574, 0.099477207), (1.3249092968, 0.0976311822), (1.3299811516, 0.09572759), (1.3350432415, 0.0937686226), (1.340113126, 0.0917576961), (1.3452077565, 0.0896982273), (1.350336746, 0.0875925732), (1.3554965616, 0.0854410986), (1.3606610945, 0.0832406976), (1.3657886505, 0.0809858239), (1.3708384761, 0.0786709828), (1.375785204, 0.0762929024), (1.3806323633, 0.0738525699), (1.3854309806, 0.0713580317), (1.3902736176, 0.0688235108), (1.3952750115, 0.0662665165), (1.4005563511, 0.0637055016), (1.4062293946, 0.0611574947), (1.412377331, 0.058635252), (1.4190530868, 0.0561469942), (1.4262876797, 0.0536976301), (1.4325338234, 0.0517711322), (1.4374780669, 0.0503451433), (1.4408895264, 0.0494028699), (1.4426240807, 0.0489338297)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0222222222, 0.0444444444, 0.0666666667, 0.0888888889, 0.1111111111, 0.1333333333, 0.1555555556, 0.1777777778, 0.2, 0.2222222222, 0.2444444444, 0.2666666667, 0.2888888889, 0.3111111111, 0.3333333333, 0.3555555556, 0.3777777778, 0.4, 0.4222222222, 0.4444444444, 0.4666666667, 0.4888888889, 0.5111111111, 0.5333333333, 0.5555555556, 0.5777777778, 0.6, 0.6222222222, 0.6444444444, 0.6666666667, 0.6888888889, 0.7111111111, 0.7333333333, 0.7555555556, 0.7777777778, 0.8, 0.8222222222, 0.8444444444, 0.8666666667, 0.8888888889, 0.9111111111, 0.9333333333, 0.9555555556, 0.9777777778, 1, 1, 1, 1, 1, 1], 5)
            make_face()
        # OneSide extrude, distance=3
        extrude(amount=3, mode=Mode.ADD)

        # Sketch1 -> Extrude3 (Cut)
        # Sketch on XY construction plane
        # Sketch has 13 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.4870056208, perimeter: 4.5092437368
            with BuildLine():
                CenterArc((0, 0), 0.75, -137.1665719339, 94.3331438679)
                Line((0.55, -0.5099019514), (0.55, 0.5099019514))
                CenterArc((0, 0), 0.75, 42.8334280661, 94.3331438679)
                Line((-0.55, 0.5099019514), (-0.55, -0.5099019514))
            make_face()
        # OneSide extrude, distance=3
        extrude(amount=3, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a stepped rectangular block or bracket with two distinct levels of decreasing height, featuring a sloped top surface on the upper step and internal geometric subdivisions visible through the mesh structure.
def model_40070_be9c502b_0019():
    """Model: KRZESLO v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2, perimeter: 6
            with BuildLine():
                Line((0.5, -1.5), (-0.5, -1.5))
                Line((0.5, 0.5), (0.5, -1.5))
                Line((-0.5, 0.5), (0.5, 0.5))
                Line((-0.5, -1.5), (-0.5, 0.5))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1, perimeter: 4
            with BuildLine():
                Line((0.5, 0.5), (-0.5, 0.5))
                Line((0.5, 0.5), (0.5, 1.5))
                Line((0.5, 1.5), (-0.5, 1.5))
                Line((-0.5, 1.5), (-0.5, 0.5))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)
    return part.part


# Description: This is a curved aerodynamic cover or fairing with a elongated, boat-like shape featuring a concave upper surface, dark reinforced edges/flanges along the perimeter, and a streamlined profile designed to reduce drag or provide protective covering.
def model_40070_be9c502b_0023():
    """Model: skrzydlo tylne v5"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 11 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 153.2766394981, perimeter: 61.8399447793
            with BuildLine():
                Line((13.5, 0), (-13.5, 0))
                Line((-13.5, 0), (-13.5, -2.4514391999))
                CenterArc((-11.5, -2.4514391999), 2, 180, 75.4998332334)
                Line((-12.0007656439, -4.3877330231), (-1.9, -7))
                Line((1.9, -7), (-1.9, -7))
                Line((12.0007656439, -4.3877330231), (1.9, -7))
                CenterArc((11.5, -2.4514391999), 2, -75.4998332334, 75.4998332334)
                Line((13.5, 0), (13.5, -2.4514391999))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


# Description: This is a curved duct or airflow component with an organic, teardrop-like shape featuring a smooth, ribbed or textured surface texture, likely designed for aerodynamic flow distribution or acoustic dampening.
def model_40070_be9c502b_0062():
    """Model: SZYBA v6 (7)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 18 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.1798811938, perimeter: 1.9510308565
            with BuildLine():
                Line((1.4730919717, 1.2000000179), (1.061288528, 1.2000000179))
                CenterArc((0, 0), 1.6019779594, 25.9100663643, 22.6001610113)
                Line((1.4409487735, 0.7000000104), (1.7663521691, 0.7000000104))
                CenterArc((0, 0), 1.9, 21.6182727605, 17.5484386511)
            make_face()
            # Profile area: 0.1181368882, perimeter: 1.5262279933
            with BuildLine():
                Line((1.4409487735, 0.7000000104), (1.7663521691, 0.7000000104))
                CenterArc((0, 0), 1.6019779594, 7.1718431959, 18.7382231684)
                Line((1.7663521691, 0.200000003), (1.5894443625, 0.200000003))
                Line((1.7663521691, 0.7000000104), (1.7663521691, 0.200000003))
            make_face()
            # Profile area: 0.0367947095, perimeter: 1.1396100722
            with BuildLine():
                CenterArc((0, 0), 1.9, 6.0423285094, 15.5759442511)
                Line((1.7663521691, 0.7000000104), (1.7663521691, 0.200000003))
                Line((1.8894443625, 0.200000003), (1.7663521691, 0.200000003))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on YZ construction plane
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 8.0485071504, perimeter: 14.8791716741
            with BuildLine():
                Line((-0.4999999962, 1.7106962251), (0.8000000119, 1.6000000238))
                Line((-0.5, 1.2000000179), (-0.4999999962, 1.7106962251))
                CenterArc((-0.5000000037, 0.7000000104), 0.5000000037, -90.0000004269, 180)
                CenterArc((-0.5000000037, 0.7000000104), 0.5000000037, 90, 179.9999995731)
                Line((-1.8000000268, 1.4000000209), (-0.4999999962, 1.7106962251))
                Line((-2.2000000328, 0.1000000015), (-1.8000000268, 1.4000000209))
                Line((-1.4000000209, -1.0000000149), (-2.2000000328, 0.1000000015))
                Line((1.2000000179, -1.4000000209), (-1.4000000209, -1.0000000149))
                Line((1.6000000238, -0.200000003), (1.2000000179, -1.4000000209))
                Line((0.8000000119, 1.6000000238), (1.6000000238, -0.200000003))
            make_face()
        # OneSide extrude, distance=3.2
        extrude(amount=3.2, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical spacer or sleeve with a smooth, hollow tubular body featuring a slightly tapered or rounded end on one side.
def model_40070_be9c502b_0063():
    """Model: silnik v5 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 17 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 2.2872488676, perimeter: 6.7306360412
            with BuildLine():
                CenterArc((0.3712910144, 0.093524511), 1.2010469955, 118.4023856845, 66.0637092926)
                CenterArc((0.3712910144, -0.093524511), 1.2010469955, 175.5339050229, 66.0637092926)
                Line((0.200000003, -1.15), (-0.200000003, -1.15))
                CenterArc((-0.3712910144, -0.093524511), 1.2010469955, -61.5976143155, 66.0637092926)
                Line((0, 0), (0.8261091072, 0))
                Line((0, 0), (0, 1.15))
                Line((0, 1.15), (-0.200000003, 1.15))
            make_face()
            # Profile area: 0.7624162892, perimeter: 3.5609514186
            with BuildLine():
                Line((0, 0), (0, 1.15))
                Line((0, 0), (0.8261091072, 0))
                CenterArc((-0.3712910144, 0.093524511), 1.2010469955, -4.4660949771, 66.0637092926)
                Line((0, 1.15), (0.200000003, 1.15))
            make_face()
        # OneSide extrude, distance=5
        extrude(amount=5)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 5), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.5026548396, perimeter: 2.5132741603
            Circle(0.400000006)
        # OneSide extrude, distance=-0.05
        extrude(amount=-0.05, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a reinforced oval ring or retaining band featuring a smooth, elliptical geometry with textured inner and outer surfaces for grip or structural reinforcement.
def model_40072_b44084ae_0004():
    """Model: uszczelka v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.8360301213, perimeter: 32.0319928553
            with BuildLine():
                CenterArc((0, 0), 2.7, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 2.39805, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 2.1618670296, perimeter: 29.2045596826
            with BuildLine():
                CenterArc((0, 0), 2.39805, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 2.2500000343, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical container or vessel with a slightly tapered, curved body and an open top with a flat or slightly curved rim, featuring a wireframe mesh surface that suggests it may be a pressure vessel, tank, or hollow structural component.
def model_40074_4615c9d1_0001():
    """Model: gora laczenie v4"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 12.5663706144, perimeter: 12.5663706144
            Circle(2)
        # OneSide extrude, distance=3
        extrude(amount=3)
    return part.part


# Description: This is a cylindrical sleeve or barrel with a curved or tapered body, featuring an open top with a flat or slightly curved rim, and appears to be a hollow container or structural component with a smooth curved lateral surface.
def model_40074_4615c9d1_0019():
    """Model: Untitled v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 5.7255526112, perimeter: 8.4823001647
            Circle(1.35)
        # OneSide extrude, distance=2.7
        extrude(amount=2.7)
    return part.part


# Description: This is a flat parallelogram-shaped plate or panel with a slight 3D depth, featuring a beveled or chamfered edge on one corner and a clean, minimalist geometric design with no holes or slots.
def model_40159_583632c6_0000():
    """Model: kabina v6"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.5, perimeter: 5
            with BuildLine():
                Line((-6, 4), (-7.5, 4))
                Line((-6, 5), (-6, 4))
                Line((-7.5, 5), (-6, 5))
                Line((-7.5, 4), (-7.5, 5))
            make_face()
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


# Description: This is a curved duct or transition component with a tapered, tubular shape that features a mesh or perforated surface on one end and transitions to a solid rectangular outlet, designed to redirect and filter airflow.
def model_40421_032c052f_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 11 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 9.8482736492, perimeter: 13.786854368
            with BuildLine():
                Line((0, 2), (0, 0))
                CenterArc((-0.65, 3.0677078252), 1.25, -58.6677485024, 58.6591987764)
                Line((0.5999999861, 3.0675212991), (0.6, 4.0677078078))
                CenterArc((-0.65, 4.0677078252), 1.25, -0.0000007972, 180.0023635674)
                Line((-1.8999591795, 3.0778097808), (-1.8999999989, 4.0676562776))
                CenterArc((-0.65, 3.0677078252), 1.25, 179.5369554228, 59.1307930796)
                Line((-1.3, 0), (-1.3, 2))
                Line((0, 0), (-1.3, 0))
            make_face()
        # OneSide extrude, distance=1.3
        extrude(amount=1.3)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((-0.65, 0.65)):
                Circle(0.25)
        # OneSide extrude, distance=-1.5
        extrude(amount=-1.5, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a rectangular box or tray with an open top, featuring a trapezoidal profile with angled side walls and a recessed or stepped interior surface.
def model_40421_9134086f_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 7.605, perimeter: 14.3341664064
            with BuildLine():
                Line((0, 0), (0, 1.3))
                Line((0, 1.3), (-5.7, 1.3))
                Line((-5.7, 1.3), (-6, 0))
                Line((0, 0), (-6, 0))
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((-1, 0.65)):
                Circle(0.25)
        # OneSide extrude, distance=-3
        extrude(amount=-3, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a bolt or fastener with a cylindrical shaft and a hexagonal or rounded head at the top, designed for threaded fastening applications.
def model_40500_6055e3d7_0008():
    """Model: zmieniacz v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.9503317777, perimeter: 3.4557519189
            Circle(0.55)
        # OneSide extrude, distance=12
        extrude(amount=12)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 12, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.1912608759, perimeter: 9.7389372261
            with BuildLine():
                CenterArc((0, 0), 1, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.55, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.9503317777, perimeter: 3.4557519189
            Circle(0.55)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical connector or adapter with a larger flanged base that transitions to a smaller hollow cylindrical shaft, featuring a threaded or textured upper rim for secure fastening or assembly.
def model_40500_6055e3d7_0023():
    """Model: krótki v1 (2)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            Circle(1)
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.1309733553, perimeter: 3.7699111843
            Circle(0.6)
        # OneSide extrude, distance=2
        extrude(amount=2, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical fastener or bolt with a hexagonal head at the base and a threaded shaft extending upward at an angle.
def model_40500_6055e3d7_0031():
    """Model: do koła v3 (3)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            Circle(1)
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.1309733553, perimeter: 3.7699111843
            Circle(0.6)
        # OneSide extrude, distance=3
        extrude(amount=3, mode=Mode.ADD)
    return part.part


# Description: A dark gray cylindrical rod or shaft with a slightly tapered end, featuring a smooth, uniform surface without visible holes, slots, or flanges.
def model_40514_bb61631d_0005():
    """Model: hex_piston_shaft"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            Circle(0.25)
        # OneSide extrude, distance=9
        extrude(amount=9)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 9, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0279559511, perimeter: 0.863647609
            with BuildLine():
                Line((-0.2, -0.15), (0.2, -0.15))
                CenterArc((0, 0), 0.25, -143.1301023542, 106.2602047083)
            make_face()
            # Profile area: 0.0965613033, perimeter: 1.87831598
            with BuildLine():
                CenterArc((0, 0), 0.25, -143.1301023542, 106.2602047083)
                Line((-0.400000006, -0.15), (-0.2, -0.15))
                Line((-0.400000006, -0.3185415474), (-0.400000006, -0.15))
                Line((0.3387926321, -0.3185415474), (-0.400000006, -0.3185415474))
                Line((0.3387926321, -0.15), (0.3387926321, -0.3185415474))
                Line((0.2, -0.15), (0.3387926321, -0.15))
            make_face()
        # OneSide extrude, distance=-0.9
        extrude(amount=-0.9, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical mesh or perforated filter sleeve with a solid dark body, open top end, and a blue mesh or screening material covering the upper rim portion.
def model_40514_bb61631d_0009():
    """Model: socket_M5x10"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            Circle(0.25)
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0541265877, perimeter: 0.8660254038
            with BuildLine():
                Line((-0.1386371118, -0.0401632241), (-0.0345361835, -0.1401448728))
                Line((-0.0345361835, -0.1401448728), (0.1041009283, -0.0999816487))
                Line((0.1041009283, -0.0999816487), (0.1386371118, 0.0401632241))
                Line((0.1386371118, 0.0401632241), (0.0345361835, 0.1401448728))
                Line((0.0345361835, 0.1401448728), (-0.1041009283, 0.0999816487))
                Line((-0.1041009283, 0.0999816487), (-0.1386371118, -0.0401632241))
            make_face()
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical dowel pin or rod with a slightly tapered end, featuring a uniform circular cross-section along its length and a rounded tip at one end.
def model_40514_bb61631d_0012():
    """Model: shaft_wheel"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            Circle(0.25)
        # OneSide extrude, distance=5.2
        extrude(amount=5.2)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.0102188193, perimeter: 0.6217505544
            with BuildLine():
                Line((0.15, 0.2), (-0.15, 0.2))
                CenterArc((0, 0), 0.25, 53.1301023542, 73.7397952917)
            make_face()
            # Profile area: 0.1664678931, perimeter: 2.0201810222
            with BuildLine():
                CenterArc((0, 0), 0.25, 53.1301023542, 73.7397952917)
                Line((0.3696466054, 0.2), (0.15, 0.2))
                Line((0.3696466054, 0.4295686226), (0.3696466054, 0.2))
                Line((-0.400000006, 0.4295686226), (0.3696466054, 0.4295686226))
                Line((-0.400000006, 0.2), (-0.400000006, 0.4295686226))
                Line((-0.15, 0.2), (-0.400000006, 0.2))
            make_face()
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a camera or sensor housing with a rectangular body, an angled front face with a light blue optical window or lens opening, and a cylindrical barrel or lens mount extending from the right side.
def model_40519_55a097c6_0002():
    """Model: Pusher v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 8 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.9, perimeter: 5.6770329614
            with BuildLine():
                Line((1, -0.5), (1, 0.5))
                Line((1, 0.5), (-0.8, 0.5))
                Line((-0.8, 0.5), (-1, 0))
                Line((-0.8, -0.5), (-1, 0))
                Line((-0.8, -0.5), (1, -0.5))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(1, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.3848451001, perimeter: 2.1991148575
            with Locations((0, 0.5)):
                Circle(0.35)
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)
    return part.part


# Description: This is a structural frame or chassis component with a hexagonal/trapezoidal overall shape, featuring multiple rectangular openings and cross-bracing internal ribs for lightweight rigidity.
def model_40519_55a097c6_0008():
    """Model: Mechanism spacer v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude3 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 20 constraints, 12 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 42.1308816936, perimeter: 35.3362573555
            with BuildLine():
                CenterArc((13.5, 2), 1, 0, 90)
                Line((13.5, 3), (8, 3))
                CenterArc((8, 2), 1, 90, 90)
                Line((7, 2), (7, -1.9999877784))
                CenterArc((8, -1.9999877784), 1, 180, 90)
                Line((13.5, -2.9999877784), (8, -2.9999877784))
                CenterArc((13.5, -1.9999877784), 1, -90, 90)
                Line((14.5, 2), (14.5, -1.9999877784))
            make_face()
            with BuildLine():
                CenterArc((12.75, 1.75), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((12.75, -1.75), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((9.25, -1.75), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((9.25, 1.75), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=2.4
        extrude(amount=2.4)

        # Sketch3 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(7, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 1, perimeter: 4
            with BuildLine():
                Line((-0.5, 1.7), (-0.5, 0.7))
                Line((-0.5, 0.7), (0.5, 0.7))
                Line((0.5, 0.7), (0.5, 1.7))
                Line((0.5, 1.7), (-0.5, 1.7))
            make_face()
        # OneSide extrude, distance=-3
        extrude(amount=-3, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical mesh or perforated container with a wide oval or elliptical opening at the top and a solid dark base, featuring a latticed or gridded surface pattern typical of a strainer, basket, or ventilated enclosure.
def model_40624_e1c5c424_0017():
    """Model: Sruba siodelko"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 7.0685834706, perimeter: 9.4247779608
            with Locations((-110, 0)):
                Circle(1.5)
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 7 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.19643492, perimeter: 6.7488170458
            with BuildLine():
                Line((109.8000016361, 1.4866070948), (109.8000016361, -1.4866070948))
                CenterArc((110, 0), 1.5, -97.6621926015, 15.3245115513)
                Line((110.2000016421, -1.4866066538), (110.2000016421, 1.4866066538))
                CenterArc((110, 0), 1.5, 82.3376810502, 15.3245115513)
            make_face()
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical rod or shaft with a hexagonal head at one end, featuring a tapered or beveled tip, commonly used as a fastener or tool component.
def model_40705_5ff43505_0014():
    """Model: Fast2mm (4)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 3 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0195063672, perimeter: 1.4683185307
            with BuildLine():
                Line((0.07, 0.1212435565), (-0.07, 0.1212435565))
                Line((-0.07, 0.1212435565), (-0.14, 0))
                Line((-0.14, 0), (-0.07, -0.1212435565))
                Line((-0.07, -0.1212435565), (0.07, -0.1212435565))
                Line((0.07, -0.1212435565), (0.14, 0))
                Line((0.14, 0), (0.07, 0.1212435565))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            Circle(0.1)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        # Sketch has 3 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            Circle(0.1)
        # OneSide extrude, distance=-1.8
        extrude(amount=-1.8, mode=Mode.ADD)

        # Sketch2 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 12 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.2), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0022283185, perimeter: 0.1828318504
            with BuildLine():
                Line((-0.02, -0.02), (0.02, -0.02))
                Line((-0.02, -0.02), (-0.02, -0.0599999987))
                CenterArc((0, -0.0599999987), 0.02, -180, 180)
                Line((0.02, -0.0599999987), (0.02, -0.02))
            make_face()
            # Profile area: 0.0022284875, perimeter: 0.1828403004
            with BuildLine():
                CenterArc((0, 0.0600042237), 0.02, 0, 180)
                Line((-0.02, 0.0600042237), (-0.02, 0.02))
                Line((0.02, 0.02), (-0.02, 0.02))
                Line((0.02, 0.02), (0.02, 0.0600042237))
            make_face()
            # Profile area: 0.0022283383, perimeter: 0.1828328431
            with BuildLine():
                Line((-0.02, 0.02), (-0.02, -0.02))
                Line((-0.02, 0.02), (-0.060000495, 0.02))
                CenterArc((-0.060000495, 0), 0.02, 90, 180)
                Line((-0.060000495, -0.02), (-0.02, -0.02))
            make_face()
            # Profile area: 0.0022283185, perimeter: 0.1828318504
            with BuildLine():
                Line((0.02, -0.02), (0.02, 0.02))
                Line((0.02, -0.02), (0.0599999987, -0.02))
                CenterArc((0.0599999987, 0), 0.02, -90, 180)
                Line((0.0599999987, 0.02), (0.02, 0.02))
            make_face()
            # Profile area: 0.0016, perimeter: 0.16
            with BuildLine():
                Line((0.02, 0.02), (-0.02, 0.02))
                Line((-0.02, 0.02), (-0.02, -0.02))
                Line((-0.02, -0.02), (0.02, -0.02))
                Line((0.02, -0.02), (0.02, 0.02))
            make_face()
        # OneSide extrude, distance=-0.06
        extrude(amount=-0.06, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical sleeve or spacer with a rounded end cap, featuring a central axial hole and text markings on its surface, designed for mechanical assembly or alignment purposes.
def model_40705_5ff43505_0017():
    """Model: Fast2.5mmc"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0338702958, perimeter: 1.8064157758
            with BuildLine():
                CenterArc((0, 0), 0.1625, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0490873852, perimeter: 0.7853981634
            Circle(0.125)
        # OneSide extrude, distance=0.15
        extrude(amount=0.15)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0490873852, perimeter: 0.7853981634
            Circle(0.125)
        # OneSide extrude, distance=-0.65
        extrude(amount=-0.65, mode=Mode.ADD)

        # Sketch2 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 12 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.15), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0033685563, perimeter: 0.254977867
            with BuildLine():
                Line((-0.0175, 0.0175), (-0.0175, -0.0175))
                Line((-0.0175, 0.0175), (-0.0999999978, 0.0175))
                CenterArc((-0.0999999978, 0), 0.0175, 90, 180)
                Line((-0.0999999978, -0.0175), (-0.0175, -0.0175))
            make_face()
            # Profile area: 0.0033685563, perimeter: 0.254977866
            with BuildLine():
                Line((0.0175, -0.0175), (0.0175, 0.0175))
                Line((0.0175, -0.0175), (0.0999999973, -0.0175))
                CenterArc((0.0999999973, 0), 0.0175, -90, 180)
                Line((0.0999999973, 0.0175), (0.0175, 0.0175))
            make_face()
            # Profile area: 0.0033685563, perimeter: 0.254977867
            with BuildLine():
                CenterArc((0, 0.0999999978), 0.0175, 0, 180)
                Line((-0.0175, 0.0999999978), (-0.0175, 0.0175))
                Line((0.0175, 0.0175), (-0.0175, 0.0175))
                Line((0.0175, 0.0175), (0.0175, 0.0999999978))
            make_face()
            # Profile area: 0.0033685563, perimeter: 0.254977867
            with BuildLine():
                Line((-0.0175, -0.0175), (0.0175, -0.0175))
                Line((-0.0175, -0.0175), (-0.0175, -0.0999999978))
                CenterArc((0, -0.0999999978), 0.0175, 180, 180)
                Line((0.0175, -0.0999999978), (0.0175, -0.0175))
            make_face()
            # Profile area: 0.001225, perimeter: 0.14
            with BuildLine():
                Line((0.0175, 0.0175), (-0.0175, 0.0175))
                Line((-0.0175, 0.0175), (-0.0175, -0.0175))
                Line((-0.0175, -0.0175), (0.0175, -0.0175))
                Line((0.0175, -0.0175), (0.0175, 0.0175))
            make_face()
        # OneSide extrude, distance=-0.06
        extrude(amount=-0.06, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical sleeve or bushing with a hollow bore, featuring a stepped diameter design with a larger cylindrical body and a smaller diameter section at one end.
def model_40705_5ff43505_0022():
    """Model: Fast2mmc"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0176714587, perimeter: 1.4137166941
            with BuildLine():
                CenterArc((0, 0), 0.125, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            Circle(0.1)
        # OneSide extrude, distance=0.15
        extrude(amount=0.15)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            Circle(0.1)
        # OneSide extrude, distance=-0.65
        extrude(amount=-0.65, mode=Mode.ADD)

        # Sketch2 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 12 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.15), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.002262442, perimeter: 0.1917713329
            with BuildLine():
                Line((-0.0175, 0.0175), (-0.0175, -0.0175))
                Line((-0.0175, 0.0175), (-0.0683967308, 0.0175))
                CenterArc((-0.0683967308, 0), 0.0175, 90, 180)
                Line((-0.0683967308, -0.0175), (-0.0175, -0.0175))
            make_face()
            # Profile area: 0.0023185563, perimeter: 0.1949778665
            with BuildLine():
                Line((-0.0175, -0.0175), (0.0175, -0.0175))
                Line((-0.0175, -0.0175), (-0.0175, -0.0699999976))
                CenterArc((0, -0.0699999976), 0.0175, 180, 180)
                Line((0.0175, -0.0699999976), (0.0175, -0.0175))
            make_face()
            # Profile area: 0.0023185563, perimeter: 0.1949778683
            with BuildLine():
                Line((0.0175, -0.0175), (0.0175, 0.0175))
                Line((0.0175, -0.0175), (0.0699999984, -0.0175))
                CenterArc((0.0699999984, 0), 0.0175, -90, 180)
                Line((0.0699999984, 0.0175), (0.0175, 0.0175))
            make_face()
            # Profile area: 0.0023185563, perimeter: 0.1949778683
            with BuildLine():
                CenterArc((0, 0.0699999984), 0.0175, 0, 180)
                Line((-0.0175, 0.0699999984), (-0.0175, 0.0175))
                Line((0.0175, 0.0175), (-0.0175, 0.0175))
                Line((0.0175, 0.0175), (0.0175, 0.0699999984))
            make_face()
            # Profile area: 0.001225, perimeter: 0.14
            with BuildLine():
                Line((0.0175, 0.0175), (-0.0175, 0.0175))
                Line((-0.0175, 0.0175), (-0.0175, -0.0175))
                Line((-0.0175, -0.0175), (0.0175, -0.0175))
                Line((0.0175, -0.0175), (0.0175, 0.0175))
            make_face()
        # OneSide extrude, distance=-0.06
        extrude(amount=-0.06, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a knurled knob or dial featuring a cylindrical body with a textured knurled surface on the upper portion and a small protruding pin or shaft on the side for mounting or engagement.
def model_40705_5ff43505_0025():
    """Model: Gear1"""
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
            # Profile area: 1.4912777453, perimeter: 4.3289662549
            with BuildLine():
                CenterArc((0, 0), 0.688976378, 7.7063667704, 344.5872664593)
                CenterArc((0, 0), 0.688976378, -7.7063667704, 15.4127335407)
            make_face()
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 0.0536304441, perimeter: 0.9002386045
            with BuildLine():
                Line((0.6827537534, 0.0923891856), (0.7942023087, 0.1074702324))
                CenterArc((0, 0), 0.688976378, -7.7063667704, 15.4127335407)
                Line((0.6827537534, -0.0923891856), (0.7942023087, -0.1074702324))
                _nurbs_edge([(0.7942023087, -0.1074702324), (0.8010548294, -0.1075677346), (0.8149349994, -0.1077652309), (0.8357939193, -0.1044872394), (0.8568308246, -0.0998061399), (0.877977493, -0.0934836599), (0.8991773713, -0.0857754797), (0.9203862743, -0.0767337298), (0.9415467579, -0.0664059018), (0.9626657831, -0.0549094607), (0.9764235334, -0.0463765944), (0.983372251, -0.0420668433)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0205247002, 0.0415739468, 0.0631260167, 0.0851773144, 0.1077258933, 0.1307703615, 0.1543096048, 0.1783426857, 0.2028687972, 0.2028687972, 0.2028687972, 0.2028687972], 3)
                CenterArc((-0.0219762933, 0), 1.0062282618, -2.3960321146, 4.7920642292)
                _nurbs_edge([(0.7942023087, 0.1074702324), (0.8010548294, 0.1075677346), (0.8149349994, 0.1077652309), (0.8357939193, 0.1044872394), (0.8568308246, 0.0998061399), (0.877977493, 0.0934836599), (0.8991773713, 0.0857754797), (0.9203862743, 0.0767337298), (0.9415467579, 0.0664059018), (0.9626657831, 0.0549094607), (0.9764235334, 0.0463765944), (0.983372251, 0.0420668433)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0205247002, 0.0415739468, 0.0631260167, 0.0851773144, 0.1077258933, 0.1307703615, 0.1543096048, 0.1783426857, 0.2028687972, 0.2028687972, 0.2028687972, 0.2028687972], 3)
            make_face()
        # OneSide extrude, distance=0.3
        extrude(amount=0.3, mode=Mode.ADD)
    return part.part


# Description: This is a solid cylindrical pin or dowel with a rounded hemispherical head at one end and a flat or slightly tapered end at the other, commonly used as a fastener, locating pin, or alignment component.
def model_40705_5ff43505_0028():
    """Model: Fast7.5mm (3)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.3688065706, perimeter: 5.4296145832
            with BuildLine():
                CenterArc((0, 0), 0.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.36415, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.4165915928, perimeter: 2.2880219296
            Circle(0.36415)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)

        # Sketch1 -> Extrude4 (Join)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.4165915928, perimeter: 2.2880219296
            Circle(0.36415)
        # OneSide extrude, distance=-4
        extrude(amount=-4, mode=Mode.ADD)

        # Sketch2 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 12 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.2), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0233132745, perimeter: 0.7256637151
            with BuildLine():
                Line((0.04, -0.04), (0.04, 0.04))
                Line((0.04, -0.04), (0.3000000045, -0.04))
                CenterArc((0.3000000045, 0), 0.04, -90, 180)
                Line((0.3000000045, 0.04), (0.04, 0.04))
            make_face()
            # Profile area: 0.0233132728, perimeter: 0.7256636735
            with BuildLine():
                Line((-0.04, 0.04), (-0.04, -0.04))
                Line((-0.04, 0.04), (-0.2999999837, 0.04))
                CenterArc((-0.2999999837, 0), 0.04, 90, 180)
                Line((-0.2999999837, -0.04), (-0.04, -0.04))
            make_face()
            # Profile area: 0.0233132745, perimeter: 0.7256637151
            with BuildLine():
                CenterArc((0, 0.3000000045), 0.04, 0, 179.9999999998)
                Line((-0.04, 0.3000000045), (-0.04, 0.04))
                Line((0.04, 0.04), (-0.04, 0.04))
                Line((0.04, 0.04), (0.04, 0.3000000045))
            make_face()
            # Profile area: 0.0233132745, perimeter: 0.7256637151
            with BuildLine():
                Line((-0.04, -0.04), (0.04, -0.04))
                Line((-0.04, -0.04), (-0.04, -0.3000000045))
                CenterArc((0, -0.3000000045), 0.04, 179.9999999998, 180)
                Line((0.04, -0.3000000045), (0.04, -0.04))
            make_face()
            # Profile area: 0.0064, perimeter: 0.32
            with BuildLine():
                Line((0.04, 0.04), (-0.04, 0.04))
                Line((-0.04, 0.04), (-0.04, -0.04))
                Line((-0.04, -0.04), (0.04, -0.04))
                Line((0.04, -0.04), (0.04, 0.04))
            make_face()
        # OneSide extrude, distance=-0.1
        extrude(amount=-0.1, mode=Mode.SUBTRACT)
    return part.part


MODELS = {
    "model_34782_b461066c_0003": {"func": model_34782_b461066c_0003, "volume": 492.4115431673, "area": 1090.6462198028},
    "model_34782_b461066c_0010": {"func": model_34782_b461066c_0010, "volume": 1668.1913743824, "area": 1964.4657082647},
    "model_34785_dc3b83fa_0022": {"func": model_34785_dc3b83fa_0022, "volume": 3562.1733700891, "area": 1765.5750713175},
    "model_34785_dc3b83fa_0028": {"func": model_34785_dc3b83fa_0028, "volume": 1347.74324839, "area": 1024.1592050703},
    "model_34785_dc3b83fa_0033": {"func": model_34785_dc3b83fa_0033, "volume": 798.7499321752, "area": 645.5972903127},
    "model_34785_dc3b83fa_0034": {"func": model_34785_dc3b83fa_0034, "volume": 713.9269305283, "area": 589.0486225481},
    "model_34785_dc3b83fa_0035": {"func": model_34785_dc3b83fa_0035, "volume": 7.137698509, "area": 73.8902592124},
    "model_34917_61633e20_0004": {"func": model_34917_61633e20_0004, "volume": 148.2, "area": 1509.6},
    "model_34917_61633e20_0007": {"func": model_34917_61633e20_0007, "volume": 8.4823001647, "area": 171.3424633268},
    "model_35132_35c342c8_0005": {"func": model_35132_35c342c8_0005, "volume": 3.5328306374, "area": 25.2977902223},
    "model_35132_35c342c8_0010": {"func": model_35132_35c342c8_0010, "volume": 0.1475479954, "area": 1.9020086759},
    "model_35145_a3d7363c_0000": {"func": model_35145_a3d7363c_0000, "volume": 26.88, "area": 539.52},
    "model_35145_a3d7363c_0011": {"func": model_35145_a3d7363c_0011, "volume": 288.9684705669, "area": 449.7024235913},
    "model_35145_a3d7363c_0015": {"func": model_35145_a3d7363c_0015, "volume": 36.8, "area": 377.92},
    "model_35154_61b67282_0003": {"func": model_35154_61b67282_0003, "volume": 0.1613011478, "area": 1.9909843442},
    "model_35166_562b126c_0009": {"func": model_35166_562b126c_0009, "volume": 16.9594182723, "area": 42.4307038086},
    "model_35580_2ab34839_0006": {"func": model_35580_2ab34839_0006, "volume": 19080.5498003333, "area": 8138.3474858622},
    "model_35580_2ab34839_0008": {"func": model_35580_2ab34839_0008, "volume": 7945.5976480552, "area": 6829.2600326853},
    "model_35580_2ab34839_0009": {"func": model_35580_2ab34839_0009, "volume": 49253.0964914873, "area": 18326.5482457437},
    "model_35962_dbbd6e18_0002": {"func": model_35962_dbbd6e18_0002, "volume": 0.0844824888, "area": 1.2345363289},
    "model_35962_dbbd6e18_0009": {"func": model_35962_dbbd6e18_0009, "volume": 0.3609426423, "area": 3.999137864},
    "model_35962_dbbd6e18_0011": {"func": model_35962_dbbd6e18_0011, "volume": 3.6572767547, "area": 77.9979311489},
    "model_35968_5488b3e5_0007": {"func": model_35968_5488b3e5_0007, "volume": 3.3462870499, "area": 31.9696322411},
    "model_35968_5488b3e5_0009": {"func": model_35968_5488b3e5_0009, "volume": 16.3355839604, "area": 127.3963221405},
    "model_35968_5488b3e5_0010": {"func": model_35968_5488b3e5_0010, "volume": 79.7336215481, "area": 540.4167682705},
    "model_36088_1ea9c8a9_0006": {"func": model_36088_1ea9c8a9_0006, "volume": 0.0700663896, "area": 1.092153267},
    "model_36088_1ea9c8a9_0013": {"func": model_36088_1ea9c8a9_0013, "volume": 1.1151454895, "area": 11.4266275293},
    "model_36194_c9cfd107_0010": {"func": model_36194_c9cfd107_0010, "volume": 0.0001842809, "area": 0.0262451541},
    "model_36194_c9cfd107_0018": {"func": model_36194_c9cfd107_0018, "volume": 0.0001762036, "area": 0.0266976936},
    "model_36268_3c96c142_0005": {"func": model_36268_3c96c142_0005, "volume": 3.83047621, "area": 35.999928},
    "model_36413_fb06800c_0001": {"func": model_36413_fb06800c_0001, "volume": 4.762767133, "area": 23.0942054136},
    "model_36413_fb06800c_0008": {"func": model_36413_fb06800c_0008, "volume": 7.955, "area": 24.2035281374},
    "model_36451_1a7f9437_0007": {"func": model_36451_1a7f9437_0007, "volume": 152.5609944614, "area": 336.5940904691},
    "model_36735_f4ef1c35_0012": {"func": model_36735_f4ef1c35_0012, "volume": 0.0318045889, "area": 0.751507263},
    "model_36851_2c8f1bb6_0008": {"func": model_36851_2c8f1bb6_0008, "volume": 4.1197249082, "area": 20.4364619726},
    "model_36851_2c8f1bb6_0013": {"func": model_36851_2c8f1bb6_0013, "volume": 1.6757933569, "area": 9.903171495},
    "model_36851_2c8f1bb6_0019": {"func": model_36851_2c8f1bb6_0019, "volume": 4.6695036226, "area": 22.6355768301},
    "model_36953_bdaf025b_0004": {"func": model_36953_bdaf025b_0004, "volume": 846.84824, "area": 1810.56928},
    "model_37040_ecbcd25e_0013": {"func": model_37040_ecbcd25e_0013, "volume": 121.6060287521, "area": 149.9137166941},
    "model_37040_ecbcd25e_0034": {"func": model_37040_ecbcd25e_0034, "volume": 424.256379904, "area": 341.1769621799},
    "model_37117_89aac9d4_0002": {"func": model_37117_89aac9d4_0002, "volume": 59.9183337723, "area": 306.1026727176},
    "model_37117_89aac9d4_0006": {"func": model_37117_89aac9d4_0006, "volume": 5.2196378808, "area": 25.4280106977},
    "model_37377_90529181_0014": {"func": model_37377_90529181_0014, "volume": 551.25, "area": 1010.1},
    "model_37520_18f4b548_0002": {"func": model_37520_18f4b548_0002, "volume": 2067.707380976, "area": 2767.513725695},
    "model_37599_faf701a1_0005": {"func": model_37599_faf701a1_0005, "volume": 254.9073888438, "area": 820.4092009695},
    "model_37599_faf701a1_0010": {"func": model_37599_faf701a1_0010, "volume": 0.8342937093, "area": 17.1826256341},
    "model_37605_e35cc4df_0002": {"func": model_37605_e35cc4df_0002, "volume": 0.2290619307, "area": 2.4523019421},
    "model_37605_e35cc4df_0012": {"func": model_37605_e35cc4df_0012, "volume": 71.8963998397, "area": 125.4559199711},
    "model_37605_e35cc4df_0015": {"func": model_37605_e35cc4df_0015, "volume": 0.6394247774, "area": 8.9569911917},
    "model_37615_8399c412_0008": {"func": model_37615_8399c412_0008, "volume": 2.5775344266, "area": 15.6269602134},
    "model_37615_8399c412_0012": {"func": model_37615_8399c412_0012, "volume": 7.6048142105, "area": 37.2453096491},
    "model_37683_e2cca100_0001": {"func": model_37683_e2cca100_0001, "volume": 0.6974335691, "area": 8.6079638708},
    "model_37683_e2cca100_0011": {"func": model_37683_e2cca100_0011, "volume": 0.5172345061, "area": 5.5854867188},
    "model_37846_cde34fcd_0000": {"func": model_37846_cde34fcd_0000, "volume": 10.142473563, "area": 51.5541925218},
    "model_37846_cde34fcd_0024": {"func": model_37846_cde34fcd_0024, "volume": 0.046181412, "area": 0.9990264638},
    "model_37846_cde34fcd_0046": {"func": model_37846_cde34fcd_0046, "volume": 7.108, "area": 30.8},
    "model_38196_ea48fa42_0007": {"func": model_38196_ea48fa42_0007, "volume": 4.556786335, "area": 21.9993051783},
    "model_38196_ea48fa42_0009": {"func": model_38196_ea48fa42_0009, "volume": 0.1538202303, "area": 1.7335308263},
    "model_38276_c9ef069a_0007": {"func": model_38276_c9ef069a_0007, "volume": 35.9162797885, "area": 95.5382376962},
    "model_38287_88ec74de_0010": {"func": model_38287_88ec74de_0010, "volume": 85.5829575118, "area": 243.544106588},
    "model_38287_88ec74de_0036": {"func": model_38287_88ec74de_0036, "volume": 5.6941366846, "area": 31.1017672705},
    "model_38287_88ec74de_0079": {"func": model_38287_88ec74de_0079, "volume": 18.8986433068, "area": 153.1526418625},
    "model_38288_740bfe5a_0002": {"func": model_38288_740bfe5a_0002, "volume": 1030.8619977777, "area": 1597.280825385},
    "model_38675_6e07d74b_0000": {"func": model_38675_6e07d74b_0000, "volume": 28.5688581936, "area": 54.1924732744},
    "model_38675_6e07d74b_0003": {"func": model_38675_6e07d74b_0003, "volume": 3.4361170585, "area": 18.064158039},
    "model_38675_6e07d74b_0005": {"func": model_38675_6e07d74b_0005, "volume": 22.5000000745, "area": 78.000000298},
    "model_38739_f321c899_0009": {"func": model_38739_f321c899_0009, "volume": 55.0370129527, "area": 260.0157415545},
    "model_38740_c9ed5246_0000": {"func": model_38740_c9ed5246_0000, "volume": 10.5196292693, "area": 36.4882409882},
    "model_38740_c9ed5246_0005": {"func": model_38740_c9ed5246_0005, "volume": 4.7143642515, "area": 18.4774163434},
    "model_38924_16a41517_0000": {"func": model_38924_16a41517_0000, "volume": 0.807389312, "area": 5.1522119519},
    "model_39109_816b707e_0007": {"func": model_39109_816b707e_0007, "volume": 0.00189, "area": 0.1116},
    "model_39109_816b707e_0009": {"func": model_39109_816b707e_0009, "volume": 0.0024116792, "area": 0.180942964},
    "model_39109_816b707e_0010": {"func": model_39109_816b707e_0010, "volume": 0.1509400045, "area": 2.0598938402},
    "model_39109_816b707e_0012": {"func": model_39109_816b707e_0012, "volume": 0.1631249904, "area": 1.8081979542},
    "model_39306_ee445998_0003": {"func": model_39306_ee445998_0003, "volume": 1.3744467859, "area": 8.560839981},
    "model_39306_ee445998_0004": {"func": model_39306_ee445998_0004, "volume": 0.1185951183, "area": 1.7907077903},
    "model_39389_d641313f_0005": {"func": model_39389_d641313f_0005, "volume": 98.9281813552, "area": 252.7899784324},
    "model_39389_d641313f_0036": {"func": model_39389_d641313f_0036, "volume": 101.9054117008, "area": 620.8572481657},
    "model_39390_61cd2601_0010": {"func": model_39390_61cd2601_0010, "volume": 0.4437499623, "area": 5.0226212549},
    "model_39637_ca6a9a60_0009": {"func": model_39637_ca6a9a60_0009, "volume": 15.8940082567, "area": 102.4675974502},
    "model_39708_228f26be_0003": {"func": model_39708_228f26be_0003, "volume": 853.5697370311, "area": 1156.2651452938},
    "model_39708_228f26be_0005": {"func": model_39708_228f26be_0005, "volume": 1597.3007802894, "area": 1461.86834548},
    "model_39708_228f26be_0006": {"func": model_39708_228f26be_0006, "volume": 9036.0966772836, "area": 5399.3312642074},
    "model_39708_228f26be_0009": {"func": model_39708_228f26be_0009, "volume": 47.6825585924, "area": 82.8892368234},
    "model_39792_60786b6c_0004": {"func": model_39792_60786b6c_0004, "volume": 4.529126806, "area": 18.5803299792},
    "model_39792_60786b6c_0005": {"func": model_39792_60786b6c_0005, "volume": 0.1379245909, "area": 2.7346865914},
    "model_39792_60786b6c_0006": {"func": model_39792_60786b6c_0006, "volume": 0.240331838, "area": 2.5918139392},
    "model_39793_5193d5ab_0010": {"func": model_39793_5193d5ab_0010, "volume": 122.0068124375, "area": 583.36576875},
    "model_39793_5193d5ab_0012": {"func": model_39793_5193d5ab_0012, "volume": 0.7541232404, "area": 5.8588052271},
    "model_39793_5193d5ab_0015": {"func": model_39793_5193d5ab_0015, "volume": 0.1099763059, "area": 2.4147778301},
    "model_39795_7d4d7d57_0005": {"func": model_39795_7d4d7d57_0005, "volume": 165.1508728511, "area": 338.3057641144},
    "model_39819_c4b9cef8_0000": {"func": model_39819_c4b9cef8_0000, "volume": 3534.2917352885, "area": 1884.9555921539},
    "model_39932_7b9150e8_0002": {"func": model_39932_7b9150e8_0002, "volume": 2622.5676285982, "area": 20174.1092906867},
    "model_40052_42bdc982_0006": {"func": model_40052_42bdc982_0006, "volume": 430.2291735289, "area": 637.6388980385},
    "model_40052_42bdc982_0021": {"func": model_40052_42bdc982_0021, "volume": 938.767024359, "area": 770.3222849673},
    "model_40061_d07e8764_0003": {"func": model_40061_d07e8764_0003, "volume": 78962.4322728897, "area": 23456.0174616949},
    "model_40061_d07e8764_0004": {"func": model_40061_d07e8764_0004, "volume": 24168.6260378374, "area": 11255.1168444923},
    "model_40061_d07e8764_0019": {"func": model_40061_d07e8764_0019, "volume": 87.5323418812, "area": 138.2283072088},
    "model_40061_d07e8764_0020": {"func": model_40061_d07e8764_0020, "volume": 114.5613913222, "area": 170.0672142774},
    "model_40061_d07e8764_0021": {"func": model_40061_d07e8764_0021, "volume": 7.2951895537, "area": 41.0077421842},
    "model_40070_be9c502b_0019": {"func": model_40070_be9c502b_0019, "volume": 2, "area": 11},
    "model_40070_be9c502b_0023": {"func": model_40070_be9c502b_0023, "volume": 153.2766394981, "area": 368.3932237755},
    "model_40070_be9c502b_0062": {"func": model_40070_be9c502b_0062, "volume": 0.2610059908, "area": 2.824463349},
    "model_40070_be9c502b_0063": {"func": model_40070_be9c502b_0063, "volume": 15.2231930418, "area": 37.9218402481},
    "model_40072_b44084ae_0004": {"func": model_40072_b44084ae_0004, "volume": 2.6454700418, "area": 43.3900747648},
    "model_40074_4615c9d1_0001": {"func": model_40074_4615c9d1_0001, "volume": 37.6991118431, "area": 62.8318530718},
    "model_40074_4615c9d1_0019": {"func": model_40074_4615c9d1_0019, "volume": 15.4589920502, "area": 34.353315667},
    "model_40159_583632c6_0000": {"func": model_40159_583632c6_0000, "volume": 0.15, "area": 3.5},
    "model_40421_032c052f_0000": {"func": model_40421_032c052f_0000, "volume": 12.5082314327, "area": 39.9756524671},
    "model_40421_9134086f_0000": {"func": model_40421_9134086f_0000, "volume": 14.6209513775, "area": 48.5907217932},
    "model_40500_6055e3d7_0008": {"func": model_40500_6055e3d7_0008, "volume": 12.9747776593, "area": 50.8938009882},
    "model_40500_6055e3d7_0023": {"func": model_40500_6055e3d7_0023, "volume": 5.4035393642, "area": 20.106192983},
    "model_40500_6055e3d7_0031": {"func": model_40500_6055e3d7_0031, "volume": 6.5345127195, "area": 23.8761041673},
    "model_40514_bb61631d_0005": {"func": model_40514_bb61631d_0005, "volume": 1.7419855116, "area": 14.4725831748},
    "model_40514_bb61631d_0009": {"func": model_40514_bb61631d_0009, "volume": 0.1855242233, "area": 2.1367004893},
    "model_40514_bb61631d_0012": {"func": model_40514_bb61631d_0012, "volume": 1.0107987931, "area": 8.5390894266},
    "model_40519_55a097c6_0002": {"func": model_40519_55a097c6_0002, "volume": 2.2848451001, "area": 11.6761478189},
    "model_40519_55a097c6_0008": {"func": model_40519_55a097c6_0008, "volume": 98.1141160646, "area": 181.0687810405},
    "model_40624_e1c5c424_0017": {"func": model_40624_e1c5c424_0017, "volume": 6.4703660106, "area": 26.1339638763},
    "model_40705_5ff43505_0014": {"func": model_40705_5ff43505_0014, "volume": 0.0661023187, "area": 1.4350981534},
    "model_40705_5ff43505_0017": {"func": model_40705_5ff43505_0017, "volume": 0.043468499, "area": 0.8823714981},
    "model_40705_5ff43505_0022": {"func": model_40705_5ff43505_0022, "volume": 0.0271568734, "area": 0.6625938361},
    "model_40705_5ff43505_0025": {"func": model_40705_5ff43505_0025, "volume": 0.4634736666, "area": 4.5473753315},
    "model_40705_5ff43505_0028": {"func": model_40705_5ff43505_0028, "volume": 1.8134806944, "area": 11.6094680578},
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
