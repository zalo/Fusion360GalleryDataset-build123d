"""Batch 001 - passing/07_16to20ops
33 models bundled from Fusion360 Gallery reconstructions.
"""

from build123d import *
from build123d import Edge, BuildLine
from collections import Counter
from OCP.BRepBuilderAPI import BRepBuilderAPI_MakeEdge
from OCP.Geom import Geom_BSplineCurve
from OCP.TColStd import TColStd_Array1OfReal, TColStd_Array1OfInteger
from OCP.TColgp import TColgp_Array1OfPnt
from OCP.gp import gp_Pnt


# Description: This is a rectangular housing or enclosure with a tilted/angled top section, featuring multiple internal compartments, access openings, and what appears to be mounting flanges or feet at the base.
def model_100155_57ec5fc6_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 13.44, perimeter: 15.2
            with BuildLine():
                Line((0, 4.8), (0, 0))
                Line((0, 0), (2.8, 0))
                Line((2.8, 0), (2.8, 4.8))
                Line((2.8, 4.8), (0, 4.8))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 10 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(2.8, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.49, perimeter: 2.8
            with BuildLine():
                Line((-0.3, 4.1), (-1, 4.1))
                Line((-0.3, 4.8), (-0.3, 4.1))
                Line((-1, 4.8), (-0.3, 4.8))
                Line((-1, 4.1), (-1, 4.8))
            make_face()
        # OneSide extrude, distance=-2.8
        extrude(amount=-2.8, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(2.8, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.1302636245, perimeter: 2.2982938447
            with BuildLine():
                Line((-1, 1.5659341681), (-1, 1.4178174918))
                CenterArc((-0.78, 1.9000000299), 0.4, 123.3670129692, 113.2659740615)
                Line((-1, 2.3821825679), (-1, 2.2340658916))
                CenterArc((-0.78, 1.9000000299), 0.53, 114.5252576384, 130.9494847232)
            make_face()
            # Profile area: 0.1247774677, perimeter: 2.1987676605
            with BuildLine():
                CenterArc((-0.78, 1.9000000299), 0.53, -114.5252576384, 114.5252610136)
                Line((-0.38, 1.9000000611), (-0.25, 1.9000000611))
                CenterArc((-0.78, 1.9000000299), 0.4, -123.3670129692, 123.3670174414)
                Line((-1, 1.5659341681), (-1, 1.4178174918))
            make_face()
            # Profile area: 0.0938164903, perimeter: 2.0372202411
            with BuildLine():
                Line((-1, 2.3821825679), (-1, 2.2340658916))
                CenterArc((-0.78, 1.9000000299), 0.4, 0.0000044721, 123.3670084971)
                Line((-0.38, 2.2477068029), (-0.38, 1.9000000611))
                CenterArc((-0.78, 1.9000000299), 0.53, 40.9993536502, 73.5259039882)
            make_face()
            # Profile area: 0.0309609692, perimeter: 0.8569607781
            with BuildLine():
                CenterArc((-0.78, 1.9000000299), 0.53, 0.0000033752, 40.999350275)
                Line((-0.38, 2.2477068029), (-0.38, 1.9000000611))
                Line((-0.38, 1.9000000611), (-0.25, 1.9000000611))
            make_face()
        # OneSide extrude, distance=-2.8
        extrude(amount=-2.8, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(2.8, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0846546446, perimeter: 1.4588773947
            with BuildLine():
                Line((-1, 2.2340658916), (-1, 1.5659341681))
                CenterArc((-0.78, 1.9000000299), 0.4, 123.3670129692, 56.6329870308)
                CenterArc((-0.78, 1.9000000299), 0.4, 180, 56.6329870308)
            make_face()
            # Profile area: 0.4180001799, perimeter: 2.3906601753
            with BuildLine():
                CenterArc((-0.78, 1.9000000299), 0.4, -123.3670129692, 246.7340259385)
                Line((-1, 2.2340658916), (-1, 1.5659341681))
            make_face()
        # OneSide extrude, distance=-2.8
        extrude(amount=-2.8, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 18 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 1.692, perimeter: 6.14
            with BuildLine():
                Line((-1.76, 0.4), (-1.04, 0.4))
                Line((-1.04, 0.4), (-1.04, 2.75))
                Line((-1.04, 2.75), (-1.76, 2.75))
                Line((-1.76, 2.75), (-1.76, 0.4))
            make_face()
        # OneSide extrude, distance=-1.4
        extrude(amount=-1.4, mode=Mode.SUBTRACT)

        # Sketch6 -> Extrude6 (Cut)
        # Sketch on BRepFace
        # Sketch has 22 constraints, 9 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.3526, perimeter: 2.5
            with BuildLine():
                Line((0.85, 3.12), (0.85, 3.94))
                Line((0.42, 3.94), (0.85, 3.94))
                Line((0.42, 3.12), (0.42, 3.94))
                Line((0.85, 3.12), (0.42, 3.12))
            make_face()
            # Profile area: 0.3526, perimeter: 2.5
            with BuildLine():
                Line((1.93, 3.94), (2.36, 3.94))
                Line((1.93, 3.12), (1.93, 3.94))
                Line((2.36, 3.12), (1.93, 3.12))
                Line((2.36, 3.94), (2.36, 3.12))
            make_face()
        # OneSide extrude, distance=-1.05
        extrude(amount=-1.05, mode=Mode.SUBTRACT)

        # Sketch7 -> Extrude7 (Join)
        # Sketch on BRepFace
        # Sketch has 10 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(2.8, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.2345984314, perimeter: 3.2358404332
            with BuildLine():
                CenterArc((-1, -0.3499999701), 0.33, -52.56191685, 162.024853958)
                CenterArc((-1, -0.3499999701), 0.33, 109.462937108, 197.975146042)
            make_face()
            with BuildLine():
                CenterArc((-1, -0.3499999701), 0.185, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.2063829532, perimeter: 3.0565921404
            with BuildLine():
                Line((-0.78, 0), (0, 0))
                Line((-1, 0), (-0.78, 0))
                Line((-1, 0), (-1.1099550177, -0.0388570864))
                CenterArc((-1, -0.3499999701), 0.33, -52.56191685, 162.024853958)
                Line((0, 0), (-0.7993917677, -0.6120235132))
            make_face()
        # OneSide extrude, distance=-2.8
        extrude(amount=-2.8, mode=Mode.ADD)

        # Sketch8 -> Extrude8 (Cut)
        # Sketch on BRepFace
        # Sketch has 14 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.7563661748, perimeter: 3.6606102913
            with BuildLine():
                Line((2, -0.0388570864), (2, -0.6691622321))
                Line((0.8, -0.0388570864), (2, -0.0388570864))
                Line((0.8, -0.6691622321), (0.8, -0.0388570864))
                Line((2, -0.6691622321), (0.8, -0.6691622321))
            make_face()
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a bracket or mounting assembly with a tall, angled rectangular body featuring internal ribbed reinforcement, multiple rectangular cutouts/slots on the sides, and a wide base with two feet for stability.
def model_100155_bf644f70_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 13.44, perimeter: 15.2
            with BuildLine():
                Line((0, 4.8), (0, 0))
                Line((0, 0), (2.8, 0))
                Line((2.8, 0), (2.8, 4.8))
                Line((2.8, 4.8), (0, 4.8))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 10 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(2.8, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.49, perimeter: 2.8
            with BuildLine():
                Line((-0.3, 4.1), (-1, 4.1))
                Line((-0.3, 4.8), (-0.3, 4.1))
                Line((-1, 4.8), (-0.3, 4.8))
                Line((-1, 4.1), (-1, 4.8))
            make_face()
        # OneSide extrude, distance=-2.8
        extrude(amount=-2.8, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(2.8, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.1302636245, perimeter: 2.2982938447
            with BuildLine():
                Line((-1, 1.5659341681), (-1, 1.4178174918))
                CenterArc((-0.78, 1.9000000299), 0.4, 123.3670129692, 113.2659740615)
                Line((-1, 2.3821825679), (-1, 2.2340658916))
                CenterArc((-0.78, 1.9000000299), 0.53, 114.5252576384, 130.9494847232)
            make_face()
            # Profile area: 0.1247774677, perimeter: 2.1987676605
            with BuildLine():
                CenterArc((-0.78, 1.9000000299), 0.53, -114.5252576384, 114.5252610136)
                Line((-0.38, 1.9000000611), (-0.25, 1.9000000611))
                CenterArc((-0.78, 1.9000000299), 0.4, -123.3670129692, 123.3670174414)
                Line((-1, 1.5659341681), (-1, 1.4178174918))
            make_face()
            # Profile area: 0.0938164903, perimeter: 2.0372202411
            with BuildLine():
                Line((-1, 2.3821825679), (-1, 2.2340658916))
                CenterArc((-0.78, 1.9000000299), 0.4, 0.0000044721, 123.3670084971)
                Line((-0.38, 2.2477068029), (-0.38, 1.9000000611))
                CenterArc((-0.78, 1.9000000299), 0.53, 40.9993536502, 73.5259039882)
            make_face()
            # Profile area: 0.0309609692, perimeter: 0.8569607781
            with BuildLine():
                CenterArc((-0.78, 1.9000000299), 0.53, 0.0000033752, 40.999350275)
                Line((-0.38, 2.2477068029), (-0.38, 1.9000000611))
                Line((-0.38, 1.9000000611), (-0.25, 1.9000000611))
            make_face()
        # OneSide extrude, distance=-2.8
        extrude(amount=-2.8, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(2.8, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0846546446, perimeter: 1.4588773947
            with BuildLine():
                Line((-1, 2.2340658916), (-1, 1.5659341681))
                CenterArc((-0.78, 1.9000000299), 0.4, 123.3670129692, 56.6329870308)
                CenterArc((-0.78, 1.9000000299), 0.4, 180, 56.6329870308)
            make_face()
            # Profile area: 0.4180001799, perimeter: 2.3906601753
            with BuildLine():
                CenterArc((-0.78, 1.9000000299), 0.4, -123.3670129692, 246.7340259385)
                Line((-1, 2.2340658916), (-1, 1.5659341681))
            make_face()
        # OneSide extrude, distance=-2.8
        extrude(amount=-2.8, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 18 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 1.692, perimeter: 6.14
            with BuildLine():
                Line((-1.76, 0.4), (-1.04, 0.4))
                Line((-1.04, 0.4), (-1.04, 2.75))
                Line((-1.04, 2.75), (-1.76, 2.75))
                Line((-1.76, 2.75), (-1.76, 0.4))
            make_face()
        # OneSide extrude, distance=-1.4
        extrude(amount=-1.4, mode=Mode.SUBTRACT)

        # Sketch6 -> Extrude6 (Cut)
        # Sketch on BRepFace
        # Sketch has 22 constraints, 9 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.3526, perimeter: 2.5
            with BuildLine():
                Line((0.85, 3.12), (0.85, 3.94))
                Line((0.42, 3.94), (0.85, 3.94))
                Line((0.42, 3.12), (0.42, 3.94))
                Line((0.85, 3.12), (0.42, 3.12))
            make_face()
            # Profile area: 0.3526, perimeter: 2.5
            with BuildLine():
                Line((1.93, 3.94), (2.36, 3.94))
                Line((1.93, 3.12), (1.93, 3.94))
                Line((2.36, 3.12), (1.93, 3.12))
                Line((2.36, 3.94), (2.36, 3.12))
            make_face()
        # OneSide extrude, distance=-1.05
        extrude(amount=-1.05, mode=Mode.SUBTRACT)

        # Sketch7 -> Extrude7 (Join)
        # Sketch on BRepFace
        # Sketch has 10 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(2.8, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.2063829532, perimeter: 3.0565921404
            with BuildLine():
                Line((-0.78, 0), (0, 0))
                Line((-1, 0), (-0.78, 0))
                Line((-1, 0), (-1.1099550177, -0.0388570864))
                CenterArc((-1, -0.3499999701), 0.33, -52.56191685, 162.024853958)
                Line((0, 0), (-0.7993917677, -0.6120235132))
            make_face()
            # Profile area: 0.2345984314, perimeter: 3.2358404332
            with BuildLine():
                CenterArc((-1, -0.3499999701), 0.33, -52.56191685, 162.024853958)
                CenterArc((-1, -0.3499999701), 0.33, 109.462937108, 197.975146042)
            make_face()
            with BuildLine():
                CenterArc((-1, -0.3499999701), 0.185, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-2.8
        extrude(amount=-2.8, mode=Mode.ADD)

        # Sketch8 -> Extrude8 (Cut)
        # Sketch on BRepFace
        # Sketch has 14 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.7563661748, perimeter: 3.6606102913
            with BuildLine():
                Line((2, -0.0388570864), (2, -0.6691622321))
                Line((0.8, -0.0388570864), (2, -0.0388570864))
                Line((0.8, -0.6691622321), (0.8, -0.0388570864))
                Line((2, -0.6691622321), (0.8, -0.6691622321))
            make_face()
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.SUBTRACT)

        # Sketch10 -> Extrude9 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.8986402337, perimeter: 3.8977337452
            with BuildLine():
                Line((-2.0000000298, 0), (-0.8, 0))
                Line((-2.0000000298, -0.7488668428), (-2.0000000298, 0))
                Line((-0.8, -0.7488668428), (-2.0000000298, -0.7488668428))
                Line((-0.8, 0), (-0.8, -0.7488668428))
            make_face()
        # OneSide extrude, distance=-1.8
        extrude(amount=-1.8, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical mesh or perforated filter component with a slightly tapered, rounded top edge and vertical ribbed or corrugated surface pattern throughout its body.
def model_105907_e625e54b_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 12.5663706144, perimeter: 12.5663706144
            Circle(2)
        # OneSide extrude, distance=6
        extrude(amount=6)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))) as sk:
            # Profile area: 1.727876011, perimeter: 17.6170495767
            with BuildLine():
                CenterArc((0, 0), 1.5000000224, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.3038405005, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # TwoSides extrude, along=1, against=-0.3
        extrude(amount=1, mode=Mode.ADD)
        extrude(sk.sketch, amount=-0.3, mode=Mode.ADD)

        # Sketch11 -> Extrude6 (Join)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 6, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.3141592747, perimeter: 1.9869176828
            Circle(0.3162277707)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)
    return part.part


# Description: This is a rectangular enclosure or mounting base with a sloped/angled top lid that features internal component cutouts and mounting provisions, designed as a compact housing for electronics or mechanical assemblies.
def model_118628_c12b368f_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 112, perimeter: 44
            with BuildLine():
                Line((-7, 4), (-7, -4))
                Line((-7, -4), (7, -4))
                Line((7, -4), (7, 4))
                Line((7, 4), (-7, 4))
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.1104459833, perimeter: 1.1780938669
            with Locations((6.7510102134, -3.734302047)):
                Circle(0.1874994623)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -0.5, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.1752745516, perimeter: 3.0729474587
            with BuildLine():
                CenterArc((6.7510102134, -3.734302047), 0.3015753156, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((6.7510102134, -3.734302047), 0.1874994623, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.1104459833, perimeter: 1.1780938669
            with Locations((6.7510102134, -3.734302047)):
                Circle(0.1874994623)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 5.0519507679, perimeter: 18.5730387869
            with BuildLine():
                CenterArc((4, 0), 1.75, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((4, 0), 1.2059909312, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 2.2070829932, perimeter: 14.4815656639
            with BuildLine():
                CenterArc((-4, 0), 1.3048127591, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-4, 0), 1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)

        # Sketch7 -> Extrude7 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.5600000226, perimeter: 31.1999999881
            with BuildLine():
                Line((6, -2), (2, -2))
                Line((6, -2), (6, 2))
                Line((2, 2), (6, 2))
                Line((2, -2), (2, 2))
            make_face()
            with BuildLine():
                Line((5.8999999985, -1.8999999985), (2.1000000015, -1.8999999985))
                Line((2.1000000015, -1.8999999985), (2.1000000015, 1.8999999985))
                Line((2.1000000015, 1.8999999985), (5.8999999985, 1.8999999985))
                Line((5.8999999985, -1.8999999985), (5.8999999985, 1.8999999985))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.6
        extrude(amount=0.6, mode=Mode.ADD)

        # Sketch8 -> Extrude8 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.1600000167, perimeter: 23.1999999881
            with BuildLine():
                Line((-5.5, 1.5), (-2.5, 1.5))
                Line((-5.5, -1.5), (-5.5, 1.5))
                Line((-2.5, -1.5), (-5.5, -1.5))
                Line((-2.5, 1.5), (-2.5, -1.5))
            make_face()
            with BuildLine():
                Line((-5.3999999985, -1.3999999985), (-5.3999999985, 1.3999999985))
                Line((-5.3999999985, 1.3999999985), (-2.6000000015, 1.3999999985))
                Line((-2.6000000015, 1.3999999985), (-2.6000000015, -1.3999999985))
                Line((-2.6000000015, -1.3999999985), (-5.3999999985, -1.3999999985))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.6
        extrude(amount=0.6, mode=Mode.ADD)

        # Sketch14 -> Extrude14 (Cut)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(-7, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((3.0154483681, 0.75)):
                Circle(0.25)
        # OneSide extrude, distance=-2
        extrude(amount=-2, mode=Mode.SUBTRACT)

        # Sketch15 -> Extrude15 (Join)
        # Sketch on BRepFace
        # Sketch has 8 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.76, perimeter: 15.2
            with BuildLine():
                Line((-1, 1), (1, 1))
                Line((-1, -1), (-1, 1))
                Line((1, -1), (-1, -1))
                Line((1, 1), (1, -1))
            make_face()
            with BuildLine():
                Line((-0.9, -0.9), (-0.9, 0.9))
                Line((-0.9, 0.9), (0.9, 0.9))
                Line((0.9, 0.9), (0.9, -0.9))
                Line((0.9, -0.9), (-0.9, -0.9))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)
    return part.part


# Description: This is a motor or pump housing with a rectangular body featuring a rounded left end, a flat top surface with horizontal cooling fins or ribbing, and a stepped right side with mounting surfaces and internal cavities for component integration.
def model_118699_c3e4046a_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 217.8803883465, perimeter: 60.9760553348
            with BuildLine():
                CenterArc((-0.4502866205, -0.3307903064), 11.9898350658, 1.5809469905, 176.838106019)
                Line((-12.4355576928, 0), (11.5349844518, 0))
            make_face()
        # OneSide extrude, distance=30
        extrude(amount=30)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on YZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 20.0433384564, perimeter: 73.0852576784
            with BuildLine():
                Line((10.9896449833, 0), (11.5349844518, 0))
                CenterArc((-0.4502866205, -0.3307903064), 11.9898350658, 1.5809469905, 176.838106019)
                Line((-12.4355576928, 0), (-12.1760771132, 0))
                CenterArc((-0.5932160649, -0.5793576572), 11.5973413056, 2.8634641419, 174.2730717161)
            make_face()
        # OneSide extrude, distance=28
        extrude(amount=28, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(30, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 50.711292872, perimeter: 30.1400135194
            with BuildLine():
                Line((5.0013913965, 4.8997934113), (-4.9963306158, 4.8997934113))
                Line((5.0013913965, 9.9720781588), (5.0013913965, 4.8997934113))
                Line((-4.9963306158, 9.9720781588), (5.0013913965, 9.9720781588))
                Line((-4.9963306158, 4.8997934113), (-4.9963306158, 9.9720781588))
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2, mode=Mode.ADD)

        # Sketch5 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(32, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 11.1400551038, perimeter: 22.2239626991
            with BuildLine():
                Line((-4.9963306158, 6.0140527486), (5.0013913965, 6.0140527486))
                Line((-4.9963306158, 4.8997934113), (-4.9963306158, 6.0140527486))
                Line((5.0013913965, 4.8997934113), (-4.9963306158, 4.8997934113))
                Line((5.0013913965, 6.0140527486), (5.0013913965, 4.8997934113))
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2, mode=Mode.ADD)

        # Sketch6 -> Extrude6 (Join)
        # Sketch on BRepFace
        # Sketch has 7 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 4.9963306158), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.9370346001, perimeter: 11.8753424056
            with BuildLine():
                Line((32, 9.9720781588), (34, 9.9720781588))
                Line((32, 9.861575122), (32, 9.9720781588))
                Line((32, 9.861575122), (33.7934357642, 9.861575122))
                Line((33.7934357642, 9.861575122), (33.834361838, 6.0140527486))
                Line((34, 6.0140527486), (33.834361838, 6.0140527486))
                Line((34, 9.9720781588), (34, 6.0140527486))
            make_face()
        # OneSide extrude, distance=-10
        extrude(amount=-10, mode=Mode.ADD)

        # Sketch7 -> Extrude7 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(34, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 46.0254366913, perimeter: 28.8633489654
            with BuildLine():
                Line((-4.8000165647, 5.1039629319), (-4.8000165647, 9.861575122))
                Line((4.8740457279, 5.1039629319), (-4.8000165647, 5.1039629319))
                Line((4.8740457279, 9.861575122), (4.8740457279, 5.1039629319))
                Line((-4.8000165647, 9.861575122), (4.8740457279, 9.861575122))
            make_face()
        # OneSide extrude, distance=-2.5
        extrude(amount=-2.5, mode=Mode.SUBTRACT)

        # Sketch8 -> Extrude8 (Join)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(34, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 18.1363838334, perimeter: 23.0976112609
            with BuildLine():
                Line((4.8740457279, 5.1039629319), (-4.8000165647, 5.1039629319))
                Line((4.8740457279, 6.9787062698), (4.8740457279, 5.1039629319))
                Line((-4.8000165647, 6.9787062698), (4.8740457279, 6.9787062698))
                Line((-4.8000165647, 5.1039629319), (-4.8000165647, 6.9787062698))
            make_face()
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.ADD)

        # Sketch9 -> Extrude9 (Join)
        # Sketch on BRepFace
        # Sketch has 12 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(30, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 11.2306945166, perimeter: 21.4161571269
            with BuildLine():
                Line((-8.1227634066, 8.8827456528), (-7.9449124115, 0))
                Line((-7.9449124115, 0), (-6.8708807742, 0))
                Line((-6.8089021342, 9.8340586179), (-6.8708807742, 0))
                CenterArc((-0.4502866205, -0.3307903064), 11.9898350658, 122.0280151915, 7.7574755679)
            make_face()
            # Profile area: 11.9476014015, perimeter: 21.0136543564
            with BuildLine():
                Line((6.4472653235, 9.4763459771), (6.3875411487, 0))
                Line((6.3875411487, 0), (7.8856727908, 0))
                Line((7.6067344916, 8.5484301382), (7.8856727908, 0))
                CenterArc((-0.4502866205, -0.3307903064), 11.9898350658, 47.7793413017, 7.1011840609)
            make_face()
            # Profile area: 6.8711712979, perimeter: 17.3029483982
            with BuildLine():
                Line((-10.0110479911, 6.9044005632), (-9.9934318608, 0))
                Line((-9.9934318608, 0), (-9.1292127181, 0))
                Line((-9.0363969299, 8.037892664), (-9.1292127181, 0))
                CenterArc((-0.4502866205, -0.3307903064), 11.9898350658, 135.7347176599, 7.1483450541)
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)

        # Sketch10 -> Extrude10 (Join)
        # Sketch on BRepFace
        # Sketch has 9 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(30, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 3.694231207, perimeter: 26.0394861106
            with BuildLine():
                Line((-1.7324685534, 0), (-2.0325134321, 0))
                Line((-1.7324685534, 0), (-1.7324685534, 4.3943292663))
                Line((-1.7324685534, 4.3943292663), (1.6320317622, 4.3943292663))
                Line((1.6320317622, 4.3943292663), (1.6320317622, 0))
                Line((1.9330805876, 0), (1.6320317622, 0))
                Line((1.9330805876, 4.6598197693), (1.9330805876, 0))
                Line((-2.0325134321, 4.6598197693), (1.9330805876, 4.6598197693))
                Line((-2.0325134321, 0), (-2.0325134321, 4.6598197693))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)

        # Sketch11 -> Extrude11 (Join)
        # Sketch on BRepFace
        # Sketch has 8 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(30, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 2.0797732816, perimeter: 5.8680596046
            with BuildLine():
                Line((-3.5487836319, 2.1971646331), (-5.2847956308, 2.1971646331))
                Line((-3.5487836319, 3.3951824366), (-3.5487836319, 2.1971646331))
                Line((-5.2847956308, 3.3951824366), (-3.5487836319, 3.3951824366))
                Line((-5.2847956308, 2.1971646331), (-5.2847956308, 3.3951824366))
            make_face()
            # Profile area: 2.0797732816, perimeter: 5.8680596046
            with BuildLine():
                Line((5.0374378758, 2.1971646331), (3.301425877, 2.1971646331))
                Line((5.0374378758, 3.3951824366), (5.0374378758, 2.1971646331))
                Line((3.301425877, 3.3951824366), (5.0374378758, 3.3951824366))
                Line((3.301425877, 2.1971646331), (3.301425877, 3.3951824366))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)
    return part.part


# Description: This is a structural bracket or support assembly with a roughly U-shaped or yoke-like form, featuring two vertical towers connected by horizontal cross-members, reinforced with diagonal bracing and mesh panels, and containing various slots, holes, and mounting flanges throughout its structure.
def model_120292_9c3e9e6c_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrusion1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 8 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 12.0536504592, perimeter: 15.5707963268
            with BuildLine():
                Line((1.75, -1.75), (1.75, 1.75))
                Line((1.75, 1.75), (-1.75, 1.75))
                Line((-1.75, 1.75), (-1.75, -1.75))
                Line((-1.75, -1.75), (1.75, -1.75))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch2 -> Extrusion2 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.3586856742, perimeter: 6.2126924911
            with BuildLine():
                Line((-0.6693721215, -0.3879101652), (0.0012539967, -0.7736483444))
                Line((0.0012539967, -0.7736483444), (0.6706261182, -0.3857381792))
                Line((0.6706261182, -0.3857381792), (0.6693721215, 0.3879101652))
                Line((0.6693721215, 0.3879101652), (-0.0012539967, 0.7736483444))
                Line((-0.0012539967, 0.7736483444), (-0.6706261182, 0.3857381792))
                Line((-0.6706261182, 0.3857381792), (-0.6693721215, -0.3879101652))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.25
        extrude(amount=-0.25, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrusion3 (Cut)
        # Sketch on BRepFace
        # Sketch has 15 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.9506566854, perimeter: 4.5361771278
            with BuildLine():
                CenterArc((2.1793935931, 0.0026351247), 1.0882917154, 113.2383755814, 133.5232488372)
                Line((1.75, -0.9973648753), (1.75, 1.0026351247))
            make_face()
            # Profile area: 0.9376232772, perimeter: 4.5242297696
            with BuildLine():
                CenterArc((-0.0035477287, -2.1925741614), 1.0935592752, 23.8729433331, 132.2541133338)
                Line((-1.0035477287, -1.75), (0.9964522713, -1.75))
            make_face()
            # Profile area: 0.9364875299, perimeter: 4.5145562442
            with BuildLine():
                CenterArc((-2.1864890505, 0.0026351247), 1.0882917154, -66.3544600121, 132.7089200243)
                Line((-1.75, 0.9995584751), (-1.75, -0.9942882257))
            make_face()
            # Profile area: 0.9376232772, perimeter: 4.5242297696
            with BuildLine():
                CenterArc((-0.0035477287, 2.1925741614), 1.0935592752, -156.1270566669, 132.2541133338)
                Line((0.9964522713, 1.75), (-1.0035477287, 1.75))
            make_face()
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrusion5 (Join)
        # Sketch on BRepFace
        # Sketch has 8 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.9376232772, perimeter: 4.5242297696
            with BuildLine():
                Line((0.9964522713, -1.75), (-1.0035477287, -1.75))
                CenterArc((-0.0035477287, -2.1925741614), 1.0935592752, 23.8729433331, 132.2541133338)
            make_face()
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.ADD)

        # Sketch4 -> Extrusion4 (Join)
        # Sketch on BRepFace
        # Sketch has 8 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 6.9325740153, perimeter: 20.753395674
            with BuildLine():
                Line((-1.0035477287, 1.75), (-1.75, 1.75))
                Line((-1.75, 0.9995584751), (-1.75, 1.75))
                CenterArc((-2.1864890505, 0.0026351247), 1.0882917154, -66.3544600121, 132.7089200243)
                Line((-1.75, -0.9942882257), (-1.75, -1.75))
                Line((-1.0035477287, -1.75), (-1.75, -1.75))
                CenterArc((-0.0035477287, -2.1925741614), 1.0935592752, 23.8729433331, 132.2541133338)
                Line((1.75, -1.75), (0.9964522713, -1.75))
                Line((1.75, -0.9973648753), (1.75, -1.75))
                CenterArc((2.1793935931, 0.0026351247), 1.0882917154, 113.2383755814, 133.5232488372)
                Line((1.75, 1.0026351247), (1.75, 1.75))
                Line((1.75, 1.75), (0.9964522713, 1.75))
                CenterArc((-0.0035477287, 2.1925741614), 1.0935592752, -156.1270566669, 132.2541133338)
            make_face()
            with BuildLine():
                Line((0.6693721215, 0.3879101652), (0.6706261182, -0.3857381792))
                Line((0.6706261182, -0.3857381792), (0.0012539967, -0.7736483444))
                Line((0.0012539967, -0.7736483444), (-0.6693721215, -0.3879101652))
                Line((-0.6693721215, -0.3879101652), (-0.6706261182, 0.3857381792))
                Line((-0.6706261182, 0.3857381792), (-0.0012539967, 0.7736483444))
                Line((-0.0012539967, 0.7736483444), (0.6693721215, 0.3879101652))
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 1.555035215, perimeter: 4.6418961643
            with BuildLine():
                Line((-0.0012539967, 0.7736483444), (0.6693721215, 0.3879101652))
                Line((-0.6706261182, 0.3857381792), (-0.0012539967, 0.7736483444))
                Line((-0.6693721215, -0.3879101652), (-0.6706261182, 0.3857381792))
                Line((0.0012539967, -0.7736483444), (-0.6693721215, -0.3879101652))
                Line((0.6706261182, -0.3857381792), (0.0012539967, -0.7736483444))
                Line((0.6693721215, 0.3879101652), (0.6706261182, -0.3857381792))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)

        # Sketch4 -> Extrusion6 (Join)
        # Sketch on BRepFace
        # Sketch has 8 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.9376232772, perimeter: 4.5242297696
            with BuildLine():
                Line((0.9964522713, -1.75), (-1.0035477287, -1.75))
                CenterArc((-0.0035477287, -2.1925741614), 1.0935592752, 23.8729433331, 132.2541133338)
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)

        # Sketch5 -> Extrusion7 (Join)
        # Sketch on BRepFace
        # Sketch has 11 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.25, perimeter: 2
            with BuildLine():
                Line((1.4991855087, -1.6994514466), (1.4991855087, -1.1994514466))
                Line((1.4991855087, -1.1994514466), (0.9991855087, -1.1994514466))
                Line((0.9991855087, -1.1994514466), (0.9991855087, -1.6994514466))
                Line((0.9991855087, -1.6994514466), (1.4991855087, -1.6994514466))
            make_face()
            # Profile area: 0.25, perimeter: 2
            with BuildLine():
                Line((-1.4991855087, -1.6994514466), (-1.4991855087, -1.1994514466))
                Line((-0.9991855087, -1.6994514466), (-1.4991855087, -1.6994514466))
                Line((-0.9991855087, -1.1994514466), (-0.9991855087, -1.6994514466))
                Line((-1.4991855087, -1.1994514466), (-0.9991855087, -1.1994514466))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)

        # Sketch7 -> Extrusion10 (Join)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(1.4991855087, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.1028148676, perimeter: 2.226552645
            with BuildLine():
                Line((1.1994514466, 2.5), (1.1994514466, 1.5))
                Line((0.9938217115, 1.5), (1.1994514466, 2.5))
                Line((0.9938217115, 1.5), (1.1994514466, 1.5))
            make_face()
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.ADD)

        # Sketch8 -> Extrusion11 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(-0.9991855087, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.1025816104, perimeter: 2.2259922699
            with BuildLine():
                Line((1.1994514466, 2.5), (0.9942882257, 1.5))
                Line((0.9942882257, 1.5), (1.1994514466, 1.5))
                Line((1.1994514466, 2.5), (1.1994514466, 1.5))
            make_face()
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.ADD)

        # Sketch8 -> Extrusion8 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(-0.9991855087, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.1639052505, perimeter: 2.0139916069
            with BuildLine():
                Line((1.5394069408, 2.2994510263), (1.6994514466, 2.2994510263))
                Line((1.4494514466, 1.5), (1.5394069408, 2.2994510263))
                Line((1.4494514466, 1.5), (1.6994514466, 1.5))
                Line((1.6994514466, 1.5), (1.6994514466, 2.2994510263))
            make_face()
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.SUBTRACT)

        # Sketch7 -> Extrusion9 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(1.4991855087, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.1639052505, perimeter: 2.0139916069
            with BuildLine():
                Line((1.6994514466, 1.5), (1.6994514466, 2.2994510263))
                Line((1.5394069408, 2.2994510263), (1.6994514466, 2.2994510263))
                Line((1.4494514466, 1.5), (1.5394069408, 2.2994510263))
                Line((1.4494514466, 1.5), (1.6994514466, 1.5))
            make_face()
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a complex bracket or mounting component with an irregular, angular geometric shape featuring multiple triangulated faces, internal cavities, and protruding flanges designed for structural support or assembly integration.
def model_128645_d5cdd476_0002():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 43 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 133780.3776, perimeter: 1463.04
            with BuildLine():
                Line((1036.32, 1036.32), (1036.32, 670.56))
                Line((1036.32, 670.56), (1402.08, 670.56))
                Line((1402.08, 1036.32), (1402.08, 670.56))
                Line((1402.08, 1036.32), (1036.32, 1036.32))
            make_face()
            # Profile area: 133780.3776, perimeter: 1463.04
            with BuildLine():
                Line((670.56, 670.56), (1036.32, 670.56))
                Line((1036.32, 1036.32), (1036.32, 670.56))
                Line((1036.32, 1036.32), (670.56, 1036.32))
                Line((670.56, 1036.32), (670.56, 670.56))
            make_face()
            # Profile area: 111483.648, perimeter: 1341.12
            with BuildLine():
                Line((304.8, 1036.32), (304.8, 670.56))
                Line((0, 1036.32), (304.8, 1036.32))
                Line((0, 670.56), (0, 1036.32))
                Line((304.8, 670.56), (0, 670.56))
            make_face()
            # Profile area: 133780.3776, perimeter: 1463.04
            with BuildLine():
                Line((304.8, 670.56), (670.56, 670.56))
                Line((670.56, 1036.32), (670.56, 670.56))
                Line((670.56, 1036.32), (304.8, 1036.32))
                Line((304.8, 1036.32), (304.8, 670.56))
            make_face()
            # Profile area: 133780.3776, perimeter: 1463.04
            with BuildLine():
                Line((1402.08, 1036.32), (1402.08, 670.56))
                Line((1402.08, 670.56), (1767.84, 670.56))
                Line((1767.84, 670.56), (1767.84, 1036.32))
                Line((1767.84, 1036.32), (1402.08, 1036.32))
            make_face()
            # Profile area: 133780.3776, perimeter: 1463.04
            with BuildLine():
                Line((1097.28, 0), (1097.28, 365.76))
                Line((1463.04, 0), (1097.28, 0))
                Line((1463.04, 0), (1463.04, 365.76))
                Line((1097.28, 365.76), (1463.04, 365.76))
            make_face()
            # Profile area: 133780.3776, perimeter: 1463.04
            with BuildLine():
                Line((365.76, 365.76), (0, 365.76))
                Line((0, 365.76), (0, 0))
                Line((0, 0), (365.76, 0))
                Line((365.76, 0), (365.76, 365.76))
            make_face()
            # Profile area: 133780.3776, perimeter: 1463.04
            with BuildLine():
                Line((365.76, 0), (365.76, 365.76))
                Line((365.76, 0), (731.52, 0))
                Line((731.52, 0), (731.52, 365.76))
                Line((365.76, 365.76), (731.52, 365.76))
            make_face()
            # Profile area: 111483.648, perimeter: 1341.12
            with BuildLine():
                Line((1463.04, 0), (1463.04, 365.76))
                Line((1767.84, 0), (1463.04, 0))
                Line((1767.84, 365.76), (1767.84, 0))
                Line((1463.04, 365.76), (1767.84, 365.76))
            make_face()
            # Profile area: 133780.3776, perimeter: 1463.04
            with BuildLine():
                Line((1097.28, 0), (731.52, 0))
                Line((1097.28, 0), (1097.28, 365.76))
                Line((731.52, 365.76), (1097.28, 365.76))
                Line((731.52, 0), (731.52, 365.76))
            make_face()
        # OneSide extrude, distance=243.84
        extrude(amount=243.84)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(1767.84, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 238994.9085397526, perimeter: 2423.7957326303
            with BuildLine():
                Line((-243.84, 0), (-243.84, 365.76))
                Line((-243.84, 365.76), (-243.84, 1036.32))
                Line((-243.84, 1036.32), (-705.0776650837, 508.3835474717))
                Line((-243.84, 0), (-705.0776650837, 508.3835474717))
            make_face()
        # OneSide extrude, distance=-1767.84
        extrude(amount=-1767.84, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 111483.648, perimeter: 1402.08
            with BuildLine():
                Line((1767.84, 0), (1767.84, 243.84))
                Line((1767.84, 243.84), (1310.64, 243.84))
                Line((1310.64, 243.84), (1310.64, 0))
                Line((1310.64, 0), (1767.84, 0))
            make_face()
        # OneSide extrude, distance=304.8
        extrude(amount=304.8, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 10 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(1767.84, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 64577.677296, perimeter: 1021.05968
            with BuildLine():
                Line((0, -292.1), (-231.12984, -292.1))
                Line((0, -12.7), (0, -292.1))
                Line((-231.12984, -12.7), (0, -12.7))
                Line((-231.12984, -292.1), (-231.12984, -12.7))
            make_face()
        # OneSide extrude, distance=-426.72
        extrude(amount=-426.72, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude5 (NewBody)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 443.8094489196, perimeter: 309.567997637
            with BuildLine():
                Line((-1833.6853083868, 503.201461588), (-1836.3237411683, 501.9374440335))
                Line((-1836.3237411683, 501.9374440335), (-1771.0839969593, 365.76))
                Line((-1771.0839969593, 365.76), (-1767.84, 365.76))
                Line((-1767.84, 365.76), (-1833.6853083868, 503.201461588))
            make_face()
        # OneSide extrude, distance=-243.84
        extrude(amount=-243.84)

        # Sketch6 -> Extrude6 (NewBody)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 387.1954339637, perimeter: 309.9595008702
            with BuildLine():
                Line((-1767.84, 670.56), (-1834.6315392827, 533.5758758095))
                Line((-1770.0887550393, 671.7435669799), (-1767.84, 670.56))
                Line((-1836.9146080192, 534.6890681308), (-1770.0887550393, 671.7435669799))
                Line((-1834.6315392827, 533.5758758095), (-1836.9146080192, 534.6890681308))
            make_face()
        # OneSide extrude, distance=-243.84
        extrude(amount=-243.84)

        # Sketch9 -> Extrude7 (Cut)
        # Sketch on Profile plane
        # Sketch has 30 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(883.92, 365.76, 121.92), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 72932.411139735, perimeter: 1085.8789110968
            with BuildLine():
                Line((-582.2805293454, 121.92), (-881.3799867249, 121.92))
                Line((-881.3799867249, 121.92), (-881.3799867249, -121.9199981689))
                Line((-881.3799867249, -121.9199981689), (-582.2805293454, -121.9199981689))
                Line((-582.2805293454, -121.9199981689), (-582.2805293454, 121.92))
            make_face()
            # Profile area: 87930.3947866444, perimeter: 1208.8939135392
            with BuildLine():
                Line((154.9400132751, -121.9199981689), (154.9400132751, 121.92))
                Line((515.6200132751, -121.9199981689), (154.9400132751, -121.9199981689))
                Line((515.6200132751, -121.9199981689), (515.4738866916, 121.92))
                Line((154.9400132751, 121.92), (515.4738866916, 121.92))
            make_face()
            # Profile area: 87805.6240544138, perimeter: 1207.8704956324
            with BuildLine():
                Line((-216.4537537053, 121.92), (-576.5180121044, 121.92))
                Line((-576.5799867249, -121.9199981689), (-576.5180121044, 121.92))
                Line((-576.5799867249, -121.9199981689), (-216.4537537053, -121.9199981689))
                Line((-216.4537537053, -121.9199981689), (-216.4537537053, 121.92))
            make_face()
            # Profile area: 87970.3510253529, perimeter: 1209.2216624341
            with BuildLine():
                Line((-210.8199867249, -121.9199981689), (-211.0015851988, 121.92))
                Line((149.8600132751, -121.9199981689), (-210.8199867249, -121.9199981689))
                Line((149.8600132751, 121.92), (149.8600132751, -121.9199981689))
                Line((-211.0015851988, 121.92), (149.8600132751, 121.92))
            make_face()
            # Profile area: 87589.8130172967, perimeter: 1206.1003959879
            with BuildLine():
                Line((520.7000132751, 121.9199981689), (879.8750097347, 121.9199981689))
                Line((520.7000132751, -121.9199981689), (520.7000132751, 121.9199981689))
                Line((879.9454099649, -121.9199981689), (520.7000132751, -121.9199981689))
                Line((879.9454099649, -121.9199981689), (879.8750097347, 121.9199981689))
            make_face()
        # OneSide extrude, distance=-358.14
        extrude(amount=-358.14, mode=Mode.SUBTRACT)

        # Sketch10 -> Extrude8 (Cut)
        # Sketch on BRepFace
        # Sketch has 67 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 670.56, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 88042.4478166795, perimeter: 1210.4035951241
            with BuildLine():
                Line((669.3113975696, 243.84), (669.3113975696, 0.6096000075))
                Line((307.34, 243.84), (669.3113975696, 243.84))
                Line((307.34, 0.6096000075), (307.34, 243.84))
                Line((307.34, 0.6096000075), (669.3113975696, 0.6096000075))
            make_face()
            # Profile area: 87728.3406692826, perimeter: 1207.8207999849
            with BuildLine():
                Line((673.1, 243.84), (673.1, 0.6096000075))
                Line((673.1, 0.6096000075), (1033.78, 0.6096000075))
                Line((1033.78, 0.6096000075), (1033.78, 243.84))
                Line((1033.78, 243.84), (673.1, 243.84))
            make_face()
            # Profile area: 87730.8118901466, perimeter: 1207.8411199849
            with BuildLine():
                Line((1404.62, 243.84), (1404.62, 0.6096000075))
                Line((1404.62, 0.6096000075), (1765.31016, 0.6096000075))
                Line((1765.31016, 0.6096000075), (1765.31016, 243.84))
                Line((1765.31016, 243.84), (1404.62, 243.84))
            make_face()
            # Profile area: 87728.3406692826, perimeter: 1207.8207999849
            with BuildLine():
                Line((1038.86, 243.84), (1038.86, 0.6096000075))
                Line((1038.86, 0.6096000075), (1399.54, 0.6096000075))
                Line((1399.54, 0.6096000075), (1399.54, 243.84))
                Line((1399.54, 243.84), (1038.86, 243.84))
            make_face()
            # Profile area: 72901.0154857419, perimeter: 1085.9007999849
            with BuildLine():
                Line((2.54, 243.84), (2.54, 0.6096000075))
                Line((2.54, 0.6096000075), (302.26, 0.6096000075))
                Line((302.26, 0.6096000075), (302.26, 243.84))
                Line((302.26, 243.84), (2.54, 243.84))
            make_face()
        # OneSide extrude, distance=-358.14
        extrude(amount=-358.14, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical dowel pin or fastener with a slightly rounded/beveled end, featuring a simple tubular shape with minimal features—essentially a straight, smooth cylindrical rod.
def model_130022_505982e4_0000():
    """Model: Untitled"""
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

        # Sketch7 -> Extrude5 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0028114193, perimeter: 0.2124567733
            with BuildLine():
                Line((3.1000000462, 0.2500000045), (3.1500000462, 0.2500000045))
                Line((3.1000000462, 0.1937716178), (3.1000000462, 0.2500000045))
                Line((3.1500000462, 0.1937716178), (3.1000000462, 0.1937716178))
                Line((3.1500000462, 0.2500000045), (3.1500000462, 0.1937716178))
            make_face()
        # OneSide extrude, distance=0.01
        extrude(amount=0.01)

        # Sketch8 -> Extrude6 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.01, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0002107283, perimeter: 0.069238495
            with BuildLine():
                Line((-3.1000000462, -0.2500000045), (-3.0850091646, -0.2350000056))
                Line((-3.0850091646, -0.2350000056), (-3.1000000462, -0.2218858111))
                Line((-3.1000000462, -0.2500000045), (-3.1000000462, -0.2218858111))
            make_face()
        # OneSide extrude, distance=-0.01
        extrude(amount=-0.01, mode=Mode.ADD)

        # Sketch9 -> Extrude7 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.01, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0003710438, perimeter: 0.0809356901
            with BuildLine():
                Line((-3.1150091639, -0.215000006), (-3.1150797722, -0.1937716178))
                Line((-3.1000000462, -0.2218858111), (-3.1150091639, -0.215000006))
                Line((-3.1000000462, -0.2218858111), (-3.1000000462, -0.1937716178))
                Line((-3.1000000462, -0.1937716178), (-3.1150797722, -0.1937716178))
            make_face()
        # OneSide extrude, distance=-0.01
        extrude(amount=-0.01, mode=Mode.SUBTRACT)

        # Sketch10 -> Extrude8 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.01, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0002816546, perimeter: 0.1224750069
            with BuildLine():
                Line((-3.1500000462, -0.1937716178), (-3.1500000462, -0.2500000045))
                Line((-3.155009163, -0.1937716178), (-3.1500000462, -0.1937716178))
                Line((-3.155009163, -0.2500000045), (-3.155009163, -0.1937716178))
                Line((-3.1500000462, -0.2500000045), (-3.155009163, -0.2500000045))
            make_face()
        # OneSide extrude, distance=-0.01
        extrude(amount=-0.01, mode=Mode.ADD)
    return part.part


# Description: This is a boat or watercraft hull assembly featuring an elongated streamlined base with multiple cubic superstructure modules stacked along its length, connected by framework and support structures, designed for modular cargo or passenger transport.
def model_130832_8f82565e_0000():
    """Model: Raspberry Pi Master"""
    with BuildPart() as part:
        # PCB -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 31 constraints, 12 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 47.2851603944, perimeter: 31.1407075111
            with BuildLine():
                CenterArc((0.3, -0.3), 0.3, 90, 90)
                Line((0, -8.2), (0, -0.3))
                CenterArc((0.3, -8.2), 0.3, -180, 90)
                Line((5.3, -8.5), (0.3, -8.5))
                CenterArc((5.3, -8.2), 0.3, -90, 90)
                Line((5.6, -0.3), (5.6, -8.2))
                CenterArc((5.3, -0.3), 0.3, 0, 90)
                Line((0.3, 0), (5.3, 0))
            make_face()
            with BuildLine():
                CenterArc((5.25, -2.35), 0.1375, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0.35, -2.35), 0.1375, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0.35, -8.15), 0.1375, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((5.25, -8.15), 0.1375, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.15
        extrude(amount=0.15)

        # Front IO -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 22 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.15, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.0446963378, perimeter: 7.0033933113
            with BuildLine():
                CenterArc((-5.3, 0.3), 0.3, -102.5133253629, 12.5133253629)
                Line((-5.3, 0), (-3.775, 0))
                Line((-3.775, 0), (-3.775, 1.915))
                Line((-3.775, 1.915), (-5.365, 1.915))
                Line((-5.365, 1.915), (-5.365, 0.0071263071))
            make_face()
            # Profile area: 0.3340536622, perimeter: 3.6076459255
            with BuildLine():
                Line((-5.365, 0.0071263071), (-5.365, -0.21))
                Line((-5.365, -0.21), (-3.775, -0.21))
                Line((-3.775, -0.21), (-3.775, 0))
                Line((-5.3, 0), (-3.775, 0))
                CenterArc((-5.3, 0.3), 0.3, -102.5133253629, 12.5133253629)
            make_face()
        # OneSide extrude, distance=1.35
        extrude(amount=1.35, mode=Mode.ADD)

        # Front IO -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 22 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.15, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.9518070978, perimeter: 5.5952280994
            with BuildLine():
                Line((-1.555, 0), (-1.555, 1.49))
                Line((-1.555, 0), (-0.3, 0))
                CenterArc((-0.3, 0.3), 0.3, -90, 10.5639775891)
                Line((-0.245, 1.49), (-0.245, 0.0050847579))
                Line((-1.555, 1.49), (-0.245, 1.49))
            make_face()
            # Profile area: 0.2751929022, perimeter: 3.0453976152
            with BuildLine():
                Line((-1.555, -0.21), (-1.555, 0))
                Line((-0.245, -0.21), (-1.555, -0.21))
                Line((-0.245, 0.0050847579), (-0.245, -0.21))
                CenterArc((-0.3, 0.3), 0.3, -90, 10.5639775891)
                Line((-1.555, 0), (-0.3, 0))
            make_face()
            # Profile area: 1.9519, perimeter: 5.6
            with BuildLine():
                Line((-3.355, 0), (-2.045, 0))
                Line((-2.045, 1.49), (-2.045, 0))
                Line((-3.355, 1.49), (-2.045, 1.49))
                Line((-3.355, 0), (-3.355, 1.49))
            make_face()
            # Profile area: 0.2751, perimeter: 3.04
            with BuildLine():
                Line((-3.355, -0.21), (-3.355, 0))
                Line((-2.045, -0.21), (-3.355, -0.21))
                Line((-2.045, 0), (-2.045, -0.21))
                Line((-3.355, 0), (-2.045, 0))
            make_face()
        # OneSide extrude, distance=1.6
        extrude(amount=1.6, mode=Mode.ADD)

        # Right IO -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 22 constraints, 14 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.15, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.15, perimeter: 1.7
            with BuildLine():
                Line((-5.6, 3.45), (-5.6, 2.85))
                Line((-5.85, 3.45), (-5.6, 3.45))
                Line((-5.85, 2.85), (-5.85, 3.45))
                Line((-5.6, 2.85), (-5.85, 2.85))
            make_face()
            # Profile area: 0.735, perimeter: 3.65
            with BuildLine():
                Line((-4.375, 2.85), (-5.6, 2.85))
                Line((-4.375, 3.45), (-4.375, 2.85))
                Line((-5.6, 3.45), (-4.375, 3.45))
                Line((-5.6, 3.45), (-5.6, 2.85))
            make_face()
        # OneSide extrude, distance=0.6
        extrude(amount=0.6, mode=Mode.ADD)

        # Right IO -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 22 constraints, 14 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.15, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.886, perimeter: 5.23
            with BuildLine():
                Line((-3.385, 3.8), (-5.6, 3.8))
                Line((-3.385, 4.2), (-3.385, 3.8))
                Line((-5.6, 4.2), (-3.385, 4.2))
                Line((-5.6, 3.8), (-5.6, 4.2))
            make_face()
        # OneSide extrude, distance=0.55
        extrude(amount=0.55, mode=Mode.ADD)

        # Right IO -> Extrude6 (Join)
        # Sketch on BRepFace
        # Sketch has 22 constraints, 14 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.15, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.7475, perimeter: 5.33
            with BuildLine():
                Line((-4.435, 4.55), (-5.6, 4.55))
                Line((-4.435, 6.05), (-4.435, 4.55))
                Line((-5.6, 6.05), (-4.435, 6.05))
                Line((-5.6, 6.05), (-5.6, 4.55))
            make_face()
        # OneSide extrude, distance=0.65
        extrude(amount=0.65, mode=Mode.ADD)

        # Right IO -> Extrude7 (Join)
        # Sketch on BRepFace
        # Sketch has 22 constraints, 14 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.15, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.4125, perimeter: 2.6
            with BuildLine():
                Line((-5.6, 7.815), (-5.6, 7.065))
                Line((-5.6, 7.065), (-5.05, 7.065))
                Line((-5.05, 7.065), (-5.05, 7.815))
                Line((-5.05, 7.815), (-5.6, 7.815))
            make_face()
        # OneSide extrude, distance=0.245
        extrude(amount=0.245, mode=Mode.ADD)

        # SD Card -> Extrude8 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.35332, perimeter: 3.404
            with BuildLine():
                Line((3.45, 8.5), (1.99, 8.5))
                Line((3.45, 8.5), (3.45, 8.742))
                Line((3.45, 8.742), (1.99, 8.742))
                Line((1.99, 8.742), (1.99, 8.5))
            make_face()
            # Profile area: 2.1316, perimeter: 5.84
            with BuildLine():
                Line((1.99, 8.5), (1.99, 7.04))
                Line((1.99, 7.04), (3.45, 7.04))
                Line((3.45, 7.04), (3.45, 8.5))
                Line((3.45, 8.5), (1.99, 8.5))
            make_face()
        # OneSide extrude, distance=0.135
        extrude(amount=0.135, mode=Mode.ADD)

        # Back IO -> Extrude9 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.15, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.555, perimeter: 4.94
            with BuildLine():
                Line((-3.91, 8.235), (-1.69, 8.235))
                Line((-3.91, 7.985), (-3.91, 8.235))
                Line((-1.69, 7.985), (-3.91, 7.985))
                Line((-1.69, 8.235), (-1.69, 7.985))
            make_face()
        # OneSide extrude, distance=0.525
        extrude(amount=0.525, mode=Mode.ADD)

        # GPIO -> Extrude10 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.15, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.048, perimeter: 11.36
            with BuildLine():
                Line((-0.7, 7.79), (-0.1, 7.79))
                Line((-0.7, 2.71), (-0.7, 7.79))
                Line((-0.1, 2.71), (-0.7, 2.71))
                Line((-0.1, 7.79), (-0.1, 2.71))
            make_face()
        # OneSide extrude, distance=0.875
        extrude(amount=0.875, mode=Mode.ADD)
    return part.part


# Description: This is a sheet metal bracket or mounting assembly featuring a base platform with multiple vertical flanges and slots, designed for structural support or component attachment.
def model_130932_a060d2a3_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude2 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 21 constraints, 12 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.3938409852, perimeter: 6.1549336143
            with BuildLine():
                Line((-3.6737297659, -0.8770085396), (-5.1187297659, -0.8770085396))
                CenterArc((-3.5687297659, -0.8770085396), 0.105, 90, 90)
                Line((-3.5687297659, 0.6729914604), (-3.5687297659, -0.7720085396))
                Line((-5.1187297659, 0.6729914604), (-3.5687297659, 0.6729914604))
                Line((-5.1187297659, 0.6729914604), (-5.1187297659, -0.8770085396))
            make_face()
            # Profile area: 2.3938409852, perimeter: 6.1549336143
            with BuildLine():
                Line((-6.6687297659, 0.6729914604), (-6.6687297659, 2.1179914604))
                Line((-5.1187297659, 0.6729914604), (-6.6687297659, 0.6729914604))
                Line((-5.1187297659, 0.6729914604), (-5.1187297659, 2.2229914604))
                Line((-6.5637297659, 2.2229914604), (-5.1187297659, 2.2229914604))
                CenterArc((-6.6687297659, 2.2229914604), 0.105, -90, 90)
            make_face()
            # Profile area: 1.9815229557, perimeter: 8.6848008429
            with BuildLine():
                Line((-3.0187297659, -1.4270085396), (-5.1187297659, -1.4270085396))
                Line((-3.0187297659, 0.6729914604), (-3.0187297659, -1.4270085396))
                Line((-3.5687297659, 0.6729914604), (-3.0187297659, 0.6729914604))
                Line((-3.5687297659, 0.6729914604), (-3.5687297659, -0.7720085396))
                CenterArc((-3.5687297659, -0.8770085396), 0.105, 180, 270)
                Line((-3.6737297659, -0.8770085396), (-5.1187297659, -0.8770085396))
                Line((-5.1187297659, -0.8770085396), (-5.1187297659, -1.4270085396))
            make_face()
            # Profile area: 1.9815229557, perimeter: 8.6848008429
            with BuildLine():
                Line((-5.1187297659, 2.2229914604), (-3.6737297659, 2.2229914604))
                CenterArc((-3.5687297659, 2.2229914604), 0.105, -90, 270)
                Line((-3.5687297659, 2.1179914604), (-3.5687297659, 0.6729914604))
                Line((-3.5687297659, 0.6729914604), (-3.0187297659, 0.6729914604))
                Line((-3.0187297659, 2.7729914604), (-3.0187297659, 0.6729914604))
                Line((-5.1187297659, 2.7729914604), (-3.0187297659, 2.7729914604))
                Line((-5.1187297659, 2.3729914604), (-5.1187297659, 2.7729914604))
                Line((-5.1187297659, 2.2229914604), (-5.1187297659, 2.3729914604))
            make_face()
            # Profile area: 2.3938409852, perimeter: 6.1549336143
            with BuildLine():
                Line((-5.1187297659, 0.6729914604), (-5.1187297659, -0.8770085396))
                Line((-5.1187297659, 0.6729914604), (-6.6687297659, 0.6729914604))
                Line((-6.6687297659, -0.7720085396), (-6.6687297659, 0.6729914604))
                CenterArc((-6.6687297659, -0.8770085396), 0.105, 0, 90)
                Line((-5.1187297659, -0.8770085396), (-6.5637297659, -0.8770085396))
            make_face()
            # Profile area: 3.9630459115, perimeter: 16.2696016859
            with BuildLine():
                CenterArc((-6.6687297659, 2.2229914604), 0.105, 0, 270)
                Line((-6.5637297659, 2.2229914604), (-5.1187297659, 2.2229914604))
                Line((-5.1187297659, 2.2229914604), (-5.1187297659, 2.3729914604))
                Line((-5.1187297659, 2.3729914604), (-5.1187297659, 2.7729914604))
                Line((-7.2187297659, 2.7729914604), (-5.1187297659, 2.7729914604))
                Line((-7.2187297659, -1.4270085396), (-7.2187297659, 2.7729914604))
                Line((-5.1187297659, -1.4270085396), (-7.2187297659, -1.4270085396))
                Line((-5.1187297659, -0.8770085396), (-5.1187297659, -1.4270085396))
                Line((-5.1187297659, -0.8770085396), (-6.5637297659, -0.8770085396))
                CenterArc((-6.6687297659, -0.8770085396), 0.105, 90, 270)
                Line((-6.6687297659, -0.7720085396), (-6.6687297659, 0.6729914604))
                Line((-6.6687297659, 0.6729914604), (-6.6687297659, 2.1179914604))
            make_face()
            # Profile area: 2.3938409852, perimeter: 6.1549336143
            with BuildLine():
                Line((-5.1187297659, 0.6729914604), (-5.1187297659, 2.2229914604))
                Line((-5.1187297659, 0.6729914604), (-3.5687297659, 0.6729914604))
                Line((-3.5687297659, 2.1179914604), (-3.5687297659, 0.6729914604))
                CenterArc((-3.5687297659, 2.2229914604), 0.105, 180, 90)
                Line((-5.1187297659, 2.2229914604), (-3.6737297659, 2.2229914604))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 14 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.84, perimeter: 8.8
            with BuildLine():
                Line((4.1187297659, -0.6729914604), (4.1187297659, -2.7729914604))
                Line((4.1187297659, -0.6729914604), (4.1187297659, 1.4270085396))
                Line((4.1187297659, 1.4270085396), (3.9187297659, 1.4270085396))
                Line((3.9187297659, 1.4270085396), (3.9187297659, 0.4270085396))
                Line((3.9187297659, 0.4270085396), (3.9187297659, -2.7729914604))
                Line((3.9187297659, -2.7729914604), (4.1187297659, -2.7729914604))
            make_face()
            # Profile area: 0.84, perimeter: 8.8
            with BuildLine():
                Line((6.3187297659, -2.7729914604), (6.3187297659, 0.4270085396))
                Line((6.3187297659, 0.4270085396), (6.3187297659, 1.4270085396))
                Line((6.3187297659, 1.4270085396), (6.1187297659, 1.4270085396))
                Line((6.1187297659, -0.6729914604), (6.1187297659, 1.4270085396))
                Line((6.1187297659, -0.6729914604), (6.1187297659, -2.7729914604))
                Line((6.1187297659, -2.7729914604), (6.3187297659, -2.7729914604))
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.8376276474, perimeter: 8.7762764735
            with BuildLine():
                Line((6.1187297659, 1.4151467764), (6.1187297659, -2.7729914604))
                Line((6.3187297659, -2.7729914604), (6.1187297659, -2.7729914604))
                Line((6.3187297659, 1.4151467764), (6.3187297659, -2.7729914604))
                Line((6.1187297659, 1.4151467764), (6.3187297659, 1.4151467764))
            make_face()
            # Profile area: 9.2071337007, perimeter: 12.7730433328
            with BuildLine():
                Line((3.9203463363, 1.4151467764), (6.1187297659, 1.4151467764))
                Line((3.9203463363, -2.7729914604), (3.9203463363, 1.4151467764))
                Line((6.1187297659, -2.7729914604), (3.9203463363, -2.7729914604))
                Line((6.1187297659, 1.4151467764), (6.1187297659, -2.7729914604))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)

        # Sketch5 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2.2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.4748269748, perimeter: 9.1967668593
            with BuildLine():
                Line((5.8187297659, -2.6756632161), (5.8187297659, 0.4270085396))
                Line((5.8187297659, 0.4270085396), (4.4203463363, 0.4270085396))
                Line((4.4203463363, -2.7729914604), (4.4203463363, 0.4270085396))
                Line((5.8187297659, -2.7729914604), (4.4203463363, -2.7729914604))
                Line((5.8187297659, -2.7729914604), (5.8187297659, -2.6756632161))
            make_face()
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.SUBTRACT)

        # Sketch6 -> Extrude6 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -2.7729914604), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.0420405243, perimeter: 0.8892067994
            with BuildLine():
                Line((5.8187297659, 1.2), (5.9983245231, 1))
                Line((6.1187297659, 1), (5.9983245231, 1))
                Line((6.1187297659, 1.2), (6.1187297659, 1))
                Line((5.8187297659, 1.2), (6.1187297659, 1.2))
            make_face()
            # Profile area: 0.0379699826, perimeter: 0.879645059
            with BuildLine():
                Line((4.1187297659, 1.2), (4.4203463363, 1.2))
                Line((4.1187297659, 1), (4.1187297659, 1.2))
                Line((4.1968130215, 1), (4.1187297659, 1))
                Line((4.4203463363, 1.2), (4.1968130215, 1))
            make_face()
        # OneSide extrude, distance=-4.2
        extrude(amount=-4.2, mode=Mode.ADD)

        # Sketch7 -> Extrude7 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2.2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.5091264597, perimeter: 3.0263427557
            with BuildLine():
                Line((4.4203463363, 0.4270085396), (4.9253461651, 0.4270085396))
                Line((4.4203463363, -0.5811630094), (4.4203463363, 0.4270085396))
                Line((4.4203463363, -0.5811630094), (4.9253461651, -0.5811630094))
                Line((4.9253461651, 0.4270085396), (4.9253461651, -0.5811630094))
            make_face()
            # Profile area: 0.9006839287, perimeter: 3.8031102998
            with BuildLine():
                Line((4.9253461651, 0.4270085396), (4.9253461651, -0.5811630094))
                Line((4.9253461651, -0.5811630094), (5.8187297659, -0.5811630094))
                Line((5.8187297659, 0.4270085396), (5.8187297659, -0.5811630094))
                Line((4.9253461651, 0.4270085396), (5.8187297659, 0.4270085396))
            make_face()
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.ADD)

        # Sketch9 -> Extrude8 (Join)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2.2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.259512825, perimeter: 5.0131733119
            with BuildLine():
                Line((6.3187297659, 1.3069435501), (6.3187297659, 1.4151467764))
                Line((6.3187297659, 1.4151467764), (3.9203463363, 1.4151467764))
                Line((3.9203463363, 1.4151467764), (3.9203463363, 1.3069435501))
                Line((3.9203463363, 1.3069435501), (6.3187297659, 1.3069435501))
            make_face()
        # OneSide extrude, distance=3
        extrude(amount=3, mode=Mode.ADD)

        # Sketch10 -> Extrude9 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -0.5811630094), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.1399359299, perimeter: 2.9969064303
            with BuildLine():
                Line((5.8187297659, 2.0999302145), (4.4203463363, 2.0999302145))
                Line((5.8187297659, 2.2), (5.8187297659, 2.0999302145))
                Line((5.8187297659, 2.2), (4.4203463363, 2.2))
                Line((4.4203463363, 2.0999302145), (4.4203463363, 2.2))
            make_face()
        # OneSide extrude, distance=-4.2
        extrude(amount=-4.2, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a linear rail or slide assembly featuring an elongated rectangular body with a central slot running lengthwise, end mounting blocks on both sides, and a dark metallic finish typical of precision machinery components.
def model_130957_57bd641b_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 5 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 44.1, perimeter: 46.2
            with BuildLine():
                Line((21, -2.9), (0, -2.9))
                Line((21, -0.8), (21, -2.9))
                Line((0, -0.8), (21, -0.8))
                Line((0, -2.9), (0, -0.8))
            make_face()
        # OneSide extrude, distance=3
        extrude(amount=3)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 15 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 8.2, perimeter: 12.2
            with BuildLine():
                Line((1, 6.1), (3, 6.1))
                Line((1, 2), (1, 6.1))
                Line((3, 2), (1, 2))
                Line((3, 2), (3, 6.1))
            make_face()
            # Profile area: 22.8, perimeter: 21.2
            with BuildLine():
                Line((3, 13.4214363007), (0.9461541421, 13.4214363007))
                Line((3.9461541421, 13.4214363007), (3, 13.4214363007))
                Line((3.9461541421, 21.0214363007), (3.9461541421, 13.4214363007))
                Line((0.9461541421, 21.0214363007), (3.9461541421, 21.0214363007))
                Line((0.9461541421, 13.4214363007), (0.9461541421, 21.0214363007))
            make_face()
        # OneSide extrude, distance=-2.9
        extrude(amount=-2.9, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.9461541421, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 4.0864704291, perimeter: 16.3113223899
            with BuildLine():
                CenterArc((13.622588082, -17.6458072262), 16.8470081362, 64.0296255603, 25.2862516642)
                Line((21, -2.5), (21, -0.8))
                Line((21, -0.8), (13.8237398632, -0.8))
            make_face()
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.9461541421, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.7576353387, perimeter: 15.6368235809
            with BuildLine():
                CenterArc((11.8886917077, -25.3754802381), 24.6232316101, 68.2825979008, 18.1485525343)
                CenterArc((13.622588082, -17.6458072262), 16.8470081362, 64.0296255603, 25.2862516642)
                Line((13.8237398632, -0.8), (13.4214363007, -0.8))
            make_face()
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(1, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            with Locations((16.7, -1.85)):
                Circle(0.3)
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            with Locations((4.05, -1.85)):
                Circle(0.3)
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.SUBTRACT)

        # Sketch6 -> Extrude6 (Join)
        # Sketch on BRepFace
        # Sketch has 6 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(1, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.3972566612, perimeter: 7.0849555922
            with BuildLine():
                Line((4.65, -2.55), (3.45, -2.55))
                Line((4.65, -1.15), (4.65, -2.55))
                Line((3.45, -1.15), (4.65, -1.15))
                Line((3.45, -2.55), (3.45, -1.15))
            make_face()
            with BuildLine():
                CenterArc((4.05, -1.85), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 1.2689877857, perimeter: 6.862257412
            with BuildLine():
                Line((17.3, -2.55), (17.3, -1.4))
                CenterArc((15.2617427293, -8.1786348993), 7.0784450128, 73.2645739116, 9.9342743128)
                Line((16.1, -2.55), (16.1, -1.15))
                Line((17.3, -2.55), (16.1, -2.55))
            make_face()
            with BuildLine():
                CenterArc((16.7, -1.85), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.4
        extrude(amount=0.4, mode=Mode.ADD)

        # Sketch10 -> Extrude9 (Join)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.9461541421, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.8990457348, perimeter: 5.1512936346
            with BuildLine():
                CenterArc((20.5, 0.9833333333), 3.5190355371, -115.2300098439, 33.398488468)
                Line((19, -2.9), (19, -2.2))
                Line((21, -2.9), (19, -2.9))
                Line((21, -2.9), (21, -2.5))
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2, mode=Mode.ADD)

        # Sketch11 -> Extrude10 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.18, perimeter: 1.8
            with BuildLine():
                Line((0.3, -2.3), (0, -2.3))
                Line((0, -2.3), (0, -2.9))
                Line((0, -2.9), (0.3, -2.9))
                Line((0.3, -2.9), (0.3, -2.3))
            make_face()
        # OneSide extrude, distance=-21
        extrude(amount=-21, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a ring-shaped assembly with a spherical mesh head, featuring a circular band forming the base ring and a textured spherical or bulbous attachment protruding from one side with a mesh or perforated surface pattern.
def model_131626_3d395aec_0000():
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
        # Sketch1 -> Extrusion1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 7.7931132763, perimeter: 9.8960168588
            Circle(1.575)
        # OneSide extrude, distance=0.01
        extrude(amount=0.01)

        # Sketch2 -> Extrusion2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.01), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 6.3347074267, perimeter: 8.9221231362
            Circle(1.42)
        # OneSide extrude, distance=-0.11
        extrude(amount=-0.11, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrusion3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.01), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.6399424235, perimeter: 18.2840692439
            with BuildLine():
                CenterArc((0, 0), 1.49, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.42, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.005
        extrude(amount=-0.005, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrusion4 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 2.8352873699, perimeter: 5.9690260418
            Circle(0.95)
        # OneSide extrude, distance=-1.98
        extrude(amount=-1.98)

        # Sketch5 -> Extrusion5 (Cut)
        # Sketch on BRepFace
        with BuildSketch(Plane.XY):
            # Profile area: 2.8352873699, perimeter: 5.9690260418
            Circle(0.95)
        # OneSide extrude, distance=-1.28
        extrude(amount=-1.28, mode=Mode.SUBTRACT)

        # Sketch6 -> Extrusion6 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -1.28), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.1178097245, perimeter: 4.7123889804
            with BuildLine():
                CenterArc((0, 0), 0.4, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.35, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.4
        extrude(amount=-0.4, mode=Mode.SUBTRACT)

        # Sketch8 -> Extrusion7 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -1.28), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            Circle(0.2)
        # OneSide extrude, distance=-0.7
        extrude(amount=-0.7, mode=Mode.SUBTRACT)

        # Sketch9 -> Extrusion8 (NewBody)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -1.28), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0235619449, perimeter: 4.7123889804
            with BuildLine():
                CenterArc((0, 0), 0.38, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.37, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.6
        extrude(amount=0.6)
    return part.part


# Description: This is a complex molded plastic or composite housing component with an irregular, organic top profile, featuring multiple internal geometric cavities, angular cutouts, and integrated structural ribs visible through semi-transparent sections.
def model_132212_4d7d45f6_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 7 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 27.36, perimeter: 34
            with BuildLine():
                Line((0, 0), (13, 0))
                Line((13, 0), (13, 1.8))
                Line((13, 1.8), (1.8, 1.8))
                Line((1.8, 4), (1.8, 1.8))
                Line((0, 4), (1.8, 4))
                Line((0, 0), (0, 4))
            make_face()
        # OneSide extrude, distance=5
        extrude(amount=5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(1.8, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 7.916813487, perimeter: 14.1097335529
            with BuildLine():
                CenterArc((-2.5, 4), 2.5, 0, 180)
                Line((-3.6, 4), (-5, 4))
                CenterArc((-2.5, 4), 1.1, 0, 180)
                Line((0, 4), (-1.4, 4))
            make_face()
        # OneSide extrude, distance=-1.8
        extrude(amount=-1.8, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(1.8, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.9006635554, perimeter: 5.6557519189
            with BuildLine():
                Line((-1.4, 4), (-3.6, 4))
                CenterArc((-2.5, 4), 1.1, 180, 180)
            make_face()
        # OneSide extrude, distance=-1.8
        extrude(amount=-1.8, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 19 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 5), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1.1038834328, perimeter: 4.6431395653
            with BuildLine():
                CenterArc((7, 4.671769568), 1.8, -90, 68.0865662614)
                Line((7.8710485908, 4), (8.6699477978, 4))
                CenterArc((7, 4.671769568), 1.1, -90, 52.3598936657)
                Line((7, 2.871769568), (7, 3.571769568))
            make_face()
            # Profile area: 2.0848331106, perimeter: 7.4652775442
            with BuildLine():
                CenterArc((7, 4.671769568), 1.8, -21.9134337386, 21.9134337386)
                CenterArc((7, 4.671769568), 1.8, 0, 90)
                Line((7, 5.771769568), (7, 6.471769568))
                CenterArc((7, 4.671769568), 1.1, -37.6401063343, 127.6401063343)
                Line((7.8710485908, 4), (8.6699477978, 4))
            make_face()
            # Profile area: 1.1038834328, perimeter: 4.6431395653
            with BuildLine():
                Line((7, 2.871769568), (7, 3.571769568))
                CenterArc((7, 4.671769568), 1.1, -142.3598936657, 52.3598936657)
                Line((5.3300522022, 4), (6.1289514092, 4))
                CenterArc((7, 4.671769568), 1.8, -158.0865662614, 68.0865662614)
            make_face()
            # Profile area: 2.595807748, perimeter: 7.3408243339
            with BuildLine():
                CenterArc((7, 4.671769568), 1.8, -158.0865662614, 68.0865662614)
                Line((5.2, 4), (5.3300522022, 4))
                Line((5.2, 4), (5.2, 1.8))
                Line((7, 1.8), (5.2, 1.8))
                Line((7, 1.8), (7, 2.871769568))
            make_face()
            # Profile area: 2.595807748, perimeter: 7.3408243339
            with BuildLine():
                Line((7, 1.8), (7, 2.871769568))
                Line((8.5, 1.8), (7, 1.8))
                Line((8.8, 1.8), (8.5, 1.8))
                Line((8.8, 4), (8.8, 1.8))
                Line((8.6699477978, 4), (8.8, 4))
                CenterArc((7, 4.671769568), 1.8, -90, 68.0865662614)
            make_face()
            # Profile area: 2.0848331106, perimeter: 7.4652775442
            with BuildLine():
                CenterArc((7, 4.671769568), 1.1, 90, 127.6401063343)
                Line((7, 5.771769568), (7, 6.471769568))
                CenterArc((7, 4.671769568), 1.8, 90, 90)
                CenterArc((7, 4.671769568), 1.8, 180, 21.9134337386)
                Line((5.3300522022, 4), (6.1289514092, 4))
            make_face()
        # OneSide extrude, distance=-5
        extrude(amount=-5, mode=Mode.ADD)

        # Sketch5 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 5), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 6.3774330868, perimeter: 18.2212373908
            with BuildLine():
                CenterArc((7, 4.671769568), 1.8, -158.0865662614, 136.1731325227)
                CenterArc((7, 4.671769568), 1.8, -21.9134337386, 201.9134337386)
                CenterArc((7, 4.671769568), 1.8, 180, 21.9134337386)
            make_face()
            with BuildLine():
                CenterArc((7, 4.671769568), 1.1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)

        # Sketch6 -> Extrude6 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 6.3774330868, perimeter: 18.2212373908
            with BuildLine():
                CenterArc((-7, 4.671769568), 1.8, -158.0865662614, 136.1731325227)
                CenterArc((-7, 4.671769568), 1.8, -21.9134337386, 201.9134337386)
                CenterArc((-7, 4.671769568), 1.8, 180, 21.9134337386)
            make_face()
            with BuildLine():
                CenterArc((-7, 4.671769568), 1.1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)

        # Sketch7 -> Extrude7 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.8, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 9.8174770425, perimeter: 12.853981634
            with BuildLine():
                CenterArc((-13, 2.5), 2.5, 90, 180)
                Line((-13, 5), (-13, 0))
            make_face()
        # OneSide extrude, distance=-1.8
        extrude(amount=-1.8, mode=Mode.ADD)

        # Sketch8 -> Extrude8 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.8, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.8013271108, perimeter: 6.9115038379
            with Locations((-13, 2.5)):
                Circle(1.1)
        # OneSide extrude, distance=-1.8
        extrude(amount=-1.8, mode=Mode.SUBTRACT)
    return part.part


# Description: This is an oval-shaped mesh or perforated filter basket with a solid rim flange around its base and an open, latticed top surface designed for filtering or straining applications.
def model_132453_391b7740_0000():
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
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.3, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 16.6190251375, perimeter: 14.4513262065
            Circle(2.3)
        # OneSide extrude, distance=0.84
        extrude(amount=0.84, mode=Mode.ADD)

        # Sketch5 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.14, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2400000072, perimeter: 2.0000000298
            with BuildLine():
                Line((-1.6000000238, 0.200000003), (-1.6000000238, -0.200000003))
                Line((-1.6000000238, -0.200000003), (-1.0000000149, -0.200000003))
                Line((-1.0000000149, -0.200000003), (-1.0000000149, 0.200000003))
                Line((-1.0000000149, 0.200000003), (-1.6000000238, 0.200000003))
            make_face()
        # OneSide extrude, distance=0.1
        extrude(amount=0.1, mode=Mode.ADD)

        # Sketch6 -> Extrude4 (Join)
        # Sketch on XY construction plane
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0305292682, perimeter: 1.1537854278
            with BuildLine():
                Line((1.5531238906, 1.24), (1.5531238906, 1.2799476779))
                _nurbs_edge([(1.0547516772, 1.3500000201), (1.0643306684, 1.3470689418), (1.0835226493, 1.3413406983), (1.1124126138, 1.3331500616), (1.1511399325, 1.3230459817), (1.1999180811, 1.3118692928), (1.2490979513, 1.3022748968), (1.2987119267, 1.2943903461), (1.348776954, 1.2882823893), (1.3992743082, 1.2838772733), (1.4501710038, 1.2810450754), (1.4911814397, 1.2799336926), (1.5220936191, 1.2797081158), (1.5427692195, 1.2798235236), (1.5531238906, 1.2799476779)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1, 1, 1, 1, 1], 5)
                Line((1.0547516772, 1.24), (1.0547516772, 1.3500000201))
                Line((1.5531238906, 1.24), (1.0547516772, 1.24))
            make_face()
        # Symmetric extrude, each_side=0.156
        extrude(amount=0.156, both=True, mode=Mode.ADD)
    return part.part


# Description: This is a 3D CAD representation of a solar panel array consisting of six interconnected photovoltaic panels arranged in a slightly staggered, parallelogram-shaped configuration with visible mounting frames and panel divisions.
def model_134381_b7f05dc3_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 691.2, perimeter: 118.4
            with BuildLine():
                Line((-16, 43.2), (0, 43.2))
                Line((-16, 0), (-16, 43.2))
                Line((0, 0), (-16, 0))
                Line((0, 43.2), (0, 0))
            make_face()
        # OneSide extrude, distance=1.8
        extrude(amount=1.8)

        # Sketch4 -> Extrude3 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 694.4, perimeter: 118.8
            with BuildLine():
                Line((2, 43.4), (2, 0))
                Line((2, 0), (18, 0))
                Line((18, 0), (18, 43.4))
                Line((18, 43.4), (2, 43.4))
            make_face()
        # OneSide extrude, distance=1.8
        extrude(amount=1.8)

        # Sketch5 -> Extrude4 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1175, perimeter: 144
            with BuildLine():
                Line((20, 47), (20, 0))
                Line((20, 0), (45, 0))
                Line((45, 0), (45, 47))
                Line((45, 47), (20, 47))
            make_face()
        # OneSide extrude, distance=1.8
        extrude(amount=1.8)

        # Sketch6 -> Extrude5 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1175, perimeter: 144
            with BuildLine():
                Line((47, 47), (47, 0))
                Line((47, 0), (72, 0))
                Line((72, 0), (72, 47))
                Line((72, 47), (47, 47))
            make_face()
        # OneSide extrude, distance=1.8
        extrude(amount=1.8)

        # Sketch7 -> Extrude6 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 400, perimeter: 82
            with BuildLine():
                Line((-34, 25), (-18, 25))
                Line((-34, 0), (-34, 25))
                Line((-18, 0), (-34, 0))
                Line((-18, 25), (-18, 0))
            make_face()
        # OneSide extrude, distance=1.8
        extrude(amount=1.8)

        # Sketch8 -> Extrude7 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 371.2, perimeter: 78.4
            with BuildLine():
                Line((-34, 50.2), (-18, 50.2))
                Line((-34, 27), (-34, 50.2))
                Line((-18, 27), (-34, 27))
                Line((-18, 50.2), (-18, 27))
            make_face()
        # OneSide extrude, distance=1.8
        extrude(amount=1.8)

        # Sketch9 -> Extrude8 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 4 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 268.8, perimeter: 65.6
            with BuildLine():
                Line((-16, 61.8), (0, 61.8))
                Line((-16, 45), (-16, 61.8))
                Line((0, 45), (-16, 45))
                Line((0, 61.8), (0, 45))
            make_face()
        # OneSide extrude, distance=1.8
        extrude(amount=1.8)
    return part.part


# Description: This is a rectangular enclosure or housing with a sloped trapezoidal profile, featuring a blue top panel, dark gray/black side walls, and what appears to be mounting slots or guides along the interior surfaces.
def model_136126_5202c059_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 28 constraints, 9 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 13.4610669171, perimeter: 43.2415415574
            with BuildLine():
                CenterArc((0.3, 7.6000001177), 0.3, 90, 90)
                Line((0, 7.6000001177), (0, 0.3))
                CenterArc((0.3, 0.3), 0.3, 180, 90)
                Line((0.3, 0), (4.2000000671, 0))
                CenterArc((4.2000000671, 0.3), 0.3, -90, 90)
                Line((4.5000000671, 0.3), (4.5000000671, 7.6000001177))
                CenterArc((4.2000000671, 7.6000001177), 0.3, 0, 90)
                Line((4.2000000671, 7.9000001177), (0.3, 7.9000001177))
            make_face()
            with BuildLine():
                Line((3.8000000611, 7.335814966), (0.8000000075, 7.335814966))
                CenterArc((3.8000000611, 7.035814966), 0.3, 0, 90)
                Line((4.1000000611, 1.5000000179), (4.1000000611, 7.035814966))
                CenterArc((3.8000000611, 1.5000000179), 0.3, -90, 90)
                Line((0.8000000075, 1.2000000179), (3.8000000611, 1.2000000179))
                CenterArc((0.8000000075, 1.5000000179), 0.3, -180, 90)
                Line((0.5000000075, 7.035814966), (0.5000000075, 1.5000000179))
                CenterArc((0.8000000075, 7.035814966), 0.3, 90, 90)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 22.0116774812, perimeter: 18.9565855957
            with BuildLine():
                CenterArc((0.8000000075, 7.035814966), 0.3, 90, 90)
                Line((0.5000000075, 7.035814966), (0.5000000075, 1.5000000179))
                CenterArc((0.8000000075, 1.5000000179), 0.3, -180, 90)
                Line((0.8000000075, 1.2000000179), (3.8000000611, 1.2000000179))
                CenterArc((3.8000000611, 1.5000000179), 0.3, -90, 90)
                Line((4.1000000611, 1.5000000179), (4.1000000611, 7.035814966))
                CenterArc((3.8000000611, 7.035814966), 0.3, 0, 90)
                Line((3.8000000611, 7.335814966), (0.8000000075, 7.335814966))
            make_face()
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 16 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 19.1727433388, perimeter: 17.4849555922
            with BuildLine():
                CenterArc((3.7, 1.8), 0.3, -90, 90)
                Line((4, 1.8), (4, 6.7))
                CenterArc((3.7, 6.7), 0.3, 0, 90)
                Line((3.7, 7), (0.8, 7))
                CenterArc((0.8, 6.7), 0.3, 90, 90)
                Line((0.5, 6.7), (0.5, 1.8))
                CenterArc((0.8, 1.8), 0.3, -180, 90)
                Line((0.8, 1.5), (3.7, 1.5))
            make_face()
        # OneSide extrude, distance=0.1
        extrude(amount=0.1, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.936156024, perimeter: 3.4298809819
            with Locations((2.1415924459, 0.7325476022)):
                Circle(0.5458825125)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 6 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -0.5), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.5916898017, perimeter: 7.7178543643
            with BuildLine():
                Line((-3.3179174813, 7.2546264254), (-3.3179174813, 7.2052521399))
                CenterArc((-3.6742456946, 7.2299392826), 0.3571823772, 3.9632349674, 151.8215370647)
                Line((-4, 6.0756426594), (-4, 7.3764431499))
                CenterArc((-3.6742456946, 6.246473414), 0.3678301431, -152.3267664593, 137.9607102831)
                Line((-3.3179174813, 7.2052521399), (-3.3179174813, 6.1552088612))
            make_face()
            with BuildLine():
                CenterArc((-3.6742456946, 6.246473414), 0.2775347705, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-3.6742456946, 7.2299392826), 0.2771986523, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1, mode=Mode.ADD)

        # Sketch6 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.150563591, perimeter: 2.526137672
            with BuildLine():
                CenterArc((1.3509358136, 7.4286899998), 0.2606259391, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((1.3509358136, 7.4286899998), 0.1414213583, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1, mode=Mode.ADD)

        # Sketch9 -> Extrude6 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.2499158298, perimeter: 3.0580312528
            with BuildLine():
                Line((3.1429163173, 7.3485760619), (1.8000000268, 7.3485760619))
                Line((3.1429163173, 7.5346753978), (3.1429163173, 7.3485760619))
                Line((1.8000000268, 7.5346753978), (3.1429163173, 7.5346753978))
                Line((1.8000000268, 7.3485760619), (1.8000000268, 7.5346753978))
            make_face()
        # OneSide extrude, distance=0.1
        extrude(amount=0.1, mode=Mode.ADD)

        # Sketch10 -> Extrude7 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(4.5000000671, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0600000018, perimeter: 1.4000000209
            with BuildLine():
                Line((0.3000000045, 5.9000000879), (0.200000003, 5.9000000879))
                Line((0.3000000045, 6.5000000969), (0.3000000045, 5.9000000879))
                Line((0.200000003, 6.5000000969), (0.3000000045, 6.5000000969))
                Line((0.200000003, 5.9000000879), (0.200000003, 6.5000000969))
            make_face()
        # OneSide extrude, distance=0.1
        extrude(amount=0.1, mode=Mode.ADD)

        # Sketch11 -> Extrude8 (Join)
        # Sketch on BRepFace
        # Sketch has 8 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.0500000015, perimeter: 1.2000000179
            with BuildLine():
                Line((-0.2266743992, 6.5000000969), (-0.3266744007, 6.5000000969))
                Line((-0.2266743992, 7.0000001043), (-0.2266743992, 6.5000000969))
                Line((-0.3266744007, 7.0000001043), (-0.2266743992, 7.0000001043))
                Line((-0.3266744007, 6.5000000969), (-0.3266744007, 7.0000001043))
            make_face()
            # Profile area: 0.0665531193, perimeter: 1.2662124883
            with BuildLine():
                Line((-0.200000003, 5.7000000849), (-0.3331062397, 5.7000000849))
                Line((-0.200000003, 6.2000000924), (-0.200000003, 5.7000000849))
                Line((-0.3331062397, 6.2000000924), (-0.200000003, 6.2000000924))
                Line((-0.3331062397, 5.7000000849), (-0.3331062397, 6.2000000924))
            make_face()
        # OneSide extrude, distance=0.1
        extrude(amount=0.1, mode=Mode.ADD)

        # Sketch12 -> Extrude9 (Join)
        # Sketch on BRepFace
        # Sketch has 12 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((0.9681767788, -0.25)):
                Circle(0.2)
            # Profile area: 0.2828318605, perimeter: 2.4283185665
            with BuildLine():
                CenterArc((2.4000000387, -0.300000003), 0.2, 0, 90)
                Line((1.8000000238, -0.100000003), (2.4000000387, -0.100000003))
                CenterArc((1.8000000238, -0.300000003), 0.2, 90, 90)
                Line((1.6000000238, -0.400000006), (1.6000000238, -0.300000003))
                Line((2.6000000387, -0.400000006), (1.6000000238, -0.400000006))
                Line((2.6000000387, -0.300000003), (2.6000000387, -0.400000006))
            make_face()
        # OneSide extrude, distance=0.05
        extrude(amount=0.05, mode=Mode.ADD)
    return part.part


# Description: This is a long, narrow metal channel or duct component with a parallelogram-like profile, featuring multiple rectangular slots and openings along its length, and appears to be designed for routing cables, wires, or fluid lines in an industrial or automotive assembly.
def model_136127_140a874c_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 97.24, perimeter: 42.2
            with BuildLine():
                Line((6.8, 0), (0, 0))
                Line((6.8, 14.3), (6.8, 0))
                Line((0, 14.3), (6.8, 14.3))
                Line((0, 0), (0, 14.3))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 0, 1), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 97.24, perimeter: 42.2
            with BuildLine():
                Line((0, 14.3), (0, 0))
                Line((0, 0), (6.8, 0))
                Line((6.8, 0), (6.8, 14.3))
                Line((6.8, 14.3), (0, 14.3))
            make_face()
        # OneSide extrude, distance=-0.1
        extrude(amount=-0.1, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 8 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.2, perimeter: 1.8
            with BuildLine():
                Line((0.600000003, 12.1000001803), (0.200000003, 12.1000001803))
                Line((0.600000003, 12.6000001803), (0.600000003, 12.1000001803))
                Line((0.200000003, 12.6000001803), (0.600000003, 12.6000001803))
                Line((0.200000003, 12.1000001803), (0.200000003, 12.6000001803))
            make_face()
            # Profile area: 0.45, perimeter: 3.6
            with BuildLine():
                Line((0.6000000045, 10.000000149), (0.3000000045, 10.000000149))
                Line((0.6000000045, 11.500000149), (0.6000000045, 10.000000149))
                Line((0.3000000045, 11.500000149), (0.6000000045, 11.500000149))
                Line((0.3000000045, 10.000000149), (0.3000000045, 11.500000149))
            make_face()
        # OneSide extrude, distance=-1.6
        extrude(amount=-1.6, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(6.8, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.400000006, perimeter: 2.8000000119
            with BuildLine():
                Line((-0.200000003, 11.0000001788), (-0.6000000089, 11.0000001788))
                Line((-0.200000003, 12.0000001788), (-0.200000003, 11.0000001788))
                Line((-0.6000000089, 12.0000001788), (-0.200000003, 12.0000001788))
                Line((-0.6000000089, 11.0000001788), (-0.6000000089, 12.0000001788))
            make_face()
        # OneSide extrude, distance=-2.4
        extrude(amount=-2.4, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 1.4, perimeter: 5.4
            with BuildLine():
                Line((-4.0182522423, 13.3071067812), (-6.0182522423, 13.3071067812))
                Line((-4.0182522423, 14.0071067812), (-4.0182522423, 13.3071067812))
                Line((-6.0182522423, 14.0071067812), (-4.0182522423, 14.0071067812))
                Line((-6.0182522423, 13.3071067812), (-6.0182522423, 14.0071067812))
            make_face()
        # OneSide extrude, distance=-2.3
        extrude(amount=-2.3, mode=Mode.SUBTRACT)

        # Sketch6 -> Extrude6 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.32, perimeter: 2.4
            with BuildLine():
                Line((2.0000000179, 0.3000000104), (1.2000000179, 0.3000000104))
                Line((2.0000000179, 0.7000000104), (2.0000000179, 0.3000000104))
                Line((1.2000000179, 0.7000000104), (2.0000000179, 0.7000000104))
                Line((1.2000000179, 0.3000000104), (1.2000000179, 0.7000000104))
            make_face()
        # OneSide extrude, distance=-2.1
        extrude(amount=-2.1, mode=Mode.SUBTRACT)

        # Sketch7 -> Extrude7 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.4, perimeter: 2.8
            with BuildLine():
                Line((3.7000000402, 0.3000000104), (2.7000000402, 0.3000000104))
                Line((3.7000000402, 0.7000000104), (3.7000000402, 0.3000000104))
                Line((2.7000000402, 0.7000000104), (3.7000000402, 0.7000000104))
                Line((2.7000000402, 0.3000000104), (2.7000000402, 0.7000000104))
            make_face()
        # OneSide extrude, distance=-6
        extrude(amount=-6, mode=Mode.SUBTRACT)

        # Sketch8 -> Extrude8 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.35, perimeter: 3.3
            with BuildLine():
                Line((5.6000000626, 0.3000000045), (4.2000000626, 0.3000000045))
                Line((5.6000000626, 0.5500000045), (5.6000000626, 0.3000000045))
                Line((4.2000000626, 0.5500000045), (5.6000000626, 0.5500000045))
                Line((4.2000000626, 0.3000000045), (4.2000000626, 0.5500000045))
            make_face()
        # OneSide extrude, distance=-2.3
        extrude(amount=-2.3, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a rectangular wooden pergola or open-roof shelter structure featuring a slatted top canopy, four vertical support posts, horizontal cross-beams, and a lower shelf platform with parallel slats.
def model_136474_c3d4bfa2_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 40 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 15, perimeter: 32
            with BuildLine():
                Line((12, 7.5), (12.5, 7.5))
                Line((12.5, 7.5), (13.5, 7.5))
                Line((13.5, 7.5), (13.5, 8.5))
                Line((-1.5, 8.5), (13.5, 8.5))
                Line((-1.5, 7.5), (-1.5, 8.5))
                Line((-0.5, 7.5), (-1.5, 7.5))
                Line((-0.5, 7.5), (12, 7.5))
            make_face()
        # OneSide extrude, distance=-7.5
        extrude(amount=-7.5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 6.5, perimeter: 27
            with BuildLine():
                Line((0.5, -7), (-12.5, -7))
                Line((-12.5, -7), (-12.5, -7.5))
                Line((-6, -7.5), (-12.5, -7.5))
                Line((-6, -7.5), (0.5, -7.5))
                Line((0.5, -7.5), (0.5, -7))
            make_face()
        # Start offset: -1 (not directly supported, may affect result)
        # OneSide extrude, distance=-5.5
        extrude(amount=-5.5, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 9 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -1), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 7, perimeter: 16
            with BuildLine():
                Line((0, -2), (0, 0))
                Line((0, 0), (-1, 0))
                Line((-1, 0), (-1, -7))
                Line((0, -7), (-1, -7))
                Line((0, -7), (0, -2))
            make_face()
            # Profile area: 7, perimeter: 16
            with BuildLine():
                Line((-11, -7), (-12, -7))
                Line((-11, 0), (-11, -7))
                Line((-11, 0), (-12, 0))
                Line((-12, 0), (-12, -7))
            make_face()
        # Start offset: -0.5 (not directly supported, may affect result)
        # OneSide extrude, distance=-4.5
        extrude(amount=-4.5, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 8 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(12, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 17.4943250485, perimeter: 18.9983787731
            with BuildLine():
                Line((7, -5), (0, -5))
                Line((7, -5), (7, -2.5016214147))
                Line((0, -2.5), (7, -2.5016214147))
                Line((0, -2.5), (0, -5))
            make_face()
        # OneSide extrude, distance=-14
        extrude(amount=-14, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -6), x_dir=(1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.25, perimeter: 2
            with BuildLine():
                Line((12, -1.5), (12, -1))
                Line((12, -1.5), (12.5, -1.5))
                Line((12.5, -1.5), (12.5, -1))
                Line((12.5, -1), (12, -1))
            make_face()
            # Profile area: 5.5, perimeter: 23
            with BuildLine():
                Line((11, -1), (11, -1.5))
                Line((11, -1), (0, -1))
                Line((0, -1.5), (0, -1))
                Line((0, -1.5), (11, -1.5))
            make_face()
            # Profile area: 0.25, perimeter: 2
            with BuildLine():
                Line((0, -1.5), (0, -1))
                Line((0, -1), (-0.5, -1))
                Line((-0.5, -1), (-0.5, -1.5))
                Line((-0.5, -1.5), (0, -1.5))
            make_face()
            # Profile area: 0.5, perimeter: 3
            with BuildLine():
                Line((12, -1), (11, -1))
                Line((11, -1), (11, -1.5))
                Line((11, -1.5), (12, -1.5))
                Line((12, -1.5), (12, -1))
            make_face()
        # Start offset: 0.5 (not directly supported, may affect result)
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.ADD)

        # Sketch6 -> Extrude6 (Join)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(12, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 1.9998552308, perimeter: 8.9994209367
            with BuildLine():
                Line((1, -2.5002316307), (1.5, -2.500347446))
                Line((1, -2.5002316307), (1, -6.5))
                Line((1, -6.5), (1.5, -6.5))
                Line((1.5, -6.5), (1.5, -2.500347446))
            make_face()
            # Profile area: 0.25, perimeter: 2
            with BuildLine():
                Line((1.5, -1.5), (1, -1.5))
                Line((1.5, -1.5), (1.5, -1))
                Line((1.5, -1), (1, -1))
                Line((1, -1), (1, -1.5))
            make_face()
            # Profile area: 0.5001447692, perimeter: 3.0005790901
            with BuildLine():
                Line((1.5, -2.500347446), (1.5, -1.5))
                Line((1.5, -1.5), (1, -1.5))
                Line((1, -1.5), (1, -2.5002316307))
                Line((1, -2.5002316307), (1.5, -2.500347446))
            make_face()
        # Start offset: 0.5 (not directly supported, may affect result)
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.ADD)

        # Sketch8 -> Extrude7 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -1.5), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.25, perimeter: 2
            with BuildLine():
                Line((-12, -1), (-12, -1.5))
                Line((-12, -1), (-12.5, -1))
                Line((-12.5, -1), (-12.5, -1.5))
                Line((-12.5, -1.5), (-12, -1.5))
            make_face()
            # Profile area: 5.75, perimeter: 24
            with BuildLine():
                Line((-11, -1.5), (-11, -1))
                Line((-11, -1.5), (0.5, -1.5))
                Line((0.5, -1.5), (0.5, -1))
                Line((0.5, -1), (-11, -1))
            make_face()
            # Profile area: 0.5, perimeter: 3
            with BuildLine():
                Line((-12, -1.5), (-11, -1.5))
                Line((-11, -1.5), (-11, -1))
                Line((-11, -1), (-12, -1))
                Line((-12, -1), (-12, -1.5))
            make_face()
        # Start offset: 0.5 (not directly supported, may affect result)
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.ADD)

        # Sketch9 -> Extrude8 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, -1, 0), z_dir=(-1, 0, 0))):
            # Profile area: 0.5001447692, perimeter: 3.0005790901
            with BuildLine():
                Line((-1, -1.5), (-1.5, -1.5))
                Line((-1.5, -2.500347446), (-1.5, -1.5))
                Line((-1.5, -2.500347446), (-1, -2.5002316307))
                Line((-1, -2.5002316307), (-1, -1.5))
            make_face()
            # Profile area: 1.9998552308, perimeter: 8.9994209367
            with BuildLine():
                Line((-1.5, -2.500347446), (-1, -2.5002316307))
                Line((-1.5, -6.5), (-1.5, -2.500347446))
                Line((-1.5, -6.5), (-1, -6.5))
                Line((-1, -6.5), (-1, -2.5002316307))
            make_face()
            # Profile area: 0.25, perimeter: 2
            with BuildLine():
                Line((-1, -1.5), (-1, -1))
                Line((-1, -1), (-1.5, -1))
                Line((-1.5, -1.5), (-1.5, -1))
                Line((-1, -1.5), (-1.5, -1.5))
            make_face()
        # Start offset: 0.5 (not directly supported, may affect result)
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.ADD)

        # Sketch10 -> Extrude9 (Join)
        # Sketch on BRepFace
        # Sketch has 26 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -1), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.4790596614, perimeter: 2.9581193229
            with BuildLine():
                Line((-7.2258645661, -1.5), (-6.2258645661, -1.5))
                Line((-7.2258645661, -1.9790596614), (-7.2258645661, -1.5))
                Line((-6.2258645661, -1.9790596614), (-7.2258645661, -1.9790596614))
                Line((-6.2258645661, -1.5), (-6.2258645661, -1.9790596614))
            make_face()
            # Profile area: 0.4790596614, perimeter: 2.9581193229
            with BuildLine():
                Line((-5.7258645661, -1.5), (-4.7258645661, -1.5))
                Line((-5.7258645661, -1.9790596614), (-5.7258645661, -1.5))
                Line((-4.7258645661, -1.9790596614), (-5.7258645661, -1.9790596614))
                Line((-4.7258645661, -1.5), (-4.7258645661, -1.9790596614))
            make_face()
            # Profile area: 0.4790596614, perimeter: 2.9581193229
            with BuildLine():
                Line((-7.7258645661, -1.5), (-7.7258645661, -1.9790596614))
                Line((-8.7258645661, -1.5), (-7.7258645661, -1.5))
                Line((-8.7258645661, -1.9790596614), (-8.7258645661, -1.5))
                Line((-7.7258645661, -1.9790596614), (-8.7258645661, -1.9790596614))
            make_face()
            # Profile area: 0.4790596614, perimeter: 2.9581193229
            with BuildLine():
                Line((-4.2258645661, -1.5), (-3.2258645661, -1.5))
                Line((-4.2258645661, -1.9790596614), (-4.2258645661, -1.5))
                Line((-3.2258645661, -1.9790596614), (-4.2258645661, -1.9790596614))
                Line((-3.2258645661, -1.5), (-3.2258645661, -1.9790596614))
            make_face()
            # Profile area: 0.4674973486, perimeter: 2.909848455
            with BuildLine():
                Line((-2.7258645661, -1.5), (-1.75, -1.5))
                Line((-2.7258645661, -1.9790596614), (-2.7258645661, -1.5))
                Line((-1.75, -1.9790596614), (-2.7258645661, -1.9790596614))
                Line((-1.75, -1.5), (-1.75, -1.9790596614))
            make_face()
            # Profile area: 0.4790596614, perimeter: 2.9581193229
            with BuildLine():
                Line((-10.2258645661, -1.5), (-9.2258645661, -1.5))
                Line((-10.2258645661, -1.9790596614), (-10.2258645661, -1.5))
                Line((-9.2258645661, -1.9790596614), (-10.2258645661, -1.9790596614))
                Line((-9.2258645661, -1.5), (-9.2258645661, -1.9790596614))
            make_face()
        # OneSide extrude, distance=-5.5
        extrude(amount=-5.5, mode=Mode.ADD)
    return part.part


# Description: This is a sheet metal enclosure or bracket with a rectangular box shape featuring multiple cutouts and mounting holes distributed across its surfaces for component access and installation.
def model_136561_426e584d_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 3.75, perimeter: 8
            with BuildLine():
                Line((-0.75, 1.25), (0.75, 1.25))
                Line((-0.75, -1.25), (-0.75, 1.25))
                Line((0.75, -1.25), (-0.75, -1.25))
                Line((0.75, 1.25), (0.75, -1.25))
            make_face()
        # OneSide extrude, distance=0.6
        extrude(amount=0.6)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.6), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1.1426548246, perimeter: 4.1132741229
            with BuildLine():
                CenterArc((0, -0.4), 0.4, -180, 180)
                Line((0.4, -0.4), (0.4, 0.4))
                CenterArc((0, 0.4), 0.4, 0, 180)
                Line((-0.4, 0.4), (-0.4, -0.4))
            make_face()
        # OneSide extrude, distance=-0.3
        extrude(amount=-0.3, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.6), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((0.45, -0.95)):
                Circle(0.15)
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((-0.45, -0.95)):
                Circle(0.15)
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((-0.45, 0.95)):
                Circle(0.15)
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((0.45, 0.95)):
                Circle(0.15)
        # OneSide extrude, distance=-1.2
        extrude(amount=-1.2, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.3), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((0, 0.4)):
                Circle(0.2)
        # OneSide extrude, distance=-0.15
        extrude(amount=-0.15, mode=Mode.SUBTRACT)

        # Sketch6 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.3), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0981747704, perimeter: 1.2853981634
            with BuildLine():
                Line((-0.4, 0.25), (-0.4, -0.25))
                CenterArc((-0.4, 0), 0.25, -90, 180)
            make_face()
            # Profile area: 0.0981747704, perimeter: 1.2853981634
            with BuildLine():
                CenterArc((-0.4, 0), 0.25, 90, 180)
                Line((-0.4, 0.25), (-0.4, -0.25))
            make_face()
        # OneSide extrude, distance=-0.3
        extrude(amount=-0.3, mode=Mode.SUBTRACT)

        # Sketch9 -> Extrude6 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.6), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0353429174, perimeter: 0.771238898
            with BuildLine():
                Line((-0.4, -0.15), (-0.4, 0.15))
                CenterArc((-0.4, 0), 0.15, 90, 180)
            make_face()
        # OneSide extrude, distance=-1.1
        extrude(amount=-1.1, mode=Mode.SUBTRACT)

        # Sketch10 -> Extrude7 (Join)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 0, 0.6), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0378927652, perimeter: 0.6900540061
            with Locations((-0.0595067492, -1.0096437108)):
                Circle(0.1098255061)
        # OneSide extrude, distance=0.6
        extrude(amount=0.6, mode=Mode.ADD)
    return part.part


# Description: A handheld game controller with a symmetrical ergonomic design featuring two rounded grip sections on either side, a central control panel with buttons and joysticks, and a curved top surface connecting the grips.
def model_136600_cf00e137_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 57.7951351589, perimeter: 35.5040335841
            with BuildLine():
                CenterArc((2.4958811786, 2.4916308008), 2.5139589878, 90, 245)
                Line((4.7743017856, 1.4291858232), (9.4980668792, 1.4291858232))
                CenterArc((11.7764874861, 2.4916308008), 2.5139589878, -155, 245)
                Line((2.4958811786, 5.0055897886), (11.7764874861, 5.0055897886))
            make_face()
        # OneSide extrude, distance=0.7
        extrude(amount=0.7)

        # Sketch3 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 8 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.7), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 4.9087385212, perimeter: 7.853981634
            with Locations((-2.4958811786, -2.4916308008)):
                Circle(1.25)
        # OneSide extrude, distance=-0.3
        extrude(amount=-0.3, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.7), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 9.6211275016, perimeter: 10.9955742876
            with Locations((-11.7764874861, -2.4916308008)):
                Circle(1.75)
        # OneSide extrude, distance=-0.3
        extrude(amount=-0.3, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 18 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.4), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 2.9918475485, perimeter: 8
            with BuildLine():
                Line((-2.0003090645, -3.4992723835), (-2.0003090645, -2.9829674805))
                Line((-2.0003090645, -2.9829674805), (-1.5003090645, -2.9829674805))
                Line((-1.5003090645, -2.9829674805), (-1.5003090645, -1.9992723835))
                Line((-2.0003090645, -1.9992723835), (-1.5003090645, -1.9992723835))
                Line((-2.0003090645, -1.4992723835), (-2.0003090645, -1.9992723835))
                Line((-3.0003090645, -1.4992723835), (-2.0003090645, -1.4992723835))
                Line((-3.0003090645, -1.9992723835), (-3.0003090645, -1.4992723835))
                Line((-3.5003090645, -1.9992723835), (-3.0003090645, -1.9992723835))
                Line((-3.5003090645, -2.4992723835), (-3.5003090645, -1.9992723835))
                Line((-3.5003090645, -2.9992723835), (-3.5003090645, -2.4992723835))
                Line((-3.0003090645, -2.9992723835), (-3.5003090645, -2.9992723835))
                Line((-3.0003090645, -3.4992723835), (-3.0003090645, -2.9992723835))
                Line((-2.0003090645, -3.4992723835), (-3.0003090645, -3.4992723835))
            make_face()
        # OneSide extrude, distance=0.4
        extrude(amount=0.4, mode=Mode.ADD)

        # Sketch6 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 9 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.8), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((-3.0003049106, -2.4972342537)):
                Circle(0.25)
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((-2.5003090645, -2.9951961578)):
                Circle(0.25)
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((-2.0003132183, -2.4931580618)):
                Circle(0.25)
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((-2.5003090645, -1.9951961578)):
                Circle(0.25)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1, mode=Mode.ADD)

        # Sketch8 -> Extrude6 (Join)
        # Sketch on Profile plane
        # Sketch has 42 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.4), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.4, perimeter: 2.8
            with BuildLine():
                Line((12.5764874861, 2.9916308008), (12.9764874861, 2.9916308008))
                Line((12.5764874861, 1.9916308008), (12.5764874861, 2.9916308008))
                Line((12.9764874861, 1.9916308008), (12.5764874861, 1.9916308008))
                Line((12.9764874861, 2.9916308008), (12.9764874861, 1.9916308008))
            make_face()
            # Profile area: 0.4, perimeter: 2.8
            with BuildLine():
                Line((11.2764874861, 3.6916308008), (12.2764874861, 3.6916308008))
                Line((11.2764874861, 3.2916308008), (11.2764874861, 3.6916308008))
                Line((12.2764874861, 3.2916308008), (11.2764874861, 3.2916308008))
                Line((12.2764874861, 3.6916308008), (12.2764874861, 3.2916308008))
            make_face()
            # Profile area: 0.4, perimeter: 2.8
            with BuildLine():
                Line((10.5764874861, 2.9916308008), (10.9764874861, 2.9916308008))
                Line((10.5764874861, 1.9916308008), (10.5764874861, 2.9916308008))
                Line((10.9764874861, 1.9916308008), (10.5764874861, 1.9916308008))
                Line((10.9764874861, 2.9916308008), (10.9764874861, 1.9916308008))
            make_face()
            # Profile area: 0.4, perimeter: 2.8
            with BuildLine():
                Line((11.2764874861, 1.6916308008), (12.2764874861, 1.6916308008))
                Line((11.2764874861, 1.2916308008), (11.2764874861, 1.6916308008))
                Line((12.2764874861, 1.2916308008), (11.2764874861, 1.2916308008))
                Line((12.2764874861, 1.6916308008), (12.2764874861, 1.2916308008))
            make_face()
        # OneSide extrude, distance=0.3
        extrude(amount=0.3, mode=Mode.ADD)

        # Sketch9 -> Extrude7 (Join)
        # Sketch on Profile plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.4), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((11.7764874861, 2.4916308008)):
                Circle(0.5)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3, mode=Mode.ADD)

        # Sketch11 -> Extrude8 (Cut)
        # Sketch on Profile plane
        # Sketch has 9 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.7), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 5, perimeter: 12
            with BuildLine():
                Line((4.6361843324, 2.9916308008), (9.6361843324, 2.9916308008))
                Line((4.6361843324, 1.9916308008), (4.6361843324, 2.9916308008))
                Line((9.6361843324, 1.9916308008), (4.6361843324, 1.9916308008))
                Line((9.6361843324, 2.9916308008), (9.6361843324, 1.9916308008))
            make_face()
        # OneSide extrude, distance=-0.3
        extrude(amount=-0.3, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a rectangular enclosure or chassis with an open frame structure featuring internal cross-bracing, multiple panel sections (some solid, some transparent or mesh), and cable routing paths along its interior surfaces.
def model_137053_59e609b3_0007():
    """Model: Cover"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 30, perimeter: 22
            with BuildLine():
                Line((-2.5, 3), (-2.5, -3))
                Line((-2.5, -3), (2.5, -3))
                Line((2.5, -3), (2.5, 3))
                Line((2.5, 3), (-2.5, 3))
            make_face()
        # OneSide extrude, distance=1.6
        extrude(amount=1.6)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1.6), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 24.64, perimeter: 20
            with BuildLine():
                Line((-2.2, 2.8), (2.2, 2.8))
                Line((-2.2, -2.8), (-2.2, 2.8))
                Line((2.2, -2.8), (-2.2, -2.8))
                Line((2.2, 2.8), (2.2, -2.8))
            make_face()
        # OneSide extrude, distance=-1.3
        extrude(amount=-1.3, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            with Locations((-0.25, -0.65)):
                Circle(0.3)
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            with Locations((-0.25, 0.65)):
                Circle(0.3)
        # OneSide extrude, distance=0.05
        extrude(amount=0.05, mode=Mode.ADD)

        # Sketch6 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -0.05), x_dir=(1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.0490873852, perimeter: 0.7853981634
            with Locations((-0.25, -0.65)):
                Circle(0.125)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3, mode=Mode.ADD)

        # Sketch8 -> Extrude7 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -0.05), x_dir=(1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.0490873852, perimeter: 0.7853981634
            with Locations((-0.25, 0.65)):
                Circle(0.125)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3, mode=Mode.ADD)

        # Sketch9 -> Extrude8 (Join)
        # Sketch on BRepFace
        # Sketch has 9 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.3), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.3742472264, perimeter: 2.2929235569
            with BuildLine():
                CenterArc((1.95, -2.55), 0.4, 51.3178125465, 167.364374907)
                Line((1.6377501001, -2.8), (2.2, -2.8))
                Line((2.2, -2.8), (2.2, -2.2377501001))
            make_face()
            # Profile area: 0.3742472264, perimeter: 2.2929235569
            with BuildLine():
                Line((2.2, 2.2377501001), (2.2, 2.8))
                Line((2.2, 2.8), (1.6377501001, 2.8))
                CenterArc((1.95, 2.55), 0.4, 141.3178125465, 167.364374907)
            make_face()
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            with Locations((-1.7, -0.6)):
                Circle(0.4)
        # OneSide extrude, distance=1.7
        extrude(amount=1.7, mode=Mode.ADD)

        # Sketch10 -> Extrude9 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 2), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((-1.7, -0.6)):
                Circle(0.25)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3, mode=Mode.ADD)

        # Sketch11 -> Extrude10 (Join)
        # Sketch on BRepFace
        # Sketch has 10 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.000000022, -0.0000000077, 1.6), x_dir=(-1, 0.0000000117, 0), z_dir=(0, 0, 1))):
            # Profile area: 3.28, perimeter: 27.4
            with BuildLine():
                Line((-2.1999999453, -2.8000000334), (-2.2000000108, 2.7999999666))
                Line((-2.2000000108, 2.7999999666), (1.4999999892, 2.8000000098))
                Line((1.4999999892, 2.8000000098), (1.4999999869, 3.0000000098))
                Line((1.4999999869, 3.0000000098), (-2.5000000131, 2.9999999631))
                Line((-2.5000000131, 2.9999999631), (-2.499999943, -3.0000000369))
                Line((-2.499999943, -3.0000000369), (1.500000057, -2.9999999902))
                Line((1.5000000547, -2.7999999902), (1.500000057, -2.9999999902))
                Line((1.5000000547, -2.7999999902), (-2.1999999453, -2.8000000334))
            make_face()
            # Profile area: 2.08, perimeter: 15.4
            with BuildLine():
                Line((1.5000000547, -2.7999999902), (1.500000057, -2.9999999902))
                Line((1.500000057, -2.9999999902), (2.500000057, -2.9999999785))
                Line((2.500000057, -2.9999999785), (2.4999999869, 3.0000000215))
                Line((2.4999999869, 3.0000000215), (1.4999999869, 3.0000000098))
                Line((1.4999999892, 2.8000000098), (1.4999999869, 3.0000000098))
                Line((1.4999999892, 2.8000000098), (1.6377500893, 2.8000000114))
                Line((1.6377500893, 2.8000000114), (2.1999999892, 2.800000018))
                Line((2.1999999892, 2.800000018), (2.1999999958, 2.2377501181))
                Line((2.1999999958, 2.2377501181), (2.2000000481, -2.2377500821))
                Line((2.2000000481, -2.2377500821), (2.2000000547, -2.799999982))
                Line((2.2000000547, -2.799999982), (1.6377501548, -2.7999999886))
                Line((1.6377501548, -2.7999999886), (1.5000000547, -2.7999999902))
            make_face()
        # OneSide extrude, distance=0.4
        extrude(amount=0.4, mode=Mode.ADD)
    return part.part


# Description: This is a hinge or connector assembly consisting of two elongated rectangular boxes joined by a cylindrical pin or rod, allowing rotational movement between the two components.
def model_138267_3dbc9e31_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            Circle(1)
        # OneSide extrude, distance=5
        extrude(amount=5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 5), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1.96, perimeter: 5.6
            with BuildLine():
                Line((0.7, -0.7), (0.7, 0.7))
                Line((0.7, 0.7), (-0.7, 0.7))
                Line((-0.7, 0.7), (-0.7, -0.7))
                Line((-0.7, -0.7), (0.7, -0.7))
            make_face()
        # OneSide extrude, distance=1.4
        extrude(amount=1.4, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.7, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 1.1309733553, perimeter: 3.7699111843
            with Locations((0, 5.7)):
                Circle(0.6)
        # OneSide extrude, distance=10
        extrude(amount=10, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(10.7, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 2.0106192983, perimeter: 10.0530964915
            with BuildLine():
                CenterArc((0, 5.7), 1, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 5.7), 0.6, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 1.1309733553, perimeter: 3.7699111843
            with Locations((0, 5.7)):
                Circle(0.6)
        # OneSide extrude, distance=9.5
        extrude(amount=9.5, mode=Mode.ADD)

        # Sketch7 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 6.4), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 83.04, perimeter: 49.6
            with BuildLine():
                Line((8.5, -2.5), (-8.5, -2.5))
                Line((8.5, 2.5), (8.5, -2.5))
                Line((-8.5, 2.5), (8.5, 2.5))
                Line((-8.5, -2.5), (-8.5, 2.5))
            make_face()
            with BuildLine():
                Line((-0.7, 0.7), (-0.7, -0.7))
                Line((0.7, 0.7), (-0.7, 0.7))
                Line((0.7, -0.7), (0.7, 0.7))
                Line((-0.7, -0.7), (0.7, -0.7))
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 1.96, perimeter: 5.6
            with BuildLine():
                Line((-0.7, -0.7), (0.7, -0.7))
                Line((0.7, -0.7), (0.7, 0.7))
                Line((0.7, 0.7), (-0.7, 0.7))
                Line((-0.7, 0.7), (-0.7, -0.7))
            make_face()
        # OneSide extrude, distance=15
        extrude(amount=15, mode=Mode.ADD)

        # Sketch8 -> Extrude6 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-8.5, 0, 0), x_dir=(0, -1, 0), z_dir=(-1, 0, 0))):
            # Profile area: 18.7896491635, perimeter: 31.9965664884
            with BuildLine():
                Line((-1.9988244938, 6.4), (-1.9988244938, 21))
                Line((0.5751000492, 6.4025485346), (-1.9988244938, 6.4))
                Line((-1.9988244938, 21), (0.5751000492, 6.4025485346))
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)

        # Sketch12 -> Extrude8 (Join)
        # Sketch on XY construction plane
        # Sketch has 8 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 85, perimeter: 44
            with BuildLine():
                Line((8.5, -2.5), (8.5, 2.5))
                Line((8.5, 2.5), (-8.5, 2.5))
                Line((-8.5, 2.5), (-8.5, -2.5))
                Line((-8.5, -2.5), (8.5, -2.5))
            make_face()
        # OneSide extrude, distance=-35
        extrude(amount=-35, mode=Mode.ADD)
    return part.part


# Description: This is a spacecraft or satellite module with a polygonal/faceted metallic body, featuring a cylindrical thruster or instrument component on one end, solar panels or radiator surfaces, and internal structural framework visible through the geometric mesh design.
def model_138657_5a4a4283_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 2.0706, perimeter: 6.1
            with BuildLine():
                Line((0.51, -1.015), (-0.51, -1.015))
                Line((0.51, 1.015), (0.51, -1.015))
                Line((-0.51, 1.015), (0.51, 1.015))
                Line((-0.51, -1.015), (-0.51, 1.015))
            make_face()
        # OneSide extrude, distance=2.03
        extrude(amount=2.03)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -1.015, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.204, perimeter: 2.44
            with BuildLine():
                Line((0.51, 1.5309329659), (-0.51, 1.5309329659))
                Line((-0.51, 1.5309329659), (-0.51, 1.3309329659))
                Line((-0.51, 1.3309329659), (0.51, 1.3309329659))
                Line((0.51, 1.3309329659), (0.51, 1.5309329659))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)

        # Sketch6 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 2.03), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.9597490884, perimeter: 3.6673635099
            with BuildLine():
                CenterArc((0, -0.015), 0.3, -14.7029121148, 209.4058242295)
                CenterArc((0, -0.5075), 0.5075, 124.8741834612, 145.1258165388)
                CenterArc((0, -0.5075), 0.5075, -90, 145.1258165388)
            make_face()
        # OneSide extrude, distance=0.4
        extrude(amount=0.4, mode=Mode.ADD)

        # Sketch7 -> Extrude6 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 2.43), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0380132711, perimeter: 0.6911503838
            Circle(0.11)
        # OneSide extrude, distance=0.02
        extrude(amount=0.02, mode=Mode.ADD)

        # Sketch8 -> Extrude7 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 2.03), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.5168908913, perimeter: 2.9007388736
            with BuildLine():
                CenterArc((0, -0.015), 0.3, 87.1793047105, 5.6413905789)
                Line((0.41, 0.2846365283), (0.0147631609, 0.2846365283))
                Line((0.41, 0.915), (0.41, 0.2846365283))
                Line((-0.41, 0.915), (0.41, 0.915))
                Line((-0.41, 0.2846365283), (-0.41, 0.915))
                Line((-0.0147631609, 0.2846365283), (-0.41, 0.2846365283))
            make_face()
        # OneSide extrude, distance=-0.01
        extrude(amount=-0.01, mode=Mode.SUBTRACT)

        # Sketch9 -> Extrude8 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 2.43), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((0, -0.5075)):
                Circle(0.2)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3, mode=Mode.ADD)

        # Sketch10 -> Extrude9 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 2.73), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0078539816, perimeter: 0.3141592654
            with Locations((0, -0.5075)):
                Circle(0.05)
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2, mode=Mode.SUBTRACT)

        # Sketch11 -> Extrude10 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.0562910151, perimeter: 0.924835249
            with BuildLine():
                CenterArc((-0.46, 0.965), 0.2061552813, -104.0362434679, 118.0724869359)
                Line((-0.26, 1.015), (-0.51, 1.015))
                Line((-0.51, 1.015), (-0.51, 0.765))
            make_face()
            # Profile area: 0.0562910151, perimeter: 0.924835249
            with BuildLine():
                CenterArc((0.46, 0.965), 0.2061552813, 165.9637565321, 118.0724869359)
                Line((0.51, 0.765), (0.51, 1.015))
                Line((0.51, 1.015), (0.26, 1.015))
            make_face()
            # Profile area: 0.0562910151, perimeter: 0.924835249
            with BuildLine():
                CenterArc((-0.46, -0.965), 0.2061552813, -14.0362434679, 118.0724869359)
                Line((-0.51, -0.765), (-0.51, -1.015))
                Line((-0.51, -1.015), (-0.26, -1.015))
            make_face()
            # Profile area: 0.0562910151, perimeter: 0.924835249
            with BuildLine():
                Line((0.26, -1.015), (0.51, -1.015))
                Line((0.51, -1.015), (0.51, -0.765))
                CenterArc((0.46, -0.965), 0.2061552813, 75.9637565321, 118.0724869359)
            make_face()
        # OneSide extrude, distance=-0.05
        extrude(amount=-0.05, mode=Mode.SUBTRACT)

        # Sketch13 -> Extrude11 (NewBody)
        # Sketch on BRepFace
        # Sketch has 13 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.015, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0078539816, perimeter: 0.3141592654
            with BuildLine():
                CenterArc((-0.1, 0.6), 0.05, 180, 90.0000013476)
                CenterArc((-0.1, 0.6), 0.05, -89.9999986524, 89.9999986524)
                CenterArc((-0.1, 0.6), 0.05, 0, 90.0000013478)
                CenterArc((-0.1, 0.6), 0.05, 90.0000013478, 89.9999986522)
            make_face()
            # Profile area: 0.0078539816, perimeter: 0.3141592654
            with BuildLine():
                CenterArc((0, 0.6), 0.05, 90, 90)
                CenterArc((0, 0.6), 0.05, 180, 90)
                CenterArc((0, 0.6), 0.05, -90, 90)
                CenterArc((0, 0.6), 0.05, 0, 90)
            make_face()
            # Profile area: 0.0078539816, perimeter: 0.3141592654
            with BuildLine():
                CenterArc((0.1, 0.6), 0.05, 89.9999986524, 90.0000013476)
                CenterArc((0.1, 0.6), 0.05, 180, 89.9999986522)
                CenterArc((0.1, 0.6), 0.05, -90.0000013478, 90.0000013478)
                CenterArc((0.1, 0.6), 0.05, 0, 89.9999986524)
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)
    return part.part


# Description: This is a rectangular box or enclosure with a hinged or removable top panel (shown in light blue), internal ribbed reinforcement structures, and mounting holes or lugs along one side for attachment purposes.
def model_145894_f94b265c_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrusion1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 2, perimeter: 9
            with BuildLine():
                Line((0, 4), (0, 0))
                Line((0, 0), (0.5, 0))
                Line((0.5, 0), (0.5, 4))
                Line((0.5, 4), (0, 4))
            make_face()
        # OneSide extrude, distance=6
        extrude(amount=6)

        # Sketch2 -> Extrusion2 (Join)
        # Sketch on BRepFace
        # Sketch has 16 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.5, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 0.3, perimeter: 12.1
            with BuildLine():
                Line((2.7491787963, 6), (2.7491787963, 0))
                Line((2.7491787963, 6), (2.6991787963, 6))
                Line((2.6991787963, 6), (2.6991787963, 0))
                Line((2.6991787963, 0), (2.7491787963, 0))
            make_face()
            # Profile area: 0.3, perimeter: 12.1
            with BuildLine():
                Line((3.299303512, 6), (3.249303512, 6))
                Line((3.249303512, 6), (3.249303512, 0))
                Line((3.249303512, 0), (3.299303512, 0))
                Line((3.299303512, 6), (3.299303512, 0))
            make_face()
            # Profile area: 0.3, perimeter: 12.1
            with BuildLine():
                Line((1.3015977688, 6), (1.3015977688, 0))
                Line((1.3015977688, 6), (1.2515977688, 6))
                Line((1.2515977688, 6), (1.2515977688, 0))
                Line((1.2515977688, 0), (1.3015977688, 0))
            make_face()
            # Profile area: 0.3, perimeter: 12.1
            with BuildLine():
                Line((0.7063573481, 6), (0.7063573481, 0))
                Line((0.7063573481, 6), (0.6563573481, 6))
                Line((0.6563573481, 6), (0.6563573481, 0))
                Line((0.6563573481, 0), (0.7063573481, 0))
            make_face()
        # OneSide extrude, distance=0.17
        extrude(amount=0.17, mode=Mode.ADD)

        # Sketch3 -> Extrusion3 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.67, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 0.3, perimeter: 12.1
            with BuildLine():
                Line((3.349303512, 0), (3.299303512, 0))
                Line((3.349303512, 6), (3.349303512, 0))
                Line((3.299303512, 6), (3.349303512, 6))
                Line((3.299303512, 0), (3.299303512, 6))
            make_face()
            # Profile area: 0.3, perimeter: 12.1
            with BuildLine():
                Line((3.299303512, 0), (3.299303512, 6))
                Line((3.249303512, 6), (3.299303512, 6))
                Line((3.249303512, 0), (3.249303512, 6))
                Line((3.299303512, 0), (3.249303512, 0))
            make_face()

        # Sketch6 -> Extrusion3 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.67, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 0.3, perimeter: 12.1
            with BuildLine():
                Line((0.6563573481, 6), (0.6563573481, 0))
                Line((0.6563573481, 6), (0.6063573481, 6))
                Line((0.6063573481, 6), (0.6063573481, 0))
                Line((0.6063573481, 0), (0.6563573481, 0))
            make_face()
            # Profile area: 0.3, perimeter: 12.1
            with BuildLine():
                Line((0.7063573481, 0), (0.7063573481, 6))
                Line((0.7063573481, 6), (0.6563573481, 6))
                Line((0.6563573481, 6), (0.6563573481, 0))
                Line((0.6563573481, 0), (0.7063573481, 0))
            make_face()

        # Sketch4 -> Extrusion3 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.67, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 0.3, perimeter: 12.1
            with BuildLine():
                Line((2.7491787963, 0), (2.7491787963, 6))
                Line((2.7491787963, 6), (2.6991787963, 6))
                Line((2.6991787963, 6), (2.6991787963, 0))
                Line((2.6991787963, 0), (2.7491787963, 0))
            make_face()
            # Profile area: 0.3, perimeter: 12.1
            with BuildLine():
                Line((2.6991787963, 6), (2.6991787963, 0))
                Line((2.6991787963, 6), (2.6491787963, 6))
                Line((2.6491787963, 6), (2.6491787963, 0))
                Line((2.6491787963, 0), (2.6991787963, 0))
            make_face()

        # Sketch5 -> Extrusion3 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.67, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 0.3, perimeter: 12.1
            with BuildLine():
                Line((1.3515977688, 0), (1.3015977688, 0))
                Line((1.3515977688, 6), (1.3515977688, 0))
                Line((1.3015977688, 6), (1.3515977688, 6))
                Line((1.3015977688, 0), (1.3015977688, 6))
            make_face()
            # Profile area: 0.3, perimeter: 12.1
            with BuildLine():
                Line((1.3015977688, 0), (1.3015977688, 6))
                Line((1.2515977688, 6), (1.3015977688, 6))
                Line((1.2515977688, 0), (1.2515977688, 6))
                Line((1.3015977688, 0), (1.2515977688, 0))
            make_face()
        # OneSide extrude, distance=0.15
        extrude(amount=0.15, mode=Mode.ADD)

        # Sketch7 -> Extrusion4 (Join)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, -1, 0), z_dir=(-1, 0, 0))):
            # Profile area: 24, perimeter: 20
            with BuildLine():
                Line((0, 0), (-4, 0))
                Line((0, 6), (0, 0))
                Line((-4, 6), (0, 6))
                Line((-4, 0), (-4, 6))
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2, mode=Mode.ADD)

        # Sketch11 -> Extrusion5 (Join)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 4, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 15, perimeter: 17
            with BuildLine():
                Line((2, 0), (-0.5, 0))
                Line((2, 6), (2, 0))
                Line((-0.5, 6), (2, 6))
                Line((-0.5, 0), (-0.5, 6))
            make_face()
        # OneSide extrude, distance=0.05
        extrude(amount=0.05, mode=Mode.ADD)
    return part.part


# Description: This is an angular, L-shaped or boot-shaped structural component with a hollow interior cavity, featuring faceted surfaces, internal ribbing/bracing elements, and stepped edges along its base, appearing to be a stamped or cast metal bracket or support frame.
def model_146291_6b0c8db3_0002():
    """Model: лестница v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude2 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 82 constraints, 11 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2079999806, perimeter: 2.1199999255
            with BuildLine():
                Line((2.76, -5.8), (2.76, -5.0000000745))
                Line((2.76, -5.0000000745), (2.63, -5.0000000745))
                Line((2.63, -5.0000000745), (2.5, -5))
                Line((2.5, -5.8), (2.5, -5))
                Line((2.5, -5.8), (2.63, -5.8))
                Line((2.63, -5.8), (2.76, -5.8))
            make_face()
        # OneSide extrude, distance=-0.1
        extrude(amount=-0.1)

        # Sketch1 -> Extrude3 (Join)
        # Sketch on XZ construction plane
        # Sketch has 82 constraints, 11 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2079999806, perimeter: 2.119999851
            with BuildLine():
                Line((3.02, -5.0000000745), (3.02, -5.8))
                Line((3.02, -5.0000000745), (2.89, -5.0000000745))
                Line((2.89, -5.0000000745), (2.76, -5.0000000745))
                Line((2.76, -5.8), (2.76, -5.0000000745))
                Line((2.76, -5.8), (2.89, -5.8))
                Line((2.89, -5.8), (3.02, -5.8))
            make_face()
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2, mode=Mode.ADD)

        # Sketch1 -> Extrude4 (Join)
        # Sketch on XZ construction plane
        # Sketch has 82 constraints, 11 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2079999903, perimeter: 2.119999851
            with BuildLine():
                Line((3.15, -5), (3.02, -5.0000000745))
                Line((3.02, -5.0000000745), (3.02, -5.8))
                Line((3.02, -5.8), (3.15, -5.8))
                Line((3.15, -5.8), (3.28, -5.8))
                Line((3.28, -5.0000000745), (3.28, -5.8))
                Line((3.28, -5.0000000745), (3.15, -5))
            make_face()
        # OneSide extrude, distance=-0.3
        extrude(amount=-0.3, mode=Mode.ADD)

        # Sketch1 -> Extrude5 (Join)
        # Sketch on XZ construction plane
        # Sketch has 82 constraints, 11 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2079999806, perimeter: 2.119999851
            with BuildLine():
                Line((3.28, -5.0000000745), (3.28, -5.8))
                Line((3.28, -5.8), (3.41, -5.8))
                Line((3.41, -5.8), (3.54, -5.8))
                Line((3.54, -5.0000000745), (3.54, -5.8))
                Line((3.54, -5.0000000745), (3.41, -5.0000000745))
                Line((3.41, -5.0000000745), (3.28, -5.0000000745))
            make_face()
        # OneSide extrude, distance=-0.4
        extrude(amount=-0.4, mode=Mode.ADD)

        # Sketch1 -> Extrude6 (Join)
        # Sketch on XZ construction plane
        # Sketch has 82 constraints, 11 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2079999806, perimeter: 2.119999851
            with BuildLine():
                Line((3.54, -5.0000000745), (3.54, -5.8))
                Line((3.54, -5.8), (3.67, -5.8))
                Line((3.67, -5.8), (3.8, -5.8))
                Line((3.8, -5.8), (3.8000000566, -5.0000000745))
                Line((3.8000000566, -5.0000000745), (3.67, -5.0000000745))
                Line((3.67, -5.0000000745), (3.54, -5.0000000745))
            make_face()
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.ADD)

        # Sketch1 -> Extrude7 (Join)
        # Sketch on XZ construction plane
        # Sketch has 82 constraints, 11 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.6400000417, perimeter: 3.2000000179
            with BuildLine():
                Line((3.8, -5.8), (3.8000000566, -5.0000000745))
                Line((4.6000000685, -5.8000000864), (3.8, -5.8))
                Line((4.6000000685, -5.0000000745), (4.6000000685, -5.8000000864))
                Line((3.8000000566, -5.0000000745), (4.6000000685, -5.0000000745))
            make_face()
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.ADD)

        # Sketch1 -> Extrude8 (Join)
        # Sketch on XZ construction plane
        # Sketch has 82 constraints, 11 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2080000031, perimeter: 2.1200000238
            with BuildLine():
                Line((3.8000000566, -5.0000000745), (4.6000000685, -5.0000000745))
                Line((4.6000000685, -5.0000000745), (4.6000000685, -4.8700000745))
                Line((4.6000000685, -4.8700000745), (4.6000000685, -4.7400000745))
                Line((4.0600000566, -4.7400000745), (4.6000000685, -4.7400000745))
                Line((3.8000000566, -4.7400000745), (4.0600000566, -4.7400000745))
                Line((3.8000000566, -4.7400000745), (3.8000000566, -4.8700000745))
                Line((3.8000000566, -4.8700000745), (3.8000000566, -5.0000000745))
            make_face()
        # OneSide extrude, distance=-0.6
        extrude(amount=-0.6, mode=Mode.ADD)

        # Sketch1 -> Extrude9 (Join)
        # Sketch on XZ construction plane
        # Sketch has 82 constraints, 11 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2080000031, perimeter: 2.1200000238
            with BuildLine():
                Line((3.8000000566, -4.7400000745), (4.0600000566, -4.7400000745))
                Line((4.0600000566, -4.7400000745), (4.6000000685, -4.7400000745))
                Line((4.6000000685, -4.7400000745), (4.6000000685, -4.4800000745))
                Line((3.8000000566, -4.4800000745), (4.6000000685, -4.4800000745))
                Line((3.8000000566, -4.4800000745), (3.8000000566, -4.5000000671))
                Line((3.8000000566, -4.5000000671), (3.8000000566, -4.7400000745))
            make_face()
        # OneSide extrude, distance=-0.7
        extrude(amount=-0.7, mode=Mode.ADD)

        # Sketch1 -> Extrude10 (Join)
        # Sketch on XZ construction plane
        # Sketch has 82 constraints, 11 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2080000031, perimeter: 2.1200000238
            with BuildLine():
                Line((3.8000000566, -4.4800000745), (4.6000000685, -4.4800000745))
                Line((4.6000000685, -4.4800000745), (4.6000000685, -4.2200000745))
                Line((3.8000000566, -4.2200000745), (4.6000000685, -4.2200000745))
                Line((3.8000000566, -4.2200000745), (3.8000000566, -4.4800000745))
            make_face()
        # OneSide extrude, distance=-0.8
        extrude(amount=-0.8, mode=Mode.ADD)

        # Sketch1 -> Extrude11 (Join)
        # Sketch on XZ construction plane
        # Sketch has 82 constraints, 11 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2080000031, perimeter: 2.1200000238
            with BuildLine():
                Line((3.8000000566, -4.2200000745), (4.6000000685, -4.2200000745))
                Line((4.6000000685, -4.2200000745), (4.6000000685, -3.9600000745))
                Line((4.6000000685, -3.9600000745), (3.8000000566, -3.9600000745))
                Line((3.8000000566, -3.9600000745), (3.8000000566, -4.2200000745))
            make_face()
        # OneSide extrude, distance=-0.9
        extrude(amount=-0.9, mode=Mode.ADD)

        # Sketch1 -> Extrude12 (Join)
        # Sketch on XZ construction plane
        # Sketch has 82 constraints, 11 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2080000186, perimeter: 2.1200000626
            with BuildLine():
                Line((4.6000000685, -3.9600000745), (3.8000000566, -3.9600000745))
                Line((4.6000000685, -3.7000000551), (4.6000000685, -3.9600000745))
                Line((3.8000000566, -3.7000000551), (4.6000000685, -3.7000000551))
                Line((3.8000000566, -3.9600000745), (3.8000000566, -3.7000000551))
            make_face()
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.ADD)

        # Sketch1 -> Extrude13 (Join)
        # Sketch on XZ construction plane
        # Sketch has 82 constraints, 11 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.6400000191, perimeter: 3.2000000477
            with BuildLine():
                Line((3.8000000566, -3.7000000551), (4.6000000685, -3.7000000551))
                Line((4.6000000685, -2.9000000432), (4.6000000685, -3.7000000551))
                Line((3.8000000566, -2.9000000432), (4.6000000685, -2.9000000432))
                Line((3.8000000566, -3.7000000551), (3.8000000566, -2.9000000432))
            make_face()
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.ADD)

        # Sketch1 -> Extrude14 (Join)
        # Sketch on XZ construction plane
        # Sketch has 82 constraints, 11 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2080000186, perimeter: 2.1200000626
            with BuildLine():
                Line((3.8000000566, -3.7000000551), (3.8000000566, -2.9000000432))
                Line((3.8000000566, -2.9000000432), (3.5400000373, -2.9000000432))
                Line((3.5400000373, -3.7000000551), (3.5400000373, -2.9000000432))
                Line((3.5400000373, -3.7000000551), (3.8000000566, -3.7000000551))
            make_face()
        # OneSide extrude, distance=-1.1
        extrude(amount=-1.1, mode=Mode.ADD)

        # Sketch1 -> Extrude15 (Join)
        # Sketch on XZ construction plane
        # Sketch has 82 constraints, 11 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2080000031, perimeter: 2.1200000238
            with BuildLine():
                Line((3.5400000373, -3.7000000551), (3.5400000373, -2.9000000432))
                Line((3.5400000373, -2.9000000432), (3.2800000373, -2.9000000432))
                Line((3.2800000373, -2.9000000432), (3.2800000373, -3.7000000551))
                Line((3.2800000373, -3.7000000551), (3.5400000373, -3.7000000551))
            make_face()
        # OneSide extrude, distance=-1.2
        extrude(amount=-1.2, mode=Mode.ADD)

        # Sketch1 -> Extrude16 (Join)
        # Sketch on XZ construction plane
        # Sketch has 82 constraints, 11 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2080000031, perimeter: 2.1200000238
            with BuildLine():
                Line((3.2800000373, -2.9000000432), (3.2800000373, -3.7000000551))
                Line((3.2800000373, -2.9000000432), (3.0200000373, -2.9000000432))
                Line((3.0200000373, -2.9000000432), (3.0200000373, -3.7000000551))
                Line((3.0200000373, -3.7000000551), (3.2800000373, -3.7000000551))
            make_face()
        # OneSide extrude, distance=-1.3
        extrude(amount=-1.3, mode=Mode.ADD)

        # Sketch1 -> Extrude17 (Join)
        # Sketch on XZ construction plane
        # Sketch has 82 constraints, 11 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2080000031, perimeter: 2.1200000238
            with BuildLine():
                Line((3.0200000373, -2.9000000432), (3.0200000373, -3.7000000551))
                Line((3.0200000373, -2.9000000432), (2.7600000373, -2.9000000432))
                Line((2.7600000373, -2.9000000432), (2.7600000373, -3.7000000551))
                Line((2.7600000373, -3.7000000551), (3.0200000373, -3.7000000551))
            make_face()
        # OneSide extrude, distance=-1.4
        extrude(amount=-1.4, mode=Mode.ADD)

        # Sketch1 -> Extrude18 (Join)
        # Sketch on XZ construction plane
        # Sketch has 82 constraints, 11 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2080000031, perimeter: 2.1200000238
            with BuildLine():
                Line((2.7600000373, -2.9000000432), (2.7600000373, -3.7000000551))
                Line((2.7600000373, -2.9000000432), (2.5000000373, -2.9000000432))
                Line((2.5000000373, -2.9000000432), (2.5000000373, -3.7000000551))
                Line((2.5000000373, -3.7000000551), (2.7600000373, -3.7000000551))
            make_face()
        # OneSide extrude, distance=-1.5
        extrude(amount=-1.5, mode=Mode.ADD)
    return part.part


# Description: This is a rectangular tube frame or ladder-like structural component with four nested rectangular openings of graduating sizes, featuring a stepped/tapered profile that decreases in size from bottom to top.
def model_147435_426b700e_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # anchor face 1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 22 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.85, perimeter: 4.4
            with BuildLine():
                Line((-2, 2), (-2, 0.3))
                Line((-2, 0.3), (-1.5, 0.3))
                Line((-1.5, 1.5), (-1.5, 0.3))
                Line((-1.5, 1.5), (-1.5, 2))
                Line((-1.5, 2), (-2, 2))
            make_face()
            # Profile area: 0.6, perimeter: 3.4
            with BuildLine():
                Line((-1.5, 1.5), (-1.5, 0.3))
                Line((-1.5, 0.3), (-1, 0.3))
                Line((-1, 1.0039453684), (-1, 0.3))
                Line((-1, 1.5), (-1, 1.0039453684))
                Line((-1, 1.5), (-1.5, 1.5))
            make_face()
            # Profile area: 0.1, perimeter: 1.4
            with BuildLine():
                Line((-0.5, 0.5), (-0.5, 0.3))
                Line((-0.5, 0.3), (0, 0.3))
                Line((0, 0.3), (0, 0.5))
                Line((0, 0.5), (-0.5, 0.5))
            make_face()
            # Profile area: 0.3519726842, perimeter: 2.4078907367
            with BuildLine():
                Line((-1, 1.0039453684), (-1, 0.3))
                Line((-1, 0.3), (-0.5, 0.3))
                Line((-0.5, 0.5), (-0.5, 0.3))
                Line((-0.5, 1.0039453684), (-0.5, 0.5))
                Line((-0.5, 1.0039453684), (-1, 1.0039453684))
            make_face()
            # Profile area: 1.1, perimeter: 5.4
            with BuildLine():
                Line((-2, 2), (-2, 2.5))
                Line((-2, 2.5), (-2.5, 2.5))
                Line((-2.5, 2.5), (-2.5, 0.3))
                Line((-2.5, 0.3), (-2, 0.3))
                Line((-2, 2), (-2, 0.3))
            make_face()
            # Profile area: 0.75, perimeter: 5.6
            with BuildLine():
                Line((-0.5, 0.3), (0, 0.3))
                Line((-1, 0.3), (-0.5, 0.3))
                Line((-1.5, 0.3), (-1, 0.3))
                Line((-2, 0.3), (-1.5, 0.3))
                Line((-2.5, 0.3), (-2, 0.3))
                Line((-2.5, 0), (-2.5, 0.3))
                Line((0, 0), (-2.5, 0))
                Line((0, 0.3), (0, 0))
            make_face()
        # OneSide extrude, distance=0.4
        extrude(amount=0.4)

        # bridge begining -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 21 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.4, 0), x_dir=(0, 0, 1), z_dir=(0, 1, 0))):
            # Profile area: 0.1103860166, perimeter: 1.4415440664
            with BuildLine():
                Line((0.4707720332, 0), (0.4707720332, 0.5))
                Line((0.4707720332, 0.5), (0.25, 0.5))
                Line((0.25, 0.5), (0.25, 0))
                Line((0.25, 0), (0.4707720332, 0))
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2, mode=Mode.ADD)

        # bridge begining -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 21 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.4, 0), x_dir=(0, 0, 1), z_dir=(0, 1, 0))):
            # Profile area: 0.1259863421, perimeter: 1.5039453684
            with BuildLine():
                Line((1.0039453684, 1), (0.7519726842, 1))
                Line((0.7519726842, 1), (0.7519726842, 0.5))
                Line((0.7519726842, 0.5), (1.0039453684, 0.5))
                Line((1.0039453684, 0.5), (1.0039453684, 1))
            make_face()
        # OneSide extrude, distance=3
        extrude(amount=3, mode=Mode.ADD)

        # bridge begining -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 21 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.4, 0), x_dir=(0, 0, 1), z_dir=(0, 1, 0))):
            # Profile area: 0.1240136579, perimeter: 1.4960546316
            with BuildLine():
                Line((1.5, 1.5), (1.2519726842, 1.5))
                Line((1.2519726842, 1.5), (1.2519726842, 1))
                Line((1.2519726842, 1), (1.5, 1))
                Line((1.5, 1), (1.5, 1.5))
            make_face()
        # OneSide extrude, distance=4
        extrude(amount=4, mode=Mode.ADD)

        # bridge begining -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 21 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.4, 0), x_dir=(0, 0, 1), z_dir=(0, 1, 0))):
            # Profile area: 0.125, perimeter: 1.5
            with BuildLine():
                Line((2, 1.5), (2, 2))
                Line((2, 2), (1.75, 2))
                Line((1.75, 2), (1.75, 1.5))
                Line((1.75, 1.5), (2, 1.5))
            make_face()
        # OneSide extrude, distance=5
        extrude(amount=5, mode=Mode.ADD)

        # bridge begining -> Extrude6 (Join)
        # Sketch on BRepFace
        # Sketch has 21 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.4, 0), x_dir=(0, 0, 1), z_dir=(0, 1, 0))):
            # Profile area: 0.125, perimeter: 1.5
            with BuildLine():
                Line((2.25, 2.5), (2.25, 2))
                Line((2.25, 2), (2.5, 2))
                Line((2.5, 2), (2.5, 2.5))
                Line((2.5, 2.5), (2.25, 2.5))
            make_face()
        # OneSide extrude, distance=6
        extrude(amount=6, mode=Mode.ADD)

        # E anchor -> Extrude7 (Join)
        # Sketch on BRepFace
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 6.4, 0), x_dir=(0, 0, 1), z_dir=(0, 1, 0))):
            # Profile area: 0.125, perimeter: 1.5
            with BuildLine():
                Line((2.5, 2), (2.5, 2.5))
                Line((2.5, 2.5), (2.25, 2.5))
                Line((2.25, 2.5), (2.25, 2))
                Line((2.25, 2), (2.5, 2))
            make_face()
            # Profile area: 1.125, perimeter: 5.5
            with BuildLine():
                Line((2.25, 2.5), (2.25, 2))
                Line((2.25, 2.5), (0, 2.5))
                Line((0, 2.5), (0, 2))
                Line((0, 2), (2.25, 2))
            make_face()
        # OneSide extrude, distance=0.25
        extrude(amount=0.25, mode=Mode.ADD)

        # D anchor -> Extrude8 (Join)
        # Sketch on BRepFace
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 5.4, 0), x_dir=(0, 0, 1), z_dir=(0, 1, 0))):
            # Profile area: 0.875, perimeter: 4.5
            with BuildLine():
                Line((1.75, 2), (1.75, 1.5))
                Line((1.75, 2), (0, 2))
                Line((0, 2), (0, 1.5))
                Line((0, 1.5), (1.75, 1.5))
            make_face()
            # Profile area: 0.125, perimeter: 1.5
            with BuildLine():
                Line((2, 1.5), (2, 2))
                Line((2, 2), (1.75, 2))
                Line((1.75, 2), (1.75, 1.5))
                Line((1.75, 1.5), (2, 1.5))
            make_face()
        # OneSide extrude, distance=0.25
        extrude(amount=0.25, mode=Mode.ADD)

        # C anchor -> Extrude9 (Join)
        # Sketch on BRepFace
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 4.4, 0), x_dir=(0, 0, 1), z_dir=(0, 1, 0))):
            # Profile area: 0.6259863421, perimeter: 3.5039453684
            with BuildLine():
                Line((1.2519726842, 1.5), (1.2519726842, 1))
                Line((1.2519726842, 1.5), (0, 1.5))
                Line((0, 1.5), (0, 1))
                Line((0, 1), (1.2519726842, 1))
            make_face()
            # Profile area: 0.1240136579, perimeter: 1.4960546316
            with BuildLine():
                Line((1.5, 1), (1.5, 1.5))
                Line((1.5, 1.5), (1.2519726842, 1.5))
                Line((1.2519726842, 1.5), (1.2519726842, 1))
                Line((1.2519726842, 1), (1.5, 1))
            make_face()
        # OneSide extrude, distance=0.25
        extrude(amount=0.25, mode=Mode.ADD)

        # B anchor -> Extrude10 (Join)
        # Sketch on BRepFace
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 3.4, 0), x_dir=(0, 0, 1), z_dir=(0, 1, 0))):
            # Profile area: 0.3759863421, perimeter: 2.5039453684
            with BuildLine():
                Line((0.7519726842, 1), (0.7519726842, 0.5))
                Line((0.7519726842, 1), (0, 1))
                Line((0, 1), (0, 0.5))
                Line((0, 0.5), (0.7519726842, 0.5))
            make_face()
            # Profile area: 0.1259863421, perimeter: 1.5039453684
            with BuildLine():
                Line((1.0039453684, 0.5), (1.0039453684, 1))
                Line((1.0039453684, 1), (0.7519726842, 1))
                Line((0.7519726842, 1), (0.7519726842, 0.5))
                Line((0.7519726842, 0.5), (1.0039453684, 0.5))
            make_face()
        # OneSide extrude, distance=0.25
        extrude(amount=0.25, mode=Mode.ADD)

        # A anchor -> Extrude11 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2.4, 0.4707720332), x_dir=(0, 0, 1), z_dir=(0, 1, 0))):
            # Profile area: 0.1103860166, perimeter: 1.4415440664
            with BuildLine():
                Line((0, 0), (0, 0.5))
                Line((0, 0.5), (-0.2207720332, 0.5))
                Line((-0.2207720332, 0.5), (-0.2207720332, 0))
                Line((-0.2207720332, 0), (0, 0))
            make_face()
            # Profile area: 0.125, perimeter: 1.5
            with BuildLine():
                Line((-0.2207720332, 0.5), (-0.2207720332, 0))
                Line((-0.2207720332, 0.5), (-0.4707720332, 0.5))
                Line((-0.4707720332, 0.5), (-0.4707720332, 0))
                Line((-0.4707720332, 0), (-0.2207720332, 0))
            make_face()
        # OneSide extrude, distance=0.25
        extrude(amount=0.25, mode=Mode.ADD)

        # base -> Extrude13 (Join)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 2.625, perimeter: 10.44427191
            with BuildLine():
                Line((-2, 6.65), (-2.5, 6.65))
                Line((-2.5, 6.65), (-2.5, 6.4))
                Line((-2.5, 6.4), (-0.5, 2.4))
                Line((-0.5, 2.4), (0, 2.4))
                Line((0, 2.4), (0, 2.65))
                Line((-2, 6.65), (0, 2.65))
            make_face()
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2, mode=Mode.ADD)
    return part.part


# Description: This is a torus-shaped elastomeric sealing ring with a circular cross-section, commonly used as a gasket or seal in mechanical assemblies.
def model_148133_3050ab1d_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 3 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 92.4884877217, perimeter: 115.6106096521
            with BuildLine():
                CenterArc((0, 0), 10, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 8.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)
    return part.part


# Description: This is a structural skylight or roof panel frame with a parallelogram/trapezoidal shape, featuring internal diagonal cross-bracing and triangular support ribs that create multiple compartments for glass or panel inserts.
def model_21337_062b39fa_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.55575, perimeter: 4.1893714768
            with BuildLine():
                Line((0.855, -0.325), (-0.855, -0.325))
                Line((0.855, 0.325), (0.855, -0.325))
                Line((-0.855, -0.325), (0.855, 0.325))
            make_face()
            # Profile area: 0.55575, perimeter: 4.1893714768
            with BuildLine():
                Line((-0.855, -0.325), (0.855, 0.325))
                Line((-0.855, 0.325), (0.855, 0.325))
                Line((-0.855, -0.325), (-0.855, 0.325))
            make_face()
        # OneSide extrude, distance=0.02
        extrude(amount=0.02)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.0050265482, perimeter: 0.2513274123
            with Locations((-0.7500000112, 0.2500000037)):
                Circle(0.04)
            # Profile area: 0.0050265482, perimeter: 0.2513274123
            with Locations((-0.7500000112, -0.2500000037)):
                Circle(0.04)
            # Profile area: 0.0050265482, perimeter: 0.2513274123
            with Locations((0.7500000112, 0.2500000037)):
                Circle(0.04)
            # Profile area: 0.0050265482, perimeter: 0.2513274123
            with Locations((0.7500000112, -0.2500000037)):
                Circle(0.04)
            # Profile area: 0.0050265482, perimeter: 0.2513274123
            Circle(0.04)
        # OneSide extrude, distance=0.012
        extrude(amount=0.012, mode=Mode.ADD)

        # Sketch4 -> Extrude3 (NewBody)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -0.012, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.0044178647, perimeter: 0.235619449
            Circle(0.0375)
        # OneSide extrude, distance=0.01
        extrude(amount=0.01)

        # Sketch10 -> Extrude9 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.02, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0005815084, perimeter: 0.0893771322
            with BuildLine():
                CenterArc((-0.64, 0.317), 0.015, 147.7690473645, 244.461905271)
                Line((-0.6273114225, 0.325), (-0.6526885775, 0.325))
            make_face()
        # OneSide extrude, distance=-0.02
        extrude(amount=-0.02, mode=Mode.SUBTRACT)

        # Sketch12 -> Extrude10 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.02, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0001253499, perimeter: 0.0556249575
            with BuildLine():
                Line((-0.1996228449, 0.325), (-0.225, 0.325))
                CenterArc((-0.2123114225, 0.317), 0.015, 32.2309526355, 115.538094729)
            make_face()
            # Profile area: 0.0005815084, perimeter: 0.0893771322
            with BuildLine():
                CenterArc((-0.2123114225, 0.317), 0.015, 147.7690473645, 244.461905271)
                Line((-0.1996228449, 0.325), (-0.225, 0.325))
            make_face()
        # OneSide extrude, distance=-0.02
        extrude(amount=-0.02, mode=Mode.SUBTRACT)

        # Sketch13 -> Extrude11 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.02, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0005815084, perimeter: 0.0893771322
            with BuildLine():
                Line((-0.855, -0.0873114225), (-0.855, -0.1126885775))
                CenterArc((-0.847, -0.1), 0.015, -122.2309526355, 244.461905271)
            make_face()
        # OneSide extrude, distance=-0.02
        extrude(amount=-0.02, mode=Mode.SUBTRACT)

        # Sketch11 -> Extrude12 (Join)
        # Sketch on BRepFace
        # Sketch has 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.02, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0005815084, perimeter: 0.0893771322
            with BuildLine():
                CenterArc((-0.863, 0.1), 0.015, 57.7690473645, 244.461905271)
                Line((-0.855, 0.1126885775), (-0.855, 0.0873114225))
            make_face()
        # OneSide extrude, distance=-0.02
        extrude(amount=-0.02, mode=Mode.ADD)

        # Sketch14 -> Extrude13 (Join)
        # Sketch on BRepFace
        # Sketch has 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.02, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0005815084, perimeter: 0.0893771322
            with BuildLine():
                CenterArc((0.863, -0.1), 0.015, -122.2309526355, 244.461905271)
                Line((0.855, -0.1126885775), (0.855, -0.0873114225))
            make_face()
        # OneSide extrude, distance=-0.02
        extrude(amount=-0.02, mode=Mode.ADD)
    return part.part


# Description: This is a dual-pocket mounting bracket or clamp with a horizontal cylindrical rod passing through two symmetrical box-shaped flanges, featuring rectangular cutouts or pockets on each side.
def model_21734_7cf58bd0_0012():
    """Model: CRANKSHAFT v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 6.9067348675, perimeter: 10.5611437633
            with BuildLine():
                CenterArc((0, 0), 1.9, -120, 60)
                Line((0.95, 1.6454482672), (0.95, -1.6454482672))
                CenterArc((0, 0), 1.9, 60, 60)
                Line((-0.95, -1.6454482672), (-0.95, 1.6454482672))
            make_face()
        # OneSide extrude, distance=0.635
        extrude(amount=0.635)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.635, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.1309733553, perimeter: 3.7699111843
            with Locations((0, 0.94)):
                Circle(0.6)
        # OneSide extrude, distance=2.159
        extrude(amount=2.159, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 1.1309733553, perimeter: 3.7699111843
            with Locations((0, -0.94)):
                Circle(0.6)
        # OneSide extrude, distance=0.83
        extrude(amount=0.83, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-0.83, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 5.7757615122, perimeter: 14.3310549476
            with BuildLine():
                CenterArc((0, 0), 1.9, -120, 60)
                Line((0.95, -1.6454482672), (0.95, 1.6454482672))
                CenterArc((0, 0), 1.9, 60, 60)
                Line((-0.95, -1.6454482672), (-0.95, 1.6454482672))
            make_face()
            with BuildLine():
                CenterArc((0, -0.94), 0.6, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 1.1309733553, perimeter: 3.7699111843
            with Locations((0, -0.94)):
                Circle(0.6)
        # OneSide extrude, distance=0.635
        extrude(amount=0.635, mode=Mode.ADD)

        # Sketch5 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-1.465, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 1.1309733553, perimeter: 3.7699111843
            with Locations((0, 0.94)):
                Circle(0.6)
        # OneSide extrude, distance=4.7
        extrude(amount=4.7, mode=Mode.ADD)

        # Sketch6 -> Extrude6 (Join)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-6.165, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 5.7757615122, perimeter: 14.3310549476
            with BuildLine():
                CenterArc((0, 0), 1.9, 60, 60)
                Line((-0.95, 1.6454482672), (-0.95, -1.6454482672))
                CenterArc((0, 0), 1.9, -120, 60)
                Line((0.95, -1.6454482672), (0.95, 1.6454482672))
            make_face()
            with BuildLine():
                CenterArc((0, 0.94), 0.6, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 1.1309733553, perimeter: 3.7699111843
            with Locations((0, 0.94)):
                Circle(0.6)
        # OneSide extrude, distance=0.635
        extrude(amount=0.635, mode=Mode.ADD)

        # Sketch7 -> Extrude7 (Join)
        # Sketch on BRepFace
        # Sketch has 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-6.8, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 1.1309733553, perimeter: 3.7699111843
            with Locations((0, -0.94)):
                Circle(0.6)
        # OneSide extrude, distance=0.83
        extrude(amount=0.83, mode=Mode.ADD)

        # Sketch8 -> Extrude8 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-7.63, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 5.7757615122, perimeter: 14.3310549476
            with BuildLine():
                CenterArc((0, 0), 1.9, 60, 60)
                Line((-0.95, 1.6454482672), (-0.95, -1.6454482672))
                CenterArc((0, 0), 1.9, -120, 60)
                Line((0.95, -1.6454482672), (0.95, 1.6454482672))
            make_face()
            with BuildLine():
                CenterArc((0, -0.94), 0.6, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 1.1309733553, perimeter: 3.7699111843
            with Locations((0, -0.94)):
                Circle(0.6)
        # OneSide extrude, distance=0.635
        extrude(amount=0.635, mode=Mode.ADD)

        # Sketch9 -> Extrude9 (Join)
        # Sketch on BRepFace
        # Sketch has 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-8.265, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 1.1309733553, perimeter: 3.7699111843
            with Locations((0, 0.94)):
                Circle(0.6)
        # OneSide extrude, distance=2.464
        extrude(amount=2.464, mode=Mode.ADD)
    return part.part


# Description: This is a long, narrow rectangular channel or duct with an open top, featuring parallel side walls and a closed bottom, with a slight taper toward one end and what appears to be internal ribbing or stiffening features along its length.
def model_21852_6cf9a734_0002():
    """Model: Standard v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 78, perimeter: 38
            with BuildLine():
                Line((3, -6.5), (3, 6.5))
                Line((3, 6.5), (-3, 6.5))
                Line((-3, 6.5), (-3, -6.5))
                Line((-3, -6.5), (3, -6.5))
            make_face()
        # OneSide extrude, distance=1.2
        extrude(amount=1.2)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1.2), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 2.0106192983, perimeter: 5.0265482457
            with Locations((0, 2.5)):
                Circle(0.8)
        # OneSide extrude, distance=-3.5
        extrude(amount=-3.5, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1.2), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.1617529226, perimeter: 1.6329650009
            with BuildLine():
                CenterArc((1.9445436483, 4.4445436483), 0.325, 138.3876331056, 173.2247337889)
                CenterArc((0, 2.5), 2.75, 38.2247337889, 13.5505324223)
            make_face()
            # Profile area: 0.1700778014, perimeter: 1.7098279579
            with BuildLine():
                CenterArc((0, 2.5), 2.75, 38.2247337889, 13.5505324223)
                CenterArc((1.9445436483, 4.4445436483), 0.325, -48.3876331056, 186.7752662111)
            make_face()
            # Profile area: 0.1700778014, perimeter: 1.7098279579
            with BuildLine():
                CenterArc((0, 2.5), 2.75, 128.2247337889, 13.5505324223)
                CenterArc((-1.9445436483, 4.4445436483), 0.325, 41.6123668944, 186.7752662111)
            make_face()
            # Profile area: 0.1617529226, perimeter: 1.6329650009
            with BuildLine():
                CenterArc((-1.9445436483, 4.4445436483), 0.325, -131.6123668944, 173.2247337889)
                CenterArc((0, 2.5), 2.75, 128.2247337889, 13.5505324223)
            make_face()
            # Profile area: 0.1617529226, perimeter: 1.6329650009
            with BuildLine():
                CenterArc((0, 2.5), 2.75, -141.7752662111, 13.5505324223)
                CenterArc((-1.9445436483, 0.5554563517), 0.325, -41.6123668944, 173.2247337889)
            make_face()
            # Profile area: 0.1700778014, perimeter: 1.7098279579
            with BuildLine():
                CenterArc((-1.9445436483, 0.5554563517), 0.325, 131.6123668944, 186.7752662111)
                CenterArc((0, 2.5), 2.75, -141.7752662111, 13.5505324223)
            make_face()
            # Profile area: 0.1617529226, perimeter: 1.6329650009
            with BuildLine():
                CenterArc((1.9445436483, 0.5554563517), 0.325, 48.3876331056, 173.2247337889)
                CenterArc((0, 2.5), 2.75, -51.7752662111, 13.5505324223)
            make_face()
            # Profile area: 0.1700778014, perimeter: 1.7098279579
            with BuildLine():
                CenterArc((0, 2.5), 2.75, -51.7752662111, 13.5505324223)
                CenterArc((1.9445436483, 0.5554563517), 0.325, -138.3876331056, 186.7752662111)
            make_face()
        # OneSide extrude, distance=-7.5
        extrude(amount=-7.5, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(3, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((-0.6, 3)):
                Circle(0.15)
            # Profile area: 0.0353429174, perimeter: 0.771238898
            with BuildLine():
                Line((-0.6, 1.85), (-0.6, 2.15))
                CenterArc((-0.6, 2), 0.15, -90, 180)
            make_face()
            # Profile area: 0.0353429174, perimeter: 0.771238898
            with BuildLine():
                CenterArc((-0.6, 2), 0.15, 90, 180)
                Line((-0.6, 1.85), (-0.6, 2.15))
            make_face()
        # OneSide extrude, distance=-1.2
        extrude(amount=-1.2, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(3, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            with Locations((-0.6, 3.7)):
                Circle(0.3)
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            with Locations((-0.6, 1.3)):
                Circle(0.3)
        # OneSide extrude, distance=-1.5
        extrude(amount=-1.5, mode=Mode.SUBTRACT)

        # Sketch8 -> Extrude7 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -6.5, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.331830724, perimeter: 2.0420352248
            with Locations((0, 0.6)):
                Circle(0.325)
        # OneSide extrude, distance=-7.85
        extrude(amount=-7.85, mode=Mode.SUBTRACT)

        # Sketch9 -> Extrude8 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -6.5, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            with Locations((2, 0.6)):
                Circle(0.3)
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((1, 0.6)):
                Circle(0.25)
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((-1, 0.6)):
                Circle(0.25)
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            with Locations((-2, 0.6)):
                Circle(0.3)
        # OneSide extrude, distance=-1.5
        extrude(amount=-1.5, mode=Mode.SUBTRACT)

        # Sketch11 -> Extrude10 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.9503317777, perimeter: 3.4557519189
            with Locations((0, 1)):
                Circle(0.55)
        # OneSide extrude, distance=-0.15
        extrude(amount=-0.15, mode=Mode.SUBTRACT)

        # Sketch12 -> Extrude11 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.331830724, perimeter: 2.0420352248
            with Locations((0, 1)):
                Circle(0.325)
        # OneSide extrude, distance=-0.6
        extrude(amount=-0.6, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a truss or frame bracket with a elongated parallelogram shape, featuring multiple triangular cutouts and slots for lightweighting, and mounting holes along its edges for structural assembly.
def model_22025_b77024b9_0014():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 225, perimeter: 60
            with BuildLine():
                Line((0, 15), (0, 0))
                Line((0, 0), (15, 0))
                Line((15, 0), (15, 15))
                Line((15, 15), (0, 15))
            make_face()
        # OneSide extrude, distance=2.5
        extrude(amount=2.5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 28.2743338823, perimeter: 18.8495559215
            with Locations((-7.5, -7.5)):
                Circle(3)
        # OneSide extrude, distance=0.9
        extrude(amount=0.9, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 6.157521601, perimeter: 8.7964594301
            with Locations((-1.7, -1.7)):
                Circle(1.4)
        # OneSide extrude, distance=-1.7
        extrude(amount=-1.7, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.8, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.2698006922, perimeter: 5.3407075111
            with Locations((-1.7, -1.7)):
                Circle(0.85)
        # OneSide extrude, distance=-0.8
        extrude(amount=-0.8, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 6.157521601, perimeter: 8.7964594301
            with Locations((-13.3, -1.7)):
                Circle(1.4)
            # Profile area: 6.157521601, perimeter: 8.7964594301
            with Locations((-13.3, -13.3)):
                Circle(1.4)
            # Profile area: 6.157521601, perimeter: 8.7964594301
            with Locations((-1.7, -13.3)):
                Circle(1.4)
        # OneSide extrude, distance=-1.7
        extrude(amount=-1.7, mode=Mode.SUBTRACT)

        # Sketch8 -> Extrude6 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.8, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.2698006922, perimeter: 5.3407075111
            with Locations((-13.3, -1.7)):
                Circle(0.85)

        # Sketch7 -> Extrude6 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.8, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.2698006922, perimeter: 5.3407075111
            with Locations((-13.3, -13.3)):
                Circle(0.85)

        # Sketch6 -> Extrude6 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.8, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.2698006922, perimeter: 5.3407075111
            with Locations((-1.7, -13.3)):
                Circle(0.85)
        # OneSide extrude, distance=-0.8
        extrude(amount=-0.8, mode=Mode.SUBTRACT)

        # Sketch9 -> Extrude7 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 3.4, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.9087385212, perimeter: 7.853981634
            with Locations((-7.5, -7.5)):
                Circle(1.25)
        # OneSide extrude, distance=-3.4
        extrude(amount=-3.4, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a ball joint or spherical connector featuring a cylindrical shaft connected to a spherical head, commonly used in mechanical linkages, suspension systems, or articulated assemblies.
def model_22543_684108ff_0006():
    """Model: 7.1_Crankshaft v1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 3.5377985381, perimeter: 8.0267692299
            with BuildLine():
                CenterArc((0, 0), 1.0795, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0.711), 0.198, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.61
        extrude(amount=0.61)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.3166921744, perimeter: 1.994911335
            Circle(0.3175)
        # OneSide extrude, distance=0.076
        extrude(amount=0.076, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -0.076), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.1784511021, perimeter: 4.489335902
            with BuildLine():
                CenterArc((0, 0), 0.397, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.3175, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.3166921744, perimeter: 1.994911335
            Circle(0.3175)
        # OneSide extrude, distance=0.825
        extrude(amount=0.825, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -0.901), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.3750127005, perimeter: 2.1708405236
            Circle(0.3455)
        # OneSide extrude, distance=0.635
        extrude(amount=0.635, mode=Mode.ADD)

        # Sketch5 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -1.536), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.1201305761, perimeter: 4.6652650906
            with BuildLine():
                CenterArc((0, 0), 0.397, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.3455, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.3750127005, perimeter: 2.1708405236
            Circle(0.3455)
        # OneSide extrude, distance=1.436
        extrude(amount=1.436, mode=Mode.ADD)

        # Sketch6 -> Extrude6 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -2.972), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.3166921744, perimeter: 1.994911335
            Circle(0.3175)
        # OneSide extrude, distance=0.935
        extrude(amount=0.935, mode=Mode.ADD)

        # Sketch7 -> Extrude7 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.9207864436, perimeter: 6.0516046253
            with BuildLine():
                CenterArc((0, 0), 0.635, 105.6388622317, 328.7222755366)
                CenterArc((0, 0.711), 0.198, -149.8302003665, 119.660400733)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.3175, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.025
        extrude(amount=0.025, mode=Mode.ADD)

        # Sketch8 -> Extrude8 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0814838107, perimeter: 1.0119069937
            with Locations((0, 1.2435)):
                Circle(0.16105)
        # OneSide extrude, distance=-1.8
        extrude(amount=-1.8, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a motorized 3-axis gimbal stabilizer featuring a cylindrical handle base with articulated clamp arms extending upward that support a camera mounting plate, designed to stabilize video footage through powered stabilization of pan, tilt, and roll movements.
def model_23054_311abee4_0001():
    """Model: P3-Camshaft"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 45 constraints, 9 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0536504592, perimeter: 1.7853981634
            with BuildLine():
                Line((1.5, 1.5), (1.5, 2))
                Line((2, 1.5), (1.5, 1.5))
                CenterArc((2, 2), 0.5, 180, 90)
            make_face()
            # Profile area: 5.9866129921, perimeter: 16.6085184059
            with BuildLine():
                Line((0, -1.5), (2.4494897428, -1.5))
                CenterArc((0, 0), 1.5, 180, 90)
                Line((-1.5, 2.4494897428), (-1.5, 0))
                CenterArc((-2.5, 2.4494897428), 1, -44.4153085972, 44.4153085972)
                CenterArc((0, 0), 2.5, 135.5846914028, 178.8306171944)
                CenterArc((2.4494897428, -2.5), 1, 90, 44.4153085972)
            make_face()
            # Profile area: 12.75, perimeter: 21.780972451
            with BuildLine():
                Line((-1.5, 2.4494897428), (-1.5, 0))
                CenterArc((0, 0), 1.5, 90, 90)
                Line((1.5, 1.5), (0, 1.5))
                Line((1.5, 1.5), (1.5, 2))
                Line((1.5, 2), (1.5, 5))
                CenterArc((0, 5), 1.5, 0, 180)
                Line((-1.5, 5), (-1.5, 2.4494897428))
            make_face()
            with BuildLine():
                CenterArc((0, 5), 0.75, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 1.7671458676, perimeter: 4.7123889804
            with Locations((0, 5)):
                Circle(0.75)
            # Profile area: 3.0275441818, perimeter: 17.6084058392
            with BuildLine():
                Line((1.5, 1.5), (0, 1.5))
                CenterArc((0, 0), 1.5, 90, 90)
                CenterArc((0, 0), 1.5, 180, 90)
                CenterArc((0, 0), 1.5, -90, 90)
                Line((1.5, 0), (1.5, 1.5))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 1.3823007676, perimeter: 13.8230076758
            with BuildLine():
                CenterArc((0, 0), 1.2, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 1.3744467859, perimeter: 10.9955742876
            with BuildLine():
                CenterArc((0, 0), 1, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.75, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 1.7671458676, perimeter: 4.7123889804
            Circle(0.75)
            # Profile area: 12.75, perimeter: 21.780972451
            with BuildLine():
                CenterArc((5, 0), 1.5, -90, 180)
                Line((5, 1.5), (2, 1.5))
                Line((2, 1.5), (1.5, 1.5))
                Line((1.5, 0), (1.5, 1.5))
                CenterArc((0, 0), 1.5, -90, 90)
                Line((0, -1.5), (2.4494897428, -1.5))
                Line((2.4494897428, -1.5), (5, -1.5))
            make_face()
            with BuildLine():
                CenterArc((5, 0), 0.75, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 1.7671458676, perimeter: 4.7123889804
            with Locations((5, 0)):
                Circle(0.75)
        # Symmetric extrude, each_side=0.4
        extrude(amount=0.4, both=True)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.4, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.7671458676, perimeter: 4.7123889804
            with Locations((0, -5)):
                Circle(0.75)
        # OneSide extrude, distance=1.7
        extrude(amount=1.7, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 2.1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 18.5342917353, perimeter: 28.8495559215
            with BuildLine():
                Line((1.5, -5), (1.5, 0))
                CenterArc((0, 0), 1.5, 0, 180)
                Line((-1.5, 0), (-1.5, -5))
                CenterArc((0, -5), 1.5, 180, 180)
            make_face()
            with BuildLine():
                CenterArc((0, -5), 0.75, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0, 0), 0.75, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 1.7671458676, perimeter: 4.7123889804
            with Locations((0, -5)):
                Circle(0.75)
            # Profile area: 1.7671458676, perimeter: 4.7123889804
            Circle(0.75)
        # OneSide extrude, distance=0.8
        extrude(amount=0.8, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2.9, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.5238934212, perimeter: 7.5398223686
            Circle(1.2)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1, mode=Mode.ADD)

        # Sketch5 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 3, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            Circle(1)
        # OneSide extrude, distance=0.9
        extrude(amount=0.9, mode=Mode.ADD)

        # Sketch6 -> Extrude6 (Join)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -0.4, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 1.7671458676, perimeter: 4.7123889804
            with Locations((5, 0)):
                Circle(0.75)
        # OneSide extrude, distance=1.7
        extrude(amount=1.7, mode=Mode.ADD)

        # Sketch7 -> Extrude7 (Join)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, -2.1, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 20.3014376029, perimeter: 24.1371669412
            with BuildLine():
                CenterArc((0, 0), 1.5, 90, 180)
                Line((5, -1.5), (0, -1.5))
                CenterArc((5, 0), 1.5, -90, 180)
                Line((0, 1.5), (5, 1.5))
            make_face()
            with BuildLine():
                CenterArc((5, 0), 0.75, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 1.7671458676, perimeter: 4.7123889804
            with Locations((5, 0)):
                Circle(0.75)
        # OneSide extrude, distance=0.8
        extrude(amount=0.8, mode=Mode.ADD)

        # Sketch8 -> Extrude8 (Join)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -2.9, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 4.5238934212, perimeter: 7.5398223686
            Circle(1.2)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1, mode=Mode.ADD)

        # Sketch9 -> Extrude9 (Join)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -3, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            Circle(1)
        # OneSide extrude, distance=5.9
        extrude(amount=5.9, mode=Mode.ADD)

        # Sketch10 -> Extrude10 (Cut)
        # Sketch on BRepFace
        # Sketch has 8 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -8.9, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.0600000009, perimeter: 1.000000006
            with BuildLine():
                Line((0.15, 0.9000000134), (-0.15, 0.9000000134))
                Line((0.15, 1.1000000164), (0.15, 0.9000000134))
                Line((-0.15, 1.1000000164), (0.15, 1.1000000164))
                Line((-0.15, 0.9000000134), (-0.15, 1.1000000164))
            make_face()
        # OneSide extrude, distance=-3.5
        extrude(amount=-3.5, mode=Mode.SUBTRACT)
    return part.part


MODELS = {
    "model_100155_57ec5fc6_0000": {"func": model_100155_57ec5fc6_0000, "volume": 9.9657071861, "area": 59.8459789378},
    "model_100155_bf644f70_0000": {"func": model_100155_bf644f70_0000, "volume": 9.777878179, "area": 57.6815093727},
    "model_105907_e625e54b_0000": {"func": model_105907_e625e54b_0000, "volume": 75.9794183444, "area": 106.2134633244},
    "model_118628_c12b368f_0000": {"func": model_118628_c12b368f_0000, "volume": 229.3611849211, "area": 373.2274616198},
    "model_118699_c3e4046a_0000": {"func": model_118699_c3e4046a_0000, "volume": 6088.7428759054, "area": 2446.9678058937},
    "model_120292_9c3e9e6c_0000": {"func": model_120292_9c3e9e6c_0000, "volume": 14.1387955609, "area": 50.4876551061},
    "model_128645_d5cdd476_0002": {"func": model_128645_d5cdd476_0002, "volume": 440635935.011105597, "area": 11860810.6688171532},
    "model_130022_505982e4_0000": {"func": model_130022_505982e4_0000, "volume": 0.1985885476, "area": 2.6499112444},
    "model_130832_8f82565e_0000": {"func": model_130832_8f82565e_0000, "volume": 24.3295632592, "area": 154.1665000444},
    "model_130932_a060d2a3_0000": {"func": model_130932_a060d2a3_0000, "volume": 25.6524276632, "area": 99.1254659314},
    "model_130957_57bd641b_0000": {"func": model_130957_57bd641b_0000, "volume": 76.359531608, "area": 196.9161795087},
    "model_131626_3d395aec_0000": {"func": model_131626_3d395aec_0000, "volume": 1.8751341881, "area": 18.3439165839},
    "model_132212_4d7d45f6_0000": {"func": model_132212_4d7d45f6_0000, "volume": 229.0582488414, "area": 418.5376027108},
    "model_132453_391b7740_0000": {"func": model_132453_391b7740_0000, "volume": 19.8839924734, "area": 56.4314664959},
    "model_134381_b7f05dc3_0000": {"func": model_134381_b7f05dc3_0000, "volume": 8596.08, "area": 10903.36},
    "model_136126_5202c059_0000": {"func": model_136126_5202c059_0000, "volume": 19.8845591483, "area": 87.0805217979},
    "model_136127_140a874c_0000": {"func": model_136127_140a874c_0000, "volume": 80.3789999857, "area": 279.3100000286},
    "model_136474_c3d4bfa2_0000": {"func": model_136474_c3d4bfa2_0000, "volume": 200.7567260099, "area": 553.6451883362},
    "model_136561_426e584d_0000": {"func": model_136561_426e584d_0000, "volume": 1.6719359151, "area": 16.0885454246},
    "model_136600_cf00e137_0000": {"func": model_136600_cf00e137_0000, "volume": 36.5885330891, "area": 157.8287569298},
    "model_137053_59e609b3_0007": {"func": model_137053_59e609b3_0007, "volume": 20.3555853988, "area": 143.5528808187},
    "model_138267_3dbc9e31_0000": {"func": model_138267_3dbc9e31_0000, "volume": 4313.3647568627, "area": 2683.1458506914},
    "model_138657_5a4a4283_0000": {"func": model_138657_5a4a4283_0000, "volume": 4.7143914933, "area": 19.9143852707},
    "model_145894_f94b265c_0000": {"func": model_145894_f94b265c_0000, "volume": 61.314, "area": 116.798},
    "model_146291_6b0c8db3_0002": {"func": model_146291_6b0c8db3_0002, "volume": 3.4560002537, "area": 19.8400001853},
    "model_147435_426b700e_0000": {"func": model_147435_426b700e_0000, "volume": 5.30491444, "area": 57.2132465839},
    "model_148133_3050ab1d_0000": {"func": model_148133_3050ab1d_0000, "volume": 27.7465463165, "area": 219.660158339},
    "model_21337_062b39fa_0000": {"func": model_21337_062b39fa_0000, "volume": 0.0225641414, "area": 2.3463708339},
    "model_21734_7cf58bd0_0012": {"func": model_21734_7cf58bd0_0012, "volume": 29.9645869246, "area": 116.6982785042},
    "model_21852_6cf9a734_0002": {"func": model_21852_6cf9a734_0002, "volume": 84.3341115984, "area": 245.332236259},
    "model_22025_b77024b9_0014": {"func": model_22025_b77024b9_0014, "volume": 522.1226804197, "area": 692.5984434646},
    "model_22543_684108ff_0006": {"func": model_22543_684108ff_0006, "volume": 3.8315388313, "area": 21.9832351867},
    "model_23054_311abee4_0001": {"func": model_23054_311abee4_0001, "volume": 97.5853833742, "area": 282.9415846521},
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
