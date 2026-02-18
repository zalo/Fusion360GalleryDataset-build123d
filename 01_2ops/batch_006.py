"""Batch 006 - passing/01_2ops
195 models bundled from Fusion360 Gallery reconstructions.
"""

from build123d import *
from build123d import Edge, BuildLine
from collections import Counter
from OCP.BRepBuilderAPI import BRepBuilderAPI_MakeEdge
from OCP.Geom import Geom_BSplineCurve
from OCP.TColStd import TColStd_Array1OfReal, TColStd_Array1OfInteger
from OCP.TColgp import TColgp_Array1OfPnt
from OCP.gp import gp_Pnt


def model_148051_b9c68456_0000():
    """Model: BT-50KE x 15 in v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2688417913, perimeter: 15.3623880761
            with BuildLine():
                CenterArc((0, 0), 1.24, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.205, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=38.1
        extrude(amount=38.1)
    return part.part


def model_148051_b9c68456_0002():
    """Model: BT-20G x 3.5in (18mm dia)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2017687882, perimeter: 11.5296450387
            with BuildLine():
                CenterArc((-0.008285473, -2.17424), 0.935, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-0.008285473, -2.17424), 0.9, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=8.89
        extrude(amount=8.89)
    return part.part


def model_148051_b9c68456_0003():
    """Model: Fin small"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 8 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 4.53628125, perimeter: 11.4110006523
            with BuildLine():
                Line((5.08, 0.93472), (0, 0.93472))
                Line((1.508125, 2.7206575), (5.08, 0.93472))
                Line((0, 0.93472), (1.508125, 2.7206575))
            make_face()
        # Symmetric extrude, full_length=True, total=0.238125
        extrude(amount=0.1190625, both=True)
    return part.part


def model_148051_b9c68456_0005():
    """Model: Fin medium"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 7 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 5.590021582, perimeter: 15.166177412
            with BuildLine():
                Line((0, 1.23952), (7.223125, 1.23952))
                Line((7.223125, 1.23952), (2.2225, 2.7873325))
                Line((2.2225, 2.7873325), (0, 1.23952))
            make_face()
        # Symmetric extrude, full_length=True, total=0.238125
        extrude(amount=0.1190625, both=True)
    return part.part


def model_148051_b9c68456_0007():
    """Model: Adapter ring"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.8282208529, perimeter: 13.4536820434
            with BuildLine():
                CenterArc((0, 0), 1.2065, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.93472, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.508
        extrude(amount=0.508)
    return part.part


def model_148051_b9c68456_0008():
    """Model: Engine mount tube"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1905017438, perimeter: 11.5385671618
            with BuildLine():
                CenterArc((0, 0), 0.93472, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.9017, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=6.985
        extrude(amount=6.985)
    return part.part


def model_148051_b9c68456_0010():
    """Model: Engine hook"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 19 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 0.5780329804, perimeter: 15.5642128107
            with BuildLine():
                Line((7.0107568645, 0.90972), (7.0107568645, 0.63472))
                Line((7.0107568645, 0.63472), (7.0857568645, 0.63472))
                Line((7.0857568645, 0.63472), (7.0857568645, 0.90972))
                CenterArc((6.9857568645, 0.90972), 0.1, 0, 90)
                Line((6.9857568645, 1.00972), (0.025, 1.00972))
                CenterArc((0.025, 0.90972), 0.1, 90, 90)
                Line((-0.075, 0.90972), (-0.075, 0.63472))
                Line((-0.075, 0.63472), (0, 0.63472))
                Line((0, 0.63472), (0, 0.90972))
                CenterArc((0.025, 0.90972), 0.025, 90, 90)
                Line((0.025, 0.93472), (6.9857568645, 0.93472))
                CenterArc((6.9857568645, 0.90972), 0.025, 0, 90)
            make_face()
        # Symmetric extrude, full_length=True, total=0.3175
        extrude(amount=0.15875, both=True)
    return part.part


def model_148051_b9c68456_0011():
    """Model: Split adapter ring"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 10 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.7409187301, perimeter: 13.360991886
            with BuildLine():
                Line((-0.16, -1.1958437398), (-0.16, -0.9209242523))
                CenterArc((0, 0), 0.93472, -80.1439002431, 340.2878004862)
                Line((0.16, -0.9209242523), (0.16, -1.1958437398))
                CenterArc((0, 0), 1.2065, -82.3792704623, 344.7585409246)
            make_face()
        # OneSide extrude, distance=0.508
        extrude(amount=0.508)
    return part.part


def model_148051_c59af578_0000():
    """Model: Panel brace"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 23 constraints, 9 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 6.3796987454, perimeter: 13.9439641035
            with BuildLine():
                Line((0.127, 1.825625), (0.127, 2.301875))
                Line((0.127, 2.301875), (0, 2.301875))
                Line((0, 2.301875), (0, 2.936875))
                CenterArc((0.0868985409, 2.3078490517), 0.635, 97.8654999297, 54.1345000703)
                Line((-1.825625, 0.0635), (-0.4737731805, 2.6059634941))
                Line((-1.825625, 0.0635), (-1.5875, 0.0635))
                Line((-1.5875, 0.0635), (-1.5875, 0))
                Line((-1.5875, -0.0635), (-1.5875, 0))
                Line((-1.825625, -0.0635), (-1.5875, -0.0635))
                Line((-1.825625, -0.0635), (-0.4737731805, -2.6059634941))
                CenterArc((0.0868985409, -2.3078490517), 0.635, -152, 54.1345000703)
                Line((0, -2.301875), (0, -2.936875))
                Line((0.127, -2.301875), (0, -2.301875))
                Line((0.127, -1.825625), (0.127, -2.301875))
                Line((0.127, -1.825625), (0, -1.825625))
                Line((0, 1.825625), (0, -1.825625))
                Line((0.127, 1.825625), (0, 1.825625))
            make_face()
        # OneSide extrude, distance=0.127
        extrude(amount=0.127)
    return part.part


def model_148051_c59af578_0001():
    """Model: BT-101 x 1 in"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.1109684084, perimeter: 62.2193681681
            with BuildLine():
                CenterArc((0, 0), 5.00126, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 4.90126, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=2.54
        extrude(amount=2.54)
    return part.part


def model_148051_c59af578_0002():
    """Model: Solae panel"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 22 constraints, 12 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 44.6267819556, perimeter: 29.5027524371
            with BuildLine():
                Line((-5.42875, -1.27), (-5.42875, 1.27))
                Line((-4.3175, -3.175), (-5.42875, -1.27))
                Line((1.23875, -3.175), (-4.3175, -3.175))
                Line((2.35, -1.27), (1.23875, -3.175))
                Line((2.35, 1.27), (2.35, -1.27))
                Line((1.23875, 3.175), (2.35, 1.27))
                Line((-4.3175, 3.175), (1.23875, 3.175))
                Line((-5.42875, 1.27), (-4.3175, 3.175))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.238125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-2.8575, -2.063775), 0.238125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-2.8575, 2.063775), 0.238125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.127
        extrude(amount=0.127)
    return part.part


def model_148051_c59af578_0003():
    """Model: Leg"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 31 constraints, 43 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 0.2778323313, perimeter: 2.3196997919
            with BuildLine():
                Line((-0.9525, -11.1743944941), (-0.9315679354, -11.6506444941))
                Line((-0.9315679354, -11.6506444941), (-0.5275384398, -11.860819864))
                Line((-0.5684680426, -10.929582372), (-0.5275384398, -11.860819864))
                Line((-0.5684680426, -10.929582372), (-0.9525, -11.1743944941))
            make_face()
            # Profile area: 30.3341743955, perimeter: 68.8689419619
            with BuildLine():
                Line((-0.5684680426, -10.929582372), (-0.5275384398, -11.860819864))
                Line((-0.5275384398, -11.860819864), (-0.4946063518, -12.6100965002))
                Line((-0.4946063518, -12.6100965002), (-0.3677288414, -12.60452))
                Line((-0.3677288414, -12.60452), (-0.2979552928, -14.19202))
                Line((-0.2979552928, -14.19202), (1.879548913, -12.9891480856))
                Line((1.879548913, -12.9891480856), (1.9409580544, -13.1003142556))
                Line((1.9409580544, -13.1003142556), (2.3578311919, -12.8700299753))
                Line((2.3578311919, -12.8700299753), (2.3094775372, -12.782497558))
                Line((1.898330261, -12.6869464187), (2.3094775372, -12.782497558))
                CenterArc((2.0420742663, -12.0684299186), 0.635, 167.6698060661, 89.2468292783)
                Line((2.936875, -5.00126), (1.4217217, -11.9328286889))
                Line((2.936875, -5.00126), (0.396875, -5.00126))
                Line((0.396875, -5.00126), (0.396875, -4.8723822147))
                CenterArc((1.031875, -4.8723822147), 0.635, 112, 68)
                Line((0.7939998132, -4.283620467), (5.336068, -2.4485058))
                CenterArc((5.5006480876, -2.9374893362), 0.5159375, 29, 79.601994152)
                Line((5.9518971927, -2.6873578728), (6.2211127515, -3.1730355973))
                Line((6.2211127515, -3.1730355973), (6.6675, -1.23952))
                Line((6.6675, -1.23952), (0, -1.23952))
                Line((0, -1.23952), (-0.9525, -2.19202))
                Line((-0.9525, -2.19202), (-0.5684680426, -10.929582372))
            make_face()
            with BuildLine():
                CenterArc((0.7010636359, -2.7221265), 0.9525, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((2.9510084059, -2.2847815401), 0.555625, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((4.8232455768, -1.9208555), 0.2778125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0.860447996, -7.0095813032), 1.11125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0.6322176749, -9.6680766658), 0.714375, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0.4450589013, -11.8481583), 0.4365625, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, full_length=True, total=0.127
        extrude(amount=0.0635, both=True)
    return part.part


def model_148051_c59af578_0006():
    """Model: Centering ring large hole"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.8491136803, perimeter: 10.5636052977
            with BuildLine():
                CenterArc((0, 0), 1.205, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.47625, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.127
        extrude(amount=0.127)
    return part.part


def model_148051_c59af578_0009():
    """Model: Disc #3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.5542113053, perimeter: 6.9821896726
            with BuildLine():
                CenterArc((0, 0), 0.635, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.47625, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.127
        extrude(amount=0.127)
    return part.part


def model_148051_c59af578_0011():
    """Model: Dowel n/12 in antennae"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0351880194, perimeter: 0.664970445
            Circle(0.1058333333)
        # OneSide extrude, distance=10.16
        extrude(amount=10.16)
    return part.part


def model_148051_c59af578_0013():
    """Model: Motor retainer"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 20 constraints, 9 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 0.3867809725, perimeter: 15.571238898
            with BuildLine():
                Line((0, -0.58472), (-0.05, -0.58472))
                Line((-0.05, -0.58472), (-0.05, -0.88472))
                CenterArc((0.05, -0.88472), 0.1, 180, 90)
                Line((0.05, -0.98472), (6.95, -0.98472))
                CenterArc((6.95, -0.88472), 0.1, -90, 90)
                Line((7.05, -0.88472), (7.05, -0.58472))
                Line((7.05, -0.58472), (7, -0.58472))
                Line((7, -0.58472), (7, -0.88472))
                CenterArc((6.95, -0.88472), 0.05, -90, 90)
                Line((6.95, -0.93472), (0.05, -0.93472))
                CenterArc((0.05, -0.88472), 0.05, 180, 90)
                Line((0, -0.88472), (0, -0.58472))
            make_face()
        # Symmetric extrude, full_length=True, total=0.3175
        extrude(amount=0.15875, both=True)
    return part.part


def model_148051_c59af578_0014():
    """Model: Centering ring"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 12 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.6516496737, perimeter: 12.9963647536
            with BuildLine():
                CenterArc((0, 0), 0.93472, -75.2409059989, 330.4818119977)
                Line((0.238125, -1.1761362525), (0.238125, -0.9038793961))
                CenterArc((0, 0), 1.2, -78.5543968581, 337.1087937162)
                Line((-0.238125, -0.9038793961), (-0.238125, -1.1761362525))
            make_face()
            # Profile area: 0.1274296015, perimeter: 1.5055040107
            with BuildLine():
                Line((-0.238125, -0.9038793961), (-0.238125, -1.1761362525))
                CenterArc((0, 0), 1.2, -101.4456031419, 22.8912062838)
                Line((0.238125, -1.1761362525), (0.238125, -0.9038793961))
                CenterArc((0, 0), 0.93472, -104.7590940011, 29.5181880023)
            make_face()
        # OneSide extrude, distance=0.635
        extrude(amount=0.635)
    return part.part


def model_148051_c59af578_0015():
    """Model: BT-50 x 2.75 in"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2688417913, perimeter: 15.3623880761
            with BuildLine():
                CenterArc((0, 0), 1.24, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.205, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=6.985
        extrude(amount=6.985)
    return part.part


def model_148051_c59af578_0017():
    """Model: Centering ring small hole"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.5264830534, perimeter: 8.2362087402
            with BuildLine():
                CenterArc((0, 0), 1.205, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.1058333333, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.127
        extrude(amount=0.127)
    return part.part


def model_148051_db355cb7_0004():
    """Model: Wing (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 7 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 14.7817160139, perimeter: 15.082272951
            with BuildLine():
                Line((-1.4604958159, 5.36702), (1.6352561841, 5.36702))
                Line((-2.2225, 2.7873325), (-1.4604958159, 5.36702))
                Line((0, 1.23952), (-2.2225, 2.7873325))
                Line((2.3919856033, 1.23952), (0, 1.23952))
                Line((1.6352561841, 5.36702), (2.3919856033, 1.23952))
            make_face()
        # Symmetric extrude, full_length=True, total=0.238125
        extrude(amount=0.1190625, both=True)
    return part.part


def model_148051_db355cb7_0009():
    """Model: Fin 4"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 10 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 2.4477017578, perimeter: 6.9456225397
            with BuildLine():
                Line((0.61515625, 2.35077), (0, 1.23952))
                Line((0, 1.23952), (2.8178125, 1.23952))
                Line((2.8178125, 1.23952), (2.20265625, 2.35077))
                Line((2.20265625, 2.35077), (0.61515625, 2.35077))
            make_face()
        # Symmetric extrude, full_length=True, total=0.238125
        extrude(amount=0.1190625, both=True)
    return part.part


def model_148051_db355cb7_0010():
    """Model: Strake (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 2.8351757812, perimeter: 8.658413312
            with BuildLine():
                Line((2.0281733826, 3.223895), (2.3919856033, 1.23952))
                Line((5.2494856033, 1.23952), (2.3919856033, 1.23952))
                Line((2.0281733826, 3.223895), (5.2494856033, 1.23952))
            make_face()
        # Symmetric extrude, full_length=True, total=0.238125
        extrude(amount=0.1190625, both=True)
    return part.part


def model_148051_db355cb7_0011():
    """Model: Fin 3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 4 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 4.815861084, perimeter: 11.7458525474
            with BuildLine():
                Line((5.23875, -1.23952), (1.6271875, -2.82702))
                Line((0, -1.23952), (5.23875, -1.23952))
                Line((0.5953125, -2.6285825), (0, -1.23952))
                Line((1.6271875, -2.82702), (0.5953125, -2.6285825))
            make_face()
        # Symmetric extrude, full_length=True, total=0.238125
        extrude(amount=0.1190625, both=True)
    return part.part


def model_148051_db355cb7_0013():
    """Model: Fin 2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 8 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 1.9106431815, perimeter: 5.4517437956
            with BuildLine():
                Line((1.1509375, -0.5878608), (0.635, -0.9))
                Line((1.1509375, 0.5878608), (1.1509375, -0.5878608))
                Line((0.635, 0.9), (1.1509375, 0.5878608))
                Line((0, 0.9), (0.635, 0.9))
                Line((0, -0.9), (0, 0.9))
                Line((0.635, -0.9), (0, -0.9))
            make_face()
        # Symmetric extrude, full_length=True, total=0.238125
        extrude(amount=0.1190625, both=True)
    return part.part


def model_148051_db355cb7_0014():
    """Model: Wing"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 7 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 23.0035137207, perimeter: 19.1589924406
            with BuildLine():
                Line((4.1671875, 1.23952), (1.905, 6.31952))
                Line((1.905, 6.31952), (-1.0715625, 6.31952))
                Line((-1.0715625, 6.31952), (-2.2225, 2.7079575))
                Line((-2.2225, 2.7079575), (0, 1.23952))
                Line((0, 1.23952), (4.1671875, 1.23952))
            make_face()
        # Symmetric extrude, full_length=True, total=0.238125
        extrude(amount=0.1190625, both=True)
    return part.part


def model_148051_db355cb7_0015():
    """Model: Strake"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 4.1238996572, perimeter: 12.1509663136
            with BuildLine():
                Line((8.6849824, 1.23952), (4.1671875, 1.23952))
                Line((3.3542138672, 3.065145), (8.6849824, 1.23952))
                Line((4.1671875, 1.23952), (3.3542138672, 3.065145))
            make_face()
        # Symmetric extrude, full_length=True, total=0.238125
        extrude(amount=0.1190625, both=True)
    return part.part


def model_148051_db355cb7_0016():
    """Model: Fin 1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 7 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 7.106840625, perimeter: 12.4675142797
            with BuildLine():
                Line((2.9765625, -2.83972), (5.23875, -0.93472))
                Line((5.23875, -0.93472), (0, -0.93472))
                Line((0, -0.93472), (0.7540625, -2.83972))
                Line((0.7540625, -2.83972), (2.9765625, -2.83972))
            make_face()
        # Symmetric extrude, full_length=True, total=0.238125
        extrude(amount=0.1190625, both=True)
    return part.part


def model_148051_e7ab8ae7_0000():
    """Model: BT-55J x 2.75 in v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.5727908806, perimeter: 20.8287592933
            with BuildLine():
                CenterArc((0, 0), 1.685, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.63, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=6.985
        extrude(amount=6.985)
    return part.part


def model_148051_e7ab8ae7_0002():
    """Model: BT-20DJ x 4in (18mm dia) v1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2017687882, perimeter: 11.5296450387
            with BuildLine():
                CenterArc((0, 0), 0.935, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.9, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=10.16
        extrude(amount=10.16)
    return part.part


def model_148051_e7ab8ae7_0003():
    """Model: Fin"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 9 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 16.4486295732, perimeter: 16.3661150355
            with BuildLine():
                Line((4.0616768293, 4.74472), (4.92125, 0.93472))
                Line((0.3484756098, 4.74472), (4.0616768293, 4.74472))
                Line((0, 0.93472), (0.3484756098, 4.74472))
                Line((4.92125, 0.93472), (0, 0.93472))
            make_face()
        # Symmetric extrude, full_length=True, total=0.238125
        extrude(amount=0.1190625, both=True)
    return part.part


def model_148051_e7ab8ae7_0004():
    """Model: Fin extension"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 7 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 8.8663399581, perimeter: 12.0472964225
            with BuildLine():
                Line((3.1043368902, 2.69875), (3.7132012195, 0))
                Line((0.2468368902, 2.69875), (3.1043368902, 2.69875))
                Line((0, 0), (0.2468368902, 2.69875))
                Line((0, 0), (3.7132012195, 0))
            make_face()
        # Symmetric extrude, full_length=True, total=0.238125
        extrude(amount=0.1190625, both=True)
    return part.part


def model_148051_e7ab8ae7_0006():
    """Model: Laser mount"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 7 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 1.4175878906, perimeter: 7.9375
            with BuildLine():
                Line((3.571875, 0.93472), (0, 0.93472))
                Line((3.571875, 1.331595), (3.571875, 0.93472))
                Line((0, 1.331595), (3.571875, 1.331595))
                Line((0, 0.93472), (0, 1.331595))
            make_face()
        # Symmetric extrude, full_length=True, total=0.238125
        extrude(amount=0.1190625, both=True)
    return part.part


def model_148051_e7ab8ae7_0007():
    """Model: BT-20L x 12 in (18mm dia) v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2017687882, perimeter: 11.5296450387
            with BuildLine():
                CenterArc((0, 0), 0.935, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.9, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=30.48
        extrude(amount=30.48)
    return part.part


def model_148051_e7ab8ae7_0008():
    """Model: Laser"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.044534837, perimeter: 0.7480917506
            Circle(0.1190625)
        # OneSide extrude, distance=7.62
        extrude(amount=7.62)
    return part.part


def model_148051_e7ab8ae7_0009():
    """Model: Winglet"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 7 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 3.0241875, perimeter: 10.9614254661
            with BuildLine():
                Line((4.7625, 0.93472), (0, 2.20472))
                Line((0, 2.20472), (0, 0.93472))
                Line((0, 0.93472), (4.7625, 0.93472))
            make_face()
        # Symmetric extrude, full_length=True, total=0.238125
        extrude(amount=0.1190625, both=True)
    return part.part


def model_148051_e7ab8ae7_0010():
    """Model: Wing extension"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 3 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 2.1421328125, perimeter: 7.4172894141
            with BuildLine():
                Line((0, 1.5875), (-2.69875, 0))
                Line((-2.69875, 0), (0, 0))
                Line((0, 0), (0, 1.5875))
            make_face()
        # OneSide extrude, distance=0.238125
        extrude(amount=0.238125)
    return part.part


def model_148051_e7ab8ae7_0011():
    """Model: Wing"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 8 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 16.129, perimeter: 18.0798063314
            with BuildLine():
                Line((0, 4.22275), (5.715, 4.22275))
                Line((0, 1.68275), (0, 4.22275))
                Line((6.985, 1.68275), (0, 1.68275))
                Line((5.715, 4.22275), (6.985, 1.68275))
            make_face()
        # Symmetric extrude, full_length=True, total=0.238125
        extrude(amount=0.1190625, both=True)
    return part.part


def model_148051_e7ab8ae7_0012():
    """Model: Launch Lug 1/8"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0294524311, perimeter: 2.3561944902
            with BuildLine():
                CenterArc((0, 1.88275), 0.2, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 1.88275), 0.175, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=5
        extrude(amount=5)
    return part.part


def model_148051_e7ab8ae7_0013():
    """Model: Centering ring rear"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 16 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 5.4869492452, perimeter: 16.7748683653
            with BuildLine():
                CenterArc((0, -0.37719), 1.62941, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.93472, -79.5789972637, 339.1579945274)
                Line((0.1690718525, -1.25222), (0.1690718525, -0.9193020108))
                Line((-0.1690718525, -1.25222), (0.1690718525, -1.25222))
                Line((-0.1690718525, -0.9193020108), (-0.1690718525, -1.25222))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


def model_148051_e7ab8ae7_0014():
    """Model: Centering ring front"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 9 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 5.5960419296, perimeter: 16.1109039417
            with BuildLine():
                CenterArc((0, -0.37719), 1.62941, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.93472, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


def model_148083_5be191c8_0001():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 78.5398163397, perimeter: 31.4159265359
            Circle(5)
        # OneSide extrude, distance=25
        extrude(amount=25)
    return part.part


def model_148098_33ec30c9_0001():
    """Model: Back Panel"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 2032.254, perimeter: 180.34
            with BuildLine():
                Line((0, 45.72), (0, 0))
                Line((0, 0), (44.45, 0))
                Line((44.45, 0), (44.45, 45.72))
                Line((44.45, 45.72), (0, 45.72))
            make_face()
        # OneSide extrude, distance=1.905
        extrude(amount=1.905)
    return part.part


def model_148098_33ec30c9_0003():
    """Model: Top Right Trim"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 46.355, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 43.5483, perimeter: 49.53
            with BuildLine():
                Line((-22.86, 49.53), (0, 49.53))
                Line((-22.86, 47.625), (-22.86, 49.53))
                Line((0, 47.625), (-22.86, 47.625))
                Line((0, 49.53), (0, 47.625))
            make_face()
            # Profile area: 43.5483, perimeter: 49.53
            with BuildLine():
                Line((-22.86, 45.72), (-22.86, 47.625))
                Line((0, 45.72), (-22.86, 45.72))
                Line((0, 47.625), (0, 45.72))
                Line((0, 47.625), (-22.86, 47.625))
            make_face()
        # OneSide extrude, distance=1.905
        extrude(amount=1.905)
    return part.part


def model_148098_33ec30c9_0006():
    """Model: Right Panel"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 44.45, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 958.0626, perimeter: 133.35
            with BuildLine():
                Line((-1.905, 45.72), (-1.905, 0))
                Line((-1.905, 45.72), (-22.86, 45.72))
                Line((-22.86, 0), (-22.86, 45.72))
                Line((-1.905, 0), (-22.86, 0))
            make_face()
            # Profile area: 87.0966, perimeter: 95.25
            with BuildLine():
                Line((0, 0), (-1.905, 0))
                Line((0, 45.72), (0, 0))
                Line((0, 45.72), (-1.905, 45.72))
                Line((-1.905, 45.72), (-1.905, 0))
            make_face()
        # OneSide extrude, distance=1.905
        extrude(amount=1.905)
    return part.part


def model_148098_33ec30c9_0008():
    """Model: Top"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 45.72), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1018.54635, perimeter: 146.05
            with BuildLine():
                Line((-22.86, -46.355), (-22.86, 1.905))
                Line((0, -46.355), (-22.86, -46.355))
                Line((0, -44.45), (0, -46.355))
                Line((-1.905, -44.45), (0, -44.45))
                Line((-1.905, 0), (-1.905, -44.45))
                Line((0, 0), (-1.905, 0))
                Line((0, 1.905), (0, 0))
                Line((-22.86, 1.905), (0, 1.905))
            make_face()
            # Profile area: 84.67725, perimeter: 92.71
            with BuildLine():
                Line((0, 0), (0, -44.45))
                Line((0, 0), (-1.905, 0))
                Line((-1.905, 0), (-1.905, -44.45))
                Line((-1.905, -44.45), (0, -44.45))
            make_face()
        # OneSide extrude, distance=1.905
        extrude(amount=1.905)
    return part.part


def model_148098_33ec30c9_0009():
    """Model: Top Leeft Trim"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -1.905, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 87.0966, perimeter: 53.34
            with BuildLine():
                Line((22.86, 45.72), (0, 45.72))
                Line((22.86, 49.53), (22.86, 45.72))
                Line((0, 49.53), (22.86, 49.53))
                Line((0, 45.72), (0, 49.53))
            make_face()
        # OneSide extrude, distance=1.905
        extrude(amount=1.905)
    return part.part


def model_148098_33ec30c9_0011():
    """Model: Left Door Panel"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(22.86, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 86.4917625, perimeter: 94.615
            with BuildLine():
                Line((0, 0.15875), (-1.905, 0.15875))
                Line((0, 0.15875), (0, 45.56125))
                Line((-1.905, 45.56125), (0, 45.56125))
                Line((-1.905, 0.15875), (-1.905, 45.56125))
            make_face()
            # Profile area: 1001.862915625, perimeter: 134.9375
            with BuildLine():
                Line((22.06625, 0.15875), (0, 0.15875))
                Line((22.06625, 45.56125), (22.06625, 0.15875))
                Line((0, 45.56125), (22.06625, 45.56125))
                Line((0, 0.15875), (0, 45.56125))
            make_face()
        # OneSide extrude, distance=1.905
        extrude(amount=1.905)
    return part.part


def model_148128_e1d30e8b_0000():
    """Model: tornillo m3 10 mm v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            Circle(0.15)
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


def model_20440_27177360_0001():
    """Model: cavilha v3"""
    with BuildPart() as part:
        # cavilha -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 3 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 6.4655394559, perimeter: 12.0820665259
            with BuildLine():
                Line((4.6, 0), (4.6, 1.8111041113))
                Line((4.6, 1.8111041113), (0, 1))
                Line((0, 0), (0, 1))
                Line((0, 0), (4.6, 0))
            make_face()
        # OneSide extrude, distance=1.7
        extrude(amount=1.7)
    return part.part


def model_20440_27177360_0002():
    """Model: suporte v4"""
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
        # suporte -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 153.995899972, perimeter: 74.4290002971
            with BuildLine():
                _nurbs_edge([(457.5291469123, -653.5203359778), (457.9647462394, -652.3861358817), (457.3983476188, -651.1130345519), (456.2641475227, -650.6775344069)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(454.6863472488, -654.7849357779), (455.8206472423, -655.2209356482), (457.0935473468, -654.654536074), (457.5291469123, -653.5203359778)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                Line((453.8714473274, -655.9236353095), (454.6863472488, -654.7849357779))
                _nurbs_edge([(456.5760474231, -662.4841354545), (456.6741473701, -660.0075348075), (455.6864473846, -657.6111353095), (453.8714473274, -655.9236353095)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(457.7279474762, -663.7302349265), (457.0658473995, -663.7043350394), (456.5502474334, -663.1462352927), (456.5760474231, -662.4841354545)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(457.7753474739, -663.7312343772), (457.7597472694, -663.7312343772), (457.7436473396, -663.7312343772), (457.7279474762, -663.7302349265)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                Line((464.2753474739, -663.7312343772), (457.7753474739, -663.7312343772))
                _nurbs_edge([(465.4756467369, -662.5314338859), (465.4755475547, -663.1941345389), (464.9379470375, -663.7312343772), (464.2753474739, -663.7312343772)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(465.457046273, -662.3229339774), (465.4692466285, -662.3917339499), (465.4756467369, -662.4616344626), (465.4756467369, -662.5314338859)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                Line((464.6757466819, -657.8913334067), (465.457046273, -662.3229339774))
                _nurbs_edge([(464.5361468818, -657.5046337302), (464.6045472648, -657.6242340262), (464.6518466499, -657.7551334556), (464.6757466819, -657.8913334067)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(462.8803470161, -647.6101344283), (462.2372472313, -651.0002344306), (462.824646714, -654.5085342582), (464.5361468818, -657.5046337302)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(462.8832471397, -647.1785343345), (462.9086473014, -647.3210342582), (462.9076478508, -647.4675343688), (462.8803470161, -647.6101344283)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                Line((462.2753474739, -643.7312343772), (462.8832471397, -647.1785343345))
                Line((453.2753474739, -643.7312343772), (462.2753474739, -643.7312343772))
                Line((453.2753474739, -646.5315342601), (453.2753474739, -643.7312343772))
                _nurbs_edge([(454.6893475082, -647.0462344344), (454.2934474971, -646.7136343177), (453.7924474504, -646.5315342601), (453.2753474739, -646.5315342601)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                _nurbs_edge([(454.9608474996, -650.1453345473), (455.7416474846, -649.214634722), (455.6205475357, -647.8269346412), (454.6893475082, -647.0462344344)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
                Line((455.1518474844, -650.5554345305), (454.9608474996, -650.1453345473))
                _nurbs_edge([(456.2641475227, -650.6775344069), (455.9101474311, -650.5418341811), (455.5268476036, -650.4998343642), (455.1518474844, -650.5554345305)], [1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], 3)
            make_face()
            with BuildLine():
                Line((458.6752474739, -660.6316343772), (458.6752474739, -658.8313343772))
                Line((458.6752474739, -658.8313343772), (462.2753474739, -658.8313343772))
                Line((462.2753474739, -658.8313343772), (462.2753474739, -660.6316343772))
                Line((462.2753474739, -660.6316343772), (458.6752474739, -660.6316343772))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.6
        extrude(amount=1.6)
    return part.part


def model_20440_27177360_0004():
    """Model: tampo v3"""
    with BuildPart() as part:
        # tampo -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1008, perimeter: 132
            with BuildLine():
                Line((25.0799894526, -19.1120219043), (-16.9200105474, -19.1120219043))
                Line((25.0799894526, 4.8879780957), (25.0799894526, -19.1120219043))
                Line((-16.9200105474, 4.8879780957), (25.0799894526, 4.8879780957))
                Line((-16.9200105474, -19.1120219043), (-16.9200105474, 4.8879780957))
            make_face()
        # OneSide extrude, distance=1.8
        extrude(amount=1.8)
    return part.part


def model_20506_17515038_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 74.6128255228, perimeter: 40.8407044967
            with BuildLine():
                CenterArc((0, 0), 5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((2.5, 0), 1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


def model_20722_90d46353_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 18 constraints, 12 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 103.2256, perimeter: 40.64
            with BuildLine():
                Line((-174.2771788615, 3.3680835951), (-164.1171788615, 3.3680835951))
                Line((-174.2771788615, -6.7919164049), (-174.2771788615, 3.3680835951))
                Line((-164.1171788615, -6.7919164049), (-174.2771788615, -6.7919164049))
                Line((-164.1171788615, 3.3680835951), (-164.1171788615, -6.7919164049))
            make_face()
            # Profile area: 103.2256, perimeter: 40.64
            with BuildLine():
                Line((-164.1171788615, 125.2880835951), (-174.2771788615, 125.2880835951))
                Line((-164.1171788615, 135.4480835951), (-164.1171788615, 125.2880835951))
                Line((-174.2771788615, 135.4480835951), (-164.1171788615, 135.4480835951))
                Line((-174.2771788615, 125.2880835951), (-174.2771788615, 135.4480835951))
            make_face()
            # Profile area: 103.2256, perimeter: 40.64
            with BuildLine():
                Line((-11.7171788615, 135.4480835951), (-1.5571788615, 135.4480835951))
                Line((-11.7171788615, 125.2880835951), (-11.7171788615, 135.4480835951))
                Line((-1.5571788615, 125.2880835951), (-11.7171788615, 125.2880835951))
                Line((-1.5571788615, 135.4480835951), (-1.5571788615, 125.2880835951))
            make_face()
            # Profile area: 103.2256, perimeter: 40.64
            with BuildLine():
                Line((-11.7171788615, 3.3680835951), (-1.5571788615, 3.3680835951))
                Line((-11.7171788615, -6.7919164049), (-11.7171788615, 3.3680835951))
                Line((-1.5571788615, -6.7919164049), (-11.7171788615, -6.7919164049))
                Line((-1.5571788615, 3.3680835951), (-1.5571788615, -6.7919164049))
            make_face()
        # OneSide extrude, distance=60.96
        extrude(amount=60.96)
    return part.part


def model_20773_eb772a0a_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 170.1886534226, perimeter: 52.1990908556
            with BuildLine():
                Line((7.2973034784, -6.8556384035), (-5.423965869, -6.8556384035))
                Line((7.2973034784, 6.5226376768), (7.2973034784, -6.8556384035))
                Line((-5.423965869, 6.5226376768), (7.2973034784, 6.5226376768))
                Line((-5.423965869, -6.8556384035), (-5.423965869, 6.5226376768))
            make_face()
        # OneSide extrude, distance=7
        extrude(amount=7)
    return part.part


def model_20797_78b83489_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch11 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2016.125, perimeter: 216.8025612107
            with BuildLine():
                Line((127, -63.5), (190.5, -63.5))
                Line((190.5, -63.5), (190.5, 0))
                Line((190.5, 0), (127, -63.5))
            make_face()
        # OneSide extrude, distance=2.54
        extrude(amount=2.54)
    return part.part


def model_20945_8b57f672_0001():
    """Model: Ground v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 9 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 999999.9999999998, perimeter: 4000
            with BuildLine():
                Line((0, 1000), (0, 0))
                Line((0, 0), (1000, 0))
                Line((1000, 0), (1000, 1000))
                Line((1000, 1000), (0, 1000))
            make_face()
            # Profile area: 999999.9999999999, perimeter: 4000
            with BuildLine():
                Line((0, 0), (1000, 0))
                Line((0, 0), (0, -1000))
                Line((0, -1000), (1000, -1000))
                Line((1000, -1000), (1000, 0))
            make_face()
            # Profile area: 1000000.0000000001, perimeter: 4000
            with BuildLine():
                Line((0, 0), (0, -1000))
                Line((-1000, 0), (0, 0))
                Line((-1000, 0), (-1000, -1000))
                Line((-1000, -1000), (0, -1000))
            make_face()
            # Profile area: 1000000, perimeter: 4000
            with BuildLine():
                Line((0, 1000), (-1000, 1000))
                Line((-1000, 1000), (-1000, 0))
                Line((-1000, 0), (0, 0))
                Line((0, 1000), (0, 0))
            make_face()
        # OneSide extrude, distance=5
        extrude(amount=5)
    return part.part


def model_21028_d4d30a2e_0000():
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
        # griff_rundung -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 3 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))) as sk:
            # Profile area: 1.8764577518, perimeter: 7.8202436161
            with BuildLine():
                Line((-0.2845755331, 1.966570742), (-0.5845755331, 1.966570742))
                _nurbs_edge([(-0.5845755331, 1.966570742), (-0.5978521594, 1.9412459191), (-0.6236595143, 1.8894640054), (-0.6601328172, 1.8083943127), (-0.7042704836, 1.6934801852), (-0.7518883361, 1.5383647959), (-0.7919513922, 1.3717546528), (-0.8245963007, 1.1938251537), (-0.8502218509, 1.0051035079), (-0.8694558297, 0.806533287), (-0.8829740675, 0.5994568953), (-0.8913686821, 0.3856363374), (-0.8950007467, 0.1672764643), (-0.8938650648, -0.0529402447), (-0.8874421398, -0.2718017712), (-0.8748524424, -0.4858255489), (-0.8550154887, -0.6915187874), (-0.8268157351, -0.885653022), (-0.7892577321, -1.0655169736), (-0.7416701978, -1.2292631962), (-0.6837906908, -1.3760268281), (-0.6292245599, -1.4796328877), (-0.5836868545, -1.5495986929), (-0.5512863135, -1.5928168442), (-0.5345755331, -1.613569505)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1, 1, 1, 1, 1, 1], 5)
                Line((-0.2845755331, -1.613569505), (-0.5345755331, -1.613569505))
                Line((-0.2845755331, 1.966570742), (-0.2845755331, -1.613569505))
            make_face()
        # TwoSides extrude, along=8.1, against=-2.8
        extrude(amount=8.1)
        extrude(sk.sketch, amount=-2.8)
    return part.part


def model_21233_05d745b4_0011():
    """Model: Link2 v2 (3)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 8.8272607854, perimeter: 25.0212246325
            with BuildLine():
                CenterArc((0, 0), 0.8, 38.6821874535, 282.635625093)
                Line((0.6244997998, -0.5), (6.6755002002, -0.5))
                CenterArc((7.3, 0), 0.8, -141.3178125465, 282.635625093)
                Line((0.6244997998, 0.5), (6.6755002002, 0.5))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((7.3, 0), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.15
        extrude(amount=0.15)
    return part.part


def model_21233_05d745b4_0012():
    """Model: Link1 v1 (5)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 13 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2465033971, perimeter: 2.2929238004
            with BuildLine():
                CenterArc((7.8000001162, 0), 0.4, -180, 90)
                Line((7, 0), (7.4000001162, 0))
                CenterArc((7.8, 0), 0.8, -180, 38.6821881371)
                Line((7.8000001162, -0.5000000075), (7.1755002061, -0.5000000075))
                Line((7.8000001162, -0.4), (7.8000001162, -0.5000000075))
            make_face()
            # Profile area: 1.0149576958, perimeter: 6.6519746786
            with BuildLine():
                Line((7.8, 0.4), (7.8, 0.5))
                CenterArc((7.8000001162, 0), 0.4, -90, 180.0000166486)
                Line((7.8000001162, -0.4), (7.8000001162, -0.5000000075))
                Line((7.8000001162, -0.5000000075), (7.1755002061, -0.5000000075))
                CenterArc((7.8, 0), 0.8, -141.3178118629, 282.6356244095)
                Line((7.8, 0.5), (7.1755002002, 0.5))
            make_face()
            # Profile area: 0.2465033344, perimeter: 2.2929235569
            with BuildLine():
                Line((0.6244997998, 0.5), (0, 0.5))
                Line((0, 0.5), (0, 0.4))
                CenterArc((0, 0), 0.4, 0, 90)
                Line((0.4, 0), (0.8, 0))
                CenterArc((0, 0), 0.8, 0, 38.6821874535)
            make_face()
            # Profile area: 0.2465033808, perimeter: 2.2929235569
            with BuildLine():
                Line((7.8, 0.5), (7.1755002002, 0.5))
                CenterArc((7.8, 0), 0.8, 141.3178125465, 38.6821874535)
                Line((7, 0), (7.4000001162, 0))
                CenterArc((7.8000001162, 0), 0.4, 90.0000166486, 89.9999833514)
                Line((7.8, 0.4), (7.8, 0.5))
            make_face()
            # Profile area: 0.246503339, perimeter: 2.2929235679
            with BuildLine():
                CenterArc((0, 0), 0.8, -38.6821881371, 38.6821881371)
                Line((0.4, 0), (0.8, 0))
                CenterArc((0, 0), 0.4, -90, 90)
                Line((0, -0.5000000075), (0, -0.4))
                Line((0.6244997939, -0.5000000075), (0, -0.5000000075))
            make_face()
            # Profile area: 3.1556659678, perimeter: 13.831210884
            with BuildLine():
                CenterArc((7.8, 0), 0.8, -180, 38.6821881371)
                Line((0.8, 0), (7, 0))
                CenterArc((0, 0), 0.8, -38.6821881371, 38.6821881371)
                Line((7.1755002061, -0.5000000075), (0.6244997939, -0.5000000075))
            make_face()
            # Profile area: 1.0149578004, perimeter: 6.6519744461
            with BuildLine():
                Line((0.6244997939, -0.5000000075), (0, -0.5000000075))
                Line((0, -0.5000000075), (0, -0.4))
                CenterArc((0, 0), 0.4, 90, 180)
                Line((0, 0.5), (0, 0.4))
                Line((0.6244997998, 0.5), (0, 0.5))
                CenterArc((0, 0), 0.8, 38.6821874535, 282.6356244095)
            make_face()
            # Profile area: 3.155665919, perimeter: 13.831210853
            with BuildLine():
                Line((7.1755002002, 0.5), (0.6244997998, 0.5))
                CenterArc((0, 0), 0.8, 0, 38.6821874535)
                Line((0.8, 0), (7, 0))
                CenterArc((7.8, 0), 0.8, 141.3178125465, 38.6821874535)
            make_face()
        # OneSide extrude, distance=0.15
        extrude(amount=0.15)
    return part.part


def model_21234_8b71bd47_0005():
    """Model: 19 204 Woodruff Key v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.6333843489, perimeter: 3.264911335
            with BuildLine():
                Line((0.635, 0), (-0.635, 0))
                CenterArc((0, 0), 0.635, 0, 180)
            make_face()
        # OneSide extrude, distance=0.15875
        extrude(amount=0.15875)
    return part.part


def model_21235_01764fc7_0020():
    """Model: 6-BUSHING v1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.5834608722, perimeter: 9.9745566751
            with BuildLine():
                CenterArc((0, 0), 0.9525, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.635, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-2.54
        extrude(amount=-2.54)
    return part.part


def model_21235_01764fc7_0022():
    """Model: 13-HANDLE v2 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.7125573925, perimeter: 2.9923670025
            Circle(0.47625)
        # OneSide extrude, distance=-7.62
        extrude(amount=-7.62)
    return part.part


def model_21236_b696e901_0018():
    """Model: Green Gear Rod v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0702153812, perimeter: 0.9393362034
            Circle(0.1495)
        # OneSide extrude, distance=3.989
        extrude(amount=3.989)
    return part.part


def model_21236_b696e901_0026():
    """Model: Pink B4 Left v1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 8.7114799776, perimeter: 14.3240332615
            with BuildLine():
                Line((0, -1.3), (6.068, -1.3))
                Line((6.068, -1.3), (4.0683020228, 0.6996979772))
                Line((0, 0), (4.0683020228, 0.6996979772))
                Line((0, 0), (0, -1.3))
            make_face()
        # OneSide extrude, distance=0.25
        extrude(amount=0.25)
    return part.part


def model_21236_b696e901_0029():
    """Model: Boot v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.4191163065, perimeter: 6.4873888297
            with BuildLine():
                CenterArc((0, 0), 0.735, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.2975, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.592
        extrude(amount=0.592)
    return part.part


def model_21236_b696e901_0033():
    """Model: Glove v1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.5358181918, perimeter: 7.7785834103
            with BuildLine():
                CenterArc((0, 0), 0.945, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.293, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.34
        extrude(amount=1.34)
    return part.part


def model_21236_b696e901_0038():
    """Model: Shaft v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0716314541, perimeter: 0.9487609814
            Circle(0.151)
        # OneSide extrude, distance=9.5
        extrude(amount=9.5)
    return part.part


def model_21237_7887a24b_0004():
    """Model: Drive Gear Rubber Washer A v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 4.3589598069, perimeter: 11.6238928183
            with BuildLine():
                CenterArc((0, 0), 1.3, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.55, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


def model_21237_7887a24b_0006():
    """Model: Crankshaft Spacer Tension Spring v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 6 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.7694516208, perimeter: 6.3958029695
            with BuildLine():
                CenterArc((0, 0), 0.625, 0, 360)
            make_face()
            with BuildLine():
                Line((0.32, 0.2482438317), (0.32, -0.2482438317))
                CenterArc((0, 0), 0.405, -142.1970502185, 104.394100437)
                Line((-0.32, 0.2482438317), (-0.32, -0.2482438317))
                CenterArc((0, 0), 0.405, 37.8029497815, 104.394100437)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.325
        extrude(amount=0.325)
    return part.part


def model_21242_6c2af7c2_0000():
    """Model: 26 TEETH 16 v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 18 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 6.8943897988, perimeter: 13.6190391984
            with BuildLine():
                Line((0.1465834369, 1.6383017121), (0.1598486997, 1.8330434783))
                CenterArc((0, 1.84), 0.16, -2.491906369, 184.983812738)
                Line((-0.1483194944, 1.6371074845), (-0.1598486997, 1.8330434783))
                CenterArc((-0.2481468344, 1.6312336278), 0.1, -81.3504614501, 84.7178716865)
                CenterArc((0, 0), 1.55, 98.6496523114, 342.7637279656)
                CenterArc((0.2463522351, 1.6315056164), 0.1, 176.1031202872, 85.3103080845)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


def model_21242_6c2af7c2_0008():
    """Model: 49 HOUR HAND v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 50 constraints, 21 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 6.0459570092, perimeter: 27.6441105058
            with BuildLine():
                Line((-6.4220485754, 0.375), (-6.6495190528, 0.375))
                CenterArc((-6.6495190528, 0), 0.375, 90, 61.5055919803)
                CenterArc((-7.2824070154, 0.3435501523), 0.3451207401, -84.5317539972, 56.0373459775)
                CenterArc((-7.2824070154, -0.3435501523), 0.3451207401, 28.4944080197, 56.0373459775)
                CenterArc((-6.6495190528, 0), 0.375, -151.5055919803, 61.5055919803)
                Line((-6.375, -0.375), (-6.6495190528, -0.375))
                CenterArc((-6, -0.375), 0.375, 180, 173.2436729694)
                CenterArc((-5.5779514246, -0.425), 0.05, 90, 83.2436729694)
                Line((-5.5779514246, -0.375), (-0.704893609, -0.375))
                CenterArc((-0.704893609, -0.475), 0.1, 33.9744759503, 56.0255240497)
                CenterArc((0, 0), 0.75, -146.0255240497, 125.4018878977)
                CenterArc((0.7955271646, -0.2993936044), 0.1, 90, 69.376363848)
                Line((0.7955271646, -0.1993936044), (0.9854247218, -0.1993936044))
                CenterArc((0.9854247218, -0.2993936044), 0.1, 48.5903778907, 41.4096221093)
                CenterArc((1.2499998529, 0.0006063956), 0.3, -131.4096221093, 262.8192442185)
                CenterArc((0.9854247218, 0.3006063956), 0.1, -90, 41.4096221093)
                Line((0.7950696793, 0.2006063956), (0.9854247218, 0.2006063956))
                CenterArc((0.7950696793, 0.3006063956), 0.1, -159.2889905999, 69.2889905999)
                CenterArc((0, 0), 0.75, 20.7110094001, 125.3145146496)
                CenterArc((-0.704893609, 0.475), 0.1, -90, 56.0255240497)
                Line((-0.704893609, 0.375), (-5.5779514246, 0.375))
                CenterArc((-5.5779514246, 0.425), 0.05, -173.2436729694, 83.2436729694)
                CenterArc((-6, 0.375), 0.375, 6.7563270306, 166.4873459388)
                CenterArc((-6.4220485754, 0.425), 0.05, -90, 83.2436729694)
            make_face()
            with BuildLine():
                CenterArc((-6.6495190528, 0), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-6, -0.375), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-6, 0.375), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1.2499998529, 0.0006063956), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0, 0), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)
    return part.part


def model_21242_6c2af7c2_0009():
    """Model: 48 MINUTE HAND v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 21 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 7.5722266335, perimeter: 22.9072261968
            with BuildLine():
                CenterArc((0, 0), 0.75, -142.7522191042, 86.9132201077)
                Line((0.4211402147, -0.6205972281), (1.1085193331, -0.1541385068))
                CenterArc((0.9962152758, 0.0113540874), 0.2, -55.8389989965, 112.9839669694)
                Line((0.4068864871, 0.6300344329), (1.1047183391, 0.1793632695))
                CenterArc((0, 0), 0.75, 57.144967973, 85.6072511312)
                CenterArc((-0.7562241731, 0.575), 0.2, -90, 52.7522191042)
                Line((-0.7562241731, 0.375), (-7.6495190528, 0.375))
                CenterArc((-7.6493576675, -1.7207785117), 2.0957785179, 90.0044120593, 34.9312746511)
                CenterArc((-7.6494315457, 1.7452108805), 2.1202108805, -124.4733402545, 34.4709754936)
                Line((-7.6495190528, -0.3749999982), (-0.7562241731, -0.375))
                CenterArc((-0.7562241731, -0.575), 0.2, 37.2477808958, 52.7522191042)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=0.1
        extrude(amount=0.1, both=True)
    return part.part


def model_21242_6c2af7c2_0010():
    """Model: 31 PAWL v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 13 constraints, 11 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.681404653, perimeter: 28.9447589402
            with BuildLine():
                Line((4.9021492949, -0.2208434044), (2.8075592275, 0.8709254756))
                CenterArc((5.2999894991, -0.0105503424), 0.45, -152.1396629901, 257.5120140089)
                Line((1.2803299759, 2.4563499654), (5.1806986179, 0.4233502057))
                Line((1.2803299759, 2.4563499654), (0, 2.4563499654))
                Line((0, 2.4563499654), (0, 2.2363499654))
                Line((0, 2.2363499654), (1.2252505181, 2.2363499654))
                CenterArc((0, 0), 2.55, -125, 186.282564341)
                Line((-1.5888067287, -2.2690511627), (-1.4626199127, -2.0888377129))
                CenterArc((0, 0), 2.77, -125, 140.8166873885)
                CenterArc((2.7613379287, 0.7822485815), 0.1, 62.47, 133.3466873885)
            make_face()
            with BuildLine():
                CenterArc((5.2999894991, -0.0105503424), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


def model_21242_6c2af7c2_0013():
    """Model: 33 15 TEETH v1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 18 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 5.8153409339, perimeter: 12.9019686303
            with BuildLine():
                Line((0.144786974, 1.5231157395), (0.1598278427, 1.7175797101))
                CenterArc((0, 1.725), 0.16, -2.6581490146, 185.3162980292)
                Line((-0.1469931619, 1.5215668398), (-0.1598278427, 1.7175797101))
                CenterArc((-0.2467794761, 1.5150329667), 0.1, -80.748670579, 84.4949729099)
                CenterArc((0, 0), 1.435, 99.2515108487, 341.5835937515)
                CenterArc((0.244489195, 1.5154042476), 0.1, 175.5772496954, 85.2578547218)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


def model_21242_6c2af7c2_0015():
    """Model: 45 TEETH 8 v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 18 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.0757989844, perimeter: 6.7039549589
            with BuildLine():
                Line((0.1198664323, 0.7172561996), (0.1593939372, 0.9060869565))
                CenterArc((0, 0.92), 0.16, -4.9885419756, 189.9770839511)
                Line((-0.1202346901, 0.7169094967), (-0.1593939372, 0.9060869565))
                CenterArc((-0.2181588007, 0.6966396039), 0.1, -72.6116898472, 84.3065194075)
                CenterArc((0, 0), 0.63, 107.3884198188, 325.2571813782)
                CenterArc((0.2177453014, 0.6967689601), 0.1, 168.1779707188, 84.4676267514)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.305, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


def model_21242_6c2af7c2_0016():
    """Model: 39 TEETH 10 v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 18 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.1679593469, perimeter: 8.0738022686
            with BuildLine():
                Line((0.1272055668, 0.9499915478), (0.1596123849, 1.1388695652))
                CenterArc((0, 1.15), 0.16, -3.989015133, 187.978030266)
                Line((-0.1429267279, 0.9370858864), (-0.1596123849, 1.1388695652))
                CenterArc((-0.2425865323, 0.9288443219), 0.1, -75.3630221403, 80.0904528158)
                CenterArc((0, 0), 0.86, 104.6370078313, 331.7612579814)
                CenterArc((0.2257644665, 0.933075777), 0.1000000001, 170.2611499597, 86.1372360151)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


def model_21242_6c2af7c2_0018():
    """Model: 30.5 15 TEETH BIG HOLE v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 18 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 13.5608984829, perimeter: 18.7158911163
            with BuildLine():
                Line((0.2172020211, 2.3364174894), (0.2376836835, 2.5567364074))
                Line((0.2376836835, 2.5567364074), (0.2397422626, 2.5788803089))
                CenterArc((0, 2.59), 0.24, -2.6555813939, 185.3111627879)
                Line((-0.2376836835, 2.5567364074), (-0.2397422626, 2.5788803089))
                Line((-0.2172020526, 2.3364178283), (-0.2376836835, 2.5567364074))
                CenterArc((-0.4163433892, 2.3179049123), 0.2, -79.8170854417, 85.1282482296)
                CenterArc((0, 0), 2.155, 100.1829145583, 339.6341791489)
                CenterArc((0.4163433892, 2.3179049123), 0.2, 174.6889347256, 85.1280616552)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.65, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


def model_21242_6c2af7c2_0019():
    """Model: 3 ANGLED BRACE v1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 5 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 26.25, perimeter: 28.0710678119
            with BuildLine():
                Line((0, 0), (13, 0))
                Line((13, 0), (10.5, 2.5))
                Line((10.5, 2.5), (2.5, 2.5))
                Line((0, 0), (2.5, 2.5))
            make_face()
        # Symmetric extrude, each_side=0.5
        extrude(amount=0.5, both=True)
    return part.part


def model_21242_6c2af7c2_0020():
    """Model: 4 FRONT v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 46 constraints, 28 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 181.6117285141, perimeter: 136.0889811295
            with BuildLine():
                Line((-2.4, -5.4017219545), (-2.5, -5.4017219545))
                Line((-2.5, -5.4017219545), (-2.5, -6.2617219545))
                CenterArc((-6.5546484056, -11.0180152914), 6.25, 0.607743943, 48.9453036045)
                Line((0.305, -10.9517219545), (-0.305, -10.9517219545))
                CenterArc((6.5546484056, -11.0180152914), 6.25, 130.4469524525, 48.9453036045)
                Line((2.5, -5.4017219545), (2.5, -6.2617219545))
                Line((2.4, -5.4017219545), (2.5, -5.4017219545))
                CenterArc((2.4, -5.1017219545), 0.3, 180, 90)
                Line((2.1, -5.1017219545), (2.1, 33.3982780455))
                CenterArc((2.4, 33.3982780455), 0.3, 90, 90)
                Line((2.4, 33.6982780455), (2.5, 33.6982780455))
                Line((2.5, 33.6982780455), (2.5, 34.5582780455))
                CenterArc((6.5546484056, 39.3145713824), 6.25, -179.392256057, 48.9453036045)
                Line((-0.305, 39.2482780455), (0.305, 39.2482780455))
                CenterArc((-6.5546484056, 39.3145713824), 6.25, -49.5530475475, 48.9453036045)
                Line((-2.5, 33.6982780455), (-2.5, 34.5582780455))
                Line((-2.4, 33.6982780455), (-2.5, 33.6982780455))
                CenterArc((-2.4, 33.3982780455), 0.3, 0, 90)
                Line((-2.1, -5.1017219545), (-2.1, 33.3982780455))
                CenterArc((-2.4, -5.1017219545), 0.3, -90, 90)
            make_face()
            with BuildLine():
                CenterArc((0, 34.2482780455), 1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0, 29.3482780455), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0, 25.1082780455), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0, 21.2482780455), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0, 17.6282780455), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0, 12.5082780455), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0, 7.9082780455), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0, 3.8382780455), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0, -0.0917219545), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0, -5.2417219545), 1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=0.5
        extrude(amount=0.5, both=True)
    return part.part


def model_21246_c66f2b12_0016():
    """Model: 3X4mm Screw v1 (3)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0665083019, perimeter: 0.9142034622
            Circle(0.1455)
        # OneSide extrude, distance=-0.4
        extrude(amount=-0.4)
    return part.part


def model_21246_c66f2b12_0017():
    """Model: 4mm nut v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.381541889, perimeter: 3.5807255757
            with BuildLine():
                Line((0.3671947712, 0.212), (0, 0.424))
                Line((0, 0.424), (-0.3671947712, 0.212))
                Line((-0.3671947712, 0.212), (-0.3671947712, -0.212))
                Line((-0.3671947712, -0.212), (0, -0.424))
                Line((0, -0.424), (0.3671947712, -0.212))
                Line((0.3671947712, -0.212), (0.3671947712, 0.212))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.165, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.33
        extrude(amount=0.33)
    return part.part


def model_21246_c66f2b12_0018():
    """Model: B1 v2 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 9 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.5625, perimeter: 7.8743811123
            with BuildLine():
                Line((1.6, 0), (0, 0))
                Line((1.25, 2.5), (1.6, 0))
                Line((0, 2.5), (1.25, 2.5))
                Line((0, 0), (0, 2.5))
            make_face()
            # Profile area: 3.5625, perimeter: 7.8743811123
            with BuildLine():
                Line((0, 0), (0, 2.5))
                Line((-1.25, 2.5), (0, 2.5))
                Line((-1.6, 0), (-1.25, 2.5))
                Line((0, 0), (-1.6, 0))
            make_face()
        # OneSide extrude, distance=0.6
        extrude(amount=0.6)
    return part.part


def model_21246_c66f2b12_0029():
    """Model: 3X12 mm Tapping Screw v1 (7)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0665083019, perimeter: 0.9142034622
            Circle(0.1455)
        # OneSide extrude, distance=-1.2
        extrude(amount=-1.2)
    return part.part


def model_21256_433456a3_0002():
    """Model: Bottom Slot v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 25 constraints, 12 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2, perimeter: 6
            with BuildLine():
                Line((0.5, -0.6), (0.5, -1))
                Line((0.5, 0.6), (0.5, -0.6))
                Line((0.5, 1), (0.5, 0.6))
                Line((-0.5, 1), (0.5, 1))
                Line((-0.5, -1), (-0.5, 1))
                Line((0.5, -1), (-0.5, -1))
            make_face()
            # Profile area: 9.622328595, perimeter: 25.3377248662
            with BuildLine():
                Line((0.5, -0.6), (9.0333333333, -0.6))
                CenterArc((9.0333333333, -0.4), 0.2, -90, 19.4712206345)
                Line((9.1, -0.5885618083), (9.1, 0.5885618083))
                CenterArc((9.0333333333, 0.4), 0.2, 70.5287793655, 19.4712206345)
                Line((9.0333333333, 0.6), (0.5, 0.6))
                Line((0.5, 0.6), (0.5, -0.6))
            make_face()
            with BuildLine():
                CenterArc((8.2, 0), 0.198, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((7.059, 0.141), (5.245, 0.141))
                CenterArc((7.059, 0), 0.141, -90, 180)
                Line((5.245, -0.141), (7.059, -0.141))
                CenterArc((5.245, 0), 0.141, 90, 180)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.4785606855, perimeter: 3.1246521515
            with BuildLine():
                Line((9.1, -0.5885618083), (9.1, 0.5885618083))
                CenterArc((9.0333333333, -0.4), 0.2, -70.5287793655, 17.3986770114)
                Line((9.8466666667, -0.04), (9.1533333333, -0.56))
                CenterArc((9.8166666667, 0), 0.05, -53.1301023542, 106.2602047083)
                Line((9.1533333333, 0.56), (9.8466666667, 0.04))
                CenterArc((9.0333333333, 0.4), 0.2, 53.1301023542, 17.3986770114)
            make_face()
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)
    return part.part


def model_21256_433456a3_0009():
    """Model: Main Gear Rod v1 v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            Circle(0.15)
        # OneSide extrude, distance=2.466
        extrude(amount=2.466)
    return part.part


def model_21368_8605ac77_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 99.2699081699, perimeter: 37.7079632679
            with BuildLine():
                CenterArc((0, 6), 5, 0, 180)
                Line((-5, 6), (-5, 0))
                Line((-5, 0), (5, 0))
                Line((5, 0), (5, 6))
            make_face()
        # OneSide extrude, distance=-8
        extrude(amount=-8)
    return part.part


def model_21385_601444ba_0007():
    """Model: Eccentric Rod v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0374760852, perimeter: 0.6862494993
            Circle(0.10922)
        # OneSide extrude, distance=7.70128
        extrude(amount=7.70128)
    return part.part


def model_21385_601444ba_0018():
    """Model: Eccentric v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.391502222, perimeter: 5.4820163487
            Circle(0.87249)
        # OneSide extrude, distance=0.47498
        extrude(amount=0.47498)
    return part.part


def model_21385_601444ba_0036():
    """Model: Beam Pivot Shaft v2 (3)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1771905384, perimeter: 1.4921936786
            Circle(0.23749)
        # OneSide extrude, distance=3.81
        extrude(amount=3.81)
    return part.part


def model_21385_601444ba_0040():
    """Model: Grounding Link v1 (11)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 11 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2633799998, perimeter: 4.428554314
            with BuildLine():
                CenterArc((-1.2395202616, -0.0111317412), 0.23622, -12.8084751634, 31.2261460576)
                Line((1.0701377017, -0.0635), (-1.0091782249, -0.0635))
                CenterArc((1.3004797384, -0.0111317412), 0.23622, 161.5823291058, 31.2261460576)
                Line((-1.015399777, 0.0635), (1.0763592538, 0.0635))
            make_face()
            # Profile area: 0.0961274759, perimeter: 2.4816697008
            with BuildLine():
                CenterArc((-1.2395202616, -0.0111317412), 0.23622, 18.4176708942, 328.7738539424)
                CenterArc((-1.2395202616, -0.0111317412), 0.23622, -12.8084751634, 31.2261460576)
            make_face()
            with BuildLine():
                CenterArc((-1.2395202616, -0.0111317412), 0.15875, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0961274759, perimeter: 2.4816697008
            with BuildLine():
                CenterArc((1.3004797384, -0.0111317412), 0.23622, -167.1915248366, 328.7738539424)
                CenterArc((1.3004797384, -0.0111317412), 0.23622, 161.5823291058, 31.2261460576)
            make_face()
            with BuildLine():
                CenterArc((1.3004797384, -0.0111317412), 0.15875, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.15748
        extrude(amount=0.15748)
    return part.part


def model_21422_b2a6bf27_0000():
    """Model: Component1"""
    with BuildPart() as part:
        # Sketch2 -> Extrude2 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.7671458676, perimeter: 4.7123889804
            with Locations((1.9958956079, -0.0012760151)):
                Circle(0.75)
        # OneSide extrude, distance=1.9
        extrude(amount=1.9)
    return part.part


def model_21452_73ad419b_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 19 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.5393804003, perimeter: 4.398229715
            with BuildLine():
                CenterArc((-5.0024801057, 4.4148342513), 0.7, 89.9993567146, 202.2343364173)
                CenterArc((-5.0024801057, 4.4148342513), 0.7, -67.7663068681, 157.7656635827)
            make_face()
            # Profile area: 17.1872695941, perimeter: 30.5402753897
            with BuildLine():
                CenterArc((-5.0024801057, 4.4148342513), 0.7, -67.7663068681, 157.7656635827)
                CenterArc((-2.8457207944, -0.8613754937), 5, 22.6934069421, 89.5398374937)
                CenterArc((2.5975198943, 1.4148342513), 0.9, -59.9993470396, 262.6920940679)
                CenterArc((3.7975198943, -0.6636267178), 1.5, 59.9999988986, 59.9996093251)
                CenterArc((4.9975198943, 1.4148342513), 0.9, 33.107772594, 206.8922274059)
                CenterArc((-0.1710250991, -1.9554974181), 7.0703316694, 33.1077751332, 56.8922303922)
                Line((-5.0024722465, 5.1148342513), (-0.171025781, 5.1148342513))
            make_face()
            # Profile area: 1.9085175176, perimeter: 8.4823001359
            with BuildLine():
                CenterArc((4.9975198943, 1.4148342513), 0.9, 33.107772594, 206.8922274059)
                CenterArc((4.9975198943, 1.4148342513), 0.9, -119.9999981643, 153.1077707584)
            make_face()
            with BuildLine():
                CenterArc((4.9975198943, 1.4148342513), 0.45, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 1.9085175371, perimeter: 8.4823001647
            with BuildLine():
                CenterArc((2.5975198943, 1.4148342513), 0.9, -59.9993470396, 262.6920940679)
                CenterArc((2.5975198943, 1.4148342513), 0.9, -157.3072529717, 97.3079059321)
            make_face()
            with BuildLine():
                CenterArc((2.5975198943, 1.4148342513), 0.45, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=1.2
        extrude(amount=1.2, both=True)
    return part.part


def model_21472_f94fbb81_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch4 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 12 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1192.2212253331, perimeter: 397.407075111
            with BuildLine():
                Line((-55, 40), (0, 40))
                CenterArc((-55, 20), 20, 90, 90)
                Line((-75, 0), (-75, 20))
                Line((0, 0), (-75, 0))
                Line((0, 40), (0, 0))
            make_face()
            with BuildLine():
                Line((-6, 34), (-6, 6))
                Line((-6, 6), (-69, 6))
                Line((-69, 6), (-69, 20))
                CenterArc((-55, 20), 14, 90, 90)
                Line((-55, 34), (-6, 34))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=32
        extrude(amount=32)
    return part.part


def model_21479_a3c5bdab_0001():
    """Model: Traseiro"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 24, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 6286.8, perimeter: 317.2
            with BuildLine():
                Line((0.35, 0), (-80.25, 0))
                Line((0.35, 78), (0.35, 0))
                Line((-80.25, 78), (0.35, 78))
                Line((-80.25, 0), (-80.25, 78))
            make_face()
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)
    return part.part


def model_21479_a3c5bdab_0002():
    """Model: Travessa Frontal"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.75, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 20.25, perimeter: 30
            with BuildLine():
                Line((-22.5, 78), (-22.5, 64.5))
                Line((-24, 78), (-22.5, 78))
                Line((-24, 64.5), (-24, 78))
                Line((-22.5, 64.5), (-24, 64.5))
            make_face()
        # OneSide extrude, distance=78
        extrude(amount=78)
    return part.part


def model_21492_8bd34fc1_0007():
    """Model: Clicks v1 (2)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 2.0665054052, perimeter: 8.8334884446
            with BuildLine():
                CenterArc((-0.29718, -1.154684), 1.55575, 9.7866037021, 151.8325963316)
                Line((-0.7823427789, -1.044599725), (-1.773558332, -0.6641077232))
                CenterArc((0.263398, -1.446022), 1.12014, 29.7471146676, 129.2528853324)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.17859375, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.27
        extrude(amount=1.27)
    return part.part


def model_21492_8bd34fc1_0008():
    """Model: Third and Fourth Wheel Pinions v1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 7 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 3.1681971405, perimeter: 15.5366703158
            with BuildLine():
                CenterArc((-0.8231303403, -0.8231302118), 0.19812, 124.9395118352, 100.0604962839)
                CenterArc((-0.8231303403, -0.8231302118), 0.19812, -134.9999918809, 100.0604800458)
                Line((-0.6607200593, -0.9365957792), (-0.4990061504, -0.705124179))
                CenterArc((-0.3390944711, -0.8168440968), 0.195072, 67.2974122125, 77.7630851215)
                CenterArc((-0.33782, -0.817372), 0.195072, -10.0605808915, 77.7631686792)
                Line((-0.1950737742, -1.1294728611), (-0.1457475055, -0.8514490015))
                CenterArc((-0.0000000909, -1.164082), 0.19812, 169.9395118352, 100.0604962792)
                CenterArc((-0.0000000909, -1.164082), 0.19812, -89.9999918856, 100.0604800505)
                Line((0.1950735923, -1.1294728611), (0.1457474558, -0.8514487214))
                CenterArc((0.33782, -0.817372), 0.195072, 112.2974122123, 77.7630851217)
                CenterArc((0.3390944711, -0.8168440968), 0.195072, 34.9394191085, 77.763168679)
                Line((0.6607199307, -0.9365959078), (0.4990063133, -0.7051244123))
                CenterArc((0.8231302118, -0.8231303403), 0.19812, -145.0604881648, 100.0604962045)
                CenterArc((0.8231302118, -0.8231303403), 0.19812, -44.9999919603, 100.0604801251)
                Line((0.9365957792, -0.6607200593), (0.705124179, -0.4990061504))
                CenterArc((0.8168440968, -0.3390944711), 0.195072, 157.2974122122, 77.7630851218)
                CenterArc((0.817372, -0.33782), 0.195072, 79.9394191085, 77.7631686789)
                Line((1.1294728611, -0.1950737742), (0.8514490015, -0.1457475055))
                CenterArc((1.164082, -0.0000000909), 0.19812, -100.0604881648, 100.0604963009)
                CenterArc((1.164082, -0.0000000909), 0.19812, 0.000008136, 100.0604800288)
                Line((1.1294728611, 0.1950735923), (0.8514487214, 0.1457474558))
                CenterArc((0.817372, 0.33782), 0.195072, -157.7025877873, 77.7630851214)
                CenterArc((0.8168440968, 0.3390944711), 0.195072, 124.9394191085, 77.7631686794)
                Line((0.9365959078, 0.6607199307), (0.7051244123, 0.4990063133))
                CenterArc((0.8231303403, 0.8231302118), 0.19812, -55.0604881648, 100.0604962357)
                CenterArc((0.8231303403, 0.8231302118), 0.19812, 45.0000080709, 100.060480094)
                Line((0.6607200593, 0.9365957792), (0.4990061504, 0.705124179))
                CenterArc((0.3390944711, 0.8168440968), 0.195072, -112.7025877875, 77.7630851216)
                CenterArc((0.33782, 0.817372), 0.195072, 169.9394191085, 77.7631686792)
                Line((0.1950737742, 1.1294728611), (0.1457475055, 0.8514490015))
                CenterArc((0.0000000909, 1.164082), 0.19812, -10.0604881648, 100.0604962422)
                CenterArc((0.0000000909, 1.164082), 0.19812, 90.0000080774, 100.0604800874)
                Line((-0.1950735923, 1.1294728611), (-0.1457474558, 0.8514487214))
                CenterArc((-0.33782, 0.817372), 0.195072, -67.7025877879, 77.7630851219)
                CenterArc((-0.3390944711, 0.8168440968), 0.195072, -145.0605808915, 77.7631686788)
                Line((-0.6607199307, 0.9365959078), (-0.4990063133, 0.7051244123))
                CenterArc((-0.8231302118, 0.8231303403), 0.19812, 34.9395118352, 100.0604962023)
                CenterArc((-0.8231302118, 0.8231303403), 0.19812, 135.0000080374, 100.0604801274)
                Line((-0.9365957792, 0.6607200593), (-0.705124179, 0.4990061504))
                CenterArc((-0.8168440968, 0.3390944711), 0.195072, -22.7025877876, 77.7630851216)
                CenterArc((-0.817372, 0.33782), 0.195072, -100.0605808915, 77.7631686791)
                Line((-1.1294728611, 0.1950737742), (-0.8514490015, 0.1457475055))
                CenterArc((-1.164082, 0.0000000909), 0.19812, 79.9395118352, 100.060496281)
                CenterArc((-1.164082, 0.0000000909), 0.19812, -179.9999918838, 100.0604800487)
                Line((-1.1294728611, -0.1950735923), (-0.8514487214, -0.1457474558))
                CenterArc((-0.817372, -0.33782), 0.195072, 22.2974122123, 77.7630851217)
                CenterArc((-0.8168440968, -0.3390944711), 0.195072, -55.0605808915, 77.763168679)
                Line((-0.9365959078, -0.6607199307), (-0.7051244123, -0.4990063133))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.1984375, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.27
        extrude(amount=1.27)
    return part.part


def model_21492_8bd34fc1_0015():
    """Model: Center Bob v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 10 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 22.2861528509, perimeter: 91.3361685757
            with BuildLine():
                CenterArc((0, 0), 5.08, 100.815672546, 338.368654908)
                Line((0.953262, -4.405122), (0.953262, 4.9897586674))
                Line((-0.953262, -4.405122), (0.953262, -4.405122))
                Line((-0.953262, -4.405122), (-0.953262, 4.9897586674))
            make_face()
            with BuildLine():
                Line((-1.425448, -4.3775120859), (-1.425448, 4.3775120859))
                CenterArc((0, 0), 4.60375, 108.0367885467, 143.9264229066)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((1.425448, -4.3775120859), (1.425448, 4.3775120859))
                CenterArc((0, 0), 4.60375, -71.9632114533, 143.9264229066)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.27
        extrude(amount=1.27)
    return part.part


def model_21495_ebbbd369_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # body -> 押し出し1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 9 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 36.5638, perimeter: 24.38
            with BuildLine():
                Line((6.86, 5.33), (0, 5.33))
                Line((0, 5.33), (0, 0))
                Line((0, 0), (6.86, 0))
                Line((6.86, 0), (6.86, 5.33))
            make_face()
        # OneSide extrude, distance=0.16
        extrude(amount=0.16)
    return part.part


def model_21497_9833a679_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 8 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.2725797182, perimeter: 7.5372028095
            with BuildLine():
                Line((0, -1.7650267045), (0.576328757, -1.7650267045))
                Line((0.576328757, -1.7650267045), (0.576328757, -1.2000000179))
                Line((0.576328757, -1.2000000179), (1.1500000171, -1.2000000179))
                CenterArc((1.1500000171, -0.6250000093), 0.5750000086, -90, 184.2269009241)
                Line((0.5999824733, -0.0515640115), (1.1076188147, -0.0515640115))
                Line((0.5999824733, -0.0515640115), (0.5999824733, -0.1008544535))
                CenterArc((0.5472960597, -0.5980708544), 0.5000000075, -174.0386071446, 257.9899600844)
                Line((0, -0.6500000097), (0.0500000007, -0.6500000097))
                Line((0, -1.7650267045), (0, -0.6500000097))
            make_face()
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)
    return part.part


def model_21519_3e869afd_0001():
    """Model: parallel slide v5"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.2173671533, perimeter: 9.7389372261
            with BuildLine():
                CenterArc((0, 0), 0.9, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.65, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=13
        extrude(amount=13)
    return part.part


def model_21557_53eafe15_0016():
    """Model: Part 12 - Spacer v1 (2)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.6278105666, perimeter: 4.7079907507
            with BuildLine():
                CenterArc((0, 0), 0.508, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.2413, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.524
        extrude(amount=1.524)
    return part.part


def model_21557_53eafe15_0044():
    """Model: Nut v1 (6)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 4 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.4007105908, perimeter: 6.0091765871
            with BuildLine():
                Line((0.508, -0.2932939367), (0.508, 0.2932939367))
                Line((0.508, 0.2932939367), (0, 0.5865878735))
                Line((0, 0.5865878735), (-0.508, 0.2932939367))
                Line((-0.508, 0.2932939367), (-0.508, -0.2932939367))
                Line((-0.508, -0.2932939367), (0, -0.5865878735))
                Line((0, -0.5865878735), (0.508, -0.2932939367))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.39624, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.47625
        extrude(amount=0.47625)
    return part.part


def model_21557_53eafe15_0046():
    """Model: Part 5 - Link v1 (6)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 6 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 16.1868279226, perimeter: 27.8397477321
            with BuildLine():
                CenterArc((-4.191, 0), 0.889, 90, 180)
                Line((-4.191, -0.889), (4.191, -0.889))
                CenterArc((4.191, 0), 0.889, -90, 180)
                Line((-4.191, 0.889), (4.191, 0.889))
            make_face()
            with BuildLine():
                CenterArc((4.191, 0), 0.43688, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-4.191, 0), 0.43688, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.47752
        extrude(amount=0.47752)
    return part.part


def model_21557_53eafe15_0049():
    """Model: Part 15 - Nut v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.3308975963, perimeter: 7.2774365502
            with BuildLine():
                CenterArc((0, 0), 0.762, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.39624, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.27
        extrude(amount=1.27)
    return part.part


def model_21604_520e1ae2_0001():
    """Model: Crankrod 2 v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 10 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.1745231019, perimeter: 6.3538945912
            with BuildLine():
                CenterArc((-1.2499995657, 0), 0.155, -90.000160534, 180.000321068)
                Line((-1.25, -0.25), (-1.25, -0.155))
                Line((1.25, -0.25), (-1.25, -0.25))
                Line((1.25, -0.155), (1.25, -0.25))
                CenterArc((1.25, 0), 0.155, 90, 180)
                Line((1.25, 0.25), (1.25, 0.155))
                Line((-1.25, 0.25), (1.25, 0.25))
                Line((-1.25, 0.155), (-1.25, 0.25))
            make_face()
            # Profile area: 0.0604363062, perimeter: 1.4623432876
            with BuildLine():
                Line((-1.25, 0.155), (-1.25, 0.25))
                CenterArc((-1.2499995657, 0), 0.25, 90.0000995311, 179.9998009389)
                Line((-1.25, -0.25), (-1.25, -0.155))
                CenterArc((-1.2499995657, 0), 0.155, 90.000160534, 179.999678932)
            make_face()
            # Profile area: 0.0604363887, perimeter: 1.4623450247
            with BuildLine():
                CenterArc((1.25, 0), 0.25, -90, 180)
                Line((1.25, 0.25), (1.25, 0.155))
                CenterArc((1.25, 0), 0.155, -90, 180)
                Line((1.25, -0.155), (1.25, -0.25))
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)
    return part.part


def model_21604_520e1ae2_0007():
    """Model: Connecting Link v1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 11 constraints, 12 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1256637061, perimeter: 1.6566370614
            with BuildLine():
                Line((-1.8, 0.1), (-1.8, 0.3))
                CenterArc((-1.8, 0), 0.3, 90, 180)
                Line((-1.8, -0.3), (-1.8, -0.1))
                CenterArc((-1.8, 0), 0.1, 90, 180)
            make_face()
            # Profile area: 1.6062942911, perimeter: 13.7119464279
            with BuildLine():
                CenterArc((-1.8, 0), 0.1, -90, 180)
                Line((-1.8, -0.3), (-1.8, -0.1))
                Line((1.8, -0.3), (-1.8, -0.3))
                Line((1.8, -0.15), (1.8, -0.3))
                CenterArc((1.8, 0), 0.15, 90, 180)
                Line((1.8, 0.3), (1.8, 0.15))
                Line((-1.8, 0.3), (1.8, 0.3))
                Line((-1.8, 0.1), (-1.8, 0.3))
            make_face()
            with BuildLine():
                CenterArc((-1.2, 0), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-0.4, 0), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0.4, 0), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1.2, 0), 0.200000003, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.1060287521, perimeter: 1.7137166941
            with BuildLine():
                CenterArc((1.8, 0), 0.3, -90, 180)
                Line((1.8, 0.3), (1.8, 0.15))
                CenterArc((1.8, 0), 0.15, -90, 180)
                Line((1.8, -0.15), (1.8, -0.3))
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)
    return part.part


def model_21604_520e1ae2_0009():
    """Model: Crankrod 1 v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 9 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.1247073545, perimeter: 6.152708138
            with BuildLine():
                CenterArc((1.2005944139, 0), 0.155, 90.2197257394, 179.5605485213)
                Line((1.2, 0.25), (1.2, 0.1549988602))
                Line((-1.2, 0.25), (1.2, 0.25))
                Line((-1.2, 0.155), (-1.2, 0.25))
                CenterArc((-1.1999995167, 0), 0.155, -90.0001786393, 180.0003572786)
                Line((-1.2, -0.25), (-1.2, -0.155))
                Line((1.2, -0.25), (-1.2, -0.25))
                Line((1.2, -0.1549988602), (1.2, -0.25))
            make_face()
            # Profile area: 0.0604362969, perimeter: 1.4623430917
            with BuildLine():
                CenterArc((-1.1999995167, 0), 0.25, 90.0001107564, 179.9997784906)
                Line((-1.2, -0.25), (-1.2, -0.155))
                CenterArc((-1.1999995167, 0), 0.155, 90.0001786393, 179.9996427214)
                Line((-1.2, 0.155), (-1.2, 0.25))
            make_face()
            # Profile area: 0.0605498833, perimeter: 1.4647271838
            with BuildLine():
                Line((1.2, -0.1549988602), (1.2, -0.25))
                CenterArc((1.2005944139, 0), 0.2500007067, -90.1362293678, 180.2724587355)
                Line((1.2, 0.25), (1.2, 0.1549988602))
                CenterArc((1.2005944139, 0), 0.155, -90.2197257394, 180.4394514787)
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)
    return part.part


def model_21636_f65686bc_0003():
    """Model: output axle support v4"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 154.9664626045, perimeter: 58.9796453401
            with BuildLine():
                Line((-5.25, 7.5), (5.25, 7.5))
                Line((-5.25, -7.5), (-5.25, 7.5))
                Line((5.25, -7.5), (-5.25, -7.5))
                Line((5.25, 7.5), (5.25, -7.5))
            make_face()
            with BuildLine():
                CenterArc((0, 5), 0.635, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0, -5), 0.635, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


def model_21636_f65686bc_0004():
    """Model: input axle support v5"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 102.4664626045, perimeter: 51.9796453401
            with BuildLine():
                Line((-3.5, 7.5), (3.5, 7.5))
                Line((-3.5, -7.5), (-3.5, 7.5))
                Line((3.5, -7.5), (-3.5, -7.5))
                Line((3.5, 7.5), (3.5, -7.5))
            make_face()
            with BuildLine():
                CenterArc((0, 5), 0.635, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0, -5), 0.635, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


def model_21636_f65686bc_0005():
    """Model: spacer1 v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 9.4247779608, perimeter: 18.8495559215
            with BuildLine():
                CenterArc((0, 0), 2, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=2.5
        extrude(amount=2.5)
    return part.part


def model_21642_b79d233e_0011():
    """Model: Horseshoe Clip v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 9 constraints, 14 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 0.1840459085, perimeter: 5.4337055033
            with BuildLine():
                Line((-0.0635, 0.4699), (-0.26924, 0.4699))
                Line((-0.26924, 0.4699), (-0.26924, 0.2513060135))
                CenterArc((0, 0), 0.3683, 136.9731886361, 266.0536227279)
                Line((0.26924, 0.4699), (0.26924, 0.2513060135))
                Line((0.0635, 0.4699), (0.26924, 0.4699))
                Line((0.0635, 0.2851142929), (0.0635, 0.4699))
                CenterArc((0, 0), 0.2921, 102.5558577986, 334.8882844028)
                Line((-0.0635, 0.2851142929), (-0.0635, 0.4699))
            make_face()
            with BuildLine():
                CenterArc((0.1651, 0.3429), 0.0635, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-0.1651, 0.3429), 0.0635, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.0635
        extrude(amount=0.0635)
    return part.part


def model_21642_b79d233e_0019():
    """Model: Piston Pin v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0951039268, perimeter: 1.0932114116
            Circle(0.17399)
        # OneSide extrude, distance=1.3843
        extrude(amount=1.3843)
    return part.part


def model_21644_aa203dc5_0015():
    """Model: PT-201-P-035 v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 24.6, perimeter: 20.2
            with BuildLine():
                Line((-2.05, 3), (-2.05, -3))
                Line((-2.05, -3), (2.05, -3))
                Line((2.05, -3), (2.05, 3))
                Line((2.05, 3), (-2.05, 3))
            make_face()
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)
    return part.part


def model_21644_aa203dc5_0018():
    """Model: PT-201-P-037 v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 93.70718, perimeter: 39.6284749851
            with BuildLine():
                Line((-3, 10.6), (3, 10.6))
                Line((-3, 10.6), (-5.8403, 0))
                Line((-5.8403, 0), (5.8403, 0))
                Line((3, 10.6), (5.8403, 0))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


def model_21644_aa203dc5_0019():
    """Model: PT-201-P-038 v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 31.1769, perimeter: 28.3922958037
            with BuildLine():
                Line((6, 0), (6, -10.3923))
                Line((0, 0), (6, 0))
                Line((6, -10.3923), (0, 0))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


def model_21646_a2dd0d00_0001():
    """Model: Saturn Tube v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1039146197, perimeter: 5.2366422545
            with BuildLine():
                CenterArc((0, 0), 0.4365625, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.396875, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=6.0325
        extrude(amount=6.0325)
    return part.part


def model_21646_a2dd0d00_0006():
    """Model: Jupiter Tube v1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0940179893, perimeter: 4.7379144207
            with BuildLine():
                CenterArc((0, 0), 0.396875, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.3571875, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=9.04875
        extrude(amount=9.04875)
    return part.part


def model_21646_a2dd0d00_0007():
    """Model: Drive Wheel Peg v1 (9)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1433365246, perimeter: 1.5803170258
            with BuildLine():
                Line((-0.254, 0), (0.254, 0))
                Line((-0.254, -0.2821585129), (-0.254, 0))
                Line((0.254, -0.2821585129), (-0.254, -0.2821585129))
                Line((0.254, 0), (0.254, -0.2821585129))
            make_face()
            # Profile area: 0.16129, perimeter: 1.7200893875
            with BuildLine():
                Line((0.254, 0), (0.0642511966, 0.508))
                Line((0.0642511966, 0.508), (-0.0627488034, 0.508))
                Line((-0.0627488034, 0.508), (-0.254, 0))
                Line((-0.254, 0), (0.254, 0))
            make_face()
        # OneSide extrude, distance=1.27
        extrude(amount=1.27)
    return part.part


def model_21646_a2dd0d00_0008():
    """Model: Mars Tube v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0841213588, perimeter: 4.2391865869
            with BuildLine():
                CenterArc((0, 0), 0.3571875, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.3175, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=12.065
        extrude(amount=12.065)
    return part.part


def model_21646_a2dd0d00_0023():
    """Model: Below Mercury v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.8889354429, perimeter: 9.4758288414
            with BuildLine():
                CenterArc((0, 0), 1.27, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.238125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.3175
        extrude(amount=0.3175)
    return part.part


def model_21646_a2dd0d00_0024():
    """Model: Below Venus v2 (2)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.8246073449, perimeter: 9.7251927583
            with BuildLine():
                CenterArc((0, 0), 1.27, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.2778125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.635
        extrude(amount=0.635)
    return part.part


def model_21646_a2dd0d00_0029():
    """Model: Below Jupiter v2 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.5722432684, perimeter: 10.4732845089
            with BuildLine():
                CenterArc((0, 0), 1.27, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.396875, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.3175
        extrude(amount=0.3175)
    return part.part


def model_21646_a2dd0d00_0036():
    """Model: Crank Plate v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 8 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 159.6200063023, perimeter: 54.7898226701
            with BuildLine():
                Line((6.0325, -6.6675), (6.0325, 6.6675))
                Line((6.0325, 6.6675), (-6.0325, 6.6675))
                Line((-6.0325, 6.6675), (-6.0325, -6.6675))
                Line((-6.0325, -6.6675), (6.0325, -6.6675))
            make_face()
            with BuildLine():
                CenterArc((0, -2.3495), 0.635, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.905
        extrude(amount=1.905)
    return part.part


def model_21646_a2dd0d00_0037():
    """Model: Foot v1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 12.9717114649, perimeter: 12.7674325442
            Circle(2.032)
        # OneSide extrude, distance=1.905
        extrude(amount=1.905)
    return part.part


def model_21646_a2dd0d00_0039():
    """Model: Frame Support v1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 5.0670751144, perimeter: 7.9796455948
            Circle(1.2700000405)
        # OneSide extrude, distance=14.9225
        extrude(amount=14.9225)
    return part.part


def model_21646_a2dd0d00_0043():
    """Model: Crank Handle v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.7125573925, perimeter: 2.9923670025
            Circle(0.47625)
        # OneSide extrude, distance=6.35
        extrude(amount=6.35)
    return part.part


def model_21646_a2dd0d00_0051():
    """Model: Mercury Tube v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0544314675, perimeter: 2.7430030857
            with BuildLine():
                CenterArc((0, 0), 0.238125, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.1984375, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=21.74875
        extrude(amount=21.74875)
    return part.part


def model_21646_a2dd0d00_0057():
    """Model: Planet Arbor v1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1237078806, perimeter: 1.2468195844
            Circle(0.1984375)
        # OneSide extrude, distance=25.55875
        extrude(amount=25.55875)
    return part.part


def model_21646_a2dd0d00_0058():
    """Model: Saturn Lantern Trundles v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0197932609, perimeter: 0.4987278338
            Circle(0.079375)
        # OneSide extrude, distance=6.2484
        extrude(amount=6.2484)
    return part.part


def model_21646_a2dd0d00_0062():
    """Model: Below Mercury v1 v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.9668714077, perimeter: 9.1017829661
            with BuildLine():
                CenterArc((0, 0), 1.27, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.17859375, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.635
        extrude(amount=0.635)
    return part.part


def model_21646_a2dd0d00_0063():
    """Model: Below Venus v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.9668714077, perimeter: 9.1017829661
            with BuildLine():
                CenterArc((0, 0), 1.27, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.17859375, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.27
        extrude(amount=1.27)
    return part.part


def model_21646_a2dd0d00_0069():
    """Model: Earth Tube v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0742247284, perimeter: 3.7404587532
            with BuildLine():
                CenterArc((0, 0), 0.3175, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.2778125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=15.08125
        extrude(amount=15.08125)
    return part.part


def model_21646_a2dd0d00_0071():
    """Model: Below Mars v2 (2)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.6662612577, perimeter: 10.223920592
            with BuildLine():
                CenterArc((0, 0), 1.27, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.3571875, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.3175
        extrude(amount=0.3175)
    return part.part


def model_21646_a2dd0d00_0073():
    """Model: Drive Wheel Peg v1 (6)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1433365246, perimeter: 1.5803170258
            with BuildLine():
                Line((-0.254, 0), (0.254, 0))
                Line((-0.254, -0.2821585129), (-0.254, 0))
                Line((0.254, -0.2821585129), (-0.254, -0.2821585129))
                Line((0.254, 0), (0.254, -0.2821585129))
            make_face()
            # Profile area: 0.1827953333, perimeter: 1.7780085803
            with BuildLine():
                Line((0.254, 0), (0.108052939, 0.508))
                Line((0.108052939, 0.508), (-0.1036137277, 0.508))
                Line((-0.1036137277, 0.508), (-0.254, 0))
                Line((-0.254, 0), (0.254, 0))
            make_face()
        # OneSide extrude, distance=1.27
        extrude(amount=1.27)
    return part.part


def model_21646_a2dd0d00_0074():
    """Model: Drive Wheel Peg v1 (1) (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2688166667, perimeter: 2.1853642095
            with BuildLine():
                Line((0.3175, 0), (0.1058333333, 0.635))
                Line((0.1058333333, 0.635), (-0.1058333333, 0.635))
                Line((-0.1058333333, 0.635), (-0.3175, 0))
                Line((-0.3175, 0), (0.3175, 0))
            make_face()
            # Profile area: 0.1791706557, perimeter: 1.8343170258
            with BuildLine():
                Line((-0.3175, 0), (0.3175, 0))
                Line((-0.3175, -0.2821585129), (-0.3175, 0))
                Line((0.3175, -0.2821585129), (-0.3175, -0.2821585129))
                Line((0.3175, 0), (0.3175, -0.2821585129))
            make_face()
        # OneSide extrude, distance=1.27
        extrude(amount=1.27)
    return part.part


def model_21646_a2dd0d00_0075():
    """Model: Venus Tube v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0643280979, perimeter: 3.2417309194
            with BuildLine():
                CenterArc((0, 0), 0.2778125, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.238125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=18.0975
        extrude(amount=18.0975)
    return part.part


def model_21647_6b6cca6f_0003():
    """Model: Blower Front Plate v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 849.0154146326, perimeter: 147.6548547187
            with BuildLine():
                CenterArc((0, 0), 17.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 6, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)
    return part.part


def model_21649_3ef60555_0001():
    """Model: Final 1/2 Ply v4"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 84.1226971647, perimeter: 197.1454316511
            with BuildLine():
                CenterArc((-1.5854995672, 23.6923026355), 3.0412652747, -89.4340391017, 180.4097512193)
                CenterArc((-1.081609047, 21.874862485), 4.8899399316, 96.5250250064, 85.3249744527)
                CenterArc((-0.7726046216, 22.1110600552), 5.211315543, -175.6633771853, 71.6615170976)
                CenterArc((-0.4017326735, 22.7570530658), 5.931342247, -105.9685281008, 58.6279976715)
                CenterArc((7.5137020732, 18.6339869001), 3.9034340523, -176.4925120661, 88.0529814977)
                CenterArc((7.5333399408, 18.6641238168), 3.9330781865, -88.737459264, 79.8970873949)
                CenterArc((9.5444457379, 18.1391717543), 1.8769328242, -2.4273136565, 91.657602225)
                CenterArc((9.5262928074, 18.1723096147), 1.8441355797, 88.6525022372, 105.0395180368)
                CenterArc((9.0165856558, 17.7448371828), 1.2820538291, 86.5740212552, 93.829971237)
                CenterArc((9.5625861849, 18.1651973084), 0.9792323958, -26.4389622295, 145.0813366894)
                CenterArc((7.4805221265, 18.7095275586), 3.1170498979, -87.4353450448, 69.1044114561)
                CenterArc((7.5615075739, 18.6417338976), 3.0466956237, 159.9752731138, 111.1247940408)
                CenterArc((-2.6114212422, 23.5056941463), 8.2486338196, -27.5932138395, 40.8754483871)
                CenterArc((-2.9403094331, 23.5317909311), 8.563323791, 12.6067116339, 45.2560176418)
                CenterArc((-2.1064959763, 25.4530080487), 6.500618435, 55.076993682, 34.2663918874)
                CenterArc((-2.0952557474, 25.4811150959), 6.4723936298, 89.4400299692, 57.3465977109)
                CenterArc((4.4617016243, 22.4404954428), 13.6639375613, 151.1843220413, 44.7027378526)
                CenterArc((22.6822632534, 27.5257811364), 32.5807310498, -164.2829759772, 12.7137615656)
                Line((-5.3847999349, 11.6077998597), (-5.9689999279, 12.0141998548))
                Line((-5.3593999352, 10.921999868), (-5.3847999349, 11.6077998597))
                CenterArc((23.7638135345, 27.9744517435), 33.748298887, -149.6498396593, 25.2536706)
                CenterArc((8.0060429667, 3.1741815484), 4.4968708627, -164.6412753401, 27.2994219204)
                CenterArc((23.4812643825, 27.7250534025), 32.4829447526, -148.8494569124, 21.2668613138)
                CenterArc((22.9879766384, 27.6297449279), 32.0119524027, -164.2599497375, 15.721218665)
                CenterArc((6.7954608911, 22.8764053227), 15.1382637752, -175.9931187095, 11.0424082021)
                CenterArc((4.4394516326, 22.409632928), 12.7589481092, 151.1041386814, 31.5509258095)
                CenterArc((-2.0872039667, 25.5092116954), 5.564522182, 81.5550156284, 65.0125790364)
                CenterArc((-2.6860235651, 23.8769237387), 7.275603814, 27.207194353, 51.5699139053)
                CenterArc((-2.3608857682, 23.5873906978), 7.1303937942, -31.1929587062, 61.6655499564)
                CenterArc((-0.4081425589, 22.7224041663), 5.0193119966, -113.7807926005, 79.4878752078)
                CenterArc((-0.7935139303, 22.1263278595), 4.3199086853, -172.8681875403, 60.5768922752)
                CenterArc((-1.1313970018, 21.9102463912), 3.961568405, 97.574224492, 87.0625174425)
                CenterArc((-1.6372879534, 23.6767221615), 2.1605890789, -30.9326326901, 121.364497536)
                CenterArc((-1.8667120429, 22.7159585492), 2.0881009004, -81.4275182445, 77.3123919575)
            make_face()
        # OneSide extrude, distance=1.27
        extrude(amount=1.27)
    return part.part


def model_21680_360ba5c7_0000():
    """Model: High-Speed-Oil-Seal-16 v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 10.7579064887, perimeter: 26.8914047962
            with BuildLine():
                CenterArc((0, 0), 2.54, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.7399, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.762
        extrude(amount=0.762)
    return part.part


def model_21680_360ba5c7_0004():
    """Model: High-Speed-Lockwasher-12 v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 9.0922323281, perimeter: 19.7496222168
            with BuildLine():
                CenterArc((0, 0), 2.032, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.11125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.254
        extrude(amount=0.254)
    return part.part


def model_21680_360ba5c7_0006():
    """Model: Hex-Nut-11 v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 4 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 5.7454311261, perimeter: 18.5306384321
            with BuildLine():
                Line((0.96237073, 1.666875), (-0.96237073, 1.666875))
                Line((-0.96237073, 1.666875), (-1.9247414599, 0))
                Line((-1.9247414599, 0), (-0.96237073, -1.666875))
                Line((-0.96237073, -1.666875), (0.96237073, -1.666875))
                Line((0.96237073, -1.666875), (1.9247414599, 0))
                Line((1.9247414599, 0), (0.96237073, 1.666875))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.11125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.27
        extrude(amount=1.27)
    return part.part


def model_21680_360ba5c7_0011():
    """Model: Slow-Speed-Oil-Seal-17 v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 6.4757773207, perimeter: 19.9570929956
            with BuildLine():
                CenterArc((0, 0), 1.91262, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.26365, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.508
        extrude(amount=0.508)
    return part.part


def model_21695_1f33863f_0000():
    """Model: 6. Washer v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.3052203171, perimeter: 6.4954313069
            with BuildLine():
                CenterArc((0, 0), 0.56388, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.4699, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.0127
        extrude(amount=0.0127)
    return part.part


def model_21695_1f33863f_0003():
    """Model: 3. Parker O-Ring v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.7125573925, perimeter: 8.9771010076
            with BuildLine():
                CenterArc((0, 0), 0.79375, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.635, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.15875
        extrude(amount=0.15875)
    return part.part


def model_21695_1f33863f_0005():
    """Model: 2.1 Main Body v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.2173390937, perimeter: 8.3766190019
            with BuildLine():
                Line((0.3240475541, 0.78232), (-0.3240475541, 0.78232))
                Line((-0.3240475541, 0.78232), (-0.78232, 0.3240475541))
                Line((-0.78232, 0.3240475541), (-0.78232, -0.3240475541))
                Line((-0.78232, -0.3240475541), (-0.3240475541, -0.78232))
                Line((-0.3240475541, -0.78232), (0.3240475541, -0.78232))
                Line((0.3240475541, -0.78232), (0.78232, -0.3240475541))
                Line((0.78232, -0.3240475541), (0.78232, 0.3240475541))
                Line((0.78232, 0.3240475541), (0.3240475541, 0.78232))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.508, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.8107319666, perimeter: 3.191858136
            Circle(0.508)
        # OneSide extrude, distance=7.874
        extrude(amount=7.874)
    return part.part


def model_21702_3390d14a_0001():
    """Model: Pump Lever Linkage v1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 18 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 2.6528967199, perimeter: 18.7419121369
            with BuildLine():
                Line((-0.4828822128, 6.4817606588), (-0.4828822128, 8.85))
                Line((-0.4828822128, 8.85), (-0.7828822128, 8.85))
                Line((-0.7828822128, 8.85), (-0.7828822128, 6.5691174789))
                CenterArc((-0.4091822128, 6.5691174789), 0.3737, 180, 32.47)
                Line((-0.7244626857, 6.3684936682), (-0.011521325, 5.2481057711))
                CenterArc((-0.0737, 5.2085393412), 0.0737, 0, 32.47)
                Line((0, 5.2085393412), (0, 0))
                Line((0, 0), (0.3, 0))
                Line((0.3, 0), (0.3, 5.1211820538))
                CenterArc((-0.0737, 5.1211825211), 0.3737, -0.000071658, 32.4701433024)
                Line((0.241580222, 5.321806726), (-0.4713608878, 6.4421942289))
                CenterArc((-0.4091822128, 6.4817606588), 0.0737, 180, 32.47)
            make_face()
        # OneSide extrude, distance=1.6
        extrude(amount=1.6)
    return part.part


def model_21702_3390d14a_0002():
    """Model: Pump - Back-up Ring v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.3847665602, perimeter: 6.6915923521
            with BuildLine():
                CenterArc((0, 0), 0.59, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.475, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.14
        extrude(amount=0.14)
    return part.part


def model_21702_3390d14a_0006():
    """Model: Pump Washer-Gasket v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.0518527019, perimeter: 8.6393797974
            with BuildLine():
                CenterArc((0, 0), 0.925, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.45, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


def model_21710_0b9db742_0002():
    """Model: Schottblech v2 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 11 constraints, 13 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 327.87175, perimeter: 80.8503466361
            with BuildLine():
                Line((0, 0), (0, 11.7))
                Line((0, 11.7), (-11.5, 11.7))
                Line((-11.5, 11.7), (-11.5, 8.35))
                Line((-20, -3.7889999997), (-11.5, 8.35))
                Line((-20, -3.7889999997), (-20, -11.2499999997))
                Line((-17.4999999997, -13.4999999997), (-20, -11.2499999997))
                Line((-7.4999999997, -13.4999999997), (-17.4999999997, -13.4999999997))
                Line((-7.4999999997, -3.9999999997), (-7.4999999997, -13.4999999997))
                Line((-3.5, 0), (-7.4999999997, -3.9999999997))
                Line((0, 0), (-3.5, 0))
            make_face()
        # OneSide extrude, distance=3
        extrude(amount=3)
    return part.part


def model_21710_0b9db742_0005():
    """Model: Gleitlagerbuchse v3 (1) (2)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.638937829, perimeter: 26.3893782902
            with BuildLine():
                CenterArc((0, 0), 2.2, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=3
        extrude(amount=3)
    return part.part


def model_21717_14f4c79a_0000():
    """Model: Turbin Blade Cutting tool v1"""
    with BuildPart() as part:
        # Sketch4 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 15 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0225091402, perimeter: 0.8086948657
            with BuildLine():
                CenterArc((-0.1269999543, -0.0771362412), 0.03175, 31.2734996099, 180.0000588237)
                CenterArc((0, 0), 0.18034, -148.7266283558, 117.4533641909)
                CenterArc((0.1270000457, -0.0771360908), 0.03175, -31.2732655519, 180.0000835347)
                CenterArc((0, 0), 0.11684, -148.7267138884, 117.4534277768)
            make_face()
        # OneSide extrude, distance=0.3175
        extrude(amount=0.3175)
    return part.part


def model_21732_adaf1650_0000():
    """Model: Crankshaft v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.1309733553, perimeter: 3.7699111843
            Circle(0.6)
        # OneSide extrude, distance=10.6
        extrude(amount=10.6)
    return part.part


def model_21734_7cf58bd0_0007():
    """Model: PISTON  v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 5.9150759738, perimeter: 10.5419283084
            with BuildLine():
                CenterArc((0, 0), 1.4, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.2778, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.9652
        extrude(amount=0.9652)
    return part.part


def model_21734_7cf58bd0_0013():
    """Model: Part 34C v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 2.3891247228, perimeter: 9.3435011088
            with BuildLine():
                Line((0, 0), (0.6, 0))
                Line((0.6, 0), (0.6, 4.05))
                CenterArc((0.3, 4.45), 0.5, -126.8698976458, 73.7397952917)
                Line((0, 4.05), (0, 0))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


def model_21736_fc59650e_0013():
    """Model: rpl006 v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 11 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 39.8926990817, perimeter: 27.5707963268
            with BuildLine():
                Line((5, 2), (-5, 2))
                Line((-5, 2), (-5, -1.5))
                CenterArc((-4.5, -1.5), 0.5, 180, 90)
                Line((-4.5, -2), (4.5, -2))
                CenterArc((4.5, -1.5), 0.5, -90, 90)
                Line((5, -1.5), (5, 2))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


def model_21736_fc59650e_0022():
    """Model: DIn6855 a6x6x12 v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 13 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.1413716694, perimeter: 1.5424777961
            with BuildLine():
                CenterArc((0, 0), 0.3, 90, 180)
                Line((0, 0), (0, -0.3))
                Line((0, 0), (0, 0.3))
            make_face()
            # Profile area: 0.0551883306, perimeter: 1.6528777961
            with BuildLine():
                CenterArc((0, 0), 0.3, 0, 90)
                Line((0.3, 0), (0.3552, 0))
                CenterArc((0.6552, 0), 0.3, 90, 90)
                Line((0.6552, 0.3), (0, 0.3))
            make_face()
            # Profile area: 0.1413716694, perimeter: 1.5424777961
            with BuildLine():
                Line((0.6552, 0), (0.6552, 0.3))
                Line((0.6552, 0), (0.6552, -0.3))
                CenterArc((0.6552, 0), 0.3, -90, 180)
            make_face()
            # Profile area: 0.0551883306, perimeter: 1.6528777961
            with BuildLine():
                CenterArc((0.6552, 0), 0.3, -180, 90)
                Line((0.3, 0), (0.3552, 0))
                CenterArc((0, 0), 0.3, -90, 90)
                Line((0, -0.3), (0.6552, -0.3))
            make_face()
            # Profile area: 0.0706858347, perimeter: 1.071238898
            with BuildLine():
                CenterArc((0, 0), 0.3, -90, 90)
                Line((0, 0), (0.3, 0))
                Line((0, 0), (0, -0.3))
            make_face()
            # Profile area: 0.0706858347, perimeter: 1.071238898
            with BuildLine():
                Line((0, 0), (0, 0.3))
                Line((0, 0), (0.3, 0))
                CenterArc((0, 0), 0.3, 0, 90)
            make_face()
            # Profile area: 0.0706858347, perimeter: 1.071238898
            with BuildLine():
                Line((0.6552, 0), (0.6552, -0.3))
                Line((0.3552, 0), (0.6552, 0))
                CenterArc((0.6552, 0), 0.3, -180, 90)
            make_face()
            # Profile area: 0.0706858347, perimeter: 1.071238898
            with BuildLine():
                CenterArc((0.6552, 0), 0.3, 90, 90)
                Line((0.3552, 0), (0.6552, 0))
                Line((0.6552, 0), (0.6552, 0.3))
            make_face()
        # OneSide extrude, distance=0.6
        extrude(amount=0.6)
    return part.part


def model_21736_fc59650e_0025():
    """Model: DIN6855 8x7x16 v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 13 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.2513274123, perimeter: 2.0566370614
            with BuildLine():
                CenterArc((0, 0), 0.4, 90, 180)
                Line((0, 0), (0, -0.4))
                Line((0, 0), (0, 0.4))
            make_face()
            # Profile area: 0.0686725877, perimeter: 2.0566370614
            with BuildLine():
                CenterArc((0, 0), 0.4, 0, 90)
                CenterArc((0.8, 0), 0.4, 90, 90)
                Line((0, 0.4), (0.8, 0.4))
            make_face()
            # Profile area: 0.2513274123, perimeter: 2.0566370614
            with BuildLine():
                Line((0.8, 0), (0.8, 0.4))
                Line((0.8, 0), (0.8, -0.4))
                CenterArc((0.8, 0), 0.4, -90, 180)
            make_face()
            # Profile area: 0.0686725877, perimeter: 2.0566370614
            with BuildLine():
                CenterArc((0.8, 0), 0.4, -180, 90)
                CenterArc((0, 0), 0.4, -90, 90)
                Line((0, -0.4), (0.8, -0.4))
            make_face()
            # Profile area: 0.1256637061, perimeter: 1.4283185307
            with BuildLine():
                CenterArc((0, 0), 0.4, -90, 90)
                Line((0, 0), (0.4, 0))
                Line((0, 0), (0, -0.4))
            make_face()
            # Profile area: 0.1256637061, perimeter: 1.4283185307
            with BuildLine():
                Line((0, 0), (0, 0.4))
                Line((0, 0), (0.4, 0))
                CenterArc((0, 0), 0.4, 0, 90)
            make_face()
            # Profile area: 0.1256637061, perimeter: 1.4283185307
            with BuildLine():
                Line((0.8, 0), (0.8, -0.4))
                Line((0.4, 0), (0.8, 0))
                CenterArc((0.8, 0), 0.4, -180, 90)
            make_face()
            # Profile area: 0.1256637061, perimeter: 1.4283185307
            with BuildLine():
                CenterArc((0.8, 0), 0.4, 90, 90)
                Line((0.4, 0), (0.8, 0))
                Line((0.8, 0), (0.8, 0.4))
            make_face()
        # OneSide extrude, distance=0.7
        extrude(amount=0.7)
    return part.part


def model_21740_6f0c9bdb_0023():
    """Model: Piston Compression Ring v1 (1) (3)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 6 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.4072570452, perimeter: 19.0640745237
            with BuildLine():
                Line((0.1, -1.4465476141), (0.1, -1.5968719423))
                CenterArc((0, 0), 1.6, -86.4166783015, 352.8333566031)
                Line((-0.1, -1.5968719423), (-0.1, -1.4465476141))
                CenterArc((0, 0), 1.45, -86.0454278779, 352.0908557558)
            make_face()
        # OneSide extrude, distance=0.15
        extrude(amount=0.15)
    return part.part


def model_21773_01f6bc23_0015():
    """Model: packing v2 (3)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 11.3804193876, perimeter: 19.7920337176
            with BuildLine():
                CenterArc((0, 0), 2.15, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.9
        extrude(amount=0.9)
    return part.part


def model_21773_01f6bc23_0018():
    """Model: Bush v4 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 4.9008845396, perimeter: 16.3362817987
            with BuildLine():
                CenterArc((0, 0), 1.6, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=4
        extrude(amount=4)
    return part.part


def model_21785_d595ced5_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 56.05, perimeter: 30.8
            with BuildLine():
                Line((9.5, -5.9), (0, -5.9))
                Line((9.5, 0), (9.5, -5.9))
                Line((0, 0), (9.5, 0))
                Line((0, -5.9), (0, 0))
            make_face()
        # OneSide extrude, distance=1.8
        extrude(amount=1.8)
    return part.part


def model_21800_040f0143_0001():
    """Model: Top Right Arm v7"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 39 constraints, 23 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 42.5753546513, perimeter: 52.244489519
            with BuildLine():
                CenterArc((0.1905184627, 0.2539861519), 1.3765, 0, 114.7004025668)
                Line((-0.3846843509, 1.5045436169), (-3.1000000462, 0.352029941))
                Line((-13.1645630923, 0.352029941), (-3.1000000462, 0.352029941))
                CenterArc((-13.1645630923, 0.7650542728), 0.4130243318, -155.0087730478, 65.0087730478)
                CenterArc((-14.9777776099, -0.080138436), 1.5875, 24.9917135909, 56.4539220705)
                CenterArc((-14.6471953221, 2.1176380785), 0.6350000041, -149.6333634828, 51.0798757159)
                Line((-15.5741692788, 2.4437656316), (-15.1950785248, 1.7966256156))
                CenterArc((-15.8262097376, 2.2961241161), 0.2921, 30.3611312992, 169.290114688)
                Line((-16.056477504, 2.0724011016), (-16.1012969702, 2.1978926322))
                CenterArc((-16.3315604289, 1.9741575539), 0.2921000004, -135.4240436978, 155.0778023697)
                Line((-16.6331499723, 1.8640711253), (-16.5396292869, 1.7691459431))
                CenterArc((-16.8412294812, 1.6590703253), 0.2921, 44.5729794949, 174.1660149428)
                Line((-16.9856900069, 1.3723353309), (-17.0690688535, 1.4762818399))
                CenterArc((-17.2135472274, 1.1895690948), 0.2921, -108.0148722678, 146.7482717803)
                Line((-17.4306059571, 0.9529987677), (-17.3038831979, 0.9117889255))
                CenterArc((-17.5209379706, 0.6752173116), 0.2921, 71.9859439142, 181.4669484655)
                Line((-16.8851897536, 0.1816114119), (-17.6041290946, 0.3952143708))
                CenterArc((-17.0180236765, -0.2654897239), 0.4664164198, 6.0308535563, 67.4224412704)
                CenterArc((-14.975433863, -0.0500843643), 1.5875, -173.9832025435, 78.5629788001)
                Line((-15.1253815373, -1.3129861519), (-15.1253886556, -1.6304861518))
                Line((-14.9665815373, -1.3129861519), (-15.1253815373, -1.3129861519))
                Line((-14.9665815373, -1.6304861519), (-14.9665815373, -1.3129861519))
                Line((-0.7392815373, -1.6304861519), (-14.9665815373, -1.6304861519))
                Line((-0.7392815373, -1.3129861519), (-0.7392815373, -1.6304861519))
                Line((-0.5804815373, -1.3129861519), (-0.7392815373, -1.3129861519))
                Line((-0.5804815373, -1.6304861519), (-0.5804815373, -1.3129861519))
                Line((0.1905184627, -1.6304861519), (-0.5804815373, -1.6304861519))
                CenterArc((0.1905184627, -0.2539861519), 1.3765, -90, 90)
                Line((0.1905184627, -0.2539861519), (1.5670184627, -0.2539861519))
                CenterArc((0, 0), 0.3175, 53.125937533, 253.7481249341)
                Line((1.5670184627, 0.2539861519), (0.1905184627, 0.2539861519))
            make_face()
            with BuildLine():
                CenterArc((-15.24, 0), 0.3175, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=3.4163
        extrude(amount=3.4163)
    return part.part


def model_21800_040f0143_0004():
    """Model: Bottom Left Arm   v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 40 constraints, 20 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 47.4253575711, perimeter: 52.902139368
            with BuildLine():
                CenterArc((0.1905184627, 0.2539861519), 1.3765, 0, 114.6917402728)
                Line((-0.3844952782, 1.5046305649), (-3.0830569648, 0.6453779387))
                Line((-13.0339031367, 0.6453779387), (-3.0830569648, 0.6453779387))
                CenterArc((-13.0339031137, 1.2720711296), 0.6266931909, -157.0556041838, 67.0556020761)
                CenterArc((-15.072916933, 0.4088943625), 1.5875, 22.9444338591, 56.8275105415)
                CenterArc((-14.678274796, 2.5960763437), 0.6350005333, -151.6570291211, 51.4289528105)
                Line((-15.5926086712, 2.9550280411), (-15.2371524482, 2.2946108445))
                CenterArc((-15.8498195457, 2.8165904159), 0.2921, 28.290300508, 169.4556577053)
                Line((-16.080958854, 2.5805011483), (-16.1280206399, 2.727559179))
                CenterArc((-16.3591603023, 2.4914710161), 0.2921000004, -137.3000045801, 155.0457352275)
                Line((-16.6785404823, 2.4068546199), (-16.5738288716, 2.2933805935))
                CenterArc((-16.8932091687, 2.2087643247), 0.2921, 42.6999614788, 174.0432860782)
                Line((-17.0349068225, 1.9102925146), (-17.1272760029, 2.034021293))
                CenterArc((-17.2689731648, 1.7355488239), 0.2921, -109.9142567063, 146.6576655612)
                Line((-17.5136387718, 1.5135067592), (-17.3684663705, 1.4609154101))
                CenterArc((-17.6131305862, 1.2388728413), 0.2921, 70.0860335569, 179.1989093444)
                Line((-17.0149390617, 0.7003662861), (-17.7164523917, 0.965656783))
                CenterArc((-17.3513202962, -0.1895587381), 0.9513773495, -0.6288276921, 69.9228228106)
                CenterArc((-14.9779100206, -0.2159728476), 1.422179924, 179.3564837974, 84.691589008)
                Line((-15.1253815373, -1.3129861519), (-15.1253815373, -1.6304861519))
                Line((-14.9665815373, -1.3129861519), (-15.1253815373, -1.3129861519))
                Line((-14.9665815373, -1.6304861519), (-14.9665815373, -1.3129861519))
                Line((-0.7392815373, -1.6304861519), (-14.9665815373, -1.6304861519))
                Line((-0.7392815373, -1.3129861519), (-0.7392815373, -1.6304861519))
                Line((-0.5804815373, -1.3129861519), (-0.7392815373, -1.3129861519))
                Line((-0.5804815373, -1.6304861519), (-0.5804815373, -1.3129861519))
                Line((0.1905184627, -1.6304861519), (-0.5804815373, -1.6304861519))
                CenterArc((0.1905184627, -0.2539861519), 1.3765, -90, 90)
                Line((0.1905184627, -0.2539861519), (1.5670184627, -0.2539861519))
                CenterArc((0, 0), 0.3175, 53.125937533, 253.7481249341)
                Line((1.5670184627, 0.2539861519), (0.1905184627, 0.2539861519))
            make_face()
            with BuildLine():
                CenterArc((-15.24, 0), 0.3175, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=3.81
        extrude(amount=3.81)
    return part.part


def model_21800_040f0143_0007():
    """Model: Top Left Arm  v6"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 40 constraints, 20 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 47.4253575711, perimeter: 52.902139368
            with BuildLine():
                CenterArc((0.1905184627, 0.2539861519), 1.3765, 0, 114.6917402728)
                Line((-0.3844952782, 1.5046305649), (-3.0830569648, 0.6453779387))
                Line((-13.0339031367, 0.6453779387), (-3.0830569648, 0.6453779387))
                CenterArc((-13.0339031137, 1.2720711296), 0.6266931909, -157.0556041838, 67.0556020761)
                CenterArc((-15.072916933, 0.4088943625), 1.5875, 22.9444338591, 56.8275105415)
                CenterArc((-14.678274796, 2.5960763437), 0.6350005333, -151.6570291211, 51.4289528105)
                Line((-15.5926086712, 2.9550280411), (-15.2371524482, 2.2946108445))
                CenterArc((-15.8498195457, 2.8165904159), 0.2921, 28.290300508, 169.4556577053)
                Line((-16.080958854, 2.5805011483), (-16.1280206399, 2.727559179))
                CenterArc((-16.3591603023, 2.4914710161), 0.2921000004, -137.3000045801, 155.0457352275)
                Line((-16.6785404823, 2.4068546199), (-16.5738288716, 2.2933805935))
                CenterArc((-16.8932091687, 2.2087643247), 0.2921, 42.6999614788, 174.0432860782)
                Line((-17.0349068225, 1.9102925146), (-17.1272760029, 2.034021293))
                CenterArc((-17.2689731648, 1.7355488239), 0.2921, -109.9142567063, 146.6576655612)
                Line((-17.5136387718, 1.5135067592), (-17.3684663705, 1.4609154101))
                CenterArc((-17.6131305862, 1.2388728413), 0.2921, 70.0860335569, 179.1989093444)
                Line((-17.0149390617, 0.7003662861), (-17.7164523917, 0.965656783))
                CenterArc((-17.3513202962, -0.1895587381), 0.9513773495, -0.6288276921, 69.9228228106)
                CenterArc((-14.9779100206, -0.2159728476), 1.422179924, 179.3564837974, 84.691589008)
                Line((-15.1253815373, -1.3129861519), (-15.1253815373, -1.6304861519))
                Line((-14.9665815373, -1.3129861519), (-15.1253815373, -1.3129861519))
                Line((-14.9665815373, -1.6304861519), (-14.9665815373, -1.3129861519))
                Line((-0.7392815373, -1.6304861519), (-14.9665815373, -1.6304861519))
                Line((-0.7392815373, -1.3129861519), (-0.7392815373, -1.6304861519))
                Line((-0.5804815373, -1.3129861519), (-0.7392815373, -1.3129861519))
                Line((-0.5804815373, -1.6304861519), (-0.5804815373, -1.3129861519))
                Line((0.1905184627, -1.6304861519), (-0.5804815373, -1.6304861519))
                CenterArc((0.1905184627, -0.2539861519), 1.3765, -90, 90)
                Line((0.1905184627, -0.2539861519), (1.5670184627, -0.2539861519))
                CenterArc((0, 0), 0.3175, 53.125937533, 253.7481249341)
                Line((1.5670184627, 0.2539861519), (0.1905184627, 0.2539861519))
            make_face()
            with BuildLine():
                CenterArc((-15.24, 0), 0.3175, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=3.4163
        extrude(amount=3.4163)
    return part.part


def model_21822_7d3db422_0000():
    """Model: Pipe 1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1001382658, perimeter: 2.6703537556
            with BuildLine():
                CenterArc((-2, 0), 0.25, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-2, 0), 0.175, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=3.5
        extrude(amount=3.5)
    return part.part


def model_21822_7d3db422_0005():
    """Model: Piston Rod"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((-15, -15)):
                Circle(0.25)
        # OneSide extrude, distance=12.4
        extrude(amount=12.4)
    return part.part


def model_21822_7d3db422_0010():
    """Model: Piston Ring"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.7225663103, perimeter: 14.4513262065
            with BuildLine():
                CenterArc((-20, -15), 1.2, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-20, -15), 1.1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)
    return part.part


def model_21822_7d3db422_0023():
    """Model: Pipe 2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1001382658, perimeter: 2.6703537556
            with BuildLine():
                CenterArc((-4.0000000596, 0), 0.25, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-4.0000000596, 0), 0.175, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=19
        extrude(amount=19)
    return part.part


def model_21822_7d3db422_0024():
    """Model: Pipe 5"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1001382658, perimeter: 2.6703537556
            with BuildLine():
                CenterArc((-7.0000001043, 0), 0.25, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-7.0000001043, 0), 0.175, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=2
        extrude(amount=2)
    return part.part


def model_21822_7d3db422_0025():
    """Model: Pipe 6"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1001382658, perimeter: 2.6703537556
            with BuildLine():
                CenterArc((-8.0000001192, 0), 0.25, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-8.0000001192, 0), 0.175, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


def model_21822_7d3db422_0026():
    """Model: Steam Chest Cover"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 19 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.8607176539, perimeter: 8.4102875206
            with BuildLine():
                Line((-11.6, 5.6), (-11.6, 5))
                Line((-13.2, 5.6), (-11.6, 5.6))
                Line((-13.2, 3.3), (-13.2, 5.6))
                Line((-13.2, 3.3), (-12.6, 3.3))
                Line((-12.6, 4.775), (-12.6, 3.3))
                CenterArc((-12.6, 5), 0.225, 0, 270)
                Line((-11.6, 5), (-12.375, 5))
            make_face()
            # Profile area: 1.8607176539, perimeter: 8.4102875206
            with BuildLine():
                Line((-12.375, 1.6), (-11.6, 1.6))
                CenterArc((-12.6, 1.6), 0.225, 90, 270)
                Line((-12.6, 3.3), (-12.6, 1.825))
                Line((-13.2, 3.3), (-12.6, 3.3))
                Line((-13.2, 1), (-13.2, 3.3))
                Line((-11.6, 1), (-13.2, 1))
                Line((-11.6, 1.6), (-11.6, 1))
            make_face()
            # Profile area: 1.8607176539, perimeter: 8.4102875206
            with BuildLine():
                Line((-11.6, 1.6), (-10.825, 1.6))
                Line((-11.6, 1.6), (-11.6, 1))
                Line((-10, 1), (-11.6, 1))
                Line((-10, 3.3), (-10, 1))
                Line((-10.6, 3.3), (-10, 3.3))
                Line((-10.6, 1.825), (-10.6, 3.3))
                CenterArc((-10.6, 1.6), 0.225, 180, 270)
            make_face()
            # Profile area: 1.8607176539, perimeter: 8.4102875206
            with BuildLine():
                Line((-10.6, 3.3), (-10, 3.3))
                Line((-10, 5.6), (-10, 3.3))
                Line((-11.6, 5.6), (-10, 5.6))
                Line((-11.6, 5.6), (-11.6, 5))
                Line((-10.825, 5), (-11.6, 5))
                CenterArc((-10.6, 5), 0.225, -90, 270)
                Line((-10.6, 3.3), (-10.6, 4.775))
            make_face()
            # Profile area: 1.660239218, perimeter: 5.3034291735
            with BuildLine():
                Line((-11.6, 5), (-11.6, 3.3))
                Line((-11.6, 5), (-12.375, 5))
                CenterArc((-12.6, 5), 0.225, -90, 90)
                Line((-12.6, 4.775), (-12.6, 3.3))
                Line((-12.6, 3.3), (-11.6, 3.3))
            make_face()
            # Profile area: 1.660239218, perimeter: 5.3034291735
            with BuildLine():
                Line((-10.6, 3.3), (-10.6, 4.775))
                CenterArc((-10.6, 5), 0.225, 180, 90)
                Line((-10.825, 5), (-11.6, 5))
                Line((-11.6, 5), (-11.6, 3.3))
                Line((-11.6, 3.3), (-10.6, 3.3))
            make_face()
            # Profile area: 1.660239218, perimeter: 5.3034291735
            with BuildLine():
                Line((-12.6, 3.3), (-11.6, 3.3))
                Line((-12.6, 3.3), (-12.6, 1.825))
                CenterArc((-12.6, 1.6), 0.225, 0, 90)
                Line((-12.375, 1.6), (-11.6, 1.6))
                Line((-11.6, 3.3), (-11.6, 1.6))
            make_face()
            # Profile area: 1.660239218, perimeter: 5.3034291735
            with BuildLine():
                CenterArc((-10.6, 1.6), 0.225, 90, 90)
                Line((-10.6, 1.825), (-10.6, 3.3))
                Line((-11.6, 3.3), (-10.6, 3.3))
                Line((-11.6, 3.3), (-11.6, 1.6))
                Line((-11.6, 1.6), (-10.825, 1.6))
            make_face()
        # OneSide extrude, distance=0.4
        extrude(amount=0.4)
    return part.part


def model_21822_7d3db422_0033():
    """Model: Steam Chest"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 15 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.5905863315, perimeter: 16.6840704497
            with BuildLine():
                Line((-13, 14.6), (-13, 10))
                Line((-13, 10), (-11.4, 10))
                Line((-11.4, 10.9), (-11.4, 10))
                Line((-11.9, 10.9), (-11.4, 10.9))
                CenterArc((-11.9, 11.3), 0.4, -180, 90)
                Line((-12.3, 13.3), (-12.3, 11.3))
                CenterArc((-11.9, 13.3), 0.4, 90, 90)
                Line((-11.4, 13.7), (-11.9, 13.7))
                Line((-11.4, 14.6), (-11.4, 13.7))
                Line((-11.4, 14.6), (-13, 14.6))
            make_face()
            with BuildLine():
                CenterArc((-12.4, 14), 0.225, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-12.4, 10.6), 0.225, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.8
        extrude(amount=1.8)
    return part.part


def model_21822_7d3db422_0037():
    """Model: Pipe 3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1001382658, perimeter: 2.6703537556
            with BuildLine():
                CenterArc((-5, 0), 0.25, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-5, 0), 0.175, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=6
        extrude(amount=6)
    return part.part


def model_21822_7d3db422_0039():
    """Model: Pipe 4"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1001382658, perimeter: 2.6703537556
            with BuildLine():
                CenterArc((-6.0000000894, 0), 0.25, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-6.0000000894, 0), 0.175, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=4
        extrude(amount=4)
    return part.part


def model_21822_7d3db422_0042():
    """Model: Rod 2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            Circle(0.2)
        # OneSide extrude, distance=2.6
        extrude(amount=2.6)
    return part.part


def model_21822_7d3db422_0043():
    """Model: Valve Plate"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 35 constraints, 14 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 13.1517699728, perimeter: 28.8823002362
            with BuildLine():
                Line((-15.9, -12.3), (-15.9, -7.7))
                Line((-15.9, -7.7), (-19.1, -7.7))
                Line((-19.1, -7.7), (-19.1, -12.3))
                Line((-19.1, -12.3), (-15.9, -12.3))
            make_face()
            with BuildLine():
                CenterArc((-18.5, -8.3), 0.225, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-16.5, -8.3), 0.225, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-18.5, -11.7), 0.225, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-16.5, -11.7), 0.225, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((-17.9000002667, -10.35), (-17.1000002548, -10.35))
                CenterArc((-17.1000002548, -10.5), 0.15, -90, 180)
                Line((-17.1000002548, -10.65), (-17.9000002667, -10.65))
                CenterArc((-17.9000002667, -10.5), 0.15, 90, 180)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((-17.9000002667, -9.85), (-17.1000002548, -9.85))
                CenterArc((-17.1000002548, -10), 0.15, -90, 180)
                Line((-17.1000002548, -10.15), (-17.9000002667, -10.15))
                CenterArc((-17.9000002667, -10), 0.15, 90, 180)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((-17.9000002667, -9.35), (-17.1000002548, -9.35))
                CenterArc((-17.1000002548, -9.5), 0.15, -90, 180)
                Line((-17.1000002548, -9.65), (-17.9000002667, -9.65))
                CenterArc((-17.9000002667, -9.5), 0.15, 90, 180)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)
    return part.part


def model_21822_7d3db422_0049():
    """Model: Floor"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1250, perimeter: 150
            with BuildLine():
                Line((25, -50), (-25, -50))
                Line((25, -25), (25, -50))
                Line((-25, -25), (25, -25))
                Line((-25, -50), (-25, -25))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


def model_21847_b2de7eb8_0001():
    """Model: 12A"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.7147123287, perimeter: 4.0840704497
            with BuildLine():
                CenterArc((0, 0), 0.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.45
        extrude(amount=0.45)
    return part.part


def model_21847_b2de7eb8_0007():
    """Model: 03A"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 3.96, perimeter: 7.8984845005
            with BuildLine():
                Line((0, -1.6), (0, -0.4))
                Line((0, -1.6), (1.6, -2))
                Line((2.3, -2), (1.6, -2))
                Line((2.3, -2), (2.3, 0))
                Line((2.3, 0), (1.6, 0))
                Line((0, -0.4), (1.6, 0))
            make_face()
        # OneSide extrude, distance=0.05
        extrude(amount=0.05)
    return part.part


def model_21863_eb40d2d8_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 19.6349540849, perimeter: 15.7079632679
            with Locations((-25, 0)):
                Circle(2.5)
        # Symmetric extrude, each_side=65
        extrude(amount=65, both=True)
    return part.part


def model_21881_f3bee5e5_0004():
    """Model: Washer v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 6.2753313255, perimeter: 14.7654854719
            with BuildLine():
                CenterArc((0, 0), 1.6, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.75, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)
    return part.part


def model_21893_0500d043_0055():
    """Model: SPINA CILINDRICA v1 (3)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            Circle(0.25)
        # OneSide extrude, distance=2.4
        extrude(amount=2.4)
    return part.part


def model_21899_d55d6c08_0027():
    """Model: BSE025-1 v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 15 constraints, 9 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.5382696836, perimeter: 4.3635032939
            with BuildLine():
                CenterArc((0, 0), 2.6, 63.6570244557, 1.6551529207)
                Line((1.385, 2.33), (1.1537330714, 2.33))
                CenterArc((1.635, 2.33), 0.25, -115.7880482314, 295.7880482314)
                CenterArc((0, 0), 2.6, 44.5718593503, 9.4826673475)
                CenterArc((1.635, 2.33), 0.55, -66.7437624777, 217.3434114675)
                CenterArc((1.635, 2.33), 0.55, 150.5996489898, 26.0281502146)
            make_face()
            # Profile area: 0.5382696836, perimeter: 4.3635032939
            with BuildLine():
                CenterArc((-1.635, 2.33), 0.25, 0, 295.7880482314)
                Line((-1.1537330714, 2.33), (-1.385, 2.33))
                CenterArc((0, 0), 2.6, 114.6878226236, 1.6551529207)
                CenterArc((-1.635, 2.33), 0.55, 3.3722007957, 26.0281502146)
                CenterArc((-1.635, 2.33), 0.55, 29.4003510102, 217.3434114675)
                CenterArc((0, 0), 2.6, 125.9454733022, 9.4826673475)
            make_face()
            # Profile area: 0.0166891323, perimeter: 0.7857503307
            with BuildLine():
                CenterArc((-1.635, 2.33), 0.25, -45.6720849581, 45.6720849581)
                CenterArc((0, 0), 2.6, 116.3429755443, 7.8275144268)
                Line((-1.1537330714, 2.33), (-1.385, 2.33))
            make_face()
            # Profile area: 0.0166891323, perimeter: 0.7857503307
            with BuildLine():
                CenterArc((0, 0), 2.6, 55.8295100288, 7.8275144268)
                CenterArc((1.635, 2.33), 0.25, 180, 45.6720849581)
                Line((1.385, 2.33), (1.1537330714, 2.33))
            make_face()
            # Profile area: 0.0903526154, perimeter: 2.5259842175
            with BuildLine():
                CenterArc((0, 0), 2.6, 90, 24.6878226236)
                Line((0, 2.6), (-1.155834058, 2.6))
                CenterArc((-1.635, 2.33), 0.55, 3.3722007957, 26.0281502146)
            make_face()
            # Profile area: 0.0011305486, perimeter: 0.1762123322
            with BuildLine():
                Line((-1.085, 2.33), (-1.1537330714, 2.33))
                CenterArc((-1.635, 2.33), 0.55, 0, 3.3722007957)
                CenterArc((0, 0), 2.6, 114.6878226236, 1.6551529207)
            make_face()
            # Profile area: 0.1978928724, perimeter: 2.0223214666
            with BuildLine():
                CenterArc((0, 0), 2.6, 116.3429755443, 7.8275144268)
                CenterArc((-1.635, 2.33), 0.25, -64.2119517686, 18.5398668105)
                CenterArc((0, 0), 2.6, 125.9454733022, 9.4826673475)
                CenterArc((-1.635, 2.33), 0.55, -113.2562375223, 113.2562375223)
                Line((-1.085, 2.33), (-1.1537330714, 2.33))
            make_face()
            # Profile area: 0.1978928724, perimeter: 2.0223214666
            with BuildLine():
                CenterArc((1.635, 2.33), 0.55, 180, 113.2562375223)
                CenterArc((0, 0), 2.6, 44.5718593503, 9.4826673475)
                CenterArc((1.635, 2.33), 0.25, -134.3279150419, 18.5398668105)
                CenterArc((0, 0), 2.6, 55.8295100288, 7.8275144268)
                Line((1.1537330714, 2.33), (1.085, 2.33))
            make_face()
            # Profile area: 9.0799881859, perimeter: 28.4957702873
            with BuildLine():
                CenterArc((0, 0), 2.6, 135.4281406497, 269.1437187005)
                CenterArc((1.635, 2.33), 0.55, 180, 113.2562375223)
                Line((1.085, 2.33), (-1.085, 2.33))
                CenterArc((-1.635, 2.33), 0.55, -113.2562375223, 113.2562375223)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.9, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0011305486, perimeter: 0.1762123322
            with BuildLine():
                Line((1.1537330714, 2.33), (1.085, 2.33))
                CenterArc((0, 0), 2.6, 63.6570244557, 1.6551529207)
                CenterArc((1.635, 2.33), 0.55, 176.6277992043, 3.3722007957)
            make_face()
            # Profile area: 0.0903526154, perimeter: 2.5259842175
            with BuildLine():
                CenterArc((0, 0), 2.6, 65.3121773764, 24.6878226236)
                CenterArc((1.635, 2.33), 0.55, 150.5996489898, 26.0281502146)
                Line((0, 2.6), (1.155834058, 2.6))
            make_face()
            # Profile area: 0.4175972547, perimeter: 4.4753373153
            with BuildLine():
                CenterArc((-1.635, 2.33), 0.55, 0, 3.3722007957)
                Line((1.085, 2.33), (-1.085, 2.33))
                CenterArc((1.635, 2.33), 0.55, 176.6277992043, 3.3722007957)
                CenterArc((0, 0), 2.6, 65.3121773764, 24.6878226236)
                CenterArc((0, 0), 2.6, 90, 24.6878226236)
            make_face()
        # OneSide extrude, distance=0.8
        extrude(amount=0.8)
    return part.part


def model_21899_d55d6c08_0029():
    """Model: BSE027-1 v1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.5890486225, perimeter: 4.7123889804
            with BuildLine():
                CenterArc((0, 0), 0.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


def model_21900_760d2078_0004():
    """Model: Backing Stay Bar v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.9401020657, perimeter: 4.0129824074
            with BuildLine():
                Line((0, 0.4340879858), (0, 0))
                Line((0, 0), (1.384, 0))
                Line((1.384, 0), (1.384, 0.4340879858))
                CenterArc((1.559, 1.008), 0.6, -163.0422367, 56.0844734)
                Line((0.9850879858, 0.833), (0.3989120142, 0.833))
                CenterArc((-0.175, 1.008), 0.6, -73.0422367, 56.0844734)
            make_face()
        # OneSide extrude, distance=0.13
        extrude(amount=0.13)
    return part.part


def model_21900_760d2078_0011():
    """Model: Screen v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 7.5985, perimeter: 11.99
            with BuildLine():
                Line((0, 1.82), (0, 0))
                Line((0, 0), (4.175, 0))
                Line((4.175, 0), (4.175, 1.82))
                Line((4.175, 1.82), (0, 1.82))
            make_face()
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)
    return part.part


def model_21901_64acc24c_0000():
    """Model: mgp3 v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.9604020085, perimeter: 15.5815636169
            with BuildLine():
                CenterArc((0, 0), 1.35, 96.3694770734, 347.2610458531)
                CenterArc((0, 1.35), 0.15, -3.1847385367, 186.3694770734)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=2.2
        extrude(amount=2.2)
    return part.part


def model_21908_385686ec_0000():
    """Model: 08A v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 19 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 27.2509733553, perimeter: 72.9699111843
            with BuildLine():
                CenterArc((10.4, 0.6), 0.6, -90, 90)
                Line((11, 0.6), (11, 8.3999993329))
                CenterArc((10.4, 8.4), 0.6, -0.0000637067, 90.0001274134)
                Line((10.3999993329, 9), (0.6, 9))
                CenterArc((0.6, 8.4), 0.6, 90, 90)
                Line((0, 8.4), (0, 0.6))
                CenterArc((0.6, 0.6), 0.6, -180, 90)
                Line((0.6, 0), (10.4, 0))
            make_face()
            with BuildLine():
                Line((10.2, 0.7), (0.8, 0.7))
                Line((0.8, 0.7), (0.8, 8.3))
                Line((0.8, 8.3), (10.2, 8.3))
                Line((10.2, 8.3), (10.2, 0.7))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.05
        extrude(amount=0.05)
    return part.part


def model_21908_385686ec_0001():
    """Model: 06A v4"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 5 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.8615009111, perimeter: 34.5621576345
            with BuildLine():
                Line((-4.6718925525, 3.9980428365), (-5.4999996518, 3.9980428365))
                Line((-5.4999996518, 3.9980428365), (-5.4999996518, 3.9480428365))
                Line((-5.4999996518, 3.9480428365), (-4.6999996598, 3.9481562248))
                Line((-4.6999996598, 3.9481562248), (-1.6636099749, -1.017301259))
                CenterArc((0, 0), 1.95, -148.5541198822, 117.1082397643)
                Line((4.6999996598, 3.9481562248), (1.6636099749, -1.017301259))
                Line((5.4999996518, 3.9480428365), (4.6999996598, 3.9481562248))
                Line((5.4999996518, 3.9980428365), (5.4999996518, 3.9480428365))
                Line((4.6718925525, 3.9980428365), (5.4999996518, 3.9980428365))
                Line((4.6718925525, 3.9980428365), (1.6193759708, -0.9937914597))
                CenterArc((0, 0), 1.9, -148.4630625226, 116.9261250453)
                Line((-4.6718925525, 3.9980428365), (-1.6193759708, -0.9937914597))
            make_face()
        # OneSide extrude, distance=7.7
        extrude(amount=7.7)
    return part.part


def model_21908_385686ec_0012():
    """Model: 01C v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 6 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.1500000022, perimeter: 3.2000000238
            with BuildLine():
                Line((0.8000000119, 0.1000000015), (0.8000000119, 0))
                Line((0.1, 0.1000000015), (0.8000000119, 0.1000000015))
                Line((0.1, 0.8), (0.1, 0.1000000015))
                Line((0, 0.8), (0.1, 0.8))
                Line((0, 0), (0, 0.8))
                Line((0.8000000119, 0), (0, 0))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


def model_21908_385686ec_0015():
    """Model: 12A v3 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.7147123287, perimeter: 4.0840704497
            with BuildLine():
                CenterArc((0, 0), 0.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


def model_21908_385686ec_0016():
    """Model: 01A v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 9 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.2200000021, perimeter: 4.599999997
            with BuildLine():
                Line((0, 0.7), (0, 0))
                Line((0, 0), (1, 0))
                Line((1, 0), (1, 0.7))
                Line((1, 0.7), (0.9, 0.7))
                Line((0.9, 0.7), (0.9, 0.1000000015))
                Line((0.9, 0.1000000015), (0.1000000015, 0.1000000015))
                Line((0.1000000015, 0.1000000015), (0.1000000015, 0.7))
                Line((0.1000000015, 0.7), (0, 0.7))
            make_face()
        # OneSide extrude, distance=11.3
        extrude(amount=11.3)
    return part.part


def model_21908_385686ec_0019():
    """Model: 01D v5"""
    with BuildPart() as part:
        # Sketch3 -> Extrude3 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 9 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.21, perimeter: 8.4
            with BuildLine():
                Line((-0.05, 0.95), (-0.05, -0.05))
                Line((-0.05, -0.05), (1.15, -0.05))
                Line((1.15, -0.05), (1.15, 0.95))
                Line((1.15, 0.95), (-0.05, 0.95))
            make_face()
            with BuildLine():
                Line((1.1, 0.9), (0, 0.9))
                Line((1.1, 0), (1.1, 0.9))
                Line((0, 0), (1.1, 0))
                Line((0, 0.9), (0, 0))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=11.3
        extrude(amount=11.3)
    return part.part


def model_21908_385686ec_0021():
    """Model: 02A v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 8 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 3.6653857674, perimeter: 9.6774721362
            with BuildLine():
                Line((1, 4), (-1, 4))
                Line((-1, 4), (-1, 3))
                Line((-1, 3), (-0.455718912, 1.7942811117))
                CenterArc((0, 2.0000000298), 0.5, -155.7048105236, 131.4096210471)
                Line((1, 3), (0.455718912, 1.7942811117))
                Line((1, 4), (1, 3))
            make_face()
            with BuildLine():
                CenterArc((0, 2.0000000298), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


MODELS = {
    "model_148051_b9c68456_0000": {"func": model_148051_b9c68456_0000, "volume": 10.2428722497, "area": 585.8446692803},
    "model_148051_b9c68456_0002": {"func": model_148051_b9c68456_0002, "volume": 1.7937245269, "area": 102.9020819702},
    "model_148051_b9c68456_0003": {"func": model_148051_b9c68456_0003, "volume": 1.0802019727, "area": 11.7898070303},
    "model_148051_b9c68456_0005": {"func": model_148051_b9c68456_0005, "volume": 1.3311238892, "area": 14.7914891603},
    "model_148051_b9c68456_0007": {"func": model_148051_b9c68456_0007, "volume": 0.9287361933, "area": 10.4909121838},
    "model_148051_b9c68456_0008": {"func": model_148051_b9c68456_0008, "volume": 1.3306546807, "area": 80.9778951129},
    "model_148051_b9c68456_0010": {"func": model_148051_b9c68456_0010, "volume": 0.1835254713, "area": 6.0977035282},
    "model_148051_b9c68456_0011": {"func": model_148051_b9c68456_0011, "volume": 0.8843867149, "area": 10.2692213384},
    "model_148051_c59af578_0000": {"func": model_148051_c59af578_0000, "volume": 0.8102217407, "area": 14.5302809319},
    "model_148051_c59af578_0001": {"func": model_148051_c59af578_0001, "volume": 7.9018597573, "area": 164.2591319637},
    "model_148051_c59af578_0002": {"func": model_148051_c59af578_0002, "volume": 5.6676013084, "area": 93.0004134708},
    "model_148051_c59af578_0003": {"func": model_148051_c59af578_0003, "volume": 3.8877248543, "area": 70.0282082794},
    "model_148051_c59af578_0006": {"func": model_148051_c59af578_0006, "volume": 0.4888374374, "area": 9.0398052335},
    "model_148051_c59af578_0009": {"func": model_148051_c59af578_0009, "volume": 0.0703848358, "area": 1.9951606989},
    "model_148051_c59af578_0011": {"func": model_148051_c59af578_0011, "volume": 0.3575102769, "area": 6.8264757601},
    "model_148051_c59af578_0013": {"func": model_148051_c59af578_0013, "volume": 0.1228029588, "area": 5.717430295},
    "model_148051_c59af578_0014": {"func": model_148051_c59af578_0014, "volume": 1.1297153398, "area": 12.0753128006},
    "model_148051_c59af578_0015": {"func": model_148051_c59af578_0015, "volume": 1.8778599124, "area": 107.8439642939},
    "model_148051_c59af578_0017": {"func": model_148051_c59af578_0017, "volume": 0.5748633478, "area": 10.0989646169},
    "model_148051_db355cb7_0004": {"func": model_148051_db355cb7_0004, "volume": 3.5198961258, "area": 33.1548982742},
    "model_148051_db355cb7_0009": {"func": model_148051_db355cb7_0009, "volume": 0.5828589811, "area": 6.5493298829},
    "model_148051_db355cb7_0010": {"func": model_148051_db355cb7_0010, "volume": 0.6751262329, "area": 7.7321362324},
    "model_148051_db355cb7_0011": {"func": model_148051_db355cb7_0011, "volume": 1.1467769206, "area": 12.4287033058},
    "model_148051_db355cb7_0013": {"func": model_148051_db355cb7_0013, "volume": 0.4549719076, "area": 5.1194828543},
    "model_148051_db355cb7_0014": {"func": model_148051_db355cb7_0014, "volume": 5.4777117047, "area": 50.5692625163},
    "model_148051_db355cb7_0015": {"func": model_148051_db355cb7_0015, "volume": 0.9820036059, "area": 11.1412481677},
    "model_148051_db355cb7_0016": {"func": model_148051_db355cb7_0016, "volume": 1.6923164238, "area": 17.1825080879},
    "model_148051_e7ab8ae7_0000": {"func": model_148051_e7ab8ae7_0000, "volume": 4.0009443008, "area": 146.6344654248},
    "model_148051_e7ab8ae7_0002": {"func": model_148051_e7ab8ae7_0002, "volume": 2.0499708879, "area": 117.5447311693},
    "model_148051_e7ab8ae7_0003": {"func": model_148051_e7ab8ae7_0003, "volume": 3.9168299171, "area": 36.7944402892},
    "model_148051_e7ab8ae7_0004": {"func": model_148051_e7ab8ae7_0004, "volume": 2.1112972025, "area": 20.6014423768},
    "model_148051_e7ab8ae7_0006": {"func": model_148051_e7ab8ae7_0006, "volume": 0.3375631165, "area": 4.7252929687},
    "model_148051_e7ab8ae7_0007": {"func": model_148051_e7ab8ae7_0007, "volume": 6.1499126636, "area": 351.8271183552},
    "model_148051_e7ab8ae7_0008": {"func": model_148051_e7ab8ae7_0008, "volume": 0.3393554582, "area": 5.7895288139},
    "model_148051_e7ab8ae7_0009": {"func": model_148051_e7ab8ae7_0009, "volume": 0.7201346484, "area": 8.6585644391},
    "model_148051_e7ab8ae7_0010": {"func": model_148051_e7ab8ae7_0010, "volume": 0.510095376, "area": 6.0505076667},
    "model_148051_e7ab8ae7_0011": {"func": model_148051_e7ab8ae7_0011, "volume": 3.840718125, "area": 36.5632538827},
    "model_148051_e7ab8ae7_0012": {"func": model_148051_e7ab8ae7_0012, "volume": 0.1472621556, "area": 11.8398773132},
    "model_148051_e7ab8ae7_0013": {"func": model_148051_e7ab8ae7_0013, "volume": 0.5486949245, "area": 12.6513853268},
    "model_148051_e7ab8ae7_0014": {"func": model_148051_e7ab8ae7_0014, "volume": 0.559604193, "area": 12.8031742534},
    "model_148083_5be191c8_0001": {"func": model_148083_5be191c8_0001, "volume": 1963.4954084936, "area": 942.4777960769},
    "model_148098_33ec30c9_0001": {"func": model_148098_33ec30c9_0001, "volume": 3871.44387, "area": 4408.0557},
    "model_148098_33ec30c9_0003": {"func": model_148098_33ec30c9_0003, "volume": 165.919023, "area": 275.8059},
    "model_148098_33ec30c9_0006": {"func": model_148098_33ec30c9_0006, "volume": 1991.028276, "area": 2351.6082},
    "model_148098_33ec30c9_0008": {"func": model_148098_33ec30c9_0008, "volume": 2101.640958, "area": 2477.4144},
    "model_148098_33ec30c9_0009": {"func": model_148098_33ec30c9_0009, "volume": 165.919023, "area": 275.8059},
    "model_148098_33ec30c9_0011": {"func": model_148098_33ec30c9_0011, "volume": 2073.3156618281, "area": 2441.02334375},
    "model_148128_e1d30e8b_0000": {"func": model_148128_e1d30e8b_0000, "volume": 0.0706858347, "area": 1.0838494655},
    "model_20440_27177360_0001": {"func": model_20440_27177360_0001, "volume": 10.991417075, "area": 33.4705920059},
    "model_20440_27177360_0002": {"func": model_20440_27177360_0002, "volume": 246.3934399552, "area": 427.0782004193},
    "model_20440_27177360_0004": {"func": model_20440_27177360_0004, "volume": 1814.4, "area": 2253.6},
    "model_20506_17515038_0000": {"func": model_20506_17515038_0000, "volume": 37.3064127614, "area": 169.6460032938},
    "model_20722_90d46353_0000": {"func": model_20722_90d46353_0000, "volume": 25170.5303039993, "area": 10735.4623999999},
    "model_20773_eb772a0a_0000": {"func": model_20773_eb772a0a_0000, "volume": 1191.3205739584, "area": 705.7709428344},
    "model_20797_78b83489_0000": {"func": model_20797_78b83489_0000, "volume": 5120.9575, "area": 4582.9285054752},
    "model_20945_8b57f672_0001": {"func": model_20945_8b57f672_0001, "volume": 20000000, "area": 8040000},
    "model_21028_d4d30a2e_0000": {"func": model_21028_d4d30a2e_0000, "volume": 20.4533870976, "area": 88.9935589845},
    "model_21233_05d745b4_0011": {"func": model_21233_05d745b4_0011, "volume": 1.3240891178, "area": 21.4077052658},
    "model_21233_05d745b4_0012": {"func": model_21233_05d745b4_0012, "volume": 1.3990891251, "area": 22.5577053623},
    "model_21234_8b71bd47_0005": {"func": model_21234_8b71bd47_0005, "volume": 0.1005497654, "area": 1.7850733722},
    "model_21235_01764fc7_0020": {"func": model_21235_01764fc7_0020, "volume": 4.0219906153, "area": 28.5022956992},
    "model_21235_01764fc7_0022": {"func": model_21235_01764fc7_0022, "volume": 5.4296873307, "area": 24.2269513443},
    "model_21236_b696e901_0018": {"func": model_21236_b696e901_0018, "volume": 0.2800891556, "area": 3.8874428779},
    "model_21236_b696e901_0026": {"func": model_21236_b696e901_0026, "volume": 2.1778699944, "area": 21.0039682706},
    "model_21236_b696e901_0029": {"func": model_21236_b696e901_0029, "volume": 0.8401168534, "area": 6.6787668001},
    "model_21236_b696e901_0033": {"func": model_21236_b696e901_0033, "volume": 3.397996377, "area": 15.4949381533},
    "model_21236_b696e901_0038": {"func": model_21236_b696e901_0038, "volume": 0.6804988139, "area": 9.1564922313},
    "model_21237_7887a24b_0004": {"func": model_21237_7887a24b_0004, "volume": 0.4358959807, "area": 9.8803088955},
    "model_21237_7887a24b_0006": {"func": model_21237_7887a24b_0006, "volume": 0.2500717768, "area": 3.6175392067},
    "model_21242_6c2af7c2_0000": {"func": model_21242_6c2af7c2_0000, "volume": 6.8943897988, "area": 27.407818796},
    "model_21242_6c2af7c2_0008": {"func": model_21242_6c2af7c2_0008, "volume": 1.2091914018, "area": 17.6207361196},
    "model_21242_6c2af7c2_0009": {"func": model_21242_6c2af7c2_0009, "volume": 1.5144453202, "area": 19.7258985064},
    "model_21242_6c2af7c2_0010": {"func": model_21242_6c2af7c2_0010, "volume": 4.681404653, "area": 38.3075682461},
    "model_21242_6c2af7c2_0013": {"func": model_21242_6c2af7c2_0013, "volume": 5.8153409339, "area": 24.5326504982},
    "model_21242_6c2af7c2_0015": {"func": model_21242_6c2af7c2_0015, "volume": 1.0757989844, "area": 8.8555529277},
    "model_21242_6c2af7c2_0016": {"func": model_21242_6c2af7c2_0016, "volume": 2.1679593469, "area": 12.4097209624},
    "model_21242_6c2af7c2_0018": {"func": model_21242_6c2af7c2_0018, "volume": 13.5608984829, "area": 45.8376880821},
    "model_21242_6c2af7c2_0019": {"func": model_21242_6c2af7c2_0019, "volume": 26.25, "area": 80.5710678119},
    "model_21242_6c2af7c2_0020": {"func": model_21242_6c2af7c2_0020, "volume": 181.6117285141, "area": 499.3124381577},
    "model_21246_c66f2b12_0016": {"func": model_21246_c66f2b12_0016, "volume": 0.0266033207, "area": 0.4986979886},
    "model_21246_c66f2b12_0017": {"func": model_21246_c66f2b12_0017, "volume": 0.1259088234, "area": 1.9447232179},
    "model_21246_c66f2b12_0018": {"func": model_21246_c66f2b12_0018, "volume": 4.275, "area": 20.6992573347},
    "model_21246_c66f2b12_0029": {"func": model_21246_c66f2b12_0029, "volume": 0.0798099622, "area": 1.2300607584},
    "model_21256_433456a3_0002": {"func": model_21256_433456a3_0002, "volume": 3.6302667841, "area": 33.1142174963},
    "model_21256_433456a3_0009": {"func": model_21256_433456a3_0009, "volume": 0.1743112684, "area": 2.4655219145},
    "model_21368_8605ac77_0000": {"func": model_21368_8605ac77_0000, "volume": 794.159265359, "area": 500.2035224833},
    "model_21385_601444ba_0007": {"func": model_21385_601444ba_0007, "volume": 0.2886138251, "area": 5.3599517139},
    "model_21385_601444ba_0018": {"func": model_21385_601444ba_0018, "volume": 1.1359157254, "area": 7.3868525693},
    "model_21385_601444ba_0036": {"func": model_21385_601444ba_0036, "volume": 0.6750959512, "area": 6.0396389922},
    "model_21385_601444ba_0040": {"func": model_21385_601444ba_0040, "volume": 0.0717533922, "area": 2.3092096272},
    "model_21422_b2a6bf27_0000": {"func": model_21422_b2a6bf27_0000, "volume": 3.3575771485, "area": 12.487830798},
    "model_21452_73ad419b_0000": {"func": model_21452_73ad419b_0000, "volume": 54.1048440299, "area": 124.99713756},
    "model_21472_f94fbb81_0000": {"func": model_21472_f94fbb81_0000, "volume": 38151.0792106585, "area": 15101.468854219},
    "model_21479_a3c5bdab_0001": {"func": model_21479_a3c5bdab_0001, "volume": 1886.04, "area": 12668.76},
    "model_21479_a3c5bdab_0002": {"func": model_21479_a3c5bdab_0002, "volume": 1579.5, "area": 2380.5},
    "model_21492_8bd34fc1_0007": {"func": model_21492_8bd34fc1_0007, "volume": 2.6244618645, "area": 15.351541135},
    "model_21492_8bd34fc1_0008": {"func": model_21492_8bd34fc1_0008, "volume": 4.0236103684, "area": 26.067965582},
    "model_21492_8bd34fc1_0015": {"func": model_21492_8bd34fc1_0015, "volume": 28.3034141206, "area": 160.5692397928},
    "model_21495_ebbbd369_0000": {"func": model_21495_ebbbd369_0000, "volume": 5.850208, "area": 77.0284},
    "model_21497_9833a679_0000": {"func": model_21497_9833a679_0000, "volume": 0.3817739155, "area": 4.8063202793},
    "model_21519_3e869afd_0001": {"func": model_21519_3e869afd_0001, "volume": 15.8257729925, "area": 129.0409182462},
    "model_21557_53eafe15_0016": {"func": model_21557_53eafe15_0016, "volume": 0.9567833035, "area": 8.4305990372},
    "model_21557_53eafe15_0044": {"func": model_21557_53eafe15_0044, "volume": 0.1908384188, "area": 3.6632915311},
    "model_21557_53eafe15_0046": {"func": model_21557_53eafe15_0046, "volume": 7.7295340696, "area": 45.6676921823},
    "model_21557_53eafe15_0049": {"func": model_21557_53eafe15_0049, "volume": 1.6902399473, "area": 11.9041396113},
    "model_21604_520e1ae2_0001": {"func": model_21604_520e1ae2_0001, "volume": 0.2590791593, "area": 4.2945081741},
    "model_21604_520e1ae2_0007": {"func": model_21604_520e1ae2_0007, "volume": 0.3675973499, "area": 6.8124335352},
    "model_21604_520e1ae2_0009": {"func": model_21604_520e1ae2_0009, "volume": 0.2491387069, "area": 4.1553418403},
    "model_21636_f65686bc_0003": {"func": model_21636_f65686bc_0003, "volume": 154.9664626045, "area": 368.9125705491},
    "model_21636_f65686bc_0004": {"func": model_21636_f65686bc_0004, "volume": 102.4664626045, "area": 256.9125705491},
    "model_21636_f65686bc_0005": {"func": model_21636_f65686bc_0005, "volume": 23.5619449019, "area": 65.9734457254},
    "model_21642_b79d233e_0011": {"func": model_21642_b79d233e_0011, "volume": 0.0116869152, "area": 0.7131321165},
    "model_21642_b79d233e_0019": {"func": model_21642_b79d233e_0019, "volume": 0.1316523658, "area": 1.7035404106},
    "model_21644_aa203dc5_0015": {"func": model_21644_aa203dc5_0015, "volume": 36.9, "area": 79.5},
    "model_21644_aa203dc5_0018": {"func": model_21644_aa203dc5_0018, "volume": 93.70718, "area": 227.0428349851},
    "model_21644_aa203dc5_0019": {"func": model_21644_aa203dc5_0019, "volume": 31.1769, "area": 90.7460958037},
    "model_21646_a2dd0d00_0001": {"func": model_21646_a2dd0d00_0001, "volume": 0.6268649436, "area": 31.7978736395},
    "model_21646_a2dd0d00_0006": {"func": model_21646_a2dd0d00_0006, "volume": 0.8507452805, "area": 43.0602390928},
    "model_21646_a2dd0d00_0007": {"func": model_21646_a2dd0d00_0007, "volume": 0.3868756862, "area": 3.510449194},
    "model_21646_a2dd0d00_0008": {"func": model_21646_a2dd0d00_0008, "volume": 1.0149241943, "area": 51.3140288891},
    "model_21646_a2dd0d00_0023": {"func": model_21646_a2dd0d00_0023, "volume": 1.5522370031, "area": 12.7864465429},
    "model_21646_a2dd0d00_0024": {"func": model_21646_a2dd0d00_0024, "volume": 3.063625664, "area": 15.8247120913},
    "model_21646_a2dd0d00_0029": {"func": model_21646_a2dd0d00_0029, "volume": 1.4516872377, "area": 12.4697543684},
    "model_21646_a2dd0d00_0036": {"func": model_21646_a2dd0d00_0036, "volume": 304.0761120058, "area": 423.614624791},
    "model_21646_a2dd0d00_0037": {"func": model_21646_a2dd0d00_0037, "volume": 24.7111103406, "area": 50.2653819265},
    "model_21646_a2dd0d00_0039": {"func": model_21646_a2dd0d00_0039, "volume": 75.6134283946, "area": 129.2104116169},
    "model_21646_a2dd0d00_0043": {"func": model_21646_a2dd0d00_0043, "volume": 4.5247394423, "area": 20.4266452511},
    "model_21646_a2dd0d00_0051": {"func": model_21646_a2dd0d00_0051, "volume": 1.1838163784, "area": 59.7657512943},
    "model_21646_a2dd0d00_0057": {"func": model_21646_a2dd0d00_0057, "volume": 3.1618187943, "area": 32.1145658139},
    "model_21646_a2dd0d00_0058": {"func": model_21646_a2dd0d00_0058, "volume": 0.1236762114, "area": 3.1558375183},
    "model_21646_a2dd0d00_0062": {"func": model_21646_a2dd0d00_0062, "volume": 3.1539633439, "area": 15.7133749988},
    "model_21646_a2dd0d00_0063": {"func": model_21646_a2dd0d00_0063, "volume": 6.3079266877, "area": 21.4930071822},
    "model_21646_a2dd0d00_0069": {"func": model_21646_a2dd0d00_0069, "volume": 1.1194016849, "area": 56.5592430282},
    "model_21646_a2dd0d00_0071": {"func": model_21646_a2dd0d00_0071, "volume": 1.4815379493, "area": 12.5786173034},
    "model_21646_a2dd0d00_0073": {"func": model_21646_a2dd0d00_0073, "volume": 0.4141874595, "area": 3.6270172355},
    "model_21646_a2dd0d00_0074": {"func": model_21646_a2dd0d00_0074, "volume": 0.5689438994, "area": 4.3880698135},
    "model_21646_a2dd0d00_0075": {"func": model_21646_a2dd0d00_0075, "volume": 1.1641777523, "area": 58.7958815101},
    "model_21647_6b6cca6f_0003": {"func": model_21647_6b6cca6f_0003, "volume": 254.7046243898, "area": 1742.3272856809},
    "model_21649_3ef60555_0001": {"func": model_21649_3ef60555_0001, "volume": 106.8358253991, "area": 418.6200925263},
    "model_21680_360ba5c7_0000": {"func": model_21680_360ba5c7_0000, "volume": 8.1975247444, "area": 42.0070634321},
    "model_21680_360ba5c7_0004": {"func": model_21680_360ba5c7_0004, "volume": 2.3094270113, "area": 23.2008686992},
    "model_21680_360ba5c7_0006": {"func": model_21680_360ba5c7_0006, "volume": 7.2966975302, "area": 35.024773061},
    "model_21680_360ba5c7_0011": {"func": model_21680_360ba5c7_0011, "volume": 3.2896948789, "area": 23.0897578832},
    "model_21695_1f33863f_0000": {"func": model_21695_1f33863f_0000, "volume": 0.003876298, "area": 0.6929326118},
    "model_21695_1f33863f_0003": {"func": model_21695_1f33863f_0003, "volume": 0.1131184861, "area": 2.8502295699},
    "model_21695_1f33863f_0005": {"func": model_21695_1f33863f_0005, "volume": 15.9690315287, "area": 44.8809491783},
    "model_21702_3390d14a_0001": {"func": model_21702_3390d14a_0001, "volume": 4.2446347519, "area": 35.292852859},
    "model_21702_3390d14a_0002": {"func": model_21702_3390d14a_0002, "volume": 0.0538673184, "area": 1.7063560498},
    "model_21702_3390d14a_0006": {"func": model_21702_3390d14a_0006, "volume": 0.2051852702, "area": 4.9676433835},
    "model_21710_0b9db742_0002": {"func": model_21710_0b9db742_0002, "volume": 983.6152500001, "area": 898.2945399084},
    "model_21710_0b9db742_0005": {"func": model_21710_0b9db742_0005, "volume": 7.916813487, "area": 84.4460105285},
    "model_21717_14f4c79a_0000": {"func": model_21717_14f4c79a_0000, "volume": 0.007146652, "area": 0.3017789004},
    "model_21732_adaf1650_0000": {"func": model_21732_adaf1650_0000, "volume": 11.9883175661, "area": 42.2230052642},
    "model_21734_7cf58bd0_0007": {"func": model_21734_7cf58bd0_0007, "volume": 5.7092313299, "area": 22.0052211509},
    "model_21734_7cf58bd0_0013": {"func": model_21734_7cf58bd0_0013, "volume": 2.3891247228, "area": 14.1217505544},
    "model_21736_fc59650e_0013": {"func": model_21736_fc59650e_0013, "volume": 19.9463495408, "area": 93.5707963268},
    "model_21736_fc59650e_0022": {"func": model_21736_fc59650e_0022, "volume": 0.4055180033, "area": 3.2689400329},
    "model_21736_fc59650e_0025": {"func": model_21736_fc59650e_0025, "volume": 0.7998583772, "area": 5.1646015352},
    "model_21740_6f0c9bdb_0023": {"func": model_21740_6f0c9bdb_0023, "volume": 0.2110885568, "area": 5.674125269},
    "model_21773_01f6bc23_0015": {"func": model_21773_01f6bc23_0015, "volume": 10.2423774489, "area": 40.5736691211},
    "model_21773_01f6bc23_0018": {"func": model_21773_01f6bc23_0018, "volume": 19.6035381584, "area": 75.1468962739},
    "model_21785_d595ced5_0000": {"func": model_21785_d595ced5_0000, "volume": 100.89, "area": 167.54},
    "model_21800_040f0143_0001": {"func": model_21800_040f0143_0001, "volume": 145.450184041, "area": 263.6335588463},
    "model_21800_040f0143_0004": {"func": model_21800_040f0143_0004, "volume": 180.6906053305, "area": 296.4078661343},
    "model_21800_040f0143_0007": {"func": model_21800_040f0143_0007, "volume": 162.0192427797, "area": 275.5802938651},
    "model_21822_7d3db422_0000": {"func": model_21822_7d3db422_0000, "volume": 0.3504839304, "area": 9.5465146761},
    "model_21822_7d3db422_0005": {"func": model_21822_7d3db422_0005, "volume": 2.4347343065, "area": 19.870573534},
    "model_21822_7d3db422_0010": {"func": model_21822_7d3db422_0010, "volume": 0.1445132621, "area": 4.335397862},
    "model_21822_7d3db422_0023": {"func": model_21822_7d3db422_0023, "volume": 1.9026270508, "area": 50.9369978871},
    "model_21822_7d3db422_0024": {"func": model_21822_7d3db422_0024, "volume": 0.2002765317, "area": 5.5409840428},
    "model_21822_7d3db422_0025": {"func": model_21822_7d3db422_0025, "volume": 0.1001382658, "area": 2.8706302872},
    "model_21822_7d3db422_0026": {"func": model_21822_7d3db422_0026, "volume": 5.6335309951, "area": 36.6696016859},
    "model_21822_7d3db422_0033": {"func": model_21822_7d3db422_0033, "volume": 8.2630553968, "area": 39.2124994725},
    "model_21822_7d3db422_0037": {"func": model_21822_7d3db422_0037, "volume": 0.600829595, "area": 16.222399065},
    "model_21822_7d3db422_0039": {"func": model_21822_7d3db422_0039, "volume": 0.4005530633, "area": 10.8816915539},
    "model_21822_7d3db422_0042": {"func": model_21822_7d3db422_0042, "volume": 0.326725636, "area": 3.518583772},
    "model_21822_7d3db422_0043": {"func": model_21822_7d3db422_0043, "volume": 2.6303539946, "area": 32.0799999928},
    "model_21822_7d3db422_0049": {"func": model_21822_7d3db422_0049, "volume": 1250, "area": 2650},
    "model_21847_b2de7eb8_0001": {"func": model_21847_b2de7eb8_0001, "volume": 0.3216205479, "area": 3.2672563597},
    "model_21847_b2de7eb8_0007": {"func": model_21847_b2de7eb8_0007, "volume": 0.198, "area": 8.314924225},
    "model_21863_eb40d2d8_0000": {"func": model_21863_eb40d2d8_0000, "volume": 2552.5440310417, "area": 2081.3051330032},
    "model_21881_f3bee5e5_0004": {"func": model_21881_f3bee5e5_0004, "volume": 1.2550662651, "area": 15.5037597455},
    "model_21893_0500d043_0055": {"func": model_21893_0500d043_0055, "volume": 0.471238898, "area": 4.162610266},
    "model_21899_d55d6c08_0027": {"func": model_21899_d55d6c08_0027, "volume": 8.9490041161, "area": 49.3943993627},
    "model_21899_d55d6c08_0029": {"func": model_21899_d55d6c08_0029, "volume": 0.2945243113, "area": 3.5342917353},
    "model_21900_760d2078_0004": {"func": model_21900_760d2078_0004, "volume": 0.1222132685, "area": 2.4018918444},
    "model_21900_760d2078_0011": {"func": model_21900_760d2078_0011, "volume": 2.27955, "area": 18.794},
    "model_21901_64acc24c_0000": {"func": model_21901_64acc24c_0000, "volume": 4.3128844186, "area": 38.2002439741},
    "model_21908_385686ec_0000": {"func": model_21908_385686ec_0000, "volume": 1.3625486678, "area": 58.1504422698},
    "model_21908_385686ec_0001": {"func": model_21908_385686ec_0001, "volume": 6.6335570151, "area": 267.8516156076},
    "model_21908_385686ec_0012": {"func": model_21908_385686ec_0012, "volume": 0.1500000022, "area": 3.5000000283},
    "model_21908_385686ec_0015": {"func": model_21908_385686ec_0015, "volume": 0.3573561643, "area": 3.4714598822},
    "model_21908_385686ec_0016": {"func": model_21908_385686ec_0016, "volume": 2.4860000236, "area": 52.4199999705},
    "model_21908_385686ec_0019": {"func": model_21908_385686ec_0019, "volume": 2.373, "area": 95.34},
    "model_21908_385686ec_0021": {"func": model_21908_385686ec_0021, "volume": 0.3665385767, "area": 8.2985187484},
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
