"""Batch 004 - passing/05_8to10ops
51 models bundled from Fusion360 Gallery reconstructions.
"""

from build123d import *
from build123d import Edge, BuildLine
from collections import Counter
from OCP.BRepBuilderAPI import BRepBuilderAPI_MakeEdge
from OCP.Geom import Geom_BSplineCurve
from OCP.TColStd import TColStd_Array1OfReal, TColStd_Array1OfInteger
from OCP.TColgp import TColgp_Array1OfPnt
from OCP.gp import gp_Pnt


def model_21822_7d3db422_0030():
    """Model: Screw 4"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            Circle(0.2)
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            Circle(0.2)
        # OneSide extrude, distance=0.4
        extrude(amount=0.4, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.4, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
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

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.8, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1315276082, perimeter: 1.35
            with BuildLine():
                Line((-0.1125, 0.1948557159), (-0.225, 0))
                Line((-0.225, 0), (-0.1125, -0.1948557159))
                Line((-0.1125, -0.1948557159), (0.1125, -0.1948557159))
                Line((0.1125, -0.1948557159), (0.225, 0))
                Line((0.225, 0), (0.1125, 0.1948557159))
                Line((0.1125, 0.1948557159), (-0.1125, 0.1948557159))
            make_face()
        # OneSide extrude, distance=-0.3
        extrude(amount=-0.3, mode=Mode.SUBTRACT)
    return part.part


def model_21822_7d3db422_0038():
    """Model: Pipe Connector Female"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            with Locations((-5.0000000745, -10.5000001565)):
                Circle(0.4)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.363370605, perimeter: 5.9773757896
            with BuildLine():
                Line((4.5000000671, 10.7886752954), (4.5000000671, 10.2113250176))
                Line((4.5000000671, 10.2113250176), (5.0000000745, 9.9226498787))
                Line((5.0000000745, 9.9226498787), (5.500000082, 10.2113250176))
                Line((5.500000082, 10.2113250176), (5.500000082, 10.7886752954))
                Line((5.500000082, 10.7886752954), (5.0000000745, 11.0773504343))
                Line((5.0000000745, 11.0773504343), (4.5000000671, 10.7886752954))
            make_face()
            with BuildLine():
                CenterArc((5.0000000745, 10.5000001565), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            with Locations((5.0000000745, 10.5000001565)):
                Circle(0.4)
        # OneSide extrude, distance=0.6
        extrude(amount=0.6, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 1.1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            with Locations((5.0000000745, 10.5000001565)):
                Circle(0.4)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.6, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((5.0000000745, 10.5000001565)):
                Circle(0.25)
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.096211275, perimeter: 1.0995574288
            with Locations((5.0000000745, 10.5000001565)):
                Circle(0.175)
        # OneSide extrude, distance=-1.2
        extrude(amount=-1.2, mode=Mode.SUBTRACT)
    return part.part


def model_21822_7d3db422_0044():
    """Model: Screw 3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1256637099, perimeter: 1.2566370802
            Circle(0.200000003)
        # OneSide extrude, distance=1.2
        extrude(amount=1.2)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0333794182, perimeter: 2.6703537743
            with BuildLine():
                CenterArc((0, 0), 0.225, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.200000003, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.1256637099, perimeter: 1.2566370802
            Circle(0.200000003)
        # OneSide extrude, distance=0.8
        extrude(amount=0.8, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.6263550353, perimeter: 4.5553093477
            with BuildLine():
                CenterArc((0, 0), 0.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.225, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.275
        extrude(amount=-0.275, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.233826866, perimeter: 1.8000000268
            with BuildLine():
                Line((-0.1500000022, 0.259807625), (-0.3000000045, 0))
                Line((-0.3000000045, 0), (-0.1500000022, -0.259807625))
                Line((-0.1500000022, -0.259807625), (0.1500000022, -0.259807625))
                Line((0.1500000022, -0.259807625), (0.3000000045, 0))
                Line((0.3000000045, 0), (0.1500000022, 0.259807625))
                Line((0.1500000022, 0.259807625), (-0.1500000022, 0.259807625))
            make_face()
        # OneSide extrude, distance=-0.1
        extrude(amount=-0.1, mode=Mode.SUBTRACT)
    return part.part


def model_21822_7d3db422_0046():
    """Model: Screw 1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            Circle(0.2)
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0333794219, perimeter: 2.6703537556
            with BuildLine():
                CenterArc((0, 0), 0.225, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            Circle(0.2)
        # OneSide extrude, distance=1.3
        extrude(amount=1.3, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2.3, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.3436116965, perimeter: 3.926990817
            with BuildLine():
                CenterArc((0, 0), 0.4, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.225, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.1590431281, perimeter: 1.4137166941
            Circle(0.225)
        # OneSide extrude, distance=0.4
        extrude(amount=0.4, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2.7, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.162379768, perimeter: 1.5000000224
            with BuildLine():
                Line((-0.2165063542, -0.1250000019), (0, -0.2500000037))
                Line((0, -0.2500000037), (0.2165063542, -0.1250000019))
                Line((0.2165063542, -0.1250000019), (0.2165063542, 0.1250000019))
                Line((0.2165063542, 0.1250000019), (0, 0.2500000037))
                Line((0, 0.2500000037), (-0.2165063542, 0.1250000019))
                Line((-0.2165063542, 0.1250000019), (-0.2165063542, -0.1250000019))
            make_face()
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2, mode=Mode.SUBTRACT)
    return part.part


def model_21852_6cf9a734_0010():
    """Model: Crosshead v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 9 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.7, perimeter: 6.2
            with BuildLine():
                Line((0, 1.4), (0, 0))
                Line((0, 0), (1, 0))
                Line((1, 0), (1, 0.2))
                Line((1, 0.2), (0.3, 0.2))
                Line((0.3, 0.2), (0.3, 1.2))
                Line((0.3, 1.2), (1, 1.2))
                Line((1, 1.2), (1, 1.4))
                Line((1, 1.4), (0, 1.4))
            make_face()
        # OneSide extrude, distance=-5
        extrude(amount=-5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on YZ construction plane
        # Sketch has 5 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.8, perimeter: 5.4
            with BuildLine():
                Line((1.5, 2.6), (1.5, 1.4))
                Line((1.5, 1.4), (3, 1.4))
                Line((3, 1.4), (3, 2.6))
                Line((3, 2.6), (1.5, 2.6))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 16 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.3, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0706858417, perimeter: 1.0712389512
            with BuildLine():
                Line((0.9, 0.3999999851), (0.9, 0.7))
                Line((0.5999999851, 0.7), (0.9, 0.7))
                CenterArc((0.9, 0.7), 0.3000000149, -179.9999999999, 89.9999999999)
            make_face()
            # Profile area: 0.4800000238, perimeter: 3.8000000298
            with BuildLine():
                Line((4.1, 0.7), (4.1, 0.3999999851))
                Line((2.5, 0.7), (4.1, 0.7))
                Line((2.5, 0.7), (2.5, 0.3999999851))
                Line((4.1, 0.3999999851), (2.5, 0.3999999851))
            make_face()
            # Profile area: 0.4800000238, perimeter: 3.8000000298
            with BuildLine():
                Line((2.5, 0.7), (2.5, 0.3999999851))
                Line((0.9, 0.7), (2.5, 0.7))
                Line((0.9, 0.3999999851), (0.9, 0.7))
                Line((2.5, 0.3999999851), (0.9, 0.3999999851))
            make_face()
            # Profile area: 0.0706858417, perimeter: 1.0712389512
            with BuildLine():
                Line((4.1, 0.7), (4.4000000149, 0.7))
                Line((4.1, 0.7), (4.1, 0.3999999851))
                CenterArc((4.1, 0.7), 0.3000000149, -90, 89.9999999999)
            make_face()
            # Profile area: 0.9600000477, perimeter: 7.0000000298
            with BuildLine():
                Line((0.9, 0.7), (0.9, 1.0000000149))
                Line((0.9, 0.7), (2.5, 0.7))
                Line((2.5, 0.7), (4.1, 0.7))
                Line((4.1, 1.0000000149), (4.1, 0.7))
                Line((0.9, 1.0000000149), (4.1, 1.0000000149))
            make_face()
            # Profile area: 0.0706858417, perimeter: 1.0712389512
            with BuildLine():
                CenterArc((4.1, 0.7), 0.3000000149, -0.0000000001, 90.0000000001)
                Line((4.1, 1.0000000149), (4.1, 0.7))
                Line((4.1, 0.7), (4.4000000149, 0.7))
            make_face()
            # Profile area: 0.0706858417, perimeter: 1.0712389512
            with BuildLine():
                Line((0.5999999851, 0.7), (0.9, 0.7))
                Line((0.9, 0.7), (0.9, 1.0000000149))
                CenterArc((0.9, 0.7), 0.3000000149, 90, 90.0000000001)
            make_face()
        # OneSide extrude, distance=-1.9
        extrude(amount=-1.9, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2.6, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((-0.5, -2.5)):
                Circle(0.25)
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -1.5), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.079521564, perimeter: 1.1568583471
            with BuildLine():
                CenterArc((0.5, 2), 0.225, 180, 180)
                Line((0.5, 2), (0.725, 2))
                Line((0.275, 2), (0.5, 2))
            make_face()
            # Profile area: 0.039760782, perimeter: 0.8034291735
            with BuildLine():
                Line((0.5, 2.225), (0.5, 2))
                Line((0.5, 2), (0.725, 2))
                CenterArc((0.5, 2), 0.225, 0, 90)
            make_face()
            # Profile area: 0.039760782, perimeter: 0.8034291735
            with BuildLine():
                Line((0.275, 2), (0.5, 2))
                Line((0.5, 2.225), (0.5, 2))
                CenterArc((0.5, 2), 0.225, 90, 90)
            make_face()
        # OneSide extrude, distance=-1.1
        extrude(amount=-1.1, mode=Mode.SUBTRACT)
    return part.part


def model_21880_c4d6cbae_0000():
    """Model: Swivel Pin (Part No. 6) v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 2.5446900494, perimeter: 5.6548667765
            Circle(0.9)
        # OneSide extrude, distance=2.1
        extrude(amount=2.1)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 2.2698006922, perimeter: 5.3407075111
            Circle(0.85)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -0.3), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.5654866776, perimeter: 11.3097335529
            with BuildLine():
                CenterArc((0, 0), 0.95, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.85, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 2.2698006922, perimeter: 5.3407075111
            Circle(0.85)
        # OneSide extrude, distance=1.2
        extrude(amount=1.2, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -1.5), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 4.2332961007, perimeter: 15.3938040026
            with BuildLine():
                CenterArc((0, 0), 1.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.95, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 2.8352873699, perimeter: 5.9690260418
            Circle(0.95)
        # OneSide extrude, distance=0.6
        extrude(amount=0.6, mode=Mode.ADD)

        # Sketch5 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 7 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -2.1), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 1.7879269772, perimeter: 7.086922922
            with BuildLine():
                Line((-0.3000000045, 1.4696938448), (-0.3000000045, -1.4696938448))
                CenterArc((0, 0), 1.5, -101.5369592071, 23.0739184142)
                Line((0.3000000045, -1.4696938448), (0.3000000045, 1.4696938448))
                CenterArc((0, 0), 1.5, 78.4630407929, 23.0739184142)
            make_face()
            # Profile area: 0.1260365418, perimeter: 1.6646861416
            with BuildLine():
                CenterArc((0, 0), 1.5, 78.4630407929, 23.0739184142)
                Line((0.3000000045, 1.4696938448), (0.3000000045, 1.7000000253))
                Line((0.3000000045, 1.7000000253), (-0.3000000045, 1.7000000253))
                Line((-0.3000000045, 1.7000000253), (-0.3000000045, 1.4696938448))
            make_face()
            # Profile area: 0.1260365418, perimeter: 1.6646861416
            with BuildLine():
                CenterArc((0, 0), 1.5, -101.5369592071, 23.0739184142)
                Line((-0.3000000045, -1.4696938448), (-0.3000000045, -1.7000000253))
                Line((-0.3000000045, -1.7000000253), (0.3000000045, -1.7000000253))
                Line((0.3000000045, -1.7000000253), (0.3000000045, -1.4696938448))
            make_face()
        # OneSide extrude, distance=-0.4
        extrude(amount=-0.4, mode=Mode.SUBTRACT)
    return part.part


def model_21881_f3bee5e5_0002():
    """Model: Screw v5"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.1309733553, perimeter: 3.7699111843
            Circle(0.6)
        # OneSide extrude, distance=6.3
        extrude(amount=6.3)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 2.9095547686, perimeter: 11.252370673
            with BuildLine():
                Line((0.0055814881, 1.247064091), (-1.0771984389, 0.628365756))
                Line((-1.0771984389, 0.628365756), (-1.082779927, -0.618698335))
                Line((-1.082779927, -0.618698335), (-0.0055814881, -1.247064091))
                Line((-0.0055814881, -1.247064091), (1.0771984389, -0.628365756))
                Line((1.0771984389, -0.628365756), (1.082779927, 0.618698335))
                Line((1.082779927, 0.618698335), (0.0055814881, 1.247064091))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.6, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 1.1309733553, perimeter: 3.7699111843
            Circle(0.6)
        # OneSide extrude, distance=1.8
        extrude(amount=1.8, mode=Mode.ADD)

        # Sketch6 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.4100251136, perimeter: 14.2368836939
            with BuildLine():
                Line((1.082779927, -0.618698335), (1.0771984389, 0.628365756))
                Line((1.0771984389, 0.628365756), (-0.0055814881, 1.247064091))
                Line((-0.0055814881, 1.247064091), (-1.082779927, 0.618698335))
                Line((-1.082779927, 0.618698335), (-1.0771984389, -0.628365756))
                Line((-1.0771984389, -0.628365756), (0.0055814881, -1.247064091))
                Line((0.0055814881, -1.247064091), (1.082779927, -0.618698335))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.075, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.05
        extrude(amount=-0.05, mode=Mode.SUBTRACT)
    return part.part


def model_21893_0500d043_0030():
    """Model: SEMI ALBERO M v2 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            Circle(0.5)
        # Symmetric extrude, each_side=1.15
        extrude(amount=1.15, both=True)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 8 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.15, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0146814767, perimeter: 0.8869167062
            with BuildLine():
                CenterArc((0, 0), 0.5, -25.8419327632, 51.6838655263)
                Line((0.45, -0.2179449472), (0.45, 0.2179449472))
            make_face()
            # Profile area: 0.0146814767, perimeter: 0.8869167062
            with BuildLine():
                Line((-0.45, 0.2179449472), (-0.45, -0.2179449472))
                CenterArc((0, 0), 0.5, 154.1580672368, 51.6838655263)
            make_face()
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.15, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            Circle(0.25)
        # OneSide extrude, distance=2.2
        extrude(amount=2.2, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -1.15, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            Circle(0.3)
        # OneSide extrude, distance=2
        extrude(amount=2, mode=Mode.ADD)
    return part.part


def model_21893_0500d043_0037():
    """Model: TRAVERSA v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.3273228961, perimeter: 4.0840704497
            Circle(0.65)
        # Symmetric extrude, each_side=1.5
        extrude(amount=1.5, both=True)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.008399624, perimeter: 0.5566142278
            with BuildLine():
                Line((0.65, 0), (0.6, 0))
                CenterArc((0, 0), 0.65, 0, 22.619864948)
                Line((0.6, 0), (0.6, 0.25))
            make_face()
            # Profile area: 0.008399624, perimeter: 0.5566142278
            with BuildLine():
                Line((0.6, 0), (0.6, -0.25))
                CenterArc((0, 0), 0.65, -22.619864948, 22.619864948)
                Line((0.65, 0), (0.6, 0))
            make_face()
        # Symmetric extrude, each_side=0.5
        extrude(amount=0.5, both=True, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            Circle(0.5)
        # OneSide extrude, distance=1.5
        extrude(amount=1.5, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 3, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            Circle(0.3)
        # OneSide extrude, distance=2
        extrude(amount=2, mode=Mode.ADD)
    return part.part


def model_21896_ba833d7d_0001():
    """Model: End Nozzle"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 33.1830724035, perimeter: 20.4203522483
            Circle(3.25)
        # OneSide extrude, distance=-3.7
        extrude(amount=-3.7)

        # Sketch2 -> Extrude2 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 33.1830724035, perimeter: 20.4203522483
            with Locations((-8.5, 0)):
                Circle(3.25)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch3 -> Extrude3 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            with Locations((-8, 1.5)):
                Circle(0.4)
        # OneSide extrude, distance=0.75
        extrude(amount=0.75)

        # Sketch4 -> Extrude9 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 7.0685834706, perimeter: 9.4247779608
            with Locations((-7.5, 0)):
                Circle(1.5)
        # OneSide extrude, distance=-1.5
        extrude(amount=-1.5)
    return part.part


def model_21899_d55d6c08_0018():
    """Model: BSE010-1 v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 10 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.2004085081, perimeter: 6.5061009831
            with BuildLine():
                CenterArc((0, 0), 1.25, 68.8998039759, 42.2003920482)
                Line((-0.45, 1.166190379), (-0.45, -1.166190379))
                CenterArc((0, 0), 1.25, -111.1001960241, 42.2003920482)
                Line((0.45, -1.166190379), (0.45, 1.166190379))
            make_face()
        # OneSide extrude, distance=2.3
        extrude(amount=2.3)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 13 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-0.45, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.0353429174, perimeter: 0.771238898
            with BuildLine():
                Line((-0.4320652264, 0.5), (-0.7320652264, 0.5))
                CenterArc((-0.5820652264, 0.5), 0.15, 0, 180)
            make_face()
            # Profile area: 0.0353429174, perimeter: 0.771238898
            with BuildLine():
                Line((0.7679347736, 0.5), (0.4679347736, 0.5))
                CenterArc((0.6179347736, 0.5), 0.15, 0, 180)
            make_face()
            # Profile area: 1.8086283306, perimeter: 6.2849555922
            with BuildLine():
                CenterArc((-0.5820652264, 0.5), 0.15, 0, 180)
                Line((0.4679347736, 0.5), (-0.4320652264, 0.5))
                CenterArc((0.6179347736, 0.5), 0.15, 0, 180)
                Line((0.7679347736, 1.8), (0.7679347736, 0.5))
                CenterArc((0.6179347736, 1.8), 0.15, 180, 180)
                Line((-0.4320652264, 1.8), (0.4679347736, 1.8))
                CenterArc((-0.5820652264, 1.8), 0.15, 180, 180)
                Line((-0.7320652264, 0.5), (-0.7320652264, 1.8))
            make_face()
            # Profile area: 0.0353429174, perimeter: 0.771238898
            with BuildLine():
                Line((0.4679347736, 1.8), (0.7679347736, 1.8))
                CenterArc((0.6179347736, 1.8), 0.15, 180, 180)
            make_face()
            # Profile area: 0.0353429174, perimeter: 0.771238898
            with BuildLine():
                Line((-0.7320652264, 1.8), (-0.4320652264, 1.8))
                CenterArc((-0.5820652264, 1.8), 0.15, 180, 180)
            make_face()
            # Profile area: 0.0353429174, perimeter: 0.771238898
            with BuildLine():
                CenterArc((-0.5820652264, 1.8), 0.15, 0, 180)
                Line((-0.7320652264, 1.8), (-0.4320652264, 1.8))
            make_face()
            # Profile area: 0.0353429174, perimeter: 0.771238898
            with BuildLine():
                CenterArc((0.6179347736, 1.8), 0.15, 0, 180)
                Line((0.4679347736, 1.8), (0.7679347736, 1.8))
            make_face()
            # Profile area: 0.0353429174, perimeter: 0.771238898
            with BuildLine():
                CenterArc((0.6179347736, 0.5), 0.15, 180, 180)
                Line((0.7679347736, 0.5), (0.4679347736, 0.5))
            make_face()
            # Profile area: 0.0353429174, perimeter: 0.771238898
            with BuildLine():
                CenterArc((-0.5820652264, 0.5), 0.15, 180, 180)
                Line((-0.4320652264, 0.5), (-0.7320652264, 0.5))
            make_face()
        # OneSide extrude, distance=-1.7
        extrude(amount=-1.7, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            Circle(0.3)
        # OneSide extrude, distance=7.65
        extrude(amount=7.65, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -7.65, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            Circle(0.25)
        # OneSide extrude, distance=1.5
        extrude(amount=1.5, mode=Mode.ADD)

        # Sketch5 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2.3, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            Circle(0.3)
        # OneSide extrude, distance=7.55
        extrude(amount=7.55, mode=Mode.ADD)
    return part.part


def model_21908_385686ec_0007():
    """Model: 15A v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 7.0685834706, perimeter: 9.4247779608
            Circle(1.5)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.1), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.8482300165, perimeter: 16.9646003294
            with BuildLine():
                CenterArc((0, 0), 1.4, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.7
        extrude(amount=0.7, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.1), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 5.3092915846, perimeter: 8.1681408993
            Circle(1.3)
        # OneSide extrude, distance=0.4
        extrude(amount=0.4, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.5), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            with Locations((0, -0.8000000119)):
                Circle(0.3)
            # Profile area: 0.2827433472, perimeter: 1.8849556202
            with Locations((0.8000000119, 0)):
                Circle(0.3000000045)
            # Profile area: 0.2827433472, perimeter: 1.8849556202
            with Locations((0, 0.8000000119)):
                Circle(0.3000000045)
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            with Locations((-0.8000000119, 0)):
                Circle(0.3)
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.SUBTRACT)
    return part.part


def model_21940_6c2dac17_0003():
    """Model: base v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 9 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 25.9111583617, perimeter: 25.3648359429
            with BuildLine():
                CenterArc((-4.45, 0.125), 1.125, 90, 180)
                Line((-4.45, -1), (-1.45, -1))
                Line((-1.45, -1), (-1.2, -1.25))
                Line((-1.2, -1.25), (4.45, -1.25))
                CenterArc((4.45, 0), 1.25, -90, 180)
                Line((4.45, 1.25), (-4.45, 1.25))
            make_face()
        # OneSide extrude, distance=0.6
        extrude(amount=0.6)
    return part.part


def model_22019_0ef07114_0000():
    """Model: Dust Seal v3"""
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
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 13.042650512, perimeter: 31.1206168265
            with BuildLine():
                CenterArc((0, 0), 2.8956, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 2.0574, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.778
        extrude(amount=1.778)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.778, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.8748176727, perimeter: 29.5246877584
            with BuildLine():
                CenterArc((0, 0), 2.413, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 2.286, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.508
        extrude(amount=-0.508, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.778, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.9948817652, perimeter: 34.9508465897
            with BuildLine():
                CenterArc((0, 0), 2.8956, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 2.667, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-1.016
        extrude(amount=-1.016, mode=Mode.SUBTRACT)

        # Sketch9 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 9 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.778, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0061197234, perimeter: 0.404790202
            with BuildLine():
                CenterArc((0, 0), 2.413, 88.0505250537, 3.8989498927)
                Line((0.082085897, 2.4498108555), (0.082085897, 2.4116033889))
                Line((-0.082085897, 2.4498108555), (0.082085897, 2.4498108555))
                Line((-0.082085897, 2.4116033889), (-0.082085897, 2.4498108555))
            make_face()
        # OneSide extrude, distance=-0.0508
        extrude(amount=-0.0508, mode=Mode.SUBTRACT)
    return part.part


def model_22025_b77024b9_0005():
    """Model: Assembly 2 v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 225, perimeter: 60
            with BuildLine():
                Line((7.5, -7.5), (7.5, 7.5))
                Line((7.5, 7.5), (-7.5, 7.5))
                Line((-7.5, 7.5), (-7.5, -7.5))
                Line((-7.5, -7.5), (7.5, -7.5))
            make_face()
        # OneSide extrude, distance=9
        extrude(amount=9)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 12 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 7.5), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 12, perimeter: 14
            with BuildLine():
                Line((4.5, 6), (7.5, 6))
                Line((4.5, 2), (4.5, 6))
                Line((7.5, 2), (4.5, 2))
                Line((7.5, 6), (7.5, 2))
            make_face()
            # Profile area: 12, perimeter: 14
            with BuildLine():
                Line((-7.5, 2), (-7.5, 6))
                Line((-7.5, 2), (-4.5, 2))
                Line((-4.5, 2), (-4.5, 6))
                Line((-4.5, 6), (-7.5, 6))
            make_face()
        # OneSide extrude, distance=-15
        extrude(amount=-15, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-4.5, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 12.0000001016, perimeter: 14.0000000508
            with BuildLine():
                Line((7.5, 2), (7.5, 6))
                Line((7.5, 6), (4.4999999746, 6))
                Line((4.4999999746, 6), (4.4999999746, 2))
                Line((4.4999999746, 2), (7.5, 2))
            make_face()
            # Profile area: 12.0000001016, perimeter: 14.0000000508
            with BuildLine():
                Line((-4.4999999746, 6), (-4.4999999746, 2))
                Line((-7.5, 6), (-4.4999999746, 6))
                Line((-7.5, 2), (-7.5, 6))
                Line((-4.4999999746, 2), (-7.5, 2))
            make_face()
        # OneSide extrude, distance=-12
        extrude(amount=-12, mode=Mode.SUBTRACT)
    return part.part


def model_22025_b77024b9_0009():
    """Model: Set Screw Part 7 v2 (1) (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            Circle(0.5)
        # OneSide extrude, distance=0.7
        extrude(amount=0.7)

        # Sketch3 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.7, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.2252211349, perimeter: 8.1681408993
            with BuildLine():
                CenterArc((0, 0), 0.8, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            Circle(0.5)
        # OneSide extrude, distance=4.9
        extrude(amount=4.9, mode=Mode.ADD)

        # Sketch4 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 5.6, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.7907078125, perimeter: 11.9380520836
            with BuildLine():
                CenterArc((0, 0), 1.1, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.8, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 2.0106192983, perimeter: 5.0265482457
            Circle(0.8)
        # OneSide extrude, distance=1.9
        extrude(amount=1.9, mode=Mode.ADD)

        # Sketch5 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 11 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 7.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.9369001148, perimeter: 7.6901839487
            with BuildLine():
                CenterArc((0, 0), 1.1, -79.5243181457, 159.0486362915)
                Line((0.200000003, -1.0816653821), (0.200000003, -1.2000000179))
                Line((0.200000003, -1.2000000179), (1.2000000179, -1.2000000179))
                Line((1.2000000179, -1.2000000179), (1.2000000179, 1.2000000179))
                Line((1.2000000179, 1.2000000179), (0.200000003, 1.2000000179))
                Line((0.200000003, 1.2000000179), (0.200000003, 1.0816653821))
            make_face()
            # Profile area: 1.4630999567, perimeter: 5.2168453757
            with BuildLine():
                Line((0.200000003, 0), (0.200000003, -1.0816653821))
                CenterArc((0, 0), 1.1, -79.5243181457, 159.0486362915)
                Line((0.200000003, 1.0816653821), (0.200000003, 0))
            make_face()
            # Profile area: 1.4630999567, perimeter: 5.2168453757
            with BuildLine():
                CenterArc((0, 0), 1.1, 100.4756818543, 159.0486362915)
                Line((-0.200000003, -1.0816653821), (-0.200000003, 0))
                Line((-0.200000003, 0), (-0.200000003, 1.0816653821))
            make_face()
            # Profile area: 0.9369001148, perimeter: 7.6901839487
            with BuildLine():
                Line((-0.200000003, 1.0816653821), (-0.200000003, 1.2000000179))
                Line((-0.200000003, 1.2000000179), (-1.2000000179, 1.2000000179))
                Line((-1.2000000179, 1.2000000179), (-1.2000000179, -1.2000000179))
                Line((-1.2000000179, -1.2000000179), (-0.200000003, -1.2000000179))
                Line((-0.200000003, -1.2000000179), (-0.200000003, -1.0816653821))
                CenterArc((0, 0), 1.1, 100.4756818543, 159.0486362915)
            make_face()
        # OneSide extrude, distance=-1.4
        extrude(amount=-1.4, mode=Mode.SUBTRACT)
    return part.part


def model_22124_6f71410e_0010():
    """Model: Guide Bar v4 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.8815968645, perimeter: 4.8625963791
            with Locations((3.8853984609, 1.8313343592)):
                Circle(0.77390625)
        # OneSide extrude, distance=13.335
        extrude(amount=13.335)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 13.335), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1.1888327329, perimeter: 3.8651407116
            with Locations((3.8853984609, 1.8313343592)):
                Circle(0.61515625)
        # OneSide extrude, distance=0.714375
        extrude(amount=0.714375, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.2090663183, perimeter: 1.6208654597
            with Locations((-3.8853984609, 1.8313343592)):
                Circle(0.25796875)
        # OneSide extrude, distance=-0.635
        extrude(amount=-0.635, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 14.049375), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.2090663183, perimeter: 1.6208654597
            with Locations((3.8853984609, 1.8313343592)):
                Circle(0.25796875)
        # OneSide extrude, distance=-0.635
        extrude(amount=-0.635, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude5 (Cut)
        # Sketch on YZ construction plane
        # Sketch has 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.1781393481, perimeter: 1.4961835013
            with Locations((-1.27, 1.8313343592)):
                Circle(0.238125)
        # OneSide extrude, distance=7.112
        extrude(amount=7.112, mode=Mode.SUBTRACT)
    return part.part


def model_22181_526fb582_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 12 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 9.4247779608, perimeter: 18.8495559215
            with BuildLine():
                CenterArc((0, 0), 2, 90, 90)
                CenterArc((0, 0), 2, -180, 90)
                CenterArc((0, 0), 2, -90, 90)
                CenterArc((0, 0), 2, 0, 90)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 4, perimeter: 10
            with BuildLine():
                Line((-2, -2), (0, -2))
                Line((-2, -3), (-2, -2))
                Line((2, -3), (-2, -3))
                Line((2, -2), (2, -3))
                Line((0, -2), (2, -2))
            make_face()
            # Profile area: 0.8584073464, perimeter: 7.1415926536
            with BuildLine():
                Line((-2, -2), (-2, 0))
                Line((-2, -2), (0, -2))
                CenterArc((0, 0), 2, -180, 90)
            make_face()
            # Profile area: 0.8584073464, perimeter: 7.1415926536
            with BuildLine():
                CenterArc((0, 0), 2, -90, 90)
                Line((0, -2), (2, -2))
                Line((2, 0), (2, -2))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4, perimeter: 10
            with BuildLine():
                Line((2, 2), (2, 3))
                Line((2, 3), (-2, 3))
                Line((-2, 3), (-2, 2))
                Line((-2, 2), (2, 2))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 12, perimeter: 14
            with BuildLine():
                Line((-2, 6), (2, 6))
                Line((-2, 3), (-2, 6))
                Line((2, 3), (-2, 3))
                Line((2, 6), (2, 3))
            make_face()
            # Profile area: 4, perimeter: 10
            with BuildLine():
                Line((-2, 2), (-2, 3))
                Line((2, 2), (-2, 2))
                Line((2, 3), (2, 2))
                Line((2, 3), (-2, 3))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 3, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4, perimeter: 10
            with BuildLine():
                Line((2, 5), (2, 6))
                Line((2, 6), (-2, 6))
                Line((-2, 6), (-2, 5))
                Line((-2, 5), (2, 5))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)

        # Sketch5 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 4, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 9.4247779608, perimeter: 18.8495559215
            with BuildLine():
                CenterArc((0, 8), 2, 90, 90)
                CenterArc((0, 8), 2, 180, 90)
                CenterArc((0, 8), 2, -90, 90)
                CenterArc((0, 8), 2, 0, 90)
            make_face()
            with BuildLine():
                CenterArc((0, 8), 1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.8584073464, perimeter: 7.1415926536
            with BuildLine():
                Line((0, 6), (-2, 6))
                CenterArc((0, 8), 2, 180, 90)
                Line((-2, 6), (-2, 8))
            make_face()
            # Profile area: 4, perimeter: 10
            with BuildLine():
                Line((2, 6), (0, 6))
                Line((0, 6), (-2, 6))
                Line((-2, 5), (-2, 6))
                Line((2, 5), (-2, 5))
                Line((2, 6), (2, 5))
            make_face()
            # Profile area: 0.8584073464, perimeter: 7.1415926536
            with BuildLine():
                CenterArc((0, 8), 2, -90, 90)
                Line((2, 6), (0, 6))
                Line((2, 8), (2, 6))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)
    return part.part


def model_22198_327974c6_0004():
    """Model: Valve v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            Circle(0.3)
        # OneSide extrude, distance=0.8
        extrude(amount=0.8)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            Circle(0.15)
        # OneSide extrude, distance=3.4
        extrude(amount=3.4, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -3.4, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.2120575041, perimeter: 2.8274333882
            with BuildLine():
                CenterArc((0, 0), 0.3, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            Circle(0.15)
        # OneSide extrude, distance=0.8
        extrude(amount=0.8, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -4.2, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            Circle(0.15)
        # OneSide extrude, distance=1.8
        extrude(amount=1.8, mode=Mode.ADD)

        # Sketch5 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -6, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.7147123287, perimeter: 4.0840704497
            with BuildLine():
                CenterArc((0, 0), 0.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            Circle(0.15)
        # OneSide extrude, distance=0.8
        extrude(amount=0.8, mode=Mode.ADD)
    return part.part


def model_22202_c9c16395_0005():
    """Model: eccentric rod clevis v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 9 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.2762214959, perimeter: 2.8877550972
            with BuildLine():
                CenterArc((0.23749, 0), 0.23876, -90, 180)
                Line((0.23749, 0.23876), (-0.23749, 0.23876))
                Line((-0.23749, 0.23876), (-0.23749, -0.23876))
                Line((-0.23749, -0.23876), (0.23749, -0.23876))
            make_face()
            with BuildLine():
                CenterArc((0.23749, 0), 0.11303, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=0.23876
        extrude(amount=0.23876, both=True)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 9 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.23876, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0473423992, perimeter: 0.9075806206
            with BuildLine():
                Line((-0.23749, 0.08128), (-0.23749, -0.08128))
                Line((-0.23749, 0.08128), (-0.5287203103, 0.08128))
                Line((-0.5287203103, 0.08128), (-0.5287203103, -0.08128))
                Line((-0.5287203103, -0.08128), (-0.23749, -0.08128))
            make_face()
            # Profile area: 0.0524386048, perimeter: 0.97028
            with BuildLine():
                Line((-0.23749, -0.08128), (0.08509, -0.08128))
                Line((0.08509, -0.08128), (0.08509, 0.08128))
                Line((0.08509, 0.08128), (-0.23749, 0.08128))
                Line((-0.23749, 0.08128), (-0.23749, -0.08128))
            make_face()
        # OneSide extrude, distance=-0.7874
        extrude(amount=-0.7874, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-0.23749, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.0791730436, perimeter: 0.9974556675
            Circle(0.15875)
        # OneSide extrude, distance=0.635
        extrude(amount=0.635, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-0.87249, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.0275227795, perimeter: 0.5880998616
            Circle(0.093599)
        # OneSide extrude, distance=-0.762
        extrude(amount=-0.762, mode=Mode.SUBTRACT)
    return part.part


def model_22202_c9c16395_0009():
    """Model: Frame spreader bar v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.077911342, perimeter: 0.9894760222
            Circle(0.15748)
        # Symmetric extrude, each_side=1.27
        extrude(amount=1.27, both=True)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1.27), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0973891775, perimeter: 2.4736900554
            with BuildLine():
                CenterArc((0, 0), 0.23622, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.15748, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.08128
        extrude(amount=-0.08128, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -1.27), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.0973891775, perimeter: 2.4736900554
            with BuildLine():
                CenterArc((0, 0), 0.23622, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.15748, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.08128
        extrude(amount=-0.08128, mode=Mode.ADD)
    return part.part


def model_22206_703c82ed_0000():
    """Model: HOLDER"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 13 constraints, 11 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 16.746380358, perimeter: 24.1042314719
            with BuildLine():
                Line((0, 3.8100001119), (0, 2.5400001119))
                Line((0, 2.5400001119), (2.3812494357, 2.540000151))
                CenterArc((2.38125, 1.9050000755), 0.6350000755, -90.0000108187, 180.0000617379)
                Line((0, 1.27), (2.3812498801, 1.27))
                Line((0, 0), (0, 1.27))
                Line((0, 0), (1.2699999809, 0))
                Line((1.2699999809, 0), (2.0692423796, -0.9525))
                Line((2.0692423796, -0.9525), (3.4925, -0.9525))
                Line((3.4925, -0.9525), (3.4925, 0.1092036632))
                Line((3.4925, 0.1092036632), (5.08, 0.417782404))
                Line((5.08, 0.417782404), (5.08, 3.5020891219))
                Line((3.33375, 3.8100001119), (5.08, 3.5020891219))
                Line((3.33375, 3.8100001119), (0, 3.8100001119))
            make_face()
        # OneSide extrude, distance=-1.27
        extrude(amount=-1.27)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 12 constraints, 14 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 15.9794605486, perimeter: 19.0765292088
            with BuildLine():
                Line((5.08, 0.8283597264), (5.08, 2.5400001119))
                Line((5.08, 0.8283597264), (5.55625, 0.8283597264))
                Line((5.55625, 0.8283597264), (7.9195306779, -0.9525))
                Line((7.9195306779, -0.9525), (11.4355428897, -0.9525))
                Line((11.4355428897, -0.9525), (11.4355428897, 1.11125))
                Line((11.4355428897, 1.11125), (10.2265028897, 1.11125))
                Line((10.2265028897, 1.11125), (8.3304874522, 2.5400001119))
                Line((8.3304874522, 2.5400001119), (5.08, 2.5400001119))
            make_face()
            with BuildLine():
                CenterArc((10.2265028897, -0.15875), 0.2413, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 4.7981100732, perimeter: 8.8733769069
            with BuildLine():
                Line((5.08, 3.5020891219), (3.33375, 3.8100001119))
                Line((3.33375, 3.8100001119), (3.33375, 1.2625307132))
                Line((3.33375, 1.2625307132), (3.9774349587, 0.8283597264))
                Line((3.9774349587, 0.8283597264), (5.08, 0.8283597264))
                Line((5.08, 0.8283597264), (5.08, 2.5400001119))
                Line((5.08, 2.5400001119), (5.08, 3.5020891219))
            make_face()
        # OneSide extrude, distance=0.3175
        extrude(amount=0.3175, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.3175, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 1.2667686977, perimeter: 3.9898226701
            with Locations((4.1275, 1.9050000755)):
                Circle(0.635)
        # OneSide extrude, distance=0.635
        extrude(amount=0.635, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 3.4925, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.564515, perimeter: 3.048
            with BuildLine():
                Line((0.9525, -0.9525), (0.9525, -0.0635))
                Line((0.9525, -0.0635), (0.3175, -0.0635))
                Line((0.3175, -0.0635), (0.3175, -0.9525))
                Line((0.3175, -0.9525), (0.9525, -0.9525))
            make_face()
        # OneSide extrude, distance=-1.11125
        extrude(amount=-1.11125, mode=Mode.SUBTRACT)
    return part.part


def model_22253_f4ff5358_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 38.4845100065, perimeter: 21.9911485751
            Circle(3.5)
        # OneSide extrude, distance=13
        extrude(amount=13)

        # Sketch2 -> Extrude2 (NewBody)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 13, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 5.6941366846, perimeter: 45.5530934771
            with BuildLine():
                CenterArc((0, 0), 3.75, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 3.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=2
        extrude(amount=2)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 13, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 38.4845100065, perimeter: 21.9911485751
            Circle(3.5)
        # OneSide extrude, distance=2
        extrude(amount=2, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 35.2565235549, perimeter: 21.0486707791
            Circle(3.35)
        # OneSide extrude, distance=-14.7
        extrude(amount=-14.7, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 15, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 6.2831854008, perimeter: 9.6884483319
            Ellipse(2.0000000298, 1, rotation=180)
        # OneSide extrude, distance=-4
        extrude(amount=-4, mode=Mode.SUBTRACT)
    return part.part


def model_22254_539990c2_0009():
    """Model: Pump Body v23"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 100.2874914842, perimeter: 35.4999969856
            Circle(5.65)
        # OneSide extrude, distance=-6.675
        extrude(amount=-6.675)

        # Sketch4 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -6.675), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 620.7787083493, perimeter: 130.6902543893
            with BuildLine():
                CenterArc((0, 0), 15.15, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 5.65, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 100.2874914842, perimeter: 35.4999969856
            Circle(5.65)
        # OneSide extrude, distance=18.416
        extrude(amount=18.416, mode=Mode.ADD)

        # Sketch3 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 63.6172512352, perimeter: 28.2743338823
            Circle(4.5)
        # OneSide extrude, distance=-15
        extrude(amount=-15, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -15), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 8.730077336, perimeter: 10.9985226281
            with BuildLine():
                Line((1.5875, -0.9165435523), (1.5875, 0.9165435523))
                Line((1.5875, 0.9165435523), (0, 1.8330871047))
                Line((0, 1.8330871047), (-1.5875, 0.9165435523))
                Line((-1.5875, 0.9165435523), (-1.5875, -0.9165435523))
                Line((-1.5875, -0.9165435523), (0, -1.8330871047))
                Line((0, -1.8330871047), (1.5875, -0.9165435523))
            make_face()
        # OneSide extrude, distance=2.54
        extrude(amount=2.54, mode=Mode.ADD)
    return part.part


def model_22289_4b848f64_0001():
    """Model: Iris Blade 45* v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 10.3553390593, perimeter: 14.9660576267
            with BuildLine():
                Line((-2.0710678119, 5), (2.0710678119, 5))
                Line((0, 0), (-2.0710678119, 5))
                Line((2.0710678119, 5), (0, 0))
            make_face()
        # OneSide extrude, distance=0.4
        extrude(amount=0.4)

        # Sketch2 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.4, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0754767635, perimeter: 0.9738937226
            with Locations((0, -4.5)):
                Circle(0.155)
        # OneSide extrude, distance=-1.5
        extrude(amount=-1.5, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.1864959211, perimeter: 2.8791496109
            with BuildLine():
                Line((0.2744830841, -4.6596633017), (0.2755140173, -4.3421223271))
                Line((0.2755140173, -4.3421223271), (0.0010309333, -4.1824590255))
                Line((0.0010309333, -4.1824590255), (-0.2744830841, -4.3403366983))
                Line((-0.2744830841, -4.3403366983), (-0.2755140173, -4.6578776729))
                Line((-0.2755140173, -4.6578776729), (-0.0010309333, -4.8175409745))
                Line((-0.0010309333, -4.8175409745), (0.2744830841, -4.6596633017))
            make_face()
            with BuildLine():
                CenterArc((0, -4.5), 0.155, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.25
        extrude(amount=-0.25, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.3106858347, perimeter: 2.5424777961
            with BuildLine():
                CenterArc((0.605, -4.5), 0.15, 90, 180)
                Line((0.605, -4.65), (1.405, -4.65))
                CenterArc((1.405, -4.5), 0.15, -90, 180)
                Line((1.405, -4.35), (0.605, -4.35))
            make_face()
        # OneSide extrude, distance=0.4
        extrude(amount=0.4, mode=Mode.ADD)
    return part.part


def model_22305_5b45cdb3_0021():
    """Model: 26-FIRE-BOX v3 (2)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 8 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.4069468613, perimeter: 28.1389372261
            with BuildLine():
                CenterArc((1.6, 3.1), 1.6, 0, 180)
                Line((0, 3.1), (0, 0))
                Line((0, 0), (3.2, 0))
                Line((3.2, 0), (3.2, 3.1))
            make_face()
            with BuildLine():
                Line((3.1, 0.1), (3.1, 3.1))
                Line((0.1, 0.1), (3.1, 0.1))
                Line((0.1, 3.1), (0.1, 0.1))
                CenterArc((1.6, 3.1), 1.5, 0, 180)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=2.7
        extrude(amount=2.7)

        # Sketch11 -> Extrude10 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(3.2, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.315, perimeter: 2.5
            with BuildLine():
                Line((-1.8, 1.25), (-1.8, 0.9))
                Line((-1.8, 0.9), (-0.9, 0.9))
                Line((-0.9, 0.9), (-0.9, 1.25))
                Line((-0.9, 1.25), (-1.8, 1.25))
            make_face()
        # OneSide extrude, distance=0.05
        extrude(amount=0.05, mode=Mode.ADD)

        # Sketch12 -> Extrude11 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.315, perimeter: 2.5
            with BuildLine():
                Line((0.9, 1.25), (0.9, 0.9))
                Line((0.9, 0.9), (1.8, 0.9))
                Line((1.8, 0.9), (1.8, 1.25))
                Line((1.8, 1.25), (0.9, 1.25))
            make_face()
        # OneSide extrude, distance=0.05
        extrude(amount=0.05, mode=Mode.ADD)

        # Sketch13 -> Extrude12 (NewBody)
        # Sketch on BRepFace
        # Sketch has 9 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.25, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.3599999946, perimeter: 2.5999999732
            with BuildLine():
                Line((0.4, 0.9000000134), (0, 0.9000000134))
                Line((0.4, 1.8), (0.4, 0.9000000134))
                Line((0, 1.8), (0.4, 1.8))
                Line((0, 0.9000000134), (0, 1.8))
            make_face()
            # Profile area: 0.0449999993, perimeter: 1.8999999732
            with BuildLine():
                Line((-3.2, 0.9000000134), (-3.2, 1.8))
                Line((-3.2, 1.8), (-3.25, 1.8))
                Line((-3.25, 1.8), (-3.25, 0.9000000134))
                Line((-3.25, 0.9000000134), (-3.2, 0.9000000134))
            make_face()
            # Profile area: 0.3149999953, perimeter: 2.4999999732
            with BuildLine():
                Line((-3.25, 1.8), (-3.25, 0.9000000134))
                Line((-3.25, 1.8), (-3.6, 1.8))
                Line((-3.6, 1.8), (-3.6, 0.9000000134))
                Line((-3.6, 0.9000000134), (-3.25, 0.9000000134))
            make_face()
        # OneSide extrude, distance=0.05
        extrude(amount=0.05)

        # Sketch14 -> Extrude13 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-0.05, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.0176714587, perimeter: 0.471238898
            with Locations((1.35, 1.1)):
                Circle(0.075)
        # OneSide extrude, distance=-10
        extrude(amount=-10, mode=Mode.SUBTRACT)
    return part.part


def model_22340_ec24cd79_0025():
    """Model: part 5 v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 547.3911039615, perimeter: 82.9380460548
            Circle(13.2)
        # OneSide extrude, distance=9
        extrude(amount=9)

        # Sketch11 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 55.4176944093, perimeter: 26.3893782902
            Circle(4.2)
        # OneSide extrude, distance=-9
        extrude(amount=-9, mode=Mode.SUBTRACT)

        # Sketch12 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 10 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(9, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.162543179, perimeter: 1.6196983254
            with BuildLine():
                Line((0, 4.6000000685), (-0.400000006, 4.6000000685))
                Line((-0.400000006, 4.6000000685), (-0.400000006, 4.1809089915))
                CenterArc((0, 0), 4.2, 90, 5.4650238816)
                Line((0, 4.6000000685), (0, 4.2))
            make_face()
            # Profile area: 0.162543179, perimeter: 1.6196983254
            with BuildLine():
                Line((0, 4.6000000685), (0.400000006, 4.6000000685))
                Line((0, 4.6000000685), (0, 4.2))
                CenterArc((0, 0), 4.2, 84.5349761184, 5.4650238816)
                Line((0.400000006, 4.6000000685), (0.400000006, 4.1809089915))
            make_face()
        # OneSide extrude, distance=-9
        extrude(amount=-9, mode=Mode.SUBTRACT)
    return part.part


def model_22344_51f483c9_0008():
    """Model: Displacer Crank End v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 18 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.3167367185, perimeter: 8.9840704422
            with BuildLine():
                Line((2, 0.75), (1.4000000075, 0.75))
                CenterArc((1.4000000075, 1.05), 0.3, -179.9999982925, 89.9999982925)
                Line((1.1, 1.3000000194), (1.1000000075, 1.0499999911))
                CenterArc((0.55, 1.3), 0.55, 0.000002018, 179.9999960875)
                Line((0, 1.3000000182), (0, 0))
                Line((0, 0), (2, 0))
                Line((2, 0), (2, 0.75))
            make_face()
            with BuildLine():
                CenterArc((0.55, 1.3), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 2.3167367185, perimeter: 8.9840704422
            with BuildLine():
                Line((0, 0), (2, 0))
                Line((0, -1.3000000194), (0, 0))
                CenterArc((0.55, -1.3), 0.55, -179.999997982, 179.999995964)
                Line((1.1, -1.3000000194), (1.1000000075, -1.0499999911))
                CenterArc((1.4000000075, -1.05), 0.3, 90, 89.9999982925)
                Line((2, -0.75), (1.4000000075, -0.75))
                Line((2, 0), (2, -0.75))
            make_face()
            with BuildLine():
                CenterArc((0.55, -1.3), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.2
        extrude(amount=1.2)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -0.75), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))) as sk:
            # Profile area: 0.7000000037, perimeter: 3.8000000149
            with BuildLine():
                Line((0, 0.35), (0, 0.85))
                Line((-1.4000000075, 0.85), (0, 0.85))
                Line((-1.4000000075, 0.85), (-1.4000000075, 0.35))
                Line((0, 0.35), (-1.4000000075, 0.35))
            make_face()
        # TwoSides extrude, along=1.1098, against=-0.1
        extrude(amount=1.1098, mode=Mode.SUBTRACT)
        extrude(sk.sketch, amount=-0.1, mode=Mode.SUBTRACT)

        # Sketch2 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -0.75), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.2999999963, perimeter: 2.1999999851
            with BuildLine():
                Line((-1.4000000075, 0.85), (-1.4000000075, 0.35))
                Line((-2, 0.85), (-1.4000000075, 0.85))
                Line((-2, 0.35), (-2, 0.85))
                Line((-1.4000000075, 0.35), (-2, 0.35))
            make_face()
        # OneSide extrude, distance=-0.1
        extrude(amount=-0.1, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(2, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            with Locations((0, 0.6)):
                Circle(0.3)
        # OneSide extrude, distance=-4.7
        extrude(amount=-4.7, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((-1.55, 0)):
                Circle(0.15)
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((-0.55, 0)):
                Circle(0.15)
        # OneSide extrude, distance=-2.4
        extrude(amount=-2.4, mode=Mode.SUBTRACT)
    return part.part


def model_22369_481ab478_0012():
    """Model: bell screw v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0383526891, perimeter: 0.6942291446
            Circle(0.11049)
        # OneSide extrude, distance=0.3175
        extrude(amount=0.3175)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0248286665, perimeter: 0.5585751738
            Circle(0.0889)
        # OneSide extrude, distance=-0.1524
        extrude(amount=-0.1524, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.3175, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0427205056, perimeter: 1.7035833002
            with BuildLine():
                CenterArc((0, 0), 0.1606437032, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.11049, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0383526891, perimeter: 0.6942291446
            Circle(0.11049)
        # OneSide extrude, distance=0.0762
        extrude(amount=0.0762, mode=Mode.ADD)

        # Sketch5 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 13 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.3937, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0161471655, perimeter: 0.7348315202
            with BuildLine():
                Line((0.0253999997, -0.1578857715), (-0.0253999997, -0.1578857715))
                Line((0.0253999997, 0.1586229472), (0.0253999997, -0.1578857715))
                CenterArc((0, 0), 0.1606437032, 80.9025638306, 18.1948723388)
                Line((-0.0253999997, -0.1578857715), (-0.0253999997, 0.1586229472))
            make_face()
        # OneSide extrude, distance=-0.0508
        extrude(amount=-0.0508, mode=Mode.SUBTRACT)
    return part.part


def model_22447_4062c6cb_0002():
    """Model: Roller bearing Casing v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.1547562844, perimeter: 7.2256631033
            Circle(1.15)
        # OneSide extrude, distance=1.2
        extrude(amount=1.2)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            Circle(1)
        # OneSide extrude, distance=-0.7
        extrude(amount=-0.7, mode=Mode.SUBTRACT)

        # Sketch1 -> Extrude3 (Join)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.9138271862, perimeter: 16.650441064
            with BuildLine():
                CenterArc((0, 0), 1.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 4.1547562844, perimeter: 7.2256631033
            Circle(1.15)
        # OneSide extrude, distance=-0.3
        extrude(amount=-0.3, mode=Mode.ADD)

        # Sketch3 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -0.3, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            Circle(1)
        # OneSide extrude, distance=-0.3
        extrude(amount=-0.3, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -0.3, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.0314159387, perimeter: 0.6283186524
            with Locations((0.5413, 1.1819451596)):
                Circle(0.1000000194)
            # Profile area: 0.1427909734, perimeter: 1.7420690236
            with BuildLine():
                CenterArc((0, 1.3000000194), 0.1000000194, -90, 180)
                CenterArc((0, 0), 1.4, 90, 24.5435394891)
                CenterArc((-0.54, 1.1825396612), 0.0999999806, 114.5435394891, 180)
                CenterArc((0, 0), 1.2, 90, 24.5435394891)
            make_face()
        # OneSide extrude, distance=-0.85
        extrude(amount=-0.85, mode=Mode.SUBTRACT)
    return part.part


def model_22524_0be3da8a_0010():
    """Model: Cylinder Head v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.0241875, perimeter: 6.985
            with BuildLine():
                Line((1.5875, -1.905), (0, -1.905))
                Line((1.5875, 0), (1.5875, -1.905))
                Line((0, 0), (1.5875, 0))
                Line((0, -1.905), (0, 0))
            make_face()
        # OneSide extrude, distance=3.175
        extrude(amount=3.175)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 10 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.1002126001, perimeter: 2.1580538168
            with BuildLine():
                CenterArc((0.79375, 0.9525), 0.9525, -146.4426902381, 56.4426896696)
                Line((0, 0.4259858145), (0, 0))
                Line((0, 0), (0.7937499905, 0))
            make_face()
            # Profile area: 0.678284201, perimeter: 5.2420757482
            with BuildLine():
                CenterArc((0.79375, 0.9525), 0.9525, -90.0000005685, 56.4426908065)
                Line((1.5875, 0.4259858145), (1.5875, 0.9525))
                Line((1.42875, 0.9525), (1.5875, 0.9525))
                CenterArc((0.79375, 0.9525), 0.635, -180, 180)
                Line((0, 0.9525), (0.15875, 0.9525))
                Line((0, 0.9525), (0, 0.4259858145))
                CenterArc((0.79375, 0.9525), 0.9525, -146.4426902381, 56.4426896696)
            make_face()
            # Profile area: 0.678284201, perimeter: 5.2420757482
            with BuildLine():
                Line((1.5875, 0.9525), (1.5875, 1.4790141855))
                CenterArc((0.79375, 0.9525), 0.9525, 33.5573097619, 56.4426902381)
                CenterArc((0.79375, 0.9525), 0.9525, 90, 56.4426902381)
                Line((0, 1.4790141855), (0, 0.9525))
                Line((0, 0.9525), (0.15875, 0.9525))
                CenterArc((0.79375, 0.9525), 0.635, 0, 180)
                Line((1.42875, 0.9525), (1.5875, 0.9525))
            make_face()
            # Profile area: 0.1002126001, perimeter: 2.1580538357
            with BuildLine():
                CenterArc((0.79375, 0.9525), 0.9525, 33.5573097619, 56.4426902381)
                Line((1.5875, 1.4790141855), (1.5875, 1.905))
                Line((1.5875, 1.905), (0.79375, 1.905))
            make_face()
            # Profile area: 0.1002126001, perimeter: 2.1580538357
            with BuildLine():
                CenterArc((0.79375, 0.9525), 0.9525, 90, 56.4426902381)
                Line((0.79375, 1.905), (0, 1.905))
                Line((0, 1.905), (0, 1.4790141855))
            make_face()
            # Profile area: 0.1002126001, perimeter: 2.1580538546
            with BuildLine():
                Line((0.7937499905, 0), (1.5875, 0))
                Line((1.5875, 0), (1.5875, 0.4259858145))
                CenterArc((0.79375, 0.9525), 0.9525, -90.0000005685, 56.4426908065)
            make_face()
        # OneSide extrude, distance=-2.21996
        extrude(amount=-2.21996, mode=Mode.SUBTRACT)

        # Sketch2 -> Extrude10 (Cut)
        # Sketch on BRepFace
        # Sketch has 10 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.3600891365, perimeter: 2.4617431466
            with BuildLine():
                CenterArc((0.79375, 0.9525), 0.47879, 0, 180)
                Line((0.31496, 0.9525), (1.27254, 0.9525))
            make_face()
            # Profile area: 0.3600891365, perimeter: 2.4617431466
            with BuildLine():
                Line((0.31496, 0.9525), (1.27254, 0.9525))
                CenterArc((0.79375, 0.9525), 0.47879, -180, 180)
            make_face()
        # OneSide extrude, distance=-2.37998
        extrude(amount=-2.37998, mode=Mode.SUBTRACT)
    return part.part


def model_22645_1ba0af00_0010():
    """Model: Disc v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 383.8633523605, perimeter: 133.5176877776
            with BuildLine():
                CenterArc((0, 0), 13.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 7.75, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-2.1
        extrude(amount=-2.1)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))) as sk:
            # Profile area: 188.6919087562, perimeter: 48.6946861306
            Circle(7.75)
        # TwoSides extrude, along=3.8, against=-2.1
        extrude(amount=3.8, mode=Mode.ADD)
        extrude(sk.sketch, amount=-2.1, mode=Mode.ADD)

        # Sketch2 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -2.1, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 143.1388152792, perimeter: 42.4115008235
            Circle(6.75)
        # OneSide extrude, distance=-4.4
        extrude(amount=-4.4, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 3.8, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 28.2743338823, perimeter: 18.8495559215
            Circle(3)
        # OneSide extrude, distance=-25
        extrude(amount=-25, mode=Mode.SUBTRACT)
    return part.part


def model_22645_1ba0af00_0011():
    """Model: part2 v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 78.5398163397, perimeter: 31.4159265359
            Circle(5)
        # OneSide extrude, distance=3
        extrude(amount=3)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 3, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 50.2654824574, perimeter: 25.1327412287
            Circle(4)
        # OneSide extrude, distance=7
        extrude(amount=7, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 10, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 92.8733328217, perimeter: 67.5442420522
            with BuildLine():
                CenterArc((0, 0), 6.75, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 50.2654824574, perimeter: 25.1327412287
            Circle(4)
        # OneSide extrude, distance=0.6
        extrude(amount=0.6, mode=Mode.ADD)

        # Sketch5 -> Extrude4 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1057459941, perimeter: 1.3378316507
            with BuildLine():
                CenterArc((0, 0), 5, -87.9274691445, 2.2363531339)
                CenterArc((-0.001276216, 0.0228934152), 5.0229246131, -90.5193986222, 2.5970334747)
                Line((0.0756667217, -5.2878674786), (-0.0468094893, -4.9998248121))
                Line((0.3756667217, -5.2878674786), (0.0756667217, -5.2878674786))
                Line((0.3756667217, -4.9858674786), (0.3756667217, -5.2878674786))
            make_face()
        # OneSide extrude, distance=2.7
        extrude(amount=2.7)
    return part.part


def model_22666_bdaa1303_0000():
    """Model: RearCover v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 2.6049274122, perimeter: 5.7214057089
            Circle(0.91059)
        # OneSide extrude, distance=-0.47498
        extrude(amount=-0.47498)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -0.47498), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 1.7758272995, perimeter: 4.7239500413
            Circle(0.75184)
        # OneSide extrude, distance=0.23876
        extrude(amount=0.23876, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -0.71374), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.8291001127, perimeter: 10.4453557502
            with BuildLine():
                CenterArc((0, 0), 0.91059, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.75184, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 1.7758272995, perimeter: 4.7239500413
            Circle(0.75184)
        # OneSide extrude, distance=0.07874
        extrude(amount=0.07874, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 13 constraints, 9 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -0.79248), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 1.7326406211, perimeter: 16.2226189765
            with BuildLine():
                CenterArc((0, 0), 1.19126, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.91059, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-0.52578, 0.9106776736), 0.08001, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0.52578, 0.9106776736), 0.08001, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1.05156, 0), 0.08001, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-1.05156, 0), 0.08001, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-0.52578, -0.9106776736), 0.08001, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0.52578, -0.9106776736), 0.08001, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 2.6049274122, perimeter: 5.7214057089
            Circle(0.91059)
        # OneSide extrude, distance=0.16002
        extrude(amount=0.16002, mode=Mode.ADD)

        # Sketch5 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -0.9525), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 1.4287174751, perimeter: 4.2371916756
            Circle(0.67437)
        # OneSide extrude, distance=-0.79248
        extrude(amount=-0.79248, mode=Mode.SUBTRACT)
    return part.part


def model_22711_33843a5d_0004():
    """Model: Clamping Screw v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 2.56, perimeter: 6.4
            with BuildLine():
                Line((-0.8, 0.8), (0.8, 0.8))
                Line((-0.8, -0.8), (-0.8, 0.8))
                Line((0.8, -0.8), (-0.8, -0.8))
                Line((0.8, 0.8), (0.8, -0.8))
            make_face()
        # OneSide extrude, distance=1.6
        extrude(amount=1.6)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1.6), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1.6512996385, perimeter: 4.5553093477
            Circle(0.725)
        # OneSide extrude, distance=0.9
        extrude(amount=0.9, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 2.5), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 3.2574388827, perimeter: 12.4092909817
            with BuildLine():
                CenterArc((0, 0), 1.25, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.725, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 1.6512996385, perimeter: 4.5553093477
            Circle(0.725)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 3), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 2.0106192983, perimeter: 5.0265482457
            Circle(0.8)
        # OneSide extrude, distance=4.5
        extrude(amount=4.5, mode=Mode.ADD)
    return part.part


def model_22711_33843a5d_0007():
    """Model: Tool Fixing Screw v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.56, perimeter: 6.4
            with BuildLine():
                Line((-0.8, 0.8), (0.8, 0.8))
                Line((-0.8, -0.8), (-0.8, 0.8))
                Line((0.8, -0.8), (-0.8, -0.8))
                Line((0.8, 0.8), (0.8, -0.8))
            make_face()
        # OneSide extrude, distance=1.6
        extrude(amount=1.6)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.6, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.6512996385, perimeter: 4.5553093477
            Circle(0.725)
        # OneSide extrude, distance=1.2
        extrude(amount=1.2, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2.8, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.0742529726, perimeter: 13.0376095124
            with BuildLine():
                CenterArc((0, 0), 1.35, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.725, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 1.6512996385, perimeter: 4.5553093477
            Circle(0.725)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 3.1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.0106192983, perimeter: 5.0265482457
            Circle(0.8)
        # OneSide extrude, distance=4.5
        extrude(amount=4.5, mode=Mode.ADD)

        # Sketch5 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 7.6, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.5393804003, perimeter: 4.398229715
            Circle(0.7)
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)
    return part.part


def model_22742_3c107495_0002():
    """Model: Body v5"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 26 constraints, 12 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.0251014744, perimeter: 4.2110208849
            with BuildLine():
                Line((11.4564392374, 5), (10.4116521263, 5))
                CenterArc((0, 0), 11.55, 20.2624154646, 5.3893547604)
                Line((11.8427192823, 4), (10.8352434214, 4))
                CenterArc((0, 0), 12.5, 18.6629248849, 4.9152535933)
            make_face()
            # Profile area: 1.2931584907, perimeter: 51.83732063
            with BuildLine():
                Line((-10.3561575886, 5), (-10.4116521263, 5))
                CenterArc((0, 0), 11.5, 90, 64.2285382594)
                CenterArc((0, 0), 11.5, 25.7714617406, 64.2285382594)
                Line((10.4116521263, 5), (10.3561575886, 5))
                CenterArc((0, 0), 11.55, 25.651770225, 128.69645955)
            make_face()
            # Profile area: 1.0251014744, perimeter: 4.2110208849
            with BuildLine():
                CenterArc((0, 0), 12.5, -23.5781784782, 4.9152535933)
                Line((10.8352434214, -4), (11.8427192823, -4))
                CenterArc((0, 0), 11.55, -25.651770225, 5.3893547604)
                Line((10.4116521263, -5), (11.4564392374, -5))
            make_face()
            # Profile area: 1.0251014744, perimeter: 4.2110208849
            with BuildLine():
                Line((-11.4564392374, -5), (-10.4116521263, -5))
                CenterArc((0, 0), 11.55, -159.7375845354, 5.3893547604)
                Line((-11.8427192823, -4), (-10.8352434214, -4))
                CenterArc((0, 0), 12.5, -161.3370751151, 4.9152535933)
            make_face()
            # Profile area: 1.0251014744, perimeter: 4.2110208849
            with BuildLine():
                CenterArc((0, 0), 12.5, 156.4218215218, 4.9152535933)
                Line((-10.8352434214, 4), (-11.8427192823, 4))
                CenterArc((0, 0), 11.55, 154.348229775, 5.3893547604)
                Line((-10.4116521263, 5), (-11.4564392374, 5))
            make_face()
            # Profile area: 5.8422030671, perimeter: 13.7731834649
            with BuildLine():
                Line((-11.8427192823, 4), (-17.5, 4))
                CenterArc((0, 0), 12.5, 156.4218215218, 4.9152535933)
                Line((-11.4564392374, 5), (-17.5, 5))
                Line((-17.5, 5), (-17.5, 4))
            make_face()
            # Profile area: 0.0543421604, perimeter: 2.282497253
            with BuildLine():
                Line((-10.4116521263, -5), (-10.3561575886, -5))
                CenterArc((0, 0), 11.5, -159.6455936018, 5.4170553423)
                Line((-10.8352434214, -4), (-10.7819293264, -4))
                CenterArc((0, 0), 11.55, -159.7375845354, 5.3893547604)
            make_face()
            # Profile area: 1.2931584907, perimeter: 51.83732063
            with BuildLine():
                Line((10.3561575886, -5), (10.4116521263, -5))
                CenterArc((0, 0), 11.5, -154.2285382594, 128.4570765189)
                Line((-10.4116521263, -5), (-10.3561575886, -5))
                CenterArc((0, 0), 11.55, -154.348229775, 128.69645955)
            make_face()
            # Profile area: 26.0906727015, perimeter: 57.0149050683
            with BuildLine():
                Line((-10.4116521263, 5), (-11.4564392374, 5))
                CenterArc((0, 0), 11.55, 25.651770225, 128.69645955)
                Line((11.4564392374, 5), (10.4116521263, 5))
                CenterArc((0, 0), 12.5, 23.5781784782, 132.8436430436)
            make_face()
            # Profile area: 0.0525021838, perimeter: 2.2051877807
            with BuildLine():
                CenterArc((0, 0), 11.55, 159.7375845354, 5.2077648246)
                Line((-11.1018016556, 3), (-11.153586867, 3))
                CenterArc((0, 0), 11.5, 159.6455936018, 5.2327410833)
                Line((-10.7819293264, 4), (-10.8352434214, 4))
            make_face()
            # Profile area: 5.8422030671, perimeter: 13.7731834649
            with BuildLine():
                Line((11.8427192823, -4), (17.5, -4))
                CenterArc((0, 0), 12.5, -23.5781784782, 4.9152535933)
                Line((11.4564392374, -5), (17.5, -5))
                Line((17.5, -5), (17.5, -4))
            make_face()
            # Profile area: 0.0543421604, perimeter: 2.282497253
            with BuildLine():
                CenterArc((0, 0), 11.55, 154.348229775, 5.3893547604)
                Line((-10.7819293264, 4), (-10.8352434214, 4))
                CenterArc((0, 0), 11.5, 154.2285382594, 5.4170553423)
                Line((-10.3561575886, 5), (-10.4116521263, 5))
            make_face()
            # Profile area: 0.0543421604, perimeter: 2.282497253
            with BuildLine():
                CenterArc((0, 0), 11.55, -25.651770225, 5.3893547604)
                Line((10.7819293264, -4), (10.8352434214, -4))
                CenterArc((0, 0), 11.5, -25.7714617406, 5.4170553423)
                Line((10.3561575886, -5), (10.4116521263, -5))
            make_face()
            # Profile area: 26.0906727015, perimeter: 57.0149050683
            with BuildLine():
                Line((10.4116521263, -5), (11.4564392374, -5))
                CenterArc((0, 0), 11.55, -154.348229775, 128.69645955)
                Line((-11.4564392374, -5), (-10.4116521263, -5))
                CenterArc((0, 0), 12.5, -156.4218215218, 132.8436430436)
            make_face()
            # Profile area: 5.8422030671, perimeter: 13.7731834649
            with BuildLine():
                Line((-17.5, -4), (-17.5, -5))
                Line((-17.5, -5), (-11.4564392374, -5))
                CenterArc((0, 0), 12.5, -161.3370751151, 4.9152535933)
                Line((-17.5, -4), (-11.8427192823, -4))
            make_face()
            # Profile area: 0.0543421604, perimeter: 2.282497253
            with BuildLine():
                Line((10.4116521263, 5), (10.3561575886, 5))
                CenterArc((0, 0), 11.5, 20.3544063982, 5.4170553423)
                Line((10.8352434214, 4), (10.7819293264, 4))
                CenterArc((0, 0), 11.55, 20.2624154646, 5.3893547604)
            make_face()
            # Profile area: 0.0525021838, perimeter: 2.2051877807
            with BuildLine():
                Line((10.8352434214, 4), (10.7819293264, 4))
                CenterArc((0, 0), 11.5, 15.1216653149, 5.2327410833)
                Line((11.153586867, 3), (11.1018016556, 3))
                CenterArc((0, 0), 11.55, 15.05465064, 5.2077648246)
            make_face()
            # Profile area: 5.8422030671, perimeter: 13.7731834649
            with BuildLine():
                CenterArc((0, 0), 12.5, 18.6629248849, 4.9152535933)
                Line((17.5, 4), (11.8427192823, 4))
                Line((17.5, 4), (17.5, 5))
                Line((17.5, 5), (11.4564392374, 5))
            make_face()
        # OneSide extrude, distance=4
        extrude(amount=4)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 26 constraints, 12 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.0251014744, perimeter: 4.2110208849
            with BuildLine():
                Line((11.4564392374, 5), (10.4116521263, 5))
                CenterArc((0, 0), 11.55, 20.2624154646, 5.3893547604)
                Line((11.8427192823, 4), (10.8352434214, 4))
                CenterArc((0, 0), 12.5, 18.6629248849, 4.9152535933)
            make_face()
            # Profile area: 1.2931584907, perimeter: 51.83732063
            with BuildLine():
                Line((-10.3561575886, 5), (-10.4116521263, 5))
                CenterArc((0, 0), 11.5, 90, 64.2285382594)
                CenterArc((0, 0), 11.5, 25.7714617406, 64.2285382594)
                Line((10.4116521263, 5), (10.3561575886, 5))
                CenterArc((0, 0), 11.55, 25.651770225, 128.69645955)
            make_face()
            # Profile area: 1.0251014744, perimeter: 4.2110208849
            with BuildLine():
                CenterArc((0, 0), 12.5, -23.5781784782, 4.9152535933)
                Line((10.8352434214, -4), (11.8427192823, -4))
                CenterArc((0, 0), 11.55, -25.651770225, 5.3893547604)
                Line((10.4116521263, -5), (11.4564392374, -5))
            make_face()
            # Profile area: 1.0251014744, perimeter: 4.2110208849
            with BuildLine():
                Line((-11.4564392374, -5), (-10.4116521263, -5))
                CenterArc((0, 0), 11.55, -159.7375845354, 5.3893547604)
                Line((-11.8427192823, -4), (-10.8352434214, -4))
                CenterArc((0, 0), 12.5, -161.3370751151, 4.9152535933)
            make_face()
            # Profile area: 1.0251014744, perimeter: 4.2110208849
            with BuildLine():
                CenterArc((0, 0), 12.5, 156.4218215218, 4.9152535933)
                Line((-10.8352434214, 4), (-11.8427192823, 4))
                CenterArc((0, 0), 11.55, 154.348229775, 5.3893547604)
                Line((-10.4116521263, 5), (-11.4564392374, 5))
            make_face()
            # Profile area: 5.5037690021, perimeter: 13.0646650714
            with BuildLine():
                Line((12.1346610995, -3), (17.5, -3))
                CenterArc((0, 0), 12.5, -18.6629248849, 4.7763845223)
                Line((11.8427192823, -4), (17.5, -4))
                Line((17.5, -4), (17.5, -3))
            make_face()
            # Profile area: 6.6276574294, perimeter: 16.7284198227
            with BuildLine():
                Line((-10.3561575886, -5), (-2.8722813233, -5))
                CenterArc((0, 3), 8.5, -124.56032178, 14.8103989844)
                Line((-10.7819293264, -4), (-4.8218253805, -4))
                CenterArc((0, 0), 11.5, -159.6455936018, 5.4170553423)
            make_face()
            # Profile area: 5.8422030671, perimeter: 13.7731834649
            with BuildLine():
                Line((-11.8427192823, 4), (-17.5, 4))
                CenterArc((0, 0), 12.5, 156.4218215218, 4.9152535933)
                Line((-11.4564392374, 5), (-17.5, 5))
                Line((-17.5, 5), (-17.5, 4))
            make_face()
            # Profile area: 0.0543421604, perimeter: 2.282497253
            with BuildLine():
                Line((-10.4116521263, -5), (-10.3561575886, -5))
                CenterArc((0, 0), 11.5, -159.6455936018, 5.4170553423)
                Line((-10.8352434214, -4), (-10.7819293264, -4))
                CenterArc((0, 0), 11.55, -159.7375845354, 5.3893547604)
            make_face()
            # Profile area: 1.2931584907, perimeter: 51.83732063
            with BuildLine():
                Line((10.3561575886, -5), (10.4116521263, -5))
                CenterArc((0, 0), 11.5, -154.2285382594, 128.4570765189)
                Line((-10.4116521263, -5), (-10.3561575886, -5))
                CenterArc((0, 0), 11.55, -154.348229775, 128.69645955)
            make_face()
            # Profile area: 5.5037690021, perimeter: 13.0646650714
            with BuildLine():
                Line((-12.1346610995, 3), (-17.5, 3))
                CenterArc((0, 0), 12.5, 161.3370751151, 4.7763845223)
                Line((-11.8427192823, 4), (-17.5, 4))
                Line((-17.5, 4), (-17.5, 3))
            make_face()
            # Profile area: 8.3324865522, perimeter: 26.3191344571
            with BuildLine():
                Line((-8.2613558209, 5), (-10.3561575886, 5))
                CenterArc((0, 3), 8.5, 90, 76.3910393692)
                CenterArc((0, 0), 11.5, 90, 64.2285382594)
            make_face()
            # Profile area: 2.2168964287, perimeter: 6.5396409375
            with BuildLine():
                Line((10.3561575886, 5), (8.2613558209, 5))
                CenterArc((0, 3), 8.5, 6.7563270306, 6.8526336002)
                Line((10.7819293264, 4), (8.4409715081, 4))
                CenterArc((0, 0), 11.5, 20.3544063982, 5.4170553423)
            make_face()
            # Profile area: 8.3324865522, perimeter: 26.3191344571
            with BuildLine():
                CenterArc((0, 3), 8.5, 13.6089606308, 76.3910393692)
                Line((10.3561575886, 5), (8.2613558209, 5))
                CenterArc((0, 0), 11.5, 25.7714617406, 64.2285382594)
            make_face()
            # Profile area: 2.2168964287, perimeter: 6.5396409375
            with BuildLine():
                CenterArc((0, 0), 11.5, 154.2285382594, 5.4170553423)
                Line((-8.4409715081, 4), (-10.7819293264, 4))
                CenterArc((0, 3), 8.5, 166.3910393692, 6.8526336002)
                Line((-8.2613558209, 5), (-10.3561575886, 5))
            make_face()
            # Profile area: 26.0906727015, perimeter: 57.0149050683
            with BuildLine():
                Line((-10.4116521263, 5), (-11.4564392374, 5))
                CenterArc((0, 0), 11.55, 25.651770225, 128.69645955)
                Line((11.4564392374, 5), (10.4116521263, 5))
                CenterArc((0, 0), 12.5, 23.5781784782, 132.8436430436)
            make_face()
            # Profile area: 1.9264096543, perimeter: 11.6044827031
            with BuildLine():
                Line((-2.8722813233, -5), (2.8722813233, -5))
                CenterArc((0, 3), 8.5, -109.7499227956, 39.4998455913)
            make_face()
            # Profile area: 5.5037690021, perimeter: 13.0646650714
            with BuildLine():
                Line((-17.5, -4), (-11.8427192823, -4))
                CenterArc((0, 0), 12.5, -166.1134596374, 4.7763845223)
                Line((-17.5, -3), (-12.1346610995, -3))
                Line((-17.5, -3), (-17.5, -4))
            make_face()
            # Profile area: 94.5449818302, perimeter: 46.6106603138
            with BuildLine():
                Line((2.8722813233, -5), (10.3561575886, -5))
                CenterArc((0, 3), 8.5, -109.7499227956, 39.4998455913)
                Line((-10.3561575886, -5), (-2.8722813233, -5))
                CenterArc((0, 0), 11.5, -154.2285382594, 128.4570765189)
            make_face()
            # Profile area: 5.7609503038, perimeter: 14.0908941554
            with BuildLine():
                Line((-12.1346610995, -3), (-11.153586867, -3))
                CenterArc((0, 0), 11.55, 164.94534936, 30.10930128)
                Line((-11.153586867, 3), (-12.1346610995, 3))
                CenterArc((0, 0), 12.5, 166.1134596374, 27.7730807253)
            make_face()
            # Profile area: 5.8422030671, perimeter: 13.7731834649
            with BuildLine():
                Line((11.8427192823, -4), (17.5, -4))
                CenterArc((0, 0), 12.5, -23.5781784782, 4.9152535933)
                Line((11.4564392374, -5), (17.5, -5))
                Line((17.5, -5), (17.5, -4))
            make_face()
            # Profile area: 0.0543421604, perimeter: 2.282497253
            with BuildLine():
                CenterArc((0, 0), 11.55, 154.348229775, 5.3893547604)
                Line((-10.7819293264, 4), (-10.8352434214, 4))
                CenterArc((0, 0), 11.5, 154.2285382594, 5.4170553423)
                Line((-10.3561575886, 5), (-10.4116521263, 5))
            make_face()
            # Profile area: 0.0543421604, perimeter: 2.282497253
            with BuildLine():
                CenterArc((0, 0), 11.55, -25.651770225, 5.3893547604)
                Line((10.7819293264, -4), (10.8352434214, -4))
                CenterArc((0, 0), 11.5, -25.7714617406, 5.4170553423)
                Line((10.3561575886, -5), (10.4116521263, -5))
            make_face()
            # Profile area: 26.0906727015, perimeter: 57.0149050683
            with BuildLine():
                Line((10.4116521263, -5), (11.4564392374, -5))
                CenterArc((0, 0), 11.55, -154.348229775, 128.69645955)
                Line((-11.4564392374, -5), (-10.4116521263, -5))
                CenterArc((0, 0), 12.5, -156.4218215218, 132.8436430436)
            make_face()
            # Profile area: 0.9934715612, perimeter: 4.0804055717
            with BuildLine():
                Line((11.153586867, -3), (12.1346610995, -3))
                CenterArc((0, 0), 11.55, -20.2624154646, 5.2077648246)
                Line((10.8352434214, -4), (11.8427192823, -4))
                CenterArc((0, 0), 12.5, -18.6629248849, 4.7763845223)
            make_face()
            # Profile area: 0.9934715612, perimeter: 4.0804055717
            with BuildLine():
                CenterArc((0, 0), 11.55, 15.05465064, 5.2077648246)
                Line((12.1346610995, 3), (11.153586867, 3))
                CenterArc((0, 0), 12.5, 13.8865403626, 4.7763845223)
                Line((11.8427192823, 4), (10.8352434214, 4))
            make_face()
            # Profile area: 16.4674432564, perimeter: 35.5466247488
            with BuildLine():
                CenterArc((0, 3), 8.5, 166.3910393692, 6.8526336002)
                Line((-0.75, 4), (-8.4409715081, 4))
                CenterArc((0, 3), 1.25, 53.1301023542, 73.7397952917)
                Line((8.4409715081, 4), (0.75, 4))
                CenterArc((0, 3), 8.5, 6.7563270306, 6.8526336002)
                Line((8.2613558209, 5), (-8.2613558209, 5))
            make_face()
            # Profile area: 5.5037690021, perimeter: 13.0646650714
            with BuildLine():
                Line((17.5, 4), (11.8427192823, 4))
                CenterArc((0, 0), 12.5, 13.8865403626, 4.7763845223)
                Line((17.5, 3), (12.1346610995, 3))
                Line((17.5, 3), (17.5, 4))
            make_face()
            # Profile area: 5.7609503038, perimeter: 14.0908941554
            with BuildLine():
                Line((12.1346610995, 3), (11.153586867, 3))
                CenterArc((0, 0), 11.55, -15.05465064, 30.10930128)
                Line((11.153586867, -3), (12.1346610995, -3))
                CenterArc((0, 0), 12.5, -13.8865403626, 27.7730807253)
            make_face()
            # Profile area: 30.7263524766, perimeter: 22.789824077
            with BuildLine():
                Line((-17.5, -3), (-12.1346610995, -3))
                CenterArc((0, 0), 12.5, 166.1134596374, 27.7730807253)
                Line((-12.1346610995, 3), (-17.5, 3))
                Line((-17.5, 3), (-17.5, -3))
            make_face()
            # Profile area: 0.9934715612, perimeter: 4.0804055717
            with BuildLine():
                Line((-11.8427192823, -4), (-10.8352434214, -4))
                CenterArc((0, 0), 11.55, -164.94534936, 5.2077648246)
                Line((-12.1346610995, -3), (-11.153586867, -3))
                CenterArc((0, 0), 12.5, -166.1134596374, 4.7763845223)
            make_face()
            # Profile area: 79.8064183801, perimeter: 39.1883892941
            with BuildLine():
                CenterArc((0, 3), 8.5, 90, 76.3910393692)
                Line((8.2613558209, 5), (-8.2613558209, 5))
                CenterArc((0, 3), 8.5, 13.6089606308, 76.3910393692)
            make_face()
            # Profile area: 6.6276574294, perimeter: 16.7284198227
            with BuildLine():
                CenterArc((0, 0), 11.5, -25.7714617406, 5.4170553423)
                Line((4.8218253805, -4), (10.7819293264, -4))
                CenterArc((0, 3), 8.5, -70.2500772044, 14.8103989844)
                Line((2.8722813233, -5), (10.3561575886, -5))
            make_face()
            # Profile area: 30.7263524766, perimeter: 22.789824077
            with BuildLine():
                Line((17.5, 3), (12.1346610995, 3))
                CenterArc((0, 0), 12.5, -13.8865403626, 27.7730807253)
                Line((12.1346610995, -3), (17.5, -3))
                Line((17.5, -3), (17.5, 3))
            make_face()
            # Profile area: 5.8422030671, perimeter: 13.7731834649
            with BuildLine():
                Line((-17.5, -4), (-17.5, -5))
                Line((-17.5, -5), (-11.4564392374, -5))
                CenterArc((0, 0), 12.5, -161.3370751151, 4.9152535933)
                Line((-17.5, -4), (-11.8427192823, -4))
            make_face()
            # Profile area: 0.0543421604, perimeter: 2.282497253
            with BuildLine():
                Line((10.4116521263, 5), (10.3561575886, 5))
                CenterArc((0, 0), 11.5, 20.3544063982, 5.4170553423)
                Line((10.8352434214, 4), (10.7819293264, 4))
                CenterArc((0, 0), 11.55, 20.2624154646, 5.3893547604)
            make_face()
            # Profile area: 0.9934715612, perimeter: 4.0804055717
            with BuildLine():
                Line((-11.153586867, 3), (-12.1346610995, 3))
                CenterArc((0, 0), 11.55, 159.7375845354, 5.2077648246)
                Line((-10.8352434214, 4), (-11.8427192823, 4))
                CenterArc((0, 0), 12.5, 161.3370751151, 4.7763845223)
            make_face()
            # Profile area: 5.8422030671, perimeter: 13.7731834649
            with BuildLine():
                CenterArc((0, 0), 12.5, 18.6629248849, 4.9152535933)
                Line((17.5, 4), (11.8427192823, 4))
                Line((17.5, 4), (17.5, 5))
                Line((17.5, 5), (11.4564392374, 5))
            make_face()
            # Profile area: 7.9013917375, perimeter: 19.7825472463
            with BuildLine():
                CenterArc((0, 3), 8.5, -70.2500772044, 14.8103989844)
                Line((-4.8218253805, -4), (4.8218253805, -4))
                CenterArc((0, 3), 8.5, -124.56032178, 14.8103989844)
                Line((-2.8722813233, -5), (2.8722813233, -5))
            make_face()
            # Profile area: 5.4915410396, perimeter: 13.6548501143
            with BuildLine():
                Line((-10.7819293264, -4), (-4.8218253805, -4))
                CenterArc((0, 3), 8.5, -135.099127844, 10.538806064)
                Line((-11.1018016556, -3), (-6.0207972894, -3))
                CenterArc((0, 0), 11.5, -164.8783346851, 5.2327410833)
            make_face()
            # Profile area: 10.9174324267, perimeter: 24.8121720456
            with BuildLine():
                CenterArc((0, 3), 8.5, -135.099127844, 10.538806064)
                Line((-4.8218253805, -4), (4.8218253805, -4))
                CenterArc((0, 3), 8.5, -55.43967822, 10.538806064)
                Line((-6.0207972894, -3), (6.0207972894, -3))
            make_face()
            # Profile area: 5.4915410396, perimeter: 13.6548501143
            with BuildLine():
                CenterArc((0, 0), 11.5, -20.3544063982, 5.2327410833)
                Line((6.0207972894, -3), (11.1018016556, -3))
                CenterArc((0, 3), 8.5, -55.43967822, 10.538806064)
                Line((4.8218253805, -4), (10.7819293264, -4))
            make_face()
            # Profile area: 0.0525021838, perimeter: 2.2051877807
            with BuildLine():
                CenterArc((0, 0), 11.55, -20.2624154646, 5.2077648246)
                Line((11.1018016556, -3), (11.153586867, -3))
                CenterArc((0, 0), 11.5, -20.3544063982, 5.2327410833)
                Line((10.7819293264, -4), (10.8352434214, -4))
            make_face()
            # Profile area: 0.3034955876, perimeter: 12.2433953443
            with BuildLine():
                Line((11.153586867, 3), (11.1018016556, 3))
                CenterArc((0, 0), 11.5, -15.1216653149, 30.2433306298)
                Line((11.1018016556, -3), (11.153586867, -3))
                CenterArc((0, 0), 11.55, -15.05465064, 30.10930128)
            make_face()
            # Profile area: 0.0525021838, perimeter: 2.2051877807
            with BuildLine():
                Line((10.8352434214, 4), (10.7819293264, 4))
                CenterArc((0, 0), 11.5, 15.1216653149, 5.2327410833)
                Line((11.153586867, 3), (11.1018016556, 3))
                CenterArc((0, 0), 11.55, 15.05465064, 5.2077648246)
            make_face()
            # Profile area: 2.469906007, perimeter: 6.9953592155
            with BuildLine():
                Line((10.7819293264, 4), (8.4409715081, 4))
                CenterArc((0, 3), 8.5, 0, 6.7563270306)
                Line((11.1018016556, 3), (8.5, 3))
                CenterArc((0, 0), 11.5, 15.1216653149, 5.2327410833)
            make_face()
            # Profile area: 7.3809018569, perimeter: 17.1024118228
            with BuildLine():
                Line((8.4409715081, 4), (0.75, 4))
                CenterArc((0, 3), 1.25, 0, 53.1301023542)
                Line((8.5, 3), (1.25, 3))
                CenterArc((0, 3), 8.5, 0, 6.7563270306)
            make_face()
            # Profile area: 2.1988987781, perimeter: 6.318238045
            with BuildLine():
                CenterArc((0, 3), 1.25, 126.8698976458, 53.1301023542)
                Line((1.25, 3), (-1.25, 3))
                CenterArc((0, 3), 1.25, 0, 53.1301023542)
                Line((0.75, 4), (-0.75, 4))
            make_face()
            # Profile area: 7.3809018569, perimeter: 17.1024118228
            with BuildLine():
                CenterArc((0, 3), 8.5, 173.2436729694, 6.7563270306)
                Line((-1.25, 3), (-8.5, 3))
                CenterArc((0, 3), 1.25, 126.8698976458, 53.1301023542)
                Line((-0.75, 4), (-8.4409715081, 4))
            make_face()
            # Profile area: 2.469906007, perimeter: 6.9953592155
            with BuildLine():
                CenterArc((0, 0), 11.5, 159.6455936018, 5.2327410833)
                Line((-8.5, 3), (-11.1018016556, 3))
                CenterArc((0, 3), 8.5, 173.2436729694, 6.7563270306)
                Line((-8.4409715081, 4), (-10.7819293264, 4))
            make_face()
            # Profile area: 0.0525021838, perimeter: 2.2051877807
            with BuildLine():
                CenterArc((0, 0), 11.55, 159.7375845354, 5.2077648246)
                Line((-11.1018016556, 3), (-11.153586867, 3))
                CenterArc((0, 0), 11.5, 159.6455936018, 5.2327410833)
                Line((-10.7819293264, 4), (-10.8352434214, 4))
            make_face()
            # Profile area: 0.3034955876, perimeter: 12.2433953443
            with BuildLine():
                Line((-11.153586867, -3), (-11.1018016556, -3))
                CenterArc((0, 0), 11.5, 164.8783346851, 30.2433306298)
                Line((-11.1018016556, 3), (-11.153586867, 3))
                CenterArc((0, 0), 11.55, 164.94534936, 30.10930128)
            make_face()
            # Profile area: 0.0525021838, perimeter: 2.2051877807
            with BuildLine():
                Line((-10.8352434214, -4), (-10.7819293264, -4))
                CenterArc((0, 0), 11.5, -164.8783346851, 5.2327410833)
                Line((-11.153586867, -3), (-11.1018016556, -3))
                CenterArc((0, 0), 11.55, -164.94534936, 5.2077648246)
            make_face()
            # Profile area: 21.8368012357, perimeter: 20.4142100059
            with BuildLine():
                CenterArc((0, 0), 11.5, 164.8783346851, 30.2433306298)
                Line((-11.1018016556, -3), (-6.0207972894, -3))
                CenterArc((0, 3), 8.5, -180, 44.900872156)
                Line((-8.5, 3), (-11.1018016556, 3))
            make_face()
            # Profile area: 90.2904315318, perimeter: 43.7909423501
            with BuildLine():
                CenterArc((0, 3), 8.5, -180, 44.900872156)
                Line((-6.0207972894, -3), (6.0207972894, -3))
                CenterArc((0, 3), 8.5, -44.900872156, 44.900872156)
                Line((8.5, 3), (1.25, 3))
                CenterArc((0, 3), 1.25, 180, 180)
                Line((-1.25, 3), (-8.5, 3))
            make_face()
            # Profile area: 21.8368012357, perimeter: 20.4142100059
            with BuildLine():
                Line((11.1018016556, 3), (8.5, 3))
                CenterArc((0, 3), 8.5, -44.900872156, 44.900872156)
                Line((6.0207972894, -3), (11.1018016556, -3))
                CenterArc((0, 0), 11.5, -15.1216653149, 30.2433306298)
            make_face()
            # Profile area: 2.4543692606, perimeter: 6.426990817
            with BuildLine():
                CenterArc((0, 3), 1.25, 180, 180)
                Line((1.25, 3), (-1.25, 3))
            make_face()
            # Profile area: 0.2554704825, perimeter: 3.108752772
            with BuildLine():
                Line((0.75, 4), (-0.75, 4))
                CenterArc((0, 3), 1.25, 53.1301023542, 73.7397952917)
            make_face()
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.ADD)

        # Sketch1 -> Extrude3 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 26 constraints, 12 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.9264096543, perimeter: 11.6044827031
            with BuildLine():
                Line((-2.8722813233, -5), (2.8722813233, -5))
                CenterArc((0, 3), 8.5, -109.7499227956, 39.4998455913)
            make_face()
            # Profile area: 10.9174324267, perimeter: 24.8121720456
            with BuildLine():
                CenterArc((0, 3), 8.5, -135.099127844, 10.538806064)
                Line((-4.8218253805, -4), (4.8218253805, -4))
                CenterArc((0, 3), 8.5, -55.43967822, 10.538806064)
                Line((-6.0207972894, -3), (6.0207972894, -3))
            make_face()
            # Profile area: 7.3809018569, perimeter: 17.1024118228
            with BuildLine():
                Line((8.4409715081, 4), (0.75, 4))
                CenterArc((0, 3), 1.25, 0, 53.1301023542)
                Line((8.5, 3), (1.25, 3))
                CenterArc((0, 3), 8.5, 0, 6.7563270306)
            make_face()
            # Profile area: 16.4674432564, perimeter: 35.5466247488
            with BuildLine():
                CenterArc((0, 3), 8.5, 166.3910393692, 6.8526336002)
                Line((-0.75, 4), (-8.4409715081, 4))
                CenterArc((0, 3), 1.25, 53.1301023542, 73.7397952917)
                Line((8.4409715081, 4), (0.75, 4))
                CenterArc((0, 3), 8.5, 6.7563270306, 6.8526336002)
                Line((8.2613558209, 5), (-8.2613558209, 5))
            make_face()
            # Profile area: 7.3809018569, perimeter: 17.1024118228
            with BuildLine():
                CenterArc((0, 3), 8.5, 173.2436729694, 6.7563270306)
                Line((-1.25, 3), (-8.5, 3))
                CenterArc((0, 3), 1.25, 126.8698976458, 53.1301023542)
                Line((-0.75, 4), (-8.4409715081, 4))
            make_face()
            # Profile area: 79.8064183801, perimeter: 39.1883892941
            with BuildLine():
                CenterArc((0, 3), 8.5, 90, 76.3910393692)
                Line((8.2613558209, 5), (-8.2613558209, 5))
                CenterArc((0, 3), 8.5, 13.6089606308, 76.3910393692)
            make_face()
            # Profile area: 90.2904315318, perimeter: 43.7909423501
            with BuildLine():
                CenterArc((0, 3), 8.5, -180, 44.900872156)
                Line((-6.0207972894, -3), (6.0207972894, -3))
                CenterArc((0, 3), 8.5, -44.900872156, 44.900872156)
                Line((8.5, 3), (1.25, 3))
                CenterArc((0, 3), 1.25, 180, 180)
                Line((-1.25, 3), (-8.5, 3))
            make_face()
            # Profile area: 7.9013917375, perimeter: 19.7825472463
            with BuildLine():
                CenterArc((0, 3), 8.5, -70.2500772044, 14.8103989844)
                Line((-4.8218253805, -4), (4.8218253805, -4))
                CenterArc((0, 3), 8.5, -124.56032178, 14.8103989844)
                Line((-2.8722813233, -5), (2.8722813233, -5))
            make_face()
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.SUBTRACT)

        # Sketch1 -> Extrude4 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 26 constraints, 12 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2554704825, perimeter: 3.108752772
            with BuildLine():
                Line((0.75, 4), (-0.75, 4))
                CenterArc((0, 3), 1.25, 53.1301023542, 73.7397952917)
            make_face()
            # Profile area: 2.4543692606, perimeter: 6.426990817
            with BuildLine():
                CenterArc((0, 3), 1.25, 180, 180)
                Line((1.25, 3), (-1.25, 3))
            make_face()
            # Profile area: 2.1988987781, perimeter: 6.318238045
            with BuildLine():
                CenterArc((0, 3), 1.25, 126.8698976458, 53.1301023542)
                Line((1.25, 3), (-1.25, 3))
                CenterArc((0, 3), 1.25, 0, 53.1301023542)
                Line((0.75, 4), (-0.75, 4))
            make_face()
        # OneSide extrude, distance=-2
        extrude(amount=-2, mode=Mode.SUBTRACT)

        # Sketch2 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -1, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 263.8937829015, perimeter: 131.9468914508
            with BuildLine():
                CenterArc((0, 0), 12.5, 156.4218215218, 47.1563569564)
                CenterArc((0, 0), 12.5, -156.4218215218, 132.8436430436)
                CenterArc((0, 0), 12.5, -23.5781784782, 47.1563569564)
                CenterArc((0, 0), 12.5, 23.5781784782, 132.8436430436)
            make_face()
            with BuildLine():
                CenterArc((0, -3), 8.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 226.9800692219, perimeter: 53.407075111
            with Locations((0, -3)):
                Circle(8.5)
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)

        # Sketch1 -> Extrude6 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 26 constraints, 12 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2554704825, perimeter: 3.108752772
            with BuildLine():
                Line((0.75, 4), (-0.75, 4))
                CenterArc((0, 3), 1.25, 53.1301023542, 73.7397952917)
            make_face()
            # Profile area: 2.4543692606, perimeter: 6.426990817
            with BuildLine():
                CenterArc((0, 3), 1.25, 180, 180)
                Line((1.25, 3), (-1.25, 3))
            make_face()
            # Profile area: 2.1988987781, perimeter: 6.318238045
            with BuildLine():
                CenterArc((0, 3), 1.25, 126.8698976458, 53.1301023542)
                Line((1.25, 3), (-1.25, 3))
                CenterArc((0, 3), 1.25, 0, 53.1301023542)
                Line((0.75, 4), (-0.75, 4))
            make_face()
        # OneSide extrude, distance=-2
        extrude(amount=-2, mode=Mode.SUBTRACT)
    return part.part


def model_22760_c2a5214f_0010():
    """Model: hanger v12"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 4 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 3.0422187715, perimeter: 6.6585004094
            with BuildLine():
                CenterArc((0, 0), 1.25, 43.2810120024, 93.4379759952)
                Line((-0.91, 0.8569714114), (-0.91, -0.5430285886))
                Line((-0.91, -0.5430285886), (0.91, -0.5430285886))
                Line((0.91, -0.5430285886), (0.91, 0.8569714114))
            make_face()
        # TwoSides extrude (symmetric), distance=9
        extrude(amount=9, both=True)

        # Sketch3 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(9, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            with Locations((0, 0.2569714114)):
                Circle(0.4)
        # OneSide extrude, distance=3.7
        extrude(amount=3.7, mode=Mode.ADD)

        # Sketch4 -> Extrude3 (Join)
        # Sketch on XY construction plane
        # Sketch has 14 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 4.1233403578, perimeter: 10.9955742876
            with BuildLine():
                CenterArc((0, -2.0430285886), 1.25, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, -2.0430285886), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 11.9441768806, perimeter: 24.1412788079
            with BuildLine():
                Line((-2.5, -0.5430285886), (2.5, -0.5430285886))
                CenterArc((6.0941467849, 0.2088618278), 8.6269750295, -175, 32.5010110143)
                Line((0.75, -5.0430285886), (-0.75, -5.0430285886))
                CenterArc((-6.0941467849, 0.2088618278), 8.6269750295, -37.5010110143, 32.5010110143)
            make_face()
            with BuildLine():
                CenterArc((0, -2.0430285886), 1.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # TwoSides extrude (symmetric), distance=0.7
        extrude(amount=0.7, both=True, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on XY construction plane
        # Sketch has 14 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY) as sk:
            # Profile area: 4.1233403578, perimeter: 10.9955742876
            with BuildLine():
                CenterArc((0, -2.0430285886), 1.25, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, -2.0430285886), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # TwoSides offset extrude, full=0.7, trim=0.45
        extrude(amount=0.7, mode=Mode.SUBTRACT)
        extrude(sk.sketch, amount=0.45, mode=Mode.ADD)

        # Sketch4 -> Extrude5 (Cut)
        # Sketch on XY construction plane
        # Sketch has 14 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY) as sk:
            # Profile area: 4.1233403578, perimeter: 10.9955742876
            with BuildLine():
                CenterArc((0, -2.0430285886), 1.25, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, -2.0430285886), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # TwoSides offset extrude, full=-0.7, trim=-0.45
        extrude(amount=-0.7, mode=Mode.SUBTRACT)
        extrude(sk.sketch, amount=-0.45, mode=Mode.ADD)

        # Sketch5 -> Extrude6 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -5.0430285886, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            Circle(0.5)
        # OneSide extrude, distance=1.2
        extrude(amount=1.2, mode=Mode.ADD)
    return part.part


def model_22764_b884dce6_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 25 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 120.029779568, perimeter: 140.2980210539
            with BuildLine():
                Line((-13, 6.9062863695), (0, -6.0937136305))
                Line((0, -6.0937136305), (0, -3))
                CenterArc((0, 2), 5, -169.7484474721, 79.7484474721)
                Line((-5.0306460229, 1.2204780813), (-4.920179378, 1.1101489516))
                Line((-12.9958281657, 9.1757447095), (-5.0306460229, 1.2204780813))
                Line((-9.1715728753, 13), (-12.9958281657, 9.1757447095))
                Line((-5.8284271247, 13), (-9.1715728753, 13))
                Line((0.0091450935, 7.1624277817), (-5.8284271247, 13))
                Line((0.0091450935, 7.1624277817), (0.1407784683, 6.9980177494))
                CenterArc((0, 2), 5, 38.682146014, 49.7044383516)
                Line((0, 10), (3.9031260092, 5.124997177))
                Line((0, 10), (-5, 15))
                Line((-5, 15), (-10, 15))
                Line((-10, 15), (-15, 10))
                Line((-15, 10), (-15, 2.5))
                Line((-15, 2.5), (0, -12.5))
                Line((0, -12.5), (0, -9.6715728753))
                Line((-13, 3.3284271247), (0, -9.6715728753))
                Line((-13, 6.9062863695), (-13, 3.3284271247))
            make_face()
            # Profile area: 231.3134067574, perimeter: 74.8299763564
            with BuildLine():
                Line((0, -9.6715728753), (0, -6.0937136305))
                Line((0, -12.5), (0, -9.6715728753))
                Line((0, -12.5), (15, 2.5))
                Line((15, 2.5), (15, 10))
                Line((15, 10), (10, 15))
                Line((10, 15), (5, 15))
                Line((5, 15), (0, 10))
                Line((0, 10), (3.9031260092, 5.124997177))
                CenterArc((0, 2), 5, -90, 128.682146014)
                Line((0, -6.0937136305), (0, -3))
            make_face()
            # Profile area: 73.6038850391, perimeter: 37.4827574185
            with BuildLine():
                Line((-5.0306460229, 1.2204780813), (-4.9238897715, 1.1309145506))
                CenterArc((0, 2), 5, 88.3865843656, 101.6232430375)
                Line((0.0091450935, 7.1624277817), (0.1407784683, 6.9980177494))
                Line((0.0091450935, 7.1624277817), (-5.8284271247, 13))
                Line((-5.8284271247, 13), (-9.1715728753, 13))
                Line((-9.1715728753, 13), (-12.9958281657, 9.1757447095))
                Line((-12.9958281657, 9.1757447095), (-5.0306460229, 1.2204780813))
            make_face()
            # Profile area: 46.5121701814, perimeter: 43.9252711112
            with BuildLine():
                Line((-13, 6.9062863695), (-13, 3.3284271247))
                Line((-13, 3.3284271247), (0, -9.6715728753))
                Line((0, -9.6715728753), (0, -6.0937136305))
                Line((-13, 6.9062863695), (0, -6.0937136305))
            make_face()
        # OneSide extrude, distance=-7
        extrude(amount=-7)

        # Sketch4 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 8 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 73.9427959558, perimeter: 69.2889075686
            with BuildLine():
                Line((15, 5.7950486884), (15, 10))
                Line((15, 2.5), (15, 5.7950486884))
                Line((12.6700487117, 0.1700487117), (15, 2.5))
                Line((17.8221309005, 0), (12.6700487117, 0.1700487117))
                Line((17.8221309005, 15.6115270897), (17.8221309005, 0))
                Line((1.4200487117, 15.6115270897), (17.8221309005, 15.6115270897))
                Line((1.4200487117, 11.4200487117), (1.4200487117, 15.6115270897))
                Line((5, 15), (1.4200487117, 11.4200487117))
                Line((10, 15), (5, 15))
                Line((15, 10), (10, 15))
            make_face()
            # Profile area: 15.7229857027, perimeter: 40.0822472067
            with BuildLine():
                Line((15, 10), (10, 15))
                Line((10, 15), (5, 15))
                Line((5, 15), (1.4200487117, 11.4200487117))
                CenterArc((7.0450487117, 5.7950487117), 7.9549512883, -0.0000001676, 135.0000001676)
                Line((15, 5.7950486884), (15, 10))
            make_face()
            # Profile area: 1.3614632302, perimeter: 12.8379015085
            with BuildLine():
                CenterArc((7.0450487117, 5.7950487117), 7.9549512883, -45, 44.9999998324)
                Line((12.6700487117, 0.1700487117), (15, 2.5))
                Line((15, 2.5), (15, 5.7950486884))
            make_face()
        # OneSide extrude, distance=-8
        extrude(amount=-8, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude4 (Cut)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 218.6456419924, perimeter: 73.1255865477
            with BuildLine():
                Line((0, 10), (0, 7))
                CenterArc((0, 2), 5, -90, 180)
                Line((0, -3), (0, -12.5))
                Line((0, -12.5), (12.6700487117, 0.1700487117))
                CenterArc((7.0450487117, 5.7950487117), 7.9549512883, -45, 179.9999991462)
                Line((1.4200487117, 11.4200487117), (0, 10))
            make_face()
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.SUBTRACT)

        # Sketch6 -> Extrude5 (Cut)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 235.7291497158, perimeter: 76.3376844119
            with BuildLine():
                Line((-4.920179378, 1.1101489516), (-5.0306460229, 1.2204780813))
                Line((-5.0306460229, 1.2204780813), (-4.9238897715, 1.1309145506))
                CenterArc((0, 2), 5, 90, 100.0098274031)
                Line((0, 7), (0, 10))
                Line((0, 10), (-5, 15))
                Line((-5, 15), (-10, 15))
                Line((-10, 15), (-15, 10))
                Line((-15, 10), (-15, 2.5))
                Line((-15, 2.5), (0, -12.5))
                Line((0, -12.5), (0, -3))
                CenterArc((0, 2), 5, -169.7484474721, 79.7484474721)
            make_face()
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.SUBTRACT)

        # Sketch7 -> Extrude6 (NewBody)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -1, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.6054052988, perimeter: 3.6011405328
            with BuildLine():
                Line((1.4200485931, 11.4200485931), (1.1977760357, 12.5992834765))
                CenterArc((7.0450487117, 5.7950487117), 7.9549512883, 126.3487486429, 8.6512513571)
                Line((1.1977760357, 12.5992834765), (2.3301596804, 12.2021597161))
            make_face()
        # OneSide extrude, distance=-6
        extrude(amount=-6)
    return part.part


def model_22772_2b5f6629_0001():
    """Model: Spur Gear 1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 27.3397100679, perimeter: 18.5353966562
            Circle(2.95)
        # OneSide extrude, distance=1.6
        extrude(amount=1.6)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 9 constraints, 9 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.6, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0161229959, perimeter: 0.6243211012
            with BuildLine():
                CenterArc((0.6537, -2.6187), 0.6253, -170.2547642885, 21.9769978475)
                CenterArc((0, 0), 2.7248, -90, 0.7869373796)
                Line((0, -2.95), (0, -2.7248))
                CenterArc((0, 0), 2.95, -90, 2.3666070809)
            make_face()
            # Profile area: 0.0161229959, perimeter: 0.6243211012
            with BuildLine():
                CenterArc((0, 0), 2.95, -92.3666070809, 2.3666070809)
                Line((0, -2.95), (0, -2.7248))
                CenterArc((0, 0), 2.7248, -90.7869373796, 0.7869373796)
                CenterArc((-0.6537, -2.6187), 0.6253, -31.722233559, 21.9769978475)
            make_face()
        # OneSide extrude, distance=-2
        extrude(amount=-2, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.6, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 6.157521601, perimeter: 8.7964594301
            Circle(1.4)
        # OneSide extrude, distance=1.6
        extrude(amount=1.6, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 3.2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.5393804003, perimeter: 4.398229715
            Circle(0.7)
        # OneSide extrude, distance=-6
        extrude(amount=-6, mode=Mode.SUBTRACT)
    return part.part


def model_22848_cc91b848_0020():
    """Model: Towel Side Support v9"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 15.62496875, perimeter: 22.86
            with BuildLine():
                Line((-0.79375, 4.92125), (0.79375, 4.92125))
                Line((-0.79375, -4.92125), (-0.79375, 4.92125))
                Line((0.79375, -4.92125), (-0.79375, -4.92125))
                Line((0.79375, 4.92125), (0.79375, -4.92125))
            make_face()
        # OneSide extrude, distance=-43.4975
        extrude(amount=-43.4975)

        # Sketch5 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 11 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.79375, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 3.12499375, perimeter: 20.32
            with BuildLine():
                Line((7.3025, -4.92125), (7.3025, 4.92125))
                Line((7.62, -4.92125), (7.3025, -4.92125))
                Line((7.62, 4.92125), (7.62, -4.92125))
                Line((7.3025, 4.92125), (7.62, 4.92125))
            make_face()
            # Profile area: 3.12499375, perimeter: 20.32
            with BuildLine():
                Line((35.8775, 4.92125), (35.8775, -4.92125))
                Line((35.8775, -4.92125), (36.195, -4.92125))
                Line((36.195, -4.92125), (36.195, 4.92125))
                Line((36.195, 4.92125), (35.8775, 4.92125))
            make_face()
        # OneSide extrude, distance=-0.254
        extrude(amount=-0.254, mode=Mode.SUBTRACT)

        # Sketch8 -> Extrude3 (Join)
        # Sketch on XY construction plane
        # Sketch has 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.4560367312, perimeter: 2.393893602
            with Locations((0, 2.69875)):
                Circle(0.381)
        # OneSide extrude, distance=1.905
        extrude(amount=1.905, mode=Mode.ADD)
    return part.part


def model_22998_00817368_0003():
    """Model: vasca v10"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4530.8625617597, perimeter: 261.3716694115
            with BuildLine():
                Line((0, 0), (0, -90))
                Line((0, -90), (15, -90))
                CenterArc((15, -45), 45, -90, 180)
                Line((0, 0), (15, 0))
            make_face()
        # OneSide extrude, distance=30
        extrude(amount=30)

        # Sketch5 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 14 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 30, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 832.5663706144, perimeter: 170.5663706144
            with BuildLine():
                CenterArc((-4.5, 9), 2, -90, 90)
                Line((-2.5, 81), (-2.5, 9))
                CenterArc((-4.5, 81), 2, 0, 90)
                Line((-11.5, 83), (-4.5, 83))
                CenterArc((-11.5, 81), 2, 90, 90)
                Line((-13.5, 9), (-13.5, 81))
                CenterArc((-11.5, 9), 2, 180, 90)
                Line((-4.5, 7), (-11.5, 7))
            make_face()
        # OneSide extrude, distance=-0.4
        extrude(amount=-0.4, mode=Mode.SUBTRACT)

        # Sketch6 -> Extrude3 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 245.4369260617, perimeter: 64.2699081699
            with BuildLine():
                CenterArc((23.7755740472, -44.7007376348), 12.5, -90, 180)
                Line((23.7755740472, -57.2007376348), (23.7755740472, -32.2007376348))
            make_face()
        # OneSide extrude, distance=1.5
        extrude(amount=1.5, mode=Mode.SUBTRACT)

        # Sketch16 -> Extrude7 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 29.6, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 28.2743338823, perimeter: 18.8495559215
            with Locations((-8, 45)):
                Circle(3)
        # OneSide extrude, distance=-0.3
        extrude(amount=-0.3, mode=Mode.SUBTRACT)
    return part.part


def model_23037_d0df320c_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.7671458676, perimeter: 4.7123889804
            with Locations((4, 1)):
                Circle(0.75)
            # Profile area: 1.7671458676, perimeter: 4.7123889804
            with Locations((1, 1)):
                Circle(0.75)
        # OneSide extrude, distance=-3
        extrude(amount=-3)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XY construction plane
        # Sketch has 12 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.1820343854, perimeter: 1.7532210643
            with BuildLine():
                CenterArc((4, 1), 0.75, 165.5818576128, 29.8841513957)
                Line((3.2736217253, 1.1867474283), (2.7879583838, 1.1867474425))
                Line((2.7879583838, 1.1867474425), (2.7877445445, 1.186747431))
                Line((2.7877445445, 1.186747431), (2.7877445445, 0.8000000119))
                Line((2.7877445445, 0.8000000119), (3.277158382, 0.8000000119))
            make_face()
            # Profile area: 0.1407864589, perimeter: 1.5399142661
            with BuildLine():
                Line((2.1056020564, 0.8000000119), (2.1056020564, 1.186747431))
                Line((2.1056020564, 1.186747431), (1.7263782747, 1.1867474283))
                CenterArc((1, 1), 0.75, -15.4660090085, 29.8841513957)
                Line((1.722841618, 0.8000000119), (2.1056020564, 0.8000000119))
            make_face()
            # Profile area: 0.3641517875, perimeter: 2.6271500614
            with BuildLine():
                Line((3.277158382, 0.8000000119), (4.2000000626, 0.8000000119))
                Line((4.2000000626, 0.8000000119), (4.2000000626, 1.1867474283))
                Line((4.2000000626, 1.1867474283), (3.2736217253, 1.1867474283))
                CenterArc((4, 1), 0.75, 165.5818576128, 29.8841513957)
            make_face()
            # Profile area: 0.4028265009, perimeter: 2.8271499153
            with BuildLine():
                CenterArc((1, 1), 0.75, -15.4660090085, 29.8841513957)
                Line((1.7263782747, 1.1867474283), (0.7000000104, 1.1867474283))
                Line((0.7000000104, 1.1867474283), (0.7000000104, 0.8000000119))
                Line((0.7000000104, 0.8000000119), (1.722841618, 0.8000000119))
            make_face()
            # Profile area: 0.2638168467, perimeter: 2.1377798144
            with BuildLine():
                Line((2.7877445445, 1.186747431), (2.7877445445, 0.8000000119))
                Line((2.1056020564, 1.186747431), (2.7877445445, 1.186747431))
                Line((2.1056020564, 0.8000000119), (2.1056020564, 1.186747431))
                Line((2.7877445445, 0.8000000119), (2.1056020564, 0.8000000119))
            make_face()
        # OneSide extrude, distance=0.1
        extrude(amount=0.1, mode=Mode.ADD)

        # Sketch2 -> Extrude3 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 12 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.2638168467, perimeter: 2.1377798144
            with BuildLine():
                Line((2.7877445445, 1.186747431), (2.7877445445, 0.8000000119))
                Line((2.1056020564, 1.186747431), (2.7877445445, 1.186747431))
                Line((2.1056020564, 0.8000000119), (2.1056020564, 1.186747431))
                Line((2.7877445445, 0.8000000119), (2.1056020564, 0.8000000119))
            make_face()
            # Profile area: 0.8961061999, perimeter: 3.9912177813
            with BuildLine():
                Line((2.1056020564, 1.186747431), (2.7877445445, 1.186747431))
                Line((2.7879583838, 1.1867474425), (2.7877445445, 1.186747431))
                Line((2.7879583838, 2.5), (2.7879583838, 1.1867474425))
                Line((2.1056020564, 2.5), (2.7879583838, 2.5))
                Line((2.1056020564, 1.186747431), (2.1056020564, 2.5))
            make_face()
        # OneSide extrude, distance=-3
        extrude(amount=-3)

        # Sketch3 -> Extrude4 (Join)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 0, -3), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.4028265009, perimeter: 2.8271499153
            with BuildLine():
                CenterArc((-1, 1), 0.75, 165.5818576128, 29.8841513957)
                Line((-0.7000000104, 0.8000000119), (-1.722841618, 0.8000000119))
                Line((-0.7000000104, 1.1867474283), (-0.7000000104, 0.8000000119))
                Line((-1.7263782747, 1.1867474283), (-0.7000000104, 1.1867474283))
            make_face()
            # Profile area: 0.5866376892, perimeter: 3.8839254685
            with BuildLine():
                Line((-2.7879583838, 1.1867474425), (-2.1056020564, 1.186747431))
                Line((-3.2736217253, 1.1867474283), (-2.7879583838, 1.1867474425))
                CenterArc((-4, 1), 0.75, -15.4660090085, 29.8841513957)
                Line((-1.722841618, 0.8000000119), (-3.277158382, 0.8000000119))
                CenterArc((-1, 1), 0.75, 165.5818576128, 29.8841513957)
                Line((-2.1056020564, 1.186747431), (-1.7263782747, 1.1867474283))
            make_face()
            # Profile area: 0.8961062017, perimeter: 3.9912177813
            with BuildLine():
                Line((-2.1056020564, 1.186747431), (-2.1056020564, 2.5))
                Line((-2.1056020564, 2.5), (-2.7879583838, 2.5))
                Line((-2.7879583838, 2.5), (-2.7879583838, 1.1867474425))
                Line((-2.7879583838, 1.1867474425), (-2.1056020564, 1.186747431))
            make_face()
            # Profile area: 0.3641517875, perimeter: 2.6271500614
            with BuildLine():
                CenterArc((-4, 1), 0.75, -15.4660090085, 29.8841513957)
                Line((-4.2000000626, 1.1867474283), (-3.2736217253, 1.1867474283))
                Line((-4.2000000626, 0.8000000119), (-4.2000000626, 1.1867474283))
                Line((-3.277158382, 0.8000000119), (-4.2000000626, 0.8000000119))
            make_face()
        # OneSide extrude, distance=0.1
        extrude(amount=0.1, mode=Mode.ADD)

        # Sketch2 -> Extrude5 (Join)
        # Sketch on XY construction plane
        # Sketch has 12 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.8961061999, perimeter: 3.9912177813
            with BuildLine():
                Line((2.1056020564, 1.186747431), (2.7877445445, 1.186747431))
                Line((2.7879583838, 1.1867474425), (2.7877445445, 1.186747431))
                Line((2.7879583838, 2.5), (2.7879583838, 1.1867474425))
                Line((2.1056020564, 2.5), (2.7879583838, 2.5))
                Line((2.1056020564, 1.186747431), (2.1056020564, 2.5))
            make_face()
        # OneSide extrude, distance=0.1
        extrude(amount=0.1, mode=Mode.ADD)
    return part.part


def model_23132_1847c4ef_0001():
    """Model: Ring v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 63.6172512352, perimeter: 28.2743338823
            Circle(4.5)
        # OneSide extrude, distance=0.75
        extrude(amount=0.75)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.75), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 59.4467869876, perimeter: 27.3318560862
            Circle(4.35)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1.25), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 4.1704642476, perimeter: 55.6061899685
            with BuildLine():
                CenterArc((0, 0), 4.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 4.35, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 59.4467869876, perimeter: 27.3318560862
            Circle(4.35)
        # OneSide extrude, distance=0.75
        extrude(amount=0.75, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 2), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 12.5663706144, perimeter: 12.5663706144
            Circle(2)
        # OneSide extrude, distance=-2
        extrude(amount=-2, mode=Mode.SUBTRACT)
    return part.part


def model_23231_efe613bb_0009():
    """Model: Fan v9 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 21 constraints, 9 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.1046735764, perimeter: 33.2159277417
            with BuildLine():
                Line((0, -4), (0, 0))
                Line((4, -4), (0, -4))
                Line((4, 0), (4, -4))
                Line((0, 0), (4, 0))
            make_face()
            with BuildLine():
                CenterArc((0.4, -0.4), 0.21, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((3.6, -0.4), 0.21, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0.4, -3.6), 0.21, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((3.6, -3.6), 0.21, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((2, -2), 1.9, 43.4920422458, 3.0159155085)
                CenterArc((2, -2), 1.9, -43.4920422458, 86.9840844915)
                CenterArc((2, -2), 1.9, -46.5079577542, 3.0159155085)
                CenterArc((2, -2), 1.9, -133.4920422458, 86.9840844915)
                CenterArc((2, -2), 1.9, -136.5079577542, 3.0159155085)
                CenterArc((2, -2), 1.9, 136.5079577542, 86.9840844915)
                CenterArc((2, -2), 1.9, 133.4920422458, 3.0159155085)
                CenterArc((2, -2), 1.9, 46.5079577542, 86.9840844915)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(4, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.2427083588, perimeter: 2.0090278686
            with BuildLine():
                Line((-0.6000000089, 0.200000003), (-0.6000000089, 0.8000000119))
                Line((-0.6000000089, 0.8000000119), (-1.0045139343, 0.8000000119))
                Line((-1.0045139343, 0.8000000119), (-1.0045139343, 0.200000003))
                Line((-1.0045139343, 0.200000003), (-0.6000000089, 0.200000003))
            make_face()
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.2400000036, perimeter: 2.0000000179
            with BuildLine():
                Line((-3.0000000507, 0.200000003), (-3.4000000507, 0.200000003))
                Line((-3.0000000507, 0.8000000119), (-3.0000000507, 0.200000003))
                Line((-3.4000000507, 0.8000000119), (-3.0000000507, 0.8000000119))
                Line((-3.4000000507, 0.200000003), (-3.4000000507, 0.8000000119))
            make_face()
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2, mode=Mode.SUBTRACT)

        # Sketch1 -> Extrude5 (Join)
        # Sketch on XZ construction plane
        # Sketch has 21 constraints, 9 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0900197502, perimeter: 2.0012388063
            with BuildLine():
                Line((0.6923177372, -0.6216070591), (1.3291329945, -1.2584223163))
                CenterArc((2, -2), 1.9, 133.4920422458, 3.0159155085)
                Line((0.6216070591, -0.6923177372), (1.2584223163, -1.3291329945))
                CenterArc((2, -2), 1, 132.1340160174, 5.7319679652)
            make_face()
            # Profile area: 0.6871519788, perimeter: 3.3474078455
            with BuildLine():
                CenterArc((2, -2), 0.1, 75, 30)
                Line((2.0258819045, -1.9034074174), (2.6708670055, -1.2584223163))
                CenterArc((2, -2), 1, 47.8659839826, 84.2680320348)
                Line((1.3291329945, -1.2584223163), (1.9741180955, -1.9034074174))
            make_face()
            # Profile area: 0.0903922029, perimeter: 2.0290548235
            with BuildLine():
                Line((2.0965925826, -1.9741180955), (2.7415776837, -1.3291329945))
                CenterArc((2, -2), 1, 42.1340160174, 5.7319679652)
                Line((2.0258819045, -1.9034074174), (2.6708670055, -1.2584223163))
                CenterArc((2, -2), 0.1, 15, 60)
            make_face()
            # Profile area: 0.6871519788, perimeter: 3.3474078455
            with BuildLine():
                Line((2.0965925826, -2.0258819045), (2.7415776837, -2.6708670055))
                CenterArc((2, -2), 1, -42.1340160174, 84.2680320348)
                Line((2.0965925826, -1.9741180955), (2.7415776837, -1.3291329945))
                CenterArc((2, -2), 0.1, -15, 30)
            make_face()
            # Profile area: 0.0903922029, perimeter: 2.0290548235
            with BuildLine():
                Line((2.0258819045, -2.0965925826), (2.6708670055, -2.7415776837))
                CenterArc((2, -2), 1, -47.8659839826, 5.7319679652)
                Line((2.0965925826, -2.0258819045), (2.7415776837, -2.6708670055))
                CenterArc((2, -2), 0.1, -75, 60)
            make_face()
            # Profile area: 0.6871519788, perimeter: 3.3474078455
            with BuildLine():
                Line((1.9741180955, -2.0965925826), (1.3291329945, -2.7415776837))
                CenterArc((2, -2), 1, -132.1340160174, 84.2680320348)
                Line((2.0258819045, -2.0965925826), (2.6708670055, -2.7415776837))
                CenterArc((2, -2), 0.1, -105, 30)
            make_face()
            # Profile area: 0.0903922029, perimeter: 2.0290548235
            with BuildLine():
                Line((1.9034074174, -2.0258819045), (1.2584223163, -2.6708670055))
                CenterArc((2, -2), 1, -137.8659839826, 5.7319679652)
                Line((1.9741180955, -2.0965925826), (1.3291329945, -2.7415776837))
                CenterArc((2, -2), 0.1, -165, 60)
            make_face()
            # Profile area: 0.6871519788, perimeter: 3.3474078455
            with BuildLine():
                Line((1.2584223163, -1.3291329945), (1.9034074174, -1.9741180955))
                CenterArc((2, -2), 1, 137.8659839826, 84.2680320348)
                Line((1.9034074174, -2.0258819045), (1.2584223163, -2.6708670055))
                CenterArc((2, -2), 0.1, 165, 30)
            make_face()
            # Profile area: 0.0903922029, perimeter: 2.0290548235
            with BuildLine():
                Line((1.3291329945, -1.2584223163), (1.9741180955, -1.9034074174))
                CenterArc((2, -2), 1, 132.1340160174, 5.7319679652)
                Line((1.2584223163, -1.3291329945), (1.9034074174, -1.9741180955))
                CenterArc((2, -2), 0.1, 105, 60)
            make_face()
            # Profile area: 0.0007878669, perimeter: 0.1255649583
            with BuildLine():
                Line((2, -1.9292893219), (2.0258819045, -1.9034074174))
                CenterArc((2, -2), 0.1, 75, 30)
                Line((1.9741180955, -1.9034074174), (2, -1.9292893219))
            make_face()
            # Profile area: 0.0045661148, perimeter: 0.2779248359
            with BuildLine():
                Line((2.0707106781, -2), (2.0965925826, -1.9741180955))
                CenterArc((2, -2), 0.1, 15, 60)
                Line((2, -1.9292893219), (2.0258819045, -1.9034074174))
                Line((2, -1.9292893219), (2.0707106781, -2))
            make_face()
            # Profile area: 0.0007878669, perimeter: 0.1255649583
            with BuildLine():
                Line((2.0707106781, -2), (2.0965925826, -2.0258819045))
                CenterArc((2, -2), 0.1, -15, 30)
                Line((2.0707106781, -2), (2.0965925826, -1.9741180955))
            make_face()
            # Profile area: 0.0045661148, perimeter: 0.2779248359
            with BuildLine():
                Line((2, -2.0707106781), (2.0258819045, -2.0965925826))
                CenterArc((2, -2), 0.1, -75, 60)
                Line((2.0707106781, -2), (2.0965925826, -2.0258819045))
                Line((2.0707106781, -2), (2, -2.0707106781))
            make_face()
            # Profile area: 0.0007878669, perimeter: 0.1255649583
            with BuildLine():
                Line((2, -2.0707106781), (1.9741180955, -2.0965925826))
                CenterArc((2, -2), 0.1, -105, 30)
                Line((2, -2.0707106781), (2.0258819045, -2.0965925826))
            make_face()
            # Profile area: 0.0045661148, perimeter: 0.2779248359
            with BuildLine():
                Line((1.9292893219, -2), (1.9034074174, -2.0258819045))
                CenterArc((2, -2), 0.1, -165, 60)
                Line((2, -2.0707106781), (1.9741180955, -2.0965925826))
                Line((1.9292893219, -2), (2, -2.0707106781))
            make_face()
            # Profile area: 0.0007878669, perimeter: 0.1255649583
            with BuildLine():
                Line((1.9034074174, -1.9741180955), (1.9292893219, -2))
                CenterArc((2, -2), 0.1, 165, 30)
                Line((1.9292893219, -2), (1.9034074174, -2.0258819045))
            make_face()
            # Profile area: 0.0045661148, perimeter: 0.2779248359
            with BuildLine():
                Line((2, -1.9292893219), (1.9292893219, -2))
                Line((1.9741180955, -1.9034074174), (2, -1.9292893219))
                CenterArc((2, -2), 0.1, 105, 60)
                Line((1.9034074174, -1.9741180955), (1.9292893219, -2))
            make_face()
            # Profile area: 0.01, perimeter: 0.4
            with BuildLine():
                Line((2, -1.9292893219), (1.9292893219, -2))
                Line((1.9292893219, -2), (2, -2.0707106781))
                Line((2.0707106781, -2), (2, -2.0707106781))
                Line((2, -1.9292893219), (2.0707106781, -2))
            make_face()
        # OneSide extrude, distance=0.15
        extrude(amount=0.15, mode=Mode.ADD)

        # Sketch1 -> Extrude6 (Join)
        # Sketch on XZ construction plane
        # Sketch has 21 constraints, 9 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0900197502, perimeter: 2.0012388063
            with BuildLine():
                Line((2.6708670055, -2.7415776837), (3.3076822628, -3.3783929409))
                CenterArc((2, -2), 1.9, -46.5079577542, 3.0159155085)
                Line((2.7415776837, -2.6708670055), (3.3783929409, -3.3076822628))
                CenterArc((2, -2), 1, -47.8659839826, 5.7319679652)
            make_face()
            # Profile area: 0.0900197502, perimeter: 2.0012388063
            with BuildLine():
                Line((1.2584223163, -2.6708670055), (0.6216070591, -3.3076822628))
                CenterArc((2, -2), 1.9, -136.5079577542, 3.0159155085)
                Line((1.3291329945, -2.7415776837), (0.6923177372, -3.3783929409))
                CenterArc((2, -2), 1, -137.8659839826, 5.7319679652)
            make_face()
            # Profile area: 0.0900197502, perimeter: 2.0012388063
            with BuildLine():
                CenterArc((2, -2), 1, 42.1340160174, 5.7319679652)
                Line((2.7415776837, -1.3291329945), (3.3783929409, -0.6923177372))
                CenterArc((2, -2), 1.9, 43.4920422458, 3.0159155085)
                Line((2.6708670055, -1.2584223163), (3.3076822628, -0.6216070591))
            make_face()
        # OneSide extrude, distance=0.15
        extrude(amount=0.15, mode=Mode.ADD)

        # Sketch1 -> Extrude7 (Join)
        # Sketch on XZ construction plane
        # Sketch has 21 constraints, 9 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0045661148, perimeter: 0.2779248359
            with BuildLine():
                Line((2, -1.9292893219), (1.9292893219, -2))
                Line((1.9741180955, -1.9034074174), (2, -1.9292893219))
                CenterArc((2, -2), 0.1, 105, 60)
                Line((1.9034074174, -1.9741180955), (1.9292893219, -2))
            make_face()
            # Profile area: 0.0045661148, perimeter: 0.2779248359
            with BuildLine():
                Line((1.9292893219, -2), (1.9034074174, -2.0258819045))
                CenterArc((2, -2), 0.1, -165, 60)
                Line((2, -2.0707106781), (1.9741180955, -2.0965925826))
                Line((1.9292893219, -2), (2, -2.0707106781))
            make_face()
            # Profile area: 0.0045661148, perimeter: 0.2779248359
            with BuildLine():
                Line((2, -2.0707106781), (2.0258819045, -2.0965925826))
                CenterArc((2, -2), 0.1, -75, 60)
                Line((2.0707106781, -2), (2.0965925826, -2.0258819045))
                Line((2.0707106781, -2), (2, -2.0707106781))
            make_face()
            # Profile area: 0.0007878669, perimeter: 0.1255649583
            with BuildLine():
                Line((2, -1.9292893219), (2.0258819045, -1.9034074174))
                CenterArc((2, -2), 0.1, 75, 30)
                Line((1.9741180955, -1.9034074174), (2, -1.9292893219))
            make_face()
            # Profile area: 0.0045661148, perimeter: 0.2779248359
            with BuildLine():
                Line((2.0707106781, -2), (2.0965925826, -1.9741180955))
                CenterArc((2, -2), 0.1, 15, 60)
                Line((2, -1.9292893219), (2.0258819045, -1.9034074174))
                Line((2, -1.9292893219), (2.0707106781, -2))
            make_face()
            # Profile area: 0.0007878669, perimeter: 0.1255649583
            with BuildLine():
                Line((2.0707106781, -2), (2.0965925826, -2.0258819045))
                CenterArc((2, -2), 0.1, -15, 30)
                Line((2.0707106781, -2), (2.0965925826, -1.9741180955))
            make_face()
            # Profile area: 0.0007878669, perimeter: 0.1255649583
            with BuildLine():
                Line((2, -2.0707106781), (1.9741180955, -2.0965925826))
                CenterArc((2, -2), 0.1, -105, 30)
                Line((2, -2.0707106781), (2.0258819045, -2.0965925826))
            make_face()
            # Profile area: 0.0007878669, perimeter: 0.1255649583
            with BuildLine():
                Line((1.9034074174, -1.9741180955), (1.9292893219, -2))
                CenterArc((2, -2), 0.1, 165, 30)
                Line((1.9292893219, -2), (1.9034074174, -2.0258819045))
            make_face()
            # Profile area: 0.01, perimeter: 0.4
            with BuildLine():
                Line((2, -1.9292893219), (1.9292893219, -2))
                Line((1.9292893219, -2), (2, -2.0707106781))
                Line((2.0707106781, -2), (2, -2.0707106781))
                Line((2, -1.9292893219), (2.0707106781, -2))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)
    return part.part


def model_23315_4192448e_0000():
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
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 7.283920012, perimeter: 45.8829607057
            with BuildLine():
                CenterArc((0, 0), 3.81, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 3.4925, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=2.54
        extrude(amount=2.54, both=True)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on YZ construction plane
        # Sketch has 5 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.9793260902, perimeter: 13.1031958439
            with BuildLine():
                CenterArc((0, 0), 3.81, 45, 90)
                Line((2.6940768363, 2.6940768363), (2.9185832393, 2.9185832393))
                CenterArc((0, 0), 4.1275, 45, 90)
                Line((-2.6940768363, 2.6940768363), (-2.9185832393, 2.9185832393))
            make_face()
        # Symmetric extrude, each_side=2.286
        extrude(amount=2.286, both=True, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.8241469248, perimeter: 4.7877872041
            with Locations((0, -3.81)):
                Circle(0.762)
            # Profile area: 1.8241469248, perimeter: 4.7877872041
            with Locations((0, 3.81)):
                Circle(0.762)
        # Symmetric extrude, each_side=5.03936
        extrude(amount=5.03936, both=True, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on XZ construction plane
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1317036015, perimeter: 3.3099435819
            with BuildLine():
                Line((1.6784066215, -0.2499396968), (1.5866097465, -0.2499396968))
                _nurbs_edge([(1.6561898246, -0.1876838374), (1.6585431541, -0.1984381039), (1.6632912904, -0.2201361799), (1.6733389209, -0.2399475041), (1.6784066215, -0.2499396968)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.032880336, 0.066340185, 0.066340185, 0.066340185, 0.066340185], 3)
                _nurbs_edge([(1.6505745902, -0.0326545405), (1.6503725919, -0.0660304042), (1.6500592359, -0.1178057409), (1.6545824159, -0.1693621611), (1.6561898246, -0.1876838374)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.1000464704, 0.1552001692, 0.1552001692, 0.1552001692, 0.1552001692], 3)
                Line((1.6505745902, 0.0845329595), (1.6505745902, -0.0326545405))
                _nurbs_edge([(1.646180059, 0.165587647), (1.6474472185, 0.1551002682), (1.650698092, 0.1281950984), (1.6506213928, 0.1010792864), (1.6505745902, 0.0845329595)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0316661308, 0.0812388532, 0.0812388532, 0.0812388532, 0.0812388532], 3)
                _nurbs_edge([(1.618836309, 0.2254021001), (1.6249134131, 0.2167228069), (1.6376851011, 0.1984823385), (1.6432585849, 0.1769003562), (1.646180059, 0.165587647)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0315206845, 0.06624411, 0.06624411, 0.06624411, 0.06624411], 3)
                _nurbs_edge([(1.5578011527, 0.2647087407), (1.5703248046, 0.2596149889), (1.593186674, 0.2503163683), (1.6108492363, 0.233160186), (1.618836309, 0.2254021001)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.040098797, 0.0732001718, 0.0732001718, 0.0732001718, 0.0732001718], 3)
                _nurbs_edge([(1.4498909965, 0.2803337407), (1.470099324, 0.2799934482), (1.5067763011, 0.2793758364), (1.5419896842, 0.269253748), (1.5578011527, 0.2647087407)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0603073057, 0.1094543659, 0.1094543659, 0.1094543659, 0.1094543659], 3)
                _nurbs_edge([(1.3322152152, 0.2620231938), (1.3503633502, 0.2673594539), (1.3887565774, 0.2786485613), (1.4287841168, 0.2797519264), (1.4498909965, 0.2803337407)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0565038213, 0.1195364734, 0.1195364734, 0.1195364734, 0.1195364734], 3)
                _nurbs_edge([(1.2545784965, 0.2097771001), (1.2649726254, 0.2205920191), (1.2870476458, 0.2435607123), (1.3165854352, 0.255634439), (1.3322152152, 0.2620231938)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0444974336, 0.0945035189, 0.0945035189, 0.0945035189, 0.0945035189], 3)
                _nurbs_edge([(1.2160042777, 0.120665772), (1.2201958987, 0.1377193791), (1.2280417202, 0.1696400992), (1.2461462776, 0.1970233287), (1.2545784965, 0.2097771001)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0522200261, 0.0977447658, 0.0977447658, 0.0977447658, 0.0977447658], 3)
                Line((1.3019417777, 0.108947022), (1.2160042777, 0.120665772))
                _nurbs_edge([(1.3456429496, 0.1858513188), (1.3362330723, 0.1763240315), (1.3148953412, 0.1547200627), (1.3065864642, 0.1253596039), (1.3019417777, 0.108947022)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0395689558, 0.0897261157, 0.0897261157, 0.0897261157, 0.0897261157], 3)
                _nurbs_edge([(1.437195684, 0.2075798345), (1.4188344312, 0.2072940102), (1.3865638761, 0.206791664), (1.35796827, 0.1921585187), (1.3456429496, 0.1858513188)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0541671108, 0.0952006246, 0.0952006246, 0.0952006246, 0.0952006246], 3)
                _nurbs_edge([(1.5372933402, 0.1777946782), (1.523724301, 0.1864568323), (1.4933709657, 0.2058336844), (1.4571980162, 0.2069580828), (1.437195684, 0.2075798345)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0474566297, 0.1061583633, 0.1061583633, 0.1061583633, 0.1061583633], 3)
                _nurbs_edge([(1.562195684, 0.1021110845), (1.5618450425, 0.1179929462), (1.5612267776, 0.1459964654), (1.5445235372, 0.1681885636), (1.5372933402, 0.1777946782)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0461977674, 0.081457709, 0.081457709, 0.081457709, 0.081457709], 3)
                _nurbs_edge([(1.5617074027, 0.0791618657), (1.5618451046, 0.0840850579), (1.5620590398, 0.0917337812), (1.5621597847, 0.0993847523), (1.562195684, 0.1021110845)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0147750469, 0.0229546688, 0.0229546688, 0.0229546688, 0.0229546688], 3)
                _nurbs_edge([(1.4049691215, 0.0488884282), (1.4359508259, 0.0526391055), (1.4889392075, 0.059053934), (1.5403541802, 0.0732613602), (1.5617074027, 0.0791618657)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0934491895, 0.1598272721, 0.1598272721, 0.1598272721, 0.1598272721], 3)
                _nurbs_edge([(1.3268441215, 0.0357048345), (1.3376426726, 0.0380865137), (1.3634581961, 0.0437802679), (1.389702643, 0.0470097994), (1.4049691215, 0.0488884282)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0331575417, 0.0792679764, 0.0792679764, 0.0792679764, 0.0792679764], 3)
                _nurbs_edge([(1.2636116996, 0.0068962407), (1.2733704109, 0.0128861863), (1.2932569187, 0.025092624), (1.3155107135, 0.0321239316), (1.3268441215, 0.0357048345)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0342122059, 0.0697183556, 0.0697183556, 0.0697183556, 0.0697183556], 3)
                _nurbs_edge([(1.2182015434, -0.0436408687), (1.2243544975, -0.0337112649), (1.2364773166, -0.0141475254), (1.2546584342, -0.0000473638), (1.2636116996, 0.0068962407)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0347315782, 0.0684296734, 0.0684296734, 0.0684296734, 0.0684296734], 3)
                _nurbs_edge([(1.200867559, -0.1132209468), (1.2015450811, -0.1008822955), (1.202879925, -0.0765728705), (1.2131461238, -0.0545068935), (1.2182015434, -0.0436408687)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0366947705, 0.0722954841, 0.0722954841, 0.0722954841, 0.0722954841], 3)
                _nurbs_edge([(1.2467659965, -0.2199103999), (1.2333795902, -0.2048905876), (1.2062541755, -0.1744553365), (1.2026785908, -0.1338085321), (1.200867559, -0.1132209468)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0586997345, 0.1189456386, 0.1189456386, 0.1189456386, 0.1189456386], 3)
                _nurbs_edge([(1.3781136527, -0.2616584468), (1.3521067059, -0.2606175691), (1.3042886513, -0.2587037441), (1.2647847803, -0.2320622883), (1.2467659965, -0.2199103999)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0762789292, 0.1402513728, 0.1402513728, 0.1402513728, 0.1402513728], 3)
                _nurbs_edge([(1.4750374809, -0.244568603), (1.4595594937, -0.2495526997), (1.4280439445, -0.2597010827), (1.3949529326, -0.2609983144), (1.3781136527, -0.2616584468)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.04853692, 0.0988285925, 0.0988285925, 0.0988285925, 0.0988285925], 3)
                _nurbs_edge([(1.5690316215, -0.185974853), (1.5535340869, -0.1985447395), (1.5246157046, -0.2220001337), (1.4907529719, -0.2374147651), (1.4750374809, -0.244568603)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0595718446, 0.1111609958, 0.1111609958, 0.1111609958, 0.1111609958], 3)
                _nurbs_edge([(1.5866097465, -0.2499396968), (1.5824329701, -0.2401730624), (1.5736624633, -0.2196648223), (1.570623395, -0.1975552099), (1.5690316215, -0.185974853)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0317178514, 0.0666019929, 0.0666019929, 0.0666019929, 0.0666019929], 3)
            make_face()
            with BuildLine():
                _nurbs_edge([(1.4894417777, -0.1705939937), (1.5017004476, -0.1626097324), (1.5258420233, -0.1468859508), (1.5403876397, -0.122035034), (1.5475472465, -0.109802978)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0432275866, 0.0851301217, 0.0851301217, 0.0851301217, 0.0851301217], 3)
                _nurbs_edge([(1.3991097465, -0.1928107905), (1.4153610771, -0.1919996818), (1.4469295194, -0.1904240915), (1.4755533846, -0.177072318), (1.4894417777, -0.1705939937)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0482940843, 0.0938119497, 0.0938119497, 0.0938119497, 0.0938119497], 3)
                _nurbs_edge([(1.3212288871, -0.1693732905), (1.3318463101, -0.1761913725), (1.3554482965, -0.1913476188), (1.3836143016, -0.192291511), (1.3991097465, -0.1928107905)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0371920518, 0.0826760219, 0.0826760219, 0.0826760219, 0.0826760219], 3)
                _nurbs_edge([(1.294617559, -0.1107795405), (1.2957372863, -0.1220196108), (1.2979822899, -0.144555453), (1.3134672633, -0.1610870577), (1.3212288871, -0.1693732905)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0329061013, 0.0659752734, 0.0659752734, 0.0659752734, 0.0659752734], 3)
                _nurbs_edge([(1.3068245902, -0.0690314937), (1.3032642459, -0.0754944131), (1.2960986021, -0.0885018568), (1.2951133005, -0.1033226522), (1.294617559, -0.1107795405)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0218472611, 0.0439703795, 0.0439703795, 0.0439703795, 0.0439703795], 3)
                _nurbs_edge([(1.341492559, -0.0404670405), (1.3344836842, -0.0440214922), (1.320789335, -0.0509663875), (1.3114056379, -0.0631053479), (1.3068245902, -0.0690314937)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0232483062, 0.0454238997, 0.0454238997, 0.0454238997, 0.0454238997], 3)
                _nurbs_edge([(1.4181527152, -0.0228889155), (1.4026010376, -0.0251168264), (1.3765346066, -0.0288510657), (1.3515649089, -0.0371281899), (1.341492559, -0.0404670405)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0470034112, 0.0787832161, 0.0787832161, 0.0787832161, 0.0787832161], 3)
                _nurbs_edge([(1.5617074027, 0.0103142095), (1.5418872654, 0.0038015016), (1.4950736827, -0.0115809948), (1.4462850217, -0.0187532695), (1.4181527152, -0.0228889155)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0624833085, 0.1475805887, 0.1475805887, 0.1475805887, 0.1475805887], 3)
                Line((1.5617074027, -0.021912353), (1.5617074027, 0.0103142095))
                _nurbs_edge([(1.5475472465, -0.109802978), (1.5516562325, -0.0976150886), (1.5612433761, -0.0691781348), (1.5615386699, -0.0390994903), (1.5617074027, -0.021912353)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0383644679, 0.0895125115, 0.0895125115, 0.0895125115, 0.0895125115], 3)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.1116638807, perimeter: 2.8707938555
            with BuildLine():
                _nurbs_edge([(0.9171761527, -0.2616584468), (0.886721402, -0.2607990272), (0.8317341812, -0.2592473121), (0.7842903956, -0.2318773353), (0.7631234184, -0.2196662593)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0896669597, 0.1618971354, 0.1618971354, 0.1618971354, 0.1618971354], 3)
                _nurbs_edge([(1.0265511527, -0.2404182124), (1.0095549124, -0.2466109007), (0.974243631, -0.2594767908), (0.9366664545, -0.2609133441), (0.9171761527, -0.2616584468)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0539205795, 0.1120250545, 0.1120250545, 0.1120250545, 0.1120250545], 3)
                _nurbs_edge([(1.1005257621, -0.1803596187), (1.0907793913, -0.19267636), (1.0706082383, -0.2181671688), (1.0415624776, -0.2328367385), (1.0265511527, -0.2404182124)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.046533653, 0.0963063541, 0.0963063541, 0.0963063541, 0.0963063541], 3)
                _nurbs_edge([(1.1261605277, -0.0975959468), (1.1250290722, -0.1121258469), (1.1227313156, -0.1416331267), (1.1080020699, -0.1673209356), (1.1005257621, -0.1803596187)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0431422286, 0.0876131153, 0.0876131153, 0.0876131153, 0.0876131153], 3)
                _nurbs_edge([(1.105164434, -0.0224006343), (1.1112836402, -0.0334617882), (1.1242059566, -0.0568203295), (1.1254864149, -0.083532828), (1.1261605277, -0.0975959468)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0374111155, 0.0790034286, 0.0790034286, 0.0790034286, 0.0790034286], 3)
                _nurbs_edge([(1.0473031059, 0.0237419438), (1.0588465444, 0.0179711838), (1.0814213441, 0.0066856599), (1.0973706666, -0.012852938), (1.105164434, -0.0224006343)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0382277952, 0.074759771, 0.074759771, 0.074759771, 0.074759771], 3)
                _nurbs_edge([(0.9171761527, 0.0645134282), (0.943723237, 0.057463213), (0.9877106185, 0.0457813085), (1.0303838487, 0.0299992708), (1.0473031059, 0.0237419438)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0823375343, 0.1364297672, 0.1364297672, 0.1364297672, 0.1364297672], 3)
                _nurbs_edge([(0.839539434, 0.0869743657), (0.84819416, 0.084247146), (0.8738931843, 0.0761490404), (0.8999166656, 0.069153237), (0.9171761527, 0.0645134282)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0272205849, 0.0808278012, 0.0808278012, 0.0808278012, 0.0808278012], 3)
                _nurbs_edge([(0.8058480277, 0.1104118657), (0.8102227, 0.1057855637), (0.819801051, 0.095656269), (0.8325909834, 0.0900306331), (0.839539434, 0.0869743657)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0189130213, 0.0414100864, 0.0414100864, 0.0414100864, 0.0414100864], 3)
                _nurbs_edge([(0.7951058402, 0.1411735845), (0.7955617659, 0.1356088088), (0.7964779122, 0.1244268361), (0.8027149095, 0.1150981003), (0.8058480277, 0.1104118657)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0164559656, 0.0330669499, 0.0330669499, 0.0330669499, 0.0330669499], 3)
                _nurbs_edge([(0.8209847465, 0.1880485845), (0.8134443035, 0.1813774711), (0.7991837238, 0.1687609784), (0.7964119889, 0.1500098441), (0.7951058402, 0.1411735845)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0291349386, 0.0551003587, 0.0551003587, 0.0551003587, 0.0551003587], 3)
                _nurbs_edge([(0.9074105277, 0.2080681157), (0.8897226177, 0.2079256069), (0.8592516258, 0.2076801068), (0.8322939391, 0.1938503815), (0.8209847465, 0.1880485845)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0521207357, 0.0897884774, 0.0897884774, 0.0897884774, 0.0897884774], 3)
                _nurbs_edge([(0.9867562309, 0.1856071782), (0.9757415393, 0.1921427167), (0.9513874625, 0.2065931446), (0.9229735788, 0.2075461364), (0.9074105277, 0.2080681157)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0378320004, 0.0836485925, 0.0836485925, 0.0836485925, 0.0836485925], 3)
                _nurbs_edge([(1.0206917777, 0.1231071782), (1.017974839, 0.1355883227), (1.0127135837, 0.1597576151), (0.9952173306, 0.1771812138), (0.9867562309, 0.1856071782)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0374272933, 0.0724766222, 0.0724766222, 0.0724766222, 0.0724766222], 3)
                Line((1.1066292777, 0.1348259282), (1.0206917777, 0.1231071782))
                _nurbs_edge([(1.0763558402, 0.2151481938), (1.0831989623, 0.2037050426), (1.0980957107, 0.1787945201), (1.1036347227, 0.1502551582), (1.1066292777, 0.1348259282)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0396982435, 0.0864188516, 0.0864188516, 0.0864188516, 0.0864188516], 3)
                _nurbs_edge([(1.0082406059, 0.2627556157), (1.0222844867, 0.2568054427), (1.0484198234, 0.2457323086), (1.0675194433, 0.2248222065), (1.0763558402, 0.2151481938)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0451235185, 0.0839738218, 0.0839738218, 0.0839738218, 0.0839738218], 3)
                _nurbs_edge([(0.9010628715, 0.2803337407), (0.9203198186, 0.2797734472), (0.9568566999, 0.2787103826), (0.9917418497, 0.2678785001), (1.0082406059, 0.2627556157)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0574802452, 0.1090592859, 0.1090592859, 0.1090592859, 0.1090592859], 3)
                _nurbs_edge([(0.8251351371, 0.2698356938), (0.8373013378, 0.2728971471), (0.8622225185, 0.2791682117), (0.887913763, 0.2799391597), (0.9010628715, 0.2803337407)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.037517611, 0.0768508744, 0.0768508744, 0.0768508744, 0.0768508744], 3)
                _nurbs_edge([(0.769226934, 0.2442009282), (0.7771512829, 0.2491859239), (0.7946376775, 0.2601861466), (0.8143538093, 0.2664244283), (0.8251351371, 0.2698356938)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0279731519, 0.0617274144, 0.0617274144, 0.0617274144, 0.0617274144], 3)
                _nurbs_edge([(0.7260140434, 0.1951286626), (0.731784308, 0.2045603383), (0.7433310312, 0.2234338141), (0.76059188, 0.2372760817), (0.769226934, 0.2442009282)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.032896647, 0.0658286065, 0.0658286065, 0.0658286065, 0.0658286065], 3)
                _nurbs_edge([(0.7101449027, 0.1309196782), (0.7107827902, 0.1422184003), (0.7120475553, 0.1646208312), (0.7213856434, 0.1850185729), (0.7260140434, 0.1951286626)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0336211204, 0.0666619485, 0.0666619485, 0.0666619485, 0.0666619485], 3)
                _nurbs_edge([(0.7294320121, 0.0613396001), (0.7238067111, 0.0721632382), (0.7124636634, 0.0939883893), (0.7109220111, 0.1185425432), (0.7101449027, 0.1309196782)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0361613599, 0.0729169925, 0.0729169925, 0.0729169925, 0.0729169925], 3)
                _nurbs_edge([(0.7860726371, 0.0120231938), (0.774479076, 0.0183658119), (0.7519734601, 0.0306782087), (0.7367925944, 0.0513275683), (0.7294320121, 0.0613396001)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.039107678, 0.0759164824, 0.0759164824, 0.0759164824, 0.0759164824], 3)
                _nurbs_edge([(0.9201058402, -0.0302131343), (0.8925963905, -0.0233221559), (0.8470510396, -0.0119132753), (0.8033701958, 0.0052332082), (0.7860726371, 0.0120231938)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0849553687, 0.140654288, 0.140654288, 0.140654288, 0.140654288], 3)
                _nurbs_edge([(1.0099495902, -0.0599982905), (0.9995361742, -0.0553219022), (0.970655472, -0.0423523464), (0.9398218736, -0.0349478297), (0.9201058402, -0.0302131343)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0341894953, 0.0948215873, 0.0948215873, 0.0948215873, 0.0948215873], 3)
                _nurbs_edge([(1.0358284965, -0.1068732905), (1.0346988012, -0.0974402894), (1.0324116513, -0.0783424952), (1.017497283, -0.0661623028), (1.0099495902, -0.0599982905)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0273864957, 0.0554459443, 0.0554459443, 0.0554459443, 0.0554459443], 3)
                _nurbs_edge([(1.0065316215, -0.1647346187), (1.015072252, -0.1564045789), (1.0314798836, -0.1404015189), (1.034419184, -0.1177392267), (1.0358284965, -0.1068732905)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0346516853, 0.066570271, 0.066570271, 0.066570271, 0.066570271], 3)
                _nurbs_edge([(0.9166878715, -0.1893928218), (0.9347540294, -0.1889772856), (0.9669285931, -0.1882372447), (0.9944594576, -0.171898908), (1.0065316215, -0.1647346187)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0530934647, 0.0945557474, 0.0945557474, 0.0945557474, 0.0945557474], 3)
                _nurbs_edge([(0.8231820121, -0.1615607905), (0.8361890502, -0.1696622057), (0.8646916893, -0.1874150338), (0.8983755006, -0.1886962709), (0.9166878715, -0.1893928218)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0452077724, 0.0990648913, 0.0990648913, 0.0990648913, 0.0990648913], 3)
                _nurbs_edge([(0.7824105277, -0.0814826655), (0.7856172824, -0.0976004325), (0.7917070676, -0.1282088667), (0.8130688849, -0.1508445764), (0.8231820121, -0.1615607905)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.048177775, 0.0914919704, 0.0914919704, 0.0914919704, 0.0914919704], 3)
                Line((0.6954964652, -0.0951545405), (0.7824105277, -0.0814826655))
                _nurbs_edge([(0.7631234184, -0.2196662593), (0.7469434422, -0.2032476404), (0.7125530489, -0.1683500141), (0.7014014599, -0.1204948366), (0.6954964652, -0.0951545405)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0678242309, 0.1441597908, 0.1441597908, 0.1441597908, 0.1441597908], 3)
            make_face()
            # Profile area: 0.1116638807, perimeter: 2.8707938555
            with BuildLine():
                _nurbs_edge([(0.4171761527, -0.2616584468), (0.386721402, -0.2607990272), (0.3317341812, -0.2592473121), (0.2842903956, -0.2318773353), (0.2631234184, -0.2196662593)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0896669597, 0.1618971354, 0.1618971354, 0.1618971354, 0.1618971354], 3)
                _nurbs_edge([(0.5265511527, -0.2404182124), (0.5095549124, -0.2466109007), (0.474243631, -0.2594767908), (0.4366664545, -0.2609133441), (0.4171761527, -0.2616584468)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0539205795, 0.1120250545, 0.1120250545, 0.1120250545, 0.1120250545], 3)
                _nurbs_edge([(0.6005257621, -0.1803596187), (0.5907793913, -0.19267636), (0.5706082383, -0.2181671688), (0.5415624776, -0.2328367385), (0.5265511527, -0.2404182124)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.046533653, 0.0963063541, 0.0963063541, 0.0963063541, 0.0963063541], 3)
                _nurbs_edge([(0.6261605277, -0.0975959468), (0.6250290722, -0.1121258469), (0.6227313156, -0.1416331267), (0.6080020699, -0.1673209356), (0.6005257621, -0.1803596187)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0431422286, 0.0876131153, 0.0876131153, 0.0876131153, 0.0876131153], 3)
                _nurbs_edge([(0.605164434, -0.0224006343), (0.6112836402, -0.0334617882), (0.6242059566, -0.0568203295), (0.6254864149, -0.083532828), (0.6261605277, -0.0975959468)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0374111155, 0.0790034286, 0.0790034286, 0.0790034286, 0.0790034286], 3)
                _nurbs_edge([(0.5473031059, 0.0237419438), (0.5588465444, 0.0179711838), (0.5814213441, 0.0066856599), (0.5973706666, -0.012852938), (0.605164434, -0.0224006343)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0382277952, 0.074759771, 0.074759771, 0.074759771, 0.074759771], 3)
                _nurbs_edge([(0.4171761527, 0.0645134282), (0.443723237, 0.057463213), (0.4877106185, 0.0457813085), (0.5303838487, 0.0299992708), (0.5473031059, 0.0237419438)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0823375343, 0.1364297672, 0.1364297672, 0.1364297672, 0.1364297672], 3)
                _nurbs_edge([(0.339539434, 0.0869743657), (0.34819416, 0.084247146), (0.3738931843, 0.0761490404), (0.3999166656, 0.069153237), (0.4171761527, 0.0645134282)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0272205849, 0.0808278012, 0.0808278012, 0.0808278012, 0.0808278012], 3)
                _nurbs_edge([(0.3058480277, 0.1104118657), (0.3102227, 0.1057855637), (0.319801051, 0.095656269), (0.3325909834, 0.0900306331), (0.339539434, 0.0869743657)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0189130213, 0.0414100864, 0.0414100864, 0.0414100864, 0.0414100864], 3)
                _nurbs_edge([(0.2951058402, 0.1411735845), (0.2955617659, 0.1356088088), (0.2964779122, 0.1244268361), (0.3027149095, 0.1150981003), (0.3058480277, 0.1104118657)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0164559656, 0.0330669499, 0.0330669499, 0.0330669499, 0.0330669499], 3)
                _nurbs_edge([(0.3209847465, 0.1880485845), (0.3134443035, 0.1813774711), (0.2991837238, 0.1687609784), (0.2964119889, 0.1500098441), (0.2951058402, 0.1411735845)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0291349386, 0.0551003587, 0.0551003587, 0.0551003587, 0.0551003587], 3)
                _nurbs_edge([(0.4074105277, 0.2080681157), (0.3897226177, 0.2079256069), (0.3592516258, 0.2076801068), (0.3322939391, 0.1938503815), (0.3209847465, 0.1880485845)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0521207357, 0.0897884774, 0.0897884774, 0.0897884774, 0.0897884774], 3)
                _nurbs_edge([(0.4867562309, 0.1856071782), (0.4757415393, 0.1921427167), (0.4513874625, 0.2065931446), (0.4229735788, 0.2075461364), (0.4074105277, 0.2080681157)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0378320004, 0.0836485925, 0.0836485925, 0.0836485925, 0.0836485925], 3)
                _nurbs_edge([(0.5206917777, 0.1231071782), (0.517974839, 0.1355883227), (0.5127135837, 0.1597576151), (0.4952173306, 0.1771812138), (0.4867562309, 0.1856071782)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0374272933, 0.0724766222, 0.0724766222, 0.0724766222, 0.0724766222], 3)
                Line((0.6066292777, 0.1348259282), (0.5206917777, 0.1231071782))
                _nurbs_edge([(0.5763558402, 0.2151481938), (0.5831989623, 0.2037050426), (0.5980957107, 0.1787945201), (0.6036347227, 0.1502551582), (0.6066292777, 0.1348259282)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0396982435, 0.0864188516, 0.0864188516, 0.0864188516, 0.0864188516], 3)
                _nurbs_edge([(0.5082406059, 0.2627556157), (0.5222844867, 0.2568054427), (0.5484198234, 0.2457323086), (0.5675194433, 0.2248222065), (0.5763558402, 0.2151481938)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0451235185, 0.0839738218, 0.0839738218, 0.0839738218, 0.0839738218], 3)
                _nurbs_edge([(0.4010628715, 0.2803337407), (0.4203198186, 0.2797734472), (0.4568566999, 0.2787103826), (0.4917418497, 0.2678785001), (0.5082406059, 0.2627556157)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0574802452, 0.1090592859, 0.1090592859, 0.1090592859, 0.1090592859], 3)
                _nurbs_edge([(0.3251351371, 0.2698356938), (0.3373013378, 0.2728971471), (0.3622225185, 0.2791682117), (0.387913763, 0.2799391597), (0.4010628715, 0.2803337407)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.037517611, 0.0768508744, 0.0768508744, 0.0768508744, 0.0768508744], 3)
                _nurbs_edge([(0.269226934, 0.2442009282), (0.2771512829, 0.2491859239), (0.2946376775, 0.2601861466), (0.3143538093, 0.2664244283), (0.3251351371, 0.2698356938)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0279731519, 0.0617274144, 0.0617274144, 0.0617274144, 0.0617274144], 3)
                _nurbs_edge([(0.2260140434, 0.1951286626), (0.231784308, 0.2045603383), (0.2433310312, 0.2234338141), (0.26059188, 0.2372760817), (0.269226934, 0.2442009282)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.032896647, 0.0658286065, 0.0658286065, 0.0658286065, 0.0658286065], 3)
                _nurbs_edge([(0.2101449027, 0.1309196782), (0.2107827902, 0.1422184003), (0.2120475553, 0.1646208312), (0.2213856434, 0.1850185729), (0.2260140434, 0.1951286626)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0336211204, 0.0666619485, 0.0666619485, 0.0666619485, 0.0666619485], 3)
                _nurbs_edge([(0.2294320121, 0.0613396001), (0.2238067111, 0.0721632382), (0.2124636634, 0.0939883893), (0.2109220111, 0.1185425432), (0.2101449027, 0.1309196782)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0361613599, 0.0729169925, 0.0729169925, 0.0729169925, 0.0729169925], 3)
                _nurbs_edge([(0.2860726371, 0.0120231938), (0.274479076, 0.0183658119), (0.2519734601, 0.0306782087), (0.2367925944, 0.0513275683), (0.2294320121, 0.0613396001)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.039107678, 0.0759164824, 0.0759164824, 0.0759164824, 0.0759164824], 3)
                _nurbs_edge([(0.4201058402, -0.0302131343), (0.3925963905, -0.0233221559), (0.3470510396, -0.0119132753), (0.3033701958, 0.0052332082), (0.2860726371, 0.0120231938)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0849553687, 0.140654288, 0.140654288, 0.140654288, 0.140654288], 3)
                _nurbs_edge([(0.5099495902, -0.0599982905), (0.4995361742, -0.0553219022), (0.470655472, -0.0423523464), (0.4398218736, -0.0349478297), (0.4201058402, -0.0302131343)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0341894953, 0.0948215873, 0.0948215873, 0.0948215873, 0.0948215873], 3)
                _nurbs_edge([(0.5358284965, -0.1068732905), (0.5346988012, -0.0974402894), (0.5324116513, -0.0783424952), (0.517497283, -0.0661623028), (0.5099495902, -0.0599982905)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0273864957, 0.0554459443, 0.0554459443, 0.0554459443, 0.0554459443], 3)
                _nurbs_edge([(0.5065316215, -0.1647346187), (0.515072252, -0.1564045789), (0.5314798836, -0.1404015189), (0.534419184, -0.1177392267), (0.5358284965, -0.1068732905)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0346516853, 0.066570271, 0.066570271, 0.066570271, 0.066570271], 3)
                _nurbs_edge([(0.4166878715, -0.1893928218), (0.4347540294, -0.1889772856), (0.4669285931, -0.1882372447), (0.4944594576, -0.171898908), (0.5065316215, -0.1647346187)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0530934647, 0.0945557474, 0.0945557474, 0.0945557474, 0.0945557474], 3)
                _nurbs_edge([(0.3231820121, -0.1615607905), (0.3361890502, -0.1696622057), (0.3646916893, -0.1874150338), (0.3983755006, -0.1886962709), (0.4166878715, -0.1893928218)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0452077724, 0.0990648913, 0.0990648913, 0.0990648913, 0.0990648913], 3)
                _nurbs_edge([(0.2824105277, -0.0814826655), (0.2856172824, -0.0976004325), (0.2917070676, -0.1282088667), (0.3130688849, -0.1508445764), (0.3231820121, -0.1615607905)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.048177775, 0.0914919704, 0.0914919704, 0.0914919704, 0.0914919704], 3)
                Line((0.1954964652, -0.0951545405), (0.2824105277, -0.0814826655))
                _nurbs_edge([(0.2631234184, -0.2196662593), (0.2469434422, -0.2032476404), (0.2125530489, -0.1683500141), (0.2014014599, -0.1204948366), (0.1954964652, -0.0951545405)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0678242309, 0.1441597908, 0.1441597908, 0.1441597908, 0.1441597908], 3)
            make_face()
            # Profile area: 0.0455760956, perimeter: 1.212890625
            with BuildLine():
                Line((0.0968636527, 0.2686149907), (0.0968636527, -0.2499396968))
                Line((0.0089730277, 0.2686149907), (0.0968636527, 0.2686149907))
                Line((0.0089730277, -0.2499396968), (0.0089730277, 0.2686149907))
                Line((0.0968636527, -0.2499396968), (0.0089730277, -0.2499396968))
            make_face()
            # Profile area: 0.0088834763, perimeter: 0.3779296875
            with BuildLine():
                Line((0.0968636527, 0.4658806157), (0.0968636527, 0.364806397))
                Line((0.0089730277, 0.4658806157), (0.0968636527, 0.4658806157))
                Line((0.0089730277, 0.364806397), (0.0089730277, 0.4658806157))
                Line((0.0968636527, 0.364806397), (0.0089730277, 0.364806397))
            make_face()
            # Profile area: 0.0629138947, perimeter: 1.607421875
            with BuildLine():
                Line((-0.1277457223, 0.4658806157), (-0.1277457223, -0.2499396968))
                Line((-0.2156363473, 0.4658806157), (-0.1277457223, 0.4658806157))
                Line((-0.2156363473, -0.2499396968), (-0.2156363473, 0.4658806157))
                Line((-0.1277457223, -0.2499396968), (-0.2156363473, -0.2499396968))
            make_face()
            # Profile area: 0.1287653984, perimeter: 3.2366769316
            with BuildLine():
                _nurbs_edge([(-0.5515738473, -0.1893928218), (-0.5362606673, -0.188487324), (-0.5066472811, -0.1867362276), (-0.4812962467, -0.1714054019), (-0.469054316, -0.1640021968)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0452472678, 0.0875014088, 0.0875014088, 0.0875014088, 0.0875014088], 3)
                _nurbs_edge([(-0.6599722848, -0.1439826655), (-0.6444931307, -0.1572269746), (-0.6132462066, -0.1839625389), (-0.5722574995, -0.1875716156), (-0.5515738473, -0.1893928218)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0595324036, 0.1201748168, 0.1201748168, 0.1201748168, 0.1201748168], 3)
                _nurbs_edge([(-0.7083121285, -0.0131232905), (-0.705772337, -0.0391602022), (-0.7010863063, -0.0871994869), (-0.6728875422, -0.1261452139), (-0.6599722848, -0.1439826655)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0768252981, 0.1417461649, 0.1417461649, 0.1417461649, 0.1417461649], 3)
                Line((-0.3215933785, -0.0131232905), (-0.7083121285, -0.0131232905))
                _nurbs_edge([(-0.3211050973, 0.0103142095), (-0.3211361059, 0.007058811), (-0.3212105389, -0.000755424), (-0.3214523219, -0.0085663718), (-0.3215933785, -0.0131232905)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0097663879, 0.0234431666, 0.0234431666, 0.0234431666, 0.0234431666], 3)
                _nurbs_edge([(-0.387023066, 0.2095329595), (-0.367828066, 0.1820755281), (-0.3261860836, 0.1225088769), (-0.3228846986, 0.0496100809), (-0.3211050973, 0.0103142095)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0985092295, 0.2137077149, 0.2137077149, 0.2137077149, 0.2137077149], 3)
                _nurbs_edge([(-0.556944941, 0.2803337407), (-0.5241005599, 0.2776338973), (-0.4597348455, 0.2723429665), (-0.4109259005, 0.2301807447), (-0.387023066, 0.2095329595)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0961260888, 0.1883799956, 0.1883799956, 0.1883799956, 0.1883799956], 3)
                _nurbs_edge([(-0.7317496285, 0.2080681157), (-0.7072137021, 0.2291422821), (-0.6569500042, 0.2723143033), (-0.5908027863, 0.2776186695), (-0.556944941, 0.2803337407)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0944836836, 0.1935569599, 0.1935569599, 0.1935569599, 0.1935569599], 3)
                _nurbs_edge([(-0.799132441, 0.0049431157), (-0.7973045067, 0.0449998746), (-0.7939115096, 0.1193529102), (-0.7513716678, 0.1800642455), (-0.7317496285, 0.2080681157)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.1174255496, 0.2179643664, 0.2179643664, 0.2179643664, 0.2179643664], 3)
                _nurbs_edge([(-0.7324820504, -0.1915900874), (-0.7518932469, -0.1645114066), (-0.7938291901, -0.1060106323), (-0.7972793057, -0.0338278791), (-0.799132441, 0.0049431157)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0978925136, 0.2114869579, 0.2114869579, 0.2114869579, 0.2114869579], 3)
                _nurbs_edge([(-0.5520621285, -0.2616584468), (-0.5874549845, -0.2593130664), (-0.6551369666, -0.2548279807), (-0.7075007812, -0.2120149516), (-0.7324820504, -0.1915900874)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.103483123, 0.1978914298, 0.1978914298, 0.1978914298, 0.1978914298], 3)
                _nurbs_edge([(-0.4036246285, -0.2177131343), (-0.4251209086, -0.230518905), (-0.4707566081, -0.2577050182), (-0.5239336482, -0.2602907176), (-0.5520621285, -0.2616584468)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0739169762, 0.1569226345, 0.1569226345, 0.1569226345, 0.1569226345], 3)
                _nurbs_edge([(-0.3240347848, -0.094177978), (-0.3323788234, -0.1189569729), (-0.3485260717, -0.1669088822), (-0.3856731725, -0.2011607898), (-0.4036246285, -0.2177131343)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0770342017, 0.1490753388, 0.1490753388, 0.1490753388, 0.1490753388], 3)
                Line((-0.4148550973, -0.0829475093), (-0.3240347848, -0.094177978))
                _nurbs_edge([(-0.469054316, -0.1640021968), (-0.4580159114, -0.1535831032), (-0.4338405907, -0.1307641416), (-0.4215395219, -0.0997828197), (-0.4148550973, -0.0829475093)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.045000919, 0.0985569645, 0.0985569645, 0.0985569645, 0.0985569645], 3)
            make_face()
            with BuildLine():
                _nurbs_edge([(-0.5559683785, 0.2080681157), (-0.5752562175, 0.2064678603), (-0.6133430596, 0.2033079067), (-0.643091638, 0.1793606979), (-0.6577750191, 0.167540772)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0566386847, 0.1118419047, 0.1118419047, 0.1118419047, 0.1118419047], 3)
                _nurbs_edge([(-0.4470816598, 0.1572868657), (-0.4621648641, 0.1720979836), (-0.4924633289, 0.2018498932), (-0.5347386096, 0.2059893609), (-0.5559683785, 0.2080681157)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0614450349, 0.1234280316, 0.1234280316, 0.1234280316, 0.1234280316], 3)
                _nurbs_edge([(-0.4138785348, 0.0591423345), (-0.416101379, 0.0787696859), (-0.4200929425, 0.1140145392), (-0.4387946596, 0.1439999143), (-0.4470816598, 0.1572868657)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0583420753, 0.1047649192, 0.1047649192, 0.1047649192, 0.1047649192], 3)
                Line((-0.703429316, 0.0591423345), (-0.4138785348, 0.0591423345))
                _nurbs_edge([(-0.6577750191, 0.167540772), (-0.6700162803, 0.1524257309), (-0.6956440316, 0.1207815639), (-0.7007580445, 0.0802918662), (-0.703429316, 0.0591423345)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0571844695, 0.1197188221, 0.1197188221, 0.1197188221, 0.1197188221], 3)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.2377333281, perimeter: 5.7493660229
            with BuildLine():
                _nurbs_edge([(-1.2825308785, -0.0409553218), (-1.2757126393, -0.0615647249), (-1.2640560216, -0.0967990315), (-1.2529577949, -0.1322129126), (-1.248351191, -0.146912353)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0651225382, 0.1113349794, 0.1113349794, 0.1113349794, 0.1113349794], 3)
                Line((-1.4519644723, 0.4658806157), (-1.2825308785, -0.0409553218))
                Line((-1.5945425973, 0.4658806157), (-1.4519644723, 0.4658806157))
                Line((-1.5945425973, -0.2499396968), (-1.5945425973, 0.4658806157))
                Line((-1.5032340035, -0.2499396968), (-1.5945425973, -0.2499396968))
                Line((-1.5032340035, 0.3594353032), (-1.5032340035, -0.2499396968))
                Line((-1.2962027535, -0.2499396968), (-1.5032340035, 0.3594353032))
                Line((-1.2107535348, -0.2499396968), (-1.2962027535, -0.2499396968))
                Line((-1.0027457223, 0.349181397), (-1.2107535348, -0.2499396968))
                Line((-1.0027457223, -0.2499396968), (-1.0027457223, 0.349181397))
                Line((-0.9114371285, -0.2499396968), (-1.0027457223, -0.2499396968))
                Line((-0.9114371285, 0.4658806157), (-0.9114371285, -0.2499396968))
                Line((-1.0388785348, 0.4658806157), (-0.9114371285, 0.4658806157))
                Line((-1.2102652535, -0.0321662593), (-1.0388785348, 0.4658806157))
                _nurbs_edge([(-1.248351191, -0.146912353), (-1.2431839643, -0.1308261631), (-1.2308583787, -0.0924551525), (-1.217831123, -0.0543162677), (-1.2102652535, -0.0321662593)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0506862338, 0.1209038322, 0.1209038322, 0.1209038322, 0.1209038322], 3)
            make_face()
        # OneSide extrude, distance=-3.5687
        extrude(amount=-3.5687, mode=Mode.SUBTRACT)
    return part.part


def model_23410_0163b27d_0001():
    """Model: joint counterpart"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2827433472, perimeter: 1.8849556202
            with Locations((4.5000000671, -9.0000001341)):
                Circle(0.3000000045)
        # OneSide extrude, distance=0.05
        extrude(amount=0.05)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.05, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1416091006, perimeter: 4.3098267508
            with BuildLine():
                Line((-4.2979274728, 9.3500001341), (-4.7020726613, 9.3500001341))
                Line((-4.7020726613, 9.3500001341), (-4.9041452555, 9.0000001341))
                Line((-4.9041452555, 9.0000001341), (-4.7020726613, 8.6500001341))
                Line((-4.7020726613, 8.6500001341), (-4.2979274728, 8.6500001341))
                Line((-4.2979274728, 8.6500001341), (-4.0958548786, 9.0000001341))
                Line((-4.0958548786, 9.0000001341), (-4.2979274728, 9.3500001341))
            make_face()
            with BuildLine():
                CenterArc((-4.5000000671, 9.0000001341), 0.3000000045, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.2827433472, perimeter: 1.8849556202
            with Locations((-4.5000000671, 9.0000001341)):
                Circle(0.3000000045)
        # OneSide extrude, distance=0.7
        extrude(amount=0.7, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 6 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.75, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.21, perimeter: 2
            with BuildLine():
                Line((-4.6500226613, 8.6500001341), (-4.3500226613, 8.6500001341))
                Line((-4.3500226613, 9.3500001341), (-4.3500226613, 8.6500001341))
                Line((-4.3500226613, 9.3500001341), (-4.6500226613, 9.3500001341))
                Line((-4.6500226613, 8.6500001341), (-4.6500226613, 9.3500001341))
            make_face()
        # OneSide extrude, distance=0.7
        extrude(amount=0.7, mode=Mode.ADD)
    return part.part


def model_23493_57512264_0008():
    """Model: blaszka"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.1547562844, perimeter: 7.2256631033
            Circle(1.15)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            Circle(0.15)
        # OneSide extrude, distance=0.8
        extrude(amount=0.8, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -0.8, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.1256637061, perimeter: 2.5132741229
            with BuildLine():
                CenterArc((0, 0), 0.25, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            Circle(0.15)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 57 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0778539816, perimeter: 1.1141592654
            with BuildLine():
                CenterArc((0.6869513295, -0.4462961971), 0.05, 0, 90)
                Line((0.6869513295, -0.3962961971), (0.5869513295, -0.3962961971))
                CenterArc((0.5869513295, -0.4462961971), 0.05, 90, 90)
                Line((0.5369513295, -0.4462961971), (0.5369513295, -0.7462961971))
                CenterArc((0.5869513295, -0.7462961971), 0.05, -180, 90)
                Line((0.5869513295, -0.7962961971), (0.6869513295, -0.7962961971))
                CenterArc((0.6869513295, -0.7462961971), 0.05, -90, 90)
                Line((0.7369513295, -0.7462961971), (0.7369513295, -0.4462961971))
            make_face()
            # Profile area: 0.0778539816, perimeter: 1.1141592654
            with BuildLine():
                CenterArc((0.6869513295, 0.7537038029), 0.05, 0, 90)
                Line((0.5869513295, 0.8037038029), (0.6869513295, 0.8037038029))
                CenterArc((0.5869513295, 0.7537038029), 0.05, 90, 90)
                Line((0.5369513295, 0.4537038029), (0.5369513295, 0.7537038029))
                CenterArc((0.5869513295, 0.4537038029), 0.05, 180, 90)
                Line((0.6869513295, 0.4037038029), (0.5869513295, 0.4037038029))
                CenterArc((0.6869513295, 0.4537038029), 0.05, -90, 90)
                Line((0.7369513295, 0.7537038029), (0.7369513295, 0.4537038029))
            make_face()
            # Profile area: 0.0778539816, perimeter: 1.1141592654
            with BuildLine():
                CenterArc((-0.7130486705, 0.3906611771), 0.05, 90, 90)
                Line((-0.7630486705, 0.3906611771), (-0.7630486705, 0.0906611771))
                CenterArc((-0.7130486705, 0.0906611771), 0.05, 180, 90)
                Line((-0.7130486705, 0.0406611771), (-0.6130486705, 0.0406611771))
                CenterArc((-0.6130486705, 0.0906611771), 0.05, -90, 90)
                Line((-0.5630486705, 0.0906611771), (-0.5630486705, 0.3906611771))
                CenterArc((-0.6130486705, 0.3906611771), 0.05, 0, 90)
                Line((-0.6130486705, 0.4406611771), (-0.7130486705, 0.4406611771))
            make_face()
            # Profile area: 0.0778539816, perimeter: 1.1141592654
            with BuildLine():
                CenterArc((-0.6130486705, -0.0832535713), 0.05, 0, 90)
                Line((-0.7130486705, -0.0332535713), (-0.6130486705, -0.0332535713))
                CenterArc((-0.7130486705, -0.0832535713), 0.05, 90, 90)
                Line((-0.7630486705, -0.3832535713), (-0.7630486705, -0.0832535713))
                CenterArc((-0.7130486705, -0.3832535713), 0.05, -180, 90)
                Line((-0.6130486705, -0.4332535713), (-0.7130486705, -0.4332535713))
                CenterArc((-0.6130486705, -0.3832535713), 0.05, -90, 90)
                Line((-0.5630486705, -0.0832535713), (-0.5630486705, -0.3832535713))
            make_face()
        # OneSide extrude, distance=-0.08
        extrude(amount=-0.08, mode=Mode.SUBTRACT)
    return part.part


def model_23554_a0845d54_0002():
    """Model: serbatoio esterno v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 38.4845100065, perimeter: 21.9911485751
            Circle(3.5)
        # OneSide extrude, distance=13
        extrude(amount=13)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.3926990817, perimeter: 2.5707963268
            with BuildLine():
                Line((-1, 0), (-2, 0))
                CenterArc((-1.5, 0), 0.5, -180, 180)
            make_face()
            # Profile area: 0.3926990817, perimeter: 2.5707963268
            with BuildLine():
                CenterArc((-1.5, 0), 0.5, 0, 180)
                Line((-1, 0), (-2, 0))
            make_face()
            # Profile area: 0.3926990817, perimeter: 2.5707963268
            with BuildLine():
                CenterArc((1.5, 0), 0.5, 0, 180)
                Line((1, 0), (2, 0))
            make_face()
            # Profile area: 0.3926990817, perimeter: 2.5707963268
            with BuildLine():
                Line((1, 0), (2, 0))
                CenterArc((1.5, 0), 0.5, -180, 180)
            make_face()
        # OneSide extrude, distance=-2.5
        extrude(amount=-2.5, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 13, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 28.2743338823, perimeter: 18.8495559215
            Circle(3)
        # OneSide extrude, distance=-10
        extrude(amount=-10, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on YZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.7671458676, perimeter: 4.7123889804
            with Locations((0, 5)):
                Circle(0.75)
        # OneSide extrude, distance=7.5
        extrude(amount=7.5, mode=Mode.SUBTRACT)
    return part.part


def model_23596_d6a0ebb5_0000():
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
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 7.283920012, perimeter: 45.8829607057
            with BuildLine():
                CenterArc((0, 0), 3.81, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 3.4925, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=2.54
        extrude(amount=2.54, both=True)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on YZ construction plane
        # Sketch has 6 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.9793260902, perimeter: 13.1031958439
            with BuildLine():
                CenterArc((0, 0), 3.81, 45, 90)
                Line((2.6940768363, 2.6940768363), (2.9185832393, 2.9185832393))
                CenterArc((0, 0), 4.1275, 45, 90)
                Line((-2.6940768363, 2.6940768363), (-2.9185832393, 2.9185832393))
            make_face()
        # Symmetric extrude, each_side=2.286
        extrude(amount=2.286, both=True, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.2667686977, perimeter: 3.9898226701
            with Locations((0, -3.81)):
                Circle(0.635)
            # Profile area: 1.2667686977, perimeter: 3.9898226701
            with Locations((0, 3.81)):
                Circle(0.635)
        # Symmetric extrude, each_side=3.81
        extrude(amount=3.81, both=True, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on XZ construction plane
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1911927255, perimeter: 4.1258996073
            with BuildLine():
                _nurbs_edge([(-1.3196285505, -0.2613248011), (-1.3326135101, -0.2689480498), (-1.3599076366, -0.2849719666), (-1.3904387809, -0.2933798193), (-1.4064449806, -0.2977877042)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0449694572, 0.0945249033, 0.0945249033, 0.0945249033, 0.0945249033], 3)
                _nurbs_edge([(-1.2534000415, -0.1953443667), (-1.2634277229, -0.2083707423), (-1.2826114569, -0.2332912115), (-1.307669023, -0.252267675), (-1.3196285505, -0.2613248011)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0490612521, 0.0938579888, 0.0938579888, 0.0938579888, 0.0938579888], 3)
                _nurbs_edge([(-1.2037906784, -0.0894283435), (-1.2103238785, -0.1093127965), (-1.2225901306, -0.1466463714), (-1.2435866164, -0.1798333147), (-1.2534000415, -0.1953443667)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0625053824, 0.1173554726, 0.1173554726, 0.1173554726, 0.1173554726], 3)
                _nurbs_edge([(-1.1844430107, 0.0574153879), (-1.1850590971, 0.031235191), (-1.1862278409, -0.0184298361), (-1.198152113, -0.0666342062), (-1.2037906784, -0.0894283435)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0782842867, 0.1485088603, 0.1485088603, 0.1485088603, 0.1485088603], 3)
                _nurbs_edge([(-1.2129684228, 0.2303040841), (-1.2046535732, 0.2034881043), (-1.1872015242, 0.1472040086), (-1.1853909536, 0.088270586), (-1.1844430107, 0.0574153879)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0838253937, 0.1759412299, 0.1759412299, 0.1759412299, 0.1759412299], 3)
                _nurbs_edge([(-1.2990406889, 0.3545755962), (-1.2809834848, 0.3370172032), (-1.2441865635, 0.3012367579), (-1.223502354, 0.2542388826), (-1.2129684228, 0.2303040841)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0748049882, 0.1524374013, 0.1524374013, 0.1524374013, 0.1524374013], 3)
                _nurbs_edge([(-1.4057008166, 0.4066654065), (-1.3858321807, 0.4010689905), (-1.3471014397, 0.390159669), (-1.3147809586, 0.3662296568), (-1.2990406889, 0.3545755962)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0613456237, 0.119583522, 0.119583522, 0.119583522, 0.119583522], 3)
                _nurbs_edge([(-1.5351812977, 0.4170834044), (-1.5101848262, 0.4169801803), (-1.4667329341, 0.4168007438), (-1.4238953294, 0.4096868898), (-1.4057008166, 0.4066654065)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.074831465, 0.1300811091, 0.1300811091, 0.1300811091, 0.1300811091], 3)
                Line((-1.7857086573, 0.4170834044), (-1.5351812977, 0.4170834044))
                Line((-1.7857086573, -0.3101900598), (-1.7857086573, 0.4170834044))
                Line((-1.5232750613, -0.3101900598), (-1.7857086573, -0.3101900598))
                _nurbs_edge([(-1.4064449806, -0.2977877042), (-1.4245994524, -0.3014017505), (-1.4631544838, -0.3090769764), (-1.5024713784, -0.3098048966), (-1.5232750613, -0.3101900598)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0554185462, 0.1176935254, 0.1176935254, 0.1176935254, 0.1176935254], 3)
            make_face()
            with BuildLine():
                _nurbs_edge([(-1.3211168784, 0.2342728594), (-1.3336752786, 0.2527631285), (-1.3573715937, 0.2876522256), (-1.3946351503, 0.3071920836), (-1.4121500391, 0.3163763502)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0658664195, 0.1242826644, 0.1242826644, 0.1242826644, 0.1242826644], 3)
                _nurbs_edge([(-1.2836617965, 0.0589037159), (-1.2843192073, 0.0931028446), (-1.2854930511, 0.1541673047), (-1.3102326729, 0.2097980797), (-1.3211168784, 0.2342728594)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.1013266689, 0.1809244439, 0.1809244439, 0.1809244439, 0.1809244439], 3)
                _nurbs_edge([(-1.3027613897, -0.081242778), (-1.2971993246, -0.0600435441), (-1.285154738, -0.014136852), (-1.2841841676, 0.033347269), (-1.2836617965, 0.0589037159)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.065519185, 0.1418810262, 0.1418810262, 0.1418810262, 0.1418810262], 3)
                _nurbs_edge([(-1.3560914535, -0.1732681772), (-1.3451481669, -0.1603619158), (-1.3218803282, -0.1329203601), (-1.3093816911, -0.099137138), (-1.3027613897, -0.081242778)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0503666849, 0.107090671, 0.107090671, 0.107090671, 0.107090671], 3)
                _nurbs_edge([(-1.4213277835, -0.2109713337), (-1.4086487899, -0.2063145303), (-1.3846906163, -0.1975150541), (-1.3652458045, -0.1810293982), (-1.3560914535, -0.1732681772)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.040152233, 0.0758714923, 0.0758714923, 0.0758714923, 0.0758714923], 3)
                _nurbs_edge([(-1.5341891188, -0.2243658087), (-1.512678626, -0.2241556879), (-1.4745322524, -0.2237830631), (-1.4374845338, -0.2148619075), (-1.4213277835, -0.2109713337)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0642694265, 0.1139744022, 0.1139744022, 0.1139744022, 0.1139744022], 3)
                Line((-1.6894664604, -0.2243658087), (-1.5341891188, -0.2243658087))
                Line((-1.6894664604, 0.3312591532), (-1.6894664604, -0.2243658087))
                Line((-1.5366695959, 0.3312591532), (-1.6894664604, 0.3312591532))
                _nurbs_edge([(-1.4121500391, 0.3163763502), (-1.428896848, 0.3206836987), (-1.4696592384, 0.3311679542), (-1.5118263867, 0.3312253424), (-1.5366695959, 0.3312591532)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.051696944, 0.1258323921, 0.1258323921, 0.1258323921, 0.1258323921], 3)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0470462022, perimeter: 1.2322969437
            with BuildLine():
                Line((-0.9736031431, 0.2166615346), (-0.9736031431, -0.3101900598))
                Line((-1.0629000205, 0.2166615346), (-0.9736031431, 0.2166615346))
                Line((-1.0629000205, -0.3101900598), (-1.0629000205, 0.2166615346))
                Line((-0.9736031431, -0.3101900598), (-1.0629000205, -0.3101900598))
            make_face()
            # Profile area: 0.0091700224, perimeter: 0.3839765787
            with BuildLine():
                Line((-0.9736031431, 0.4170834044), (-0.9736031431, 0.3143919924))
                Line((-1.0629000205, 0.4170834044), (-0.9736031431, 0.4170834044))
                Line((-1.0629000205, 0.3143919924), (-1.0629000205, 0.4170834044))
                Line((-0.9736031431, 0.3143919924), (-1.0629000205, 0.3143919924))
            make_face()
            # Profile area: 0.1329188786, perimeter: 3.2884637663
            with BuildLine():
                _nurbs_edge([(-0.6159195442, -0.2486744305), (-0.6003613482, -0.2477544483), (-0.5702741627, -0.2459753426), (-0.5445175447, -0.230399201), (-0.53207977, -0.2228775403)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0459712331, 0.0889013757, 0.0889013757, 0.0889013757, 0.0889013757], 3)
                _nurbs_edge([(-0.7260523576, -0.2025376937), (-0.710325564, -0.2159939317), (-0.6785787172, -0.243157328), (-0.6369341649, -0.2468241058), (-0.6159195442, -0.2486744305)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0604848882, 0.1220976465, 0.1220976465, 0.1220976465, 0.1220976465], 3)
                _nurbs_edge([(-0.7751656312, -0.0695845863), (-0.7725851889, -0.0960380954), (-0.7678241582, -0.1448459937), (-0.7391742389, -0.1844148542), (-0.7260523576, -0.2025376937)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0780545318, 0.1440140753, 0.1440140753, 0.1440140753, 0.1440140753], 3)
                Line((-0.3822594423, -0.0695845863), (-0.7751656312, -0.0695845863))
                _nurbs_edge([(-0.3817632932, -0.0457720539), (-0.3817948284, -0.0490795498), (-0.3818705251, -0.0570188225), (-0.3821161465, -0.064954757), (-0.3822594423, -0.0695845863)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0099226844, 0.0238182902, 0.0238182902, 0.0238182902, 0.0238182902], 3)
                _nurbs_edge([(-0.4487360257, 0.1566341737), (-0.4292338837, 0.128737447), (-0.3869255676, 0.06821776), (-0.3835713658, -0.0058474299), (-0.3817632932, -0.0457720539)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.1000853511, 0.2171270555, 0.2171270555, 0.2171270555, 0.2171270555], 3)
                _nurbs_edge([(-0.6213765878, 0.2285677412), (-0.5880067044, 0.2258247093), (-0.5226111556, 0.2204491412), (-0.4730212926, 0.1776123232), (-0.4487360257, 0.1566341737)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.097664077, 0.1913940131, 0.1913940131, 0.1913940131, 0.1913940131], 3)
                _nurbs_edge([(-0.7989781637, 0.1551459053), (-0.774049639, 0.1765572471), (-0.7229816975, 0.2204199774), (-0.6557761369, 0.2258092244), (-0.6213765878, 0.2285677412)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0959954588, 0.1966538552, 0.1966538552, 0.1966538552, 0.1966538552], 3)
                _nurbs_edge([(-0.867439105, -0.0512290975), (-0.8655819295, -0.0105314107), (-0.8621346565, 0.0650112813), (-0.8189141564, 0.1266939897), (-0.7989781637, 0.1551459053)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.1193044095, 0.2214518068, 0.2214518068, 0.2214518068, 0.2214518068], 3)
                _nurbs_edge([(-0.799722268, -0.2509068629), (-0.819444084, -0.223394918), (-0.8620510728, -0.1639581436), (-0.8655563446, -0.0906204328), (-0.867439105, -0.0512290975)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0994588633, 0.2148708148, 0.2148708148, 0.2148708148, 0.2148708148], 3)
                _nurbs_edge([(-0.6164156932, -0.322096326), (-0.6523748461, -0.3197134323), (-0.7211397357, -0.3151566111), (-0.7743413291, -0.2716585349), (-0.799722268, -0.2509068629)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.1051388706, 0.2010576515, 0.2010576515, 0.2010576515, 0.2010576515], 3)
                _nurbs_edge([(-0.4656031865, -0.2774478576), (-0.4874434033, -0.290458508), (-0.5338092817, -0.3180795817), (-0.5878371506, -0.3207066918), (-0.6164156932, -0.322096326)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0750996246, 0.1594334021, 0.1594334021, 0.1594334021, 0.1594334021], 3)
                _nurbs_edge([(-0.38473983, -0.1519361517), (-0.3932173988, -0.1771116177), (-0.4096230454, -0.2258307501), (-0.4473645106, -0.260630685), (-0.4656031865, -0.2774478576)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0782667961, 0.1514605689, 0.1514605689, 0.1514605689, 0.1514605689], 3)
                Line((-0.4770133037, -0.1405259749), (-0.38473983, -0.1519361517))
                _nurbs_edge([(-0.53207977, -0.2228775403), (-0.5208647205, -0.2122917531), (-0.4963025342, -0.1891077199), (-0.4838046673, -0.1576306644), (-0.4770133037, -0.1405259749)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0457209679, 0.1001339262, 0.1001339262, 0.1001339262, 0.1001339262], 3)
            make_face()
            with BuildLine():
                _nurbs_edge([(-0.6203844089, 0.1551459053), (-0.6399808399, 0.1535200365), (-0.6786770546, 0.1503095045), (-0.7089016076, 0.1259791605), (-0.7238199252, 0.1139701226)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0575448717, 0.1136313396, 0.1136313396, 0.1136313396, 0.1136313396], 3)
                _nurbs_edge([(-0.5097554464, 0.1035521248), (-0.5250799942, 0.1186002295), (-0.5558632526, 0.1488281815), (-0.5988149579, 0.1530338875), (-0.6203844089, 0.1551459053)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0624281996, 0.1254029435, 0.1254029435, 0.1254029435, 0.1254029435], 3)
                _nurbs_edge([(-0.4760211248, 0.0038373092), (-0.4782795855, 0.0237786647), (-0.4823351061, 0.0595873814), (-0.5013359134, 0.0900525619), (-0.5097554464, 0.1035521248)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0592754942, 0.1064410782, 0.1064410782, 0.1064410782, 0.1064410782], 3)
                Line((-0.7702047366, 0.0038373092), (-0.4760211248, 0.0038373092))
                _nurbs_edge([(-0.7238199252, 0.1139701226), (-0.7362570548, 0.0986132414), (-0.762294865, 0.0664627714), (-0.7674907171, 0.0253252341), (-0.7702047366, 0.0038373092)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0580994351, 0.1216343422, 0.1216343422, 0.1216343422, 0.1216343422], 3)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.1692704467, perimeter: 4.115577622
            with BuildLine():
                _nurbs_edge([(-0.0806344289, -0.5240064642), (-0.1097168765, -0.5228115561), (-0.1639509174, -0.5205832465), (-0.2110790083, -0.4939444862), (-0.2329351444, -0.4815904877)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0858613291, 0.1601174322, 0.1601174322, 0.1601174322, 0.1601174322], 3)
                _nurbs_edge([(0.0530628424, -0.4942408583), (0.0331522032, -0.5029127628), (-0.0094203157, -0.5214548507), (-0.0558952468, -0.5231200552), (-0.0806344289, -0.5240064642)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.064567583, 0.138057077, 0.138057077, 0.138057077, 0.138057077], 3)
                _nurbs_edge([(0.132437871, -0.4131295463), (0.1226782251, -0.4294478745), (0.1027261104, -0.4628082196), (0.0698549573, -0.483612873), (0.0530628424, -0.4942408583)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0562076156, 0.1149079384, 0.1149079384, 0.1149079384, 0.1149079384], 3)
                _nurbs_edge([(0.1574906569, -0.2387525818), (0.1575143286, -0.274134739), (0.1575541349, -0.3336334557), (0.1396819764, -0.3902010542), (0.132437871, -0.4131295463)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.1052963711, 0.1770666191, 0.1770666191, 0.1770666191, 0.1770666191], 3)
                Line((0.1574906569, 0.2166615346), (0.1574906569, -0.2387525818))
                Line((0.0751390916, 0.2166615346), (0.1574906569, 0.2166615346))
                Line((0.0751390916, 0.1531615475), (0.0751390916, 0.2166615346))
                _nurbs_edge([(-0.0786499519, 0.2285678008), (-0.04882239, 0.2252961233), (0.0114650266, 0.2186834144), (0.0537665176, 0.175154347), (0.0751390916, 0.1531615475)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0871435137, 0.1761343194, 0.1761343194, 0.1761343194, 0.1761343194], 3)
                _nurbs_edge([(-0.200440957, 0.1938412407), (-0.1820704734, 0.2039672084), (-0.1441753481, 0.2248553256), (-0.1009307787, 0.227305435), (-0.0786499519, 0.2285678008)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0620947257, 0.128090662, 0.128090662, 0.128090662, 0.128090662], 3)
                _nurbs_edge([(-0.2795680303, 0.0953666189), (-0.2697044494, 0.1152330741), (-0.2505155214, 0.1538819162), (-0.2168174104, 0.1807728891), (-0.200440957, 0.1938412407)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0656400229, 0.1276982159, 0.1276982159, 0.1276982159, 0.1276982159], 3)
                _nurbs_edge([(-0.3068531293, -0.0437876961), (-0.3058177918, -0.0193781302), (-0.3037908984, 0.0284087852), (-0.2875252045, 0.0733710755), (-0.2795680303, 0.0953666189)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0728119188, 0.1425448127, 0.1425448127, 0.1425448127, 0.1425448127], 3)
                _nurbs_edge([(-0.2473219175, -0.2318072697), (-0.2646810887, -0.2038725871), (-0.3004422427, -0.1463251112), (-0.3046750238, -0.0786248909), (-0.3068531293, -0.0437876961)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0970736494, 0.1999787711, 0.1999787711, 0.1999787711, 0.1999787711], 3)
                _nurbs_edge([(-0.0791461009, -0.3101900598), (-0.1130066267, -0.3073193139), (-0.1788219266, -0.3017393946), (-0.2249336585, -0.2546636016), (-0.2473219175, -0.2318072697)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0983384559, 0.1911421877, 0.1911421877, 0.1911421877, 0.1911421877], 3)
                _nurbs_edge([(0.0667055112, -0.2412330291), (0.046144591, -0.2613448871), (0.0054372113, -0.3011631944), (-0.051143689, -0.307201598), (-0.0791461009, -0.3101900598)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0836389242, 0.1655918808, 0.1655918808, 0.1655918808, 0.1655918808], 3)
                _nurbs_edge([(0.0602562886, -0.3558307072), (0.0622157923, -0.3417517242), (0.0675020511, -0.3037700912), (0.0670131727, -0.2653878133), (0.0667055112, -0.2412330291)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0425965997, 0.1149151477, 0.1149151477, 0.1149151477, 0.1149151477], 3)
                _nurbs_edge([(0.0146157008, -0.4252837679), (0.0250001909, -0.4159983766), (0.0463416516, -0.3969157051), (0.0555358653, -0.3697684465), (0.0602562886, -0.3558307072)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0410560895, 0.0843755361, 0.0843755361, 0.0843755361, 0.0843755361], 3)
                _nurbs_edge([(-0.0811304588, -0.4500884792), (-0.0623899006, -0.4495616176), (-0.0284496437, -0.4486074401), (0.0012949671, -0.4324981169), (0.0146157008, -0.4252837679)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0552913311, 0.100135864, 0.100135864, 0.100135864, 0.100135864], 3)
                _nurbs_edge([(-0.1719156045, -0.4252837679), (-0.1591044907, -0.4325039197), (-0.1310236805, -0.4483298436), (-0.0987047481, -0.4494690209), (-0.0811304588, -0.4500884792)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0434948058, 0.0953367055, 0.0953367055, 0.0953367055, 0.0953367055], 3)
                _nurbs_edge([(-0.2021773595, -0.3667447349), (-0.1999102857, -0.3789457513), (-0.1956980954, -0.4016150638), (-0.1794285835, -0.4178067346), (-0.1719156045, -0.4252837679)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0362202118, 0.0672966311, 0.0672966311, 0.0672966311, 0.0672966311], 3)
                Line((-0.2889937896, -0.3538462898), (-0.2021773595, -0.3667447349))
                _nurbs_edge([(-0.2329351444, -0.4815904877), (-0.2497541202, -0.4650005612), (-0.2851983418, -0.430039037), (-0.2876863762, -0.3800923158), (-0.2889937896, -0.3538462898)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0683842003, 0.144112506, 0.144112506, 0.144112506, 0.144112506], 3)
            make_face()
            with BuildLine():
                _nurbs_edge([(-0.0722007293, 0.1546498159), (-0.0914338376, 0.1524772276), (-0.1306888665, 0.1480429461), (-0.158976104, 0.12038666), (-0.1734039325, 0.1062806466)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0563785353, 0.1150693378, 0.1150693378, 0.1150693378, 0.1150693378], 3)
                _nurbs_edge([(0.0312347871, 0.1055365422), (0.0164217308, 0.1198593285), (-0.0125831524, 0.1479042326), (-0.0526139985, 0.1524336251), (-0.0722007293, 0.1546498159)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0599626825, 0.1174106528, 0.1174106528, 0.1174106528, 0.1174106528], 3)
                _nurbs_edge([(0.0741469126, -0.0403150698), (0.0732610812, -0.0111890821), (0.0716605678, 0.0414355279), (0.0437138966, 0.0857490808), (0.0312347871, 0.1055365422)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0855077219, 0.1544946922, 0.1544946922, 0.1544946922, 0.1544946922], 3)
                _nurbs_edge([(0.0324750405, -0.1888951442), (0.0445793568, -0.1691322805), (0.0723224182, -0.1238358482), (0.0734891991, -0.0704235478), (0.0741469126, -0.0403150698)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0683924322, 0.1567552769, 0.1567552769, 0.1567552769, 0.1567552769], 3)
                _nurbs_edge([(-0.0707125205, -0.2362720749), (-0.0509844889, -0.2342412527), (-0.0112395955, -0.2301498758), (0.0178330705, -0.2027131831), (0.0324750405, -0.1888951442)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0577816423, 0.1164092424, 0.1164092424, 0.1164092424, 0.1164092424], 3)
                _nurbs_edge([(-0.1738999624, -0.1886470696), (-0.159351838, -0.2025376134), (-0.1303814722, -0.2301985081), (-0.0905444708, -0.2342534258), (-0.0707125205, -0.2362720749)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0585437271, 0.1165808837, 0.1165808837, 0.1165808837, 0.1165808837], 3)
                _nurbs_edge([(-0.2150758046, -0.0373384735), (-0.2144920169, -0.0680759422), (-0.2134623064, -0.1222920367), (-0.1858553368, -0.1685951924), (-0.1738999624, -0.1886470696)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0902579262, 0.1592008864, 0.1592008864, 0.1592008864, 0.1592008864], 3)
                _nurbs_edge([(-0.1734039325, 0.1062806466), (-0.1855215176, 0.0867800786), (-0.2126989291, 0.0430440572), (-0.2142283218, -0.0086778172), (-0.2150758046, -0.0373384735)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0677313161, 0.1519083078, 0.1519083078, 0.1519083078, 0.1519083078], 3)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0246337948, perimeter: 0.7282657623
            with BuildLine():
                Line((0.5320414763, -0.0021158239), (0.5320414763, -0.0919087908))
                Line((0.257701562, -0.0021158239), (0.5320414763, -0.0021158239))
                Line((0.257701562, -0.0919087908), (0.257701562, -0.0021158239))
                Line((0.5320414763, -0.0919087908), (0.257701562, -0.0919087908))
            make_face()
            # Profile area: 0.0470461708, perimeter: 1.2322968245
            with BuildLine():
                Line((0.720556901, 0.2166615346), (0.720556901, -0.3101900598))
                Line((0.6312600833, 0.2166615346), (0.720556901, 0.2166615346))
                Line((0.6312600833, -0.3101900598), (0.6312600833, 0.2166615346))
                Line((0.720556901, -0.3101900598), (0.6312600833, -0.3101900598))
            make_face()
            # Profile area: 0.0091700163, perimeter: 0.3839764595
            with BuildLine():
                Line((0.720556901, 0.4170834044), (0.720556901, 0.3143919924))
                Line((0.6312600833, 0.4170834044), (0.720556901, 0.4170834044))
                Line((0.6312600833, 0.3143919924), (0.6312600833, 0.4170834044))
                Line((0.720556901, 0.3143919924), (0.6312600833, 0.3143919924))
            make_face()
            # Profile area: 0.0987428556, perimeter: 2.5661116766
            with BuildLine():
                _nurbs_edge([(1.067822383, -0.2486744305), (1.0844610903, -0.2474802277), (1.1168731835, -0.2451539284), (1.1429437285, -0.2258315685), (1.155630992, -0.2164283177)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.04891384, 0.095283841, 0.095283841, 0.095283841, 0.095283841], 3)
                _nurbs_edge([(0.9616584044, -0.2005533358), (0.9763704737, -0.2145881815), (1.0061247948, -0.2429728565), (1.0471049353, -0.2467598977), (1.067822383, -0.2486744305)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0591637694, 0.1196553496, 0.1196553496, 0.1196553496, 0.1196553496], 3)
                _nurbs_edge([(0.9209787112, -0.046268203), (0.9215000267, -0.0776500917), (0.9224151893, -0.13274059), (0.9498511379, -0.1801502379), (0.9616584044, -0.2005533358)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.092215773, 0.1618835923, 0.1618835923, 0.1618835923, 0.1618835923], 3)
                _nurbs_edge([(0.9631466132, 0.1067767361), (0.9509014941, 0.086474042), (0.9227003519, 0.039715888), (0.9216008195, -0.0151981799), (0.9209787112, -0.046268203)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0699975773, 0.1612080389, 0.1612080389, 0.1612080389, 0.1612080389], 3)
                _nurbs_edge([(1.0727833968, 0.1551459053), (1.05145253, 0.1532489613), (1.0093954589, 0.1495088457), (0.9784144217, 0.1208835891), (0.9631466132, 0.1067767361)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0623276719, 0.1228885522, 0.1228885522, 0.1228885522, 0.1228885522], 3)
                _nurbs_edge([(1.1489338141, 0.1283568361), (1.1377347929, 0.1361693468), (1.1148553827, 0.1521301736), (1.087002726, 0.1541266598), (1.0727833968, 0.1551459053)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0401737201, 0.0820742286, 0.0820742286, 0.0820742286, 0.0820742286], 3)
                _nurbs_edge([(1.1928381186, 0.0484857777), (1.1883494193, 0.0646881372), (1.1799905159, 0.0948603429), (1.158762477, 0.1177560408), (1.1489338141, 0.1283568361)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0495794352, 0.0923273499, 0.0923273499, 0.0923273499, 0.0923273499], 3)
                Line((1.2796544295, 0.0618802527), (1.1928381186, 0.0484857777))
                _nurbs_edge([(1.2097052794, 0.185159556), (1.2263563489, 0.1686492301), (1.2611263472, 0.134173126), (1.2733069949, 0.0866466735), (1.2796544295, 0.0618802527)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0690170209, 0.1441181724, 0.1441181724, 0.1441181724, 0.1441181724], 3)
                _nurbs_edge([(1.0693108302, 0.2285677412), (1.0960349369, 0.2272027316), (1.1466349727, 0.2246181911), (1.1894858412, 0.19780943), (1.2097052794, 0.185159556)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0787619913, 0.1491297586, 0.1491297586, 0.1491297586, 0.1491297586], 3)
                _nurbs_edge([(0.9435509902, 0.1965697029), (0.9633228667, 0.2059023171), (1.0031635125, 0.2247076832), (1.0471524557, 0.2272746788), (1.0693108302, 0.2285677412)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0649347346, 0.1308445232, 0.1308445232, 0.1308445232, 0.1308445232], 3)
                _nurbs_edge([(0.8574787837, 0.1005755881), (0.8679807157, 0.1204882629), (0.8886633384, 0.1597045079), (0.9254455393, 0.1844092086), (0.9435509902, 0.1965697029)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0663853531, 0.1307400582, 0.1307400582, 0.1307400582, 0.1307400582], 3)
                _nurbs_edge([(0.8292013865, -0.0487485906), (0.830119399, -0.021803182), (0.8318661857, 0.0294683191), (0.8492370607, 0.07769441), (0.8574787837, 0.1005755881)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0803068555, 0.1528072213, 0.1528072213, 0.1528072213, 0.1528072213], 3)
                _nurbs_edge([(0.8949338656, -0.2514029524), (0.8757991501, -0.2236588543), (0.8339283731, -0.1629489396), (0.83086488, -0.0889373109), (0.8292013865, -0.0487485906)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0991373107, 0.2169332612, 0.2169332612, 0.2169332612, 0.2169332612], 3)
                _nurbs_edge([(1.0688146811, -0.322096326), (1.0349129737, -0.3195494072), (0.9692261979, -0.3146145853), (0.9191602141, -0.2720159416), (0.8949338656, -0.2514029524)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0991323139, 0.192075343, 0.192075343, 0.192075343, 0.192075343], 3)
                _nurbs_edge([(1.2144180995, -0.2707506201), (1.1931691806, -0.2857235388), (1.1495206127, -0.3164802312), (1.0961853601, -0.3201916788), (1.0688146811, -0.322096326)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0764497481, 0.1570396144, 0.1570396144, 0.1570396144, 0.1570396144], 3)
                _nurbs_edge([(1.2880882483, -0.1286197683), (1.2818822833, -0.1568265269), (1.2699867061, -0.2108931663), (1.2323970824, -0.2513839991), (1.2144180995, -0.2707506201)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0848812907, 0.1627002312, 0.1627002312, 0.1627002312, 0.1627002312], 3)
                Line((1.2002796393, -0.1172095916), (1.2880882483, -0.1286197683))
                _nurbs_edge([(1.155630992, -0.2164283177), (1.166401992, -0.2033402128), (1.1901796074, -0.1744474523), (1.1967083473, -0.13744845), (1.2002796393, -0.1172095916)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0500299336, 0.1104440182, 0.1104440182, 0.1104440182, 0.1104440182], 3)
            make_face()
            # Profile area: 0.1359518155, perimeter: 3.3629027168
            with BuildLine():
                Line((1.8194047671, -0.3101900598), (1.7261392337, -0.3101900598))
                _nurbs_edge([(1.7968324881, -0.2469380876), (1.7992235661, -0.2578644114), (1.8040478569, -0.2799095997), (1.8142560778, -0.3000379733), (1.8194047671, -0.3101900598)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0334064691, 0.0674016183, 0.0674016183, 0.0674016183, 0.0674016183], 3)
                _nurbs_edge([(1.7911273699, -0.0894283435), (1.7909221007, -0.1233382149), (1.7906036705, -0.1759419544), (1.795199324, -0.2283232646), (1.7968324881, -0.2469380876)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.1016471908, 0.1576833566, 0.1576833566, 0.1576833566, 0.1576833566], 3)
                Line((1.7911273699, 0.0296341398), (1.7911273699, -0.0894283435))
                _nurbs_edge([(1.7866625052, 0.111985735), (1.7879499191, 0.1013305507), (1.7912527544, 0.0739948835), (1.791174886, 0.0464452109), (1.7911273699, 0.0296341398)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0321728054, 0.0825387042, 0.0825387042, 0.0825387042, 0.0825387042], 3)
                _nurbs_edge([(1.7588814955, 0.1727572301), (1.7650557246, 0.1639390582), (1.7780315661, 0.1454066715), (1.7836942615, 0.1234794418), (1.7866625052, 0.111985735)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0320248719, 0.0673038945, 0.0673038945, 0.0673038945, 0.0673038945], 3)
                _nurbs_edge([(1.6968697768, 0.2126927593), (1.7095937419, 0.2075174869), (1.7328213496, 0.1980700233), (1.7507665737, 0.1806394322), (1.7588814955, 0.1727572301)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0407402414, 0.074371341, 0.074371341, 0.074371341, 0.074371341], 3)
                _nurbs_edge([(1.5872329932, 0.2285677412), (1.6077645991, 0.2282219923), (1.6450284221, 0.2275944757), (1.6808052506, 0.2173104823), (1.6968697768, 0.2126927593)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0612720662, 0.111205691, 0.111205691, 0.111205691, 0.111205691], 3)
                _nurbs_edge([(1.4676744204, 0.2099642375), (1.4861129094, 0.2153858669), (1.5251204231, 0.2268555857), (1.565788394, 0.2279766131), (1.5872329932, 0.2285677412)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0574078285, 0.1214490325, 0.1214490325, 0.1214490325, 0.1214490325], 3)
                _nurbs_edge([(1.3887953025, 0.1568822482), (1.3993557694, 0.1678701843), (1.4217840797, 0.1912063532), (1.4517945238, 0.2034732579), (1.4676744204, 0.2099642375)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0452094171, 0.0960157202, 0.0960157202, 0.0960157202, 0.0960157202], 3)
                _nurbs_edge([(1.3496040564, 0.0663451174), (1.3538627104, 0.0836715869), (1.3618340019, 0.1161030406), (1.3802281898, 0.1439244139), (1.3887953025, 0.1568822482)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0530555348, 0.0993086401, 0.0993086401, 0.0993086401, 0.0993086401], 3)
                Line((1.4369165164, 0.0544388512), (1.3496040564, 0.0663451174))
                _nurbs_edge([(1.4813169699, 0.1325736263), (1.4717565835, 0.1228938797), (1.4500775428, 0.1009441787), (1.4416355935, 0.0711140117), (1.4369165164, 0.0544388512)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0402020258, 0.0911617291, 0.0911617291, 0.0911617291, 0.0911617291], 3)
                _nurbs_edge([(1.5743345481, 0.1546498159), (1.5556794951, 0.1543594162), (1.5228926078, 0.153849029), (1.4938394771, 0.1389817392), (1.4813169699, 0.1325736263)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0550338415, 0.0967238402, 0.0967238402, 0.0967238402, 0.0967238402], 3)
                _nurbs_edge([(1.6760336619, 0.1243880907), (1.6622475066, 0.1331888383), (1.6314085418, 0.1528756864), (1.5946568677, 0.1540181021), (1.5743345481, 0.1546498159)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0482159648, 0.1078567892, 0.1078567892, 0.1078567892, 0.1078567892], 3)
                _nurbs_edge([(1.7013344031, 0.0474935988), (1.7009781264, 0.0636295668), (1.7003499262, 0.0920811066), (1.6833795024, 0.1146282876), (1.6760336619, 0.1243880907)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0469369384, 0.0827609582, 0.0827609582, 0.0827609582, 0.0827609582], 3)
                _nurbs_edge([(1.7008384925, 0.0241771558), (1.700978346, 0.0291791207), (1.7011956243, 0.0369502366), (1.701297943, 0.0447236346), (1.7013344031, 0.0474935988)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0150114486, 0.0233219761, 0.0233219761, 0.0233219761, 0.0233219761], 3)
                _nurbs_edge([(1.5415922862, -0.0065806886), (1.5730696681, -0.0027699801), (1.626905894, 0.0037475304), (1.679143553, 0.0181822429), (1.7008384925, 0.0241771558)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0949442994, 0.1623846211, 0.1623846211, 0.1623846211, 0.1623846211], 3)
                _nurbs_edge([(1.4622172576, -0.0199751636), (1.4731885797, -0.0175553808), (1.4994171592, -0.0117705297), (1.5260815284, -0.0084893579), (1.5415922862, -0.0065806886)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0336880427, 0.0805362838, 0.0805362838, 0.0805362838, 0.0805362838], 3)
                _nurbs_edge([(1.3979732257, -0.0492447397), (1.4078880798, -0.0431589386), (1.4280927359, -0.030757191), (1.4507025565, -0.0236133633), (1.4622172576, -0.0199751636)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0347596357, 0.0708337684, 0.0708337684, 0.0708337684, 0.0708337684], 3)
                _nurbs_edge([(1.3518363696, -0.1005904457), (1.3580878202, -0.0905019856), (1.3704047002, -0.0706252626), (1.3888767111, -0.0562994601), (1.3979732257, -0.0492447397)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0352873266, 0.0695246265, 0.0695246265, 0.0695246265, 0.0695246265], 3)
                _nurbs_edge([(1.3342251044, -0.1712838194), (1.3349134896, -0.1587477373), (1.3362697336, -0.1340493761), (1.3467001112, -0.1116303204), (1.3518363696, -0.1005904457)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0372819365, 0.0734521942, 0.0734521942, 0.0734521942, 0.0734521942], 3)
                _nurbs_edge([(1.3808578711, -0.2796802899), (1.3672572957, -0.2644201619), (1.339697897, -0.2334979442), (1.3360651096, -0.1922008031), (1.3342251044, -0.1712838194)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0596389036, 0.1208487344, 0.1208487344, 0.1208487344, 0.1208487344], 3)
                _nurbs_edge([(1.5143071871, -0.322096326), (1.4878841153, -0.3210388136), (1.439300927, -0.319094402), (1.3991649735, -0.2920266359), (1.3808578711, -0.2796802899)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0774994225, 0.1424955078, 0.1424955078, 0.1424955078, 0.1424955078], 3)
                _nurbs_edge([(1.6127816897, -0.3047330162), (1.5970561039, -0.3097968371), (1.5650363391, -0.3201075727), (1.5314159102, -0.3214256066), (1.5143071871, -0.322096326)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0493133554, 0.100409744, 0.100409744, 0.100409744, 0.100409744], 3)
                _nurbs_edge([(1.7082797747, -0.2452018043), (1.6925343099, -0.257972798), (1.6631532393, -0.2818034992), (1.6287486739, -0.2974647221), (1.6127816897, -0.3047330162)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0605248996, 0.1129395901, 0.1129395901, 0.1129395901, 0.1129395901], 3)
                _nurbs_edge([(1.7261392337, -0.3101900598), (1.7218955959, -0.3002671741), (1.7129846895, -0.2794308274), (1.7098970098, -0.2569674538), (1.7082797747, -0.2452018043)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0322253306, 0.0676676303, 0.0676676303, 0.0676676303, 0.0676676303], 3)
            make_face()
            with BuildLine():
                _nurbs_edge([(1.6274165374, -0.2295748374), (1.6398713598, -0.2214628459), (1.6643992283, -0.205487519), (1.6791774841, -0.1802389305), (1.6864516001, -0.1678111336)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0439192187, 0.0864921859, 0.0864921859, 0.0864921859, 0.0864921859], 3)
                _nurbs_edge([(1.5356392127, -0.2521470568), (1.5521506097, -0.2513229767), (1.584224141, -0.2497221942), (1.6133059783, -0.2361567937), (1.6274165374, -0.2295748374)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0490669188, 0.0953129136, 0.0953129136, 0.0953129136, 0.0953129136], 3)
                _nurbs_edge([(1.4565121394, -0.2283345839), (1.4672994788, -0.2352617406), (1.4912791575, -0.2506604396), (1.5198958409, -0.2516194567), (1.5356392127, -0.2521470568)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0377872021, 0.08399893, 0.08399893, 0.08399893, 0.08399893], 3)
                _nurbs_edge([(1.4294749957, -0.1688033125), (1.4306125873, -0.1802232353), (1.4328934114, -0.2031197085), (1.4486262599, -0.2199157788), (1.4565121394, -0.2283345839)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0334325911, 0.0670309627, 0.0670309627, 0.0670309627, 0.0670309627], 3)
                _nurbs_edge([(1.4418775302, -0.126387336), (1.4382601647, -0.1329536614), (1.4309797774, -0.1461691888), (1.4299786822, -0.1612271278), (1.4294749957, -0.1688033125)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0221968881, 0.0446739324, 0.0446739324, 0.0446739324, 0.0446739324], 3)
                _nurbs_edge([(1.4771000605, -0.0973658344), (1.469979068, -0.100977167), (1.4560656542, -0.1080332008), (1.4465318566, -0.1203663753), (1.4418775302, -0.126387336)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0236202296, 0.0461505929, 0.0461505929, 0.0461505929, 0.0461505929], 3)
                _nurbs_edge([(1.5549868804, -0.0795064947), (1.5391863584, -0.0817700497), (1.5127028344, -0.0855640328), (1.4873335837, -0.0939735703), (1.4771000605, -0.0973658344)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0477555179, 0.0800438371, 0.0800438371, 0.0800438371, 0.0800438371], 3)
                _nurbs_edge([(1.7008384925, -0.0457720539), (1.6807012394, -0.0523889714), (1.6331386252, -0.0680176122), (1.5835693273, -0.0753046643), (1.5549868804, -0.0795064947)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0634830289, 0.1499419414, 0.1499419414, 0.1499419414, 0.1499419414], 3)
                Line((1.7008384925, -0.0785142562), (1.7008384925, -0.0457720539))
                _nurbs_edge([(1.6864516001, -0.1678111336), (1.6906263531, -0.1554282376), (1.7003669421, -0.1265363), (1.7006670238, -0.0959763888), (1.7008384925, -0.0785142562)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0389783226, 0.0909447406, 0.0909447406, 0.0909447406, 0.0909447406], 3)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-3.556
        extrude(amount=-3.556, mode=Mode.SUBTRACT)
    return part.part


def model_23635_3815ae50_0000():
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
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 7.283920012, perimeter: 45.8829607057
            with BuildLine():
                CenterArc((0, 0), 3.81, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 3.4925, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=2.54
        extrude(amount=2.54, both=True)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on YZ construction plane
        # Sketch has 9 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.9793260902, perimeter: 13.1031958439
            with BuildLine():
                CenterArc((0, 0), 3.81, 45, 90)
                Line((2.9185832393, 2.9185832393), (2.6940768363, 2.6940768363))
                CenterArc((0, 0), 4.1275, 45, 90)
                Line((-2.6940768363, 2.6940768363), (-2.9185832393, 2.9185832393))
            make_face()
        # Symmetric extrude, each_side=2.286
        extrude(amount=2.286, both=True, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.2667686977, perimeter: 3.9898226701
            with Locations((0, -3.81)):
                Circle(0.635)
            # Profile area: 1.2667686977, perimeter: 3.9898226701
            with Locations((-0.0002773366, 3.8099999899)):
                Circle(0.635)
        # Symmetric extrude, each_side=3.81
        extrude(amount=3.81, both=True, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on XZ construction plane
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1359083765, perimeter: 3.3630282879
            with BuildLine():
                Line((1.2078385743, -0.3265107978), (1.1145728024, -0.3265107978))
                _nurbs_edge([(1.1850181016, -0.2635069001), (1.1874856357, -0.2743682904), (1.1924718652, -0.2963162681), (1.2026814196, -0.3163773424), (1.2078385743, -0.3265107978)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0332746291, 0.0672391655, 0.0672391655, 0.0672391655, 0.0672391655], 3)
                _nurbs_edge([(1.1795611772, -0.1057490814), (1.1793673993, -0.1396768043), (1.1790665324, -0.192354263), (1.1834558066, -0.244829236), (1.1850181016, -0.2635069001)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.1017083232, 0.1579161682, 0.1579161682, 0.1579161682, 0.1579161682], 3)
                Line((1.1795611772, 0.0133134019), (1.1795611772, -0.1057490814))
                _nurbs_edge([(1.1750963124, 0.095664997), (1.1763837263, 0.0850098128), (1.1796865616, 0.0576741455), (1.1796086932, 0.0301244729), (1.1795611772, 0.0133134019)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0321728054, 0.0825387042, 0.0825387042, 0.0825387042, 0.0825387042], 3)
                _nurbs_edge([(1.1473150643, 0.1561884474), (1.1534910057, 0.1474342629), (1.1664927188, 0.1290047816), (1.1721344559, 0.1071424871), (1.1750963124, 0.095664997)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0318670149, 0.0670870665, 0.0670870665, 0.0670870665, 0.0670870665], 3)
                _nurbs_edge([(1.0853033456, 0.1963720214), (1.0980348864, 0.1911826863), (1.1213074094, 0.1816968809), (1.1392074687, 0.1641404163), (1.1473150643, 0.1561884474)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0407675479, 0.0745207285, 0.0745207285, 0.0745207285, 0.0745207285], 3)
                _nurbs_edge([(0.975666562, 0.2122470629), (0.9961982517, 0.2119013353), (1.0334620889, 0.2112738598), (1.0692389001, 0.2009897677), (1.0853033456, 0.1963720214)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0612723041, 0.1112057116, 0.1112057116, 0.1112057116, 0.1112057116], 3)
                _nurbs_edge([(0.8561079892, 0.1933954846), (0.8745431734, 0.1988894819), (0.9135288592, 0.2105078768), (0.954218078, 0.2116467364), (0.975666562, 0.2122470629)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.057453339, 0.1214990747, 0.1214990747, 0.1214990747, 0.1214990747], 3)
                _nurbs_edge([(0.7772291097, 0.1403134357), (0.7877793492, 0.1513578165), (0.8101511342, 0.1747774282), (0.8402194798, 0.1869587264), (0.8561079892, 0.1933954846)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0452932569, 0.0960443603, 0.0960443603, 0.0960443603, 0.0960443603], 3)
                _nurbs_edge([(0.7380377444, 0.0500243794), (0.7422897118, 0.0673345714), (0.7502397701, 0.0997000685), (0.7686604494, 0.1274193764), (0.7772291097, 0.1403134357)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0529963224, 0.0990891561, 0.0990891561, 0.0990891561, 0.0990891561], 3)
                Line((0.8253500852, 0.0381181132), (0.7380377444, 0.0500243794))
                _nurbs_edge([(0.8695025834, 0.1160048436), (0.860011388, 0.1063821278), (0.8384292825, 0.0845009567), (0.8300464094, 0.0547727187), (0.8253500852, 0.0381181132)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0399397791, 0.0908193851, 0.0908193851, 0.0908193851, 0.0908193851], 3)
                _nurbs_edge([(0.9627681169, 0.1383290779), (0.944088527, 0.1380226281), (0.9111928819, 0.1374829554), (0.8820827192, 0.1224859093), (0.8695025834, 0.1160048436)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0551015281, 0.0970364088, 0.0970364088, 0.0970364088, 0.0970364088], 3)
                _nurbs_edge([(1.0644674691, 0.1080673527), (1.0506813132, 0.1168680994), (1.0198422794, 0.1365549886), (0.9830905198, 0.1376973777), (0.9627681169, 0.1383290779)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0482159648, 0.1078570257, 0.1078570257, 0.1078570257, 0.1078570257], 3)
                _nurbs_edge([(1.0897682103, 0.0311728608), (1.0894120438, 0.0473088199), (1.0887840359, 0.0757604288), (1.071813421, 0.0983075412), (1.0644674691, 0.1080673527)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0469368472, 0.0827610439, 0.0827610439, 0.0827610439, 0.0827610439], 3)
                _nurbs_edge([(1.0892720612, 0.0078564178), (1.0894120199, 0.0128583821), (1.0896294613, 0.0206294959), (1.089731758, 0.0284028964), (1.0897682103, 0.0311728608)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0150114545, 0.023321982, 0.023321982, 0.023321982, 0.023321982], 3)
                _nurbs_edge([(0.9300260934, -0.0229014266), (0.9615034776, -0.0190907271), (1.0153396306, -0.0125732415), (1.0675772017, 0.0018615035), (1.0892720612, 0.0078564178)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0949442994, 0.1623843901, 0.1623843901, 0.1623843901, 0.1623843901], 3)
                _nurbs_edge([(0.8506510648, -0.0362959016), (0.8616223869, -0.0338761188), (0.8878509665, -0.0280912676), (0.9145153356, -0.0248100959), (0.9300260934, -0.0229014266)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0336880427, 0.0805362838, 0.0805362838, 0.0805362838, 0.0805362838], 3)
                _nurbs_edge([(0.7861588391, -0.0655654777), (0.7961375414, -0.0594819729), (0.8164408839, -0.0471040627), (0.8391188717, -0.0399393141), (0.8506510648, -0.0362959016)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0349219882, 0.071054639, 0.071054639, 0.071054639, 0.071054639], 3)
                _nurbs_edge([(0.7400221023, -0.1171592582), (0.7463164701, -0.1070121105), (0.7586701871, -0.0870966886), (0.7771129073, -0.0726509421), (0.7861588391, -0.0655654777)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0355107822, 0.0696956652, 0.0696956652, 0.0696956652, 0.0696956652], 3)
                _nurbs_edge([(0.7226587924, -0.1876045573), (0.7233301423, -0.1750918762), (0.724649683, -0.150498157), (0.734958271, -0.1281414305), (0.7400221023, -0.1171592582)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0372130411, 0.0731423638, 0.0731423638, 0.0731423638, 0.0731423638], 3)
                _nurbs_edge([(0.7692915591, -0.2962491024), (0.75569091, -0.2809246505), (0.7281527321, -0.2498961694), (0.7245049802, -0.2085370792), (0.7226587924, -0.1876045573)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0597897314, 0.1210604174, 0.1210604174, 0.1210604174, 0.1210604174], 3)
                _nurbs_edge([(0.9027407559, -0.338417064), (0.8763251028, -0.3373715921), (0.8277841511, -0.3354504509), (0.7876053377, -0.3085228758), (0.7692915591, -0.2962491024)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0774909652, 0.1423960703, 0.1423960703, 0.1423960703, 0.1423960703], 3)
                _nurbs_edge([(1.0009673032, -0.3210537542), (0.9853041063, -0.3261175122), (0.9533718264, -0.3364409054), (0.9198299218, -0.3377500644), (0.9027407559, -0.338417064)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0491340148, 0.100168639, 0.100168639, 0.100168639, 0.100168639], 3)
                _nurbs_edge([(1.0967135819, -0.2615225423), (1.0809491476, -0.2742983583), (1.0515007143, -0.2981639632), (1.0169993029, -0.3137918434), (1.0009673032, -0.3210537542)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0605749592, 0.1131558291, 0.1131558291, 0.1131558291, 0.1131558291], 3)
                _nurbs_edge([(1.1145728024, -0.3265107978), (1.1103292625, -0.3165879053), (1.1014185491, -0.2957515158), (1.0983308364, -0.2732881844), (1.0967135819, -0.2615225423)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0322252462, 0.0676675459, 0.0676675459, 0.0676675459, 0.0676675459], 3)
            make_face()
            with BuildLine():
                _nurbs_edge([(1.0158501061, -0.2461435903), (1.0283025612, -0.2379640234), (1.0528091358, -0.2218665419), (1.0676068252, -0.1965730529), (1.0748854073, -0.1841318715)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0440326723, 0.0866568048, 0.0866568048, 0.0866568048, 0.0866568048], 3)
                _nurbs_edge([(0.9240727815, -0.2684677947), (0.9405791641, -0.2676554791), (0.9726224102, -0.26607856), (1.0017344848, -0.2526531781), (1.0158501061, -0.2461435903)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0490598215, 0.0952380643, 0.0952380643, 0.0952380643, 0.0952380643], 3)
                _nurbs_edge([(0.8446977529, -0.2446553219), (0.8555482545, -0.2515829882), (0.8796285774, -0.2669574334), (0.9083132906, -0.267932235), (0.9240727815, -0.2684677947)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0379511889, 0.0842243899, 0.0842243899, 0.0842243899, 0.0842243899], 3)
                _nurbs_edge([(0.8179088029, -0.1851240504), (0.8190293908, -0.1965381307), (0.8212727865, -0.2193889024), (0.8368842815, -0.236227628), (0.8446977529, -0.2446553219)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0334201137, 0.0669064323, 0.0669064323, 0.0669064323, 0.0669064323], 3)
                _nurbs_edge([(0.830311099, -0.1429560889), (0.8266938702, -0.1494593246), (0.8193957601, -0.1625802337), (0.8184073289, -0.1775658777), (0.8179088029, -0.1851240504)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0220280217, 0.0444436714, 0.0444436714, 0.0444436714, 0.0444436714], 3)
                _nurbs_edge([(0.8655338677, -0.1136865724), (0.8584072751, -0.1173155627), (0.8444503001, -0.1244227078), (0.834957007, -0.1368663259), (0.830311099, -0.1429560889)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0236525534, 0.0463220103, 0.0463220103, 0.0463220103, 0.0463220103], 3)
                _nurbs_edge([(0.9434204492, -0.0958272327), (0.9276200083, -0.0980907956), (0.9011365678, -0.1018847994), (0.8757673911, -0.1102943095), (0.8655338677, -0.1136865724)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0477552832, 0.0800436024, 0.0800436024, 0.0800436024, 0.0800436024], 3)
                _nurbs_edge([(1.0892720612, -0.0620927919), (1.06913481, -0.0687097363), (1.0215722108, -0.0843384372), (0.9720028992, -0.0916254346), (0.9434204492, -0.0958272327)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0634830462, 0.149941948, 0.149941948, 0.149941948, 0.149941948], 3)
                Line((1.0892720612, -0.0948349941), (1.0892720612, -0.0620927919))
                _nurbs_edge([(1.0748854073, -0.1841318715), (1.0790600635, -0.1717489708), (1.0888004363, -0.142856994), (1.0891005654, -0.1122971189), (1.0892720612, -0.0948349941)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0389782566, 0.0909446746, 0.0909446746, 0.0909446746, 0.0909446746], 3)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.1263325184, perimeter: 3.1436945339
            with BuildLine():
                Line((0.3347133788, -0.1176552881), (0.3347133788, -0.3265107978))
                Line((0.3977172765, -0.0571318973), (0.3347133788, -0.1176552881))
                Line((0.5718462857, -0.3265107978), (0.3977172765, -0.0571318973))
                Line((0.68197898, -0.3265107978), (0.5718462857, -0.3265107978))
                Line((0.4602251443, 0.0048798215), (0.68197898, -0.3265107978))
                Line((0.6616392526, 0.2003407966), (0.4602251443, 0.0048798215))
                Line((0.5460493955, 0.2003407966), (0.6616392526, 0.2003407966))
                Line((0.3347133788, -0.0139716972), (0.5460493955, 0.2003407966))
                Line((0.3347133788, 0.4007626664), (0.3347133788, -0.0139716972))
                Line((0.245416561, 0.4007626664), (0.3347133788, 0.4007626664))
                Line((0.245416561, -0.3265107978), (0.245416561, 0.4007626664))
                Line((0.3347133788, -0.3265107978), (0.245416561, -0.3265107978))
            make_face()
            # Profile area: 0.1131328882, perimeter: 2.8992185855
            with BuildLine():
                _nurbs_edge([(-0.13607963, -0.5194913257), (-0.1470734355, -0.5255661751), (-0.1699037066, -0.5381815028), (-0.1959813725, -0.5395945835), (-0.2095014659, -0.5403272022)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0371781217, 0.0772058956, 0.0772058956, 0.0772058956, 0.0772058956], 3)
                _nurbs_edge([(-0.0815093127, -0.4549991), (-0.0892599677, -0.468393022), (-0.1036153015, -0.4932005023), (-0.1258498431, -0.5112068629), (-0.13607963, -0.5194913257)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0459556288, 0.0851164698, 0.0851164698, 0.0851164698, 0.0851164698], 3)
                _nurbs_edge([(-0.031403741, -0.3354404677), (-0.0405021924, -0.3600657348), (-0.0554962296, -0.4006476045), (-0.0741677555, -0.4396597182), (-0.0815093127, -0.4549991)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0786978922, 0.1296923029, 0.1296923029, 0.1296923029, 0.1296923029], 3)
                Line((0.1690180692, 0.200340737), (-0.031403741, -0.3354404677))
                Line((0.0797212514, 0.200340737), (0.1690180692, 0.200340737))
                Line((-0.032892069, -0.1067412604), (0.0797212514, 0.200340737))
                _nurbs_edge([(-0.0696030465, -0.2267959226), (-0.064244487, -0.2064580597), (-0.0535743186, -0.1659605297), (-0.0397658991, -0.1264230263), (-0.032892069, -0.1067412604)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0630687887, 0.1255849826, 0.1255849826, 0.1255849826, 0.1255849826], 3)
                _nurbs_edge([(-0.1078022328, -0.1047569025), (-0.1008315071, -0.1245279074), (-0.0866491165, -0.1647532907), (-0.0753490606, -0.2058821379), (-0.0696030465, -0.2267959226)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0628701331, 0.1279133368, 0.1279133368, 0.1279133368, 0.1279133368], 3)
                Line((-0.2174389568, 0.200340737), (-0.1078022328, -0.1047569025))
                Line((-0.3136811462, 0.200340737), (-0.2174389568, 0.200340737))
                Line((-0.1137554256, -0.3275029767), (-0.3136811462, 0.200340737))
                _nurbs_edge([(-0.1216928569, -0.3493310917), (-0.1206299499, -0.3462675139), (-0.1180919893, -0.3389524434), (-0.1153494054, -0.3317114285), (-0.1137554256, -0.3275029767)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0097277495, 0.0232274735, 0.0232274735, 0.0232274735, 0.0232274735], 3)
                _nurbs_edge([(-0.1489780751, -0.4158077348), (-0.1451821082, -0.4080850227), (-0.1346002143, -0.3865566682), (-0.1267359988, -0.3638758091), (-0.1216928569, -0.3493310917)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0257972483, 0.071914154, 0.071914154, 0.071914154, 0.071914154], 3)
                _nurbs_edge([(-0.178247532, -0.4435889829), (-0.1725452873, -0.4399228791), (-0.1610303232, -0.4325196448), (-0.1530211047, -0.4214138877), (-0.1489780751, -0.4158077348)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0201426237, 0.0406754887, 0.0406754887, 0.0406754887, 0.0406754887], 3)
                _nurbs_edge([(-0.2258725372, -0.4535107721), (-0.2168100046, -0.4532846784), (-0.2002946374, -0.4528726502), (-0.1851030079, -0.4464757091), (-0.178247532, -0.4435889829)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0269035938, 0.0490285383, 0.0490285383, 0.0490285383, 0.0490285383], 3)
                _nurbs_edge([(-0.2769702283, -0.4455733407), (-0.2678826461, -0.4478835141), (-0.2510931469, -0.452151608), (-0.2338037668, -0.4530833501), (-0.2258725372, -0.4535107721)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0280482282, 0.0518196917, 0.0518196917, 0.0518196917, 0.0518196917], 3)
                Line((-0.2670483199, -0.5294131149), (-0.2769702283, -0.4455733407))
                _nurbs_edge([(-0.2095014659, -0.5403272022), (-0.2186599112, -0.5397623259), (-0.2382887173, -0.5385516569), (-0.2570439428, -0.5325920677), (-0.2670483199, -0.5294131149)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0274212397, 0.0587704768, 0.0587704768, 0.0587704768, 0.0587704768], 3)
            make_face()
            # Profile area: 0.2454016787, perimeter: 5.8413561344
            with BuildLine():
                _nurbs_edge([(-0.7839780358, -0.1141826618), (-0.7770507017, -0.1351218071), (-0.765207567, -0.1709198662), (-0.7539317827, -0.2069003811), (-0.7492514757, -0.221835028)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0661644777, 0.1131163598, 0.1131163598, 0.1131163598, 0.1131163598], 3)
                Line((-0.9561225978, 0.4007626664), (-0.7839780358, -0.1141826618))
                Line((-1.1009819714, 0.4007626664), (-0.9561225978, 0.4007626664))
                Line((-1.1009819714, -0.3265107978), (-1.1009819714, 0.4007626664))
                Line((-1.008212438, -0.3265107978), (-1.1009819714, -0.3265107978))
                Line((-1.008212438, 0.2926142108), (-1.008212438, -0.3265107978))
                Line((-0.7978686598, -0.3265107978), (-1.008212438, 0.2926142108))
                Line((-0.7110522595, -0.3265107978), (-0.7978686598, -0.3265107978))
                Line((-0.4997163621, 0.2821962725), (-0.7110522595, -0.3265107978))
                Line((-0.4997163621, -0.3265107978), (-0.4997163621, 0.2821962725))
                Line((-0.4069467989, -0.3265107978), (-0.4997163621, -0.3265107978))
                Line((-0.4069467989, 0.4007626664), (-0.4069467989, -0.3265107978))
                Line((-0.53642728, 0.4007626664), (-0.4069467989, 0.4007626664))
                Line((-0.7105561701, -0.105252992), (-0.53642728, 0.4007626664))
                _nurbs_edge([(-0.7492514757, -0.221835028), (-0.7440015692, -0.2054914463), (-0.7314787739, -0.1665064989), (-0.7182430866, -0.1277573896), (-0.7105561701, -0.105252992)], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0.0514972535, 0.1228382958, 0.1228382958, 0.1228382958, 0.1228382958], 3)
            make_face()
        # OneSide extrude, distance=-3.556
        extrude(amount=-3.556, mode=Mode.SUBTRACT)
    return part.part


MODELS = {
    "model_21822_7d3db422_0030": {"func": model_21822_7d3db422_0030, "volume": 0.2495682417, "area": 3.4837608005},
    "model_21822_7d3db422_0038": {"func": model_21822_7d3db422_0038, "volume": 0.8182629094, "area": 8.1262747671},
    "model_21822_7d3db422_0044": {"func": model_21822_7d3db422_0044, "volume": 0.4268959024, "area": 4.8649000698},
    "model_21822_7d3db422_0046": {"func": model_21822_7d3db422_0046, "volume": 0.5010057489, "area": 5.4050880666},
    "model_21852_6cf9a734_0010": {"func": model_21852_6cf9a734_0010, "volume": 4.3189674244, "area": 38.8572449202},
    "model_21880_c4d6cbae_0000": {"func": model_21880_c4d6cbae_0000, "volume": 12.9531134467, "area": 42.8503273005},
    "model_21881_f3bee5e5_0002": {"func": model_21881_f3bee5e5_0002, "volume": 14.3775815057, "area": 45.2635220244},
    "model_21893_0500d043_0030": {"func": model_21893_0500d043_0030, "volume": 2.7745084899, "area": 15.9918486984},
    "model_21893_0500d043_0037": {"func": model_21893_0500d043_0037, "volume": 5.7087533631, "area": 23.4095273465},
    "model_21896_ba833d7d_0001": {"func": model_21896_ba833d7d_0001, "volume": 150.3487704192, "area": 249.6623681808},
    "model_21899_d55d6c08_0018": {"func": model_21899_d55d6c08_0018, "volume": 7.7709281275, "area": 51.8460854622},
    "model_21908_385686ec_0007": {"func": model_21908_385686ec_0007, "volume": 2.8588493063, "area": 25.1955730762},
    "model_21940_6c2dac17_0003": {"func": model_21940_6c2dac17_0003, "volume": 15.546695017, "area": 67.0412182892},
    "model_22019_0ef07114_0000": {"func": model_22019_0ef07114_0000, "volume": 18.1783144772, "area": 94.9608618521},
    "model_22025_b77024b9_0005": {"func": model_22025_b77024b9_0005, "volume": 1448.9999981706, "area": 1182.0000005082},
    "model_22025_b77024b9_0009": {"func": model_22025_b77024b9_0009, "volume": 13.5276549079, "area": 45.0711980028},
    "model_22124_6f71410e_0010": {"func": model_22124_6f71410e_0010, "volume": 25.4027764901, "area": 75.3249076471},
    "model_22181_526fb582_0000": {"func": model_22181_526fb582_0000, "volume": 54.2831853072, "area": 157.6991118431},
    "model_22198_327974c6_0004": {"func": model_22198_327974c6_0004, "volume": 1.4482742133, "area": 12.8491139532},
    "model_22202_c9c16395_0005": {"func": model_22202_c9c16395_0005, "volume": 0.1281313963, "area": 3.1551812668},
    "model_22202_c9c16395_0009": {"func": model_22202_c9c16395_0009, "volume": 0.2137263933, "area": 3.1390731013},
    "model_22206_703c82ed_0000": {"func": model_22206_703c82ed_0000, "volume": 28.0418625564, "area": 108.3605992249},
    "model_22253_f4ff5358_0000": {"func": model_22253_f4ff5358_0000, "volume": 68.5000715889, "area": 721.1217388128},
    "model_22254_539990c2_0009": {"func": model_22254_539990c2_0009, "volume": 13016.4897696977, "area": 3884.1699156035},
    "model_22289_4b848f64_0001": {"func": model_22289_4b848f64_0001, "volume": 4.1895952719, "area": 28.1855367912},
    "model_22305_5b45cdb3_0021": {"func": model_22305_5b45cdb3_0021, "volume": 3.8609550874, "area": 80.8097100437},
    "model_22340_ec24cd79_0025": {"func": model_22340_ec24cd79_0025, "volume": 4424.8349087466, "area": 1974.7761758577},
    "model_22344_51f483c9_0008": {"func": model_22344_51f483c9_0008, "volume": 4.398749169, "area": 30.0546738052},
    "model_22369_481ab478_0012": {"func": model_22369_481ab478_0012, "volume": 0.021318369, "area": 0.5767501963},
    "model_22447_4062c6cb_0002": {"func": model_22447_4062c6cb_0002, "volume": 3.9124278597, "area": 32.2812837991},
    "model_22524_0be3da8a_0010": {"func": model_22524_0be3da8a_0010, "volume": 3.9863859821, "area": 28.736332546},
    "model_22645_1ba0af00_0010": {"func": model_22645_1ba0af00_0010, "volume": 1247.173013567, "area": 1666.6149027294},
    "model_22645_1ba0af00_0011": {"func": model_22645_1ba0af00_0011, "volume": 673.6466295729, "area": 642.273804471},
    "model_22666_bdaa1303_0000": {"func": model_22666_bdaa1303_0000, "volume": 1.4282645447, "area": 19.6675771791},
    "model_22711_33843a5d_0004": {"func": model_22711_33843a5d_0004, "volume": 17.0843257776, "area": 52.5211141012},
    "model_22711_33843a5d_0007": {"func": model_22711_33843a5d_0007, "volume": 18.3823925922, "area": 58.5372640328},
    "model_22742_3c107495_0002": {"func": model_22742_3c107495_0002, "volume": 1186.9325039707, "area": 2120.0332445725},
    "model_22760_c2a5214f_0010": {"func": model_22760_c2a5214f_0010, "volume": 77.9950924884, "area": 186.6981450765},
    "model_22764_b884dce6_0000": {"func": model_22764_b884dce6_0000, "volume": 2729.8811877322, "area": 1678.3468654895},
    "model_22772_2b5f6629_0001": {"func": model_22772_2b5f6629_0001, "volume": 48.6179598024, "area": 109.8388196842},
    "model_22848_cc91b848_0020": {"func": model_22848_cc91b848_0020, "volume": 678.928331351, "area": 1039.8405548119},
    "model_22998_00817368_0003": {"func": model_22998_00817368_0003, "volume": 135216.212615287, "area": 17073.1614831426},
    "model_23037_d0df320c_0000": {"func": model_23037_d0df320c_0000, "volume": 14.532588782, "area": 55.3281846903},
    "model_23132_1847c4ef_0001": {"func": model_23132_1847c4ef_0001, "volume": 100.0165291178, "area": 191.6528598322},
    "model_23231_efe613bb_0009": {"func": model_23231_efe613bb_0009, "volume": 4.5443782264, "area": 51.3534924352},
    "model_23315_4192448e_0000": {"func": model_23315_4192448e_0000, "volume": 42.6003454396, "area": 245.0822101139},
    "model_23410_0163b27d_0001": {"func": model_23410_0163b27d_0001, "volume": 0.4581838809, "area": 4.0403624681},
    "model_23493_57512264_0008": {"func": model_23493_57512264_0008, "volume": 0.4667459762, "area": 10.5509991258},
    "model_23554_a0845d54_0002": {"func": model_23554_a0845d54_0002, "volume": 212.7377858225, "area": 565.8866933157},
    "model_23596_d6a0ebb5_0000": {"func": model_23596_d6a0ebb5_0000, "volume": 43.5368745815, "area": 249.9730620948},
    "model_23635_3815ae50_0000": {"func": model_23635_3815ae50_0000, "volume": 43.5542090554, "area": 249.5324126223},
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
