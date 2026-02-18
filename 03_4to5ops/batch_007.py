"""Batch 007 - passing/03_4to5ops
118 models bundled from Fusion360 Gallery reconstructions.
"""

from build123d import *
from build123d import Edge, BuildLine
from collections import Counter
from OCP.BRepBuilderAPI import BRepBuilderAPI_MakeEdge
from OCP.Geom import Geom_BSplineCurve
from OCP.TColStd import TColStd_Array1OfReal, TColStd_Array1OfInteger
from OCP.TColgp import TColgp_Array1OfPnt
from OCP.gp import gp_Pnt


def model_24412_a8e106be_0003():
    """Model: Befestigungsbügel"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 19 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.6000000226, perimeter: 16.399999994
            with BuildLine():
                Line((-1.2, 1.599999997), (1.2, 1.599999997))
                Line((1.2, 1.599999997), (1.2, 0))
                Line((1.2, 0), (2.4, 0))
                Line((2.4, 0), (2.4, 0.200000003))
                Line((2.4, 0.200000003), (1.400000003, 0.200000003))
                Line((1.400000003, 0.200000003), (1.400000003, 1.8))
                Line((1.400000003, 1.8), (-1.400000003, 1.8))
                Line((-1.400000003, 0.200000003), (-1.400000003, 1.8))
                Line((-2.4, 0.200000003), (-1.400000003, 0.200000003))
                Line((-2.4, 0), (-2.4, 0.200000003))
                Line((-1.2, 0), (-2.4, 0))
                Line((-1.2, 1.599999997), (-1.2, 0))
            make_face()
        # OneSide extrude, distance=3.5
        extrude(amount=3.5)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.1200000024, perimeter: 6.4000000119
            with BuildLine():
                Line((-1.400000003, 1.4), (1.400000003, 1.4))
                Line((1.400000003, 1.4), (1.400000003, 1.8))
                Line((1.400000003, 1.8), (-1.400000003, 1.8))
                Line((-1.400000003, 1.4), (-1.400000003, 1.8))
            make_face()
        # OneSide extrude, distance=1.4
        extrude(amount=1.4, mode=Mode.SUBTRACT)
    return part.part


def model_24413_786c8353_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 578.0958540849, perimeter: 110.9859632679
            with BuildLine():
                Line((19.7695, 6.55), (-19.7695, 6.55))
                CenterArc((-19.7695, 4.05), 2.5, 90, 90)
                Line((-22.2695, 4.05), (-22.2695, -4.05))
                CenterArc((-19.7695, -4.05), 2.5, 180, 90)
                Line((19.7695, -6.55), (-19.7695, -6.55))
                CenterArc((19.7695, -4.05), 2.5, -90, 90)
                Line((22.2695, 4.05), (22.2695, -4.05))
                CenterArc((19.7695, 4.05), 2.5, 0, 90)
            make_face()
        # OneSide extrude, distance=18.5
        extrude(amount=18.5)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 306.1858735005, perimeter: 88.3249004941
            with BuildLine():
                CenterArc((-15.7195, 0), 4.05, 90, 180)
                Line((15.7195, -4.05), (-15.7195, -4.05))
                CenterArc((15.7195, 0), 4.05, -90, 180)
                Line((-15.7195, 4.05), (15.7195, 4.05))
            make_face()
        # OneSide extrude, distance=-16.5
        extrude(amount=-16.5, mode=Mode.SUBTRACT)
    return part.part


def model_24443_996411f9_0000():
    """Model: P13-FLYWHEEL"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 19.3522107461, perimeter: 17.5929188601
            with BuildLine():
                CenterArc((0, 0), 2.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=1
        extrude(amount=1, both=True)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -1, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 4.3903757334, perimeter: 13.5088484104
            with BuildLine():
                CenterArc((0, 0), 1.4, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.75, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.SUBTRACT)
    return part.part


def model_24476_568e9ca0_0004():
    """Model: imbus 2 mm v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.7138918343, perimeter: 7.9448454098
            with BuildLine():
                CenterArc((0, 0), 0.3500177317, -25.3755561163, 295.3755561163)
                Line((0, -0.3500177317), (2.5, -0.3500177317))
                Line((2.5, -0.3500177317), (2.5, -0.1499999966))
                Line((2.5, -0.1499999966), (0.3162473929, -0.1499999966))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(2.5, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 0.0004140438, perimeter: 0.1154038658
            with BuildLine():
                Line((-0.3500177317, 0.1267795603), (-0.3500177317, 0.0732204397))
                Line((-0.3500177317, 0.1267795603), (-0.365478918, 0.1))
                Line((-0.365478918, 0.1), (-0.3500177317, 0.0732204397))
            make_face()
            # Profile area: 0.0004140438, perimeter: 0.1154038658
            with BuildLine():
                Line((-0.1499999966, 0.0732204397), (-0.1499999966, 0.1267795603))
                Line((-0.1499999966, 0.0732204397), (-0.1345388103, 0.1))
                Line((-0.1345388103, 0.1), (-0.1499999966, 0.1267795603))
            make_face()
        # OneSide extrude, distance=-2
        extrude(amount=-2, mode=Mode.ADD)

        # Sketch2 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(2.5, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 0.0015476546, perimeter: 0.2000419615
            with BuildLine():
                Line((-0.3500177317, 0.0732204397), (-0.3077438911, 0))
                Line((-0.3500177317, 0.0732204397), (-0.3500177317, 0))
                Line((-0.3500177317, 0), (-0.3077438911, 0))
            make_face()
            # Profile area: 0.0015476546, perimeter: 0.2000419615
            with BuildLine():
                Line((-0.1499999966, 0.1267795603), (-0.1922738372, 0.2))
                Line((-0.1499999966, 0.1267795603), (-0.1499999966, 0.2))
                Line((-0.1499999966, 0.2), (-0.1922738372, 0.2))
            make_face()
            # Profile area: 0.0015476546, perimeter: 0.2000419615
            with BuildLine():
                Line((-0.3077438911, 0.2), (-0.3500177317, 0.1267795603))
                Line((-0.3077438911, 0.2), (-0.3500177317, 0.2))
                Line((-0.3500177317, 0.2), (-0.3500177317, 0.1267795603))
            make_face()
            # Profile area: 0.0015476546, perimeter: 0.2000419615
            with BuildLine():
                Line((-0.1499999966, 0), (-0.1499999966, 0.0732204397))
                Line((-0.1922738372, 0), (-0.1499999966, 0.0732204397))
                Line((-0.1922738372, 0), (-0.1499999966, 0))
            make_face()
        # OneSide extrude, distance=-2
        extrude(amount=-2, mode=Mode.SUBTRACT)
    return part.part


def model_24476_568e9ca0_0007():
    """Model: imbus 2,5 mm v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.9018020857, perimeter: 9.4361353688
            with BuildLine():
                CenterArc((0, 0), 0.35, -16.601549599, 286.601549599)
                Line((0, -0.35), (3.1, -0.35))
                Line((3.1, -0.35), (3.1, -0.1))
                Line((3.1, -0.1), (0.3354101966, -0.1))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.25
        extrude(amount=0.25)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(3.1, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 0.0024171959, perimeter: 0.25
            with BuildLine():
                Line((-0.2971687836, 0.25), (-0.35, 0.1584936491))
                Line((-0.2971687836, 0.25), (-0.35, 0.25))
                Line((-0.35, 0.25), (-0.35, 0.1584936491))
            make_face()
            # Profile area: 0.0024171959, perimeter: 0.25
            with BuildLine():
                Line((-0.35, 0.0915063509), (-0.2971687836, 0))
                Line((-0.35, 0.0915063509), (-0.35, 0))
                Line((-0.35, 0), (-0.2971687836, 0))
            make_face()
            # Profile area: 0.0024171959, perimeter: 0.25
            with BuildLine():
                Line((-0.1, 0.1584936491), (-0.1528312164, 0.25))
                Line((-0.1, 0.1584936491), (-0.1, 0.25))
                Line((-0.1, 0.25), (-0.1528312164, 0.25))
            make_face()
            # Profile area: 0.0024171959, perimeter: 0.25
            with BuildLine():
                Line((-0.1, 0), (-0.1, 0.0915063509))
                Line((-0.1528312164, 0), (-0.1, 0.0915063509))
                Line((-0.1528312164, 0), (-0.1, 0))
            make_face()
        # OneSide extrude, distance=-2.3
        extrude(amount=-2.3, mode=Mode.SUBTRACT)

        # Sketch2 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(3.1, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 0.0006476857, perimeter: 0.1443375673
            with BuildLine():
                Line((-0.35, 0.1584936491), (-0.35, 0.0915063509))
                Line((-0.35, 0.1584936491), (-0.3693375673, 0.125))
                Line((-0.3693375673, 0.125), (-0.35, 0.0915063509))
            make_face()
            # Profile area: 0.0006476857, perimeter: 0.1443375673
            with BuildLine():
                Line((-0.1, 0.0915063509), (-0.1, 0.1584936491))
                Line((-0.1, 0.0915063509), (-0.0806624327, 0.125))
                Line((-0.0806624327, 0.125), (-0.1, 0.1584936491))
            make_face()
        # OneSide extrude, distance=-2.3
        extrude(amount=-2.3, mode=Mode.ADD)
    return part.part


def model_24476_568e9ca0_0008():
    """Model: imbus 3 mm v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.0397245768, perimeter: 9.4238939575
            with BuildLine():
                CenterArc((0, 0), 0.35, -8.2132107017, 278.2132107017)
                Line((0, -0.35), (3.1, -0.35))
                Line((3.1, -0.35), (3.1, -0.05))
                Line((3.1, -0.05), (0.3464101615, -0.05))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(3.1, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 0.0034807621, perimeter: 0.3
            with BuildLine():
                Line((-0.35, 0.1098076211), (-0.2866025404, 0))
                Line((-0.35, 0.1098076211), (-0.35, 0))
                Line((-0.35, 0), (-0.2866025404, 0))
            make_face()
            # Profile area: 0.0034807621, perimeter: 0.3
            with BuildLine():
                Line((-0.2866025404, 0.3), (-0.35, 0.1901923789))
                Line((-0.2866025404, 0.3), (-0.35, 0.3))
                Line((-0.35, 0.3), (-0.35, 0.1901923789))
            make_face()
            # Profile area: 0.0034807621, perimeter: 0.3
            with BuildLine():
                Line((-0.05, 0.1901923789), (-0.1133974596, 0.3))
                Line((-0.05, 0.1901923789), (-0.05, 0.3))
                Line((-0.05, 0.3), (-0.1133974596, 0.3))
            make_face()
            # Profile area: 0.0034807621, perimeter: 0.3
            with BuildLine():
                Line((-0.05, 0), (-0.05, 0.1098076211))
                Line((-0.1133974596, 0), (-0.05, 0.1098076211))
                Line((-0.1133974596, 0), (-0.05, 0))
            make_face()
        # OneSide extrude, distance=-2.3
        extrude(amount=-2.3, mode=Mode.SUBTRACT)

        # Sketch2 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(3.1, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 0.0009326674, perimeter: 0.1732050808
            with BuildLine():
                Line((-0.35, 0.1901923789), (-0.35, 0.1098076211))
                Line((-0.35, 0.1901923789), (-0.3732050808, 0.15))
                Line((-0.3732050808, 0.15), (-0.35, 0.1098076211))
            make_face()
            # Profile area: 0.0009326674, perimeter: 0.1732050808
            with BuildLine():
                Line((-0.05, 0.1098076211), (-0.05, 0.1901923789))
                Line((-0.05, 0.1098076211), (-0.0267949192, 0.15))
                Line((-0.0267949192, 0.15), (-0.05, 0.1901923789))
            make_face()
        # OneSide extrude, distance=-2.3
        extrude(amount=-2.3, mode=Mode.ADD)
    return part.part


def model_24476_568e9ca0_0012():
    """Model: imbus 5 mm v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.5914389003, perimeter: 9.4488858385
            with BuildLine():
                CenterArc((0, 0), 0.35, 25.3769335252, 244.6230664748)
                Line((0, -0.35), (3.1, -0.35))
                Line((3.1, -0.35), (3.1, 0.15))
                Line((3.1, 0.15), (0.316227766, 0.15))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(3.1, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 0.0025907422, perimeter: 0.2886751025
            with BuildLine():
                Line((-0.35, 0.3169872944), (-0.35, 0.1830127131))
                Line((-0.35, 0.3169872944), (-0.3886751303, 0.2500000037))
                Line((-0.3886751303, 0.2500000037), (-0.35, 0.1830127131))
            make_face()
            # Profile area: 0.0025907422, perimeter: 0.2886751025
            with BuildLine():
                Line((0.15, 0.1830127131), (0.15, 0.3169872944))
                Line((0.15, 0.1830127131), (0.1886751303, 0.2500000037))
                Line((0.1886751303, 0.2500000037), (0.15, 0.3169872944))
            make_face()
        # OneSide extrude, distance=-2.3
        extrude(amount=-2.3, mode=Mode.ADD)

        # Sketch2 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(3.1, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 0.0096687848, perimeter: 0.5000000176
            with BuildLine():
                Line((-0.35, 0.1830127131), (-0.2443375651, 0.0000000075))
                Line((-0.35, 0.1830127131), (-0.35, 0))
                Line((-0.35, 0), (-0.2443375651, 0.0000000075))
            make_face()
            # Profile area: 0.009668784, perimeter: 0.5000000102
            with BuildLine():
                Line((-0.2443375651, 0.5), (-0.35, 0.3169872944))
                Line((-0.2443375651, 0.5), (-0.35, 0.5))
                Line((-0.35, 0.5), (-0.35, 0.3169872944))
            make_face()
            # Profile area: 0.009668784, perimeter: 0.5000000102
            with BuildLine():
                Line((0.15, 0.3169872944), (0.0443375651, 0.5))
                Line((0.15, 0.3169872944), (0.15, 0.5))
                Line((0.15, 0.5), (0.0443375651, 0.5))
            make_face()
            # Profile area: 0.0096687848, perimeter: 0.5000000176
            with BuildLine():
                Line((0.15, 0), (0.15, 0.1830127131))
                Line((0.0443375651, 0.0000000075), (0.15, 0.1830127131))
                Line((0.0443375651, 0.0000000075), (0.15, 0))
            make_face()
        # OneSide extrude, distance=-2.3
        extrude(amount=-2.3, mode=Mode.SUBTRACT)
    return part.part


def model_24476_568e9ca0_0030():
    """Model: schraubenzieher v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 4 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.1772842842, perimeter: 9.4201324699
            with BuildLine():
                CenterArc((0, 0), 0.35, 0, 270)
                Line((0, -0.35), (3.1, -0.35))
                Line((3.1, -0.35), (3.1, 0))
                Line((3.1, 0), (0.35, 0))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.35
        extrude(amount=0.35)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 52 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(3.1, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 0.0260860311, perimeter: 0.6512296517
            with BuildLine():
                Line((0, 0.18), (0, 0.35))
                Line((0, 0.35), (-0.17, 0.35))
                CenterArc((-0.17, 0.345), 0.005, 0, 90)
                Line((-0.165, 0.2326177395), (-0.165, 0.345))
                CenterArc((-0.155, 0.2326177395), 0.01, -180, 70.8573288337)
                CenterArc((-0.175, 0.175), 0.0509901951, 19.1426711663, 51.7146576675)
                CenterArc((-0.1173822605, 0.195), 0.01, -160.8573288337, 70.8573288337)
                Line((-0.005, 0.185), (-0.1173822605, 0.185))
                CenterArc((-0.005, 0.18), 0.005, 0, 90)
            make_face()
            # Profile area: 0.0260860311, perimeter: 0.6512296517
            with BuildLine():
                Line((-0.345, 0.185), (-0.2326177395, 0.185))
                CenterArc((-0.2326177395, 0.195), 0.01, -90, 70.8573288337)
                CenterArc((-0.175, 0.175), 0.0509901951, 109.1426711663, 51.7146576675)
                CenterArc((-0.195, 0.2326177395), 0.01, -70.8573288337, 70.8573288337)
                Line((-0.185, 0.2326177395), (-0.185, 0.345))
                CenterArc((-0.18, 0.345), 0.005, 90, 90)
                Line((-0.18, 0.35), (-0.35, 0.35))
                Line((-0.35, 0.35), (-0.35, 0.18))
                CenterArc((-0.345, 0.18), 0.005, 90, 90)
            make_face()
            # Profile area: 0.0260860311, perimeter: 0.6512296517
            with BuildLine():
                Line((-0.17, 0), (0, 0))
                Line((0, 0), (0, 0.17))
                CenterArc((-0.005, 0.17), 0.005, -90, 90)
                Line((-0.005, 0.165), (-0.1173822605, 0.165))
                CenterArc((-0.1173822605, 0.155), 0.01, 90, 70.8573288337)
                CenterArc((-0.175, 0.175), 0.0509901951, -70.8573288337, 51.7146576675)
                CenterArc((-0.155, 0.1173822605), 0.01, 109.1426711663, 70.8573288337)
                Line((-0.165, 0.1173822605), (-0.165, 0.005))
                CenterArc((-0.17, 0.005), 0.005, -90, 90)
            make_face()
            # Profile area: 0.0260860311, perimeter: 0.6512296517
            with BuildLine():
                Line((-0.35, 0.17), (-0.35, 0))
                Line((-0.35, 0), (-0.18, 0))
                CenterArc((-0.18, 0.005), 0.005, 180, 90)
                Line((-0.185, 0.1173822605), (-0.185, 0.005))
                CenterArc((-0.195, 0.1173822605), 0.01, 0, 70.8573288337)
                CenterArc((-0.175, 0.175), 0.0509901951, -160.8573288337, 51.7146576675)
                CenterArc((-0.2326177395, 0.155), 0.01, 19.1426711663, 70.8573288337)
                Line((-0.345, 0.165), (-0.2326177395, 0.165))
                CenterArc((-0.345, 0.17), 0.005, 180, 90)
            make_face()
        # OneSide extrude, distance=-0.85
        extrude(amount=-0.85, mode=Mode.SUBTRACT)
    return part.part


def model_24476_568e9ca0_0033():
    """Model: schraubenzieher flach v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 3 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.1772842842, perimeter: 9.4201324699
            with BuildLine():
                CenterArc((0, 0), 0.35, 0, 270)
                Line((0, -0.35), (3.1, -0.35))
                Line((3.1, -0.35), (3.1, 0))
                Line((3.1, 0), (0.35, 0))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.35
        extrude(amount=0.35)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 16 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(3.1, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 0.0525, perimeter: 1
            with BuildLine():
                Line((0, 0), (0, 0.35))
                Line((0, 0.35), (-0.15, 0.35))
                Line((-0.15, 0.35), (-0.15, 0))
                Line((-0.15, 0), (0, 0))
            make_face()
            # Profile area: 0.0525, perimeter: 1
            with BuildLine():
                Line((-0.2, 0.35), (-0.2, 0))
                Line((-0.2, 0.35), (-0.35, 0.35))
                Line((-0.35, 0.35), (-0.35, 0))
                Line((-0.35, 0), (-0.2, 0))
            make_face()
        # OneSide extrude, distance=-0.75
        extrude(amount=-0.75, mode=Mode.SUBTRACT)
    return part.part


def model_24504_493cee15_0006():
    """Model: tubo prismatico"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 13.3672805878, perimeter: 12.9606404924
            Circle(2.06275)
        # OneSide extrude, distance=10
        extrude(amount=10)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 10, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.537032221, perimeter: 27.0978074335
            with BuildLine():
                CenterArc((0, 0), 2.25, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 2.06275, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 13.3672805878, perimeter: 12.9606404924
            Circle(2.06275)
        # OneSide extrude, distance=22.8
        extrude(amount=22.8, mode=Mode.ADD)
    return part.part


def model_24511_4d45ac57_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> 押し出し1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 11 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 8.82, perimeter: 15.9
            with BuildLine():
                Line((-2.1, 0.6), (-1, 0.6))
                Line((-2.1, 0), (-2.1, 0.6))
                Line((2.1, 0), (-2.1, 0))
                Line((2.1, 0.6), (2.1, 0))
                Line((1, 0.6), (2.1, 0.6))
                Line((1, 3.75), (1, 0.6))
                Line((-1, 3.75), (1, 3.75))
                Line((-1, 0.6), (-1, 3.75))
            make_face()
        # OneSide extrude, distance=1.4
        extrude(amount=1.4)
    return part.part


def model_24518_b99235fc_0002():
    """Model: Spacer"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 85.3873800097, perimeter: 99.5493268683
            with BuildLine():
                Line((-1.7525981457, -26.0397357475), (-1.7525981457, -29.8497357475))
                CenterArc((21.1090250217, -118.3857159259), 91.44, 75.5235382342, 28.9550243768)
                Line((43.9674018543, -26.0397357475), (43.9674018543, -29.8488975475))
                Line((-1.7525981457, -26.0397357475), (43.9674018543, -26.0397357475))
            make_face()
        # OneSide extrude, distance=6.35
        extrude(amount=6.35)
    return part.part


def model_24592_73276617_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 15.9043128088, perimeter: 14.1371669412
            with Locations((1, -1)):
                Circle(2.25)
        # OneSide extrude, distance=1.2
        extrude(amount=1.2)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 7.7931132763, perimeter: 9.8960168588
            with Locations((-1, 1)):
                Circle(1.575)
        # OneSide extrude, distance=7.3
        extrude(amount=7.3, mode=Mode.ADD)
    return part.part


def model_24603_a4021250_0001():
    """Model: 40x20 l=300 profile"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 23 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 2.1369911184, perimeter: 21.3699111843
            with BuildLine():
                CenterArc((0.4, 0.4), 0.4, 180, 90)
                Line((0.4, 0), (3.6, 0))
                CenterArc((3.6, 0.4), 0.4, -90, 90)
                Line((4, 0.4), (4, 1.6))
                CenterArc((3.6, 1.6), 0.4, 0, 90)
                Line((3.6, 2), (0.4, 2))
                CenterArc((0.4, 1.6), 0.4, 90, 90)
                Line((0, 1.6), (0, 0.4))
            make_face()
            with BuildLine():
                Line((0.4, 0.2), (3.6, 0.2))
                CenterArc((0.4, 0.4), 0.2, 180, 90)
                Line((0.2, 1.6), (0.2, 0.4))
                CenterArc((0.4, 1.6), 0.2, 90, 90)
                Line((3.6, 1.8), (0.4, 1.8))
                CenterArc((3.6, 1.6), 0.2, 0, 90)
                Line((3.8, 0.4), (3.8, 1.6))
                CenterArc((3.6, 0.4), 0.2, -90, 90)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=30.4
        extrude(amount=30.4)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 10 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.08, perimeter: 1.3656854249
            with BuildLine():
                Line((0, 0), (-0.4, -0.4))
                Line((0, -0.4), (-0.4, -0.4))
                Line((0, -0.4), (0, 0))
            make_face()
            # Profile area: 1.52, perimeter: 8.5656854249
            with BuildLine():
                Line((-3.6, -3.6), (0, -3.6))
                Line((-3.6, -3.6), (-4, -4))
                Line((0, -4), (-4, -4))
                Line((0, -4), (0, -3.6))
            make_face()
            # Profile area: 6.4, perimeter: 11.7254833996
            with BuildLine():
                Line((0, -0.4), (-0.4, -0.4))
                Line((-0.4, -0.4), (-3.6, -3.6))
                Line((-3.6, -3.6), (0, -3.6))
                Line((0, -3.6), (0, -0.4))
            make_face()
            # Profile area: 0.08, perimeter: 1.3656854249
            with BuildLine():
                Line((-30, -0.4), (-30.4, -0.4))
                Line((-30.4, 0), (-30, -0.4))
                Line((-30.4, -0.4), (-30.4, 0))
            make_face()
            # Profile area: 6.4, perimeter: 11.7254833996
            with BuildLine():
                Line((-30.4, -3.6), (-26.8, -3.6))
                Line((-30, -0.4), (-26.8, -3.6))
                Line((-30, -0.4), (-30.4, -0.4))
                Line((-30.4, -3.6), (-30.4, -0.4))
            make_face()
            # Profile area: 1.52, perimeter: 8.5656854249
            with BuildLine():
                Line((-30.4, -4), (-26.4, -4))
                Line((-26.8, -3.6), (-26.4, -4))
                Line((-30.4, -3.6), (-26.8, -3.6))
                Line((-30.4, -4), (-30.4, -3.6))
            make_face()
        # OneSide extrude, distance=-2
        extrude(amount=-2, mode=Mode.SUBTRACT)
    return part.part


def model_24674_faae40ed_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints, 10 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 411.5115392012, perimeter: 80.9413334214
            with BuildLine():
                Line((0, 0), (20, 0))
                Line((20, 0), (20, 7.5))
                Line((20, 7.5), (15.4706667107, 24.4037019601))
                Line((15.4706667107, 24.4037019601), (4.5293332893, 24.4037019601))
                Line((0, 7.5), (4.5293332893, 24.4037019601))
                Line((0, 0), (0, 7.5))
            make_face()
        # OneSide extrude, distance=4
        extrude(amount=4)

        # Sketch29 -> Extrude6 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.2999999374, perimeter: 6.0265491791
            with BuildLine():
                Line((-5, 3), (-3.5, 2.8000000417))
                Line((-3.5, 2.8000000417), (-2, 3))
                Line((-5, 3), (-2, 3))
            make_face()
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


def model_24692_86ddfd16_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 6 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 27.0000003874, perimeter: 24.8721360104
            with BuildLine():
                Line((0, 0), (2.5, 0))
                Line((2.5, 0), (2.5, 0.200000003))
                Line((2.5, 0.200000003), (7.5, 0.200000003))
                Line((7.5, 0.200000003), (7.5, 0))
                Line((7.5, 0), (10, 0))
                Line((10, 0), (10, 2))
                Line((10, 2), (8.0000001192, 3.0000000447))
                Line((2.0000000298, 3.0000000447), (8.0000001192, 3.0000000447))
                Line((0, 2), (2.0000000298, 3.0000000447))
                Line((0, 0), (0, 2))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch2 -> Extrude2 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 5 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.7853981634, perimeter: 4.1415926536
            with BuildLine():
                CenterArc((-1.9500000179, -1.0000000149), 0.25, 180, 180)
                Line((-2.2000000179, -1.0000000149), (-2.7000000179, -1.0000000149))
                CenterArc((-1.9500000179, -1.0000000149), 0.75, 180, 180)
                Line((-1.2000000179, -1.0000000149), (-1.7000000179, -1.0000000149))
            make_face()
            # Profile area: 14.9018252296, perimeter: 23.2853981634
            with BuildLine():
                Line((-1.2000000179, -1.0000000149), (-1.7000000179, -1.0000000149))
                Line((-1.2000000179, 8.9999999851), (-1.2000000179, -1.0000000149))
                Line((-2.7000000179, 8.9999999851), (-1.2000000179, 8.9999999851))
                Line((-2.7000000179, -1.0000000149), (-2.7000000179, 8.9999999851))
                Line((-2.2000000179, -1.0000000149), (-2.7000000179, -1.0000000149))
                CenterArc((-1.9500000179, -1.0000000149), 0.25, 0, 180)
            make_face()
        # OneSide extrude, distance=4
        extrude(amount=4)
    return part.part


def model_24712_da77fe8f_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 16.1015398492, perimeter: 14.2245533219
            Circle(2.2639079745)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


def model_24735_384e3c90_0000():
    """Model: Component1"""
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
            # Profile area: 0.1134114948, perimeter: 1.1938052084
            Circle(0.19)
        # OneSide extrude, distance=2
        extrude(amount=2, mode=Mode.ADD)
    return part.part


def model_24849_f328b6fc_0001():
    """Model: TOP_P"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.153684605, perimeter: 2.22346
            with BuildLine():
                Line((-1.0000000149, 0.3000000045), (-1.0000000149, 0.8084800045))
                Line((-1.6032500149, 0.8084800045), (-1.0000000149, 0.8084800045))
                Line((-1.6032500149, 0.6708200045), (-1.6032500149, 0.8084800045))
                Line((-1.1905000149, 0.6708200045), (-1.6032500149, 0.6708200045))
                Line((-1.1905000149, 0.3000000045), (-1.1905000149, 0.6708200045))
                Line((-1.0000000149, 0.3000000045), (-1.1905000149, 0.3000000045))
            make_face()
        # OneSide extrude, distance=4.88375
        extrude(amount=4.88375)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.8084800045, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2080478064, perimeter: 8.8327929747
            with BuildLine():
                Line((1.0000000149, 4.6292), (1.0000000149, 0.26095))
                Line((1.0000000149, 4.6292), (0.9047454821, 0.26095))
                Line((1.0000000149, 0.26095), (0.9047454821, 0.26095))
            make_face()
        # OneSide extrude, distance=-0.26499
        extrude(amount=-0.26499, mode=Mode.ADD)
    return part.part


def model_24904_6a007751_0000():
    """Model: interrutore"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 13 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.5637945327, perimeter: 4.880608582
            with BuildLine():
                Line((0.6, -1.2), (0, -1.2))
                Line((0.6, -1.1129493758), (0.6, -1.2))
                CenterArc((2.5, -0.6), 1.9680236437, 164.8918477671, 30.2163044658)
                Line((0.6, 0), (0.6, -0.0870506242))
                Line((0, 0), (0.6, 0))
                Line((0, -0.0870506242), (0, 0))
                CenterArc((-1.9, -0.6), 1.9680236437, -15.1081522329, 30.2163044658)
                Line((0, -1.2), (0, -1.1129493758))
            make_face()
            with BuildLine():
                CenterArc((0.3000000045, -1.0000000149), 0.1000000015, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0.3000000045, -0.200000003), 0.1000000015, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0314159275, perimeter: 0.6283185401
            with Locations((0.3000000045, -0.200000003)):
                Circle(0.1000000015)
            # Profile area: 0.0314159275, perimeter: 0.6283185401
            with Locations((0.3000000045, -1.0000000149)):
                Circle(0.1000000015)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3, mode=Mode.ADD)
    return part.part


def model_24904_6a007751_0002():
    """Model: punte"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1642920363, perimeter: 2.8283185401
            with BuildLine():
                Line((-0.1, 0.3), (-1, 0.3))
                Line((-0.1, 0.5), (-0.1, 0.3))
                Line((-1, 0.5), (-0.1, 0.5))
                Line((-1, 0.3), (-1, 0.5))
            make_face()
            with BuildLine():
                CenterArc((-0.200000003, 0.400000006), 0.0500000007, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-0.9000000134, 0.400000006), 0.0500000007, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.01
        extrude(amount=0.01)

        # Sketch3 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0078539819, perimeter: 0.31415927
            with Locations((-0.200000003, 0.400000006)):
                Circle(0.0500000007)
            # Profile area: 0.0078539819, perimeter: 0.31415927
            with Locations((-0.9000000134, 0.400000006)):
                Circle(0.0500000007)
        # OneSide extrude, distance=0.4
        extrude(amount=0.4, mode=Mode.ADD)
    return part.part


def model_24907_c72322ea_0001():
    """Model: Pivot v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            Circle(0.4)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.3), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            Circle(0.3)
        # OneSide extrude, distance=1.52
        extrude(amount=1.52, mode=Mode.ADD)
    return part.part


def model_24907_c72322ea_0005():
    """Model: Handle_Pivot v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 2.5446900494, perimeter: 5.6548667765
            Circle(0.9)
        # OneSide extrude, distance=0.05
        extrude(amount=0.05)

        # Sketch10 -> Extrude9 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            Circle(0.5)
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2, mode=Mode.SUBTRACT)
    return part.part


def model_24978_5081ee1e_0012():
    """Model: 212_006_008_tp v2 (4)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.7707020757, perimeter: 3.1120616826
            Circle(0.4953)
        # OneSide extrude, distance=0.6096
        extrude(amount=0.6096)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.291863508, perimeter: 1.9151148816
            Circle(0.3048)
        # OneSide extrude, distance=0.7874
        extrude(amount=0.7874, mode=Mode.ADD)
    return part.part


def model_25132_c8588afc_0005():
    """Model: crankrod v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 20 constraints, 19 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.4673119072, perimeter: 3.3703537556
            with BuildLine():
                CenterArc((-3.1, 0), 0.25, 90, 180)
                Line((-3.1, 0.6), (-3.1, 0.25))
                CenterArc((-3.1, 0), 0.6, 90, 180)
                Line((-3.1, -0.25), (-3.1, -0.6))
            make_face()
            # Profile area: 0.4673119072, perimeter: 3.3703537556
            with BuildLine():
                CenterArc((3.1, 0), 0.6, -90, 180)
                Line((3.1, 0.25), (3.1, 0.6))
                CenterArc((3.1, 0), 0.25, -90, 180)
                Line((3.1, -0.6), (3.1, -0.25))
            make_face()
            # Profile area: 2.1286416941, perimeter: 28.3017541764
            with BuildLine():
                Line((-3.1, -0.25), (-3.1, -0.6))
                Line((-3.1, -0.6), (3.1, -0.6))
                Line((3.1, -0.6), (3.1, -0.25))
                CenterArc((3.1, 0), 0.25, 90, 180)
                Line((3.1, 0.25), (3.1, 0.6))
                Line((3.1, 0.6), (-3.1, 0.6))
                Line((-3.1, 0.6), (-3.1, 0.25))
                CenterArc((-3.1, 0), 0.25, -90, 180)
            make_face()
            with BuildLine():
                Line((-2.6654561972, 0.475), (2.6667718432, 0.475))
                CenterArc((2.6667718432, 0.375), 0.1, -30.4029201107, 120.4029201107)
                CenterArc((2.6667718432, 0.375), 0.1, -51.3556608473, 20.9527407367)
                CenterArc((3.1, 0), 0.475, 141.3145279845, 77.73121018)
                CenterArc((2.6658436661, -0.375), 0.1, 32.3681658885, 16.9009112149)
                CenterArc((2.6658436661, -0.375), 0.1, -89.9999791574, 122.3681450459)
                Line((-2.6655904512, -0.475), (2.6658437025, -0.475))
                CenterArc((-2.6655903571, -0.375), 0.1, 147.005536603, 122.9944094584)
                CenterArc((-2.6655903571, -0.375), 0.1, 131.390283193, 15.61525341)
                CenterArc((-3.1, 0), 0.475, -39.1632380947, 78.393448731)
                CenterArc((-2.6654561972, 0.375), 0.1, -146.6515318337, 14.8897417909)
                CenterArc((-2.6654561972, 0.375), 0.1, 90, 123.3484681663)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0981747704, perimeter: 1.2853981634
            with BuildLine():
                Line((-3.1, 0.25), (-3.1, -0.25))
                CenterArc((-3.1, 0), 0.25, 90, 180)
            make_face()
            # Profile area: 0.0981747704, perimeter: 1.2853981634
            with BuildLine():
                CenterArc((-3.1, 0), 0.25, -90, 180)
                Line((-3.1, 0.25), (-3.1, -0.25))
            make_face()
            # Profile area: 0.0981747704, perimeter: 1.2853981634
            with BuildLine():
                CenterArc((3.1, 0), 0.25, -90, 180)
                Line((3.1, -0.25), (3.1, 0.25))
            make_face()
            # Profile area: 0.0981747704, perimeter: 1.2853981634
            with BuildLine():
                Line((3.1, -0.25), (3.1, 0.25))
                CenterArc((3.1, 0), 0.25, 90, 180)
            make_face()
            # Profile area: 3.7011794144, perimeter: 22.3552888007
            with BuildLine():
                CenterArc((-2.6654561972, 0.375), 0.1, 90, 123.3484681663)
                CenterArc((-3.1, 0), 0.475, 39.2302106364, 3.1262568507)
                CenterArc((-3.1, 0), 0.475, -39.1632380947, 78.393448731)
                CenterArc((-3.1, 0), 0.475, -42.4409421094, 3.2777040147)
                CenterArc((-2.6655903571, -0.375), 0.1, 147.005536603, 122.9944094584)
                Line((-2.6655904512, -0.475), (2.6658437025, -0.475))
                CenterArc((2.6658436661, -0.375), 0.1, -89.9999791574, 122.3681450459)
                CenterArc((3.1, 0), 0.475, -140.9542618355, 3.545766663)
                CenterArc((3.1, 0), 0.475, 141.3145279845, 77.73121018)
                CenterArc((3.1, 0), 0.475, 136.9268910575, 4.3876369271)
                CenterArc((2.6667718432, 0.375), 0.1, -30.4029201107, 120.4029201107)
                Line((-2.6654561972, 0.475), (2.6667718432, 0.475))
            make_face()
            with BuildLine():
                CenterArc((2.0000000298, 0), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1.0000000149, 0), 0.3000000045, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0, 0), 0.3000000045, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-1, 0), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-2, 0), 0.3000000045, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0000176301, perimeter: 0.0519051527
            with BuildLine():
                CenterArc((-2.6654561972, 0.375), 0.1, -146.6515318337, 14.8897417909)
                CenterArc((-3.1, 0), 0.475, 39.2302106364, 3.1262568507)
            make_face()
            # Profile area: 0.0000203263, perimeter: 0.0544269539
            with BuildLine():
                CenterArc((-2.6655903571, -0.375), 0.1, 131.390283193, 15.61525341)
                CenterArc((-3.1, 0), 0.475, -42.4409421094, 3.2777040147)
            make_face()
            # Profile area: 0.0000257511, perimeter: 0.0588931735
            with BuildLine():
                CenterArc((2.6658436661, -0.375), 0.1, 32.3681658885, 16.9009112149)
                CenterArc((3.1, 0), 0.475, -140.9542618355, 3.545766663)
            make_face()
            # Profile area: 0.0000489238, perimeter: 0.0729443189
            with BuildLine():
                CenterArc((2.6667718432, 0.375), 0.1, -51.3556608473, 20.9527407367)
                CenterArc((3.1, 0), 0.475, 136.9268910575, 4.3876369271)
            make_face()
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            with Locations((2.0000000298, 0)):
                Circle(0.3)
            # Profile area: 0.2827433472, perimeter: 1.8849556202
            with Locations((1.0000000149, 0)):
                Circle(0.3000000045)
            # Profile area: 0.2827433472, perimeter: 1.8849556202
            Circle(0.3000000045)
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            with Locations((-1, 0)):
                Circle(0.3)
            # Profile area: 0.2827433472, perimeter: 1.8849556202
            with Locations((-2, 0)):
                Circle(0.3000000045)
        # OneSide extrude, distance=0.6
        extrude(amount=0.6)

        # Sketch1 -> Extrude3 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 20 constraints, 19 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            with Locations((2.0000000298, 0)):
                Circle(0.3)
            # Profile area: 0.2827433472, perimeter: 1.8849556202
            with Locations((1.0000000149, 0)):
                Circle(0.3000000045)
            # Profile area: 0.2827433472, perimeter: 1.8849556202
            Circle(0.3000000045)
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            with Locations((-1, 0)):
                Circle(0.3)
            # Profile area: 0.2827433472, perimeter: 1.8849556202
            with Locations((-2, 0)):
                Circle(0.3000000045)
        # OneSide extrude, distance=0.6
        extrude(amount=0.6, mode=Mode.SUBTRACT)

        # Sketch1 -> Extrude4 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 20 constraints, 19 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.7011794144, perimeter: 22.3552888007
            with BuildLine():
                CenterArc((-2.6654561972, 0.375), 0.1, 90, 123.3484681663)
                CenterArc((-3.1, 0), 0.475, 39.2302106364, 3.1262568507)
                CenterArc((-3.1, 0), 0.475, -39.1632380947, 78.393448731)
                CenterArc((-3.1, 0), 0.475, -42.4409421094, 3.2777040147)
                CenterArc((-2.6655903571, -0.375), 0.1, 147.005536603, 122.9944094584)
                Line((-2.6655904512, -0.475), (2.6658437025, -0.475))
                CenterArc((2.6658436661, -0.375), 0.1, -89.9999791574, 122.3681450459)
                CenterArc((3.1, 0), 0.475, -140.9542618355, 3.545766663)
                CenterArc((3.1, 0), 0.475, 141.3145279845, 77.73121018)
                CenterArc((3.1, 0), 0.475, 136.9268910575, 4.3876369271)
                CenterArc((2.6667718432, 0.375), 0.1, -30.4029201107, 120.4029201107)
                Line((-2.6654561972, 0.475), (2.6667718432, 0.475))
            make_face()
            with BuildLine():
                CenterArc((2.0000000298, 0), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1.0000000149, 0), 0.3000000045, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0, 0), 0.3000000045, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-1, 0), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-2, 0), 0.3000000045, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.15
        extrude(amount=0.15, mode=Mode.SUBTRACT)
    return part.part


def model_25135_e643b3a2_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 7.0685834706, perimeter: 9.4247779608
            Circle(1.5)
        # OneSide extrude, distance=7
        extrude(amount=7)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 5.4977871438, perimeter: 21.9911485751
            with BuildLine():
                CenterArc((0, 0), 2, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 7.0685834706, perimeter: 9.4247779608
            Circle(1.5)
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.ADD)

        # Sketch2 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 7), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 5.4977871438, perimeter: 21.9911485751
            with BuildLine():
                CenterArc((0, 0), 2, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 7.0685834706, perimeter: 9.4247779608
            Circle(1.5)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)
    return part.part


def model_25179_1775e380_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch7 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 5.4228597762, perimeter: 23.8001502907
            with BuildLine():
                Line((3.4500000514, -1.9000000283), (5.6441341592, -3.752824386))
                CenterArc((5.6925227206, -3.6955221423), 0.075, -130.1792339219, 88.5456945853)
                Line((5.7485784195, -3.7453494303), (5.9296389176, -3.5416563699))
                CenterArc((5.7427865879, -3.3755654102), 0.25, -41.6335393366, 91.4543054147)
                Line((5.9040817924, -3.1845579312), (4.8317311028, -2.2790173488))
                Line((4.8317311028, -2.2790173488), (4.2273144537, -1.8572110428))
                CenterArc((2.4537417872, -4.3986070167), 3.0990730065, 55.0898365667, 35.9037927807)
                Line((2.4000000358, -1.3000000194), (-4.8440770608, -1.1898102895))
                Line((-4.8440770608, -1.1898102895), (-4.743153197, -1.7557676415))
                Line((-4.743153197, -1.7557676415), (2.5000000373, -1.6500000246))
                CenterArc((2.5267011007, -3.4785360123), 1.8287309275, 59.6762763441, 31.1603216389)
            make_face()
        # Symmetric extrude, each_side=4
        extrude(amount=4, both=True)

        # Sketch8 -> Extrude2 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 82.140002448, perimeter: 37.0036038626
            with BuildLine():
                Line((-3.6000000536, -5.0000000745), (-3.8000000566, 6.1000000909))
                Line((-3.6000000536, -5.0000000745), (3.6000000536, -5.0000000745))
                Line((3.6000000536, -5.0000000745), (3.8000000566, 6.1000000909))
                Line((-3.8000000566, 6.1000000909), (3.8000000566, 6.1000000909))
            make_face()
        # OneSide extrude, distance=-5
        extrude(amount=-5, mode=Mode.SUBTRACT)
    return part.part


def model_25186_e5476b73_0000():
    """Model: rączka v9"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 7.0685834706, perimeter: 9.4247779608
            Circle(1.5)
        # OneSide extrude, distance=12
        extrude(amount=12)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 4.9087385212, perimeter: 7.853981634
            Circle(1.25)
        # OneSide extrude, distance=-14
        extrude(amount=-14, mode=Mode.SUBTRACT)
    return part.part


def model_25203_1cc0cb3c_0013():
    """Model: N3 v2"""
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
        # OneSide extrude, distance=0.63
        extrude(amount=0.63)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.63, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0451603944, perimeter: 3.6128315516
            with BuildLine():
                CenterArc((0, 0), 0.3, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.275, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.03
        extrude(amount=-0.03, mode=Mode.SUBTRACT)
    return part.part


def model_25203_92cee759_0008():
    """Model: L2 v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 16 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.3330140042, perimeter: 3.1179644134
            with BuildLine():
                CenterArc((0.0000000422, 0.0001125044), 0.353, -90.0848772727, 73.6101529749)
                CenterArc((0.0000000422, 0.0001125044), 0.353, -16.4747242979, 32.8669184185)
                CenterArc((0.0000000422, 0.0001125044), 0.353, 16.3921941206, 73.5232821148)
                CenterArc((0.0000000422, 0.0001125044), 0.353, 89.9154762354, 179.9996464919)
            make_face()
            with BuildLine():
                Line((-0.0750973684, -0.1297350175), (0.0749025895, -0.1298475218))
                Line((-0.1499999156, 0.0002250087), (-0.0750973684, -0.1297350175))
                Line((-0.0749025051, 0.1300725306), (-0.1499999156, 0.0002250087))
                Line((0.0750974527, 0.1299600262), (-0.0749025051, 0.1300725306))
                Line((0.15, 0), (0.0750974527, 0.1299600262))
                Line((0.0749025895, -0.1298475218), (0.15, 0))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.44
        extrude(amount=0.44)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 16 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.3299635829, perimeter: 3.8299616985
            with BuildLine():
                CenterArc((0.0000000422, 0.0001125044), 0.353, 16.3921941206, 73.5232821148)
                Line((0.3386514505, 0.0997329023), (1.4612272701, 0.0966706341))
                CenterArc((1.7999980835, -0.0025429539), 0.353, 89.918678498, 73.7579426312)
                Line((1.8004991061, 0.3504566906), (0.000520794, 0.3531121203))
            make_face()
            # Profile area: 0.3207848843, perimeter: 3.1604422095
            with BuildLine():
                CenterArc((1.7999980835, -0.0025429539), 0.353, -90.0845494257, 180.0032279237)
                CenterArc((1.7999980835, -0.0025429539), 0.353, 89.918678498, 73.7579426312)
                CenterArc((1.7999980835, -0.0025429539), 0.353, 163.6766211292, 32.4776345427)
                CenterArc((1.7999980835, -0.0025429539), 0.353, -163.8457443281, 73.7611949024)
            make_face()
            with BuildLine():
                CenterArc((1.7999980835, -0.0025429539), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.2191150044, perimeter: 2.6475971344
            with BuildLine():
                CenterArc((1.7999980835, -0.0025429539), 0.353, 163.6766211292, 32.4776345427)
                Line((0.3386514505, 0.0997329023), (1.4612272701, 0.0966706341))
                CenterArc((0.0000000422, 0.0001125044), 0.353, -16.4747242979, 32.8669184185)
                Line((0.3385076036, -0.0999955914), (1.460935892, -0.1007561421))
            make_face()
            # Profile area: 0.3302506932, perimeter: 3.8303872469
            with BuildLine():
                CenterArc((1.7999980835, -0.0025429539), 0.353, -163.8457443281, 73.7611949024)
                Line((0.3385076036, -0.0999955914), (1.460935892, -0.1007561421))
                CenterArc((0.0000000422, 0.0001125044), 0.353, -90.0848772727, 73.6101529749)
                Line((-0.0005228875, -0.3528871083), (1.7994771736, -0.3555425695))
            make_face()
            # Profile area: 0.3330140042, perimeter: 3.1179644134
            with BuildLine():
                CenterArc((0.0000000422, 0.0001125044), 0.353, -90.0848772727, 73.6101529749)
                CenterArc((0.0000000422, 0.0001125044), 0.353, -16.4747242979, 32.8669184185)
                CenterArc((0.0000000422, 0.0001125044), 0.353, 16.3921941206, 73.5232821148)
                CenterArc((0.0000000422, 0.0001125044), 0.353, 89.9154762354, 179.9996464919)
            make_face()
            with BuildLine():
                Line((-0.0750973684, -0.1297350175), (0.0749025895, -0.1298475218))
                Line((-0.1499999156, 0.0002250087), (-0.0750973684, -0.1297350175))
                Line((-0.0749025051, 0.1300725306), (-0.1499999156, 0.0002250087))
                Line((0.0750974527, 0.1299600262), (-0.0749025051, 0.1300725306))
                Line((0.15, 0), (0.0750974527, 0.1299600262))
                Line((0.0749025895, -0.1298475218), (0.15, 0))
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((1.7999980835, -0.0025429539)):
                Circle(0.15)
            # Profile area: 0.0584567148, perimeter: 0.9
            with BuildLine():
                Line((0.0749025895, -0.1298475218), (0.15, 0))
                Line((0.15, 0), (0.0750974527, 0.1299600262))
                Line((0.0750974527, 0.1299600262), (-0.0749025051, 0.1300725306))
                Line((-0.0749025051, 0.1300725306), (-0.1499999156, 0.0002250087))
                Line((-0.1499999156, 0.0002250087), (-0.0750973684, -0.1297350175))
                Line((-0.0750973684, -0.1297350175), (0.0749025895, -0.1298475218))
            make_face()
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2, mode=Mode.ADD)

        # Sketch1 -> Extrude3 (Join)
        # Sketch on XZ construction plane
        # Sketch has 16 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.3207848843, perimeter: 3.1604422095
            with BuildLine():
                CenterArc((1.7999980835, -0.0025429539), 0.353, -90.0845494257, 180.0032279237)
                CenterArc((1.7999980835, -0.0025429539), 0.353, 89.918678498, 73.7579426312)
                CenterArc((1.7999980835, -0.0025429539), 0.353, 163.6766211292, 32.4776345427)
                CenterArc((1.7999980835, -0.0025429539), 0.353, -163.8457443281, 73.7611949024)
            make_face()
            with BuildLine():
                CenterArc((1.7999980835, -0.0025429539), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.2191150044, perimeter: 2.6475971344
            with BuildLine():
                CenterArc((1.7999980835, -0.0025429539), 0.353, 163.6766211292, 32.4776345427)
                Line((0.3386514505, 0.0997329023), (1.4612272701, 0.0966706341))
                CenterArc((0.0000000422, 0.0001125044), 0.353, -16.4747242979, 32.8669184185)
                Line((0.3385076036, -0.0999955914), (1.460935892, -0.1007561421))
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)

        # Sketch1 -> Extrude4 (Join)
        # Sketch on XZ construction plane
        # Sketch has 16 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.3207848843, perimeter: 3.1604422095
            with BuildLine():
                CenterArc((1.7999980835, -0.0025429539), 0.353, -90.0845494257, 180.0032279237)
                CenterArc((1.7999980835, -0.0025429539), 0.353, 89.918678498, 73.7579426312)
                CenterArc((1.7999980835, -0.0025429539), 0.353, 163.6766211292, 32.4776345427)
                CenterArc((1.7999980835, -0.0025429539), 0.353, -163.8457443281, 73.7611949024)
            make_face()
            with BuildLine():
                CenterArc((1.7999980835, -0.0025429539), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.59
        extrude(amount=-0.59, mode=Mode.ADD)
    return part.part


def model_25211_336c083f_0009():
    """Model: 7-Gear Housing v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 12 constraints, 11 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 118.8394080165, perimeter: 69.1141136539
            with BuildLine():
                CenterArc((0, -8), 4.6000000561, 159.8287230524, 220.3425538951)
                CenterArc((10.8885261508, -4.0000000545), 7, 159.8287428058, 40.3425242162)
                CenterArc((0, 0), 4.6000000936, -20.1712931772, 220.3425863543)
                CenterArc((-10.8885261508, -4.0000000545), 7, -20.171267022, 40.3425242162)
            make_face()
            with BuildLine():
                CenterArc((3, -4), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-3, -4), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0, 0), 1.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0, -8), 1.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.8
        extrude(amount=1.8)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1.8), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 96.8085648802, perimeter: 63.7848385717
            with BuildLine():
                CenterArc((0, -8), 4.2, 126.8698995769, 286.2602027772)
                CenterArc((3, -4), 0.8, 126.8698916719, 106.2602106822)
                CenterArc((0, 0), 4.2, -53.1301012163, 286.2602035704)
                CenterArc((-3, -4), 0.8, -53.1301124923, 106.2602148464)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0, -8), 1.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-1.6
        extrude(amount=-1.6, mode=Mode.SUBTRACT)
    return part.part


def model_25216_ff3bf7e2_0000():
    """Model: my yoke v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 7 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 38.1042619623, perimeter: 70.9044394614
            with BuildLine():
                Line((1.8, 5.8), (0.6, 5.8))
                Line((0.6, 5.8), (0.6, 1.8))
                Line((0.6, 1.8), (-0.6, 1.8))
                Line((-0.6, 1.8), (-0.6, 5.8))
                Line((-0.6, 5.8), (-1.8, 5.8))
                Line((-1.8, 1.0392304845), (-1.8, 5.8))
                Line((-1.8, 1.0392304845), (-5.9229473419, -1.3411542732))
                Line((-5.9229473419, -1.3411542732), (-5.3229473419, -2.3803847577))
                Line((-5.3229473419, -2.3803847577), (-1.8588457268, -0.3803847577))
                Line((-1.8588457268, -0.3803847577), (-1.2588457268, -1.4196152423))
                Line((-1.2588457268, -1.4196152423), (-4.7229473419, -3.4196152423))
                Line((-4.7229473419, -3.4196152423), (-4.1229473419, -4.4588457268))
                Line((0, -2.0784609691), (-4.1229473419, -4.4588457268))
                Line((0, -2.0784609691), (4.1229473419, -4.4588457268))
                Line((4.1229473419, -4.4588457268), (4.7229473419, -3.4196152423))
                Line((4.7229473419, -3.4196152423), (1.2588457268, -1.4196152423))
                Line((1.2588457268, -1.4196152423), (1.8588457268, -0.3803847577))
                Line((1.8588457268, -0.3803847577), (5.3229473419, -2.3803847577))
                Line((5.3229473419, -2.3803847577), (5.9229473419, -1.3411542732))
                Line((1.8, 1.0392304845), (5.9229473419, -1.3411542732))
                Line((1.8, 1.0392304845), (1.8, 5.8))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=3.6
        extrude(amount=3.6)
    return part.part


def model_25216_ff3bf7e2_0006():
    """Model: my spring v1 (2)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.471238898, perimeter: 9.4247779608
            with BuildLine():
                CenterArc((0, 0), 0.8, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.7, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=3.6
        extrude(amount=3.6)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(3.6, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0200600103, perimeter: 0.6030212693
            with BuildLine():
                CenterArc((0, 0), 0.7, 81.7867892084, 16.4264214933)
                Line((0.1000000012, 0.7937253932), (0.1000000011, 0.6928203229))
                CenterArc((0, 0), 0.8, 82.8192441287, 14.3615116528)
                Line((-0.1, 0.692820323), (-0.1, 0.7937253933))
            make_face()
            # Profile area: 0.0304176518, perimeter: 0.7130737744
            with BuildLine():
                Line((0.1000000015, 0.9500000142), (0.1000000012, 0.7937253932))
                Line((-0.1, 0.9500000142), (0.1000000015, 0.9500000142))
                Line((-0.1, 0.7937253933), (-0.1, 0.9500000142))
                CenterArc((0, 0), 0.8, 82.8192441287, 14.3615116528)
            make_face()
            # Profile area: 0.1395223414, perimeter: 1.7863272435
            with BuildLine():
                Line((0.1, 0), (-0.1, 0))
                Line((0.1000000011, 0.6928203229), (0.1, 0))
                CenterArc((0, 0), 0.7, 81.7867892084, 16.4264214933)
                Line((-0.1, 0), (-0.1, 0.692820323))
            make_face()
        # OneSide extrude, distance=-4
        extrude(amount=-4, mode=Mode.SUBTRACT)
    return part.part


def model_25249_dd7b7c5a_0000():
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
        # Wheel_ -> Extrude6 (NewBody)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 2.6386552641, perimeter: 5.7583261432
            with Locations((-4.3103471392, 1.1916145875)):
                Circle(0.9164660696)
        # Symmetric extrude, each_side=0.4
        extrude(amount=0.4, both=True)
    return part.part


def model_25294_84dd76e8_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 100, perimeter: 40
            with BuildLine():
                Line((10, 10), (10, 0))
                Line((0, 10), (10, 10))
                Line((0, 0), (0, 10))
                Line((10, 0), (0, 0))
            make_face()
        # OneSide extrude, distance=10
        extrude(amount=10)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 10, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 19.6349540849, perimeter: 15.7079632679
            with Locations((-5, 5)):
                Circle(2.5)
        # OneSide extrude, distance=-9
        extrude(amount=-9, mode=Mode.SUBTRACT)
    return part.part


def model_25294_96063cf2_0008():
    """Model: Bielle v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 11 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.9817477042, perimeter: 7.853981634
            with BuildLine():
                CenterArc((0, 0), 0.75, -180, 180)
                CenterArc((0, 0), 0.75, 0, 180)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=1.5
        extrude(amount=1.5, both=True)

        # Sketch1 -> Extrude2 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 11 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 5.4977871438, perimeter: 21.9911485751
            with BuildLine():
                CenterArc((0, -10), 2, 172.7849477236, 194.4301045527)
                CenterArc((0, -10), 2, 7.2150522764, 165.5698954473)
            make_face()
            with BuildLine():
                CenterArc((0, -10), 1.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=0.75
        extrude(amount=0.75, both=True)

        # Sketch1 -> Extrude3 (Join)
        # Sketch on XY construction plane
        # Sketch has 11 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 10.5244403806, perimeter: 43.9347456354
            with BuildLine():
                CenterArc((0, -10), 2, 7.2150522764, 165.5698954473)
                Line((0.75, 0), (1.9841634811, -9.7488122611))
                CenterArc((0, 0), 0.75, -180, 180)
                Line((-0.75, 0), (-1.9841634811, -9.7488122611))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.25, -113.6453926408, 47.2907852816)
                Line((0.5013436202, -1.1450565813), (1.1383006292, -7.4966479118))
                CenterArc((0, -10), 2.75, 65.5482057112, 48.9035885776)
                Line((-0.5013436202, -1.1450565813), (-1.1383006292, -7.4966479118))
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=0.5
        extrude(amount=0.5, both=True, mode=Mode.ADD)

        # Sketch1 -> Extrude4 (Join)
        # Sketch on XY construction plane
        # Sketch has 11 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 9.9657510571, perimeter: 16.1458275027
            with BuildLine():
                Line((-0.5013436202, -1.1450565813), (-1.1383006292, -7.4966479118))
                CenterArc((0, -10), 2.75, 65.5482057112, 48.9035885776)
                Line((0.5013436202, -1.1450565813), (1.1383006292, -7.4966479118))
                CenterArc((0, 0), 1.25, -113.6453926408, 47.2907852816)
            make_face()
        # Symmetric extrude, each_side=0.1
        extrude(amount=0.1, both=True, mode=Mode.ADD)
    return part.part


def model_25335_491efa81_0005():
    """Model: Loophole flushing(2) v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 27.3397100679, perimeter: 18.5353966562
            Circle(2.95)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.1), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 18.0955736847, perimeter: 15.0796447372
            Circle(2.4)
        # OneSide extrude, distance=-0.1
        extrude(amount=-0.1, mode=Mode.SUBTRACT)
    return part.part


def model_25335_491efa81_0009():
    """Model: Back switch v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 3.8013271108, perimeter: 6.9115038379
            Circle(1.1)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.2), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.904772228, perimeter: 4.6619791185
            with BuildLine():
                CenterArc((0, 0), 1.1, 76.8634412131, 26.2731175739)
                Line((0.25, 2.9), (0.25, 1.0712142643))
                Line((-0.25, 2.9), (0.25, 2.9))
                Line((-0.25, 1.0712142643), (-0.25, 2.9))
            make_face()
            # Profile area: 0.345227772, perimeter: 2.3468361756
            with BuildLine():
                Line((-0.25, 0.4), (-0.25, 1.0712142643))
                Line((0.25, 0.4), (-0.25, 0.4))
                Line((0.25, 1.0712142643), (0.25, 0.4))
                CenterArc((0, 0), 1.1, 76.8634412131, 26.2731175739)
            make_face()
        # OneSide extrude, distance=0.8
        extrude(amount=0.8, mode=Mode.ADD)
    return part.part


def model_25335_491efa81_0011():
    """Model: Bid flushing v4"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 12.5663706144, perimeter: 12.5663706144
            Circle(2)
        # OneSide extrude, distance=0.15
        extrude(amount=0.15)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.15), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1.4313881528, perimeter: 4.2411500823
            Circle(0.675)
        # OneSide extrude, distance=-0.15
        extrude(amount=-0.15, mode=Mode.SUBTRACT)
    return part.part


def model_25338_a9cdf751_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude2 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 10 constraints, 32 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.1997296748, perimeter: 10.9331950812
            with BuildLine():
                Line((3.5749997636, -0.3000000038), (3.875, -0.3000000045))
                Line((3.875, -0.3000000045), (3.8750000001, -0.2000000045))
                Line((3.8750000001, -0.2000000045), (4.2373475379, -0.200000005))
                CenterArc((3.725, -0.0000000039), 0.55, -21.323686381, 42.6473730828)
                Line((3.875, 0.2), (4.2373475368, 0.2))
                Line((3.875, 0.2999999946), (3.875, 0.2))
                Line((3.5749999991, 0.2999999958), (3.875, 0.2999999946))
                CenterArc((3.3999999984, 0.2999999968), 0.1750000007, -90.0051996579, 90.0051993195)
                Line((0.0000000001, 0.125), (3.399984117, 0.1249999969))
                CenterArc((0, 0), 0.125, 89.9999999328, 180)
                Line((-0.0000000001, -0.125), (3.4000156648, -0.1250000046))
                CenterArc((3.3999997636, -0.3000000039), 0.175, 0.0000000151, 89.9947938555)
            make_face()
            with BuildLine():
                CenterArc((4.075, -0.0000000024), 0.125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0, 0), 0.075, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.1), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.48, perimeter: 6.7
            with BuildLine():
                Line((3.5749999988, 0.0749999952), (3.5749999986, -0.0750000048))
                Line((0.3749999988, 0.0749999995), (3.5749999988, 0.0749999952))
                Line((0.3749999986, -0.0750000005), (0.3749999988, 0.0749999995))
                Line((3.5749999986, -0.0750000048), (0.3749999986, -0.0750000005))
            make_face()
        # OneSide extrude, distance=-0.025
        extrude(amount=-0.025, mode=Mode.SUBTRACT)
    return part.part


def model_25346_11e33bbb_0001():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 5.7764652617, perimeter: 37.9033153656
            with BuildLine():
                CenterArc((0, 0), 3.16865, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 2.86385, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=12.7
        extrude(amount=12.7)
    return part.part


def model_25364_b3985755_0002():
    """Model: Chute/Food Cover v41 (1)"""
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
        # Sketch has 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 35.7008253669, perimeter: 21.880822257
            Ellipse(4.15798, 2.73304)
        # OneSide extrude, distance=10.03808
        extrude(amount=10.03808)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on XY construction plane
        # Sketch has 9 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0129708537, perimeter: 0.5183854908
            with BuildLine():
                _nurbs_edge([(0, 0.1504316799), (0.0000623924, 0.1503945803), (0.0125241951, 0.1429796091), (0.0362621059, 0.1268754363), (0.0689706901, 0.0993907238), (0.0986541147, 0.0683744749), (0.1262632762, 0.0350466908), (0.1438280414, 0.0118459947), (0.1524, 0)], [1, 1, 1, 1, 1, 1, 1, 1, 1], [0.3989938521, 0.3989938521, 0.3989938521, 0.3989938521, 0.3989938521, 0.3989938521, 0.4, 0.6, 0.8, 1, 1, 1, 1, 1, 1], 5)
                Line((0, 0), (0, 0.1504316799))
                Line((0.1524, 0), (0, 0))
            make_face()
            # Profile area: 0.7901966286, perimeter: 8.6640948888
            with BuildLine():
                _nurbs_edge([(-0.1524, 0.1905), (-0.1336806099, 0.1905), (-0.0982362809, 0.1882816366), (-0.0665795389, 0.1816416876), (-0.0381892071, 0.171188569), (-0.0123398385, 0.1577691592), (0, 0.1504316799)], [1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.2, 0.3989938521, 0.3989938521, 0.3989938521, 0.3989938521, 0.3989938521, 0.3989938521], 5)
                Line((-4.15798, 0.1905), (-0.1524, 0.1905))
                Line((-4.15798, 0), (-4.15798, 0.1905))
                Line((0, 0), (-4.15798, 0))
                Line((0, 0), (0, 0.1504316799))
            make_face()
        # TwoSides extrude (symmetric), distance=3.175
        extrude(amount=3.175, both=True, mode=Mode.SUBTRACT)
    return part.part


def model_25381_9c263e4d_0005():
    """Model: Part14_MeatGrinder v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.7865924223, perimeter: 3.143980264
            Circle(0.50038)
        # OneSide extrude, distance=6.49986
        extrude(amount=6.49986)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on YZ construction plane
        # Sketch has 13 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))) as sk:
            # Profile area: 1.3534556813, perimeter: 5.9753998838
            with BuildLine():
                Line((-5.10032, -0.19939), (-6.8580002189, -0.19939))
                Line((-6.8580002189, -0.19939), (-6.8580002189, -0.7620000243))
                Line((-6.8580002189, -0.7620000243), (-4.3180001378, -0.7620000243))
                Line((-4.3180001378, -0.5080000162), (-4.3180001378, -0.7620000243))
                CenterArc((-5.10032, -1.3452771581), 1.1458871581, 46.9434541195, 43.0565458805)
            make_face()
            # Profile area: 1.3534556813, perimeter: 5.9753998838
            with BuildLine():
                Line((-6.49986, 0.19939), (-6.8580002189, 0.19939))
                Line((-5.10032, 0.19939), (-6.49986, 0.19939))
                CenterArc((-5.10032, 1.3452771581), 1.1458871581, -90, 43.0565458805)
                Line((-4.3180001378, 0.5080000162), (-4.3180001378, 0.7620000243))
                Line((-6.8580002189, 0.7620000243), (-4.3180001378, 0.7620000243))
                Line((-6.8580002189, 0.19939), (-6.8580002189, 0.7620000243))
            make_face()
        # TwoSides extrude, along=0.889, against=-1.016
        extrude(amount=0.889, mode=Mode.SUBTRACT)
        extrude(sk.sketch, amount=-1.016, mode=Mode.SUBTRACT)
    return part.part


def model_25381_9c263e4d_0008():
    """Model: Part15_MeatGrinder v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 9.5103926752, perimeter: 10.932114116
            Circle(1.7399)
        # OneSide extrude, distance=0.70104
        extrude(amount=0.70104)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.70104, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.5027804961, perimeter: 2.5135882821
            Circle(0.40005)
        # OneSide extrude, distance=-0.29972
        extrude(amount=-0.29972, mode=Mode.SUBTRACT)
    return part.part


def model_25387_9dc6258b_0004():
    """Model: Hex Head Machine Screw v1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2832735494, perimeter: 1.9812
            with BuildLine():
                Line((0.2859615883, -0.1651), (0.2859615883, 0.1651))
                Line((0.2859615883, 0.1651), (0, 0.3302))
                Line((0, 0.3302), (-0.2859615883, 0.1651))
                Line((-0.2859615883, 0.1651), (-0.2859615883, -0.1651))
                Line((-0.2859615883, -0.1651), (0, -0.3302))
                Line((0, -0.3302), (0.2859615883, -0.1651))
            make_face()
        # OneSide extrude, distance=0.254
        extrude(amount=0.254)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.0791730436, perimeter: 0.9974556675
            Circle(0.15875)
        # OneSide extrude, distance=2.6035
        extrude(amount=2.6035, mode=Mode.ADD)
    return part.part


def model_25416_a2472889_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 10.1787601976, perimeter: 33.9292006588
            with BuildLine():
                CenterArc((0, 0), 3, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 2.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.4
        extrude(amount=0.4)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0.4, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0314159275, perimeter: 0.6283185401
            with Locations((0, 2.7000000402)):
                Circle(0.1000000015)
        # OneSide extrude, distance=-0.8
        extrude(amount=-0.8, mode=Mode.ADD)
    return part.part


def model_25416_b70bf79a_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0739781348, perimeter: 1.8367815846
            with BuildLine():
                Line((0.1007052545, 0.1744266174), (-0.1007052545, 0.1744266174))
                Line((-0.1007052545, 0.1744266174), (-0.201410509, 0))
                Line((-0.201410509, 0), (-0.1007052545, -0.1744266174))
                Line((-0.1007052545, -0.1744266174), (0.1007052545, -0.1744266174))
                Line((0.1007052545, -0.1744266174), (0.201410509, 0))
                Line((0.201410509, 0), (0.1007052545, 0.1744266174))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)
    return part.part


def model_25559_893f0c7c_0004():
    """Model: pokretlo1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 19.6349540849, perimeter: 15.7079632679
            Circle(2.5)
        # OneSide extrude, distance=10
        extrude(amount=10)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            Circle(0.5)
        # OneSide extrude, distance=-2
        extrude(amount=-2, mode=Mode.SUBTRACT)
    return part.part


def model_25560_7660b86f_0005():
    """Model: podstawa"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 78.5398163397, perimeter: 31.4159265359
            Circle(5)
        # Symmetric extrude, each_side=6
        extrude(amount=6, both=True)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 19.6349540849, perimeter: 15.7079632679
            Circle(2.5)
        # Symmetric extrude, each_side=20
        extrude(amount=20, both=True, mode=Mode.ADD)
    return part.part


def model_25560_7660b86f_0008():
    """Model: przedramie_l"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 7 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1167.8199262355, perimeter: 162.8901384102
            with BuildLine():
                Line((25, 10), (-25, 10))
                Line((-25, 10), (-25, -10))
                Line((41.7819926235, -10), (-25, -10))
                Line((25, 10), (41.7819926235, -10))
            make_face()
        # OneSide extrude, distance=22.5
        extrude(amount=22.5)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 16.4418560243, -19.5946409859), x_dir=(-1, 0, 0), z_dir=(0, 0.6427876097, -0.7660444431))):
            # Profile area: 3.8013271108, perimeter: 6.9115038379
            with Locations((-11.25, -21.4633187043)):
                Circle(1.1)
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.SUBTRACT)
    return part.part


def model_25839_fac364bf_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 7.52, perimeter: 12.6
            with BuildLine():
                Line((0, 0), (-4.7, 0))
                Line((0, 1.6), (0, 0))
                Line((-4.7, 1.6), (0, 1.6))
                Line((-4.7, 0), (-4.7, 1.6))
            make_face()
        # OneSide extrude, distance=0.6
        extrude(amount=0.6)

        # Sketch3 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-4.7, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.2515551576, perimeter: 2.4045894684
            with BuildLine():
                Line((-1.3174315781, 0.31), (-1.15, 0.6))
                Line((-1.3174315781, 0.31), (-0.2825684219, 0.31))
                Line((-0.2825684219, 0.31), (-0.45, 0.6))
                Line((-0.45, 0.6), (-1.15, 0.6))
            make_face()
        # OneSide extrude, distance=-4.7
        extrude(amount=-4.7, mode=Mode.SUBTRACT)
    return part.part


def model_26086_bf892d7f_0010():
    """Model: Tractor_Lift_Arm_Mount v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 12 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 719.7590968894, perimeter: 140.6514731271
            with BuildLine():
                Line((41.3093568272, 18.0972007347), (52, 12))
                CenterArc((38.8322579774, 13.7539322318), 5, 60.3025657484, 56)
                Line((25.0473016236, 12.5176670579), (36.6167012988, 18.2362651739))
                CenterArc((22.831744945, 17), 5, -90, 26.3025657484)
                Line((0, 12), (22.831744945, 12))
                Line((0, 0), (0, 12))
                Line((52, 0), (0, 0))
                Line((52, 12), (52, 0))
            make_face()
            with BuildLine():
                CenterArc((38.8322579774, 14), 1.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=14.5
        extrude(amount=14.5, both=True)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 14.5), x_dir=(1, 0, 0), z_dir=(0, 0, 1))) as sk:
            # Profile area: 99.2037303913, perimeter: 72.3931932353
            with BuildLine():
                CenterArc((2.1205827889, 20.8346407127), 2, 44.2192305555, 135)
                Line((0, 12), (0.120768481, 20.8618938643))
                Line((22.831744945, 12), (0, 12))
                CenterArc((22.831744945, 17), 5, -90, 26.3025657484)
                Line((26.0392711739, 13.0079842188), (25.0473016236, 12.5176670579))
                Line((12.3458516413, 13.1945959637), (26.0392711739, 13.0079842188))
                Line((3.5539359353, 22.2294520826), (12.3458516413, 13.1945959637))
            make_face()
            with BuildLine():
                CenterArc((4.8328543787, 18.0474229561), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((2.1205827889, 20.8346407127), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # TwoSides offset extrude, full=-11.5, trim=-9.5
        extrude(amount=-11.5, mode=Mode.ADD)
        extrude(sk.sketch, amount=-9.5, mode=Mode.SUBTRACT)
    return part.part


def model_26086_bf892d7f_0023():
    """Model: Tractor_DashBoard v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 11 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 2201, perimeter: 191.4186414203
            with BuildLine():
                Line((14, 0), (-14, 0))
                Line((14, 0), (14, 14))
                Line((14, 14), (25, 20))
                Line((25, 20), (25, 50))
                Line((25, 50), (0, 53))
                Line((-25, 50), (0, 53))
                Line((-25, 20), (-25, 50))
                Line((-14, 14), (-25, 20))
                Line((-14, 0), (-14, 14))
            make_face()
        # OneSide extrude, distance=-16
        extrude(amount=-16)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(25, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 22.641509434, perimeter: 42.3919024198
            with BuildLine():
                Line((13.7358490566, 20), (16, 20))
                Line((16, 0), (13.7358490566, 20))
                Line((16, 20), (16, 0))
            make_face()
            # Profile area: 118.8679245283, perimeter: 68.1161555164
            with BuildLine():
                Line((13.7358490566, 20), (10.3396226415, 50))
                Line((13.7358490566, 20), (16, 20))
                Line((16, 50), (16, 20))
                Line((16, 50), (10.3396226415, 50))
            make_face()
            # Profile area: 17.4905660377, perimeter: 17.6795400799
            with BuildLine():
                Line((16, 50), (10.3396226415, 50))
                Line((16, 53), (16, 50))
                Line((10, 53), (16, 53))
                Line((10.3396226415, 50), (10, 53))
            make_face()
        # OneSide extrude, distance=-57.5
        extrude(amount=-57.5, mode=Mode.SUBTRACT)
    return part.part


def model_26086_bf892d7f_0027():
    """Model: Tractor_Front_Grill v6"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 8 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 3665, perimeter: 243.9587132481
            with BuildLine():
                Line((25, 0), (-25, 0))
                Line((25, 0), (25, 71.8))
                Line((25, 71.8), (0, 74.8))
                Line((-25, 71.8), (0, 74.8))
                Line((-25, 0), (-25, 71.8))
            make_face()
        # OneSide extrude, distance=-27
        extrude(amount=-27)

        # Sketch15 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(25, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 246, perimeter: 95.7200187266
            with BuildLine():
                Line((15, 0.0006852456), (27, 0.0006852456))
                Line((27, 0.0006852456), (27, 41.0006852456))
                Line((27, 41.0006852456), (15, 0.0006852456))
            make_face()
            # Profile area: 492.7890360705, perimeter: 93.5986295088
            with BuildLine():
                Line((27, 71.8), (27, 41.0006852456))
                Line((27, 71.8), (11, 71.8))
                Line((11, 71.8), (11, 41.0006852456))
                Line((27, 41.0006852456), (11, 41.0006852456))
            make_face()
            # Profile area: 79.3815153108, perimeter: 41.9226894138
            with BuildLine():
                Line((27, 71.8), (11, 71.8))
                Line((27, 76.7613447069), (27, 71.8))
                Line((27, 76.7613447069), (11, 76.7613447069))
                Line((11, 76.7613447069), (11, 71.8))
            make_face()
        # OneSide extrude, distance=-75
        extrude(amount=-75, mode=Mode.SUBTRACT)
    return part.part


def model_26243_b080f743_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch73 -> Extrude26 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 50, perimeter: 30
            with BuildLine():
                Line((60, 90), (60, 85))
                Line((60, 85), (70, 85))
                Line((70, 85), (70, 90))
                Line((70, 90), (60, 90))
            make_face()
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)

        # Sketch74 -> Extrude28 (Cut)
        # Sketch on BRepFace
        # Sketch has 16 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(1.5, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 9, perimeter: 12
            with BuildLine():
                Line((64, 86), (61, 86))
                Line((64, 89), (64, 86))
                Line((61, 89), (64, 89))
                Line((61, 86), (61, 89))
            make_face()
            # Profile area: 2.2918446792, perimeter: 8.5192745093
            with BuildLine():
                Line((68.3567464853, 88.3682743958), (64.7288348348, 88.3682743958))
                Line((68.3567464853, 89), (68.3567464853, 88.3682743958))
                Line((64.7288348348, 89), (68.3567464853, 89))
                Line((64.7288348348, 88.3682743958), (64.7288348348, 89))
            make_face()
            # Profile area: 2.1640784339, perimeter: 8.4488393622
            with BuildLine():
                Line((68.3567464853, 87.2436975537), (64.7288348348, 87.2436975537))
                Line((68.3567464853, 87.8402055844), (68.3567464853, 87.2436975537))
                Line((64.7288348348, 87.8402055844), (68.3567464853, 87.8402055844))
                Line((64.7288348348, 87.2436975537), (64.7288348348, 87.8402055844))
            make_face()
            # Profile area: 2.2911214784, perimeter: 8.5188758221
            with BuildLine():
                Line((64.7288348348, 86.6374107029), (64.7288348348, 86.0058844424))
                Line((64.7288348348, 86.0058844424), (68.3567464853, 86.0058844424))
                Line((68.3567464853, 86.0058844424), (68.3567464853, 86.6374107029))
                Line((68.3567464853, 86.6374107029), (64.7288348348, 86.6374107029))
            make_face()
        # OneSide extrude, distance=-0.05
        extrude(amount=-0.05, mode=Mode.SUBTRACT)
    return part.part


def model_26384_83eddf22_0007():
    """Model: Contra-piston v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.2667686977, perimeter: 3.9898226701
            Circle(0.635)
        # OneSide extrude, distance=0.889
        extrude(amount=0.889)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.889, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.0721930258, perimeter: 3.6706368565
            Circle(0.5842)
        # OneSide extrude, distance=-0.635
        extrude(amount=-0.635, mode=Mode.SUBTRACT)
    return part.part


def model_26384_83eddf22_0022():
    """Model: 4-40x1/4 Allen Head Screw v2 (7)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0247728404, perimeter: 0.5579468553
            Circle(0.0888)
        # OneSide extrude, distance=0.635
        extrude(amount=0.635)

        # Sketch2 -> Extrude2 (NewBody)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.635, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0714384346, perimeter: 1.657504284
            with BuildLine():
                CenterArc((0, 0), 0.175, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.0888, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.15
        extrude(amount=0.15)
    return part.part


def model_26384_83eddf22_0027():
    """Model: 4-40 Allen Head 1.25in long v3 (3)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0791730436, perimeter: 0.9974556675
            Circle(0.15875)
        # OneSide extrude, distance=3.175
        extrude(amount=3.175)

        # Sketch2 -> Extrude2 (NewBody)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 3.175, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1171764972, perimeter: 2.5682519943
            with BuildLine():
                CenterArc((0, 0), 0.25, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.15875, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)
    return part.part


def model_26384_83eddf22_0030():
    """Model: Piston v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.2667686977, perimeter: 3.9898226701
            Circle(0.635)
        # OneSide extrude, distance=-1.5875
        extrude(amount=-1.5875)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on YZ construction plane
        # Sketch has 3 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))) as sk:
            # Profile area: 0.1233123321, perimeter: 1.2448246731
            with Locations((0, -0.6985)):
                Circle(0.19812)
        # TwoSides extrude, along=1.4, against=-1.7
        extrude(amount=1.4, mode=Mode.SUBTRACT)
        extrude(sk.sketch, amount=-1.7, mode=Mode.SUBTRACT)
    return part.part


def model_26388_a3367cba_0000():
    """Model: bague.SLDPRT"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.3769911184, perimeter: 3.7699111843
            with BuildLine():
                CenterArc((0, 0), 0.4, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=2.25
        extrude(amount=2.25)
    return part.part


def model_26388_a3367cba_0004():
    """Model: joint.SLDPRT"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 45 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.3346613913, perimeter: 7.5585755368
            with BuildLine():
                Line((0, 0.5229), (0, 0.3))
                Line((0, 0.5229), (-3.3945451379, 0.5229))
                CenterArc((-4, 0), 0.8, 0, 40.8154722198)
                Line((-1.3, 0), (-3.2, 0))
                CenterArc((-1, 0), 0.3, 90, 90)
                Line((-1, 0.3), (0, 0.3))
            make_face()
            # Profile area: 0.9231984925, perimeter: 7.1972975955
            with BuildLine():
                Line((0, -0.3), (0, -0.4))
                Line((0, -0.4), (3.307179677, -0.4))
                CenterArc((4, 0), 0.8, 180, 30)
                Line((1.3, 0), (3.2, 0))
                CenterArc((1, 0), 0.3, -90, 90)
                Line((1, -0.3), (0, -0.3))
            make_face()
            # Profile area: 0.9231984925, perimeter: 7.1972975955
            with BuildLine():
                Line((-1.3, 0), (-3.2, 0))
                CenterArc((-4, 0), 0.8, -30, 30)
                Line((0, -0.4), (-3.307179677, -0.4))
                Line((0, -0.3), (0, -0.4))
                Line((-1, -0.3), (0, -0.3))
                CenterArc((-1, 0), 0.3, 180, 90)
            make_face()
            # Profile area: 1.3346613913, perimeter: 7.5585755368
            with BuildLine():
                Line((1, 0.3), (0, 0.3))
                CenterArc((1, 0), 0.3, 0, 90)
                Line((1.3, 0), (3.2, 0))
                CenterArc((4, 0), 0.8, 139.1845277802, 40.8154722198)
                Line((0, 0.5229), (3.3945451379, 0.5229))
                Line((0, 0.5229), (0, 0.3))
            make_face()
        # Symmetric extrude, each_side=0.15
        extrude(amount=0.15, both=True)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 45 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.9071348787, perimeter: 4.3986722863
            with BuildLine():
                CenterArc((4, 0), 0.25, -90, 180)
                Line((4, -0.25), (4, -0.8))
                CenterArc((4, 0), 0.8, -90, 180)
                Line((4, 0.25), (4, 0.8))
            make_face()
            # Profile area: 1.8746997463, perimeter: 9.6402179628
            with BuildLine():
                Line((-3.2, 0), (-3.8, 0))
                CenterArc((-4, 0), 0.2, -90, 90)
                Line((-4, -0.2), (-4, -0.8))
                Line((-4, -0.8), (0, -0.8))
                Line((0, -0.4), (0, -0.8))
                Line((0, -0.4), (-3.307179677, -0.4))
                CenterArc((-4, 0), 0.8, -30, 30)
            make_face()
            # Profile area: 0.9424777961, perimeter: 4.3415926536
            with BuildLine():
                CenterArc((-4, 0), 0.8, 90, 180)
                Line((-4, -0.2), (-4, -0.8))
                CenterArc((-4, 0), 0.2, 90, 180)
                Line((-4, 0.8), (-4, 0.2))
            make_face()
            # Profile area: 1.4632368475, perimeter: 9.7556959041
            with BuildLine():
                Line((0, 0.8), (0, 0.5229))
                Line((-4, 0.8), (0, 0.8))
                Line((-4, 0.8), (-4, 0.2))
                CenterArc((-4, 0), 0.2, 0, 90)
                Line((-3.2, 0), (-3.8, 0))
                CenterArc((-4, 0), 0.8, 0, 40.8154722198)
                Line((0, 0.5229), (-3.3945451379, 0.5229))
            make_face()
            # Profile area: 1.8570282876, perimeter: 9.6187577791
            with BuildLine():
                CenterArc((4, 0), 0.8, 180, 30)
                Line((0, -0.4), (3.307179677, -0.4))
                Line((0, -0.4), (0, -0.8))
                Line((4, -0.8), (0, -0.8))
                Line((4, -0.25), (4, -0.8))
                CenterArc((4, 0), 0.25, -180, 90)
                Line((3.2, 0), (3.75, 0))
            make_face()
            # Profile area: 1.4455653888, perimeter: 9.7342357204
            with BuildLine():
                Line((0, 0.5229), (3.3945451379, 0.5229))
                CenterArc((4, 0), 0.8, 139.1845277802, 40.8154722198)
                Line((3.2, 0), (3.75, 0))
                CenterArc((4, 0), 0.25, 90, 90)
                Line((4, 0.25), (4, 0.8))
                Line((4, 0.8), (0, 0.8))
                Line((0, 0.8), (0, 0.5229))
            make_face()
        # Symmetric extrude, each_side=0.2
        extrude(amount=0.2, both=True, mode=Mode.ADD)

        # Sketch2 -> Extrude3 (Cut)
        # Sketch on XY construction plane
        # Sketch has 5 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.8000000173, perimeter: 8.4000001729
            with BuildLine():
                Line((5.8000000864, -0.1), (1.8, -0.1))
                Line((5.8000000864, 0.1), (5.8000000864, -0.1))
                Line((1.8, 0.1), (5.8000000864, 0.1))
                Line((1.8, -0.1), (1.8, 0.1))
            make_face()
        # Symmetric extrude, each_side=-2.4
        extrude(amount=-2.4, both=True, mode=Mode.SUBTRACT)
    return part.part


def model_26410_13c212a5_0002():
    """Model: Bearing Screw"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            Circle(0.2)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0346410162, perimeter: 0.692820323
            with BuildLine():
                Line((-0.1, -0.0577350269), (0, -0.1154700538))
                Line((0, -0.1154700538), (0.1, -0.0577350269))
                Line((0.1, -0.0577350269), (0.1, 0.0577350269))
                Line((0.1, 0.0577350269), (0, 0.1154700538))
                Line((0, 0.1154700538), (-0.1, 0.0577350269))
                Line((-0.1, 0.0577350269), (-0.1, -0.0577350269))
            make_face()
        # OneSide extrude, distance=-0.15
        extrude(amount=-0.15, mode=Mode.SUBTRACT)
    return part.part


def model_26764_ab35159a_0001():
    """Model: Section"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 37 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.19, perimeter: 7.4283185307
            with BuildLine():
                CenterArc((0.45, -0.45), 0.05, -90, 90)
                Line((0.5, -0.45), (0.5, 0.45))
                CenterArc((0.45, 0.45), 0.05, 0, 90)
                Line((0.45, 0.5), (-0.45, 0.5))
                CenterArc((-0.45, 0.45), 0.05, 90, 90)
                Line((-0.5, 0.45), (-0.5, -0.45))
                CenterArc((-0.45, -0.45), 0.05, 180, 90)
                Line((-0.45, -0.5), (0.45, -0.5))
            make_face()
            with BuildLine():
                Line((-0.4, -0.45), (0.4, -0.45))
                CenterArc((-0.4, -0.4), 0.05, 180, 90)
                Line((-0.45, 0.4), (-0.45, -0.4))
                CenterArc((-0.4, 0.4), 0.05, 90, 90)
                Line((0.4, 0.45), (-0.4, 0.45))
                CenterArc((0.4, 0.4), 0.05, 0, 90)
                Line((0.45, -0.4), (0.45, 0.4))
                CenterArc((0.4, -0.4), 0.05, -90, 90)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=36.5
        extrude(amount=36.5)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.5, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((0, 0.400000006)):
                Circle(0.15)
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((0, 36.1000005379)):
                Circle(0.15)
        # OneSide extrude, distance=-2
        extrude(amount=-2, mode=Mode.SUBTRACT)
    return part.part


def model_26764_ab35159a_0008():
    """Model: Positioning block"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 15 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.0085724154, perimeter: 6.765995243
            with BuildLine():
                CenterArc((0, -0.5099999886), 0.0499999989, 180, 180)
                Line((0.0499999989, -0.5099999886), (0.0499999989, -0.4974937187))
                CenterArc((0, 0), 0.5, -84.2608296514, 84.2608292246)
                Line((0.5000000067, 0.9000000142), (0.5, -0.0000000037))
                CenterArc((0.4000000067, 0.9000000149), 0.1, -0.0000004269, 90.0000004269)
                Line((-0.4000000067, 1.0000000149), (0.4000000067, 1.0000000149))
                CenterArc((-0.4000000067, 0.9000000149), 0.1, 90, 90.0000004269)
                Line((-0.5000000067, 0.9000000142), (-0.5, -0.0000000037))
                CenterArc((0, 0), 0.5, -179.9999995731, 84.2608292246)
                Line((-0.0499999989, -0.5099999886), (-0.0499999989, -0.4974937187))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.35, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.2
        extrude(amount=1.2)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.5, -0.0000000037, 0), x_dir=(0, 0, -1), z_dir=(1, -0.0000000075, 0))):
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((-0.6000000089, 0.6000000089)):
                Circle(0.15)
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.SUBTRACT)
    return part.part


def model_26766_1aaa348c_0000():
    """Model: Component11"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 0.1964795135, perimeter: 1.65
            with BuildLine():
                Line((0.1375, 0.238156986), (0.275, 0))
                Line((-0.1375, 0.238156986), (0.1375, 0.238156986))
                Line((-0.275, 0), (-0.1375, 0.238156986))
                Line((-0.1375, -0.238156986), (-0.275, 0))
                Line((0.1375, -0.238156986), (-0.1375, -0.238156986))
                Line((0.275, 0), (0.1375, -0.238156986))
            make_face()
        # OneSide extrude, distance=0.313
        extrude(amount=0.313)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            Circle(0.15)
        # OneSide extrude, distance=2
        extrude(amount=2, mode=Mode.ADD)
    return part.part


def model_26768_c4df841f_0008():
    """Model: Pieza 8"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 13 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 48.4577396762, perimeter: 43.9025658741
            with BuildLine():
                Line((2.8999999836, 1.9999999985), (2.8999999836, 1.7999999985))
                Line((2.3949874207, 1.7999999985), (2.8999999836, 1.7999999985))
                CenterArc((1.3999999836, 1.8999999985), 1, -174.2608295227, 168.5216590455)
                Line((-1.1000000164, 1.7999999985), (0.4050125465, 1.7999999985))
                Line((-1.1000000164, -0.1000000015), (-1.1000000164, 1.7999999985))
                Line((11.8999999836, -0.1000000015), (-1.1000000164, -0.1000000015))
                Line((11.8999999836, 3.8999999985), (11.8999999836, -0.1000000015))
                Line((-1.1000000164, 3.8999999985), (11.8999999836, 3.8999999985))
                Line((-1.1000000164, 1.9999999985), (-1.1000000164, 3.8999999985))
                Line((-1.1000000164, 1.9999999985), (0.4050125465, 1.9999999985))
                CenterArc((1.3999999836, 1.8999999985), 1, 5.7391704773, 168.5216590455)
                Line((2.3949874207, 1.9999999985), (2.8999999836, 1.9999999985))
            make_face()
        # OneSide extrude, distance=3
        extrude(amount=3)
    return part.part


def model_26768_c4df841f_0012():
    """Model: Pieza 7"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 3 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 3.13, perimeter: 9.8
            with BuildLine():
                Line((1.5058364722, 2.4694466265), (1.5058364722, -0.1305533735))
                Line((1.5058364722, -0.1305533735), (2.3058364722, -0.1305533735))
                Line((2.3058364722, -0.1305533735), (2.3058364722, 3.9694466265))
                Line((2.3058364722, 3.9694466265), (1.6058364722, 3.9694466265))
                Line((1.6058364722, 3.9694466265), (1.6058364722, 2.4694466265))
                Line((1.6058364722, 2.4694466265), (1.5058364722, 2.4694466265))
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(2.3058364722, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.138544236, perimeter: 1.3194689145
            with Locations((-0.35, 2.8194466265)):
                Circle(0.21)
            # Profile area: 0.138544236, perimeter: 1.3194689145
            with Locations((-1.65, 2.8194466265)):
                Circle(0.21)
        # OneSide extrude, distance=-0.7
        extrude(amount=-0.7, mode=Mode.SUBTRACT)
    return part.part


def model_26768_c4df841f_0016():
    """Model: Pieza 2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 8 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 47.7577886746, perimeter: 26.9051075294
            with BuildLine():
                Line((0, 0), (0, 8.5))
                Line((0, 8.5), (-4, 8.5))
                Line((-4, 8.5), (-6, 6.5))
                Line((-6, 1.5762051424), (-6, 6.5))
                Line((-4.4237948576, 0), (-6, 1.5762051424))
                Line((0, 0), (-4.4237948576, 0))
            make_face()
        # OneSide extrude, distance=4
        extrude(amount=4)
    return part.part


def model_26768_c4df841f_0017():
    """Model: Pasador 3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            Circle(1)
        # OneSide extrude, distance=5.6
        extrude(amount=5.6)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.5393804003, perimeter: 4.398229715
            Circle(0.7)
        # OneSide extrude, distance=-5.4
        extrude(amount=-5.4, mode=Mode.ADD)
    return part.part


def model_26768_c4df841f_0019():
    """Model: Pasador"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 2.3778714795, perimeter: 5.4663712172
            Circle(0.87)
        # Symmetric extrude, each_side=4.63
        extrude(amount=4.63, both=True)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.7637211741, perimeter: 11.7495565244
            with BuildLine():
                CenterArc((0, 0), 1, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.87, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=4.5
        extrude(amount=4.5, both=True, mode=Mode.ADD)

        # Sketch2 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(-4.63, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.7637211741, perimeter: 11.7495565244
            with BuildLine():
                CenterArc((0, 0), 1, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.87, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 2.3778714795, perimeter: 5.4663712172
            Circle(0.87)
        # OneSide extrude, distance=3.6
        extrude(amount=3.6, mode=Mode.ADD)
    return part.part


def model_26773_35d26b3c_0012():
    """Model: Rail"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            Circle(0.4)
        # Symmetric extrude, each_side=3.175
        extrude(amount=3.175, both=True)

        # Sketch7 -> Extrude4 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1118238045, perimeter: 1.727295218
            with BuildLine():
                CenterArc((0, -3.475), 0.5, 36.8698976458, 106.2602047083)
                Line((-0.4, -3.175), (0.4, -3.175))
            make_face()
            # Profile area: 0.1118238045, perimeter: 1.727295218
            with BuildLine():
                CenterArc((0, 3.475), 0.5, -143.1301023542, 106.2602047083)
                Line((-0.4, 3.175), (0.4, 3.175))
            make_face()
        # Symmetric extrude, each_side=0.7
        extrude(amount=0.7, both=True, mode=Mode.SUBTRACT)
    return part.part


def model_26942_279de65e_0006():
    """Model: Hub v1 (1)"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))) as sk:
            # Profile area: 44.1786466911, perimeter: 23.5619449019
            with Locations((-7.5, 0)):
                Circle(3.75)
        # TwoSides extrude, along=8, against=-9
        extrude(amount=8)
        extrude(sk.sketch, amount=-9)
    return part.part


def model_26942_279de65e_0007():
    """Model: Body Frame - 2 v4"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 12 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 22.9226215564, perimeter: 62.626990817
            with BuildLine():
                Line((35, -9.25), (40.3, -9.25))
                Line((35, -9.25), (35, -10))
                Line((35, -10), (40.3, -10))
                CenterArc((40.3, -9), 1, -90, 90)
                Line((41.3, 9), (41.3, -9))
                CenterArc((40.3, 9), 1, 0, 90)
                Line((40.3, 10), (35, 10))
                Line((35, 10), (35, 9.25))
                Line((40.3, 9.25), (35, 9.25))
                CenterArc((40.3, 9), 0.25, 0, 90)
                Line((40.55, 9), (40.55, -9))
                CenterArc((40.3, -9), 0.25, -90, 90)
            make_face()
        # Symmetric extrude, each_side=140
        extrude(amount=140, both=True)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 140, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 6.25, perimeter: 12.5
            with BuildLine():
                Line((-41.3, -7.75), (-41.3, -9))
                Line((-46.3, -7.75), (-41.3, -7.75))
                Line((-46.3, -9), (-46.3, -7.75))
                Line((-41.3, -9), (-46.3, -9))
            make_face()
        # OneSide extrude, distance=-100
        extrude(amount=-100, mode=Mode.ADD)
    return part.part


def model_26942_279de65e_0009():
    """Model: Body Frame - 1 v5"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 17 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 20.4279930126, perimeter: 55.9746480336
            with BuildLine():
                Line((47.3, -8.25), (42.6630856958, -8.25))
                Line((42.6630856958, -8.25), (42.6630856958, -9))
                Line((47.3, -9), (42.6630856958, -9))
                CenterArc((47.3, -8), 1, -90, 90)
                Line((48.3, 8), (48.3, -8))
                CenterArc((47.3, 8), 1, 0, 90)
                Line((47.3, 9), (42.6630856958, 9))
                Line((42.6630856958, 9), (42.6630856958, 8.25))
                Line((47.3, 8.25), (42.6630856958, 8.25))
                CenterArc((47.3, 8), 0.25, 0, 90)
                Line((47.55, 8), (47.55, -8))
                CenterArc((47.3, -8), 0.25, -90, 90)
            make_face()
        # Symmetric extrude, each_side=140
        extrude(amount=140, both=True)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 9), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 90, perimeter: 49
            with BuildLine():
                Line((47.1630856958, 140), (47.1630856958, 120))
                Line((42.6630856958, 140), (47.1630856958, 140))
                Line((42.6630856958, 120), (42.6630856958, 140))
                Line((47.1630856958, 120), (42.6630856958, 120))
            make_face()
        # OneSide extrude, distance=-5
        extrude(amount=-5, mode=Mode.SUBTRACT)
    return part.part


def model_26942_279de65e_0014():
    """Model: Air Outlet v3"""
    with BuildPart() as part:
        # Sketch4 -> Extrude2 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))) as sk:
            # Profile area: 39.4662577107, perimeter: 105.2433538953
            with BuildLine():
                CenterArc((-20, 0), 8.75, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-20, 0), 8, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # TwoSides offset extrude, full=72.5, trim=2.5
        extrude(amount=72.5)
        extrude(sk.sketch, amount=2.5, mode=Mode.SUBTRACT)
    return part.part


def model_27054_342fcf5c_0014():
    """Model: 15 - Washer v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 93 constraints, 28 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 7.2089244201, perimeter: 31.6822710581
            with BuildLine():
                CenterArc((0, 0), 2.1708293346, 127.9434718106, 14.1130563788)
                Line((-2.0583647797, 1.5348076211), (-1.7119546181, 1.3348076211))
                Line((-2.3583647797, 1.0151923789), (-2.0583647797, 1.5348076211))
                Line((-2.0119546181, 0.8151923789), (-2.3583647797, 1.0151923789))
                CenterArc((0, 0), 2.1708293346, 157.9434718106, 44.1130563788)
                Line((-2.3583647797, -1.0151923789), (-2.0119546181, -0.8151923789))
                Line((-2.0583647797, -1.5348076211), (-2.3583647797, -1.0151923789))
                Line((-1.7119546181, -1.3348076211), (-2.0583647797, -1.5348076211))
                CenterArc((0, 0), 2.1708293346, -142.0565281894, 14.1130563788)
                Line((-1.5348076211, -2.0583647797), (-1.3348076211, -1.7119546181))
                Line((-1.0151923789, -2.3583647797), (-1.5348076211, -2.0583647797))
                Line((-0.8151923789, -2.0119546181), (-1.0151923789, -2.3583647797))
                CenterArc((0, 0), 2.1708293346, -112.0565281894, 44.1130563788)
                Line((1.0151923789, -2.3583647797), (0.8151923789, -2.0119546181))
                Line((1.5348076211, -2.0583647797), (1.0151923789, -2.3583647797))
                Line((1.3348076211, -1.7119546181), (1.5348076211, -2.0583647797))
                CenterArc((0, 0), 2.1708293346, -52.0565281894, 14.1130563788)
                Line((2.0583647797, -1.5348076211), (1.7119546181, -1.3348076211))
                Line((2.3583647797, -1.0151923789), (2.0583647797, -1.5348076211))
                Line((2.0119546181, -0.8151923789), (2.3583647797, -1.0151923789))
                CenterArc((0, 0), 2.1708293346, -22.0565281894, 44.1130563788)
                Line((2.3583647797, 1.0151923789), (2.0119546181, 0.8151923789))
                Line((2.0583647797, 1.5348076211), (2.3583647797, 1.0151923789))
                Line((1.7119546181, 1.3348076211), (2.0583647797, 1.5348076211))
                CenterArc((0, 0), 2.1708293346, 37.9434718106, 14.1130563788)
                Line((1.5348076211, 2.0583647797), (1.3348076211, 1.7119546181))
                Line((1.0151923789, 2.3583647797), (1.5348076211, 2.0583647797))
                Line((0.8151923789, 2.0119546181), (1.0151923789, 2.3583647797))
                CenterArc((0, 0), 2.1708293346, 67.9434718106, 44.1130563788)
                Line((-1.0151923789, 2.3583647797), (-0.8151923789, 2.0119546181))
                Line((-1.5348076211, 2.0583647797), (-1.0151923789, 2.3583647797))
                Line((-1.3348076211, 1.7119546181), (-1.5348076211, 2.0583647797))
            make_face()
            with BuildLine():
                Line((-0.25, 1.4), (0.25, 1.4))
                Line((0.25, 1.4), (0.25, 1.7320508076))
                CenterArc((0, 0), 1.75, 98.2132107017, 343.5735785965)
                Line((-0.25, 1.7320508076), (-0.25, 1.4))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.08
        extrude(amount=0.08)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on YZ construction plane
        # Sketch has 10 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0412680429, perimeter: 1.1917010721
            with BuildLine():
                Line((0, 2.1708293346), (0, 2.0708293346))
                CenterArc((-0.08, 2.1708293346), 0.08, 0, 80)
                Line((-0.4206389369, 2.3121272988), (-0.0661081458, 2.2496139549))
                Line((-0.4345307911, 2.2333426786), (-0.4206389369, 2.3121272988))
                Line((-0.08, 2.1708293346), (-0.4345307911, 2.2333426786))
                Line((-0.08, 2.0708293346), (-0.08, 2.1708293346))
                Line((0, 2.0708293346), (-0.08, 2.0708293346))
            make_face()
        # Symmetric extrude, each_side=0.3
        extrude(amount=0.3, both=True, mode=Mode.ADD)
    return part.part


def model_27054_342fcf5c_0025():
    """Model: 10 - Washer v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 106 constraints, 28 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 5.9060950407, perimeter: 25.311322853
            with BuildLine():
                CenterArc((0, 0), 1.6770509831, 130.3048464688, 9.3903070625)
                Line((-1.6253520778, 1.2848076211), (-1.2789419162, 1.0848076211))
                Line((-1.9253520778, 0.7651923789), (-1.6253520778, 1.2848076211))
                Line((-1.5789419162, 0.5651923789), (-1.9253520778, 0.7651923789))
                CenterArc((0, 0), 1.6770509831, 160.3048464688, 39.3903070625)
                Line((-1.9253520778, -0.7651923789), (-1.5789419162, -0.5651923789))
                Line((-1.6253520778, -1.2848076211), (-1.9253520778, -0.7651923789))
                Line((-1.2789419162, -1.0848076211), (-1.6253520778, -1.2848076211))
                CenterArc((0, 0), 1.6770509831, -139.6951535312, 9.3903070625)
                Line((-1.2848076211, -1.6253520778), (-1.0848076211, -1.2789419162))
                Line((-0.7651923789, -1.9253520778), (-1.2848076211, -1.6253520778))
                Line((-0.5651923789, -1.5789419162), (-0.7651923789, -1.9253520778))
                CenterArc((0, 0), 1.6770509831, -109.6951535312, 39.3903070625)
                Line((0.7651923789, -1.9253520778), (0.5651923789, -1.5789419162))
                Line((1.2848076211, -1.6253520778), (0.7651923789, -1.9253520778))
                Line((1.0848076211, -1.2789419162), (1.2848076211, -1.6253520778))
                CenterArc((0, 0), 1.6770509831, -49.6951535312, 9.3903070625)
                Line((1.6253520778, -1.2848076211), (1.2789419162, -1.0848076211))
                Line((1.9253520778, -0.7651923789), (1.6253520778, -1.2848076211))
                Line((1.5789419162, -0.5651923789), (1.9253520778, -0.7651923789))
                CenterArc((0, 0), 1.6770509831, -19.6951535312, 39.3903070625)
                Line((1.9253520778, 0.7651923789), (1.5789419162, 0.5651923789))
                Line((1.6253520778, 1.2848076211), (1.9253520778, 0.7651923789))
                Line((1.2789419162, 1.0848076211), (1.6253520778, 1.2848076211))
                CenterArc((0, 0), 1.6770509831, 40.3048464688, 9.3903070625)
                Line((1.2848076211, 1.6253520778), (1.0848076211, 1.2789419162))
                Line((0.7651923789, 1.9253520778), (1.2848076211, 1.6253520778))
                Line((0.5651923789, 1.5789419162), (0.7651923789, 1.9253520778))
                CenterArc((0, 0), 1.6770509831, 70.3048464688, 39.3903070625)
                Line((-0.7651923789, 1.9253520778), (-0.5651923789, 1.5789419162))
                Line((-1.2848076211, 1.6253520778), (-0.7651923789, 1.9253520778))
                Line((-1.0848076211, 1.2789419162), (-1.2848076211, 1.6253520778))
            make_face()
            with BuildLine():
                Line((-0.25, 0.95), (0.25, 0.95))
                Line((0.25, 0.95), (0.25, 1.2247448714))
                CenterArc((0, 0), 1.25, 101.5369590328, 336.9260819344)
                Line((-0.25, 1.2247448714), (-0.25, 0.95))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.08
        extrude(amount=0.08)

        # Sketch3 -> Extrude2 (Join)
        # Sketch on YZ construction plane
        # Sketch has 10 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0412680429, perimeter: 1.1917010721
            with BuildLine():
                Line((-0.08, 1.5770509831), (0, 1.5770509831))
                Line((0, 1.5770509831), (0, 1.6770509831))
                CenterArc((-0.08, 1.6770509831), 0.08, 0, 80)
                Line((-0.4206389369, 1.8183489473), (-0.0661081458, 1.7558356034))
                Line((-0.4345307911, 1.7395643271), (-0.4206389369, 1.8183489473))
                Line((-0.08, 1.6770509831), (-0.4345307911, 1.7395643271))
                Line((-0.08, 1.5770509831), (-0.08, 1.6770509831))
            make_face()
        # Symmetric extrude, each_side=0.3
        extrude(amount=0.3, both=True, mode=Mode.ADD)
    return part.part


def model_27054_342fcf5c_0034():
    """Model: 26 - Washer v1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 89 constraints, 28 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 7.8494912457, perimeter: 34.8204539703
            with BuildLine():
                CenterArc((0, 0), 2.4186773245, 67.1250163489, 5.265850868)
                CenterArc((0.0191647146, 0.2380476203), 2.1866469489, 70.9823920964, 28.8295444002)
                CenterArc((0, 0), 2.4186773245, 98.403461376, 14.4715222751)
                Line((-1.1401923789, 2.5748711306), (-0.9401923789, 2.2284609691))
                Line((-1.6598076211, 2.2748711306), (-1.1401923789, 2.5748711306))
                Line((-1.4598076211, 1.9284609691), (-1.6598076211, 2.2748711306))
                CenterArc((0, 0), 2.4186773245, 127.1250163489, 15.7499673022)
                Line((-2.2748711306, 1.6598076211), (-1.9284609691, 1.4598076211))
                Line((-2.5748711306, 1.1401923789), (-2.2748711306, 1.6598076211))
                Line((-2.2284609691, 0.9401923789), (-2.5748711306, 1.1401923789))
                CenterArc((0, 0), 2.4186773245, 157.1250163489, 45.7499673022)
                Line((-2.5748711306, -1.1401923789), (-2.2284609691, -0.9401923789))
                Line((-2.2748711306, -1.6598076211), (-2.5748711306, -1.1401923789))
                Line((-1.9284609691, -1.4598076211), (-2.2748711306, -1.6598076211))
                CenterArc((0, 0), 2.4186773245, -142.8749836511, 15.7499673022)
                Line((-1.6598076211, -2.2748711306), (-1.4598076211, -1.9284609691))
                Line((-1.1401923789, -2.5748711306), (-1.6598076211, -2.2748711306))
                Line((-0.9401923789, -2.2284609691), (-1.1401923789, -2.5748711306))
                CenterArc((0, 0), 2.4186773245, -112.8749836511, 45.7499673022)
                Line((1.1401923789, -2.5748711306), (0.9401923789, -2.2284609691))
                Line((1.6598076211, -2.2748711306), (1.1401923789, -2.5748711306))
                Line((1.4598076211, -1.9284609691), (1.6598076211, -2.2748711306))
                CenterArc((0, 0), 2.4186773245, -52.8749836511, 15.7499673022)
                Line((2.2748711306, -1.6598076211), (1.9284609691, -1.4598076211))
                Line((2.5748711306, -1.1401923789), (2.2748711306, -1.6598076211))
                Line((2.2284609691, -0.9401923789), (2.5748711306, -1.1401923789))
                CenterArc((0, 0), 2.4186773245, -22.8749836511, 45.7499673022)
                Line((2.5748711306, 1.1401923789), (2.2284609691, 0.9401923789))
                Line((2.2748711306, 1.6598076211), (2.5748711306, 1.1401923789))
                Line((1.9284609691, 1.4598076211), (2.2748711306, 1.6598076211))
                CenterArc((0, 0), 2.4186773245, 37.1250163489, 15.7499673022)
                Line((1.6598076211, 2.2748711306), (1.4598076211, 1.9284609691))
                Line((1.1401923789, 2.5748711306), (1.6598076211, 2.2748711306))
                Line((0.9401923789, 2.2284609691), (1.1401923789, 2.5748711306))
            make_face()
            with BuildLine():
                Line((-0.25, 1.65), (0.25, 1.65))
                Line((0.25, 1.65), (0.25, 1.9843134833))
                CenterArc((0, 0), 2, 97.1807557815, 345.6384884371)
                Line((-0.25, 1.9843134833), (-0.25, 1.65))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.08
        extrude(amount=0.08)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on YZ construction plane
        # Sketch has 10 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0412680429, perimeter: 1.1917010721
            with BuildLine():
                Line((0, 2.4246105836), (0, 2.3246105836))
                CenterArc((-0.08, 2.4246105836), 0.08, 0, 80)
                Line((-0.4206389369, 2.5659085478), (-0.0661081458, 2.5033952039))
                Line((-0.4345307911, 2.4871239276), (-0.4206389369, 2.5659085478))
                Line((-0.08, 2.4246105836), (-0.4345307911, 2.4871239276))
                Line((-0.08, 2.3246105836), (-0.08, 2.4246105836))
                Line((0, 2.3246105836), (-0.08, 2.3246105836))
            make_face()
        # Symmetric extrude, each_side=0.3
        extrude(amount=0.3, both=True, mode=Mode.ADD)
    return part.part


def model_27070_53448c4a_0007():
    """Model: Koncowka"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 12.1584300897), x_dir=(1, 0, 0), z_dir=(0, 0, 1))) as sk:
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((0, 22)):
                Circle(0.5)
        # TwoSides extrude, along=0.2, against=-1
        extrude(amount=0.2)
        extrude(sk.sketch, amount=-1)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 12.3584300897), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 3.156680104, perimeter: 7.1076344045
            with BuildLine():
                Line((-0.3855175899, 24.2167264576), (-0.0856705755, 22.4926058795))
                CenterArc((0, 22), 2.25, 99.8658055645, 75.1644456021)
                Line((-2.2415412959, 22.1949169539), (-0.498120288, 22.0433148786))
                CenterArc((0, 22), 0.5, 99.8658055645, 75.1644456021)
            make_face()
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2, mode=Mode.ADD)
    return part.part


def model_27663_023746a1_0011():
    """Model: FemaleHeader v5"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 16 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.05661279, perimeter: 1.3716
            with BuildLine():
                Line((0, 0.254), (0, 0))
                Line((0, 0), (0.254, 0))
                Line((0.254, 0), (0.254, 0.254))
                Line((0.254, 0.254), (0, 0.254))
            make_face()
            with BuildLine():
                Line((0.17145, 0.08255), (0.08255, 0.08255))
                Line((0.08255, 0.08255), (0.08255, 0.17145))
                Line((0.08255, 0.17145), (0.17145, 0.17145))
                Line((0.17145, 0.17145), (0.17145, 0.08255))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.85
        extrude(amount=0.85)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.01850304, perimeter: 1.0056
            with BuildLine():
                Line((0.20825, -0.20825), (0.04575, -0.20825))
                Line((0.20825, -0.04575), (0.20825, -0.20825))
                Line((0.04575, -0.04575), (0.20825, -0.04575))
                Line((0.04575, -0.20825), (0.04575, -0.04575))
            make_face()
            with BuildLine():
                Line((0.08255, -0.08255), (0.17145, -0.08255))
                Line((0.17145, -0.08255), (0.17145, -0.17145))
                Line((0.17145, -0.17145), (0.08255, -0.17145))
                Line((0.08255, -0.17145), (0.08255, -0.08255))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.8128
        extrude(amount=-0.8128, mode=Mode.SUBTRACT)

        # Sketch1 -> Extrude3 (Join)
        # Sketch on XZ construction plane
        # Sketch has 16 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.05661279, perimeter: 1.3716
            with BuildLine():
                Line((0, 0.254), (0, 0))
                Line((0, 0), (0.254, 0))
                Line((0.254, 0), (0.254, 0.254))
                Line((0.254, 0.254), (0, 0.254))
            make_face()
            with BuildLine():
                Line((0.17145, 0.08255), (0.08255, 0.08255))
                Line((0.08255, 0.08255), (0.08255, 0.17145))
                Line((0.08255, 0.17145), (0.17145, 0.17145))
                Line((0.17145, 0.17145), (0.17145, 0.08255))
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.00790321, perimeter: 0.3556
            with BuildLine():
                Line((0.17145, 0.17145), (0.17145, 0.08255))
                Line((0.08255, 0.17145), (0.17145, 0.17145))
                Line((0.08255, 0.08255), (0.08255, 0.17145))
                Line((0.17145, 0.08255), (0.08255, 0.08255))
            make_face()
        # OneSide extrude, distance=0.0254
        extrude(amount=0.0254, mode=Mode.ADD)
    return part.part


def model_27663_023746a1_0021():
    """Model: TrimPot v4 (2)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 29 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.00403225, perimeter: 0.254
            with BuildLine():
                Line((0.9525, 0.0635), (0.9525, 0))
                Line((0.9525, 0), (1.016, 0))
                Line((1.016, 0), (1.016, 0.0635))
                Line((1.016, 0.0635), (0.9525, 0.0635))
            make_face()
            # Profile area: 0.00403225, perimeter: 0.254
            with BuildLine():
                Line((0.0635, 0.889), (0, 0.889))
                Line((0.0635, 0.9525), (0.0635, 0.889))
                Line((0, 0.9525), (0.0635, 0.9525))
                Line((0, 0.889), (0, 0.9525))
            make_face()
            # Profile area: 0.0040322503, perimeter: 0.2540000107
            with BuildLine():
                Line((0.9525, 0.8889999893), (0.9525, 0.9525))
                Line((1.016, 0.8889999893), (0.9525, 0.8889999893))
                Line((1.016, 0.9524999893), (1.016, 0.8889999893))
                Line((0.9525, 0.9525), (1.016, 0.9524999893))
            make_face()
            # Profile area: 0.00403225, perimeter: 0.254
            with BuildLine():
                Line((0.0635, 0), (0.0635, 0.0635))
                Line((0.0635, 0.0635), (0, 0.0635))
                Line((0, 0.0635), (0, 0))
                Line((0, 0), (0.0635, 0))
            make_face()
            # Profile area: 0.7805765962, perimeter: 5.030885737
            with BuildLine():
                Line((0.0635, 0), (0.9525, 0))
                Line((0.9525, 0.0635), (0.9525, 0))
                Line((0.9525, 0.0635), (0.9525, 0.8889999893))
                Line((0.9525, 0.8889999893), (0.9525, 0.9525))
                Line((0.9525, 0.9525), (0.0635, 0.9525))
                Line((0.0635, 0.9525), (0.0635, 0.889))
                Line((0.0635, 0.889), (0, 0.889))
                Line((0, 0.889), (0, 0.0635))
                Line((0.0635, 0.0635), (0, 0.0635))
                Line((0.0635, 0), (0.0635, 0.0635))
            make_face()
            with BuildLine():
                CenterArc((0.47625, 0.47625), 0.19431, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.1186151538, perimeter: 1.220885737
            with Locations((0.47625, 0.47625)):
                Circle(0.19431)
        # OneSide extrude, distance=0.4445
        extrude(amount=0.4445)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 29 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.00403225, perimeter: 0.254
            with BuildLine():
                Line((0.0635, 0), (0.0635, 0.0635))
                Line((0.0635, 0.0635), (0, 0.0635))
                Line((0, 0.0635), (0, 0))
                Line((0, 0), (0.0635, 0))
            make_face()
            # Profile area: 0.00403225, perimeter: 0.254
            with BuildLine():
                Line((0.9525, 0.0635), (0.9525, 0))
                Line((0.9525, 0), (1.016, 0))
                Line((1.016, 0), (1.016, 0.0635))
                Line((1.016, 0.0635), (0.9525, 0.0635))
            make_face()
            # Profile area: 0.0040322503, perimeter: 0.2540000107
            with BuildLine():
                Line((0.9525, 0.8889999893), (0.9525, 0.9525))
                Line((1.016, 0.8889999893), (0.9525, 0.8889999893))
                Line((1.016, 0.9524999893), (1.016, 0.8889999893))
                Line((0.9525, 0.9525), (1.016, 0.9524999893))
            make_face()
            # Profile area: 0.00403225, perimeter: 0.254
            with BuildLine():
                Line((0.0635, 0.889), (0, 0.889))
                Line((0.0635, 0.9525), (0.0635, 0.889))
                Line((0, 0.9525), (0.0635, 0.9525))
                Line((0, 0.889), (0, 0.9525))
            make_face()
        # OneSide extrude, distance=-0.0381
        extrude(amount=-0.0381, mode=Mode.ADD)
    return part.part


def model_27663_023746a1_0023():
    """Model: 12PinHeader v2 (3)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.04, perimeter: 0.8
            with BuildLine():
                Line((0, 0.2), (0, 0))
                Line((0, 0), (0.2, 0))
                Line((0.2, 0), (0.2, 0.2))
                Line((0.2, 0.2), (0, 0.2))
            make_face()
        # OneSide extrude, distance=0.254
        extrude(amount=0.254)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.2, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))) as sk:
            # Profile area: 0.03556, perimeter: 0.7556
            with BuildLine():
                Line((0.2, 0.0762), (0, 0.0762))
                Line((0.2, 0.0762), (0.2, 0.254))
                Line((0, 0.254), (0.2, 0.254))
                Line((0, 0.0762), (0, 0.254))
            make_face()
        # TwoSides extrude, along=0.0254, against=-0.2286
        extrude(amount=0.0254, mode=Mode.ADD)
        extrude(sk.sketch, amount=-0.2286, mode=Mode.ADD)
    return part.part


def model_27679_501db761_0001():
    """Model: freio"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 19 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.5149686025, perimeter: 7.104446759
            with BuildLine():
                Line((-1.16, 0), (-0.95, 0))
                CenterArc((-0.06, 0), 1.1, 180, 154.349923492)
                CenterArc((0.9874, -0.4982147172), 0.06, 150.6872863467, 7.7475468286)
                CenterArc((0.9874, -0.4982147172), 0.06, 98.0261877104, 52.6610986362)
                Line((1.1277366417, -0.4178327218), (0.979022458, -0.4388024559))
                CenterArc((1.1201, -0.3181247397), 0.1, -85.6202625917, 78.1217351721)
                Line((1.2371, -0.195524325), (1.2192448216, -0.3311748108))
                Line((1.2371, -0.195524325), (0.9371, -0.156024325))
                CenterArc((0, 0), 0.95, 180, 170.5471373148)
            make_face()
            with BuildLine():
                CenterArc((1.1201, -0.3181247397), 0.05, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.12
        extrude(amount=0.12)
    return part.part


def model_27679_501db761_0004():
    """Model: 18_34.."""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 9 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.2207505369, perimeter: 10.0268763423
            with BuildLine():
                Line((0, 2.7134381711), (0, 0))
                Line((0, 0), (0.8, 0))
                Line((0.8, 0), (0.8, 4.2134381711))
                Line((0.8, 4.2134381711), (0.1, 4.2134381711))
                Line((0.1, 4.2134381711), (0.1, 2.7134381711))
                Line((0.1, 2.7134381711), (0, 2.7134381711))
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.1, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.138544236, perimeter: 1.3194689145
            with Locations((-3.0634381711, 0.35)):
                Circle(0.21)
            # Profile area: 0.138544236, perimeter: 1.3194689145
            with Locations((-3.0634381711, 1.65)):
                Circle(0.21)
        # OneSide extrude, distance=-2.4
        extrude(amount=-2.4, mode=Mode.SUBTRACT)
    return part.part


def model_27679_501db761_0006():
    """Model: 20_18"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 57.75, perimeter: 40
            with BuildLine():
                Line((0, -16.5), (0, 0))
                Line((0, 0), (-3.5, 0))
                Line((-3.5, 0), (-3.5, -16.5))
                Line((-3.5, -16.5), (0, -16.5))
            make_face()
        # OneSide extrude, distance=3
        extrude(amount=3)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 18 constraints, 9 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 3, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.5422603238, perimeter: 10.3025658741
            with BuildLine():
                Line((1.85, 0), (1.65, 0))
                Line((1.85, 0), (1.85, 1.5050125629))
                CenterArc((1.75, 2.5), 1, -84.2608295227, 168.5216590455)
                Line((1.85, 3.4949874371), (1.85, 4))
                Line((1.85, 4), (1.65, 4))
                Line((1.65, 3.4949874371), (1.65, 4))
                CenterArc((1.75, 2.5), 1, 95.7391704773, 168.5216590455)
                Line((1.65, 0), (1.65, 1.5050125629))
            make_face()
        # OneSide extrude, distance=-13
        extrude(amount=-13, mode=Mode.SUBTRACT)

        # Sketch2 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 18 constraints, 9 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 3, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.8659014751, perimeter: 3.2986722863
            with Locations((1.75, 14.4997)):
                Circle(0.525)
        # OneSide extrude, distance=-7
        extrude(amount=-7, mode=Mode.SUBTRACT)
    return part.part


def model_27679_501db761_0009():
    """Model: 8_30"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.5766127407, perimeter: 9.1162722863
            with BuildLine():
                Line((-0.8396982315, 0.4848), (-0.8396982315, -0.4848))
                Line((-0.8396982315, -0.4848), (0, -0.9696))
                Line((0, -0.9696), (0.8396982315, -0.4848))
                Line((0.8396982315, -0.4848), (0.8396982315, 0.4848))
                Line((0.8396982315, 0.4848), (0, 0.9696))
                Line((0, 0.9696), (-0.8396982315, 0.4848))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.525, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=9
        extrude(amount=9)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.8659014751, perimeter: 3.2986722863
            Circle(0.525)
        # OneSide extrude, distance=9
        extrude(amount=9, mode=Mode.ADD)
    return part.part


def model_27679_501db761_0010():
    """Model: 14_11 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            Circle(1)
        # OneSide extrude, distance=0.37
        extrude(amount=0.37)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.37, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.3778714795, perimeter: 5.4663712172
            Circle(0.87)
        # OneSide extrude, distance=0.13
        extrude(amount=0.13, mode=Mode.ADD)
    return part.part


def model_27679_501db761_0013():
    """Model: 10_44"""
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
            # Profile area: 2.3778714795, perimeter: 5.4663712172
            Circle(0.87)
        # OneSide extrude, distance=0.13
        extrude(amount=0.13, mode=Mode.ADD)
    return part.part


def model_27679_501db761_0023():
    """Model: 12_43"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.1309733553, perimeter: 3.7699111843
            Circle(0.6)
        # OneSide extrude, distance=24
        extrude(amount=24)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 10 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 24, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0450155561, perimeter: 1.3661476102
            with BuildLine():
                CenterArc((0, 0), 0.6, 146.4426902381, 67.1146195238)
                Line((-0.5, -0.331662479), (-0.5, 0.331662479))
            make_face()
            # Profile area: 0.0450155561, perimeter: 1.3661476102
            with BuildLine():
                Line((0.5, -0.331662479), (0.5, 0))
                CenterArc((0, 0), 0.6, -33.5573097619, 67.1146195238)
                Line((0.5, 0), (0.5, 0.331662479))
            make_face()
        # OneSide extrude, distance=-0.8
        extrude(amount=-0.8, mode=Mode.SUBTRACT)
    return part.part


def model_27682_04277f62_0000():
    """Model: eje union"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.9087385212, perimeter: 7.853981634
            Circle(1.25)
        # OneSide extrude, distance=0.7
        extrude(amount=0.7)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.7, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.2698006922, perimeter: 5.3407075111
            Circle(0.85)
        # OneSide extrude, distance=13
        extrude(amount=13, mode=Mode.ADD)
    return part.part


def model_27682_04277f62_0003():
    """Model: pin asiento"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            Circle(0.4)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            Circle(0.3)
        # OneSide extrude, distance=2.3
        extrude(amount=2.3, mode=Mode.ADD)
    return part.part


def model_27694_7801dc67_0009():
    """Model: top plate"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 22 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 22.7765467385, perimeter: 91.1061869541
            with BuildLine():
                CenterArc((7.5, 7.5), 7.5, 90, 90)
                CenterArc((7.5, 7.5), 7.5, -180, 90)
                CenterArc((7.5, 7.5), 7.5, -90, 90)
                CenterArc((7.5, 7.5), 7.5, 0, 90)
            make_face()
            with BuildLine():
                CenterArc((7.5, 7.5), 7, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=0.75
        extrude(amount=0.75, both=True)

        # Sketch1 -> Extrude2 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 22 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))) as sk:
            # Profile area: 3.7306412761, perimeter: 29.8451302091
            with BuildLine():
                CenterArc((11, 7.5), 2.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((11, 7.5), 2.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # TwoSides extrude, along=0.45, against=-0.25
        extrude(amount=0.45)
        extrude(sk.sketch, amount=-0.25)

        # Sketch1 -> Extrude3 (Join)
        # Sketch on XZ construction plane
        # Sketch has 22 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 11.754290235, perimeter: 28.0298660229
            with BuildLine():
                CenterArc((7.5, 7.5), 7.5, -90, 90)
                Line((7.5, 0), (14.25, 0))
                CenterArc((14.25, 0.75), 0.75, -90, 90)
                Line((15, 0.75), (15, 7.5))
            make_face()
            with BuildLine():
                CenterArc((14.25, 0.75), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 11.754290235, perimeter: 28.0298660229
            with BuildLine():
                CenterArc((7.5, 7.5), 7.5, -180, 90)
                Line((0, 7.5), (0, 0.75))
                CenterArc((0.75, 0.75), 0.75, 180, 90)
                Line((0.75, 0), (7.5, 0))
            make_face()
            with BuildLine():
                CenterArc((0.75, 0.75), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 11.754290235, perimeter: 28.0298660229
            with BuildLine():
                Line((0, 14.25), (0, 7.5))
                CenterArc((7.5, 7.5), 7.5, 90, 90)
                Line((7.5, 15), (0.75, 15))
                CenterArc((0.75, 14.25), 0.75, 90, 90)
            make_face()
            with BuildLine():
                CenterArc((0.75, 14.25), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 11.754290235, perimeter: 28.0298660229
            with BuildLine():
                CenterArc((7.5, 7.5), 7.5, 0, 90)
                Line((15, 7.5), (15, 14.25))
                CenterArc((14.25, 14.25), 0.75, 0, 90)
                Line((14.25, 15), (7.5, 15))
            make_face()
            with BuildLine():
                CenterArc((14.25, 14.25), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 134.1067364001, perimeter: 61.261056745
            with BuildLine():
                CenterArc((7.5, 7.5), 7, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((7.5, 7.5), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((11, 7.5), 2.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=0.25
        extrude(amount=0.25, both=True, mode=Mode.ADD)
    return part.part


def model_27839_4a077326_0001():
    """Model: Sruba blokady"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            with Locations((4, 11)):
                Circle(0.4)
        # OneSide extrude, distance=1.7
        extrude(amount=1.7)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(1.7, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.6283185307, perimeter: 6.2831853072
            with BuildLine():
                CenterArc((4, 11), 0.6, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((4, 11), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            with Locations((4, 11)):
                Circle(0.4)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3, mode=Mode.ADD)
    return part.part


def model_27839_4a077326_0008():
    """Model: Gwint nakretki"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            with Locations((-5, 62)):
                Circle(0.4)
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            with Locations((5, 62)):
                Circle(0.3)
        # OneSide extrude, distance=-0.8
        extrude(amount=-0.8, mode=Mode.SUBTRACT)
    return part.part


def model_27839_4a077326_0011():
    """Model: Sruba stopnia"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            with Locations((-28.6358284639, 34.2451942771)):
                Circle(0.4)
        # OneSide extrude, distance=4.2
        extrude(amount=4.2)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.6283185307, perimeter: 6.2831853072
            with BuildLine():
                CenterArc((28.6358284639, 34.2451942771), 0.6, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((28.6358284639, 34.2451942771), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            with Locations((28.6358284639, 34.2451942771)):
                Circle(0.4)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)
    return part.part


def model_27839_4a077326_0019():
    """Model: Spinka prawej raczki"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 9 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.398241138, perimeter: 11.5183182293
            with BuildLine():
                Line((1.25, -0.63), (-0.55, -0.63))
                CenterArc((-0.55, 0), 0.63, 90, 180)
                Line((-0.55, 0.63), (1.25, 0.63))
                Line((1.25, 0.7), (1.25, 0.63))
                Line((-0.55, 0.7), (1.25, 0.7))
                CenterArc((-0.55, 0), 0.7, 90, 180)
                Line((1.25, -0.7), (-0.55, -0.7))
                Line((1.25, -0.63), (1.25, -0.7))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -0.7), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            with Locations((-0.65, 0.5)):
                Circle(0.4)
        # OneSide extrude, distance=0.8
        extrude(amount=0.8, mode=Mode.ADD)
    return part.part


def model_28119_f4fb1c4c_0001():
    """Model: Component11"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 10.3815976202, perimeter: 17.4311012509
            with BuildLine():
                Line((0.5378747632, 9.874714172), (-2.1000000313, 9.874714172))
                Line((-2.1000000313, 9.874714172), (-2.1000000313, 12.1681062032))
                Line((-2.1000000313, 12.1681062032), (-2.6000000387, 12.1681062032))
                CenterArc((-2.6821359366, 10.2260632478), 1.9437790889, 87.5782011814, 93.1900703517)
                Line((-3.0000000447, 10.200000152), (-4.6257402846, 10.200000152))
                Line((-3.0000000447, 8.2000001222), (-3.0000000447, 10.200000152))
                Line((0.5378747632, 8.2000001222), (-3.0000000447, 8.2000001222))
                Line((0.5378747632, 9.874714172), (0.5378747632, 8.2000001222))
            make_face()
        # Symmetric extrude, each_side=2.5
        extrude(amount=2.5, both=True)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0.5378747632, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.6361725124, perimeter: 2.8274333882
            with Locations((0, 11.9397429587)):
                Circle(0.45)
        # OneSide extrude, distance=-6
        extrude(amount=-6, mode=Mode.SUBTRACT)
    return part.part


def model_28287_522a580c_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 5.3576375539, perimeter: 12.3590254992
            with BuildLine():
                CenterArc((0, 0), 1.417, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.55, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.8
        extrude(amount=0.8)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.8, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0153109124, perimeter: 0.5516312352
            with BuildLine():
                CenterArc((0, 0), 1.417, -3.6213041505, 3.6213041505)
                CenterArc((1.3998398403, 0.5223321883), 0.612, -88.6582149446, 19.6680751129)
                CenterArc((0, 0), 1.62, -1.7326224886, 1.7326224886)
                Line((1.417, 0), (1.62, 0))
            make_face()
        # OneSide extrude, distance=-0.8
        extrude(amount=-0.8, mode=Mode.ADD)
    return part.part


def model_28300_b3a6ab79_0002():
    """Model: wtyczka"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((0.5000000075, 10.400000155)):
                Circle(0.25)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)

        # Sketch2 -> Extrude2 (NewBody)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 19.4386045441, perimeter: 17.2787595947
            with BuildLine():
                CenterArc((-0.5000000075, -10.400000155), 2.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-0.5000000075, -10.400000155), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=5
        extrude(amount=5)
    return part.part


def model_28300_b3a6ab79_0005():
    """Model: Pokrycie Rowku"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 13 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.26235, perimeter: 6.0494
            with BuildLine():
                Line((-10.3665, -0.5), (-10.3665, -3.0247))
                Line((-10.3665, -3.0247), (-9.8665, -3.0247))
                Line((-9.8665, -3.0247), (-9.8665, -0.5))
                Line((-9.8665, -0.5), (-10.3665, -0.5))
            make_face()
            # Profile area: 1.26235, perimeter: 6.0494
            with BuildLine():
                Line((-4.5, -3.0247), (-4.5, -0.5))
                Line((-4, -3.0247), (-4.5, -3.0247))
                Line((-4, -0.5), (-4, -3.0247))
                Line((-4, -0.5), (-4.5, -0.5))
            make_face()
        # OneSide extrude, distance=-0.3
        extrude(amount=-0.3)

        # Sketch3 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 13.54880255, perimeter: 15.7824
            with BuildLine():
                Line((-9.8665, -3.0247), (-4.5, -3.0247))
                Line((-4.5, -3.0247), (-4.5, -0.5))
                Line((-4.5, -0.5), (-9.8665, -0.5))
                Line((-9.8665, -3.0247), (-9.8665, -0.5))
            make_face()
        # OneSide extrude, distance=-0.1
        extrude(amount=-0.1, mode=Mode.ADD)
    return part.part


def model_28300_b3a6ab79_0011():
    """Model: boltz"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((-5.0000000745, -1.5000000224)):
                Circle(0.15)
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -0.5, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.0199999991, perimeter: 0.5999999866
            with BuildLine():
                Line((-4.8999998905, 1.5499999654), (-5.099999886, 1.5499999654))
                Line((-5.099999886, 1.5499999654), (-5.099999886, 1.4499999676))
                Line((-5.099999886, 1.4499999676), (-4.8999998905, 1.4499999676))
                Line((-4.8999998905, 1.4499999676), (-4.8999998905, 1.5499999654))
            make_face()
        # OneSide extrude, distance=-0.05
        extrude(amount=-0.05, mode=Mode.SUBTRACT)
    return part.part


def model_28300_b3a6ab79_0013():
    """Model: Component15"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((3.5, 1)):
                Circle(0.25)
        # OneSide extrude, distance=-1.5
        extrude(amount=-1.5)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 11 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(-1.5, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.0500000015, perimeter: 1.2000000179
            with BuildLine():
                Line((-3.5500000529, 1.0500000156), (-3.6500000544, 1.0500000156))
                Line((-3.6500000544, 1.0500000156), (-3.6500000544, 0.9500000142))
                Line((-3.6500000544, 0.9500000142), (-3.5500000529, 0.9500000142))
                Line((-3.5500000529, 0.9500000142), (-3.5500000529, 0.8500000127))
                Line((-3.5500000529, 0.8500000127), (-3.4500000514, 0.8500000127))
                Line((-3.4500000514, 0.8500000127), (-3.4500000514, 0.9500000142))
                Line((-3.4500000514, 0.9500000142), (-3.3500000499, 0.9500000142))
                Line((-3.3500000499, 0.9500000142), (-3.3500000499, 1.0500000156))
                Line((-3.3500000499, 1.0500000156), (-3.4500000514, 1.0500000156))
                Line((-3.4500000514, 1.1500000171), (-3.4500000514, 1.0500000156))
                Line((-3.5500000529, 1.1500000171), (-3.4500000514, 1.1500000171))
                Line((-3.5500000529, 1.0500000156), (-3.5500000529, 1.1500000171))
            make_face()
        # OneSide extrude, distance=-0.1
        extrude(amount=-0.1, mode=Mode.SUBTRACT)
    return part.part


def model_28300_b3a6ab79_0014():
    """Model: uziom"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0804247719, perimeter: 1.0053096491
            with Locations((-3.0000000447, 0.5000000075)):
                Circle(0.16)
        # OneSide extrude, distance=2.5
        extrude(amount=2.5)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((3.0000000447, 0.5000000075)):
                Circle(0.15)
        # OneSide extrude, distance=-2
        extrude(amount=-2, mode=Mode.SUBTRACT)
    return part.part


def model_28446_d757d32d_0022():
    """Model: uszczelka v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.4948008429, perimeter: 6.5973445725
            with BuildLine():
                CenterArc((0, 0), 0.6, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.45, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.7671458676, perimeter: 4.7123889804
            Circle(0.75)
        # OneSide extrude, distance=-0.3
        extrude(amount=-0.3, mode=Mode.ADD)
    return part.part


def model_28446_d757d32d_0026():
    """Model: polkaSzklana v10 (2)"""
    with BuildPart() as part:
        # Sketch4 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1248, perimeter: 142
            with BuildLine():
                Line((39, -32), (0, -32))
                Line((39, 0), (39, -32))
                Line((0, 0), (39, 0))
                Line((0, -32), (0, 0))
            make_face()
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)
    return part.part


def model_28457_e541aa9b_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> 押し出し1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints, 12 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 9.12, perimeter: 71.4
            with BuildLine():
                Line((-10, 0), (0, 0))
                Line((0, 0), (0, 9))
                Line((0, 9), (-0.3, 9))
                Line((-0.3, 9), (-0.3, 0.3))
                Line((-0.3, 0.3), (-1.7, 0.3))
                Line((-1.7, 0.3), (-1.7, 6.3))
                Line((-1.7, 6.3), (-1.9, 6.3))
                Line((-1.9, 6.3), (-1.9, 0.3))
                Line((-1.9, 0.3), (-6, 0.3))
                Line((-6, 0.3), (-6, 6.3))
                Line((-6, 6.3), (-6.15, 6.3))
                Line((-6.15, 6.3), (-6.15, 0.3))
                Line((-6.15, 0.3), (-9.7, 0.3))
                Line((-9.7, 0.3), (-9.7, 5))
                Line((-9.7, 5), (-10, 5))
                Line((-10, 5), (-10, 0))
            make_face()
        # OneSide extrude, distance=3
        extrude(amount=3)

        # Sketch2 -> 押し出し2 (Join)
        # Sketch on YZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 84, perimeter: 36
            with BuildLine():
                Line((-7, 9), (-10, 5))
                Line((-10, 5), (-10, 0))
                Line((-10, 0), (0, 0))
                Line((0, 0), (0, 9))
                Line((0, 9), (-7, 9))
            make_face()
        # OneSide extrude, distance=0.3
        extrude(amount=0.3, mode=Mode.ADD)
    return part.part


def model_28891_f7d9b65b_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch7 -> Extrude3 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 17 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 20.3296977755, perimeter: 37.289229088
            with BuildLine():
                CenterArc((0, 5.25), 1.5, -70.5287793655, 321.057558731)
                Line((-0.5, 3.8357864376), (-0.5, 0.75))
                Line((-4, 0.75), (-0.5, 0.75))
                Line((-4, -0.75), (-4, 0.75))
                Line((4, -0.75), (-4, -0.75))
                Line((4, 0.75), (4, -0.75))
                Line((0.5, 0.75), (4, 0.75))
                Line((0.5, 3.8357864376), (0.5, 0.75))
            make_face()
            with BuildLine():
                CenterArc((0, 5.25), 0.75, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=8
        extrude(amount=8)

        # Sketch8 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 8 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.5), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 7.3002525317, perimeter: 12.7331256881
            with BuildLine():
                Line((4.5, 2.75), (4.5, 3.8357864376))
                Line((4.5, 2.75), (6, 2.75))
                Line((6, 2.75), (6.5, 0.75))
                Line((8, 0.75), (6.5, 0.75))
                Line((8, 3.8357864376), (8, 0.75))
                Line((8, 3.8357864376), (4.5, 3.8357864376))
            make_face()
            # Profile area: 24.3101463203, perimeter: 38.029158696
            with BuildLine():
                Line((0.5, 3.8357864376), (0, 3.8357864376))
                Line((0.5, 7), (0.5, 3.8357864376))
                Line((4.5, 7), (0.5, 7))
                Line((4.5, 3.8357864376), (4.5, 7))
                Line((8, 3.8357864376), (4.5, 3.8357864376))
                Line((8, 7.6003657856), (8, 3.8357864376))
                Line((-1, 7.6003657856), (8, 7.6003657856))
                Line((-1, 0.75), (-1, 7.6003657856))
                Line((0, 0.75), (-1, 0.75))
                Line((0, 3.8357864376), (0, 0.75))
            make_face()
            # Profile area: 1.5428932188, perimeter: 7.1715728753
            with BuildLine():
                Line((0, 3.8357864376), (0, 0.75))
                Line((0.5, 0.75), (0, 0.75))
                Line((0.5, 3.8357864376), (0.5, 0.75))
                Line((0.5, 3.8357864376), (0, 3.8357864376))
            make_face()
        # Symmetric extrude, each_side=2
        extrude(amount=2, both=True, mode=Mode.SUBTRACT)
    return part.part


def model_28892_073bb12b_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 17 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 20.3296977755, perimeter: 37.289229088
            with BuildLine():
                CenterArc((0, 5.25), 1.5, -70.5287793655, 321.057558731)
                Line((-0.5, 3.8357864376), (-0.5, 0.75))
                Line((-4, 0.75), (-0.5, 0.75))
                Line((-4, -0.75), (-4, 0.75))
                Line((4, -0.75), (-4, -0.75))
                Line((4, 0.75), (4, -0.75))
                Line((0.5, 0.75), (4, 0.75))
                Line((0.5, 3.8357864376), (0.5, 0.75))
            make_face()
            with BuildLine():
                CenterArc((0, 5.25), 0.75, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=8
        extrude(amount=8)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 12 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 4), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 46.25, perimeter: 53
            with BuildLine():
                Line((6.5, 2.75), (6.5, 0.75))
                Line((8, 0.75), (6.5, 0.75))
                Line((8, 0.75), (8, 10))
                Line((-1, 10), (8, 10))
                Line((-1, 0.75), (-1, 10))
                Line((0, 0.75), (-1, 0.75))
                Line((0.5, 0.75), (0, 0.75))
                Line((0.5, 9), (0.5, 0.75))
                Line((4.5, 9), (0.5, 9))
                Line((4.5, 2.75), (4.5, 9))
                Line((6.5, 2.75), (4.5, 2.75))
            make_face()
        # OneSide extrude, distance=-7
        extrude(amount=-7, mode=Mode.SUBTRACT)
    return part.part


def model_28908_ecdb7553_0000():
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
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 25.9181393921, perimeter: 34.5575191895
            with BuildLine():
                CenterArc((0, 0), 3.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=10
        extrude(amount=10)
    return part.part


def model_28933_ac11416d_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 51.2472301617, perimeter: 54.0611670558
            with BuildLine():
                CenterArc((0, 0), 5.25, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 3.3541019662, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=2
        extrude(amount=2)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 2), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 3.2226796462, perimeter: 7.7522735307
            with BuildLine():
                Line((0.6561538088, 6.7494193962), (-0.5000000075, 6.7494193962))
                Line((-0.5000000075, 6.7494193962), (-1.3000000194, 5.4000000805))
                Line((-1.3000000194, 5.4000000805), (-1.3000000194, 5.0865017399))
                CenterArc((0, 0), 5.25, 73.8971387532, 30.4395257642)
                Line((1.4561538207, 5.4000000805), (1.4561538207, 5.0440178479))
                Line((0.6561538088, 6.7494193962), (1.4561538207, 5.4000000805))
            make_face()
        # OneSide extrude, distance=-2
        extrude(amount=-2, mode=Mode.ADD)
    return part.part


def model_29592_c3dae39d_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 5.0670751144, perimeter: 7.9796455948
            Circle(1.2700000405)
        # OneSide extrude, distance=2.54
        extrude(amount=2.54)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2.54, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.012667687, perimeter: 0.398982267
            Circle(0.0635)
        # OneSide extrude, distance=-1.905
        extrude(amount=-1.905, mode=Mode.SUBTRACT)
    return part.part


def model_29733_00b4a1fc_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> 押し出し1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 9 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.7671458676, perimeter: 5.3561944902
            with BuildLine():
                Line((0, 10), (0, 8.5))
                Line((1.5, 8.5), (0, 8.5))
                CenterArc((0, 8.5), 1.5, 0, 90)
            make_face()
            # Profile area: 11.75, perimeter: 19.2360679775
            with BuildLine():
                Line((1.5, 8.5), (0, 8.5))
                Line((0, 8.5), (0, 0))
                Line((0, 0), (0.5, 0))
                Line((0.5, 0), (1.5, 2))
                Line((1.5, 2), (1.5, 8.5))
            make_face()
        # OneSide extrude, distance=-3
        extrude(amount=-3)
    return part.part


def model_29737_245fd8bb_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 4380.0262717517, perimeter: 312.7689264344
            with BuildLine():
                Line((0, 0), (60.96, 0))
                Line((49.7273701626, 69.6183182276), (60.96, 0))
                Line((63.4999990463, 88.8999986649), (49.7273701626, 69.6183182276))
                Line((0, 88.8999986649), (63.4999990463, 88.8999986649))
                Line((12.6999998093, 17.779999733), (0, 88.8999986649))
                Line((0, 0), (12.6999998093, 17.779999733))
            make_face()
        # Symmetric extrude, each_side=0.762
        extrude(amount=0.762, both=True)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 88.8999986649, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 763.8694294193, perimeter: 300.7359960327
            with BuildLine():
                Line((-68.57999897, 5.842), (5.08, 5.842))
                Line((-68.57999897, -5.842), (-68.57999897, 5.842))
                Line((5.08, -5.842), (-68.57999897, -5.842))
                Line((5.08, 5.842), (5.08, -5.842))
            make_face()
            with BuildLine():
                Line((-63.4999990463, 0.762), (-63.4999990463, -0.762))
                Line((-63.4999990463, 0.762), (0, 0.762))
                Line((0, -0.762), (0, 0.762))
                Line((-63.4999990463, -0.762), (0, -0.762))
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 96.7739985466, perimeter: 130.0479980927
            with BuildLine():
                Line((-63.4999990463, -0.762), (0, -0.762))
                Line((0, -0.762), (0, 0.762))
                Line((-63.4999990463, 0.762), (0, 0.762))
                Line((-63.4999990463, 0.762), (-63.4999990463, -0.762))
            make_face()
        # OneSide extrude, distance=1.524
        extrude(amount=1.524, mode=Mode.ADD)
    return part.part


def model_29746_74549e58_0001():
    """Model: Pieza6 v7"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 6 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.2051620437, perimeter: 2.811435982
            with BuildLine():
                Line((-0.1658218906, 0), (-0.1658218906, 0.8470933824))
                Line((-0.1658218906, 0), (0, 0))
                Line((0, 0), (0, 0.8242406666))
                CenterArc((-0.38461653, 0.8242406666), 0.38461653, 0, 77.6800548142)
                Line((-0.3025507118, 1.2), (-0.3495339111, 1.0414100721))
                CenterArc((-0.38461653, 0.8242406666), 0.219984865, 5.9628225896, 74.8606122341)
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 10 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))) as sk:
            # Profile area: 2.2372740337, perimeter: 9.6556575601
            with BuildLine():
                Line((-2, 0.8242406666), (-2, 0.6661114275))
                Line((-1.60050243, 0.8242406666), (-2, 0.8242406666))
                Line((-1.60050243, 0.8242406666), (-1.2440690228, 1.2))
                Line((-1.2440690228, 1.2), (-0.4180639521, 1.2))
                Line((-0.4180639521, 0.931686987), (-0.4180639521, 1.2))
                Line((-0.4180639521, 0.931686987), (-0.7000000104, 0.931686987))
                Line((-0.7000000104, 0.931686987), (-0.7000000104, 0.8242406666))
                Line((0, 0.8242406666), (-0.7000000104, 0.8242406666))
                Line((0, 0.6515877491), (0, 0.8242406666))
                Line((0, 0.6515877491), (0.400000006, 0.6515877491))
                Line((0.400000006, 0.6515877491), (0.400000006, 1.5707288368))
                Line((0.400000006, 1.5707288368), (-2.8000000417, 1.5707288368))
                Line((-2.8000000417, 1.5707288368), (-2.8000000417, 0.6661114275))
                Line((-2.8000000417, 0.6661114275), (-2, 0.6661114275))
            make_face()
        # TwoSides extrude, along=0.9, against=-0.7
        extrude(amount=0.9, mode=Mode.SUBTRACT)
        extrude(sk.sketch, amount=-0.7, mode=Mode.SUBTRACT)
    return part.part


def model_29746_74549e58_0002():
    """Model: Pieza 5 v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 23 constraints, 10 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.398271564, perimeter: 18.4568583471
            with BuildLine():
                Line((-2.525, -0.475), (-2.525, 0.475))
                Line((-2.525, -0.475), (-0.025, -0.475))
                Line((-0.025, -0.475), (-0.025, -0.2))
                Line((-0.025, -0.2), (2.975, -0.2))
                Line((2.975, 0.2), (2.975, -0.2))
                Line((-0.025, 0.2), (2.975, 0.2))
                Line((-0.025, 0.475), (-0.025, 0.2))
                Line((-2.525, 0.475), (-0.025, 0.475))
            make_face()
            with BuildLine():
                Line((-2.325, -0.275), (-2.325, 0.275))
                Line((-2.325, 0.275), (-0.225, 0.275))
                Line((-0.225, 0.275), (-0.225, 0.225))
                CenterArc((0, 0.225), 0.225, 180, 90)
                CenterArc((0, -0.225), 0.225, 90, 90)
                Line((-0.225, -0.275), (-0.225, -0.225))
                Line((-2.325, -0.275), (-0.225, -0.275))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.9
        extrude(amount=0.9)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.9, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1, perimeter: 5.8
            with BuildLine():
                Line((-0.475, 0.2), (-0.475, -0.2))
                Line((-2.975, 0.2), (-0.475, 0.2))
                Line((-2.975, -0.2), (-2.975, 0.2))
                Line((-2.975, -0.2), (-0.475, -0.2))
            make_face()
        # OneSide extrude, distance=0.7
        extrude(amount=0.7, mode=Mode.ADD)
    return part.part


def model_29746_74549e58_0007():
    """Model: Pieza 10 v4 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 14 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.145, perimeter: 3
            with BuildLine():
                Line((0.6, 0.2), (0.6, 0))
                Line((-0.6, 0.2), (0.6, 0.2))
                Line((-0.6, 0), (-0.6, 0.2))
                Line((-0.475, 0), (-0.6, 0))
                Line((-0.475, 0.1), (-0.475, 0))
                Line((0.475, 0.1), (-0.475, 0.1))
                Line((0.475, 0), (0.475, 0.1))
                Line((0.6, 0), (0.475, 0))
            make_face()
        # Symmetric extrude, each_side=0.65
        extrude(amount=0.65, both=True)

        # Sketch2 -> Extrude2 (Intersect)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2312828343, perimeter: 2.2152426184
            with BuildLine():
                Line((0.6, -0.4734890091), (0.6, 0.4734890091))
                CenterArc((0.0001588588, 0.457482097), 1.107482097, -57.2056009019, 32.8069451824)
                CenterArc((0.0001588588, -0.457482097), 1.107482097, 24.3986557195, 32.8069451824)
            make_face()
            # Profile area: 0.2309820279, perimeter: 2.214077047
            with BuildLine():
                Line((-0.6, 0.4732842214), (-0.6, -0.4732842214))
                CenterArc((0.0001588588, -0.457482097), 1.107482097, 122.813954888, 32.7873893925)
                CenterArc((0.0001588588, 0.457482097), 1.107482097, -155.6013442805, 32.7873893925)
            make_face()
            # Profile area: 1.4235472124, perimeter: 4.4298616337
            with BuildLine():
                CenterArc((0.0001588588, -0.457482097), 1.107482097, 57.2056009019, 32.7943993964)
                CenterArc((0.0001588588, -0.457482097), 1.107482097, 90.0000002983, 32.8139545897)
                Line((-0.6, 0.4732842214), (-0.6, -0.4732842214))
                CenterArc((0.0001588588, 0.457482097), 1.107482097, -122.813954888, 32.8139474208)
                CenterArc((0.0001588588, 0.457482097), 1.107482097, -90.0000074672, 32.7944065653)
                Line((0.6, -0.4734890091), (0.6, 0.4734890091))
            make_face()
        # OneSide extrude, distance=-0.8
        extrude(amount=-0.8, mode=Mode.INTERSECT)
    return part.part


def model_30035_a64218e0_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 64, perimeter: 32
            with BuildLine():
                Line((-4.5, 10), (3.5, 10))
                Line((-4.5, 2), (-4.5, 10))
                Line((3.5, 2), (-4.5, 2))
                Line((3.5, 10), (3.5, 2))
            make_face()
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)
    return part.part


def model_30246_6e835e6d_0001():
    """Model: rotar v4"""
    with BuildPart() as part:
        # Sketch1 -> 押し出し1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 10 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 164.7285278202, perimeter: 84.8230016469
            with BuildLine():
                CenterArc((8.0884572681, -9), 18, 90, 60)
                CenterArc((8.0884572681, 9), 18, -150, 60)
                CenterArc((-7.5, 0), 18, -30, 60)
            make_face()
            with BuildLine():
                CenterArc((2.8923048454, 0), 4.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=8
        extrude(amount=8)

        # Sketch1 -> 押し出し3 (Join)
        # Sketch on YZ construction plane
        # Sketch has 10 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 35.3429173529, perimeter: 47.1238898038
            with BuildLine():
                CenterArc((2.8923048454, 0), 4.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((2.8923048454, 0), 3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=5
        extrude(amount=5, mode=Mode.ADD)

        # Sketch3 -> 押し出し4 (Cut)
        # Sketch on YZ construction plane
        # Sketch has 9 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.7039103626, perimeter: 3.5222076415
            with BuildLine():
                CenterArc((7.7233984827, -8.3708529424), 0.45, -47.019026041, 334.3208231862)
                Line((7.8572306521, -8.8004911046), (8.0412173642, -9.1173571087))
                Line((8.1938897995, -8.9819941177), (8.0412173642, -9.1173571087))
                Line((8.0301884415, -8.7000640011), (8.1938897995, -8.9819941177))
            make_face()
        # OneSide extrude, distance=9
        extrude(amount=9, mode=Mode.SUBTRACT)
    return part.part


MODELS = {
    "model_24412_a8e106be_0003": {"func": model_24412_a8e106be_0003, "volume": 4.7040000659, "area": 52.2000000328},
    "model_24413_786c8353_0000": {"func": model_24413_786c8353_0000, "volume": 5642.706387813, "area": 4666.7928867792},
    "model_24443_996411f9_0000": {"func": model_24443_996411f9_0000, "volume": 36.5092336255, "area": 80.6446834177},
    "model_24476_568e9ca0_0004": {"func": model_24476_568e9ca0_0004, "volume": 0.1320533052, "area": 2.8039786316},
    "model_24476_568e9ca0_0007": {"func": model_24476_568e9ca0_0007, "volume": 0.2061916732, "area": 3.8570871852},
    "model_24476_568e9ca0_0008": {"func": model_24476_568e9ca0_0008, "volume": 0.2841846316, "area": 4.540578125},
    "model_24476_568e9ca0_0012": {"func": model_24476_568e9ca0_0012, "volume": 0.7186840474, "area": 7.3014004661},
    "model_24476_568e9ca0_0030": {"func": model_24476_568e9ca0_0030, "volume": 0.3233569937, "area": 5.5537957487},
    "model_24476_568e9ca0_0033": {"func": model_24476_568e9ca0_0033, "volume": 0.3332994995, "area": 5.2016149329},
    "model_24504_493cee15_0006": {"func": model_24504_493cee15_0006, "volume": 496.2911379189, "area": 483.7424367998},
    "model_24511_4d45ac57_0000": {"func": model_24511_4d45ac57_0000, "volume": 12.348, "area": 39.9},
    "model_24518_b99235fc_0002": {"func": model_24518_b99235fc_0002, "volume": 542.2098630613, "area": 802.9129856331},
    "model_24592_73276617_0000": {"func": model_24592_73276617_0000, "volume": 75.9749022876, "area": 121.0141490163},
    "model_24603_a4021250_0001": {"func": model_24603_a4021250_0001, "volume": 56.4165655266, "area": 570.2099789104},
    "model_24674_faae40ed_0000": {"func": model_24674_faae40ed_0000, "volume": 1646.0761567984, "area": 1147.9910668807},
    "model_24692_86ddfd16_0000": {"func": model_24692_86ddfd16_0000, "volume": 89.7488939593, "area": 211.9545468391},
    "model_24712_da77fe8f_0000": {"func": model_24712_da77fe8f_0000, "volume": 8.0507699246, "area": 39.3153563594},
    "model_24735_384e3c90_0000": {"func": model_24735_384e3c90_0000, "volume": 0.30568114, "area": 3.448908321},
    "model_24849_f328b6fc_0001": {"func": model_24849_f328b6fc_0001, "volume": 0.8056877779, "area": 11.6078042732},
    "model_24904_6a007751_0000": {"func": model_24904_6a007751_0000, "volume": 0.131608463, "area": 2.1037107837},
    "model_24904_6a007751_0002": {"func": model_24904_6a007751_0002, "volume": 0.0079261059, "area": 0.6270442306},
    "model_24907_c72322ea_0001": {"func": model_24907_c72322ea_0001, "volume": 0.5805663224, "area": 4.6244243861},
    "model_24907_c72322ea_0005": {"func": model_24907_c72322ea_0005, "volume": 0.0879645943, "area": 3.9584067435},
    "model_24978_5081ee1e_0012": {"func": model_24978_5081ee1e_0012, "volume": 0.6996333115, "area": 4.9464784109},
    "model_25132_c8588afc_0005": {"func": model_25132_c8588afc_0005, "volume": 3.7391770694, "area": 30.197186716},
    "model_25135_e643b3a2_0000": {"func": model_25135_e643b3a2_0000, "volume": 62.0464549084, "area": 114.668131856},
    "model_25179_1775e380_0000": {"func": model_25179_1775e380_0000, "volume": 3.1985850503, "area": 35.7858456379},
    "model_25186_e5476b73_0000": {"func": model_25186_e5476b73_0000, "volume": 25.9181393921, "area": 211.6648050356},
    "model_25203_1cc0cb3c_0013": {"func": model_25203_1cc0cb3c_0013, "volume": 0.1322414158, "area": 2.2006856538},
    "model_25203_92cee759_0008": {"func": model_25203_92cee759_0008, "volume": 0.7120663882, "area": 8.0931835553},
    "model_25211_336c083f_0009": {"func": model_25211_336c083f_0009, "volume": 59.0172306214, "area": 403.821383376},
    "model_25216_ff3bf7e2_0000": {"func": model_25216_ff3bf7e2_0000, "volume": 137.1753430643, "area": 331.4645059855},
    "model_25216_ff3bf7e2_0006": {"func": model_25216_ff3bf7e2_0006, "volume": 1.6242439957, "area": 34.113714877},
    "model_25249_dd7b7c5a_0000": {"func": model_25249_dd7b7c5a_0000, "volume": 2.1109242113, "area": 9.8839714427},
    "model_25294_84dd76e8_0000": {"func": model_25294_84dd76e8_0000, "volume": 823.2854132356, "area": 741.3716694115},
    "model_25294_96063cf2_0008": {"func": model_25294_96063cf2_0008, "volume": 23.7095144205, "area": 134.9223522197},
    "model_25335_491efa81_0005": {"func": model_25335_491efa81_0005, "volume": 0.9244136383, "area": 21.8497769057},
    "model_25335_491efa81_0009": {"func": model_25335_491efa81_0009, "volume": 1.7602654222, "area": 15.5944994453},
    "model_25335_491efa81_0011": {"func": model_25335_491efa81_0011, "volume": 1.6702473692, "area": 24.7910930276},
    "model_25338_a9cdf751_0000": {"func": model_25338_a9cdf751_0000, "volume": 0.1079729746, "area": 3.6602788578},
    "model_25346_11e33bbb_0001": {"func": model_25346_11e33bbb_0001, "volume": 73.3611088237, "area": 492.925035666},
    "model_25364_b3985755_0002": {"func": model_25364_b3985755_0002, "volume": 354.9069433995, "area": 289.3216065899},
    "model_25381_9c263e4d_0005": {"func": model_25381_9c263e4d_0005, "volume": 4.3636103192, "area": 20.7904604533},
    "model_25381_9c263e4d_0008": {"func": model_25381_9c263e4d_0008, "volume": 6.5164723107, "area": 27.4380073101},
    "model_25387_9dc6258b_0004": {"func": model_25387_9dc6258b_0004, "volume": 0.2780785006, "area": 3.6666477292},
    "model_25416_a2472889_0000": {"func": model_25416_a2472889_0000, "volume": 4.08407045, "area": 34.1805280748},
    "model_25416_b70bf79a_0000": {"func": model_25416_b70bf79a_0000, "volume": 0.014795627, "area": 0.5153125865},
    "model_25559_893f0c7c_0004": {"func": model_25559_893f0c7c_0004, "volume": 194.7787445226, "area": 202.6327261565},
    "model_25560_7660b86f_0005": {"func": model_25560_7660b86f_0005, "volume": 1492.2565104552, "area": 973.8937226128},
    "model_25560_7660b86f_0008": {"func": model_25560_7660b86f_0008, "volume": 26272.1470131869, "area": 6007.5794705381},
    "model_25839_fac364bf_0000": {"func": model_25839_fac364bf_0000, "volume": 3.3296907591, "area": 26.8184601862},
    "model_26086_bf892d7f_0010": {"func": model_26086_bf892d7f_0010, "volume": 21071.4212705743, "area": 5756.6703238533},
    "model_26086_bf892d7f_0023": {"func": model_26086_bf892d7f_0023, "volume": 28071.1320754717, "area": 6877.003443507},
    "model_26086_bf892d7f_0027": {"func": model_26086_bf892d7f_0027, "volume": 60815.5481964737, "area": 13119.568709917},
    "model_26243_b080f743_0000": {"func": model_26243_b080f743_0000, "volume": 74.2126477704, "area": 146.8743494847},
    "model_26384_83eddf22_0007": {"func": model_26384_83eddf22_0007, "volume": 0.4453148009, "area": 8.411344153},
    "model_26384_83eddf22_0022": {"func": model_26384_83eddf22_0022, "volume": 0.0264465188, "area": 0.7953444457},
    "model_26384_83eddf22_0027": {"func": model_26384_83eddf22_0027, "volume": 0.2865273626, "area": 4.3300964244},
    "model_26384_83eddf22_0030": {"func": model_26384_83eddf22_0030, "volume": 1.8563042583, "area": 10.1594491316},
    "model_26388_a3367cba_0000": {"func": model_26388_a3367cba_0000, "volume": 0.8482300165, "area": 9.2362824016},
    "model_26388_a3367cba_0004": {"func": model_26388_a3367cba_0004, "volume": 3.8849810866, "area": 46.1380099501},
    "model_26410_13c212a5_0002": {"func": model_26410_13c212a5_0002, "volume": 0.0576357006, "area": 0.9835689915},
    "model_26764_ab35159a_0001": {"func": model_26764_ab35159a_0001, "volume": 6.9208628331, "area": 271.1366352528},
    "model_26764_ab35159a_0008": {"func": model_26764_ab35159a_0008, "volume": 1.1396010632, "area": 10.9374452576},
    "model_26766_1aaa348c_0000": {"func": model_26766_1aaa348c_0000, "volume": 0.1807450909, "area": 2.4993690689},
    "model_26768_c4df841f_0008": {"func": model_26768_c4df841f_0008, "volume": 145.3732190285, "area": 228.6231769746},
    "model_26768_c4df841f_0012": {"func": model_26768_c4df841f_0012, "volume": 6.0660380696, "area": 27.1530795362},
    "model_26768_c4df841f_0016": {"func": model_26768_c4df841f_0016, "volume": 191.0311546983, "area": 203.1360074669},
    "model_26768_c4df841f_0017": {"func": model_26768_c4df841f_0017, "volume": 25.9055730215, "area": 65.2194634885},
    "model_26768_c4df841f_0019": {"func": model_26768_c4df841f_0019, "volume": 40.2023140199, "area": 88.4000190423},
    "model_26773_35d26b3c_0012": {"func": model_26773_35d26b3c_0012, "volume": 3.035153014, "area": 16.5411816409},
    "model_26942_279de65e_0006": {"func": model_26942_279de65e_0006, "volume": 751.0369937488, "area": 488.9103567149},
    "model_26942_279de65e_0007": {"func": model_26942_279de65e_0007, "volume": 7043.3340357836, "area": 18593.9026718692},
    "model_26942_279de65e_0009": {"func": model_26942_279de65e_0009, "volume": 5652.338043527, "area": 15533.7574354306},
    "model_26942_279de65e_0014": {"func": model_26942_279de65e_0014, "volume": 2762.6380397505, "area": 7445.9672880895},
    "model_27054_342fcf5c_0014": {"func": model_27054_342fcf5c_0014, "volume": 0.5970074065, "area": 17.5294815132},
    "model_27054_342fcf5c_0025": {"func": model_27054_342fcf5c_0025, "volume": 0.4928798387, "area": 14.4175062813},
    "model_27054_342fcf5c_0034": {"func": model_27054_342fcf5c_0034, "volume": 0.6482503711, "area": 19.0615866549},
    "model_27070_53448c4a_0007": {"func": model_27070_53448c4a_0007, "volume": 1.5738138169, "area": 12.8132211887},
    "model_27663_023746a1_0011": {"func": model_27663_023746a1_0011, "volume": 0.0337523193, "area": 1.5546764},
    "model_27663_023746a1_0021": {"func": model_27663_023746a1_0021, "volume": 0.4074745884, "area": 3.6757990963},
    "model_27663_023746a1_0023": {"func": model_27663_023746a1_0023, "volume": 0.01208024, "area": 0.3240024},
    "model_27679_501db761_0001": {"func": model_27679_501db761_0001, "volume": 0.0617962323, "area": 1.8824708162},
    "model_27679_501db761_0004": {"func": model_27679_501db761_0004, "volume": 6.2475391434, "area": 27.7883332945},
    "model_27679_501db761_0006": {"func": model_27679_501db761_0006, "volume": 160.025514603, "area": 266.2873908831},
    "model_27679_501db761_0009": {"func": model_27679_501db761_0009, "volume": 21.9826279423, "area": 57.2434284316},
    "model_27679_501db761_0010": {"func": model_27679_501db761_0010, "volume": 1.4715125742, "area": 9.3185921291},
    "model_27679_501db761_0013": {"func": model_27679_501db761_0013, "volume": 1.8799196191, "area": 10.135406219},
    "model_27679_501db761_0023": {"func": model_27679_501db761_0023, "volume": 27.0713356372, "area": 92.6766188234},
    "model_27682_04277f62_0000": {"func": model_27682_04277f62_0000, "volume": 32.9435259637, "area": 84.7444618306},
    "model_27682_04277f62_0003": {"func": model_27682_04277f62_0003, "volume": 0.7508406442, "area": 5.8433623357},
    "model_27694_7801dc67_0009": {"func": model_27694_7801dc67_0009, "volume": 127.3382176711, "area": 552.6891524829},
    "model_27839_4a077326_0001": {"func": model_27839_4a077326_0001, "volume": 1.1938052084, "area": 7.6654860748},
    "model_27839_4a077326_0008": {"func": model_27839_4a077326_0008, "volume": 0.2764601535, "area": 5.0265482457},
    "model_27839_4a077326_0011": {"func": model_27839_4a077326_0011, "volume": 2.6766369409, "area": 14.7026536188},
    "model_27839_4a077326_0019": {"func": model_27839_4a077326_0019, "volume": 0.8003649977, "area": 14.3254198036},
    "model_28119_f4fb1c4c_0001": {"func": model_28119_f4fb1c4c_0001, "volume": 51.103763579, "area": 108.8661668559},
    "model_28287_522a580c_0000": {"func": model_28287_522a580c_0000, "volume": 4.2983587731, "area": 20.9311269355},
    "model_28300_b3a6ab79_0002": {"func": model_28300_b3a6ab79_0002, "volume": 97.2322926286, "area": 125.977865409},
    "model_28300_b3a6ab79_0005": {"func": model_28300_b3a6ab79_0005, "volume": 2.112290255, "area": 36.3450051},
    "model_28300_b3a6ab79_0011": {"func": model_28300_b3a6ab79_0011, "volume": 0.0343429174, "area": 0.6426105668},
    "model_28300_b3a6ab79_0013": {"func": model_28300_b3a6ab79_0013, "volume": 0.2895243111, "area": 2.8688935737},
    "model_28300_b3a6ab79_0014": {"func": model_28300_b3a6ab79_0014, "volume": 0.0596902604, "area": 4.5590792589},
    "model_28446_d757d32d_0022": {"func": model_28446_d757d32d_0022, "volume": 0.5796238446, "area": 5.6077428867},
    "model_28446_d757d32d_0026": {"func": model_28446_d757d32d_0026, "volume": 374.4, "area": 2538.6},
    "model_28457_e541aa9b_0000": {"func": model_28457_e541aa9b_0000, "volume": 49.824, "area": 371.58},
    "model_28891_f7d9b65b_0000": {"func": model_28891_f7d9b65b_0000, "volume": 132.8187911019, "area": 272.3778647159},
    "model_28892_073bb12b_0000": {"func": model_28892_073bb12b_0000, "volume": 133.3187911019, "area": 273.8163119031},
    "model_28908_ecdb7553_0000": {"func": model_28908_ecdb7553_0000, "volume": 259.1813939212, "area": 397.4114706791},
    "model_28933_ac11416d_0000": {"func": model_28933_ac11416d_0000, "volume": 108.9398196158, "area": 221.4100318949},
    "model_29592_c3dae39d_0000": {"func": model_29592_c3dae39d_0000, "volume": 12.8462388469, "area": 31.1625112582},
    "model_29733_00b4a1fc_0000": {"func": model_29733_00b4a1fc_0000, "volume": 40.5514376029, "area": 91.8110791384},
    "model_29737_245fd8bb_0000": {"func": model_29737_245fd8bb_0000, "volume": 7986.7806223696, "area": 11024.5797550887},
    "model_29746_74549e58_0001": {"func": model_29746_74549e58_0001, "volume": 0.3374619361, "area": 5.2183917746},
    "model_29746_74549e58_0002": {"func": model_29746_74549e58_0002, "volume": 2.8584444076, "area": 25.4677156404},
    "model_29746_74549e58_0007": {"func": model_29746_74549e58_0007, "volume": 0.16785171, "area": 3.7538842377},
    "model_30035_a64218e0_0000": {"func": model_30035_a64218e0_0000, "volume": 96, "area": 176},
    "model_30246_6e835e6d_0001": {"func": model_30246_6e835e6d_0001, "volume": 1489.0500533624, "area": 1053.07246847},
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
