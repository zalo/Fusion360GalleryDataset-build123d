"""Batch 013 - passing/03_4to5ops
117 models bundled from Fusion360 Gallery reconstructions.
"""

from build123d import *
from build123d import Edge, BuildLine
from collections import Counter
from OCP.BRepBuilderAPI import BRepBuilderAPI_MakeEdge
from OCP.Geom import Geom_BSplineCurve
from OCP.TColStd import TColStd_Array1OfReal, TColStd_Array1OfInteger
from OCP.TColgp import TColgp_Array1OfPnt
from OCP.gp import gp_Pnt


def model_51777_87ff5835_0005():
    """Model: Table-006"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 8 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 7.25805, perimeter: 13.335
            with BuildLine():
                Line((-0.9525, 0), (-0.9525, -1.905))
                Line((-0.9525, -1.905), (0.9525, -1.905))
                Line((0.9525, -1.905), (0.9525, 0))
                Line((0.9525, 0), (1.905, 0))
                Line((1.905, 0), (1.905, 0.9525))
                Line((1.905, 0.9525), (-1.905, 0.9525))
                Line((-1.905, 0.9525), (-1.905, 0))
                Line((-1.905, 0), (-0.9525, 0))
            make_face()
        # Symmetric extrude, each_side=34.29
        extrude(amount=34.29, both=True)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -1.905, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 1.2667686977, perimeter: 3.9898226701
            with Locations((0, 25.4)):
                Circle(0.635)
            # Profile area: 1.2667686977, perimeter: 3.9898226701
            with Locations((0, -25.4)):
                Circle(0.635)
        # OneSide extrude, distance=-1.27
        extrude(amount=-1.27, mode=Mode.SUBTRACT)
    return part.part


def model_51863_0b8751d1_0000():
    """Model: bike seat"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))) as sk:
            # Profile area: 5.067074791, perimeter: 7.9796453401
            with Locations((12.4993276843, 16.9757558329)):
                Circle(1.27)
        # TwoSides extrude, along=10.16, against=-5.08
        extrude(amount=10.16)
        extrude(sk.sketch, amount=-5.08)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 10.16, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 304.609725209, perimeter: 105.9160539683
            with BuildLine():
                Line((-42.9793276843, -16.9757558329), (-2.3393276843, -24.5957558329))
                Line((-2.3393276843, -24.5957558329), (-2.3393276843, -9.3557558329))
                Line((-2.3393276843, -9.3557558329), (-42.9793276843, -16.9757558329))
            make_face()
            with BuildLine():
                CenterArc((-12.4993276843, -16.9757558329), 1.27, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 5.067074791, perimeter: 7.9796453401
            with Locations((-12.4993276843, -16.9757558329)):
                Circle(1.27)
        # OneSide extrude, distance=5.08
        extrude(amount=5.08, mode=Mode.ADD)
    return part.part


def model_51863_0b8751d1_0003():
    """Model: Pedal lever arm"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 9 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 5.08), x_dir=(1, 0, 0), z_dir=(0, 0, 1))) as sk:
            # Profile area: 114.9494117526, perimeter: 55.9911966666
            with BuildLine():
                CenterArc((23.3968902736, -18.41624014), 5.5008286483, -133.8380951952, 87.6761854498)
                Line((19.5868903303, -22.3839871392), (19.5868903303, -36.1981033768))
                CenterArc((23.3968898747, -36.19624014), 3.81, -179.9719801548, 179.9719801548)
                Line((27.2068898747, -22.3839874678), (27.2068898747, -36.19624014))
            make_face()
            with BuildLine():
                CenterArc((23.3968898747, -36.19624014), 1.27, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 40.8024793107, perimeter: 44.2818306611
            with BuildLine():
                Line((27.2068898747, -18.417983517), (27.2068898747, -22.3839874678))
                CenterArc((23.3968902736, -18.41624014), 3.81, -0.0262173629, 180.0361048086)
                Line((19.5868903303, -18.4168976259), (19.5868903303, -22.3839871392))
                CenterArc((23.3968902736, -18.41624014), 5.5008286483, -133.8380951952, 87.6761854498)
            make_face()
            with BuildLine():
                CenterArc((23.3968902736, -18.41624014), 2.54, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # TwoSides offset extrude, full=5.715, trim=0.635
        extrude(amount=5.715)
        extrude(sk.sketch, amount=0.635, mode=Mode.SUBTRACT)
    return part.part


def model_51863_0b8751d1_0006():
    """Model: Air pressure seal cap"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.8502295699, perimeter: 5.9847340051
            with Locations((0, -8.8899998665)):
                Circle(0.9525)
        # OneSide extrude, distance=1.905
        extrude(amount=1.905)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 1.2667686977, perimeter: 3.9898226701
            with Locations((0, 8.8899998665)):
                Circle(0.635)
        # OneSide extrude, distance=-1.27
        extrude(amount=-1.27, mode=Mode.SUBTRACT)
    return part.part


def model_51864_39932fe9_0002():
    """Model: Door v3 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 916.5, perimeter: 133
            with BuildLine():
                Line((0, 47), (0, 0))
                Line((0, 0), (19.5, 0))
                Line((19.5, 0), (19.5, 47))
                Line((19.5, 47), (0, 47))
            make_face()
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 47, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.7853981868, perimeter: 3.1415927004
            with Locations((-0.6500000097, 0.7500000112)):
                Circle(0.5000000075)
        # OneSide extrude, distance=-50
        extrude(amount=-50, mode=Mode.SUBTRACT)
    return part.part


def model_51864_39932fe9_0009():
    """Model: Upper Food Part v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 9 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 22.7599868053, perimeter: 227.6000016838
            with BuildLine():
                Line((0, 47.5), (0, 0))
                Line((0, 0), (9.8, 0))
                Line((9.8, 0), (9.8, 47.5))
                Line((9.8, 47.5), (0, 47.5))
            make_face()
            with BuildLine():
                Line((9.6000001431, 47.3000007048), (0.200000003, 47.3000007048))
                Line((9.6000001431, 0.200000003), (9.6000001431, 47.3000007048))
                Line((0.200000003, 0.200000003), (9.6000001431, 0.200000003))
                Line((0.200000003, 47.3000007048), (0.200000003, 0.200000003))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.5), x_dir=(1, 0, 0), z_dir=(0, 0, 1))) as sk:
            # Profile area: 1.880000028, perimeter: 19.2000002801
            with BuildLine():
                Line((0.200000003, 47.0000007004), (0.200000003, 46.8000007004))
                Line((0.200000003, 46.8000007004), (9.6000001431, 46.8000007004))
                Line((9.6000001431, 46.8000007004), (9.6000001431, 47.0000007004))
                Line((9.6000001431, 47.0000007004), (0.200000003, 47.0000007004))
            make_face()
        # TwoSides offset extrude, full=-0.48, trim=-0.01
        extrude(amount=-0.48, mode=Mode.ADD)
        extrude(sk.sketch, amount=-0.01, mode=Mode.SUBTRACT)
    return part.part


def model_51864_39932fe9_0010():
    """Model: Food Part v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 81 constraints, 12 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 9.3199777794, perimeter: 93.6000004292
            with BuildLine():
                Line((32.4, 0.200000003), (32.4, 46.8000006974))
                Line((32.2000004798, 46.8000006974), (32.4, 46.8000006974))
                Line((32.2000004798, 0.200000003), (32.2000004798, 46.8000006974))
                Line((32.2000004798, 0.200000003), (32.4, 0.200000003))
            make_face()
            # Profile area: 15.7999776828, perimeter: 158.399999994
            with BuildLine():
                Line((0.200000003, 46.8000006974), (0.200000003, 0.200000003))
                Line((0.200000003, 46.8000006974), (4.954270042, 46.8000006974))
                Line((4.954270042, 46.8000006974), (5.154270042, 46.8000006974))
                Line((5.154270042, 46.8000006974), (8.4000001252, 46.8000006974))
                Line((8.4000001252, 46.8000006974), (8.6000001252, 46.8000006974))
                Line((8.6000001252, 46.8000006974), (11.7969402424, 46.8000006974))
                Line((11.7969402424, 46.8000006974), (11.9969402424, 46.8000006974))
                Line((11.9969402424, 46.8000006974), (15.341650486, 46.8000006974))
                Line((15.341650486, 46.8000006974), (15.541650486, 46.8000006974))
                Line((15.541650486, 46.8000006974), (19, 46.8000006974))
                Line((19, 46.8000006974), (19.2, 46.8000006974))
                Line((19.2, 46.8000006974), (24, 46.8000006974))
                Line((24, 46.8000006974), (24.2, 46.8000006974))
                Line((24.2, 46.8000006974), (28, 46.8000006974))
                Line((28, 46.8000006974), (28.2, 46.8000006974))
                Line((28.2, 46.8000006974), (32.2000004798, 46.8000006974))
                Line((32.2000004798, 46.8000006974), (32.4, 46.8000006974))
                Line((32.4, 46.8000006974), (32.4, 47))
                Line((0, 47), (32.4, 47))
                Line((0, 47), (0, 0.200000003))
                Line((0, 0.200000003), (0.200000003, 0.200000003))
            make_face()
            # Profile area: 6.4800000966, perimeter: 65.200000006
            with BuildLine():
                Line((24.2, 0), (28, 0))
                Line((28, 0), (28.2, 0))
                Line((28.2, 0), (32.4, 0))
                Line((32.4, 0), (32.4, 0.200000003))
                Line((32.2000004798, 0.200000003), (32.4, 0.200000003))
                Line((28.2, 0.200000003), (32.2000004798, 0.200000003))
                Line((28, 0.200000003), (28.2, 0.200000003))
                Line((24.2, 0.200000003), (28, 0.200000003))
                Line((24, 0.200000003), (24.2, 0.200000003))
                Line((19.2, 0.200000003), (24, 0.200000003))
                Line((19, 0.200000003), (19.2, 0.200000003))
                Line((15.541650486, 0.200000003), (19, 0.200000003))
                Line((15.341650486, 0.200000003), (15.541650486, 0.200000003))
                Line((11.9969402424, 0.200000003), (15.341650486, 0.200000003))
                Line((11.7969402424, 0.200000003), (11.9969402424, 0.200000003))
                Line((8.6000001252, 0.200000003), (11.7969402424, 0.200000003))
                Line((8.4000001252, 0.200000003), (8.6000001252, 0.200000003))
                Line((5.154270042, 0.200000003), (8.4000001252, 0.200000003))
                Line((4.954270042, 0.200000003), (5.154270042, 0.200000003))
                Line((0.200000003, 0.200000003), (4.954270042, 0.200000003))
                Line((0, 0.200000003), (0.200000003, 0.200000003))
                Line((0, 0.200000003), (0, 0))
                Line((0, 0), (11.7969402424, 0))
                Line((11.7969402424, 0), (11.9969402424, 0))
                Line((11.9969402424, 0), (15.341650486, 0))
                Line((15.341650486, 0), (15.541650486, 0))
                Line((15.541650486, 0), (19, 0))
                Line((19, 0), (19.2, 0))
                Line((19.2, 0), (24, 0))
                Line((24, 0), (24.2, 0))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XY construction plane
        # Sketch has 6 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY) as sk:
            # Profile area: 9.3200001389, perimeter: 93.6000013888
            with BuildLine():
                Line((0.8835282113, 46.8000006974), (1.0835282113, 46.8000006974))
                Line((0.8835282113, 0.200000003), (0.8835282113, 46.8000006974))
                Line((1.0835282113, 0.200000003), (0.8835282113, 0.200000003))
                Line((1.0835282113, 46.8000006974), (1.0835282113, 0.200000003))
            make_face()
        # TwoSides offset extrude, full=0.48, trim=0.01
        extrude(amount=0.48, mode=Mode.ADD)
        extrude(sk.sketch, amount=0.01, mode=Mode.SUBTRACT)
    return part.part


def model_51864_39932fe9_0027():
    """Model: Knob Pin v2 (4)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            Circle(0.5)
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1), x_dir=(1, 0, 0), z_dir=(0, 0, 1))) as sk:
            # Profile area: 0.7539822369, perimeter: 7.5398223686
            with BuildLine():
                CenterArc((0, 0), 0.7, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # TwoSides offset extrude, full=-0.6, trim=-0.5
        extrude(amount=-0.6, mode=Mode.ADD)
        extrude(sk.sketch, amount=-0.5, mode=Mode.SUBTRACT)
    return part.part


def model_51871_86ebf5b2_0006():
    """Model: Gas Manifold Pipe v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.3587387169, perimeter: 14.5330993319
            with BuildLine():
                CenterArc((0, 0), 1.25, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.0630145971, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 3.5499998044, perimeter: 6.6791176979
            Circle(1.0630145971)
        # OneSide extrude, distance=55
        extrude(amount=55)

        # Sketch1 -> Extrude2 (Cut)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 3.5499998044, perimeter: 6.6791176979
            Circle(1.0630145971)
        # OneSide extrude, distance=55
        extrude(amount=55, mode=Mode.SUBTRACT)

        # Sketch2 -> Extrude3 (Cut)
        # Sketch on YZ construction plane
        # Sketch has 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            with Locations((-10, 0)):
                Circle(0.3)
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            with Locations((-27.5, 0)):
                Circle(0.3)
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            with Locations((-45, 0)):
                Circle(0.3)
        # OneSide extrude, distance=6
        extrude(amount=6, mode=Mode.SUBTRACT)
    return part.part


def model_51876_8346832d_0000():
    """Model: Tray v1"""
    with BuildPart() as part:
        # Sketch8 -> Extrude2 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 15 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2466.2810924751, perimeter: 195.1978720407
            with BuildLine():
                CenterArc((25.4, -11.43), 7.62, -90, 90)
                Line((33.02, 11.43), (33.02, -11.43))
                CenterArc((25.4, 11.43), 7.62, 0, 90)
                Line((-25.4, 19.05), (25.4, 19.05))
                CenterArc((-25.4, 11.43), 7.62, 90, 90)
                Line((-33.02, -11.43), (-33.02, 11.43))
                CenterArc((-25.4, -11.43), 7.62, 180, 90)
                Line((25.4, -19.05), (-25.4, -19.05))
            make_face()
        # OneSide extrude, distance=-10.16
        extrude(amount=-10.16)

        # Sketch9 -> Extrude3 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1913.5048795265, perimeter: 183.3140558602
            with BuildLine():
                Line((-29.7470421525, 16.0814718125), (29.7470421525, 16.0814718125))
                Line((-29.7470421525, -16.0814718125), (-29.7470421525, 16.0814718125))
                Line((29.7470421525, -16.0814718125), (-29.7470421525, -16.0814718125))
                Line((29.7470421525, 16.0814718125), (29.7470421525, -16.0814718125))
            make_face()
        # OneSide extrude, distance=-7.62
        extrude(amount=-7.62, mode=Mode.SUBTRACT)
    return part.part


def model_51876_8346832d_0001():
    """Model: Portable Handle v1"""
    with BuildPart() as part:
        # Sketch3 -> Extrude3 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 120.9049667358, perimeter: 62.6471719192
            with BuildLine():
                Line((-2.6854822353, -0.4759269051), (-2.6854822353, -24.9240730949))
                Line((-2.6854822353, -24.9240730949), (2.5399999619, -24.9240730949))
                Line((2.5399999619, -24.9240730949), (2.7272514999, -0.0205063814))
                CenterArc((0, 0), 2.7273285932, -169.950265399, 169.5194628244)
            make_face()
            # Profile area: 23.3415799876, perimeter: 17.1314126603
            with BuildLine():
                CenterArc((0, 0), 2.7273285932, -169.950265399, 169.5194628244)
                CenterArc((0, 0), 2.7273285932, -0.4308025746, 170.3810679736)
                Line((-2.6854822353, 0.4759269051), (-2.6854822353, -0.4759269051))
            make_face()
        # OneSide extrude, distance=53.34
        extrude(amount=53.34)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -0.0205063814, -2.7272514999), x_dir=(-1, 0, 0), z_dir=(0, -0.0075188525, -0.999971733))):
            # Profile area: 956.8304881828, perimeter: 130.2963205251
            with BuildLine():
                Line((-5.4761097326, -24.9042706818), (-5.4761097326, -2.5399999619))
                Line((-5.4761097326, -2.5399999619), (-48.2599992752, -2.5399999619))
                Line((-48.2599992752, -2.5399999619), (-48.2599992752, -24.9042706818))
                Line((-48.2599992752, -24.9042706818), (-5.4761097326, -24.9042706818))
            make_face()
        # OneSide extrude, distance=-17.78
        extrude(amount=-17.78, mode=Mode.SUBTRACT)
    return part.part


def model_51876_8346832d_0009():
    """Model: Bolts v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2026829916, perimeter: 1.595929068
            Circle(0.254)
        # OneSide extrude, distance=0.254
        extrude(amount=0.254)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.5067075114, perimeter: 2.5233855
            Circle(0.4016092757)
        # OneSide extrude, distance=-0.127
        extrude(amount=-0.127, mode=Mode.ADD)
    return part.part


def model_51891_9455ea02_0003():
    """Model: BallCaster v1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 19 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 11.4009182797, perimeter: 11.9694680102
            with BuildLine():
                CenterArc((0, 0), 1.905, 120, 120)
                CenterArc((0, 0), 1.905, -120, 60)
                CenterArc((0, 0), 1.905, -60, 120)
                CenterArc((0, 0), 1.905, 60, 60)
            make_face()
            # Profile area: 2.0145428892, perimeter: 11.283183098
            with BuildLine():
                CenterArc((0, 0), 1.905, -60, 120)
                Line((2.8575, -0.5499261314), (0.9525, -1.6497783942))
                CenterArc((2.54, 0), 0.635, -60, 120)
                Line((2.8575, 0.5499261314), (0.9525, 1.6497783942))
            make_face()
            with BuildLine():
                CenterArc((2.54, 0), 0.24892, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 2.0145428892, perimeter: 11.283183098
            with BuildLine():
                CenterArc((-2.54, 0), 0.635, 120, 120)
                Line((-2.8575, -0.5499261314), (-0.9525, -1.6497783942))
                CenterArc((0, 0), 1.905, 120, 120)
                Line((-2.8575, 0.5499261314), (-0.9525, 1.6497783942))
            make_face()
            with BuildLine():
                CenterArc((-2.54, 0), 0.24892, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.1946567452, perimeter: 1.5640104867
            with Locations((2.54, 0)):
                Circle(0.24892)
            # Profile area: 0.1946567452, perimeter: 1.5640104867
            with Locations((-2.54, 0)):
                Circle(0.24892)
        # OneSide extrude, distance=0.127
        extrude(amount=0.127)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 19 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 11.4009182797, perimeter: 11.9694680102
            with BuildLine():
                CenterArc((0, 0), 1.905, 120, 120)
                CenterArc((0, 0), 1.905, -120, 60)
                CenterArc((0, 0), 1.905, -60, 120)
                CenterArc((0, 0), 1.905, 60, 60)
            make_face()
        # OneSide extrude, distance=-1.27
        extrude(amount=-1.27, mode=Mode.ADD)

        # Sketch1 -> Extrude3 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 19 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1946567452, perimeter: 1.5640104867
            with Locations((2.54, 0)):
                Circle(0.24892)
            # Profile area: 0.1946567452, perimeter: 1.5640104867
            with Locations((-2.54, 0)):
                Circle(0.24892)
        # OneSide extrude, distance=0.508
        extrude(amount=0.508, mode=Mode.SUBTRACT)
    return part.part


def model_51913_1fa125b4_0012():
    """Model: pivot v2 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.5393804003, perimeter: 4.398229715
            Circle(0.7)
        # OneSide extrude, distance=1.2
        extrude(amount=1.2)

        # Sketch1 -> Extrude2 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.5393804003, perimeter: 4.398229715
            Circle(0.7)
        # OneSide extrude, distance=1.2
        extrude(amount=1.2)

        # Sketch1 -> Extrude3 (Join)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.471238898, perimeter: 9.4247779608
            with BuildLine():
                CenterArc((0, 0), 0.8, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.7, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 1.5393804003, perimeter: 4.398229715
            Circle(0.7)
        # OneSide extrude, distance=-0.15
        extrude(amount=-0.15, mode=Mode.ADD)
    return part.part


def model_51914_fb924efa_0005():
    """Model: zatyczka do rury pion"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 31.5385621722, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.7600000525, perimeter: 5.4000000805
            with BuildLine():
                Line((-0.8000000119, -4.70000007), (0.8000000119, -4.70000007))
                Line((-0.8000000119, -5.8000000864), (-0.8000000119, -4.70000007))
                Line((0.8000000119, -5.8000000864), (-0.8000000119, -5.8000000864))
                Line((0.8000000119, -4.70000007), (0.8000000119, -5.8000000864))
            make_face()
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 31.5385621722, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.2399999475, perimeter: 12.4000000805
            with BuildLine():
                Line((-1, -4.5), (1, -4.5))
                Line((-1, -6), (-1, -4.5))
                Line((1, -6), (-1, -6))
                Line((1, -4.5), (1, -6))
            make_face()
            with BuildLine():
                Line((-0.8000000119, -5.8000000864), (0.8000000119, -5.8000000864))
                Line((-0.8000000119, -4.70000007), (-0.8000000119, -5.8000000864))
                Line((0.8000000119, -4.70000007), (-0.8000000119, -4.70000007))
                Line((0.8000000119, -5.8000000864), (0.8000000119, -4.70000007))
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 1.7600000525, perimeter: 5.4000000805
            with BuildLine():
                Line((0.8000000119, -5.8000000864), (0.8000000119, -4.70000007))
                Line((0.8000000119, -4.70000007), (-0.8000000119, -4.70000007))
                Line((-0.8000000119, -4.70000007), (-0.8000000119, -5.8000000864))
                Line((-0.8000000119, -5.8000000864), (0.8000000119, -5.8000000864))
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)
    return part.part


def model_51916_fa226b15_0000():
    """Model: Camera Connector Knob"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.8502295699, perimeter: 5.9847340051
            with Locations((1.2700000405, -3.0480000973)):
                Circle(0.9525)
        # OneSide extrude, distance=0.635
        extrude(amount=0.635)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.635, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.3166921744, perimeter: 1.994911335
            with Locations((-1.2700000405, 3.0480000973)):
                Circle(0.3175)
        # OneSide extrude, distance=1.524
        extrude(amount=1.524, mode=Mode.ADD)
    return part.part


def model_51916_fa226b15_0005():
    """Model: Handle Bottom"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 5.067074791, perimeter: 7.9796453401
            with Locations((3.8100001216, -3.8100001216)):
                Circle(1.27)
        # OneSide extrude, distance=0.635
        extrude(amount=0.635)

        # Sketch1 -> Extrude2 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.8018513299, perimeter: 20.2682994695
            with BuildLine():
                CenterArc((3.8100001216, -3.8100001216), 1.7018, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((3.8100001216, -3.8100001216), 1.5240000486, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.254
        extrude(amount=0.254)

        # Sketch1 -> Extrude3 (Join)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.8018513299, perimeter: 20.2682994695
            with BuildLine():
                CenterArc((3.8100001216, -3.8100001216), 1.7018, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((3.8100001216, -3.8100001216), 1.5240000486, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 2.2295133738, perimeter: 17.5552200539
            with BuildLine():
                CenterArc((3.8100001216, -3.8100001216), 1.5240000486, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((3.8100001216, -3.8100001216), 1.27, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 5.067074791, perimeter: 7.9796453401
            with Locations((3.8100001216, -3.8100001216)):
                Circle(1.27)
        # OneSide extrude, distance=-0.3175
        extrude(amount=-0.3175, mode=Mode.ADD)
    return part.part


def model_51916_fa226b15_0008():
    """Model: Support Set Screw"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1829214, perimeter: 1.5161326146
            with Locations((1.2700000405, -1.7780000567)):
                Circle(0.2413)
        # OneSide extrude, distance=2.286
        extrude(amount=2.286)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2.286, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0708183873, perimeter: 0.9906
            with BuildLine():
                Line((-1.2705481878, 1.6129009667), (-1.127294108, 1.6949758023))
                Line((-1.127294108, 1.6949758023), (-1.1267459608, 1.8600748923))
                Line((-1.1267459608, 1.8600748923), (-1.2694518933, 1.9430991468))
                Line((-1.2694518933, 1.9430991468), (-1.412705973, 1.8610243112))
                Line((-1.412705973, 1.8610243112), (-1.4132541203, 1.6959252212))
                Line((-1.4132541203, 1.6959252212), (-1.2705481878, 1.6129009667))
            make_face()
        # OneSide extrude, distance=-0.254
        extrude(amount=-0.254, mode=Mode.SUBTRACT)
    return part.part


def model_51916_fa226b15_0010():
    """Model: Weight Arm Knob"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.8502295699, perimeter: 5.9847340051
            with Locations((2.5400000811, -2.5400000811)):
                Circle(0.9525)
        # OneSide extrude, distance=0.635
        extrude(amount=0.635)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.635, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1829214, perimeter: 1.5161326146
            with Locations((-2.5400000811, 2.5400000811)):
                Circle(0.2413)
        # OneSide extrude, distance=0.9525
        extrude(amount=0.9525, mode=Mode.ADD)
    return part.part


def model_51916_fa226b15_0011():
    """Model: Weight Cap"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 11.4009182797, perimeter: 11.9694680102
            with Locations((6.8580002189, -2.0320000648)):
                Circle(1.905)
        # OneSide extrude, distance=-1.905
        extrude(amount=-1.905)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1829214, perimeter: 1.5161326146
            with Locations((-6.8580002189, 2.0320000648)):
                Circle(0.2413)
        # OneSide extrude, distance=2.794
        extrude(amount=2.794, mode=Mode.ADD)
    return part.part


def model_51925_a4bed832_0002():
    """Model: Knife"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 15 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 14.168070905, perimeter: 31.7071508527
            with BuildLine():
                CenterArc((-20.0660006485, -31.4960010133), 0.254, -180, 90)
                Line((-20.0660006485, -31.7500010133), (-19.8120006242, -31.7500010133))
                CenterArc((-19.8120006242, -31.4960010133), 0.254, -90, 90)
                Line((-19.5580006242, -31.4960010133), (-19.5580006242, -24.3930417674))
                CenterArc((-17.5260006242, -24.3930417674), 2.032, 165.71956023, 14.28043977)
                CenterArc((-33.5280022323, -20.3200000674), 14.4802295332, -14.28043977, 28.7556348114)
                CenterArc((-19.7533708946, -16.763999752), 0.254, 14.4751950414, 75.5248049586)
                Line((-20.0660006485, -16.509999752), (-19.7533708946, -16.509999752))
                CenterArc((-20.0660006485, -16.763999752), 0.254, 90, 90)
                Line((-20.3200006485, -31.4960010133), (-20.3200006485, -16.763999752))
            make_face()
        # OneSide extrude, distance=0.127
        extrude(amount=0.127)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 31.7500010133), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0657750044, perimeter: 2.4848386048
            with BuildLine():
                Line((-18.9875982938, 0.1824816077), (-18.9962629741, -0.0664310282))
                Line((-19.5580006242, 0.127), (-18.9875982938, 0.1824816077))
                Line((-19.0245997701, 0.0761999991), (-19.5580006242, 0.127))
                Line((-19.0245997701, 0.0507999994), (-19.0245997701, 0.0761999991))
                Line((-19.5580006242, 0), (-19.0245997701, 0.0507999994))
                Line((-18.9962629741, -0.0664310282), (-19.5580006242, 0))
            make_face()
        # OneSide extrude, distance=-18.796
        extrude(amount=-18.796, mode=Mode.SUBTRACT)
    return part.part


def model_51940_aa0fca73_0003():
    """Model: main v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 5.7255526112, perimeter: 8.4823001647
            Circle(1.35)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 10.1787601976, perimeter: 22.6194671058
            with BuildLine():
                CenterArc((0, 0), 2.25, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.35, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=14
        extrude(amount=14, mode=Mode.ADD)
    return part.part


def model_52006_d21e4570_0004():
    """Model: Pan"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.3178438774, perimeter: 2.324859268
            with BuildLine():
                Line((1.8, -0.5), (1.0908712311, -0.5))
                Line((1.8, 0), (1.8, -0.5))
                Line((1.2000000179, 0), (1.8, 0))
                CenterArc((0, 0), 1.2000000179, -24.6243179608, 24.6243179608)
            make_face()
            # Profile area: 1.2566371181, perimeter: 7.0831853812
            with BuildLine():
                CenterArc((0, 0), 1.2000000179, -24.6243179608, 24.6243179608)
                Line((0.8, 0), (1.2000000179, 0))
                CenterArc((0, 0), 0.8, 180, 180)
                Line((-0.8, 0), (-1.2000000179, 0))
                CenterArc((0, 0), 1.2000000179, 180, 24.6243179608)
                CenterArc((0, 0), 1.2000000179, -155.3756820392, 130.7513640783)
            make_face()
            # Profile area: 0.3178438774, perimeter: 2.324859268
            with BuildLine():
                CenterArc((0, 0), 1.2000000179, 180, 24.6243179608)
                Line((-1.2000000179, 0), (-1.8, 0))
                Line((-1.8, 0), (-1.8, -0.5))
                Line((-1.8, -0.5), (-1.0908712311, -0.5))
            make_face()
        # OneSide extrude, distance=1.6
        extrude(amount=1.6)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 11 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((1.4505, 0.3549)):
                Circle(0.2)
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with BuildLine():
                CenterArc((1.4505, 1.2451), 0.2, 0, 90)
                CenterArc((1.4505, 1.2451), 0.2, 90, 270)
            make_face()
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((-1.4505, 1.2451)):
                Circle(0.2)
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((-1.4505, 0.3549)):
                Circle(0.2)
        # OneSide extrude, distance=-0.6
        extrude(amount=-0.6, mode=Mode.SUBTRACT)
    return part.part


def model_52024_97da327b_0001():
    """Model: Long Pin Female Top"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.8107319666, perimeter: 3.191858136
            Circle(0.508)
        # OneSide extrude, distance=0.254
        extrude(amount=0.254)

        # Sketch3 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.254, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2375191308, perimeter: 2.9923670025
            with BuildLine():
                CenterArc((0, 0), 0.3175, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.15875, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=7.62
        extrude(amount=7.62, mode=Mode.ADD)
    return part.part


def model_52024_97da327b_0002():
    """Model: Small Pin Male Top"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.8107320183, perimeter: 3.1918582379
            with Locations((2.7940000892, -1.2700000405)):
                Circle(0.5080000162)
        # OneSide extrude, distance=0.254
        extrude(amount=0.254)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.254, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0791730436, perimeter: 0.9974556675
            with Locations((-2.7940000892, 1.2700000405)):
                Circle(0.15875)
        # OneSide extrude, distance=3.81
        extrude(amount=3.81, mode=Mode.ADD)
    return part.part


def model_52024_97da327b_0005():
    """Model: Small Pin Female Top"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.8107319666, perimeter: 3.191858136
            with Locations((1.2700000405, -1.2700000405)):
                Circle(0.508)
        # OneSide extrude, distance=0.254
        extrude(amount=0.254)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.254, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2375191308, perimeter: 2.9923670025
            with BuildLine():
                CenterArc((-1.2700000405, 1.2700000405), 0.3175, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-1.2700000405, 1.2700000405), 0.15875, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=3.81
        extrude(amount=3.81, mode=Mode.ADD)
    return part.part


def model_52024_97da327b_0008():
    """Model: Long Pin Male Top"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.8107319666, perimeter: 3.191858136
            with Locations((2.0320000648, 0)):
                Circle(0.508)
        # OneSide extrude, distance=0.254
        extrude(amount=0.254)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.254, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0791730436, perimeter: 0.9974556675
            with Locations((-2.0320000648, 0)):
                Circle(0.15875)
        # OneSide extrude, distance=7.62
        extrude(amount=7.62, mode=Mode.ADD)
    return part.part


def model_52024_97da327b_0013():
    """Model: Small Clamp Top 1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 6 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.9500765233, perimeter: 5.9847340051
            with BuildLine():
                CenterArc((-3.4925000811, 2.921), 0.635, 173.8674138382, 192.2651723235)
                CenterArc((-3.4925000811, 2.921), 0.635, 6.1325861618, 167.7348276765)
            make_face()
            with BuildLine():
                CenterArc((-3.4925000811, 2.921), 0.3175, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 4.014544392, perimeter: 10.047922879
            with BuildLine():
                Line((-4.4450000811, 0), (-4.1238661965, 2.9888367768))
                Line((-2.5400000811, 0), (-4.4450000811, 0))
                Line((-2.5400000811, 0), (-2.8611339656, 2.9888367768))
                CenterArc((-3.4925000811, 2.921), 0.635, 173.8674138382, 192.2651723235)
            make_face()
        # OneSide extrude, distance=3.175
        extrude(amount=3.175)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on YZ construction plane
        # Sketch has 13 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 4.8125600374, perimeter: 8.8694173523
            with BuildLine():
                Line((-0.3240837659, 1.911449989), (-0.3240837659, 3.8061586651))
                Line((-0.3240837659, 3.8061586651), (-2.8640837659, 3.8061586651))
                Line((-2.8640837659, 3.8061586651), (-2.8640837659, 1.911449989))
                Line((-2.8640837659, 1.911449989), (-0.3240837659, 1.911449989))
            make_face()
            # Profile area: 3.2258, perimeter: 7.62
            with BuildLine():
                Line((-2.8640837659, 1.593949989), (-2.8640837659, 0.323949989))
                Line((-2.8640837659, 0.323949989), (-0.3240837659, 0.323949989))
                Line((-0.3240837659, 0.323949989), (-0.3240837659, 1.593949989))
                Line((-0.3240837659, 1.593949989), (-2.8640837659, 1.593949989))
            make_face()
        # OneSide extrude, distance=-12.7
        extrude(amount=-12.7, mode=Mode.SUBTRACT)
    return part.part


def model_52230_60438ea5_0013():
    """Model: mounting rear support adjustment"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 6 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 81, perimeter: 36
            with BuildLine():
                Line((39.75, 45.75), (30.75, 45.75))
                Line((39.75, 54.75), (39.75, 45.75))
                Line((30.75, 54.75), (39.75, 54.75))
                Line((30.75, 45.75), (30.75, 54.75))
            make_face()
        # OneSide extrude, distance=20
        extrude(amount=20)
    return part.part


def model_52352_adac16c3_0003():
    """Model: ShaftTop"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 15 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1000, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 21450.3170805592, perimeter: 2161.1976333475
            with BuildLine():
                Line((-169.9, 170), (170, 170))
                Line((170, 170), (170, -170))
                Line((170, -170), (-169.9, -170))
                Line((-169.9, -170), (-169.9, -191.1405899976))
                Line((-169.9, -191.1405899976), (188.5176366786, -191.1405899976))
                Line((188.5176366786, 191.1405899976), (188.5176366786, -191.1405899976))
                Line((188.5176366786, 191.1405899976), (-169.9, 191.1405899976))
                Line((-169.9, 191.1405899976), (-169.9, 170))
            make_face()
        # OneSide extrude, distance=-40
        extrude(amount=-40)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1000, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 21450.3170805592, perimeter: 2161.1976333475
            with BuildLine():
                Line((169.9, -170), (-170, -170))
                Line((-170, -170), (-170, 170))
                Line((-170, 170), (169.9, 170))
                Line((169.9, 191.1405899976), (169.9, 170))
                Line((-188.5176366786, 191.1405899976), (169.9, 191.1405899976))
                Line((-188.5176366786, -191.1405899976), (-188.5176366786, 191.1405899976))
                Line((169.9, -191.1405899976), (-188.5176366786, -191.1405899976))
                Line((169.9, -170), (169.9, -191.1405899976))
            make_face()
            # Profile area: 115566, perimeter: 1359.8
            with BuildLine():
                Line((169.9, 170), (169.9, -170))
                Line((-170, 170), (169.9, 170))
                Line((-170, -170), (-170, 170))
                Line((169.9, -170), (-170, -170))
            make_face()
        # OneSide extrude, distance=10
        extrude(amount=10, mode=Mode.ADD)
    return part.part


def model_52443_085efc00_0007():
    """Model: handle part 1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 5 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 141.8326611224, perimeter: 64.0933478222
            with BuildLine():
                CenterArc((4.5, 10.5), 5.8, -7.3133693199, 194.6267386398)
                Line((-1.2528156457, 9.7616828958), (0, 0))
                Line((0, 0), (9, 0))
                Line((9, 0), (10.2528156457, 9.7616828958))
            make_face()
            with BuildLine():
                CenterArc((4.5, 10.5), 2.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=2
        extrude(amount=2, both=True)

        # Sketch4 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 2), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1.1309733553, perimeter: 3.7699111843
            with Locations((8.1, 2.2)):
                Circle(0.6)
            # Profile area: 1.1309733553, perimeter: 3.7699111843
            with Locations((0.9, 2.1038406425)):
                Circle(0.6)
        # OneSide extrude, distance=-7
        extrude(amount=-7, mode=Mode.SUBTRACT)
    return part.part


def model_52454_a591c6d0_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 45.9, perimeter: 27.8
            with BuildLine():
                Line((8.5, -5.4), (0, -5.4))
                Line((8.5, 0), (8.5, -5.4))
                Line((0, 0), (8.5, 0))
                Line((0, -5.4), (0, 0))
            make_face()
        # OneSide extrude, distance=0.06
        extrude(amount=0.06)

        # Sketch2 -> Extrude2 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 9 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0425677493, perimeter: 1.6558062674
            with BuildLine():
                Line((0.02, -0.01), (-0.2479031337, -0.01))
                Line((-0.2479031337, -0.01), (-0.2479031337, -0.05))
                Line((-0.2479031337, -0.05), (0.1520968663, -0.05))
                Line((0.1520968663, -0.05), (0.1520968663, 0.11))
                Line((0.1520968663, 0.11), (-0.2479031337, 0.11))
                Line((-0.2479031337, 0.11), (-0.2479031337, 0.07))
                Line((-0.2479031337, 0.07), (0.02, 0.07))
                Line((0.02, 0.07), (0.02, -0.01))
            make_face()
        # OneSide extrude, distance=9.1
        extrude(amount=9.1)
    return part.part


def model_52557_e6a00b06_0010():
    """Model: latch"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 4 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 16.7817776668, perimeter: 24.2311287018
            with BuildLine():
                CenterArc((60.720557274, 1.3), 0.3, 90, 72.6459753637)
                Line((60.4342132806, 1.3894824979), (60, 0))
                Line((60, 0), (71, 0))
                Line((70.5657867194, 1.3894824979), (71, 0))
                CenterArc((70.279442726, 1.3), 0.3, 17.3540246363, 72.6459753637)
                Line((60.720557274, 1.6), (70.279442726, 1.6))
            make_face()
        # OneSide extrude, distance=3
        extrude(amount=3)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.6, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.4506192983, perimeter: 6.8265482457
            with BuildLine():
                CenterArc((-1.5, -63.0951891653), 0.8, 180, 180)
                Line((-0.7, -63.0951891653), (-0.7, -62.1951891653))
                CenterArc((-1.5, -62.1951891653), 0.8, 0, 180)
                Line((-2.3, -63.0951891653), (-2.3, -62.1951891653))
            make_face()
        # OneSide extrude, distance=-0.7
        extrude(amount=-0.7, mode=Mode.SUBTRACT)
    return part.part


def model_52651_47c9fcdd_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 46, perimeter: 31
            with BuildLine():
                Line((4.5, -0.5), (-7, -0.5))
                Line((4.5, 3.5), (4.5, -0.5))
                Line((-7, 3.5), (4.5, 3.5))
                Line((-7, -0.5), (-7, 3.5))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


def model_52659_7eb6fd4c_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch4 -> Extrude3 (NewBody)
        # Sketch on XZ construction plane
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 7.0685834706, perimeter: 9.4247779608
            with Locations((10, -5)):
                Circle(1.5)
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch5 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.552544031, perimeter: 20.4203522483
            with BuildLine():
                CenterArc((-10, 5), 1.75, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-10, 5), 1.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 7.0685834706, perimeter: 9.4247779608
            with Locations((-10, 5)):
                Circle(1.5)
        # OneSide extrude, distance=9
        extrude(amount=9, mode=Mode.ADD)
    return part.part


def model_52884_c8150d6e_0000():
    """Model: needle v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1200000036, perimeter: 1.4465382201
            with BuildLine():
                Line((0, 0.5000000075), (0.200000003, 0.8500000127))
                Line((0, 1.1000000164), (0.200000003, 0.8500000127))
                Line((-0.200000003, 0.8500000127), (0, 1.1000000164))
                Line((-0.200000003, 0.8500000127), (0, 0.5000000075))
            make_face()
            # Profile area: 0.1199999985, perimeter: 1.4465381761
            with BuildLine():
                Line((0, -1.0999999911), (-0.200000003, -0.8499999873))
                Line((0.200000003, -0.8499999873), (0, -1.0999999911))
                Line((0, -0.5000000075), (0.200000003, -0.8499999873))
                Line((-0.200000003, -0.8499999873), (0, -0.5000000075))
            make_face()
            # Profile area: 0.540000011, perimeter: 5.0124515297
            with BuildLine():
                Line((-0.200000003, 0.8500000127), (0, 0.5000000075))
                Line((-0.200000003, -0.8499999873), (-0.200000003, 0.8500000127))
                Line((-0.200000003, -0.8499999873), (0, -0.5000000075))
                Line((0, -0.5000000075), (0.200000003, -0.8499999873))
                Line((0.200000003, 0.8500000127), (0.200000003, -0.8499999873))
                Line((0, 0.5000000075), (0.200000003, 0.8500000127))
            make_face()
        # OneSide extrude, distance=0.05
        extrude(amount=0.05)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.05, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.3900000066, perimeter: 2.7403124392
            with BuildLine():
                Line((0.200000003, 0.8499999873), (0, 1.0999999911))
                Line((0, 1.0999999911), (-0.200000003, 0.8499999873))
                Line((-0.200000003, 0.8499999873), (-0.200000003, -0.0000000127))
                Line((-0.200000003, -0.0000000127), (0.200000003, -0.0000000127))
                Line((0.200000003, -0.0000000127), (0.200000003, 0.8499999873))
            make_face()
        # OneSide extrude, distance=0.002
        extrude(amount=0.002, mode=Mode.ADD)
    return part.part


def model_52884_c8150d6e_0007():
    """Model: side attach 2 v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 15 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 4.2930463288, perimeter: 9.1369555922
            with BuildLine():
                CenterArc((3.3181, 0.9079), 0.3, 0, 90)
                Line((3.3181, 1.2079), (0.3, 1.2079))
                CenterArc((0.3, 0.9079), 0.3, 90, 90)
                Line((0, 0.9079), (0, 0.3))
                CenterArc((0.3, 0.3), 0.3, 180, 90)
                Line((0.3, 0), (3.3181, 0))
                CenterArc((3.3181, 0.3), 0.3, -90, 90)
                Line((3.6181, 0.3), (3.6181, 0.9079))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            with Locations((2.6702069471, 0.6015925409)):
                Circle(0.4)
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            with Locations((0.9464500941, 0.6379767903)):
                Circle(0.4)
        # OneSide extrude, distance=0.4
        extrude(amount=0.4, mode=Mode.ADD)
    return part.part


def model_52884_c8150d6e_0035():
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
        # Sketch has 20 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.786558189, perimeter: 6.5371489029
            with BuildLine():
                Line((-3, -4.4000000656), (-2.3000000343, -4.4000000656))
                _nurbs_edge([(-2.3000000343, -4.4000000656), (-2.2984738752, -4.3847423196), (-2.2953457221, -4.3543049784), (-2.2904259883, -4.3088834201), (-2.2834094718, -4.248792151), (-2.2738471324, -4.1744255982), (-2.263421188, -4.1006745298), (-2.2520022758, -4.0272581911), (-2.2393873602, -3.9536889218), (-2.2252845455, -3.8792170348), (-2.2093504925, -3.8030518093), (-2.1912266899, -3.7245725824), (-2.1705785896, -3.6435545425), (-2.1471337988, -3.5603790074), (-2.120730258, -3.4763082907), (-2.0912964942, -3.3932357348), (-2.0588254601, -3.3133765973), (-2.0233550059, -3.238974036), (-1.9849497725, -3.1720245936), (-1.9436864665, -3.1139221587), (-1.8996410285, -3.0653510451), (-1.86223039, -3.0343236118), (-1.8329690733, -3.0154562183), (-1.8129288896, -3.0048272067), (-1.8027756377, -3)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1, 1, 1, 1, 1, 1], 5)
                CenterArc((0, 0), 3.5, -148.9972808661, 27.9945617323)
                Line((-3, -1.8027756377), (-3, -4.4000000656))
            make_face()
            # Profile area: 33.6039408874, perimeter: 21.2625669502
            with BuildLine():
                CenterArc((0, 0), 3.5, -148.9972808661, 27.9945617323)
                Line((-1.8027756377, -3), (1.8027756377, -3))
                CenterArc((0, 0), 3.5, -58.9972808661, 27.9945617323)
                Line((3, -1.8027756377), (3, 1.8027756377))
                CenterArc((0, 0), 3.5, 31.0027191339, 27.9945617323)
                Line((1.8027756377, 3), (-1.8027756377, 3))
                CenterArc((0, 0), 3.5, 121.0027191339, 27.9945617323)
                Line((-3, 1.8027756377), (-3, -1.8027756377))
            make_face()
            # Profile area: 1.786558189, perimeter: 6.5371489029
            with BuildLine():
                CenterArc((0, 0), 3.5, 121.0027191339, 27.9945617323)
                _nurbs_edge([(-2.3000000343, 4.4000000656), (-2.2984738752, 4.3847423196), (-2.2953457221, 4.3543049784), (-2.2904259883, 4.3088834201), (-2.2834094718, 4.248792151), (-2.2738471324, 4.1744255982), (-2.263421188, 4.1006745298), (-2.2520022758, 4.0272581911), (-2.2393873602, 3.9536889218), (-2.2252845455, 3.8792170348), (-2.2093504925, 3.8030518093), (-2.1912266899, 3.7245725824), (-2.1705785896, 3.6435545425), (-2.1471337988, 3.5603790074), (-2.120730258, 3.4763082907), (-2.0912964942, 3.3932357348), (-2.0588254601, 3.3133765973), (-2.0233550059, 3.238974036), (-1.9849497725, 3.1720245936), (-1.9436864665, 3.1139221587), (-1.8996410285, 3.0653510451), (-1.86223039, 3.0343236118), (-1.8329690733, 3.0154562183), (-1.8129288896, 3.0048272067), (-1.8027756377, 3)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1, 1, 1, 1, 1, 1], 5)
                Line((-3, 4.4000000656), (-2.3000000343, 4.4000000656))
                Line((-3, 1.8027756377), (-3, 4.4000000656))
            make_face()
            # Profile area: 1.786558189, perimeter: 6.5371489029
            with BuildLine():
                CenterArc((0, 0), 3.5, 31.0027191339, 27.9945617323)
                Line((3, 1.8027756377), (3, 4.4000000656))
                Line((3, 4.4000000656), (2.3000000343, 4.4000000656))
                _nurbs_edge([(2.3000000343, 4.4000000656), (2.2984738752, 4.3847423196), (2.2953457221, 4.3543049784), (2.2904259883, 4.3088834201), (2.2834094718, 4.248792151), (2.2738471324, 4.1744255982), (2.263421188, 4.1006745298), (2.2520022758, 4.0272581911), (2.2393873602, 3.9536889218), (2.2252845455, 3.8792170348), (2.2093504925, 3.8030518093), (2.1912266899, 3.7245725824), (2.1705785896, 3.6435545425), (2.1471337988, 3.5603790074), (2.120730258, 3.4763082907), (2.0912964942, 3.3932357348), (2.0588254601, 3.3133765973), (2.0233550059, 3.238974036), (1.9849497725, 3.1720245936), (1.9436864665, 3.1139221587), (1.8996410285, 3.0653510451), (1.86223039, 3.0343236118), (1.8329690733, 3.0154562183), (1.8129288896, 3.0048272067), (1.8027756377, 3)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1, 1, 1, 1, 1, 1], 5)
            make_face()
            # Profile area: 1.786558189, perimeter: 6.5371489029
            with BuildLine():
                CenterArc((0, 0), 3.5, -58.9972808661, 27.9945617323)
                _nurbs_edge([(2.3000000343, -4.4000000656), (2.2984738752, -4.3847423196), (2.2953457221, -4.3543049784), (2.2904259883, -4.3088834201), (2.2834094718, -4.248792151), (2.2738471324, -4.1744255982), (2.263421188, -4.1006745298), (2.2520022758, -4.0272581911), (2.2393873602, -3.9536889218), (2.2252845455, -3.8792170348), (2.2093504925, -3.8030518093), (2.1912266899, -3.7245725824), (2.1705785896, -3.6435545425), (2.1471337988, -3.5603790074), (2.120730258, -3.4763082907), (2.0912964942, -3.3932357348), (2.0588254601, -3.3133765973), (2.0233550059, -3.238974036), (1.9849497725, -3.1720245936), (1.9436864665, -3.1139221587), (1.8996410285, -3.0653510451), (1.86223039, -3.0343236118), (1.8329690733, -3.0154562183), (1.8129288896, -3.0048272067), (1.8027756377, -3)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1, 1, 1, 1, 1, 1], 5)
                Line((3, -4.4000000656), (2.3000000343, -4.4000000656))
                Line((3, -1.8027756377), (3, -4.4000000656))
            make_face()
        # Symmetric extrude, each_side=0.6
        extrude(amount=0.6, both=True)
    return part.part


def model_52886_5743bcf0_0004():
    """Model: switch"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 2.4881610166, perimeter: 6.6130525358
            with BuildLine():
                CenterArc((12.5, 12), 0.9025, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((12.5, 12), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=0.6
        extrude(amount=0.6, both=True)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 0, 0.6), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.5988402263, perimeter: 3.4289886316
            with BuildLine():
                CenterArc((12.5, 12), 0.9025, 30.9945888867, 118.0108222266)
                CenterArc((12.5, 15), 2.650662831, -106.969681786, 33.9393635719)
            make_face()
        # OneSide extrude, distance=-2
        extrude(amount=-2, mode=Mode.SUBTRACT)
    return part.part


def model_52886_5743bcf0_0008():
    """Model: strut"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 26 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.4382084481, perimeter: 14.8759616332
            with BuildLine():
                Line((-24.2000003606, 15.4427187014), (-24.2000003606, 15.2236064752))
                CenterArc((-24.2100003606, 15.4427187014), 0.01, 0, 115.3769801943)
                CenterArc((-24, 15), 0.5, 115.3769801943, 232.1672527246)
                CenterArc((-23.502003967, 14.890000222), 0.01, 90, 77.544232919)
                Line((-20.497996033, 14.900000222), (-23.502003967, 14.900000222))
                CenterArc((-20.497996033, 14.890000222), 0.01, 12.4557670811, 77.5442329189)
                CenterArc((-20, 15), 0.5, -167.5442329189, 232.1673375776)
                CenterArc((-19.790000295, 15.4427190124), 0.01, 64.6231046587, 115.3768953413)
                Line((-19.800000295, 15.2236070616), (-19.800000295, 15.4427190124))
                CenterArc((-20, 15), 0.3, 131.8103920233, 276.3793686811)
                Line((-20.200000301, 15.4427187296), (-20.200000301, 15.2236065285))
                CenterArc((-20.210000301, 15.4427187296), 0.01, 0, 115.3769724803)
                CenterArc((-20, 15), 0.5, 115.3769724804, 52.1672737253)
                CenterArc((-20.4979960585, 15.1099996625), 0.01, -90, 77.5442462057)
                Line((-23.5020039415, 15.0999996625), (-20.4979960585, 15.0999996625))
                CenterArc((-23.5020039415, 15.1099996625), 0.01, -167.5442462057, 77.5442462057)
                CenterArc((-24, 15), 0.5, 12.4557537943, 52.1673585783)
                CenterArc((-23.7900003546, 15.4427190406), 0.01, 64.6231123726, 115.3768876273)
                Line((-23.8000003546, 15.223607115), (-23.8000003546, 15.4427190406))
                CenterArc((-24, 15), 0.3, 131.8104072961, 276.379368681)
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 14.900000222, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 1.223805799, perimeter: 4.861280787
            with BuildLine():
                CenterArc((1.0000000149, 22.9807420875), 0.1, 21.8014094864, 136.3971810273)
                Line((0.9071523458, 23.0178811551), (0.5000000149, 22.0000003278))
                Line((0.5000000149, 22.0000003278), (0.9071523458, 20.9821195005))
                CenterArc((1.0000000149, 21.0192585682), 0.1, -158.1985905136, 136.3971810273)
                Line((1.092847684, 20.9821195005), (1.5000000149, 22.0000003278))
                Line((1.092847684, 23.0178811551), (1.5000000149, 22.0000003278))
            make_face()
        # OneSide extrude, distance=-0.04
        extrude(amount=-0.04, mode=Mode.SUBTRACT)
    return part.part


def model_52985_475fe7b2_0014():
    """Model: Grep (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 20, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 525, perimeter: 100
            with BuildLine():
                Line((17.5, -7.5), (17.5, 7.5))
                Line((17.5, 7.5), (-17.5, 7.5))
                Line((-17.5, 7.5), (-17.5, -7.5))
                Line((-17.5, -7.5), (17.5, -7.5))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 7.5), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.5, perimeter: 3
            with BuildLine():
                Line((-16, 19.5), (-16, 19))
                Line((-17, 19.5), (-16, 19.5))
                Line((-17, 19), (-17, 19.5))
                Line((-16, 19), (-17, 19))
            make_face()
        # OneSide extrude, distance=-17
        extrude(amount=-17, mode=Mode.SUBTRACT)
    return part.part


def model_52987_387431ac_0006():
    """Model: Spherical insert"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 11.3411494795, perimeter: 11.9380520836
            Circle(1.9)
        # OneSide extrude, distance=0.8
        extrude(amount=0.8)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.8, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            Circle(0.5)
        # OneSide extrude, distance=-0.8
        extrude(amount=-0.8, mode=Mode.SUBTRACT)
    return part.part


def model_52987_387431ac_0010():
    """Model: First step screw cap"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 22.0618344098, perimeter: 16.650441064
            Circle(2.65)
        # OneSide extrude, distance=3.9
        extrude(amount=3.9)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 3.9, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 9.0792027689, perimeter: 10.6814150222
            Circle(1.7)
        # OneSide extrude, distance=-3.9
        extrude(amount=-3.9, mode=Mode.SUBTRACT)
    return part.part


def model_53060_44095911_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 10 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 15912, perimeter: 564
            with BuildLine():
                Line((84, -204), (6, -204))
                Line((84, 0), (84, -204))
                Line((6, 0), (84, 0))
                Line((6, -204), (6, 0))
            make_face()
        # Symmetric extrude, each_side=4
        extrude(amount=4, both=True)
    return part.part


def model_53072_60d8a39b_0003():
    """Model: Component10"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((5.500000082, -5.0000000745)):
                Circle(0.2)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            with Locations((-5.500000082, -5.0000000745)):
                Circle(0.1)
        # OneSide extrude, distance=1.6
        extrude(amount=1.6, mode=Mode.ADD)
    return part.part


def model_53075_6438cc56_0007():
    """Model: handle legs"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 14 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 2.56, perimeter: 25.6
            with BuildLine():
                Line((-66.7, 4.7), (-66.7, 1.3))
                Line((-66.7, 1.3), (-63.3, 1.3))
                Line((-63.3, 1.3), (-63.3, 4.7))
                Line((-63.3, 4.7), (-66.7, 4.7))
            make_face()
            with BuildLine():
                Line((-66.5, 1.5), (-66.5, 4.5))
                Line((-66.5, 4.5), (-63.5, 4.5))
                Line((-63.5, 4.5), (-63.5, 1.5))
                Line((-63.5, 1.5), (-66.5, 1.5))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-27
        extrude(amount=-27)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 66.7), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((-23, 3)):
                Circle(0.5)
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((-20, 3)):
                Circle(0.5)
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((-17, 3)):
                Circle(0.5)
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((-14, 3)):
                Circle(0.5)
            # Profile area: 4.9087385212, perimeter: 7.853981634
            with Locations((-3.5, 3)):
                Circle(1.25)
        # OneSide extrude, distance=-4
        extrude(amount=-4, mode=Mode.SUBTRACT)
    return part.part


def model_53119_aabd4fc1_0006():
    """Model: Roof"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 16 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 177.1757123846, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 59399.7320478409, perimeter: 1372.5077676759
            with BuildLine():
                Line((-213.8941957974, -188.8528553118), (-552.5, -188.8528553118))
                Line((-213.8941957974, -7.5), (-213.8941957974, -188.8528553118))
                Line((-552.5, -7.5), (-213.8941957974, -7.5))
                Line((-552.5, -188.8528553118), (-552.5, -7.5))
            make_face()
            with BuildLine():
                Line((-215.9999999998, -172.5186488852), (-215.9999999998, -175.6225030183))
                Line((-215.9999999998, -175.6225030183), (-215.9999999998, -185.6225030183))
                Line((-215.9999999998, -185.6225030183), (-225.9999999998, -185.6225030183))
                Line((-225.9999999998, -185.6225030183), (-369.1913701903, -185.6225030183))
                Line((-369.1913701903, -185.6225030183), (-369.1913701903, -172.5186488852))
                Line((-369.1913701903, -172.5186488852), (-215.9999999998, -172.5186488852))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-10
        extrude(amount=-10)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 177.1757123846, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 59399.7320478409, perimeter: 1372.5077676759
            with BuildLine():
                Line((-552.5, -7.5), (-552.5, -188.8528553118))
                Line((-552.5, -188.8528553118), (-213.8941957974, -188.8528553118))
                Line((-213.8941957974, -188.8528553118), (-213.8941957974, -7.5))
                Line((-213.8941957974, -7.5), (-552.5, -7.5))
            make_face()
            with BuildLine():
                Line((-369.1913701903, -185.6225030183), (-369.1913701903, -172.5186488852))
                Line((-369.1913701903, -172.5186488852), (-215.9999999998, -172.5186488852))
                Line((-215.9999999998, -172.5186488852), (-215.9999999998, -185.6225030183))
                Line((-215.9999999998, -185.6225030183), (-369.1913701903, -185.6225030183))
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 2007.3973694281, perimeter: 332.5904486473
            with BuildLine():
                Line((-215.9999999998, -185.6225030183), (-369.1913701903, -185.6225030183))
                Line((-215.9999999998, -172.5186488852), (-215.9999999998, -185.6225030183))
                Line((-369.1913701903, -172.5186488852), (-215.9999999998, -172.5186488852))
                Line((-369.1913701903, -185.6225030183), (-369.1913701903, -172.5186488852))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)
    return part.part


def model_53119_aabd4fc1_0014():
    """Model: Plug"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 16 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(205.5000000001, 0, 0.2028256074), x_dir=(0, 0, -1), z_dir=(-1, 0, 0))):
            # Profile area: 75.3483521888, perimeter: 129.2088421801
            with BuildLine():
                Line((84.7470036792, -40.6485752308), (112, -40.6485752308))
                Line((84.7470036792, -48), (84.7470036792, -40.6485752308))
                Line((112, -48), (84.7470036792, -48))
                Line((112, -40.6485752308), (112, -48))
            make_face()
            with BuildLine():
                Line((85.8735018396, -46.8242876154), (85.8735018396, -41.8242876154))
                Line((85.8735018396, -41.8242876154), (110.8735018396, -41.8242876154))
                Line((110.8735018396, -41.8242876154), (110.8735018396, -46.8242876154))
                Line((110.8735018396, -46.8242876154), (85.8735018396, -46.8242876154))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-2.5
        extrude(amount=-2.5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(205.5000000001, 0, 0), x_dir=(0, 0, -1), z_dir=(-1, 0, 0))):
            # Profile area: 75.3483521888, perimeter: 129.2088421801
            with BuildLine():
                Line((111.7971743926, -48), (111.7971743926, -40.6485752308))
                Line((111.7971743926, -40.6485752308), (84.5441780718, -40.6485752308))
                Line((84.5441780718, -40.6485752308), (84.5441780718, -48))
                Line((84.5441780718, -48), (111.7971743926, -48))
            make_face()
            with BuildLine():
                Line((110.6706762322, -41.8242876154), (110.6706762322, -46.8242876154))
                Line((110.6706762322, -46.8242876154), (85.6706762322, -46.8242876154))
                Line((85.6706762322, -46.8242876154), (85.6706762322, -41.8242876154))
                Line((85.6706762322, -41.8242876154), (110.6706762322, -41.8242876154))
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 125, perimeter: 60
            with BuildLine():
                Line((85.6706762322, -41.8242876154), (110.6706762322, -41.8242876154))
                Line((85.6706762322, -46.8242876154), (85.6706762322, -41.8242876154))
                Line((110.6706762322, -46.8242876154), (85.6706762322, -46.8242876154))
                Line((110.6706762322, -41.8242876154), (110.6706762322, -46.8242876154))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)
    return part.part


def model_53119_aabd4fc1_0021():
    """Model: Frame"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 44 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(-8, 52.1621437073, -188), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 183.2035850386, perimeter: 75.0593884388
            with BuildLine():
                Line((248.5, -46.8242874146), (267.5, -46.8242874146))
                Line((248.5, -57.5), (248.5, -46.8242874146))
                Line((267.5, -57.5), (248.5, -57.5))
                Line((267.5, -46.8242874146), (267.5, -57.5))
            make_face()
            with BuildLine():
                CenterArc((258, -52.1621437073), 2.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 51.9577749503, perimeter: 31.0852531537
            with BuildLine():
                Line((216, -57.5), (216, -46.8242874146))
                Line((216, -46.8242874146), (211.1330860086, -46.8242874146))
                Line((211.1330860086, -57.5), (211.1330860086, -46.8242874146))
                Line((211.1330860086, -57.5), (216, -57.5))
            make_face()
            # Profile area: 1668.2527392839, perimeter: 333.8837692053
            with BuildLine():
                Line((211.1330860086, -57.5), (211.1330860086, -46.8242874146))
                Line((211.1330860086, -46.8242874146), (54.8669139914, -46.8242874146))
                Line((54.8669139914, -46.8242874146), (54.8669139914, -57.5))
                Line((54.8669139914, -57.5), (211.1330860086, -57.5))
            make_face()
            # Profile area: 51.9577749503, perimeter: 31.0852531537
            with BuildLine():
                Line((54.8669139914, -46.8242874146), (54.8669139914, -57.5))
                Line((54.8669139914, -46.8242874146), (50, -46.8242874146))
                Line((50, -46.8242874146), (50, -57.5))
                Line((50, -57.5), (54.8669139914, -57.5))
            make_face()
            # Profile area: 102.9855403323, perimeter: 41.2827063616
            with BuildLine():
                Line((50, -46.8242874146), (50, -57.5))
                Line((40.058653905, -46.8242874146), (50, -46.8242874146))
                CenterArc((8, -52.1621437073), 32.5, -9.4531879863, 18.9063759725)
                Line((50, -57.5), (40.058653905, -57.5))
            make_face()
            # Profile area: 346.9606590271, perimeter: 86.3514251709
            with BuildLine():
                Line((216, -46.8242874146), (248.5, -46.8242874146))
                Line((216, -57.5), (216, -46.8242874146))
                Line((248.5, -57.5), (216, -57.5))
                Line((248.5, -57.5), (248.5, -46.8242874146))
            make_face()
            # Profile area: 183.2035850386, perimeter: 75.0593884388
            with BuildLine():
                Line((17.5, -57.5), (17.5, -46.8242874146))
                Line((17.5, -46.8242874146), (-1.5, -46.8242874146))
                Line((-1.5, -46.8242874146), (-1.5, -57.5))
                Line((-1.5, -57.5), (17.5, -57.5))
            make_face()
            with BuildLine():
                CenterArc((8, -52.1621437073), 2.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 243.9751186948, perimeter: 66.5173219815
            with BuildLine():
                CenterArc((8, -52.1621437073), 32.5, -9.4531879863, 18.9063759725)
                Line((17.5, -46.8242874146), (40.058653905, -46.8242874146))
                Line((17.5, -57.5), (17.5, -46.8242874146))
                Line((40.058653905, -57.5), (17.5, -57.5))
            make_face()
        # OneSide extrude, distance=5
        extrude(amount=5)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 44 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(-8, 52.1621437073, -188), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 51.9577749503, perimeter: 31.0852531537
            with BuildLine():
                Line((216, -57.5), (216, -46.8242874146))
                Line((216, -46.8242874146), (211.1330860086, -46.8242874146))
                Line((211.1330860086, -57.5), (211.1330860086, -46.8242874146))
                Line((211.1330860086, -57.5), (216, -57.5))
            make_face()
            # Profile area: 51.9577749503, perimeter: 31.0852531537
            with BuildLine():
                Line((54.8669139914, -46.8242874146), (54.8669139914, -57.5))
                Line((54.8669139914, -46.8242874146), (50, -46.8242874146))
                Line((50, -46.8242874146), (50, -57.5))
                Line((50, -57.5), (54.8669139914, -57.5))
            make_face()
        # OneSide extrude, distance=175
        extrude(amount=175, mode=Mode.ADD)

        # Sketch2 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 9 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -13), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 2270.0097123868, perimeter: 446.6175971885
            with BuildLine():
                Line((259.5, -5.3378562927), (46.8669139912, -5.3378562927))
                Line((259.5, 5.3378562927), (259.5, -5.3378562927))
                Line((46.8669139912, 5.3378562927), (259.5, 5.3378562927))
                Line((46.8669139912, -5.3378562927), (46.8669139912, 5.3378562927))
            make_face()
            # Profile area: 530.1642440637, perimeter: 140.0593884385
            with BuildLine():
                Line((41.9999999998, 5.3378562927), (41.9999999998, -5.3378562927))
                Line((-9.5, 5.3378562927), (41.9999999998, 5.3378562927))
                Line((-9.5, -5.3378562927), (-9.5, 5.3378562927))
                Line((41.9999999998, -5.3378562927), (-9.5, -5.3378562927))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 2.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 51.9577749503, perimeter: 31.0852531537
            with BuildLine():
                Line((46.8669139912, -5.3378562927), (46.8669139912, 5.3378562927))
                Line((41.9999999998, 5.3378562927), (46.8669139912, 5.3378562927))
                Line((41.9999999998, 5.3378562927), (41.9999999998, -5.3378562927))
                Line((46.8669139912, -5.3378562927), (41.9999999998, -5.3378562927))
            make_face()
        # OneSide extrude, distance=5
        extrude(amount=5, mode=Mode.ADD)
    return part.part


def model_53206_824f0184_0001():
    """Model: Wood Screw"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 16 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.1286189951, perimeter: 1.7047174903
            with BuildLine():
                CenterArc((0, 0), 0.35, 101.5369590328, 156.9260819344)
                Line((-0.07, -0.1326649916), (-0.07, -0.342928564))
                CenterArc((0, 0), 0.15, 117.8181392847, 124.3637214307)
                Line((-0.07, 0.1326649916), (-0.07, 0.342928564))
            make_face()
            # Profile area: 0.0151322102, perimeter: 0.5909134446
            with BuildLine():
                Line((0.07, 0), (0.07, 0.1326649916))
                Line((0.07, 0), (0.07, -0.1326649916))
                CenterArc((0, 0), 0.15, -62.1818607153, 124.3637214307)
            make_face()
            # Profile area: 0.1286189951, perimeter: 1.7047174903
            with BuildLine():
                Line((0.07, 0.1326649916), (0.07, 0.342928564))
                CenterArc((0, 0), 0.15, -62.1818607153, 124.3637214307)
                Line((0.07, -0.1326649916), (0.07, -0.342928564))
                CenterArc((0, 0), 0.35, -78.4630409672, 156.9260819344)
            make_face()
            # Profile area: 0.0151322102, perimeter: 0.5909134446
            with BuildLine():
                CenterArc((0, 0), 0.15, 117.8181392847, 124.3637214307)
                Line((-0.07, 0.1326649916), (-0.07, -0.1326649916))
            make_face()
        # OneSide extrude, distance=0.12
        extrude(amount=0.12)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on YZ construction plane
        # Sketch has 16 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0284606376, perimeter: 0.707133126
            with BuildLine():
                Line((-0.07, 0.1326649916), (-0.07, 0.342928564))
                CenterArc((0, 0), 0.15, 62.1818607153, 55.6362785693)
                Line((0.07, 0.1326649916), (0.07, 0.342928564))
                CenterArc((0, 0), 0.35, 78.4630409672, 23.0739180656)
            make_face()
            # Profile area: 0.1286189951, perimeter: 1.7047174903
            with BuildLine():
                CenterArc((0, 0), 0.35, 101.5369590328, 156.9260819344)
                Line((-0.07, -0.1326649916), (-0.07, -0.342928564))
                CenterArc((0, 0), 0.15, 117.8181392847, 124.3637214307)
                Line((-0.07, 0.1326649916), (-0.07, 0.342928564))
            make_face()
            # Profile area: 0.0142303188, perimeter: 0.553566563
            with BuildLine():
                Line((0.07, -0.1326649916), (0.07, -0.342928564))
                CenterArc((0, 0), 0.15, -90, 27.8181392847)
                Line((0, -0.35), (0, -0.15))
                CenterArc((0, 0), 0.35, -90, 11.5369590328)
            make_face()
            # Profile area: 0.0142303188, perimeter: 0.553566563
            with BuildLine():
                CenterArc((0, 0), 0.35, -101.5369590328, 11.5369590328)
                Line((0, -0.35), (0, -0.15))
                CenterArc((0, 0), 0.15, -117.8181392847, 27.8181392847)
                Line((-0.07, -0.1326649916), (-0.07, -0.342928564))
            make_face()
            # Profile area: 0.1286189951, perimeter: 1.7047174903
            with BuildLine():
                Line((0.07, 0.1326649916), (0.07, 0.342928564))
                CenterArc((0, 0), 0.15, -62.1818607153, 124.3637214307)
                Line((0.07, -0.1326649916), (0.07, -0.342928564))
                CenterArc((0, 0), 0.35, -78.4630409672, 156.9260819344)
            make_face()
            # Profile area: 0.0303160607, perimeter: 0.8364781299
            with BuildLine():
                Line((-0.07, 0.1326649916), (-0.07, -0.1326649916))
                CenterArc((0, 0), 0.15, -117.8181392847, 27.8181392847)
                Line((0, -0.15), (0, 0))
                Line((0, 0), (0.07, 0))
                Line((0.07, 0), (0.07, 0.1326649916))
                CenterArc((0, 0), 0.15, 62.1818607153, 55.6362785693)
            make_face()
            # Profile area: 0.0151322102, perimeter: 0.5909134446
            with BuildLine():
                CenterArc((0, 0), 0.15, 117.8181392847, 124.3637214307)
                Line((-0.07, 0.1326649916), (-0.07, -0.1326649916))
            make_face()
            # Profile area: 0.0101053536, perimeter: 0.42549271
            with BuildLine():
                Line((0.07, 0), (0.07, -0.1326649916))
                Line((0, 0), (0.07, 0))
                Line((0, -0.15), (0, 0))
                CenterArc((0, 0), 0.15, -90, 27.8181392847)
            make_face()
            # Profile area: 0.0151322102, perimeter: 0.5909134446
            with BuildLine():
                Line((0.07, 0), (0.07, 0.1326649916))
                Line((0.07, 0), (0.07, -0.1326649916))
                CenterArc((0, 0), 0.15, -62.1818607153, 124.3637214307)
            make_face()
        # OneSide extrude, distance=-0.23
        extrude(amount=-0.23, mode=Mode.ADD)

        # Sketch1 -> Extrude3 (Join)
        # Sketch on YZ construction plane
        # Sketch has 16 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0101053536, perimeter: 0.42549271
            with BuildLine():
                Line((0.07, 0), (0.07, -0.1326649916))
                Line((0, 0), (0.07, 0))
                Line((0, -0.15), (0, 0))
                CenterArc((0, 0), 0.15, -90, 27.8181392847)
            make_face()
            # Profile area: 0.0303160607, perimeter: 0.8364781299
            with BuildLine():
                Line((-0.07, 0.1326649916), (-0.07, -0.1326649916))
                CenterArc((0, 0), 0.15, -117.8181392847, 27.8181392847)
                Line((0, -0.15), (0, 0))
                Line((0, 0), (0.07, 0))
                Line((0.07, 0), (0.07, 0.1326649916))
                CenterArc((0, 0), 0.15, 62.1818607153, 55.6362785693)
            make_face()
            # Profile area: 0.0151322102, perimeter: 0.5909134446
            with BuildLine():
                CenterArc((0, 0), 0.15, 117.8181392847, 124.3637214307)
                Line((-0.07, 0.1326649916), (-0.07, -0.1326649916))
            make_face()
            # Profile area: 0.0151322102, perimeter: 0.5909134446
            with BuildLine():
                Line((0.07, 0), (0.07, 0.1326649916))
                Line((0.07, 0), (0.07, -0.1326649916))
                CenterArc((0, 0), 0.15, -62.1818607153, 124.3637214307)
            make_face()
        # OneSide extrude, distance=-3
        extrude(amount=-3, mode=Mode.ADD)
    return part.part


def model_53213_13a055ca_0000():
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
        # Sketch on XY construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 3.4071871724, perimeter: 8.9340575731
            with BuildLine():
                Line((1.2699999809, 4.9163389533), (1.2699999809, 3.2332376184))
                CenterArc((1.2064999809, 4.9163389533), 0.0635, 0, 136.4489619986)
                _nurbs_edge([(-1.1604776631, 4.960090482), (-1.1315821275, 4.9296952121), (-1.0518865925, 4.8481254975), (-0.9213910584, 4.7248176627), (-0.740095525, 4.57725601), (-0.5079999924, 4.4330153267), (-0.2539999962, 4.3348487425), (0, 4.3012401708), (0.2539999962, 4.3348487426), (0.5079999924, 4.4330153267), (0.740095525, 4.57725601), (0.9213910584, 4.7248176627), (1.0518865925, 4.8481254975), (1.1315821275, 4.9296952121), (1.1604776631, 4.960090482)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0.0431190234, 0.0431190234, 0.0431190234, 0.0431190234, 0.0431190234, 0.0431190234, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.9568809766, 0.9568809766, 0.9568809766, 0.9568809766, 0.9568809766, 0.9568809766], 5)
                CenterArc((-1.2064999809, 4.9163389533), 0.0635, 43.5510380007, 136.4489619993)
                Line((-1.2699999809, 3.2332376184), (-1.2699999809, 4.9163389533))
                Line((1.2699999809, 3.2332376184), (-1.2699999809, 3.2332376184))
            make_face()
        # OneSide extrude, distance=9.652
        extrude(amount=9.652)
    return part.part


def model_53216_2857e8ac_0000():
    """Model: pin clamp"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((-43, 0)):
                Circle(0.5)
        # OneSide extrude, distance=1.3
        extrude(amount=1.3)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on XY construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            with Locations((0.6499999855, 0)):
                Circle(0.3)
        # OneSide extrude, distance=44.5
        extrude(amount=44.5, mode=Mode.SUBTRACT)
    return part.part


def model_53216_2857e8ac_0005():
    """Model: holder"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.5079644737, perimeter: 15.0796447372
            with BuildLine():
                CenterArc((-37.5, 0), 1.3, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-37.5, 0), 1.1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=30
        extrude(amount=30)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.0820586372, perimeter: 1.232548498
            with BuildLine():
                Line((37.7000005618, -1.5000000224), (37.3000005558, -1.5000000224))
                Line((37.7000005618, -1.5000000224), (37.7000005618, -1.2845231704))
                CenterArc((37.5, 0), 1.3, -98.8498583065, 17.6997664627)
                Line((37.3000005558, -1.5000000224), (37.3000005558, -1.2845233444))
            make_face()
            # Profile area: 0.057941367, perimeter: 1.0706414486
            with BuildLine():
                CenterArc((37.5, 0), 1.3, -98.8498583065, 17.6997664627)
                Line((37.7000005618, -1.2845231704), (37.7000005618, -1.1500000171))
                Line((37.3000005558, -1.1500000171), (37.7000005618, -1.1500000171))
                Line((37.3000005558, -1.2845233444), (37.3000005558, -1.1500000171))
            make_face()
        # OneSide extrude, distance=-29.6
        extrude(amount=-29.6, mode=Mode.SUBTRACT)
    return part.part


def model_53216_2857e8ac_0009():
    """Model: clamp lower"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 25 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 3.2962705243, perimeter: 23.998496306
            with BuildLine():
                CenterArc((-54.4000008062, 2.3000000104), 0.3, 0, 90)
                Line((-54.6500008166, 2.6000000104), (-54.4000008062, 2.6000000104))
                CenterArc((-54.6500008166, 2.4500000104), 0.15, 90, 90)
                Line((-54.8000008166, 2.4500000104), (-54.8000008166, 1.7146429866))
                CenterArc((-54.6500008166, 1.7146429866), 0.15, -180, 78.4630682538)
                CenterArc((-55, 0), 1.6, 101.5369865186, 336.9260817352)
                CenterArc((-55.3500008225, 1.714642652), 0.15, -78.4630134814, 78.4630134814)
                Line((-55.2000008225, 2.4500000104), (-55.2000008225, 1.714642652))
                CenterArc((-55.3500008225, 2.4500000104), 0.15, 0, 90)
                Line((-55.3500008225, 2.6000000104), (-55.600000833, 2.6000000104))
                CenterArc((-55.600000833, 2.3000000104), 0.3, 90, 90)
                Line((-55.900000833, 2.3000000104), (-55.900000833, 1.9209365774))
                CenterArc((-56.600000833, 1.9209365774), 0.7, -50.2081556553, 50.2081556553)
                CenterArc((-55, 0), 1.8, 129.7918443447, 280.4163602009)
                CenterArc((-53.4000008062, 1.9209379427), 0.7, -180, 50.2082045455)
                Line((-54.1000008062, 2.3000000104), (-54.1000008062, 1.9209379427))
            make_face()
        # OneSide extrude, distance=2.5
        extrude(amount=2.5)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 54.1000008062), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.1612904007, perimeter: 1.8710769749
            with BuildLine():
                Line((-2.2128398421, 1.9209379427), (-1.3871600775, 1.9209379427))
                CenterArc((-1.7999999598, 2.1000000313), 0.45, -156.552053401, 133.104106802)
            make_face()
            # Profile area: 0.3306805994, perimeter: 2.41472359
            with BuildLine():
                CenterArc((-1.7999999598, 2.1000000313), 0.45, -23.447946599, 49.8357435951)
                Line((-1.396887062, 2.3000000104), (-2.2031128575, 2.3000000104))
                CenterArc((-1.7999999598, 2.1000000313), 0.45, 153.6122030039, 49.8357435951)
                Line((-2.2128398421, 1.9209379427), (-1.3871600775, 1.9209379427))
            make_face()
            # Profile area: 0.1442015122, perimeter: 1.8054439437
            with BuildLine():
                Line((-1.396887062, 2.3000000104), (-2.2031128575, 2.3000000104))
                CenterArc((-1.7999999598, 2.1000000313), 0.45, 26.3877969961, 127.2244060078)
            make_face()
            # Profile area: 0.1442015122, perimeter: 1.8054439437
            with BuildLine():
                Line((-0.2968871127, 2.3000000104), (-1.1031129082, 2.3000000104))
                CenterArc((-0.7000000104, 2.1000000313), 0.45, 26.3877969961, 127.2244060078)
            make_face()
            # Profile area: 0.1612904007, perimeter: 1.8710769749
            with BuildLine():
                Line((-1.1128398927, 1.9209379427), (-0.2871601281, 1.9209379427))
                CenterArc((-0.7000000104, 2.1000000313), 0.45, -156.552053401, 133.104106802)
            make_face()
            # Profile area: 0.3306805994, perimeter: 2.41472359
            with BuildLine():
                CenterArc((-0.7000000104, 2.1000000313), 0.45, 153.6122030039, 49.8357435951)
                Line((-1.1128398927, 1.9209379427), (-0.2871601281, 1.9209379427))
                CenterArc((-0.7000000104, 2.1000000313), 0.45, -23.447946599, 49.8357435951)
                Line((-0.2968871127, 2.3000000104), (-1.1031129082, 2.3000000104))
            make_face()
        # Symmetric extrude, each_side=-0.3
        extrude(amount=-0.3, both=True, mode=Mode.SUBTRACT)
    return part.part


def model_53233_8dbca22c_0028():
    """Model: Roller for Table v1 (4)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 45.6036731188, perimeter: 23.9389360204
            Circle(3.81)
        # OneSide extrude, distance=71.12
        extrude(amount=71.12)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 71.12, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 5.067074791, perimeter: 7.9796453401
            Circle(1.27)
        # OneSide extrude, distance=-71.12
        extrude(amount=-71.12, mode=Mode.SUBTRACT)
    return part.part


def model_53233_8dbca22c_0030():
    """Model: Cap for Table Bolts v1 (5)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 20.2682991639, perimeter: 15.9592906802
            Circle(2.54)
        # OneSide extrude, distance=2.54
        extrude(amount=2.54)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 11.4009182797, perimeter: 11.9694680102
            Circle(1.905)
        # OneSide extrude, distance=1.905
        extrude(amount=1.905, mode=Mode.SUBTRACT)
    return part.part


def model_53470_39f2e9dc_0001():
    """Model: bearing"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 6 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 72.0053028206, perimeter: 66.1131248635
            with BuildLine():
                Line((50, 45), (57.7, 45))
                Line((57.7, 45), (57.7, 45.500000678))
                Line((57.7, 45.500000678), (52.1794508717, 45.500000678))
                CenterArc((50, 50), 5, -64.1580494127, 308.3160988255)
                Line((47.8205491283, 45.500000678), (42.7, 45.500000678))
                Line((42.7, 45.500000678), (42.7, 45.0000006706))
                Line((50, 45), (42.7, 45.0000006706))
            make_face()
            with BuildLine():
                CenterArc((50, 50), 2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=3
        extrude(amount=3)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 45.500000678, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.0106192983, perimeter: 5.0265482457
            with Locations((-44.5, 1.5)):
                Circle(0.8)
            # Profile area: 2.0106192983, perimeter: 5.0265482457
            with Locations((-56, 1.5)):
                Circle(0.8)
        # OneSide extrude, distance=-3
        extrude(amount=-3, mode=Mode.SUBTRACT)
    return part.part


def model_53470_39f2e9dc_0004():
    """Model: gasket"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 29 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 10.7853981634, perimeter: 42.7123889804
            with BuildLine():
                CenterArc((45.5, 5), 0.5, 0, 90)
                Line((45, 5.5), (45.5, 5.5))
                CenterArc((45, 5), 0.5, 90, 90)
                Line((44.5, 0), (44.5, 5))
                CenterArc((45, 0), 0.5, 180, 90)
                Line((50, -0.5), (45, -0.5))
                CenterArc((50, 0), 0.5, -90, 90)
                Line((50.5, 0.5), (50.5, 0))
                CenterArc((50, 0.5), 0.5, 0, 90)
                Line((46.5, 1), (50, 1))
                CenterArc((46.5, 1.5), 0.5, 180, 90)
                Line((46, 5), (46, 1.5))
            make_face()
            with BuildLine():
                Line((45, 0), (45, 5))
                Line((45, 5), (45.5, 5))
                Line((45.5, 5), (45.5, 0.5))
                Line((45.5, 0.5), (50, 0.5))
                Line((50, 0.5), (50, 0))
                Line((45, 0), (50, 0))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=5
        extrude(amount=5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 48.4646018366, perimeter: 54.7123889804
            with BuildLine():
                Line((-51.5, 1.5), (-51.5, -6.5))
                Line((-51.5, -6.5), (-43.5, -6.5))
                Line((-43.5, -6.5), (-43.5, 1.5))
                Line((-43.5, 1.5), (-51.5, 1.5))
            make_face()
            with BuildLine():
                CenterArc((-46.5, -1.5), 0.5, 0, 90)
                Line((-50, -1), (-46.5, -1))
                CenterArc((-50, -0.5), 0.5, -180, 90)
                Line((-50.5, 0), (-50.5, -0.5))
                CenterArc((-50, 0), 0.5, 90, 90)
                Line((-45, 0.5), (-50, 0.5))
                CenterArc((-45, 0), 0.5, 0, 90)
                Line((-44.5, -5), (-44.5, 0))
                CenterArc((-45, -5), 0.5, -90, 90)
                Line((-45.5, -5.5), (-45, -5.5))
                CenterArc((-45.5, -5), 0.5, 180, 90)
                Line((-46, -1.5), (-46, -5))
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 10.7853981634, perimeter: 42.7123889804
            with BuildLine():
                Line((-46, -1.5), (-46, -5))
                CenterArc((-45.5, -5), 0.5, 180, 90)
                Line((-45.5, -5.5), (-45, -5.5))
                CenterArc((-45, -5), 0.5, -90, 90)
                Line((-44.5, -5), (-44.5, 0))
                CenterArc((-45, 0), 0.5, 0, 90)
                Line((-45, 0.5), (-50, 0.5))
                CenterArc((-50, 0), 0.5, 90, 90)
                Line((-50.5, 0), (-50.5, -0.5))
                CenterArc((-50, -0.5), 0.5, -180, 90)
                Line((-50, -1), (-46.5, -1))
                CenterArc((-46.5, -1.5), 0.5, 0, 90)
            make_face()
            with BuildLine():
                Line((-50, -0.5), (-50, 0))
                Line((-50, 0), (-45, 0))
                Line((-45, 0), (-45, -5))
                Line((-45, -5), (-45.5, -5))
                Line((-45.5, -5), (-45.5, -0.5))
                Line((-45.5, -0.5), (-50, -0.5))
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 4.75, perimeter: 20
            with BuildLine():
                Line((-45.5, -0.5), (-50, -0.5))
                Line((-45.5, -5), (-45.5, -0.5))
                Line((-45, -5), (-45.5, -5))
                Line((-45, 0), (-45, -5))
                Line((-50, 0), (-45, 0))
                Line((-50, -0.5), (-50, 0))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)
    return part.part


def model_53470_39f2e9dc_0005():
    """Model: belt"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 26 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 69.5391187915, perimeter: 279.7787834742
            with BuildLine():
                Line((-188.75, 30), (-191.5223950224, 68.1166148266))
                CenterArc((-200, 67.5), 8.5, 4.160057349, 171.6798853019)
                Line((-211.25, 30), (-208.4776049776, 68.1166148266))
                CenterArc((-200, 30), 11.25, 180, 86.2606498514)
                CenterArc((-200.7500029877, 18.5244827777), 0.25, 0, 86.2606498514)
                Line((-200.5000029877, 16.75), (-200.5000029877, 18.5244827777))
                Line((-200.050002981, 16.75), (-200.5000029877, 16.75))
                Line((-200.050002981, 19.0040917514), (-200.050002981, 16.75))
                CenterArc((-200.300002981, 19.0040917514), 0.25, 0, 88.4371785215)
                CenterArc((-200, 30), 10.75, 180, 88.4371785215)
                Line((-210.75, 30), (-207.9789023037, 68.0806186604))
                CenterArc((-200, 67.5), 8, 4.1620342092, 171.6759315816)
                Line((-189.25, 30), (-192.0210976963, 68.0806186604))
                CenterArc((-200, 30), 10.75, -88.4372095794, 88.4372095794)
                CenterArc((-199.7000029795, 19.0040915888), 0.25, 91.5627904206, 88.4372095794)
                Line((-199.9500029795, 16.75), (-199.9500029795, 19.0040915888))
                Line((-199.9500029795, 16.75), (-199.5000029728, 16.75))
                Line((-199.5000029728, 16.75), (-199.5000029728, 18.5244823882))
                CenterArc((-199.2500029728, 18.5244823882), 0.25, 93.7393203888, 86.2606796112)
                CenterArc((-200, 30), 11.25, -86.2606796112, 86.2606796112)
            make_face()
        # OneSide extrude, distance=8
        extrude(amount=8)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-200.5000029877, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            with Locations((1.5000000224, 17.7000002638)):
                Circle(0.4)
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            with Locations((6.5000000969, 17.7000002638)):
                Circle(0.4)
        # OneSide extrude, distance=-1.5
        extrude(amount=-1.5, mode=Mode.SUBTRACT)
    return part.part


def model_53601_59d3ecd2_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 286, perimeter: 70
            with BuildLine():
                Line((12, -6), (-10, -6))
                Line((12, 7), (12, -6))
                Line((-10, 7), (12, 7))
                Line((-10, -6), (-10, 7))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            with Locations((-10, 4)):
                Circle(1)
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            with Locations((8, 4)):
                Circle(1)
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            with Locations((8, -5)):
                Circle(1)
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            with Locations((-10, -5)):
                Circle(1)
        # OneSide extrude, distance=7
        extrude(amount=7, mode=Mode.ADD)
    return part.part


def model_53708_7763f0a7_0000():
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
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 105.4340943906, perimeter: 57.4529240442
            with BuildLine():
                CenterArc((0.4792679428, 50.7131488831), 0.254, 13.7943096049, 168.6715681163)
                Line((0.2255031413, 50.7022206854), (1.2956327674, 25.8526306857))
                CenterArc((2.056927172, 25.8854152788), 0.762, -177.5341222788, 99.7122353929)
                _nurbs_edge([(0.725942066, 50.7737118829), (0.8713370745, 50.1815155526), (1.1660285139, 49.0347671546), (1.6197706763, 47.427573495), (2.2500262958, 45.4945377527), (3.0868890385, 43.3374469202), (3.9748233135, 41.3258403891), (4.9038232748, 39.3486913811), (5.8436849232, 37.3245515029), (6.7368257036, 35.2257734997), (7.4865887752, 33.1122546332), (7.9764008258, 31.1003692336), (8.0945073782, 29.3210688889), (7.7577560705, 27.8818844257), (6.9370126744, 26.8270584372), (5.686477866, 26.093585278), (4.4174997708, 25.6712867892), (3.3553461111, 25.3962608), (2.6040892515, 25.223954746), (2.2176721464, 25.1405629087)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0666666667, 0.1333333333, 0.2, 0.2666666667, 0.3333333333, 0.4, 0.4666666667, 0.5333333333, 0.6, 0.6666666667, 0.7333333333, 0.8, 0.8666666667, 0.9333333333, 1, 1, 1, 1, 1, 1], 5)
            make_face()
        # OneSide extrude, distance=-25.4
        extrude(amount=-25.4)
    return part.part


def model_53714_22f87ede_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 25, perimeter: 20
            with BuildLine():
                Line((5.5, -6), (0.5, -6))
                Line((5.5, -1), (5.5, -6))
                Line((0.5, -1), (5.5, -1))
                Line((0.5, -6), (0.5, -1))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 20 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1, perimeter: 4
            with BuildLine():
                Line((-0.5, 1), (-1.5, 1))
                Line((-0.5, 2), (-0.5, 1))
                Line((-1.5, 2), (-0.5, 2))
                Line((-1.5, 1), (-1.5, 2))
            make_face()
            # Profile area: 1, perimeter: 4
            with BuildLine():
                Line((-0.5, 5), (-0.5, 6))
                Line((-0.5, 6), (-1.5, 6))
                Line((-1.5, 6), (-1.5, 5))
                Line((-1.5, 5), (-0.5, 5))
            make_face()
            # Profile area: 1, perimeter: 4
            with BuildLine():
                Line((-4.5, 6), (-4.5, 5))
                Line((-5.5, 6), (-4.5, 6))
                Line((-5.5, 5), (-5.5, 6))
                Line((-4.5, 5), (-5.5, 5))
            make_face()
            # Profile area: 1, perimeter: 4
            with BuildLine():
                Line((-5.5, 2), (-5.5, 1))
                Line((-5.5, 1), (-4.5, 1))
                Line((-4.5, 1), (-4.5, 2))
                Line((-4.5, 2), (-5.5, 2))
            make_face()
        # OneSide extrude, distance=4
        extrude(amount=4, mode=Mode.ADD)
    return part.part


def model_53730_62d1957d_0013():
    """Model: 17.Sruba klucza"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(-6.9514938549, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((-59.754957917, 6.4090529967)):
                Circle(0.15)
        # OneSide extrude, distance=-0.4
        extrude(amount=-0.4)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(-6.9514938549, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.2611448893, perimeter: 2.9845130209
            with BuildLine():
                CenterArc((-59.754957917, 6.4090529967), 0.325, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-59.754957917, 6.4090529967), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((-59.754957917, 6.4090529967)):
                Circle(0.15)
        # OneSide extrude, distance=0.25
        extrude(amount=0.25, mode=Mode.ADD)
    return part.part


def model_53822_3d84a196_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.01, perimeter: 2.02
            with BuildLine():
                Line((1, -0.01), (0, -0.01))
                Line((1, 0), (1, -0.01))
                Line((0, 0), (1, 0))
                Line((0, -0.01), (0, 0))
            make_face()
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)

        # Sketch2 -> Extrude2 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0027499999, perimeter: 0.5699999996
            with BuildLine():
                Line((0.0499999989, -0.0399999991), (0.0499999989, -0.0499999989))
                Line((0.0499999989, -0.0499999989), (0.3249999989, -0.0499999989))
                Line((0.3249999989, -0.0499999989), (0.3249999989, -0.0399999991))
                Line((0.3249999989, -0.0399999991), (0.0499999989, -0.0399999991))
            make_face()
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)
    return part.part


def model_53831_de0554da_0002():
    """Model: short piston"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 28.2743338823, perimeter: 18.8495559215
            with Locations((7.5, 40)):
                Circle(3)
        # OneSide extrude, distance=60
        extrude(amount=60)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 60), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 21.9911485751, perimeter: 43.9822971503
            with BuildLine():
                CenterArc((7.5, 40), 4, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((7.5, 40), 3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 28.2743338823, perimeter: 18.8495559215
            with Locations((7.5, 40)):
                Circle(3)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)
    return part.part


def model_53831_de0554da_0003():
    """Model: short servomotor"""
    with BuildPart() as part:
        # Sketch1 -> Extrude2 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 82.4668071567, perimeter: 65.9734457254
            with BuildLine():
                CenterArc((-100.2686108009, 75.9831092006), 6.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-100.2686108009, 75.9831092006), 4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=50
        extrude(amount=50)

        # Sketch2 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(50, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 82.4668071567, perimeter: 65.9734457254
            with BuildLine():
                CenterArc((-100.2686108009, 75.9831092006), 6.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-100.2686108009, 75.9831092006), 4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 21.9911485751, perimeter: 43.9822971503
            with BuildLine():
                CenterArc((-100.2686108009, 75.9831092006), 4, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-100.2686108009, 75.9831092006), 3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)
    return part.part


def model_53846_89405f98_0009():
    """Model: wkret1 v1"""
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
    return part.part


def model_53846_89405f98_0029():
    """Model: bolt short v1 (3)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            Circle(0.1)
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch2 -> Extrude2 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 15 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.1578539864, perimeter: 1.5141592892
            with BuildLine():
                CenterArc((-0.150000003, 1.4000000216), 0.05, 90, 90)
                Line((-0.200000003, 1.1000000156), (-0.200000003, 1.4000000216))
                CenterArc((-0.150000003, 1.1000000156), 0.05, -180, 90)
                Line((0.150000003, 1.0500000156), (-0.150000003, 1.0500000156))
                CenterArc((0.150000003, 1.1000000156), 0.05, -90, 90)
                Line((0.200000003, 1.4000000216), (0.200000003, 1.1000000156))
                CenterArc((0.150000003, 1.4000000216), 0.05, 0, 90)
                Line((-0.150000003, 1.4500000216), (0.150000003, 1.4500000216))
            make_face()
        # Symmetric extrude, each_side=0.05
        extrude(amount=0.05, both=True)
    return part.part


def model_53848_7c64ed9f_0003():
    """Model: Leg"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 14 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 19, perimeter: 76
            with BuildLine():
                Line((-5, 5), (5, 5))
                Line((-5, -5), (-5, 5))
                Line((5, -5), (-5, -5))
                Line((5, 5), (5, -5))
            make_face()
            with BuildLine():
                Line((4.5, 4.5), (4.5, -4.5))
                Line((4.5, -4.5), (-4.5, -4.5))
                Line((-4.5, -4.5), (-4.5, 4.5))
                Line((-4.5, 4.5), (4.5, 4.5))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=100
        extrude(amount=100)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -5, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 19.6349540849, perimeter: 15.7079632679
            with Locations((0, 50)):
                Circle(2.5)
        # OneSide extrude, distance=-17
        extrude(amount=-17, mode=Mode.SUBTRACT)
    return part.part


def model_53925_fa8c0add_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 21.4546476425, perimeter: 16.4197153957
            with Locations((-4.6046047395, -5.787254612)):
                Circle(2.6132788694)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


def model_53927_ef5208b9_0003():
    """Model: hook base"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.1309733553, perimeter: 3.7699111843
            with Locations((37.5, 0)):
                Circle(0.6)
        # OneSide extrude, distance=-4
        extrude(amount=-4)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(-4, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.5664364361, perimeter: 8.6196534455
            with BuildLine():
                Line((-38.2, 0.4041451884), (-38.2, -0.4041451884))
                Line((-38.2, -0.4041451884), (-37.5, -0.8082903769))
                Line((-37.5, -0.8082903769), (-36.8, -0.4041451884))
                Line((-36.8, -0.4041451884), (-36.8, 0.4041451884))
                Line((-36.8, 0.4041451884), (-37.5, 0.8082903769))
                Line((-37.5, 0.8082903769), (-38.2, 0.4041451884))
            make_face()
            with BuildLine():
                CenterArc((-37.5, 0), 0.6, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 1.1309733553, perimeter: 3.7699111843
            with Locations((-37.5, 0)):
                Circle(0.6)
        # OneSide extrude, distance=1.2
        extrude(amount=1.2, mode=Mode.ADD)
    return part.part


def model_54077_dd26efde_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 96.1288198201, perimeter: 36.4965751818
            with BuildLine():
                Line((2.5, 2.5), (-3.5, 3.5))
                Line((-3.5, 3.5), (-7.3660254038, -1.1961524227))
                Line((-7.3660254038, -1.1961524227), (-5.2320508076, -6.8923048454))
                Line((-5.2320508076, -6.8923048454), (0.7679491924, -7.8923048454))
                Line((0.7679491924, -7.8923048454), (4.6339745962, -3.1961524227))
                Line((4.6339745962, -3.1961524227), (2.5, 2.5))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 16 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0.5, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.5, perimeter: 3
            with BuildLine():
                Line((-2, 1), (-3, 1))
                Line((-2, 1.5), (-2, 1))
                Line((-3, 1.5), (-2, 1.5))
                Line((-3, 1), (-3, 1.5))
            make_face()
            # Profile area: 0.5, perimeter: 3
            with BuildLine():
                Line((1.5, 0.5), (0.5, 0.5))
                Line((1.5, 1), (1.5, 0.5))
                Line((0.5, 1), (1.5, 1))
                Line((0.5, 0.5), (0.5, 1))
            make_face()
            # Profile area: 0.5, perimeter: 3
            with BuildLine():
                Line((0.5, -5.5), (-0.5, -5.5))
                Line((0.5, -5), (0.5, -5.5))
                Line((-0.5, -5), (0.5, -5))
                Line((-0.5, -5.5), (-0.5, -5))
            make_face()
            # Profile area: 0.4865791433, perimeter: 3.0467323452
            with BuildLine():
                Line((-3, -4.5), (-4.0675948066, -4.5))
                Line((-3, -4.0442286341), (-3, -4.5))
                Line((-4.0675948066, -4.0442286341), (-3, -4.0442286341))
                Line((-4.0675948066, -4.5), (-4.0675948066, -4.0442286341))
            make_face()
        # OneSide extrude, distance=7
        extrude(amount=7, mode=Mode.ADD)
    return part.part


def model_54177_2b99e039_0005():
    """Model: partition"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.36, perimeter: 14
            with BuildLine():
                Line((25, 0), (31.8, 0))
                Line((31.8, 0), (31.8, 0.2))
                Line((31.8, 0.2), (25, 0.2))
                Line((25, 0), (25, 0.2))
            make_face()
        # OneSide extrude, distance=-37.7
        extrude(amount=-37.7)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 10 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.4000004439, perimeter: 14.5999997854
            with BuildLine():
                Line((-25.0000003725, -5.300000079), (-31.8, -5.300000079))
                Line((-25, -4.8), (-25.0000003725, -5.300000079))
                Line((-31.8, -4.8), (-25, -4.8))
                Line((-31.8, -4.8), (-31.8, -5.300000079))
            make_face()
            # Profile area: 3.4, perimeter: 14.6
            with BuildLine():
                Line((-31.8, -33.5132), (-25, -33.5132))
                Line((-25, -33.5132), (-25, -33.0132))
                Line((-25, -33.0132), (-31.8, -33.0132))
                Line((-31.8, -33.5132), (-31.8, -33.0132))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)
    return part.part


def model_54177_2b99e039_0011():
    """Model: beam hitch"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.2500000075, perimeter: 2.0000000298
            with BuildLine():
                Line((-5.500000082, 0), (-5.0000000745, 0))
                Line((-5.0000000745, 0), (-5.0000000745, 0.5000000075))
                Line((-5.0000000745, 0.5000000075), (-5.500000082, 0.5000000075))
                Line((-5.500000082, 0.5000000075), (-5.500000082, 0))
            make_face()
        # OneSide extrude, distance=11
        extrude(amount=11)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 5.500000082), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            with Locations((2.5000000373, 0.2500000037)):
                Circle(0.1)
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            with Locations((8.5000001267, 0.2500000037)):
                Circle(0.1)
        # OneSide extrude, distance=-0.4
        extrude(amount=-0.4, mode=Mode.SUBTRACT)
    return part.part


def model_54273_21c2b38f_0009():
    """Model: kropki-pomar  ROG v1 (2)"""
    with BuildPart() as part:
        # Sketch7 -> Extrude1 (NewBody)
        # Sketch on Plane1 construction plane
        with BuildSketch(Plane(origin=(0, 1.15, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.3984, perimeter: 13.28
            with BuildLine():
                Line((-0.86, -0.86), (0.86, -0.86))
                Line((0.86, -0.86), (0.86, 0.86))
                Line((0.86, 0.86), (-0.86, 0.86))
                Line((-0.86, 0.86), (-0.86, -0.86))
            make_face()
            with BuildLine():
                Line((0.8, 0.8), (0.8, -0.8))
                Line((0.8, -0.8), (-0.8, -0.8))
                Line((-0.8, -0.8), (-0.8, 0.8))
                Line((-0.8, 0.8), (0.8, 0.8))
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 2.56, perimeter: 6.4
            with BuildLine():
                Line((-0.8, 0.8), (0.8, 0.8))
                Line((-0.8, -0.8), (-0.8, 0.8))
                Line((0.8, -0.8), (-0.8, -0.8))
                Line((0.8, 0.8), (0.8, -0.8))
            make_face()
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.25, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1256637099, perimeter: 1.2566370802
            with Locations((-0.5000000075, 0.5000000075)):
                Circle(0.200000003)
            # Profile area: 0.1256637099, perimeter: 1.2566370802
            with Locations((0, 0.5000000075)):
                Circle(0.200000003)
            # Profile area: 0.1256637099, perimeter: 1.2566370802
            with Locations((0.5000000075, 0.5000000075)):
                Circle(0.200000003)
            # Profile area: 0.1256637099, perimeter: 1.2566370802
            with Locations((0.5000000075, 0)):
                Circle(0.200000003)
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            Circle(0.2)
            # Profile area: 0.1256637099, perimeter: 1.2566370802
            with Locations((-0.5000000075, 0)):
                Circle(0.200000003)
            # Profile area: 0.1256637099, perimeter: 1.2566370802
            with Locations((-0.5000000075, -0.5000000075)):
                Circle(0.200000003)
            # Profile area: 0.1256637099, perimeter: 1.2566370802
            with Locations((0, -0.5000000075)):
                Circle(0.200000003)
            # Profile area: 0.1256637099, perimeter: 1.2566370802
            with Locations((0.5000000075, -0.5000000075)):
                Circle(0.200000003)
        # OneSide extrude, distance=0.05
        extrude(amount=0.05, mode=Mode.ADD)
    return part.part


def model_54273_21c2b38f_0028():
    """Model: side piece v3 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.2481717639, perimeter: 7.2090797377
            with BuildLine():
                Line((-0.9022699344, 0.9), (0.9022699344, 0.9))
                Line((-0.9022699344, -0.9), (-0.9022699344, 0.9))
                Line((0.9022699344, -0.9), (-0.9022699344, -0.9))
                Line((0.9022699344, 0.9), (0.9022699344, -0.9))
            make_face()
        # OneSide extrude, distance=1.8
        extrude(amount=1.8)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 13 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.9022699344, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 7.519080086, perimeter: 14.9380858107
            with BuildLine():
                Line((1.7997216236, -0.8997216236), (0.2987216236, -0.8997216236))
                Line((0.2987216236, 0), (0.2987216236, -0.8997216236))
                CenterArc((1.7997216236, -0.8997216236), 1.75, 149.0609036225, 331.878192755)
                Line((0.9, 0.6012783764), (1.7997216236, 0.6012783764))
                Line((1.7997216236, -0.8997216236), (1.7997216236, 0.6012783764))
            make_face()
            # Profile area: 0.1052910508, perimeter: 1.5083457159
            with BuildLine():
                Line((0.5622847565, 0.3377152435), (0.9, 0))
                CenterArc((1.7997216236, -0.8997216236), 1.75, 135, 14.0609036225)
                Line((0.2987216236, 0), (0.9, 0))
            make_face()
            # Profile area: 0.1052910508, perimeter: 1.5083457159
            with BuildLine():
                Line((0.9, 0), (0.9, 0.6012783764))
                CenterArc((1.7997216236, -0.8997216236), 1.75, 120.9390963775, 14.0609036225)
                Line((0.5622847565, 0.3377152435), (0.9, 0))
            make_face()
            # Profile area: 0.945732657, perimeter: 4.2743985225
            with BuildLine():
                Line((0.9, 0), (1.7997216236, -0.8997216236))
                Line((0.2987216236, 0), (0.9, 0))
                Line((0.2987216236, 0), (0.2987216236, -0.8997216236))
                Line((1.7997216236, -0.8997216236), (0.2987216236, -0.8997216236))
            make_face()
            # Profile area: 0.945732657, perimeter: 4.2743985225
            with BuildLine():
                Line((1.7997216236, -0.8997216236), (1.7997216236, 0.6012783764))
                Line((0.9, 0.6012783764), (1.7997216236, 0.6012783764))
                Line((0.9, 0), (0.9, 0.6012783764))
                Line((0.9, 0), (1.7997216236, -0.8997216236))
            make_face()
        # OneSide extrude, distance=-2.25
        extrude(amount=-2.25, mode=Mode.SUBTRACT)
    return part.part


def model_54273_21c2b38f_0055():
    """Model: bolt v2 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            Circle(0.2)
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)
    return part.part


def model_54383_13d47b0e_0007():
    """Model: gasketi"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 7 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 9.504133152, perimeter: 43.3753944282
            with BuildLine():
                Line((140.5, 5), (139.6213203436, 7.1213203436))
                Line((139.6213203436, 7.1213203436), (137.5, 8))
                Line((137.5, 8), (135.3786796564, 7.1213203436))
                Line((135.3786796564, 7.1213203436), (134.5, 5))
                Line((134.5, 5), (135.5355339059, 2.5))
                Line((133.5, 2.5), (135.5355339059, 2.5))
                Line((133.5, 2), (133.5, 2.5))
                Line((137.5, 2), (133.5, 2))
                Line((141.5, 2.0000000298), (137.5, 2))
                Line((141.5, 2.5), (141.5, 2.0000000298))
                Line((139.4644660941, 2.5), (141.5, 2.5))
                Line((139.4644660941, 2.5), (140.5, 5))
            make_face()
            with BuildLine():
                CenterArc((137.5, 5), 2.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-4
        extrude(amount=-4)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 9.504133152, perimeter: 43.3753944282
            with BuildLine():
                Line((139.4644660941, 2.5), (140.5, 5))
                Line((140.5, 5), (139.6213203436, 7.1213203436))
                Line((139.6213203436, 7.1213203436), (137.5, 8))
                Line((137.5, 8), (135.3786796564, 7.1213203436))
                Line((135.3786796564, 7.1213203436), (134.5, 5))
                Line((134.5, 5), (135.5355339059, 2.5))
                Line((135.5355339059, 2.5), (133.5, 2.5))
                Line((133.5, 2.5), (133.5, 2))
                Line((133.5, 2), (137.5, 2))
                Line((137.5, 2), (141.5, 2.0000000298))
                Line((141.5, 2.0000000298), (141.5, 2.5))
                Line((141.5, 2.5), (139.4644660941, 2.5))
            make_face()
            with BuildLine():
                CenterArc((137.5, 5), 2.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 19.6349540849, perimeter: 15.7079632679
            with Locations((137.5, 5)):
                Circle(2.5)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)
    return part.part


def model_54383_13d47b0e_0009():
    """Model: handle knob"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 5 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 42.5022128562, perimeter: 47.1327412287
            with BuildLine():
                Line((-42, 9.5), (-42, 15.5))
                Line((-42, 15.5), (-50, 15.5))
                CenterArc((-50, 12.5), 3, 90, 180)
                Line((-42, 9.5), (-50, 9.5))
            make_face()
            with BuildLine():
                CenterArc((-50, 12.5), 2.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-6
        extrude(amount=-6)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 42), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            with Locations((3, 12.5)):
                Circle(1)
        # OneSide extrude, distance=-5
        extrude(amount=-5, mode=Mode.SUBTRACT)
    return part.part


def model_54383_13d47b0e_0013():
    """Model: degree"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 28 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 441.682876357, perimeter: 91.5712190629
            with BuildLine():
                Line((-101.4565151814, 12), (-102.1141099118, 12))
                CenterArc((-165.0416848883, -3.1111474733), 64.7165084842, 13.5030762099, 1.6739311704)
                CenterArc((-106.2015886937, 12.8500002474), 3.75, 15.1770073803, 74.8229926197)
                Line((-111.6000017077, 16.6000002474), (-106.2015886937, 16.6000002474))
                CenterArc((-111.6000017077, 13.6000002474), 3, 90, 90)
                Line((-114.6000017077, 0), (-114.6000017077, 13.6000002474))
                Line((-114.6000017077, 0), (-114.6000017077, -13.6000002474))
                CenterArc((-111.6000017077, -13.6000002474), 3, 180, 90)
                Line((-111.6000017077, -16.6000002474), (-106.0379307164, -16.6000002474))
                CenterArc((-106.0379307164, -12.8500002474), 3.75, -90, 72.1291115867)
                CenterArc((-143.4235743862, -0.7957399669), 43.0309310418, -17.8708884133, 2.7784617332)
                Line((-101.4083410154, -12), (-101.8769068491, -12))
                CenterArc((-145.3749952906, -0.7573537722), 45.3813153441, -14.3436597624, 15.2998944797)
                CenterArc((-148.5769230769, 0.1923076923), 48.577303732, -0.226822962, 14.2946369498)
            make_face()
            with BuildLine():
                CenterArc((-109, -9.5), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-109, 9.5), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 14.4223087551, perimeter: 63.7882150131
            with BuildLine():
                CenterArc((-105.6935483091, 13.25), 3.75, 16.9351314223, 73.0648685777)
                Line((-112, 17), (-105.6935483091, 17))
                CenterArc((-112, 14), 3, 90, 90)
                Line((-115, 0), (-115, 14))
                Line((-114.6000017077, 0), (-115, 0))
                Line((-114.6000017077, 0), (-114.6000017077, 13.6000002474))
                CenterArc((-111.6000017077, 13.6000002474), 3, 90, 90)
                Line((-111.6000017077, 16.6000002474), (-106.2015886937, 16.6000002474))
                CenterArc((-106.2015886937, 12.8500002474), 3.75, 15.1770073803, 74.8229926197)
                CenterArc((-165.0416848883, -3.1111474733), 64.7165084842, 13.5030762099, 1.6739311704)
                Line((-101.4565151814, 12), (-102.1141099118, 12))
                CenterArc((-148.5769230769, 0.1923076923), 48.577303732, 14.0678139879, 2.8673174344)
            make_face()
            # Profile area: 13.7717171701, perimeter: 63.8183971911
            with BuildLine():
                Line((-101.4083410154, -12), (-101.8769068491, -12))
                CenterArc((-143.4235743862, -0.7957399669), 43.0309310418, -17.8708884133, 2.7784617332)
                CenterArc((-106.0379307164, -12.8500002474), 3.75, -90, 72.1291115867)
                Line((-111.6000017077, -16.6000002474), (-106.0379307164, -16.6000002474))
                CenterArc((-111.6000017077, -13.6000002474), 3, 180, 90)
                Line((-114.6000017077, 0), (-114.6000017077, -13.6000002474))
                Line((-114.6000017077, 0), (-115, 0))
                Line((-115, 0), (-115, -14))
                CenterArc((-112, -14), 3, 180, 90)
                Line((-112, -17), (-105.6622743122, -17))
                CenterArc((-105.6622743122, -13.25), 3.75, -90, 72.5377056348)
                CenterArc((-145.3749952906, -0.7573537722), 45.3813153441, -17.4622943652, 3.1186346028)
            make_face()
        # OneSide extrude, distance=0.8
        extrude(amount=0.8)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on YZ construction plane
        # Sketch has 28 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 14.4223087551, perimeter: 63.7882150131
            with BuildLine():
                CenterArc((-105.6935483091, 13.25), 3.75, 16.9351314223, 73.0648685777)
                Line((-112, 17), (-105.6935483091, 17))
                CenterArc((-112, 14), 3, 90, 90)
                Line((-115, 0), (-115, 14))
                Line((-114.6000017077, 0), (-115, 0))
                Line((-114.6000017077, 0), (-114.6000017077, 13.6000002474))
                CenterArc((-111.6000017077, 13.6000002474), 3, 90, 90)
                Line((-111.6000017077, 16.6000002474), (-106.2015886937, 16.6000002474))
                CenterArc((-106.2015886937, 12.8500002474), 3.75, 15.1770073803, 74.8229926197)
                CenterArc((-165.0416848883, -3.1111474733), 64.7165084842, 13.5030762099, 1.6739311704)
                Line((-101.4565151814, 12), (-102.1141099118, 12))
                CenterArc((-148.5769230769, 0.1923076923), 48.577303732, 14.0678139879, 2.8673174344)
            make_face()
            # Profile area: 13.7717171701, perimeter: 63.8183971911
            with BuildLine():
                Line((-101.4083410154, -12), (-101.8769068491, -12))
                CenterArc((-143.4235743862, -0.7957399669), 43.0309310418, -17.8708884133, 2.7784617332)
                CenterArc((-106.0379307164, -12.8500002474), 3.75, -90, 72.1291115867)
                Line((-111.6000017077, -16.6000002474), (-106.0379307164, -16.6000002474))
                CenterArc((-111.6000017077, -13.6000002474), 3, 180, 90)
                Line((-114.6000017077, 0), (-114.6000017077, -13.6000002474))
                Line((-114.6000017077, 0), (-115, 0))
                Line((-115, 0), (-115, -14))
                CenterArc((-112, -14), 3, 180, 90)
                Line((-112, -17), (-105.6622743122, -17))
                CenterArc((-105.6622743122, -13.25), 3.75, -90, 72.5377056348)
                CenterArc((-145.3749952906, -0.7573537722), 45.3813153441, -17.4622943652, 3.1186346028)
            make_face()
        # OneSide extrude, distance=-4
        extrude(amount=-4, mode=Mode.ADD)

        # Sketch2 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.1256637099, perimeter: 1.2566370802
            with Locations((103, 0)):
                Circle(0.200000003)
        # OneSide extrude, distance=0.15
        extrude(amount=0.15, mode=Mode.ADD)
    return part.part


def model_54478_21061ebc_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 8 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 9, perimeter: 20
            with BuildLine():
                Line((5, 1), (5, 0))
                Line((1, 1), (5, 1))
                Line((1, 5), (1, 1))
                Line((0, 5), (1, 5))
                Line((0, 0), (0, 5))
                Line((5, 0), (0, 0))
            make_face()
        # OneSide extrude, distance=5.5
        extrude(amount=5.5)
    return part.part


def model_54485_e9658dfb_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 24.7800007385, perimeter: 20.200000301
            with BuildLine():
                Line((0, 5.9000000879), (0, 0))
                Line((0, 0), (4.2000000626, 0))
                Line((4.2000000626, 0), (4.2000000626, 5.9000000879))
                Line((4.2000000626, 5.9000000879), (0, 5.9000000879))
            make_face()
        # OneSide extrude, distance=-2.5
        extrude(amount=-2.5)
    return part.part


def model_54494_37c2c718_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 4 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 342.3599129767, perimeter: 68.4103081948
            with BuildLine():
                CenterArc((9.9729900742, 14.9846411028), 18, -123.6456504534, 67.4981018725)
                Line((20, 0.0360936166), (20, 13.0360936166))
                CenterArc((10.0270099258, -1.9485474862), 18, 56.3543495466, 67.4981018725)
                Line((0, 13), (0, 0))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch8 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 14 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(1, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 40.7507904247, perimeter: 115.8520296053
            with BuildLine():
                Line((1.7722934667, 13), (18.1509748749, 13))
                Line((1.7722934667, -1), (1.7722934667, 13))
                Line((18.1509748749, -1), (1.7722934667, -1))
                Line((18.1509748749, 13), (18.1509748749, -1))
            make_face()
            with BuildLine():
                Line((2.5355548218, -0.3475873482), (17.3877135199, -0.3475873482))
                Line((2.5355548218, 12.3475873482), (2.5355548218, -0.3475873482))
                Line((17.3877135199, 12.3475873482), (2.5355548218, 12.3475873482))
                Line((17.3877135199, -0.3475873482), (17.3877135199, 12.3475873482))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.01
        extrude(amount=-0.01, mode=Mode.SUBTRACT)
    return part.part


def model_54638_8ce7a3a8_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 10 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 498.3501803444, perimeter: 217.7327351998
            with BuildLine():
                CenterArc((45, 11.1), 10.6, 180, 180)
                Line((55.6, 11.1), (55.6, 19.3))
                CenterArc((60.6, 19.3), 5, 90, 90)
                Line((77.5, 24.3), (60.6, 24.3))
                Line((77.5, 27.5), (77.5, 24.3))
                Line((12.5, 27.5), (77.5, 27.5))
                Line((12.5, 24.3), (12.5, 27.5))
                Line((29.4, 24.3), (12.5, 24.3))
                CenterArc((29.4, 19.3), 5, 0, 90)
                Line((34.4, 11.1), (34.4, 19.3))
            make_face()
            with BuildLine():
                CenterArc((45, 11.1), 7.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=25
        extrude(amount=25)

        # Sketch3 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 27.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.9087385212, perimeter: 7.853981634
            with Locations((-20, 6.25)):
                Circle(1.25)
            # Profile area: 4.9087385212, perimeter: 7.853981634
            with Locations((-20, 18.75)):
                Circle(1.25)
            # Profile area: 4.9087385212, perimeter: 7.853981634
            with Locations((-70, 6.25)):
                Circle(1.25)
            # Profile area: 4.9087385212, perimeter: 7.853981634
            with Locations((-70, 19.1030164872)):
                Circle(1.25)
        # OneSide extrude, distance=-15
        extrude(amount=-15, mode=Mode.SUBTRACT)
    return part.part


def model_54650_df3655c1_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 12, perimeter: 19
            with BuildLine():
                Line((-6, -0.3901553), (-7.5, -0.3901553))
                Line((-7.5, -0.3901553), (-7.5, -8.3901553))
                Line((-7.5, -8.3901553), (-6, -8.3901553))
                Line((-6, -8.3901553), (-6, -0.3901553))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


def model_54654_f19e7f7d_0003():
    """Model: switch"""
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
        # Sketch has 13 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.9403317777, perimeter: 8.4557519189
            with BuildLine():
                CenterArc((0.55, -20.55), 0.55, 90, 90)
                Line((0, -20.65), (0, -20.55))
                CenterArc((0.55, -20.65), 0.55, 180, 90)
                Line((2.95, -21.2), (0.55, -21.2))
                CenterArc((2.95, -20.65), 0.55, -90, 90)
                Line((3.5, -20.55), (3.5, -20.65))
                CenterArc((2.95, -20.55), 0.55, 0, 90)
                Line((0.55, -20), (2.95, -20))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 13 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 21.2), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.3237021725, perimeter: 2.7898077133
            with BuildLine():
                CenterArc((1.8618548241, 0.75), 0.25, 50.842979982, 39.157020018)
                _nurbs_edge([(2.0197167756, 0.9438545956), (2.0216051101, 0.9423168649), (2.0387500634, 0.9283439747), (2.0703381653, 0.9024071144), (2.1145309972, 0.8655831418), (2.1685418904, 0.8196003174), (2.2281976444, 0.7680911894), (2.2840031432, 0.7210153189), (2.3397329195, 0.6785271663), (2.4005632764, 0.6407350762), (2.4719381355, 0.6076965886), (2.558754953, 0.5794001392), (2.664153032, 0.5557184238), (2.7660126349, 0.5400730613), (2.8524100941, 0.5302341161), (2.9148998496, 0.5244642224), (2.9481693216, 0.5217190448), (2.95, 0.5215689402)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0.0584408876, 0.0584408876, 0.0584408876, 0.0584408876, 0.0584408876, 0.0584408876, 0.0666666667, 0.1333333333, 0.2, 0.2666666667, 0.3333333333, 0.4, 0.4666666667, 0.5333333333, 0.6, 0.6666666667, 0.7333333333, 0.8, 0.8038742651, 0.8038742651, 0.8038742651, 0.8038742651, 0.8038742651, 0.8038742651], 5)
                Line((2.95, 0.5215689402), (2.95, 1))
                Line((2.95, 1), (1.8618548241, 1))
            make_face()
            # Profile area: 0.1206383613, perimeter: 1.4184869002
            with BuildLine():
                Line((0.55, 1), (0.55, 0.5522624951))
                _nurbs_edge([(0.8333409732, 0.6000000089), (0.8314857228, 0.5996015355), (0.8078402284, 0.5945462856), (0.7613732628, 0.5851805381), (0.7063722109, 0.5752627809), (0.6487122524, 0.566044067), (0.5906737712, 0.5577323384), (0.5573254563, 0.5532369898), (0.55, 0.5522624951)], [1, 1, 1, 1, 1, 1, 1, 1, 1], [0.5943128846, 0.5943128846, 0.5943128846, 0.5943128846, 0.5943128846, 0.5943128846, 0.6, 0.6666666667, 0.7333333333, 0.7519798984, 0.7519798984, 0.7519798984, 0.7519798984, 0.7519798984, 0.7519798984], 5)
                Line((0.8333409732, 0.6000000089), (0.8333409732, 1))
                Line((0.8333409732, 1), (0.55, 1))
            make_face()
            # Profile area: 0.1836646201, perimeter: 2.1565558325
            with BuildLine():
                Line((0.8333409732, 0.6000000089), (0.8333409732, 1))
                _nurbs_edge([(1.4821673905, 0.9282546927), (1.4699094945, 0.9162009261), (1.4442892436, 0.8918216543), (1.4045593908, 0.8565585913), (1.3494459917, 0.8127939489), (1.2768746125, 0.7638767941), (1.1992186036, 0.7204107522), (1.1164908723, 0.6826660244), (1.0290642048, 0.6505953278), (0.9537474506, 0.6284251061), (0.8940752492, 0.6134865864), (0.8532337176, 0.6042726024), (0.8333409732, 0.6000000089)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0.0708761911, 0.0708761911, 0.0708761911, 0.0708761911, 0.0708761911, 0.0708761911, 0.1333333333, 0.2, 0.2666666667, 0.3333333333, 0.4, 0.4666666667, 0.5333333333, 0.5943128846, 0.5943128846, 0.5943128846, 0.5943128846, 0.5943128846, 0.5943128846], 5)
                CenterArc((1.6574536265, 0.75), 0.25, 90, 44.518935356)
                Line((1.6574536265, 1), (0.8333409732, 1))
            make_face()
            # Profile area: 2.2387199887, perimeter: 11.2635633035
            with BuildLine():
                Line((0.8333409732, 1), (0.55, 1))
                Line((1.6574536265, 1), (0.8333409732, 1))
                Line((1.8618548241, 1), (1.6574536265, 1))
                Line((2.95, 1), (1.8618548241, 1))
                Line((2.95, 0.5215689402), (2.95, 1))
                _nurbs_edge([(2.95, 0.5215689402), (2.9796708373, 0.5191361106), (3.0427088357, 0.5144814103), (3.1440087658, 0.5085398737), (3.2539732714, 0.5042311023), (3.3724138031, 0.5015064644), (3.4568230775, 0.5003810119), (3.5, 0.5)], [1, 1, 1, 1, 1, 1, 1, 1], [0.8038742651, 0.8038742651, 0.8038742651, 0.8038742651, 0.8038742651, 0.8038742651, 0.8666666667, 0.9333333333, 1, 1, 1, 1, 1, 1], 5)
                Line((3.5, 0.5), (3.5, 0.200000003))
                Line((3.5, 0.200000003), (3.9000000581, 0.9000000134))
                Line((3.9000000581, 0.9000000134), (3.3615252899, 1.4505509953))
                Line((3.3615252899, 1.4505509953), (-0.2037822565, 1.2516115151))
                Line((-0.2037822565, 1.2516115151), (-0.2978815084, 0.3500000015))
                Line((-0.2978815084, 0.3500000015), (0, 0.31891075))
                Line((0, 0.31891075), (0, 0.5))
                _nurbs_edge([(0.55, 0.5522624951), (0.5311349084, 0.5497528997), (0.4854987364, 0.5438864886), (0.4111527757, 0.5350744602), (0.3048277196, 0.5239559463), (0.1923185696, 0.5140130769), (0.0976727111, 0.5067248672), (0.0328458431, 0.5021879704), (0, 0.5)], [1, 1, 1, 1, 1, 1, 1, 1, 1], [0.7519798984, 0.7519798984, 0.7519798984, 0.7519798984, 0.7519798984, 0.7519798984, 0.8, 0.8666666667, 0.9333333333, 1, 1, 1, 1, 1, 1], 5)
                Line((0.55, 1), (0.55, 0.5522624951))
            make_face()
        # OneSide extrude, distance=-1.4
        extrude(amount=-1.4, mode=Mode.SUBTRACT)
    return part.part


def model_54659_e1303e28_0007():
    """Model: Arm 1 v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 27 constraints, 13 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 55.7471158745, perimeter: 66.9576235135
            with BuildLine():
                CenterArc((13.3966122601, 11.3442503264), 0.6, 0, 150.0434217599)
                Line((12.8767698112, 11.6438564484), (12.127754506, 10.3442503264))
                Line((7.8966122601, 10.3442503264), (12.127754506, 10.3442503264))
                Line((-0.4596266659, 0.3856725658), (7.8966122601, 10.3442503264))
                CenterArc((0, 0), 0.6, 140, 173.5)
                Line((0.4130127454, -0.4352246226), (7.1791154952, 5.9855671416))
                Line((7.1791154952, 5.9855671416), (7.5921282406, 5.550342519))
                CenterArc((8.0273528632, 5.9633552645), 0.6, -136.5, 158.043246458)
                Line((8.5854372654, 6.1836773015), (8.0346321729, 7.578888307))
                Line((8.0346321729, 7.578888307), (22.959329338, 9.1475371891))
                CenterArc((22.8966122601, 9.7442503264), 0.6, -84, 174)
                Line((13.9966122601, 10.3442503264), (22.8966122601, 10.3442503264))
                Line((13.9966122601, 10.3442503264), (13.9966122601, 11.3442503264))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((8.0273528632, 5.9633552645), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((22.8966122601, 9.7442503264), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((13.3966122601, 11.3442503264), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=1.5
        extrude(amount=1.5, both=True)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on XY construction plane
        # Sketch has 3 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 3.0159289474, perimeter: 7.5398223686
            with BuildLine():
                CenterArc((8.0273528632, 5.9633552645), 1, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((8.0273528632, 5.9633552645), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 4.398229715, perimeter: 8.7964594301
            with BuildLine():
                CenterArc((13.3966122601, 11.3442503264), 1.2, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((13.3966122601, 11.3442503264), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=0.5
        extrude(amount=0.5, both=True, mode=Mode.SUBTRACT)

        # Sketch2 -> Extrude3 (Cut)
        # Sketch on XY construction plane
        # Sketch has 3 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.6414821615, perimeter: 5.9690260418
            with BuildLine():
                CenterArc((22.8966122601, 9.7442503264), 0.75, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((22.8966122601, 9.7442503264), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=0.75
        extrude(amount=0.75, both=True, mode=Mode.SUBTRACT)
    return part.part


def model_54735_cf8dcb52_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 8 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 29.047738817, perimeter: 31.6084069043
            with BuildLine():
                Line((0, 0), (10, 0))
                Line((10, 0), (10, 1.8494006889))
                Line((10, 1.8494006889), (7.8006632103, 1.8494006889))
                CenterArc((5, 1.8494006889), 2.8006632103, 0, 180)
                Line((0, 1.8494006889), (2.1993367897, 1.8494006889))
                Line((0, 0), (0, 1.8494006889))
            make_face()
            with BuildLine():
                CenterArc((5, 1.8494006889), 0.75, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch2 -> Extrude2 (NewBody)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 623.6963461564, perimeter: 123.6643563159
            with BuildLine():
                Line((-1.9116293611, 3.6413083479), (-1.9116293611, -25.2792404489))
                Line((-1.9116293611, -25.2792404489), (20, -25.2792404489))
                Line((20, -25.2792404489), (20, 3.6413083479))
                Line((20, 3.6413083479), (-1.9116293611, 3.6413083479))
            make_face()
            with BuildLine():
                Line((10, 1), (0, 1))
                Line((10, 0), (10, 1))
                Line((0, 0), (10, 0))
                Line((0, 1), (0, 0))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


def model_54738_5424d7af_0002():
    """Model: Adorno Amarre v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            Circle(1)
        # OneSide extrude, distance=-2
        extrude(amount=-2)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on YZ construction plane
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 37.3775565427, perimeter: 33.8919293457
            with BuildLine():
                CenterArc((2.4290024623, 2.3255258384), 1.127958645, 97.6210713093, 77.3816329464)
                Line((4.4406518962, 3.7327010832), (2.2794115554, 3.4435210376))
                Line((3.8626348501, 5.102744056), (4.4406518962, 3.7327010832))
                Line((1.693593663, 5.5787351743), (3.8626348501, 5.102744056))
                CenterArc((1.8593394891, 6.3340213754), 0.77325864, 90, 167.6227680735)
                Line((3.7866864431, 7.1072800154), (1.8593394891, 7.1072800154))
                Line((4.5776319178, 7.4159416641), (3.7866864431, 7.1072800154))
                Line((4.2275718626, 8.8618418921), (4.5776319178, 7.4159416641))
                Line((0.228856658, 9.3881463738), (4.2275718626, 8.8618418921))
                Line((-1.673353671, 8.6458203918), (0.228856658, 9.3881463738))
                Line((-1.3842894897, 0), (-1.673353671, 8.6458203918))
                Line((1.1932312812, -0.2156641975), (-1.3842894897, 0))
                Line((1.3053314017, 2.4237808768), (1.1932312812, -0.2156641975))
            make_face()
        # Symmetric extrude, each_side=2
        extrude(amount=2, both=True, mode=Mode.ADD)
    return part.part


def model_54742_df860110_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 100.6391300846, perimeter: 39.5196791593
            with BuildLine():
                Line((4.406874178, 0), (1.5763043033, 5.0356417296))
                Line((-1.5763043033, 5.0356417296), (1.5763043033, 5.0356417296))
                Line((-4.406874178, 0), (-1.5763043033, 5.0356417296))
                Line((-4.406874178, -8), (-4.406874178, 0))
                Line((4.406874178, -8), (-4.406874178, -8))
                Line((4.406874178, -8), (4.406874178, 0))
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2)
    return part.part


def model_54762_e14d0186_0000():
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
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 2.9313206035, perimeter: 63.9991407731
            with BuildLine():
                _nurbs_edge([(3.8000000566, 0), (4.07993041, 0.0756969842), (4.6394947828, 0.2204989812), (5.4779523712, 0.4179267589), (6.59408836, 0.6409566583), (7.9860407342, 0.8481680246), (9.3744851262, 0.9773440686), (10.7591308236, 1.0220178718), (12.1398111049, 0.9784807022), (13.5166727653, 0.8499980313), (14.8899997734, 0.6428867599), (15.9860635268, 0.4194083093), (16.8067426114, 0.2213519648), (17.3532635885, 0.076002668), (17.6263744701, 0)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1, 1, 1, 1, 1], 5)
                _nurbs_edge([(17.6263744701, 0), (17.6303852627, 0.0060819759), (17.6375136761, 0.01805097), (17.6455266995, 0.0354195696), (17.6507640682, 0.0573888274), (17.6476815144, 0.0827485633), (17.6343269563, 0.1058661683), (17.6102483432, 0.1266429705), (17.5757896725, 0.1451540565), (17.531831488, 0.1615916276), (17.479336204, 0.1761657557), (17.4311734934, 0.1864790636), (17.3918221324, 0.19350916), (17.3641761808, 0.1978877484), (17.3500002585, 0.200000003)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1, 1, 1, 1, 1], 5)
                _nurbs_edge([(17.3500002585, 0.200000003), (17.2703652456, 0.2180835309), (17.1129216505, 0.2536775875), (16.8822356618, 0.3053496459), (16.5856267628, 0.3708033464), (16.2328898604, 0.4469204473), (15.8972210315, 0.5175004397), (15.5766237175, 0.5828968451), (15.2675879417, 0.6437509212), (14.9649684007, 0.700997697), (14.6630417531, 0.7555615756), (14.3563317988, 0.8081169724), (14.0405880013, 0.8587967436), (13.7135238721, 0.9069954761), (13.3742757828, 0.951693544), (13.0229996768, 0.9917341673), (12.6604405184, 1.0260929701), (12.2874733225, 1.0542138383), (11.9049430947, 1.0759357969), (11.5136204509, 1.0912809162), (11.1141124385, 1.1002816919), (10.7068080962, 1.1028119551), (10.2917688932, 1.0983681411), (9.8688816829, 1.0861603708), (9.4381027224, 1.0653178761), (8.9996782712, 1.0350604618), (8.5543652599, 0.9948776068), (8.1036836481, 0.9447250462), (7.6500750309, 0.8851619975), (7.1965461224, 0.8171536973), (6.7463852843, 0.7419216699), (6.3028445794, 0.6607743453), (5.8688553195, 0.5749563435), (5.4466819659, 0.485469607), (5.0377452468, 0.3929736371), (4.642858178, 0.2978760821), (4.3384736816, 0.2198835821), (4.1167049141, 0.1603467054), (3.9717527298, 0.1201926945), (3.9000000581, 0.1000000015)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0285714286, 0.0571428571, 0.0857142857, 0.1142857143, 0.1428571429, 0.1714285714, 0.2, 0.2285714286, 0.2571428571, 0.2857142857, 0.3142857143, 0.3428571429, 0.3714285714, 0.4, 0.4285714286, 0.4571428571, 0.4857142857, 0.5142857143, 0.5428571429, 0.5714285714, 0.6, 0.6285714286, 0.6571428571, 0.6857142857, 0.7142857143, 0.7428571429, 0.7714285714, 0.8, 0.8285714286, 0.8571428571, 0.8857142857, 0.9142857143, 0.9428571429, 0.9714285714, 1, 1, 1, 1, 1, 1], 5)
                _nurbs_edge([(3.9000000581, 0.1000000015), (3.8636442873, 0.0896984472), (3.7906098128, 0.06947652), (3.6800893073, 0.0402871684), (3.5307591293, 0.0036927844), (3.3405952517, -0.0379175232), (3.1466336396, -0.0750450835), (2.9485896123, -0.1073538669), (2.7463548466, -0.1347160114), (2.5401462033, -0.1573874939), (2.3302854684, -0.1757481424), (2.1597256866, -0.1872836533), (2.0304004443, -0.1942763817), (1.9435692357, -0.1982130019), (1.9000000283, -0.200000003)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1, 1, 1, 1, 1], 5)
                _nurbs_edge([(-0.1000000015, 0.1000000015), (-0.0636442307, 0.0896984472), (0.0093902438, 0.06947652), (0.1199107493, 0.0402871684), (0.2692409273, 0.0036927844), (0.4594048049, -0.0379175232), (0.653366417, -0.0750450835), (0.8514104443, -0.1073538669), (1.05364521, -0.1347160114), (1.2598538534, -0.1573874939), (1.4697145882, -0.1757481424), (1.64027437, -0.1872836533), (1.7695996123, -0.1942763817), (1.856430821, -0.1982130019), (1.9000000283, -0.200000003)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1, 1, 1, 1, 1], 5)
                _nurbs_edge([(-13.5500002019, 0.200000003), (-13.470365189, 0.2180835309), (-13.3129215939, 0.2536775875), (-13.0822356052, 0.3053496459), (-12.7856267062, 0.3708033464), (-12.4328898038, 0.4469204473), (-12.0972209748, 0.5175004397), (-11.7766236609, 0.5828968451), (-11.4675878851, 0.6437509212), (-11.1649683441, 0.700997697), (-10.8630416965, 0.7555615756), (-10.5563317422, 0.8081169724), (-10.2405879447, 0.8587967436), (-9.9135238155, 0.9069954761), (-9.5742757262, 0.951693544), (-9.2229996201, 0.9917341673), (-8.8604404617, 1.0260929701), (-8.4874732659, 1.0542138383), (-8.1049430381, 1.0759357969), (-7.7136203943, 1.0912809162), (-7.3141123819, 1.1002816919), (-6.9068080396, 1.1028119551), (-6.4917688366, 1.0983681411), (-6.0688816263, 1.0861603708), (-5.6381026658, 1.0653178761), (-5.1996782146, 1.0350604618), (-4.7543652032, 0.9948776068), (-4.3036835915, 0.9447250462), (-3.8500749743, 0.8851619975), (-3.3965460657, 0.8171536973), (-2.9463852277, 0.7419216699), (-2.5028445228, 0.6607743453), (-2.0688552629, 0.5749563435), (-1.6466819092, 0.485469607), (-1.2377451901, 0.3929736371), (-0.8428581214, 0.2978760821), (-0.538473625, 0.2198835821), (-0.3167048575, 0.1603467054), (-0.1717526731, 0.1201926945), (-0.1000000015, 0.1000000015)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0285714286, 0.0571428571, 0.0857142857, 0.1142857143, 0.1428571429, 0.1714285714, 0.2, 0.2285714286, 0.2571428571, 0.2857142857, 0.3142857143, 0.3428571429, 0.3714285714, 0.4, 0.4285714286, 0.4571428571, 0.4857142857, 0.5142857143, 0.5428571429, 0.5714285714, 0.6, 0.6285714286, 0.6571428571, 0.6857142857, 0.7142857143, 0.7428571429, 0.7714285714, 0.8, 0.8285714286, 0.8571428571, 0.8857142857, 0.9142857143, 0.9428571429, 0.9714285714, 1, 1, 1, 1, 1, 1], 5)
                _nurbs_edge([(-13.8263744134, 0), (-13.830385206, 0.0060819759), (-13.8375136195, 0.01805097), (-13.8455266429, 0.0354195696), (-13.8507640116, 0.0573888274), (-13.8476814577, 0.0827485633), (-13.8343268997, 0.1058661683), (-13.8102482866, 0.1266429705), (-13.7757896159, 0.1451540565), (-13.7318314314, 0.1615916276), (-13.6793361474, 0.1761657557), (-13.6311734368, 0.1864790636), (-13.5918220758, 0.19350916), (-13.5641761241, 0.1978877484), (-13.5500002019, 0.200000003)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1, 1, 1, 1, 1], 5)
                _nurbs_edge([(0, 0), (-0.2799303534, 0.0756969842), (-0.8394947261, 0.2204989812), (-1.6779523146, 0.4179267589), (-2.7940883033, 0.6409566583), (-4.1860406776, 0.8481680246), (-5.5744850696, 0.9773440686), (-6.959130767, 1.0220178718), (-8.3398110483, 0.9784807022), (-9.7166727087, 0.8499980313), (-11.0899997168, 0.6428867599), (-12.1860634701, 0.4194083093), (-13.0067425548, 0.2213519648), (-13.5532635319, 0.076002668), (-13.8263744134, 0)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1, 1, 1, 1, 1], 5)
                _nurbs_edge([(0, 0), (0.0278799514, -0.0088348142), (0.0845677314, -0.0261528398), (0.1723831446, -0.0510750279), (0.2951284829, -0.0821605671), (0.4585874599, -0.117217821), (0.6328108305, -0.1481960978), (0.8184172871, -0.174860955), (1.0152929533, -0.197255544), (1.2226018949, -0.2156966274), (1.4393672392, -0.2305543738), (1.6196397058, -0.2398410225), (1.7584432169, -0.2454421704), (1.8525521907, -0.2485800948), (1.9000000283, -0.2500000037)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1, 1, 1, 1, 1], 5)
                _nurbs_edge([(3.8000000566, 0), (3.7721201053, -0.0088348142), (3.7154323252, -0.0261528398), (3.627616912, -0.0510750279), (3.5048715737, -0.0821605671), (3.3414125968, -0.117217821), (3.1671892261, -0.1481960978), (2.9815827696, -0.174860955), (2.7847071033, -0.197255544), (2.5773981617, -0.2156966274), (2.3606328174, -0.2305543738), (2.1803603508, -0.2398410225), (2.0415568397, -0.2454421704), (1.9474478659, -0.2485800948), (1.9000000283, -0.2500000037)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1, 1, 1, 1, 1], 5)
            make_face()
        # OneSide extrude, distance=30
        extrude(amount=30)
    return part.part


def model_54958_9a4ff7d7_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 14.1371669412, perimeter: 13.3286488145
            with Locations((2.5, -2.5)):
                Circle(2.1213203436)
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 10.2101761242, perimeter: 11.3271733991
            with Locations((-2.5, 2.5)):
                Circle(1.8027756377)
        # OneSide extrude, distance=-0.8
        extrude(amount=-0.8, mode=Mode.SUBTRACT)
    return part.part


def model_54975_feb7a663_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch3 -> Extrude2 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 7 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 8, perimeter: 18
            with BuildLine():
                Line((-3, 5), (-4, 5))
                Line((-4, 5), (-4, 0))
                Line((-4, 0), (0, 0))
                Line((0, 0), (0, 1))
                Line((0, 1), (-3, 1))
                Line((-3, 1), (-3, 5))
            make_face()
        # OneSide extrude, distance=5.5
        extrude(amount=5.5)

        # Sketch6 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 18 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 3), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 1.25, perimeter: 6
            with BuildLine():
                Line((-4.5, 4), (-4, 4))
                Line((-4.5, 1.5), (-4.5, 4))
                Line((-4, 1.5), (-4.5, 1.5))
                Line((-4, 4), (-4, 1.5))
            make_face()
            # Profile area: 0.0981747704, perimeter: 1.2853981634
            with BuildLine():
                CenterArc((-4.25, 1.5), 0.25, 180, 180)
                Line((-4, 1.5), (-4.5, 1.5))
            make_face()
            # Profile area: 0.0981747704, perimeter: 1.2853981634
            with BuildLine():
                CenterArc((-4.25, 4), 0.25, 0, 180)
                Line((-4.5, 4), (-4, 4))
            make_face()
            # Profile area: 0.0981747704, perimeter: 1.2853981634
            with BuildLine():
                CenterArc((-2.75, 1.5), 0.25, 180, 180)
                Line((-2.5, 1.5), (-3, 1.5))
            make_face()
            # Profile area: 1.25, perimeter: 6
            with BuildLine():
                Line((-2.5, 1.5), (-3, 1.5))
                Line((-2.5, 4), (-2.5, 1.5))
                Line((-3, 4), (-2.5, 4))
                Line((-3, 1.5), (-3, 4))
            make_face()
            # Profile area: 0.0981747704, perimeter: 1.2853981634
            with BuildLine():
                CenterArc((-2.75, 4), 0.25, 0, 180)
                Line((-3, 4), (-2.5, 4))
            make_face()
            # Profile area: 0.0981747704, perimeter: 1.2853981634
            with BuildLine():
                CenterArc((-1.25, 4), 0.25, 0, 180)
                Line((-1.5, 4), (-1, 4))
            make_face()
            # Profile area: 1.25, perimeter: 6
            with BuildLine():
                Line((-1.5, 4), (-1, 4))
                Line((-1.5, 1.5), (-1.5, 4))
                Line((-1, 1.5), (-1.5, 1.5))
                Line((-1, 4), (-1, 1.5))
            make_face()
            # Profile area: 0.0981747704, perimeter: 1.2853981634
            with BuildLine():
                CenterArc((-1.25, 1.5), 0.25, 180, 180)
                Line((-1, 1.5), (-1.5, 1.5))
            make_face()
        # OneSide extrude, distance=-1.5
        extrude(amount=-1.5, mode=Mode.SUBTRACT)
    return part.part


def model_55031_57f7bdba_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 78.5398163397, perimeter: 31.4159265359
            with Locations((-2.5, 2.5)):
                Circle(5)
        # OneSide extrude, distance=5
        extrude(amount=5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(5, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 19.6349540849, perimeter: 15.7079632679
            with Locations((-2.5, 2.5)):
                Circle(2.5)
        # OneSide extrude, distance=6
        extrude(amount=6, mode=Mode.ADD)
    return part.part


def model_55048_18943959_0000():
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
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0799727426, perimeter: 1.0024804846
            with Locations((0.0105288116, -0.0449944158)):
                Circle(0.1595497245)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)
    return part.part


def model_55065_df019eea_0000():
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
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 0.0829982894, perimeter: 1.0212674798
            with Locations((0.0049999999, -0.0499999989)):
                Circle(0.1625397676)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)
    return part.part


def model_55087_d1c6a5b5_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 25, perimeter: 20
            with BuildLine():
                Line((5, -5), (0, -5))
                Line((5, 0), (5, -5))
                Line((0, 0), (5, 0))
                Line((0, -5), (0, 0))
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2)

        # Sketch7 -> Extrude3 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 25, perimeter: 20
            with BuildLine():
                Line((-5, -10), (-5, -5))
                Line((-5, -5), (-10, -5))
                Line((-10, -5), (-10, -10))
                Line((-10, -10), (-5, -10))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


def model_55110_ccc772b9_0008():
    """Model: lever clamp"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(1.5, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.0000000298, perimeter: 5.0000000745
            with BuildLine():
                Line((4.5000000671, 3.0000000447), (4.0000000596, 3.0000000447))
                Line((4.5000000671, 5.0000000745), (4.5000000671, 3.0000000447))
                Line((4.0000000596, 5.0000000745), (4.5000000671, 5.0000000745))
                Line((4.0000000596, 3.0000000447), (4.0000000596, 5.0000000745))
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(1.7, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0706858368, perimeter: 0.9424778101
            with Locations((4.2500000633, 4.7500000708)):
                Circle(0.1500000022)
        # OneSide extrude, distance=-0.3
        extrude(amount=-0.3, mode=Mode.SUBTRACT)
    return part.part


def model_55124_a3f4d43f_0007():
    """Model: Handle"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
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
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 1.7671458676, perimeter: 14.1371669412
            with BuildLine():
                CenterArc((0, 0), 1.25, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            Circle(1)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)
    return part.part


def model_55124_a3f4d43f_0011():
    """Model: Terminal"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((-2, -3)):
                Circle(0.5)
        # OneSide extrude, distance=3
        extrude(amount=3)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.9817477042, perimeter: 7.853981634
            with BuildLine():
                CenterArc((2, -3), 0.75, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((2, -3), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((2, -3)):
                Circle(0.5)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)
    return part.part


def model_55210_474c3ef7_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 20.25, perimeter: 18
            with BuildLine():
                Line((0.5, 6.5), (0.5, 2))
                Line((0.5, 2), (5, 2))
                Line((5, 2), (5, 6.5))
                Line((5, 6.5), (0.5, 6.5))
            make_face()
        # OneSide extrude, distance=6
        extrude(amount=6)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 6.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.926990817, perimeter: 7.024814731
            with Locations((-2.5, 3)):
                Circle(1.1180339887)
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.SUBTRACT)
    return part.part


def model_55230_077b4106_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 10.2101761242, perimeter: 20.3534635455
            with BuildLine():
                CenterArc((-6, 2), 2.1213203436, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-6, 2), 1.1180339887, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=2
        extrude(amount=2)

        # Sketch3 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 3.7455129428, perimeter: 20.2817314897
            with BuildLine():
                CenterArc((6, 2), 1.7986431305, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((6, 2), 1.4292946905, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=5.5
        extrude(amount=5.5, mode=Mode.ADD)
    return part.part


def model_55247_13a4b5ed_0001():
    """Model: screw2 v1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.1309733553, perimeter: 3.7699111843
            Circle(0.6)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.3), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            Circle(0.4)
        # OneSide extrude, distance=1.5
        extrude(amount=1.5, mode=Mode.ADD)
    return part.part


def model_55281_7d5cf788_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.7671458676, perimeter: 4.7123889804
            Circle(0.75)
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch3 -> Extrude2 (Join)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.7671458676, perimeter: 4.7123889804
            Circle(0.75)
        # OneSide extrude, distance=-0.1
        extrude(amount=-0.1, mode=Mode.ADD)
    return part.part


def model_55333_c8841f88_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 36 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 75, perimeter: 40
            with BuildLine():
                Line((5, -7.5), (5, 7.5))
                Line((5, 7.5), (0, 7.5))
                Line((0, 7.5), (0, -7.5))
                Line((0, -7.5), (5, -7.5))
            make_face()
            # Profile area: 34.406118504, perimeter: 38.879301744
            with BuildLine():
                Line((0, 7.5), (0, -7.5))
                Line((0, 7.5), (-2.5, 7.5))
                Line((-2.5, 7.5), (-2.5, 0.525868337))
                Line((-1.2099274755, 0.7120713852), (-2.5, 0.525868337))
                CenterArc((-1, 0), 0.7423713373, 90, 16.426170658)
                CenterArc((-1, 0), 0.7423713373, -90, 180)
                Line((-1, -0.7423713373), (-2.5, -0.9588743377))
                Line((-2.5, -0.9588743377), (-2.5, -7.5))
                Line((-2.5, -7.5), (0, -7.5))
            make_face()
            # Profile area: 16.7506072545, perimeter: 31.4960652732
            with BuildLine():
                CenterArc((-21.1375299127, -2.9153668784), 1.4590146403, -171.4394130664, 61.1614218743)
                Line((-22.5802896865, -3.1325487284), (-28.9709043969, -9.9688751319))
                CenterArc((-29.2236527649, -11.2407449508), 1.2967399792, 78.760498829, 135.1830881907)
                CenterArc((-29.2236527649, -11.2407449508), 1.2967399792, -146.0564129802, 126.7281371604)
                CenterArc((-29.2236527649, -11.2407449508), 1.2967399792, -19.3282758198, 31.0195487401)
                Line((-27.9538153591, -10.9779759715), (-27.9255103021, -11.0044356083))
                Line((-27.9255103021, -11.0044356083), (-21.6431884345, -4.2839549026))
            make_face()
            with BuildLine():
                CenterArc((-29.2236527649, -11.2407449508), 0.75, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 30.8421717572, perimeter: 48.5556786138
            with BuildLine():
                Line((-2.5, 0.525868337), (-20, -2))
                Line((-19.9996812185, -2.0021176956), (-20, -2))
                CenterArc((-21.1375299127, -2.9153668784), 1.4590146403, 38.7508899155, 149.8096970181)
                CenterArc((-21.1375299127, -2.9153668784), 1.4590146403, -171.4394130664, 61.1614218743)
                CenterArc((-21.1375299127, -2.9153668784), 1.4590146403, -110.2779911921, 88.6482751438)
                Line((-2.5, -0.9588743377), (-19.7812511527, -3.4531694869))
                Line((-2.5, 0.525868337), (-2.5, -0.9588743377))
            make_face()
            with BuildLine():
                CenterArc((-21.1375299127, -2.9153668784), 0.6839566574, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 350, perimeter: 150
            with BuildLine():
                Line((0, -7.5), (5, -7.5))
                Line((-2.5, -7.5), (0, -7.5))
                Line((-10, -7.5), (-2.5, -7.5))
                Line((-10, -12.5), (-10, -7.5))
                Line((17.5, -12.5), (-10, -12.5))
                Line((17.5, 12.5), (17.5, -12.5))
                Line((-10, 12.5), (17.5, 12.5))
                Line((-10, 12.5), (-10, 7.5))
                Line((-2.5, 7.5), (-10, 7.5))
                Line((0, 7.5), (-2.5, 7.5))
                Line((5, 7.5), (0, 7.5))
                Line((12.5, 7.5), (5, 7.5))
                Line((12.5, -7.5), (12.5, 7.5))
                Line((5, -7.5), (12.5, -7.5))
            make_face()
            # Profile area: 16.6832753721, perimeter: 21.9339932482
            with BuildLine():
                CenterArc((-29.2236527649, -11.2407449508), 1.2967399792, -146.0564129802, 126.7281371604)
                Line((-30.2994123636, -11.9648139114), (-30.2994123636, -13.5))
                Line((-30.2994123636, -13.5), (-32.5, -13.5))
                Line((-32.5, -13.5), (-32.5, -15.5))
                Line((-32.5, -15.5), (-25.5, -15.5))
                Line((-25.5, -15.5), (-25.5, -13.5))
                Line((-25.5, -13.5), (-28, -13.5))
                Line((-28, -13.5), (-28, -11.66994011))
            make_face()
            # Profile area: 1.7303017233, perimeter: 4.6637285561
            with BuildLine():
                CenterArc((-1, 0), 0.7423713373, 106.426170658, 163.573829342)
                CenterArc((-1, 0), 0.7423713373, -90, 180)
                Line((-1, 0.7423713373), (-1.2099274755, 0.7120713852))
            make_face()
            # Profile area: 1.3625020245, perimeter: 6.4231250854
            with BuildLine():
                Line((-2.5, 0.525868337), (-2.5, -0.9588743377))
                Line((-1, -0.7423713373), (-2.5, -0.9588743377))
                CenterArc((-1, 0), 0.7423713373, 106.426170658, 163.573829342)
                Line((-1.2099274755, 0.7120713852), (-2.5, 0.525868337))
            make_face()
            # Profile area: 1.7671458676, perimeter: 4.7123889804
            with Locations((-29.2236527649, -11.2407449508)):
                Circle(0.75)
            # Profile area: 1.4696267049, perimeter: 4.2974264204
            with Locations((-21.1375299127, -2.9153668784)):
                Circle(0.6839566574)
        # TwoSides extrude (symmetric), distance=2.5
        extrude(amount=2.5, both=True)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(2.5, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 2.3506661558, perimeter: 5.4350107732
            with Locations((-21.1375299127, -2.9153668784)):
                Circle(0.8650088303)
            # Profile area: 2.0144560858, perimeter: 5.0313419442
            with Locations((-29.2236527649, -11.2407449508)):
                Circle(0.8007629408)
        # OneSide extrude, distance=-15
        extrude(amount=-15, mode=Mode.SUBTRACT)
    return part.part


def model_55365_029f1d33_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 109.8360834229, perimeter: 46.9752314065
            with BuildLine():
                CenterArc((0, 0), 6.0763402812, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=2.5
        extrude(amount=2.5)

        # Sketch3 -> Extrude2 (Join)
        # Sketch on XY construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 6.157521601, perimeter: 8.7964594301
            Circle(1.4)
        # Symmetric extrude, each_side=6
        extrude(amount=6, both=True, mode=Mode.ADD)
    return part.part


def model_55370_47aea996_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 28.2743338823, perimeter: 18.8495559215
            Circle(3)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch3 -> Extrude2 (Join)
        # Sketch on XY construction plane
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.4877528463, perimeter: 3.0677887216
            with BuildLine():
                CenterArc((0, 0), 3, 80.760098179, 14.568136603)
                Line((0.2456896265, 3.9324307442), (0.4817058254, 2.9610740446))
                Line((0, 4), (0.2456896265, 3.9324307442))
                Line((-0.2785837779, 2.987037174), (0, 4))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)
    return part.part


def model_55371_c557ad25_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 65.224687654, perimeter: 46.9461153478
            with BuildLine():
                Line((-13.7635061444, 3.0792505292), (6.4889736956, 3.0792505292))
                Line((-13.7635061444, -0.1413273047), (-13.7635061444, 3.0792505292))
                Line((6.4889736956, -0.1413273047), (-13.7635061444, -0.1413273047))
                Line((6.4889736956, 3.0792505292), (6.4889736956, -0.1413273047))
            make_face()
        # OneSide extrude, distance=10
        extrude(amount=10)

        # Sketch3 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 32 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 3.0792505292, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.8527137039, perimeter: 5.3938610413
            with BuildLine():
                Line((-1, 9.668862437), (-1, 12))
                Line((-1, 12), (-1.3657929577, 12))
                Line((-1.3657929577, 12), (-1.3657929577, 9.668862437))
                Line((-1.3657929577, 9.668862437), (-1, 9.668862437))
            make_face()
            # Profile area: 0.667916488, perimeter: 5.177490053
            with BuildLine():
                Line((-2, 9.7018926039), (-2, 12))
                Line((-2, 12), (-2.2906376304, 12))
                Line((-2.2906376304, 12), (-2.2906376304, 9.7018926039))
                Line((-2.2906376304, 9.7018926039), (-2, 9.7018926039))
            make_face()
            # Profile area: 0.7371584382, perimeter: 5.1810447934
            with BuildLine():
                Line((-7.6745548325, 9.7349227708), (-8, 9.7349227708))
                Line((-7.6745548325, 12), (-7.6745548325, 9.7349227708))
                Line((-8, 12), (-7.6745548325, 12))
                Line((-8, 9.7349227708), (-8, 12))
            make_face()
            # Profile area: 0.7467093835, perimeter: 5.1331744466
            with BuildLine():
                Line((-8.665459839, 9.7679529377), (-9, 9.7679529377))
                Line((-8.665459839, 12), (-8.665459839, 9.7679529377))
                Line((-9, 12), (-8.665459839, 12))
                Line((-9, 9.7679529377), (-9, 12))
            make_face()
            # Profile area: 1.1757634988, perimeter: 6.7004821889
            with BuildLine():
                Line((-9, -2.0480610048), (-9, -5))
                Line((-9, -5), (-8.6016979007, -5))
                Line((-8.6016979007, -5), (-8.6016979007, -2.0480610048))
                Line((-8.6016979007, -2.0480610048), (-9, -2.0480610048))
            make_face()
            # Profile area: 1.0824560413, perimeter: 6.7023104849
            with BuildLine():
                Line((-8, -2.0109901105), (-8, -5))
                Line((-8, -5), (-7.6378546471, -5))
                Line((-7.6378546471, -5), (-7.6378546471, -2.0109901105))
                Line((-7.6378546471, -2.0109901105), (-8, -2.0109901105))
            make_face()
            # Profile area: 0.872755305, perimeter: 6.58183687
            with BuildLine():
                Line((-1.290918435, -2), (-1, -2))
                Line((-1.290918435, -5), (-1.290918435, -2))
                Line((-1, -5), (-1.290918435, -5))
                Line((-1, -2), (-1, -5))
            make_face()
            # Profile area: 0.9738577442, perimeter: 6.6492384961
            with BuildLine():
                Line((-2.0297746511, -2), (-1.705155403, -2))
                Line((-2.0297746511, -5), (-2.0297746511, -2))
                Line((-1.705155403, -5), (-2.0297746511, -5))
                Line((-1.705155403, -2), (-1.705155403, -5))
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2, mode=Mode.ADD)
    return part.part


def model_55372_b32c3159_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 100, perimeter: 50
            with BuildLine():
                Line((10, -2), (-10, -2))
                Line((10, 3), (10, -2))
                Line((-10, 3), (10, 3))
                Line((-10, -2), (-10, 3))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch13 -> Extrude10 (Cut)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.6914006222, perimeter: 5.1801948029
            with BuildLine():
                CenterArc((4.5, 0.1091746717), 0.5117803327, -12.3171778297, 204.6343556593)
                CenterArc((3.7500002123, -0.25), 0.3535532404, -45.0000243325, 90.0000486651)
                CenterArc((4.5, -0.7401863579), 0.5546976532, 154.3416405241, 231.3167189519)
                CenterArc((5.2429944305, -0.25), 0.3486348997, 134.1858679835, 91.628264033)
            make_face()
            # Profile area: 1.808172582, perimeter: 5.3811371209
            with BuildLine():
                CenterArc((-4.5, 0.1456768073), 0.5207895277, -16.2436729821, 212.4873459643)
                CenterArc((-5.2625002647, -0.25), 0.3625001917, -43.602790121, 87.2055802421)
                CenterArc((-4.5, -0.7695612225), 0.5680345524, 151.6698966011, 236.6602067978)
                CenterArc((-3.7375002215, -0.25), 0.3624998396, 136.3971568861, 87.2056862278)
            make_face()
        # OneSide extrude, distance=-0.3
        extrude(amount=-0.3, mode=Mode.SUBTRACT)
    return part.part


def model_55387_2c3bab51_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 84.7008573921, perimeter: 37.0457593393
            with BuildLine():
                Line((5.7253846134, -5.2974950562), (-2.5, -5.2974950562))
                Line((5.7253846134, 5), (5.7253846134, -5.2974950562))
                Line((-2.5, 5), (5.7253846134, 5))
                Line((-2.5, -5.2974950562), (-2.5, 5))
            make_face()
        # OneSide extrude, distance=4
        extrude(amount=4)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 0, 4), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 7.853981634, perimeter: 9.9345882658
            with Locations((1, 2.5)):
                Circle(1.5811388301)
            # Profile area: 7.853981634, perimeter: 9.9345882658
            with Locations((1, -2.5)):
                Circle(1.5811388301)
        # OneSide extrude, distance=5
        extrude(amount=5, mode=Mode.ADD)
    return part.part


def model_55401_aba9dece_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 76.1836218496, perimeter: 30.9410993164
            Circle(4.9244289009)
        # OneSide extrude, distance=50
        extrude(amount=50)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 50, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 19.6349540849, perimeter: 15.7079632679
            Circle(2.5)
        # OneSide extrude, distance=20
        extrude(amount=20, mode=Mode.ADD)
    return part.part


def model_55460_998dd656_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 15, perimeter: 16
            with BuildLine():
                Line((0, -2.5), (0, 2.5))
                Line((0, 2.5), (-3, 2.5))
                Line((-3, 2.5), (-3, -2.5))
                Line((-3, -2.5), (0, -2.5))
            make_face()
        # OneSide extrude, distance=5
        extrude(amount=5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            with Locations((-2.5, 1.5)):
                Circle(1)
        # OneSide extrude, distance=4
        extrude(amount=4, mode=Mode.ADD)
    return part.part


def model_55533_a261f37b_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 20.4598560896, perimeter: 26.700038812
            with BuildLine():
                CenterArc((-16.2500710639, 5.4374866755), 19.7549158849, -1.268959563, 23.7772296783)
                Line((3.5, 5), (4.5999999642, 5))
                CenterArc((-30.9331169639, 12.1865189583), 36.2525647833, -11.4337523252, 19.0457409992)
                CenterArc((0.8333333333, 17), 4.1666666667, -73.7397952917, 73.5840119175)
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 5, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.0182190355, perimeter: 1.0154959622
            with BuildLine():
                Line((3.5, 0.5), (3.5, 0))
                CenterArc((4.0499999821, 0.25), 0.6041522824, 155.5560445179, 48.8879109643)
            make_face()
            # Profile area: 0.0182190355, perimeter: 1.0154959622
            with BuildLine():
                CenterArc((4.0499999821, 0.25), 0.6041522824, -24.4439554821, 48.8879109643)
                Line((4.5999999642, 0), (4.5999999642, 0.5))
            make_face()
            # Profile area: 0.2801216018, perimeter: 2.4825043741
            with BuildLine():
                CenterArc((4.0499999821, 0.25), 0.6041522824, 24.4439554821, 131.1120890357)
                Line((4.5999999642, 0.5), (3.5, 0.5))
            make_face()
            # Profile area: 0.2801216018, perimeter: 2.4825043741
            with BuildLine():
                Line((3.5, 0), (4.5999999642, 0))
                CenterArc((4.0499999821, 0.25), 0.6041522824, -155.5560445179, 131.1120890357)
            make_face()
            # Profile area: 0.5499999821, perimeter: 3.1999999285
            with BuildLine():
                Line((4.5999999642, 0), (4.5999999642, 0.5))
                Line((4.5999999642, 0.5), (3.5, 0.5))
                Line((3.5, 0.5), (3.5, 0))
                Line((3.5, 0), (4.5999999642, 0))
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)
    return part.part


def model_55538_1ca911e8_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 75, perimeter: 35
            with BuildLine():
                Line((0, 7.5), (0, 0))
                Line((0, 0), (10, 0))
                Line((10, 0), (10, 7.5))
                Line((10, 7.5), (0, 7.5))
            make_face()
        # OneSide extrude, distance=10
        extrude(amount=10)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 7.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 19.6349540849, perimeter: 15.7079632679
            with Locations((-5, 5)):
                Circle(2.5)
        # OneSide extrude, distance=15
        extrude(amount=15, mode=Mode.ADD)
    return part.part


def model_55554_81f133cf_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 12.5663706144, perimeter: 12.5663706144
            with Locations((5, 3.7828513702)):
                Circle(2)
        # OneSide extrude, distance=20.5
        extrude(amount=20.5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XY construction plane
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 75, perimeter: 35
            with BuildLine():
                Line((0, 7.5), (0, 0))
                Line((0, 0), (10, 0))
                Line((10, 0), (10, 7.5))
                Line((10, 7.5), (0, 7.5))
            make_face()
        # OneSide extrude, distance=-12
        extrude(amount=-12, mode=Mode.ADD)
    return part.part


def model_55605_2f8bc12e_0047():
    """Model: Bolt M10X1.5in v1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            Circle(0.5)
        # OneSide extrude, distance=4
        extrude(amount=4)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 4, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.4316268703, perimeter: 8.6841552378
            with BuildLine():
                Line((-0.8, 0.4618802154), (-0.8, -0.4618802154))
                Line((-0.8, -0.4618802154), (0, -0.9237604307))
                Line((0, -0.9237604307), (0.8, -0.4618802154))
                Line((0.8, -0.4618802154), (0.8, 0.4618802154))
                Line((0.8, 0.4618802154), (0, 0.9237604307))
                Line((0, 0.9237604307), (-0.8, 0.4618802154))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            Circle(0.5)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)
    return part.part


def model_55605_2f8bc12e_0050():
    """Model: Bolt M10X60mm v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.7853981868, perimeter: 3.1415927004
            Circle(0.5000000075)
        # OneSide extrude, distance=7
        extrude(amount=7)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 7, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.431626913, perimeter: 8.6841553672
            with BuildLine():
                Line((-0.8000000119, 0.4618802222), (-0.8000000119, -0.4618802222))
                Line((-0.8000000119, -0.4618802222), (0, -0.9237604445))
                Line((0, -0.9237604445), (0.8000000119, -0.4618802222))
                Line((0.8000000119, -0.4618802222), (0.8000000119, 0.4618802222))
                Line((0.8000000119, 0.4618802222), (0, 0.9237604445))
                Line((0, 0.9237604445), (-0.8000000119, 0.4618802222))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.5000000075, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.7853981868, perimeter: 3.1415927004
            Circle(0.5000000075)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)
    return part.part


MODELS = {
    "model_51777_87ff5835_0005": {"func": model_51777_87ff5835_0005, "volume": 494.5394765077, "area": 939.1645495819},
    "model_51863_0b8751d1_0000": {"func": model_51863_0b8751d1_0000, "volume": 1650.3803638145, "area": 1238.4803508146},
    "model_51863_0b8751d1_0003": {"func": model_51863_0b8751d1_0003, "volume": 791.2196066016, "area": 735.3681720934},
    "model_51863_0b8751d1_0006": {"func": model_51863_0b8751d1_0006, "volume": 3.8208910846, "area": 22.1684522105},
    "model_51864_39932fe9_0002": {"func": model_51864_39932fe9_0002, "volume": 1337.8362852202, "area": 2178.5840605453},
    "model_51864_39932fe9_0009": {"func": model_51864_39932fe9_0009, "volume": 12.2635934158, "area": 171.7279746403},
    "model_51864_39932fe9_0010": {"func": model_51864_39932fe9_0010, "volume": 20.1803778447, "area": 283.4559132193},
    "model_51864_39932fe9_0027": {"func": model_51864_39932fe9_0027, "volume": 0.8607963871, "area": 6.3460171603},
    "model_51871_86ebf5b2_0006": {"func": model_51871_86ebf5b2_0006, "volume": 74.5709689042, "area": 801.3975217832},
    "model_51876_8346832d_0000": {"func": model_51876_8346832d_0000, "volume": 10476.5087175555, "area": 8312.6256705384},
    "model_51876_8346832d_0001": {"func": model_51876_8346832d_0001, "volume": 2613.6192394515, "area": 2461.2003038983},
    "model_51876_8346832d_0009": {"func": model_51876_8346832d_0009, "volume": 0.1158333338, "area": 1.7392509647},
    "model_51891_9455ea02_0003": {"func": model_51891_9455ea02_0003, "volume": 16.4387767306, "area": 48.420453517},
    "model_51913_1fa125b4_0012": {"func": model_51913_1fa125b4_0012, "volume": 2.1488493751, "area": 10.0530964915},
    "model_51914_fb924efa_0005": {"func": model_51914_fb924efa_0005, "volume": 1.4800000262, "area": 10.1000000402},
    "model_51916_fa226b15_0000": {"func": model_51916_fa226b15_0000, "volume": 2.2925346507, "area": 12.5410101077},
    "model_51916_fa226b15_0005": {"func": model_51916_fa226b15_0005, "volume": 6.5640172696, "area": 31.8070419555},
    "model_51916_fa226b15_0008": {"func": model_51916_fa226b15_0008, "volume": 0.4001704499, "area": 4.0833343569},
    "model_51916_fa226b15_0010": {"func": model_51916_fa226b15_0010, "volume": 1.9841284104, "area": 10.9448815485},
    "model_51916_fa226b15_0011": {"func": model_51916_fa226b15_0011, "volume": 22.2298317143, "area": 49.839747644},
    "model_51925_a4bed832_0002": {"func": model_51925_a4bed832_0002, "volume": 1.698067601, "area": 31.8873101294},
    "model_51940_aa0fca73_0003": {"func": model_51940_aa0fca73_0003, "volume": 143.6477532891, "area": 346.7847050665},
    "model_52006_d21e4570_0004": {"func": model_52006_d21e4570_0004, "volume": 2.7763924015, "area": 20.764585178},
    "model_52024_97da327b_0001": {"func": model_52024_97da327b_0001, "volume": 2.0158216964, "area": 25.2340324591},
    "model_52024_97da327b_0002": {"func": model_52024_97da327b_0002, "volume": 0.5075752288, "area": 6.2325021223},
    "model_52024_97da327b_0005": {"func": model_52024_97da327b_0005, "volume": 1.110873808, "area": 13.8331141794},
    "model_52024_97da327b_0008": {"func": model_52024_97da327b_0008, "volume": 0.8092245118, "area": 10.0328080861},
    "model_52024_97da327b_0013": {"func": model_52024_97da327b_0013, "volume": 5.923940423, "area": 45.692832749},
    "model_52230_60438ea5_0013": {"func": model_52230_60438ea5_0013, "volume": 1620, "area": 882},
    "model_52352_adac16c3_0003": {"func": model_52352_adac16c3_0003, "volume": 2228175.8540279558, "area": 375294.5158284908},
    "model_52443_085efc00_0007": {"func": model_52443_085efc00_0007, "volume": 558.2828576474, "area": 565.674109587},
    "model_52454_a591c6d0_0000": {"func": model_52454_a591c6d0_0000, "volume": 3.1413665187, "area": 108.620972532},
    "model_52557_e6a00b06_0010": {"func": model_52557_e6a00b06_0010, "volume": 47.9298994917, "area": 111.0355252112},
    "model_52651_47c9fcdd_0000": {"func": model_52651_47c9fcdd_0000, "volume": 46, "area": 123},
    "model_52659_7eb6fd4c_0000": {"func": model_52659_7eb6fd4c_0000, "volume": 93.6587309851, "area": 127.6272015521},
    "model_52884_c8150d6e_0000": {"func": model_52884_c8150d6e_0000, "volume": 0.0397800007, "area": 1.7995118944},
    "model_52884_c8150d6e_0007": {"func": model_52884_c8150d6e_0007, "volume": 4.6951701885, "area": 19.7336675481},
    "model_52884_c8150d6e_0035": {"func": model_52884_c8150d6e_0035, "volume": 48.9002055589, "area": 121.9768707161},
    "model_52886_5743bcf0_0004": {"func": model_52886_5743bcf0_0004, "volume": 2.2671849484, "area": 11.3678297313},
    "model_52886_5743bcf0_0008": {"func": model_52886_5743bcf0_0008, "volume": 2.8274646641, "area": 32.8227913941},
    "model_52985_475fe7b2_0014": {"func": model_52985_475fe7b2_0014, "volume": 517.5, "area": 1164},
    "model_52987_387431ac_0006": {"func": model_52987_387431ac_0006, "volume": 8.4446010528, "area": 33.1752184219},
    "model_52987_387431ac_0010": {"func": model_52987_387431ac_0010, "volume": 50.6322633997, "area": 132.5595020182},
    "model_53060_44095911_0000": {"func": model_53060_44095911_0000, "volume": 127296, "area": 36336},
    "model_53072_60d8a39b_0003": {"func": model_53072_60d8a39b_0003, "volume": 0.0753982237, "area": 1.5079644737},
    "model_53075_6438cc56_0007": {"func": model_53075_6438cc56_0007, "volume": 65.8998675301, "area": 672.2868162},
    "model_53119_aabd4fc1_0006": {"func": model_53119_aabd4fc1_0006, "volume": 655404.4498956776, "area": 137579.2538303259},
    "model_53119_aabd4fc1_0014": {"func": model_53119_aabd4fc1_0014, "volume": 388.7192326612, "area": 792.9276520081},
    "model_53119_aabd4fc1_0021": {"func": model_53119_aabd4fc1_0021, "volume": 46088.7860266999, "area": 27559.5456906187},
    "model_53206_824f0184_0001": {"func": model_53206_824f0184_0001, "volume": 0.3188144244, "area": 4.2808214754},
    "model_53213_13a055ca_0000": {"func": model_53213_13a055ca_0000, "volume": 32.8861708727, "area": 93.0458988739},
    "model_53216_2857e8ac_0000": {"func": model_53216_2857e8ac_0000, "volume": 0.7515457629, "area": 6.761362672},
    "model_53216_2857e8ac_0005": {"func": model_53216_2857e8ac_0005, "volume": 43.5238697497, "area": 463.3218361867},
    "model_53216_2857e8ac_0009": {"func": model_53216_2857e8ac_0009, "volume": 7.8627828234, "area": 68.1744716688},
    "model_53233_8dbca22c_0028": {"func": model_53233_8dbca22c_0028, "volume": 2882.9628730731, "area": 2351.1227030124},
    "model_53233_8dbca22c_0030": {"func": model_53233_8dbca22c_0030, "volume": 29.7627305535, "area": 103.875033215},
    "model_53470_39f2e9dc_0001": {"func": model_53470_39f2e9dc_0001, "volume": 214.005287453, "area": 339.3340555609},
    "model_53470_39f2e9dc_0004": {"func": model_53470_39f2e9dc_0004, "volume": 117.926990817, "area": 373.5619449019},
    "model_53470_39f2e9dc_0005": {"func": model_53470_39f2e9dc_0005, "volume": 555.4081716345, "area": 2377.8111602684},
    "model_53601_59d3ecd2_0000": {"func": model_53601_59d3ecd2_0000, "volume": 373.9645943005, "area": 817.929188601},
    "model_53708_7763f0a7_0000": {"func": model_53708_7763f0a7_0000, "volume": 2678.02483459, "area": 1670.1687090384},
    "model_53714_22f87ede_0000": {"func": model_53714_22f87ede_0000, "volume": 41, "area": 134},
    "model_53730_62d1957d_0013": {"func": model_53730_62d1957d_0013, "volume": 0.1112320149, "area": 1.5511613727},
    "model_53822_3d84a196_0000": {"func": model_53822_3d84a196_0000, "volume": 0.003825, "area": 0.8024999997},
    "model_53831_de0554da_0002": {"func": model_53831_de0554da_0002, "volume": 1721.5927741672, "area": 1244.0706908216},
    "model_53831_de0554da_0003": {"func": model_53831_de0554da_0003, "volume": 4175.5693357025, "area": 3537.4333279421},
    "model_53846_89405f98_0009": {"func": model_53846_89405f98_0009, "volume": 0.6078981785, "area": 4.9008845396},
    "model_53846_89405f98_0029": {"func": model_53846_89405f98_0029, "volume": 0.0472013252, "area": 1.1582742855},
    "model_53848_7c64ed9f_0003": {"func": model_53848_7c64ed9f_0003, "volume": 1880.3650459151, "area": 7575.1681469282},
    "model_53925_fa8c0add_0000": {"func": model_53925_fa8c0add_0000, "volume": 2.1454647642, "area": 44.5512668245},
    "model_53927_ef5208b9_0003": {"func": model_53927_ef5208b9_0003, "volume": 6.5607851709, "area": 24.2941550335},
    "model_54077_dd26efde_0000": {"func": model_54077_dd26efde_0000, "volume": 61.9704639131, "area": 294.8330536471},
    "model_54177_2b99e039_0005": {"func": model_54177_2b99e039_0005, "volume": 54.672000222, "area": 545.1199997996},
    "model_54177_2b99e039_0011": {"func": model_54177_2b99e039_0011, "volume": 2.7248673407, "area": 23.0026551673},
    "model_54273_21c2b38f_0009": {"func": model_54273_21c2b38f_0009, "volume": 0.3523886693, "area": 7.1702866851},
    "model_54273_21c2b38f_0028": {"func": model_54273_21c2b38f_0028, "volume": 5.4667053772, "area": 18.4314377885},
    "model_54273_21c2b38f_0055": {"func": model_54273_21c2b38f_0055, "volume": 0.1884955592, "area": 2.1362830044},
    "model_54383_13d47b0e_0007": {"func": model_54383_13d47b0e_0007, "volume": 52.5860762264, "area": 245.6134677669},
    "model_54383_13d47b0e_0009": {"func": model_54383_13d47b0e_0009, "volume": 239.3053138694, "area": 399.2167996206},
    "model_54383_13d47b0e_0013": {"func": model_54383_13d47b0e_0013, "volume": 488.696475083, "area": 1522.1800541416},
    "model_54478_21061ebc_0000": {"func": model_54478_21061ebc_0000, "volume": 49.5, "area": 128},
    "model_54485_e9658dfb_0000": {"func": model_54485_e9658dfb_0000, "volume": 61.9500018463, "area": 100.0600022295},
    "model_54494_37c2c718_0000": {"func": model_54494_37c2c718_0000, "volume": 341.9524050724, "area": 754.2886544442},
    "model_54638_8ce7a3a8_0000": {"func": model_54638_8ce7a3a8_0000, "volume": 12395.9226555376, "area": 6501.2797974299},
    "model_54650_df3655c1_0000": {"func": model_54650_df3655c1_0000, "volume": 6, "area": 33.5},
    "model_54654_f19e7f7d_0003": {"func": model_54654_f19e7f7d_0003, "volume": 2.6753419891, "area": 13.5905744468},
    "model_54659_e1303e28_0007": {"func": model_54659_e1303e28_0007, "volume": 161.5695042868, "area": 313.1753009691},
    "model_54735_cf8dcb52_0000": {"func": model_54735_cf8dcb52_0000, "volume": 91.4173734326, "area": 1349.4630124826},
    "model_54738_5424d7af_0002": {"func": model_54738_5424d7af_0002, "volume": 155.4295360962, "area": 222.1504725643},
    "model_54742_df860110_0000": {"func": model_54742_df860110_0000, "volume": 201.2782601693, "area": 280.3176184878},
    "model_54762_e14d0186_0000": {"func": model_54762_e14d0186_0000, "volume": 87.9396529519, "area": 1925.8299867231},
    "model_54958_9a4ff7d7_0000": {"func": model_54958_9a4ff7d7_0000, "volume": 5.9690260418, "area": 50.6647214161},
    "model_54975_feb7a663_0000": {"func": model_54975_feb7a663_0000, "volume": 39.6609513775, "area": 126.0342917353},
    "model_55031_57f7bdba_0000": {"func": model_55031_57f7bdba_0000, "volume": 510.5088062083, "area": 408.4070449667},
    "model_55048_18943959_0000": {"func": model_55048_18943959_0000, "volume": 0.0159945485, "area": 0.360441582},
    "model_55065_df019eea_0000": {"func": model_55065_df019eea_0000, "volume": 0.0165996579, "area": 0.3702500748},
    "model_55087_d1c6a5b5_0000": {"func": model_55087_d1c6a5b5_0000, "volume": 75, "area": 160},
    "model_55110_ccc772b9_0008": {"func": model_55110_ccc772b9_0008, "volume": 0.1858628386, "area": 3.0471239629},
    "model_55124_a3f4d43f_0007": {"func": model_55124_a3f4d43f_0007, "volume": 20.1258279371, "area": 155.116137271},
    "model_55124_a3f4d43f_0011": {"func": model_55124_a3f4d43f_0011, "volume": 2.7096236637, "area": 13.9015474921},
    "model_55210_474c3ef7_0000": {"func": model_55210_474c3ef7_0000, "volume": 117.573009183, "area": 155.524814731},
    "model_55230_077b4106_0000": {"func": model_55230_077b4106_0000, "volume": 41.0206734339, "area": 172.6768025327},
    "model_55247_13a4b5ed_0001": {"func": model_55247_13a4b5ed_0001, "volume": 1.0932742434, "area": 7.1628312502},
    "model_55281_7d5cf788_0000": {"func": model_55281_7d5cf788_0000, "volume": 1.9438604544, "area": 8.7179196137},
    "model_55333_c8841f88_0000": {"func": model_55333_c8841f88_0000, "volume": 2628.2331348331, "area": 2336.5257554102},
    "model_55365_029f1d33_0000": {"func": model_55365_029f1d33_0000, "volume": 348.4804677697, "area": 411.0005045744},
    "model_55370_47aea996_0000": {"func": model_55370_47aea996_0000, "volume": 14.3810433643, "area": 67.72005993},
    "model_55371_c557ad25_0000": {"func": model_55371_c557ad25_0000, "volume": 666.4655377455, "area": 694.9494055344},
    "model_55372_b32c3159_0000": {"func": model_55372_b32c3159_0000, "volume": 98.9501280387, "area": 253.1683995771},
    "model_55387_2c3bab51_0000": {"func": model_55387_2c3bab51_0000, "volume": 417.3432459083, "area": 416.9306347993},
    "model_55401_aba9dece_0000": {"func": model_55401_aba9dece_0000, "volume": 4201.8801741763, "area": 2013.5814748767},
    "model_55460_998dd656_0000": {"func": model_55460_998dd656_0000, "volume": 87.5663706144, "area": 135.1327412287},
    "model_55533_a261f37b_0000": {"func": model_55533_a261f37b_0000, "volume": 10.4592642961, "area": 56.2222942832},
    "model_55538_1ca911e8_0000": {"func": model_55538_1ca911e8_0000, "volume": 1044.524311274, "area": 735.6194490192},
    "model_55554_81f133cf_0000": {"func": model_55554_81f133cf_0000, "volume": 1157.6105975944, "area": 827.6105975944},
    "model_55605_2f8bc12e_0047": {"func": model_55605_2f8bc12e_0047, "volume": 4.2501051704, "area": 19.7717019738},
    "model_55605_2f8bc12e_0050": {"func": model_55605_2f8bc12e_0050, "volume": 6.6062998575, "area": 29.1964804357},
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
