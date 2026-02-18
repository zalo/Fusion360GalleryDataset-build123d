"""Batch 005 - passing/06_11to15ops
56 models bundled from Fusion360 Gallery reconstructions.
"""

from build123d import *
from build123d import Edge, BuildLine
from collections import Counter
from OCP.BRepBuilderAPI import BRepBuilderAPI_MakeEdge
from OCP.Geom import Geom_BSplineCurve
from OCP.TColStd import TColStd_Array1OfReal, TColStd_Array1OfInteger
from OCP.TColgp import TColgp_Array1OfPnt
from OCP.gp import gp_Pnt


# Description: This is a parallelogram-shaped panel or trim piece with a tapered, elongated form featuring internal ribbing or structural reinforcements and a recessed upper surface.
def model_53619_db3904ac_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 45, perimeter: 28
            with BuildLine():
                Line((5, -4), (0, -4))
                Line((5, 5), (5, -4))
                Line((0, 5), (5, 5))
                Line((0, -4), (0, 5))
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 10 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 17.7721615875, perimeter: 17.1598671516
            with BuildLine():
                Line((-4.2924107099, 0.7654127184), (-0.7526891589, 0.8269815219))
                Line((-4.2040032371, -4.3173210455), (-4.2924107099, 0.7654127184))
                Line((-0.7526891589, -4.2572899737), (-4.2040032371, -4.3173210455))
                Line((-0.7526891589, 0.8269815219), (-0.7526891589, -4.2572899737))
            make_face()
            # Profile area: 7.953186206, perimeter: 11.5578483148
            with BuildLine():
                Line((-4.2924107099, 3.2049609715), (-0.7526891589, 3.27526564))
                Line((-4.2482069735, 0.9793773562), (-4.2924107099, 3.2049609715))
                Line((-0.7526891589, 0.9793773562), (-4.2482069735, 0.9793773562))
                Line((-0.7526891589, 3.27526564), (-0.7526891589, 0.9793773562))
            make_face()
        # OneSide extrude, distance=-0.1
        extrude(amount=-0.1, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 17 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.5374397798, perimeter: 2.9395139457
            with BuildLine():
                Line((-2.8474497862, 2.6801994856), (-2.8437486296, 1.9909895004))
                Line((-2.8437486296, 1.9909895004), (-2.0640254132, 1.9943493852))
                Line((-2.0640254132, 1.9943493852), (-2.0559622543, 2.6733478917))
                Line((-2.0559622543, 2.6733478917), (-2.8474497862, 2.6801994856))
            make_face()
            # Profile area: 0.3913516087, perimeter: 2.5481097683
            with BuildLine():
                Line((-1.3181922849, 0.9793773562), (-1.3135635395, 1.4970332786))
                Line((-1.3135635395, 1.4970332786), (-2.0699492776, 1.4955008296))
                Line((-2.0760782831, 0.9793773562), (-2.0699492776, 1.4955008296))
                Line((-2.0760782831, 0.9793773562), (-1.3181922849, 0.9793773562))
            make_face()
            # Profile area: 0.3951033809, perimeter: 2.5640979781
            with BuildLine():
                Line((-2.0760782831, 0.9793773562), (-2.0699492776, 1.4955008296))
                Line((-2.0699492776, 1.4955008296), (-2.8410793944, 1.4939385082))
                Line((-2.8410793944, 1.4939385082), (-2.8383161271, 0.9793773562))
                Line((-2.8383161271, 0.9793773562), (-2.0760782831, 0.9793773562))
            make_face()
            # Profile area: 0.4407924987, perimeter: 2.7435847225
            with BuildLine():
                Line((-2.8410793944, 1.4939385082), (-2.8383161271, 0.9793773562))
                Line((-2.8410793944, 1.4939385082), (-3.6955606894, 1.492207316))
                Line((-3.6955606894, 1.492207316), (-3.7000000551, 0.9793773562))
                Line((-2.8383161271, 0.9793773562), (-3.7000000551, 0.9793773562))
            make_face()
            # Profile area: 0.5853556961, perimeter: 3.0746897023
            with BuildLine():
                Line((-3.691274544, 1.9873374487), (-2.8437486296, 1.9909895004))
                Line((-2.8474497862, 2.6801994856), (-2.8437486296, 1.9909895004))
                Line((-2.8474497862, 2.6801994856), (-3.6852139326, 2.6874516779))
                Line((-3.6852139326, 2.6874516779), (-3.691274544, 1.9873374487))
            make_face()
            # Profile area: 0.5082243745, perimeter: 2.8561331489
            with BuildLine():
                Line((-2.0640254132, 1.9943493852), (-2.0559622543, 2.6733478917))
                Line((-2.0640254132, 1.9943493852), (-1.3090875793, 1.997602468))
                Line((-1.3090875793, 1.997602468), (-1.3031035136, 2.6668306919))
                Line((-1.3031035136, 2.6668306919), (-2.0559622543, 2.6733478917))
            make_face()
            # Profile area: 0.3775984569, perimeter: 2.5108050611
            with BuildLine():
                Line((-2.0640254132, 1.9943493852), (-1.3090875793, 1.997602468))
                Line((-2.0699492776, 1.4955008296), (-2.0640254132, 1.9943493852))
                Line((-1.3135635395, 1.4970332786), (-2.0699492776, 1.4955008296))
                Line((-1.3135635395, 1.4970332786), (-1.3090875793, 1.997602468))
            make_face()
            # Profile area: 0.4221726809, perimeter: 2.6942236749
            with BuildLine():
                Line((-2.8410793944, 1.4939385082), (-3.6955606894, 1.492207316))
                Line((-2.8437486296, 1.9909895004), (-2.8410793944, 1.4939385082))
                Line((-3.691274544, 1.9873374487), (-2.8437486296, 1.9909895004))
                Line((-3.691274544, 1.9873374487), (-3.6955606894, 1.492207316))
            make_face()
            # Profile area: 0.3861195283, perimeter: 2.5468040415
            with BuildLine():
                Line((-2.0699492776, 1.4955008296), (-2.0640254132, 1.9943493852))
                Line((-2.8437486296, 1.9909895004), (-2.0640254132, 1.9943493852))
                Line((-2.8437486296, 1.9909895004), (-2.8410793944, 1.4939385082))
                Line((-2.0699492776, 1.4955008296), (-2.8410793944, 1.4939385082))
            make_face()
        # OneSide extrude, distance=0.05
        extrude(amount=0.05, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2157779925, perimeter: 3.9157321057
            with BuildLine():
                Line((-3.7000000551, -4.6469673096), (-1.8551934035, -4.6469673096))
                Line((-3.7000000551, -4.7642083677), (-3.7000000551, -4.6469673096))
                Line((-1.8638779263, -4.7642083677), (-3.7000000551, -4.7642083677))
                Line((-1.8551934035, -4.6469673096), (-1.8638779263, -4.7642083677))
            make_face()
        # OneSide extrude, distance=-0.03
        extrude(amount=-0.03, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude5 (Cut)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 0.2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0207080186, perimeter: 0.5101221784
            with Locations((-1.2620926059, -4.6817494144)):
                Circle(0.0811884663)
            # Profile area: 0.0569413685, perimeter: 0.8458997224
            with Locations((-1.5500000231, -4.6750000697)):
                Circle(0.1346291222)
        # OneSide extrude, distance=-0.03
        extrude(amount=-0.03, mode=Mode.SUBTRACT)

        # Sketch6 -> Extrude6 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.174457259, perimeter: 1.4806399199
            with Locations((0.6455256016, 3.6261386414)):
                Circle(0.2356511622)
            # Profile area: 0.5144705447, perimeter: 2.5426418416
            with Locations((0.6455256016, 2.8850387413)):
                Circle(0.4046740176)
            # Profile area: 5.2656779397, perimeter: 8.1345227596
            with Locations((2.5225499344, 1.5783626017)):
                Circle(1.2946495069)
        # OneSide extrude, distance=-0.03
        extrude(amount=-0.03, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a tapered punch or drift tool with an elongated hexagonal or octagonal body that gradually narrows from a wider blue-anodized upper section to a pointed tip, featuring a cylindrical shank at the end.
def model_53704_b0cfbbcc_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 7 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.2099999906, perimeter: 1.9485280939
            with BuildLine():
                Line((0.6999999844, -0.1499999966), (0.1499999966, -0.1499999966))
                Line((0.849999981, 0), (0.6999999844, -0.1499999966))
                Line((0.6999999844, 0.1499999966), (0.849999981, 0))
                Line((0.1499999966, 0.1499999966), (0.6999999844, 0.1499999966))
                Line((0, 0), (0.1499999966, 0.1499999966))
                Line((0.1499999966, -0.1499999966), (0, 0))
            make_face()
        # OneSide extrude, distance=4
        extrude(amount=4)

        # Sketch3 -> Extrude2 (Cut)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))) as sk:
            # Profile area: 0.025597751, perimeter: 0.5671603177
            with Locations((-0.6766757253, -0.0025186139)):
                Circle(0.0902663681)
        # TwoSides extrude, along=0.4, against=-6.8
        extrude(amount=0.4, mode=Mode.SUBTRACT)
        extrude(sk.sketch, amount=-6.8, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude3 (NewBody)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.025597751, perimeter: 0.5671603177
            with Locations((-0.6766757253, -0.0025186139)):
                Circle(0.0902663681)
        # OneSide extrude, distance=0.04
        extrude(amount=0.04)

        # Sketch6 -> Extrude4 (NewBody)
        # Sketch on Profile plane
        with BuildSketch(Plane(origin=(0, 0, 4), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0246350682, perimeter: 0.556484126
            with BuildLine():
                CenterArc((0.681777572, -0.0022649406), 0.0901217178, 92.8465081477, 180)
                CenterArc((0.6766757253, -0.0025186139), 0.0902663681, -83.9094061388, 173.5118285729)
            make_face()
        # OneSide extrude, distance=0.04
        extrude(amount=0.04)

        # Sketch7 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 4.04), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0270319302, perimeter: 1.3622549679
            with BuildLine():
                CenterArc((0.681777572, -0.0022649406), 0.1282424125, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0.6766757253, -0.0025186139), 0.0902663681, -83.9094061388, 173.5118285729)
                CenterArc((0.681777572, -0.0022649406), 0.0901217178, 92.8465081477, 180)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0246350682, perimeter: 0.556484126
            with BuildLine():
                CenterArc((0.681777572, -0.0022649406), 0.0901217178, 92.8465081477, 180)
                CenterArc((0.6766757253, -0.0025186139), 0.0902663681, -83.9094061388, 173.5118285729)
            make_face()
        # OneSide extrude, distance=1.2
        extrude(amount=1.2, mode=Mode.ADD)
    return part.part


# Description: This is a rounded rectangular connector or spacer block with a cylindrical or rounded upper section and a flat rectangular base or mounting tab extending downward.
def model_54482_a0855783_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch5 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            Circle(0.5)
        # Symmetric extrude, each_side=0.3
        extrude(amount=0.3, both=True)

        # Sketch22 -> Extrude5 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0176714587, perimeter: 0.471238898
            with Locations((-4.6414718458, -1.0527141924)):
                Circle(0.075)
        # Symmetric extrude, each_side=0.7
        extrude(amount=0.7, both=True)
    return part.part


# Description: This is a cylindrical roller or spacer with rounded end caps, featuring a smooth curved surface and grid-pattern surface geometry indicating a machined or textured finish.
def model_54508_46ea0fd2_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 19.6349540849, perimeter: 15.7079632679
            Circle(2.5)
        # Symmetric extrude, each_side=2
        extrude(amount=2, both=True)
    return part.part


# Description: This is a curved, fan-shaped duct or baffle component with a segmented cylindrical body, featuring a mesh or perforated top surface and solid side panels, designed to direct or filter airflow.
def model_54612_ac95f0d2_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 50, perimeter: 30.5291382244
            with BuildLine():
                CenterArc((0, -9.5), 13, 67.380135052, 45.2397298961)
                Line((-5, 2.5), (-5, -2.5))
                CenterArc((0, -14.5), 13, 67.380135052, 45.2397298961)
                Line((5, 2.5), (5, -2.5))
            make_face()
        # OneSide extrude, distance=5
        extrude(amount=5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            with Locations((2.5, 0.5)):
                Circle(1)
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            with Locations((-2.5, 0.5)):
                Circle(1)
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.ADD)

        # Sketch9 -> Extrude6 (Cut)
        # Sketch on XY construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.5, perimeter: 7
            with BuildLine():
                Line((-1.5, 1.5), (-1.5, 2))
                Line((1.5, 1.5), (-1.5, 1.5))
                Line((1.5, 2), (1.5, 1.5))
                Line((-1.5, 2), (1.5, 2))
            make_face()
        # OneSide extrude, distance=0.3
        extrude(amount=0.3, mode=Mode.SUBTRACT)

        # Sketch16 -> Extrude7 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 16 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))) as sk:
            # Profile area: 0.0314159275, perimeter: 0.6283185401
            with Locations((3.9000000581, -2.0000000298)):
                Circle(0.1000000015)
            # Profile area: 0.0199540422, perimeter: 0.603839937
            with BuildLine():
                Line((3.8000000566, -2.1957965102), (3.8000000566, -2.4000000358))
                Line((3.8000000566, -2.4000000358), (3.8977164995, -2.4000000358))
                Line((3.8977164995, -2.4000000358), (3.8977164995, -2.1957965102))
                Line((3.8977164995, -2.1957965102), (3.8000000566, -2.1957965102))
            make_face()
            # Profile area: 0.029314937, perimeter: 0.7954329693
            with BuildLine():
                Line((3.8000000566, -2.5), (3.8000000566, -2.8000000417))
                Line((3.8000000566, -2.8000000417), (3.8977164995, -2.8000000417))
                Line((3.8977164995, -2.8000000417), (3.8977164995, -2.5))
                Line((3.8977164995, -2.5), (3.8000000566, -2.5))
            make_face()
            # Profile area: 0.0300000009, perimeter: 0.8000000119
            with BuildLine():
                Line((4.0000000596, -2.5000000373), (4.0000000596, -2.8000000417))
                Line((4.0000000596, -2.8000000417), (4.1000000611, -2.8000000417))
                Line((4.1000000611, -2.8000000417), (4.1000000611, -2.5000000373))
                Line((4.1000000611, -2.5000000373), (4.0000000596, -2.5000000373))
            make_face()
            # Profile area: 0.0314159275, perimeter: 0.6283185401
            with Locations((3.9000000581, -3.0000000447)):
                Circle(0.1000000015)
            # Profile area: 0.0200000006, perimeter: 0.6000000089
            with BuildLine():
                Line((4.0000000596, -2.2000000328), (4.0000000596, -2.4000000358))
                Line((4.0000000596, -2.4000000358), (4.1000000611, -2.4000000358))
                Line((4.1000000611, -2.4000000358), (4.1000000611, -2.2000000328))
                Line((4.1000000611, -2.2000000328), (4.0000000596, -2.2000000328))
            make_face()
        # TwoSides offset extrude, full=3.1, trim=3
        extrude(amount=3.1)
        extrude(sk.sketch, amount=3, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a socket head cap screw (or hex socket bolt) featuring a cylindrical shank with a recessed hexagonal socket in the rounded head and threads along the shaft.
def model_54748_098dc1a6_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 113.0973355292, perimeter: 37.6991118431
            Circle(6)
        # OneSide extrude, distance=7
        extrude(amount=7)

        # Sketch4 -> Extrude2 (Join)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 23.7582944428, perimeter: 17.2787595947
            Circle(2.75)
        # OneSide extrude, distance=14
        extrude(amount=14, mode=Mode.ADD)

        # Sketch6 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 1.7900246699, perimeter: 5.2619734931
            with BuildLine():
                CenterArc((-3, 0), 0.9, 65.4048576637, 229.1902846726)
                CenterArc((0, 0), 2.75, 162.6877060252, 34.6245879497)
            make_face()
            # Profile area: 1.7940680884, perimeter: 5.268440267
            with BuildLine():
                CenterArc((0, 0), 2.75, -17.335870032, 34.671740064)
                CenterArc((3, 0), 0.9011224814, -114.5860363112, 229.1720726225)
            make_face()
        # OneSide extrude, distance=5
        extrude(amount=5, mode=Mode.ADD)

        # Sketch7 -> Extrude4 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 28.2743338823, perimeter: 18.8495559215
            with Locations((-128, -77)):
                Circle(3)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch11 -> Extrude8 (Cut)
        # Sketch on XY construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1, perimeter: 4
            with BuildLine():
                Line((0.5, -7.5), (0.5, -6.5))
                Line((0.5, -6.5), (-0.5, -6.5))
                Line((-0.5, -6.5), (-0.5, -7.5))
                Line((-0.5, -7.5), (0.5, -7.5))
            make_face()
        # OneSide extrude, distance=4
        extrude(amount=4, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical rod or shaft with rounded ends, featuring a uniform diameter throughout its length and a slight taper or chamfer at both extremities.
def model_54751_d9d0d87b_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            with Locations((-2.5, 1)):
                Circle(0.4)
        # OneSide extrude, distance=6.5
        extrude(amount=6.5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XY construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.3848451001, perimeter: 2.1991148575
            with Locations((-2.5, 1)):
                Circle(0.35)
        # OneSide extrude, distance=-4.5
        extrude(amount=-4.5, mode=Mode.ADD)
    return part.part


# Description: This is a sledgehammer consisting of a long cylindrical handle with a large rectangular head at the base, featuring a flat striking surface and a rounded poll (back end).
def model_54759_5a7a83c9_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch5 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            with Locations((11, -10)):
                Circle(1)
        # Symmetric extrude, each_side=0.4
        extrude(amount=0.4, both=True)

        # Sketch6 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.4, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2865527074, perimeter: 1.8976110039
            with Locations((-11, 10)):
                Circle(0.3020141713)
        # OneSide extrude, distance=8
        extrude(amount=8, mode=Mode.ADD)
    return part.part


# Description: This is a flat rectangular plate or panel with a parallelogram shape, featuring a dark blue-gray color and beveled or rounded edges.
def model_54780_39d5176d_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 50, perimeter: 30
            with BuildLine():
                Line((0, 5), (0, 0))
                Line((0, 0), (10, 0))
                Line((10, 0), (10, 5))
                Line((10, 5), (0, 5))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch3 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((0.2430997044, 1.0084225869)):
                Circle(0.15)
        # OneSide extrude, distance=-0.3
        extrude(amount=-0.3, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.0762544037, perimeter: 1.2225327448
            with BuildLine():
                Line((0.3546425718, 3.3699233579), (0.1799950368, 3.3699233579))
                Line((0.3546425718, 3.8065421953), (0.3546425718, 3.3699233579))
                Line((0.1799950368, 3.8065421953), (0.3546425718, 3.8065421953))
                Line((0.1799950368, 3.3699233579), (0.1799950368, 3.8065421953))
            make_face()
        # OneSide extrude, distance=-0.3
        extrude(amount=-0.3, mode=Mode.SUBTRACT)

        # Sketch2 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 8 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.5, perimeter: 3
            with BuildLine():
                Line((-0.5, 4), (-0.5, 4.5))
                Line((-0.5, 4.5), (-1.5, 4.5))
                Line((-1.5, 4.5), (-1.5, 4))
                Line((-1.5, 4), (-0.5, 4))
            make_face()
        # OneSide extrude, distance=-0.02
        extrude(amount=-0.02, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude5 (NewBody)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1000697627, perimeter: 2.4563176366
            with BuildLine():
                Line((-2.1404098738, 0.2920699244), (-1, 0.2920699244))
                Line((-2.1404098738, 0.2043209799), (-2.1404098738, 0.2920699244))
                Line((-1, 0.2043209799), (-2.1404098738, 0.2043209799))
                Line((-1, 0.2920699244), (-1, 0.2043209799))
            make_face()
        # OneSide extrude, distance=0.02
        extrude(amount=0.02)

        # Sketch6 -> Extrude6 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0300000009, perimeter: 0.8000000119
            with BuildLine():
                Line((-2.6000000387, 0.3000000045), (-2.3000000343, 0.3000000045))
                Line((-2.6000000387, 0.200000003), (-2.6000000387, 0.3000000045))
                Line((-2.3000000343, 0.200000003), (-2.6000000387, 0.200000003))
                Line((-2.3000000343, 0.3000000045), (-2.3000000343, 0.200000003))
            make_face()
        # OneSide extrude, distance=0.02
        extrude(amount=0.02, mode=Mode.ADD)

        # Sketch10 -> Extrude10 (NewBody)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.0773491888, perimeter: 1.3283663797
            with BuildLine():
                Line((-1.6384505234, 4), (-1.7890603323, 4))
                Line((-1.6384505234, 4.5135733809), (-1.6384505234, 4))
                Line((-1.7890603323, 4.5135733809), (-1.6384505234, 4.5135733809))
                Line((-1.7890603323, 4), (-1.7890603323, 4.5135733809))
            make_face()
        # OneSide extrude, distance=0.05
        extrude(amount=0.05)
    return part.part


# Description: This is a U-shaped bracket or clamp assembly with two opposing cylindrical head sections at each end (featuring geometric faceted tops), connected by a curved central body with internal ribbing and mounting slots, designed for securing or guiding components.
def model_54843_a145d131_0000():
    """Model: C v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 16 constraints, 11 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 229.7528256357, perimeter: 88.14797175
            with BuildLine():
                Line((11.7708170315, 8.1608816255), (1.0049386235, 10.0591964598))
                CenterArc((0.5708170315, 7.5971772797), 2.5, 79.9999732863, 100.0000923818)
                Line((-1.9291829685, 7.5971744144), (-1.9291829685, -12.2597742025))
                CenterArc((0.5708170315, -12.2597750885), 2.5, 179.9999796934, 99.9999776846)
                Line((1.0049356442, -14.721794794), (13.8708170315, -12.4531927748))
                Line((13.8708170315, -8.8391183745), (13.8708170315, -12.4531927748))
                Line((6.7708170315, -8.8391183745), (13.8708170315, -8.8391183745))
                CenterArc((6.7708170315, -6.3391183745), 2.5, 180, 90)
                Line((4.2708170315, 1.6608781225), (4.2708170315, -6.3391183745))
                CenterArc((6.7708170315, 1.6608816255), 2.5, 90, 90.0000802813)
                Line((11.7708170315, 4.1608816255), (6.7708170315, 4.1608816255))
                Line((11.7708170315, 8.1608816255), (11.7708170315, 4.1608816255))
            make_face()
        # Symmetric extrude, each_side=2.5
        extrude(amount=2.5, both=True)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 8 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(2.5, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 25.4066435704, perimeter: 60.7403096522
            with BuildLine():
                Line((6.7708170315, 4.1608816255), (11.7708170315, 4.1608816255))
                Line((11.7708170315, 4.1608816255), (11.7708170315, 4.9608816255))
                Line((11.7708170315, 4.9608816255), (5.9708170315, 4.9608816255))
                CenterArc((5.9708170315, 2.4608816255), 2.5, 90, 90.0000467535)
                Line((3.4708170315, 2.4608795855), (3.4708170315, -7.1391183745))
                CenterArc((5.9708170315, -7.1391183745), 2.5, -180, 90)
                Line((5.9708170315, -9.6391183745), (10.9708170315, -9.6391183745))
                Line((10.9708170315, -9.6391183745), (13.8708170315, -9.6712863541))
                Line((13.8708170315, -9.6712863541), (13.8708170315, -8.8391183745))
                Line((13.8708170315, -8.8391183745), (6.7708170315, -8.8391183745))
                CenterArc((6.7708170315, -6.3391183745), 2.5, 180, 90)
                Line((4.2708170315, -6.3391183745), (4.2708170315, 1.6608781225))
                CenterArc((6.7708170315, 1.6608816255), 2.5, 90, 90.0000802813)
            make_face()
        # TwoSides extrude (symmetric), distance=0.25
        extrude(amount=0.25, both=True, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 8 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-2.5, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 25.36, perimeter: 60.707963268
            with BuildLine():
                Line((-5.9708170315, -9.6391183745), (-13.8708170315, -9.6391183745))
                CenterArc((-5.9708170315, -7.1391183745), 2.5, -90, 90)
                Line((-3.4708170315, 2.4608795871), (-3.4708170315, -7.1391183745))
                CenterArc((-5.9708170315, 2.4608816255), 2.5, -0.0000467152, 90.0000467152)
                Line((-11.7708170315, 4.9608816255), (-5.9708170315, 4.9608816255))
                Line((-11.7708170315, 4.9608816255), (-11.7708170315, 4.1608816255))
                Line((-11.7708170315, 4.1608816255), (-6.7708170315, 4.1608816255))
                CenterArc((-6.7708170315, 1.6608816255), 2.5, -0.0000802813, 90.0000802813)
                Line((-4.2708170315, 1.6608781225), (-4.2708170315, -6.3391183745))
                CenterArc((-6.7708170315, -6.3391183745), 2.5, -90, 90)
                Line((-6.7708170315, -8.8391183745), (-13.8708170315, -8.8391183745))
                Line((-13.8708170315, -8.8391183745), (-13.8708170315, -9.6391183745))
            make_face()
        # TwoSides extrude (symmetric), distance=0.25
        extrude(amount=0.25, both=True, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 17 constraints, 11 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(2.5, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 153.4849531935, perimeter: 78.6210590713
            with BuildLine():
                Line((3.4708170315, -7.1391183745), (3.4708170315, 2.4608795855))
                CenterArc((5.9708170315, 2.4608816255), 2.5, 90, 90.0000467535)
                Line((5.9708170315, 4.9608816255), (9.5208170315, 4.9608816255))
                Line((9.5208170315, 7.7452760425), (9.5208170315, 4.9608816255))
                Line((9.5208170315, 7.7452760425), (1.8049374756, 9.1057937881))
                CenterArc((1.3708170315, 6.6437744056), 2.5, 80, 100)
                Line((-1.1291829685, 6.6437744056), (-1.1291829685, -11.3063722144))
                CenterArc((1.3708170315, -11.3063722144), 2.5, -180, 100)
                Line((1.8049374756, -13.768391597), (12.0791955346, -11.9567626944))
                CenterArc((11.8708170315, -10.7749935124), 1.2, -79.9999665524, 80.0000165147)
                Line((13.0708170315, -10.774992466), (13.0708170315, -9.6624124287))
                Line((13.0708170315, -9.6624124287), (10.9708170315, -9.6391183745))
                Line((5.9708170315, -9.6391183745), (10.9708170315, -9.6391183745))
                CenterArc((5.9708170315, -7.1391183745), 2.5, -180, 90)
            make_face()
            # Profile area: 5.8185597685, perimeter: 9.7067630043
            with BuildLine():
                Line((9.5208170315, 4.9608816255), (11.7708170315, 4.9608816255))
                Line((11.7708170315, 7.348540336), (11.7708170315, 4.9608816255))
                Line((11.7708170315, 7.348540336), (9.5208170315, 7.7452760425))
                Line((9.5208170315, 7.7452760425), (9.5208170315, 4.9608816255))
            make_face()
        # TwoSides extrude (symmetric), distance=2.1
        extrude(amount=2.1, both=True, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 7 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(-2.5, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 154.6422956861, perimeter: 79.2584119134
            with BuildLine():
                CenterArc((-1.3708170315, -11.3063722144), 2.5, -100, 100)
                Line((1.1291829685, 6.6437744056), (1.1291829685, -11.3063722144))
                CenterArc((-1.3708170315, 6.6437744056), 2.5, 0, 100)
                Line((-11.7708170315, 7.348540336), (-1.8049374756, 9.1057937881))
                Line((-11.7708170315, 7.348540336), (-11.7708170315, 4.9608816255))
                Line((-11.7708170315, 4.9608816255), (-5.9708170315, 4.9608816255))
                CenterArc((-5.9708170315, 2.4608816255), 2.5, -0.0000467152, 90.0000467152)
                Line((-3.4708170315, 2.4608795871), (-3.4708170315, -7.1391183745))
                CenterArc((-5.9708170315, -7.1391183745), 2.5, -90, 90)
                Line((-5.9708170315, -9.6391183745), (-10.9708170315, -9.6391183745))
                Line((-10.9708170315, -12.1521997293), (-10.9708170315, -9.6391183745))
                Line((-1.8049374756, -13.768391597), (-10.9708170315, -12.1521997293))
            make_face()
        # TwoSides extrude (symmetric), distance=2.1
        extrude(amount=2.1, both=True, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude7 (Cut)
        # Sketch on BRepFace
        # Sketch has 17 constraints, 11 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(2.5, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 5.8185597685, perimeter: 9.7067630043
            with BuildLine():
                Line((9.5208170315, 4.9608816255), (11.7708170315, 4.9608816255))
                Line((11.7708170315, 7.348540336), (11.7708170315, 4.9608816255))
                Line((11.7708170315, 7.348540336), (9.5208170315, 7.7452760425))
                Line((9.5208170315, 7.7452760425), (9.5208170315, 4.9608816255))
            make_face()
            # Profile area: 12.6036723301, perimeter: 22.1379741701
            with BuildLine():
                Line((9.5208170315, 8.5576173321), (11.7708170315, 8.1608816255))
                Line((11.7708170315, 8.1608816255), (11.7708170315, 7.348540336))
                Line((11.7708170315, 7.348540336), (11.7708170315, 4.9608816255))
                Line((9.5208170315, 4.9608816255), (11.7708170315, 4.9608816255))
                Line((9.5208170315, 4.9608816255), (9.5208170315, 4.1608816255))
                Line((9.5208170315, 4.1608816255), (14.0208170315, 4.1608816255))
                Line((14.0208170315, 4.1608816255), (14.0208170315, 8.6608816255))
                Line((14.0208170315, 8.6608816255), (9.5208170315, 8.6608816255))
                Line((9.5208170315, 8.6608816255), (9.5208170315, 8.5576173321))
            make_face()
        # OneSide extrude, distance=-5
        extrude(amount=-5, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude8 (Join)
        # Sketch on BRepFace
        # Sketch has 17 constraints, 11 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(2.5, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 5.8185597685, perimeter: 9.7067630043
            with BuildLine():
                Line((9.5208170315, 4.9608816255), (11.7708170315, 4.9608816255))
                Line((11.7708170315, 7.348540336), (11.7708170315, 4.9608816255))
                Line((11.7708170315, 7.348540336), (9.5208170315, 7.7452760425))
                Line((9.5208170315, 7.7452760425), (9.5208170315, 4.9608816255))
            make_face()
            # Profile area: 12.6036723301, perimeter: 22.1379741701
            with BuildLine():
                Line((9.5208170315, 8.5576173321), (11.7708170315, 8.1608816255))
                Line((11.7708170315, 8.1608816255), (11.7708170315, 7.348540336))
                Line((11.7708170315, 7.348540336), (11.7708170315, 4.9608816255))
                Line((9.5208170315, 4.9608816255), (11.7708170315, 4.9608816255))
                Line((9.5208170315, 4.9608816255), (9.5208170315, 4.1608816255))
                Line((9.5208170315, 4.1608816255), (14.0208170315, 4.1608816255))
                Line((14.0208170315, 4.1608816255), (14.0208170315, 8.6608816255))
                Line((14.0208170315, 8.6608816255), (9.5208170315, 8.6608816255))
                Line((9.5208170315, 8.6608816255), (9.5208170315, 8.5576173321))
            make_face()
        # OneSide extrude, distance=-5
        extrude(amount=-5, mode=Mode.ADD)
    return part.part


# Description: This is a telephone handset with an overall curved, organic shape featuring a rounded earpiece on one end, a cylindrical grip section in the middle, and a flared mouthpiece portion that tapers upward with a smooth, ergonomic design.
def model_54976_69951f7f_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 234.251768454, perimeter: 63.9167354528
            with BuildLine():
                CenterArc((17.5, 6.8715138834), 3.1229095753, -143.1812699702, 106.3625399403)
                CenterArc((8.3400208868, 20.3542767628), 19.2797543509, -52.7871021423, 59.1770232573)
                CenterArc((18.75, 11.25), 14.2521928137, 52.1250163489, 75.7499673022)
                CenterArc((-0.1256708848, 10.1426654615), 15.9760110091, -18.7778205323, 69.4464328665)
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)

        # Sketch4 -> Extrude4 (NewBody)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 113.0973355292, perimeter: 37.6991118431
            with Locations((17.5, -2.5)):
                Circle(6)
        # OneSide extrude, distance=-2.5
        extrude(amount=-2.5)

        # Sketch5 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 50.2654824574, perimeter: 25.1327412287
            with Locations((17.5, -2.5)):
                Circle(4)
        # OneSide extrude, distance=2
        extrude(amount=2, mode=Mode.ADD)

        # Sketch22 -> Extrude15 (NewBody)
        # Sketch on YZ construction plane
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 2.2069016, perimeter: 5.2661886991
            with Locations((35.8508306783, -0.5244567039)):
                Circle(0.8381399627)
        # TwoSides extrude (symmetric), distance=6
        extrude(amount=6, both=True)

        # Sketch23 -> Extrude16 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(6, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 3.9378624886, perimeter: 14.0535308954
            with BuildLine():
                CenterArc((35.8508306783, -0.5244567039), 1.3985489472, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((35.8508306783, -0.5244567039), 0.8381399627, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 2.2069016, perimeter: 5.2661886991
            with Locations((35.8508306783, -0.5244567039)):
                Circle(0.8381399627)
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)
    return part.part


# Description: This is a dual-chamber cylindrical component with a tapered design featuring two stacked circular housings connected by a central shaft, with ribbed flanges on the ends and internal radial partitions or vanes visible through the semi-transparent sections.
def model_54980_620ee8ed_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 54.8174770425, perimeter: 30.853981634
            with BuildLine():
                Line((-4.5, 2.5), (4.5, 2.5))
                CenterArc((-4.5, 0), 2.5, 90, 180)
                Line((4.5, -2.5), (-4.5, -2.5))
                Line((4.5, 2.5), (4.5, -2.5))
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2)

        # Sketch3 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 22.3174770425, perimeter: 17.853981634
            with BuildLine():
                Line((0, -4.5), (0, 0.5))
                Line((0, -4.5), (2.5, -4.5))
                CenterArc((2.5, -2), 2.5, -90, 180)
                Line((2.5, 0.5), (0, 0.5))
            make_face()
        # OneSide extrude, distance=-1.5
        extrude(amount=-1.5, mode=Mode.ADD)

        # Sketch2 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -2.5, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 22.3174770425, perimeter: 17.853981634
            with BuildLine():
                Line((0, 0.5), (0, -4.5))
                Line((-2.5, 0.5), (0, 0.5))
                CenterArc((-2.5, -2), 2.5, 90, 180)
                Line((0, -4.5), (-2.5, -4.5))
            make_face()
        # OneSide extrude, distance=-1.5
        extrude(amount=-1.5, mode=Mode.ADD)

        # Sketch6 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 7.0685834706, perimeter: 9.4247779608
            with Locations((5, 0)):
                Circle(1.5)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3, mode=Mode.ADD)
    return part.part


# Description: This is a pair of triangular prism-shaped mounting brackets or feet with dark blue/gray coloring, featuring angled sides and what appears to be reinforcing ribs or slots on their inner faces for structural rigidity.
def model_55051_83f272e3_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 97.5316522068, perimeter: 47.9395017172
            with BuildLine():
                Line((-7.3481202675, 7.3481202675), (-7.3481202675, -6.4449382637))
                Line((-7.3481202675, -6.4449382637), (6.7940153562, -6.7940153562))
                Line((-7.3481202675, 7.3481202675), (6.7940153562, -6.7940153562))
            make_face()
        # TwoSides extrude (symmetric), distance=5
        extrude(amount=5, both=True)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(0.7071067812, 0.7071067812, 0))):
            # Profile area: 84.2567378781, perimeter: 48.4287547742
            with BuildLine():
                Line((-2.0676871474, 10.3918113402), (-2.4138983069, -9.6081886598))
                Line((-2.4138983069, -9.6081886598), (1.9429483254, -9.6081886598))
                Line((1.9429483254, -9.6081886598), (2.0011400081, 10.3918113402))
                Line((2.0011400081, 10.3918113402), (-2.0676871474, 10.3918113402))
            make_face()
        # OneSide extrude, distance=-10
        extrude(amount=-10, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane.XY) as sk:
            # Profile area: 3.3063461811, perimeter: 9.4894246797
            with BuildLine():
                Line((0, -1.2073946851), (2.6217962673, -3.8291909524))
                Line((2.6217962673, -3.8291909524), (3.3893428823, -3.3893428823))
                Line((0.5343116931, -0.5343116931), (3.3893428823, -3.3893428823))
                Line((0.5343116931, -0.5343116931), (0, -1.2073946851))
            make_face()
        # TwoSides extrude, along=2, against=-1.7
        extrude(amount=2)
        extrude(sk.sketch, amount=-1.7)

        # Sketch4 -> Extrude4 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane.XY) as sk:
            # Profile area: 2.6055315597, perimeter: 9.9188468572
            with BuildLine():
                Line((-2.1813920401, 3.2324209114), (-1, 3))
                Line((-1, 3), (-4.336334408, 6.336334408))
                Line((-4.336334408, 6.336334408), (-4.336334408, 5.3873632793))
                Line((-4.336334408, 5.3873632793), (-2.1813920401, 3.2324209114))
            make_face()
        # TwoSides extrude, along=2, against=-1.7
        extrude(amount=2)
        extrude(sk.sketch, amount=-1.7)

        # Sketch5 -> Extrude5 (Join)
        # Sketch on XY construction plane
        # Sketch has 8 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 16.2399986112, perimeter: 34.8415004441
            with BuildLine():
                Line((0.570062324, -3.0207292678), (1.0869472561, -2.2943419412))
                Line((1.0869472561, -2.2943419412), (-3.9058126586, 2.6984179735))
                Line((-3.9058126586, 2.6984179735), (-2.7766008804, 3.8276297518))
                Line((-2.7766008804, 3.8276297518), (-3.7063254752, 4.7573543465))
                Line((-3.7063254752, 4.7573543465), (-4.8730873627, 3.590592459))
                Line((-4.8730873627, 3.590592459), (-10, 8))
                Line((-10, 8), (-10, 7))
                Line((-10, 7), (0.570062324, -3.0207292678))
            make_face()
        # TwoSides extrude (symmetric), distance=0.5
        extrude(amount=0.5, both=True, mode=Mode.ADD)

        # Sketch6 -> Extrude6 (Cut)
        # Sketch on XY construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 4.3884800718, perimeter: 7.4261205899
            with Locations((-10, 7.5)):
                Circle(1.1819037999)
        # TwoSides extrude (symmetric), distance=0.5
        extrude(amount=0.5, both=True, taper=-5, mode=Mode.SUBTRACT)

        # Sketch7 -> Extrude7 (Join)
        # Sketch on XY construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 2.9436390964, perimeter: 6.0820111674
            with Locations((-9.8626330468, 7.3778147136)):
                Circle(0.9679821412)
        # TwoSides extrude (symmetric), distance=0.5
        extrude(amount=0.5, both=True, mode=Mode.ADD)
    return part.part


# Description: This is a rectangular box-shaped component with a hinged or removable lid on the left side, featuring an open compartment design with a sloped top surface and internal structural elements visible through the open section.
def model_55104_4bb0d5c8_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 209, perimeter: 60
            with BuildLine():
                Line((10, -5), (10, 6))
                Line((10, 6), (-9, 6))
                Line((-9, 6), (-9, -5))
                Line((-9, -5), (10, -5))
            make_face()
        # TwoSides extrude (symmetric), distance=6
        extrude(amount=6, both=True)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -6), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 95, perimeter: 48
            with BuildLine():
                Line((-10, 0), (9, 0))
                Line((-10, 0), (-10, -5))
                Line((9, -5), (-10, -5))
                Line((9, -5), (9, 0))
            make_face()
        # OneSide extrude, distance=-15
        extrude(amount=-15, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -6), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 36, perimeter: 26
            with BuildLine():
                Line((9, 1), (9, 5))
                Line((18, 1), (9, 1))
                Line((18, 5), (18, 1))
                Line((9, 5), (18, 5))
            make_face()
        # OneSide extrude, distance=-12
        extrude(amount=-12, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 8 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 6, perimeter: 10
            with BuildLine():
                Line((16, 3), (16, 5))
                Line((16, 5), (13, 5))
                Line((13, 5), (13, 3))
                Line((13, 3), (16, 3))
            make_face()
            # Profile area: 6, perimeter: 10
            with BuildLine():
                Line((13, -2), (16, -2))
                Line((13, -4), (13, -2))
                Line((16, -4), (13, -4))
                Line((16, -2), (16, -4))
            make_face()
        # OneSide extrude, distance=-5
        extrude(amount=-5, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(-18, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 16.5, perimeter: 25
            with BuildLine():
                Line((5.5, 3), (-5.5, 3))
                Line((5.5, 4.5), (5.5, 3))
                Line((-5.5, 4.5), (5.5, 4.5))
                Line((-5.5, 3), (-5.5, 4.5))
            make_face()
        # OneSide extrude, distance=-9
        extrude(amount=-9, mode=Mode.SUBTRACT)

        # Sketch6 -> Extrude6 (Join)
        # Sketch on BRepFace
        # Sketch has 12 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 6, perimeter: 10
            with BuildLine():
                Line((-13, 3), (-16, 3))
                Line((-13, 5), (-13, 3))
                Line((-16, 5), (-13, 5))
                Line((-16, 3), (-16, 5))
            make_face()
            # Profile area: 6, perimeter: 10
            with BuildLine():
                Line((-13, -4), (-16, -4))
                Line((-13, -2), (-13, -4))
                Line((-16, -2), (-13, -2))
                Line((-16, -4), (-16, -2))
            make_face()
        # OneSide extrude, distance=-2
        extrude(amount=-2, mode=Mode.ADD)
    return part.part


# Description: This is a mounting base or stand with a rectangular platform featuring an angled support bracket and a vertical cylindrical post for attaching components.
def model_55119_643f4796_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 150, perimeter: 50
            with BuildLine():
                Line((0, -10), (0, 0))
                Line((0, 0), (-15, 0))
                Line((-15, 0), (-15, -10))
                Line((-15, -10), (0, -10))
            make_face()
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)

        # Sketch3 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 8 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 12, perimeter: 16
            with BuildLine():
                Line((3, 8), (5, 8))
                Line((3, 2), (3, 8))
                Line((5, 2), (3, 2))
                Line((5, 8), (5, 2))
            make_face()
            # Profile area: 12.2120719299, perimeter: 16.0706906433
            with BuildLine():
                Line((10, 8), (10, 2))
                Line((10, 2), (12.0353453216, 2))
                Line((12.0353453216, 2), (12.0353453216, 8))
                Line((12.0353453216, 8), (10, 8))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)

        # Sketch7 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-10, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 5.9088468024, perimeter: 14.0000000894
            with BuildLine():
                Line((-3.0000000447, 2.5000000373), (-2, 2.5))
                Line((-2, 2.5), (-0.958110934, 8.4088465181))
                Line((-0.958110934, 8.4088465181), (-1.9581109787, 8.4088465553))
                Line((-3.0000000447, 2.5000000373), (-1.9581109787, 8.4088465553))
            make_face()
        # OneSide extrude, distance=-2
        extrude(amount=-2, mode=Mode.ADD)

        # Sketch8 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(-10, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.2858659037, perimeter: 3.510066123
            with BuildLine():
                CenterArc((-3.2135456506, 2.7139808405), 1.2322665483, -80.1172069736, 70.1172069736)
                Line((-3.0020477428, 1.5), (-2, 1.5))
                Line((-2, 1.5), (-2, 2.5))
            make_face()
        # OneSide extrude, distance=-2.1
        extrude(amount=-2.1, mode=Mode.SUBTRACT)

        # Sketch9 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(-3, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 6, perimeter: 14
            with BuildLine():
                Line((-2, 2.5), (-8, 2.5))
                Line((-8, 2.5), (-8, 1.5))
                Line((-8, 1.5), (-2, 1.5))
                Line((-2, 2.5), (-2, 1.5))
            make_face()
        # OneSide extrude, distance=-2.2
        extrude(amount=-2.2, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a toroidal (doughnut-shaped) ring or bushing with a hollow center and meshed surface texture, featuring a smooth outer curved profile and a symmetrical geometric form.
def model_55232_aeefe2c8_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 763.4106324303, perimeter: 97.945397738
            Circle(15.5884942031)
        # OneSide extrude, distance=10
        extrude(amount=10)

        # Sketch3 -> Extrude2 (Cut)
        # Sketch on XY construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 276.6732259013, perimeter: 58.9642119912
            Circle(9.3844458039)
        # OneSide extrude, distance=10
        extrude(amount=10, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude3 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 7 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 11.4989877134, perimeter: 16.1430507148
            with BuildLine():
                CenterArc((0, 0), 9.3844458039, 68.2998178863, 41.7775081669)
                Line((-3.2215679614, 8.814154691), (-3.2215679614, 7.4623337673))
                Line((-3.2215679614, 7.4623337673), (3.4698961192, 7.4623337673))
                Line((3.4698961192, 7.4623337673), (3.4698961192, 8.7193832333))
            make_face()
        # OneSide extrude, distance=-3
        extrude(amount=-3)
    return part.part


# Description: This is a valve or flow control component consisting of a rounded rectangular body (top) connected to a circular disk with a central axle/shaft (bottom), featuring two opposing rectangular slots through the disk that allow rotational control of fluid or gas flow.
def model_55279_5d386bad_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 4.9087385212, perimeter: 7.853981634
            Circle(1.25)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 2.9266095057, perimeter: 6.0643927719
            Circle(0.9651780865)
        # OneSide extrude, distance=0.7
        extrude(amount=0.7, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.9163715758, perimeter: 4.907324674
            Circle(0.7810249792)
        # OneSide extrude, distance=0.4
        extrude(amount=0.4)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.4084070571, perimeter: 2.2654347136
            Circle(0.3605551329)
        # OneSide extrude, distance=0.6
        extrude(amount=0.6, mode=Mode.SUBTRACT)

        # Sketch18 -> Extrude5 (NewBody)
        # Sketch on YZ construction plane
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.5707963268, perimeter: 4.4428829382
            with Locations((3.5, 2.5)):
                Circle(0.7071067812)
        # OneSide extrude, distance=2
        extrude(amount=2)

        # Sketch20 -> Extrude6 (Join)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.4084070571, perimeter: 2.2654347136
            Circle(0.3605551329)
        # OneSide extrude, distance=4.5
        extrude(amount=4.5, mode=Mode.ADD)
    return part.part


# Description: This is a adjustable solar panel mount consisting of a base bracket with a cylindrical post that tilts to support and angle a flat solar panel array for optimal sun exposure.
def model_55327_eb2ad109_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 27.53749481, perimeter: 23.6335652675
            with BuildLine():
                Line((11.1234591141, 1.8066764803), (2.5, 1.8066764803))
                Line((11.1234591141, 5), (11.1234591141, 1.8066764803))
                Line((2.5, 5), (11.1234591141, 5))
                Line((2.5, 1.8066764803), (2.5, 5))
            make_face()
        # OneSide extrude, distance=2.5
        extrude(amount=2.5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 2.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.3719709456, perimeter: 4.152191635
            with Locations((-6.3215880777, -3.7264980532)):
                Circle(0.6608418234)
        # OneSide extrude, distance=11
        extrude(amount=11, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 4.25, perimeter: 11.0322475511
            with BuildLine():
                Line((14, 16.5), (9.5, 16.5))
                Line((14.5, 17.5), (14, 16.5))
                Line((10.5, 17.5), (14.5, 17.5))
                Line((9.5, 16.5), (10.5, 17.5))
            make_face()
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5)

        # Sketch4 -> Extrude4 (NewBody)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 17.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.3926990817, perimeter: 2.5707963268
            with BuildLine():
                CenterArc((-14, -0.5), 0.5, -180, 180)
                Line((-14.5, -0.5), (-13.5, -0.5))
            make_face()
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)

        # Sketch5 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 19, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 44.6073009183, perimeter: 27.5707963268
            with BuildLine():
                Line((-14.5, -0.5), (-21, -0.5))
                Line((-21, -0.5), (-21, -6.5))
                Line((-21, -6.5), (-13.5, -6.5))
                Line((-13.5, -6.5), (-13.5, -0.5))
                CenterArc((-14, -0.5), 0.5, 180, 180)
            make_face()
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.ADD)
    return part.part


# Description: This is a rectangular box or enclosure with an angled, hinged lid featuring vertical ribbed or slotted details on the upper surface, designed for compact storage or equipment housing with a tilted access cover.
def model_55373_ddd74d2f_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 900, perimeter: 120
            with BuildLine():
                Line((0, -30), (30, -30))
                Line((30, -30), (30, 0))
                Line((0, 0), (30, 0))
                Line((0, -30), (0, 0))
            make_face()
        # OneSide extrude, distance=5
        extrude(amount=5)

        # Sketch3 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 150, perimeter: 70
            with BuildLine():
                Line((-5, 0), (-5, 30))
                Line((0, 0), (-5, 0))
                Line((0, 30), (0, 0))
                Line((-5, 30), (0, 30))
            make_face()
        # OneSide extrude, distance=30
        extrude(amount=30, mode=Mode.ADD)

        # Sketch4 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(5, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.9314165294, perimeter: 10.7123889804
            with BuildLine():
                CenterArc((-27, 32), 3, 90, 90)
                Line((-27, 35), (-30, 35))
                Line((-30, 35), (-30, 32))
            make_face()
            # Profile area: 1.9314165294, perimeter: 10.7123890425
            with BuildLine():
                CenterArc((-3, 32), 3, -0.0000005935, 90.0000005935)
                Line((0, 31.9999999689), (0, 35))
                Line((0, 35), (-3, 35))
            make_face()
        # OneSide extrude, distance=-5
        extrude(amount=-5, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(5, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 60, perimeter: 46
            with BuildLine():
                Line((-5, 5), (-5, 8))
                Line((-5, 8), (-25, 8))
                Line((-25, 8), (-25, 5))
                Line((-25, 5), (-5, 5))
            make_face()
        # OneSide extrude, distance=-5
        extrude(amount=-5, mode=Mode.SUBTRACT)

        # Sketch6 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 16 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 50, perimeter: 45
            with BuildLine():
                Line((5, 30), (5, 10))
                Line((5, 10), (7.5, 10))
                Line((7.5, 10), (7.5, 30))
                Line((7.5, 30), (5, 30))
            make_face()
            # Profile area: 50, perimeter: 45
            with BuildLine():
                Line((10, 30), (10, 10))
                Line((10, 10), (12.5, 10))
                Line((12.5, 10), (12.5, 30))
                Line((12.5, 30), (10, 30))
            make_face()
            # Profile area: 50, perimeter: 45
            with BuildLine():
                Line((17.5, 30), (20, 30))
                Line((17.5, 10), (17.5, 30))
                Line((20, 10), (17.5, 10))
                Line((20, 30), (20, 10))
            make_face()
            # Profile area: 50, perimeter: 45
            with BuildLine():
                Line((22.5, 30), (25, 30))
                Line((22.5, 10), (22.5, 30))
                Line((25, 10), (22.5, 10))
                Line((25, 30), (25, 10))
            make_face()
        # OneSide extrude, distance=-2
        extrude(amount=-2, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a torus or ring-shaped seal/gasket with a circular cross-section, featuring a uniform toroidal geometry with textured or reinforced surface patterns visible on portions of the outer diameter.
def model_55376_85564033_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch8 -> Extrude6 (NewBody)
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
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch12 -> Extrude9 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((0, -0.2500000037)):
                Circle(0.25)
        # OneSide extrude, distance=200
        extrude(amount=200, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a robotic gripper or end-effector assembly featuring a central cylindrical shaft with two opposing angular jaw/claw mechanisms that have textured gripping surfaces and are designed to grasp or manipulate objects.
def model_55472_b5c56340_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 9 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1323.2854132356, perimeter: 177.1238898038
            with BuildLine():
                Line((25, 15), (25, 7.5))
                Line((-25, 15), (25, 15))
                Line((-25, 7.5), (-25, 15))
                CenterArc((-25, 0), 7.5, -90, 180)
                Line((-25, -15), (-25, -7.5))
                Line((25, -15), (-25, -15))
                Line((25, -7.5), (25, -15))
                CenterArc((25, 0), 7.5, 90, 180)
            make_face()
        # OneSide extrude, distance=10
        extrude(amount=10)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 12 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(10, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 375, perimeter: 115
            with BuildLine():
                Line((25, 7.5), (-25, 7.5))
                Line((25, 15), (25, 7.5))
                Line((-25, 15), (25, 15))
                Line((-25, 7.5), (-25, 15))
            make_face()
            # Profile area: 375, perimeter: 115
            with BuildLine():
                Line((-25, -7.5), (-25, -15))
                Line((-25, -15), (25, -15))
                Line((25, -15), (25, -7.5))
                Line((25, -7.5), (-25, -7.5))
            make_face()
        # OneSide extrude, distance=10
        extrude(amount=10, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -15, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 41.9894602907, perimeter: 26.5832376675
            with BuildLine():
                CenterArc((10, 0), 5.1702341003, 90, 180)
                Line((10, 5.1702341003), (10, -5.1702341003))
            make_face()
            # Profile area: 41.9894602907, perimeter: 26.5832376675
            with BuildLine():
                Line((10, 5.1702341003), (10, -5.1702341003))
                CenterArc((10, 0), 5.1702341003, -90, 180)
            make_face()
        # OneSide extrude, distance=-35
        extrude(amount=-35, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (NewBody)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -7.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 77.4370520028, perimeter: 47.592739892
            with BuildLine():
                Line((-20, 11.1803398875), (-20, -11.1803398875))
                CenterArc((-10, 0), 15, 131.8103148958, 96.3793702084)
            make_face()
        # OneSide extrude, distance=15
        extrude(amount=15)

        # Sketch5 -> Extrude5 (NewBody)
        # Sketch on XZ construction plane
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 49.7086977141, perimeter: 24.9931574282
            with Locations((10, 0)):
                Circle(3.9777845482)
        # TwoSides extrude (symmetric), distance=25
        extrude(amount=25, both=True)

        # Sketch7 -> Extrude6 (NewBody)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 5.8801833052, perimeter: 8.5960783322
            with Locations((10, 29.6294834848)):
                Circle(1.3681083578)
        # Symmetric extrude, each_side=7.5
        extrude(amount=7.5, both=True)
    return part.part


# Description: This is a paddle or impeller component featuring a large circular disk with a cylindrical shaft protruding from one side and textured/meshed surfaces on the edges, designed for fluid mixing or agitation applications.
def model_55611_69142616_0008():
    """Model: clutch"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            with Locations((15, 12.5)):
                Circle(1)
        # OneSide extrude, distance=3
        extrude(amount=3)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.2916, perimeter: 2.16
            with BuildLine():
                Line((-15.27, 12.77), (-14.73, 12.77))
                Line((-15.27, 12.23), (-15.27, 12.77))
                Line((-14.73, 12.23), (-15.27, 12.23))
                Line((-14.73, 12.77), (-14.73, 12.23))
            make_face()
        # OneSide extrude, distance=-1.5
        extrude(amount=-1.5, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 3), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 3.926990817, perimeter: 15.7079632679
            with BuildLine():
                CenterArc((15, 12.5), 1.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((15, 12.5), 1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            with Locations((15, 12.5)):
                Circle(1)
        # OneSide extrude, distance=1.5
        extrude(amount=1.5, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 4.5), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 43.1968989869, perimeter: 34.5575191895
            with BuildLine():
                CenterArc((15, 12.5), 4, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((15, 12.5), 1.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 7.0685834706, perimeter: 9.4247779608
            with Locations((15, 12.5)):
                Circle(1.5)
        # OneSide extrude, distance=1.5
        extrude(amount=1.5, mode=Mode.ADD)

        # Sketch6 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 6), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            with Locations((15, 12.5)):
                Circle(1)
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.SUBTRACT)

        # Sketch7 -> Extrude6 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 4.5), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            with Locations((-15, 15.2000002265)):
                Circle(0.4)
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            with Locations((-15, 9.8)):
                Circle(0.4)
        # OneSide extrude, distance=-3
        extrude(amount=-3, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a circular flange or disc with a central mounting hole, featuring a rounded boss or protrusion on the top edge and textured surface details along one side, designed for mechanical assembly or connection purposes.
def model_55611_69142616_0010():
    """Model: rotor"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 113.0973355292, perimeter: 37.6991118431
            with Locations((12.5, 10)):
                Circle(6)
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 50.2654824574, perimeter: 25.1327412287
            with Locations((-12.5, 10)):
                Circle(4)
        # OneSide extrude, distance=3
        extrude(amount=3, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -3), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            with Locations((-12.5, 10)):
                Circle(1)
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -3), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            with Locations((-12.5, 12.7)):
                Circle(0.4)
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            with Locations((-12.5, 7.3)):
                Circle(0.4)
        # OneSide extrude, distance=-0.8
        extrude(amount=-0.8, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1, perimeter: 4
            with BuildLine():
                Line((13, 9.5), (13, 10.5))
                Line((13, 10.5), (12, 10.5))
                Line((12, 10.5), (12, 9.5))
                Line((12, 9.5), (13, 9.5))
            make_face()
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.SUBTRACT)

        # Sketch6 -> Extrude6 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.2768603765, perimeter: 4.3424307068
            with BuildLine():
                CenterArc((-12.5, 10), 4, 90, 2.473199293)
                CenterArc((-13.036361091, 14.641718732), 0.8363528866, -50.1104614145, 137.0207347367)
                CenterArc((-12.9966718389, 15.3770012198), 0.1, 86.9102733222, 9.2205649561)
                Line((-13.0073517627, 15.4764292804), (-13.175049704, 15.4584162444))
                CenterArc((-13.2134645568, 14.6278165897), 0.8314875148, -49.423079403, 136.7750628714)
            make_face()
        # OneSide extrude, distance=2.5
        extrude(amount=2.5, mode=Mode.ADD)
    return part.part


# Description: This is a rectangular box-shaped component with a prominent pyramidal or wedge-shaped protrusion on the upper surface, featuring a faceted/low-poly geometric design with angular surfaces and internal geometric structure visible through transparent faces.
def model_56047_f7d96d9b_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 56, perimeter: 30
            with BuildLine():
                Line((3.5, -4), (3.5, 4))
                Line((3.5, 4), (-3.5, 4))
                Line((-3.5, 4), (-3.5, -4))
                Line((-3.5, -4), (3.5, -4))
            make_face()
        # Symmetric extrude, each_side=1
        extrude(amount=1, both=True)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.5, perimeter: 7
            with BuildLine():
                Line((-0.5, -1.5), (0.5, -1.5))
                Line((-0.5, -4), (-0.5, -1.5))
                Line((0.5, -4), (-0.5, -4))
                Line((0.5, -1.5), (0.5, -4))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 38.5, perimeter: 25
            with BuildLine():
                Line((3.5, 4), (-3.5, 4))
                Line((-3.5, -1.5), (-3.5, 4))
                Line((-0.5, -1.5), (-3.5, -1.5))
                Line((-0.5, -1.5), (0.5, -1.5))
                Line((3.5, -1.5), (0.5, -1.5))
                Line((3.5, 4), (3.5, -1.5))
            make_face()
        # OneSide extrude, distance=1.5
        extrude(amount=1.5, mode=Mode.ADD)

        # Sketch23 -> Extrude12 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 5.7306725946, perimeter: 10.8392195034
            with BuildLine():
                Line((-1.7700075928, 2.4795961463), (-1.7700075928, -1.5))
                Line((-3.2100211982, 2.4795961463), (-1.7700075928, 2.4795961463))
                Line((-3.2100211982, -1.5), (-3.2100211982, 2.4795961463))
                Line((-1.7700075928, -1.5), (-3.2100211982, -1.5))
            make_face()
            # Profile area: 1.3974620994, perimeter: 4.8209284552
            with BuildLine():
                Line((-1.7700075928, -1.5), (-1.7700075928, -2.4704506222))
                Line((-1.7700075928, -1.5), (-3.2100211982, -1.5))
                Line((-3.2100211982, -2.4704506222), (-3.2100211982, -1.5))
                Line((-1.7700075928, -2.4704506222), (-3.2100211982, -2.4704506222))
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)
    return part.part


# Description: This is a circular fan or pulley wheel with a large flat disc center, a raised cylindrical hub, and a perforated mesh or ventilation pattern around the outer rim.
def model_56065_00bbe5da_0018():
    """Model: Heat_Exchange_Piston_Exhaust v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 9.3482016398, perimeter: 10.8384946549
            Circle(1.725)
        # Symmetric extrude, each_side=0.05
        extrude(amount=0.05, both=True)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.05), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 9.0792027689, perimeter: 10.6814150222
            Circle(1.7)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.35), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 2.5446900494, perimeter: 5.6548667765
            Circle(0.9)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.55), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            Circle(0.4)
        # OneSide extrude, distance=0.9
        extrude(amount=0.9, mode=Mode.ADD)

        # Sketch5 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1.45), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            Circle(0.25)
        # OneSide extrude, distance=-3.5
        extrude(amount=-3.5, mode=Mode.SUBTRACT)

        # Sketch6 -> Extrude6 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.55), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0490873852, perimeter: 0.7853981634
            with Locations((0, 0.6000000089)):
                Circle(0.125)
        # OneSide extrude, distance=-2.1
        extrude(amount=-2.1, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a dark blue parallelogram-shaped frame or bracket with a hollow center, two small rectangular cutouts on the right side, and slanted edges giving it a skewed, three-dimensional appearance.
def model_56127_3a60f829_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch2 -> Extrude2 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 5 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 157.5, perimeter: 57
            with BuildLine():
                Line((-20.8097869983, -9.6324778246), (-20.8097869983, 11.3675221754))
                Line((-13.3097869983, -9.6324778246), (-20.8097869983, -9.6324778246))
                Line((-13.3097869983, 11.3675221754), (-13.3097869983, -9.6324778246))
                Line((-20.8097869983, 11.3675221754), (-13.3097869983, 11.3675221754))
            make_face()
            # Profile area: 157.5, perimeter: 57
            with BuildLine():
                Line((-20.8097869983, 11.3675221754), (-28.3097869983, 11.3675221754))
                Line((-28.3097869983, 11.3675221754), (-28.3097869983, -9.6324778246))
                Line((-28.3097869983, -9.6324778246), (-20.8097869983, -9.6324778246))
                Line((-20.8097869983, -9.6324778246), (-20.8097869983, 11.3675221754))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on XY construction plane
        # Sketch has 12 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 34.115069186, perimeter: 29.0981151957
            with BuildLine():
                Line((-14.4495309831, -0.9447638032), (-17.3877364476, -0.9447638032))
                Line((-14.4495309831, 10.6660883301), (-14.4495309831, -0.9447638032))
                Line((-17.3877364476, 10.6660883301), (-14.4495309831, 10.6660883301))
                Line((-17.3877364476, -0.9447638032), (-17.3877364476, 10.6660883301))
            make_face()
        # OneSide extrude, distance=6
        extrude(amount=6, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 8 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 6.1082352753, perimeter: 10.0342108849
            with BuildLine():
                Line((17.3877364476, -4.5028158546), (14.4495309831, -4.5028158546))
                Line((17.3877364476, -2.4239158767), (17.3877364476, -4.5028158546))
                Line((14.4495309831, -2.4239158767), (17.3877364476, -2.4239158767))
                Line((14.4495309831, -4.5028158546), (14.4495309831, -2.4239158767))
            make_face()
            # Profile area: 6.4637027749, perimeter: 10.2979142188
            with BuildLine():
                Line((17.4292712478, -8.1405832676), (14.4495309831, -8.1405832676))
                Line((17.4292712478, -5.971366423), (17.4292712478, -8.1405832676))
                Line((14.4495309831, -5.971366423), (17.4292712478, -5.971366423))
                Line((14.4495309831, -8.1405832676), (14.4495309831, -5.971366423))
            make_face()
        # OneSide extrude, distance=-8
        extrude(amount=-8, mode=Mode.SUBTRACT)

        # Sketch6 -> Extrude6 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 140.1910772354, perimeter: 52.0847393562
            with BuildLine():
                Line((-19.3973184024, -8.4396880805), (-27, -8.4396880805))
                Line((-19.3973184024, 10), (-19.3973184024, -8.4396880805))
                Line((-27, 10), (-19.3973184024, 10))
                Line((-27, -8.4396880805), (-27, 10))
            make_face()
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.SUBTRACT)

        # Sketch8 -> Extrude8 (NewBody)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(-19.3973184024, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.0107141759, perimeter: 0.4246362974
            with BuildLine():
                Line((0.0194589345, -8.1405832676), (0.1846358849, -8.1405832676))
                CenterArc((0.1020474097, -8.1405832676), 0.0825884752, 0, 180)
            make_face()
            # Profile area: 0.0107141759, perimeter: 0.4246362974
            with BuildLine():
                CenterArc((0.1020474097, -8.1405832676), 0.0825884752, 180, 180)
                Line((0.0194589345, -8.1405832676), (0.1846358849, -8.1405832676))
            make_face()
        # OneSide extrude, distance=7.6
        extrude(amount=7.6)

        # Sketch11 -> Extrude11 (NewBody)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.4436077013, perimeter: 2.3617586624
            with BuildLine():
                Line((13.3097869983, -0.166042974), (13.3097869983, -0.3000154407))
                CenterArc((13.6797719231, -0.2330292073), 0.376, -169.7376950483, 339.4753900966)
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


# Description: This is an oval or elliptical mesh/perforated screen component featuring concentric circular patterns with radial line texturing, a solid central hub or core, and a hollow, latticed outer shell structure designed for filtration, ventilation, or acoustic purposes.
def model_56252_f65e7429_0005():
    """Model: wheel"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 176.7145867644, perimeter: 47.1238898038
            Circle(7.5)
        # OneSide extrude, distance=3
        extrude(amount=3)

        # Sketch3 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(3, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 100.5309649149, perimeter: 50.2654824574
            with BuildLine():
                CenterArc((0, 0), 6, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 100.5309649149, perimeter: 50.2654824574
            with BuildLine():
                CenterArc((0, 0), 6, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(3, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            Circle(0.5)
        # OneSide extrude, distance=-3
        extrude(amount=-3, mode=Mode.SUBTRACT)

        # Sketch6 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 7 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(3, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0972293472, perimeter: 1.3447992007
            with BuildLine():
                Line((-0.233118905, 7.2902519259), (-0.233118905, 7.4963761629))
                Line((0.233118905, 7.2902519259), (-0.233118905, 7.2902519259))
                Line((0.233118905, 7.4963761629), (0.233118905, 7.2902519259))
                CenterArc((0, 0), 7.5, 88.2188158632, 3.5623682736)
            make_face()
        # OneSide extrude, distance=-3
        extrude(amount=-3, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a complex hexagonal or multi-faceted mechanical housing with angled planar surfaces, featuring a prominent circular opening or boss on the left side and internal geometric subdivisions, designed as an enclosure or mounting structure with multiple intersecting faces and geometric complexity.
def model_56482_33e4f73c_0009():
    """Model: Bevel gearbox 180'"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 13 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 136, perimeter: 50
            with BuildLine():
                Line((0, 0), (14, 0))
                Line((14, 0), (14, 8))
                Line((14, 8), (11, 8))
                Line((11, 8), (11, 11))
                Line((3, 11), (11, 11))
                Line((3, 8), (3, 11))
                Line((0, 8), (3, 8))
                Line((0, 0), (0, 8))
            make_face()
        # OneSide extrude, distance=8
        extrude(amount=8)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(14, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 19.6349540849, perimeter: 15.7079632679
            with Locations((-4, 4)):
                Circle(2.5)
        # OneSide extrude, distance=-0.8
        extrude(amount=-0.8, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 11, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 19.6349540849, perimeter: 15.7079632679
            with Locations((-7, 4)):
                Circle(2.5)
        # OneSide extrude, distance=-0.8
        extrude(amount=-0.8, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 19.6349540849, perimeter: 15.7079632679
            with Locations((4, 4)):
                Circle(2.5)
        # OneSide extrude, distance=-0.8
        extrude(amount=-0.8, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(13.2, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))) as sk:
            # Profile area: 9.6211275016, perimeter: 10.9955742876
            with Locations((-4, 4)):
                Circle(1.75)
        # TwoSides extrude, along=0.9, against=-13.3
        extrude(amount=0.9, mode=Mode.ADD)
        extrude(sk.sketch, amount=-13.3, mode=Mode.ADD)

        # Sketch6 -> Extrude6 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 10.2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 9.6211275016, perimeter: 10.9955742876
            with Locations((-7, 4)):
                Circle(1.75)
        # OneSide extrude, distance=0.9
        extrude(amount=0.9, mode=Mode.ADD)

        # Sketch9 -> Extrude9 (Cut)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(14, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((-7.5, 7.5)):
                Circle(0.2)
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((-0.5, 7.5)):
                Circle(0.2)
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((-7.5, 0.5)):
                Circle(0.2)
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((-0.5, 0.5)):
                Circle(0.2)
        # OneSide extrude, distance=-15
        extrude(amount=-15, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a structural bracket or frame assembly featuring an angular, zigzag configuration with multiple interconnected rectangular tubular sections and triangulated reinforcement panels, designed to provide rigidity while minimizing weight.
def model_57736_91b94db5_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 400, perimeter: 100
            with BuildLine():
                Line((0, 10), (0, 0))
                Line((0, 0), (40, 0))
                Line((40, 0), (40, 10))
                Line((40, 10), (0, 10))
            make_face()
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 9 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 15, perimeter: 23
            with BuildLine():
                Line((-1.5, -10), (-1.5, 0))
                Line((0, -10), (-1.5, -10))
                Line((0, 0), (0, -10))
                Line((-1.5, 0), (0, 0))
            make_face()
            # Profile area: 15, perimeter: 23
            with BuildLine():
                Line((-30.5, 0), (-32, 0))
                Line((-32, 0), (-32, -10))
                Line((-32, -10), (-30.5, -10))
                Line((-30.5, -10), (-30.5, 0))
            make_face()
        # OneSide extrude, distance=6
        extrude(amount=6, mode=Mode.ADD)

        # Sketch5 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 7.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 385, perimeter: 97
            with BuildLine():
                Line((-40, 0), (-1.5, 0))
                Line((-40, -10), (-40, 0))
                Line((-1.5, -10), (-40, -10))
                Line((-1.5, 0), (-1.5, -10))
            make_face()
            # Profile area: 15, perimeter: 23
            with BuildLine():
                Line((-1.5, 0), (-1.5, -10))
                Line((0, -10), (-1.5, -10))
                Line((0, 0), (0, -10))
                Line((-1.5, 0), (0, 0))
            make_face()
        # OneSide extrude, distance=1.5
        extrude(amount=1.5, mode=Mode.ADD)

        # Sketch6 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 9, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 15, perimeter: 23
            with BuildLine():
                Line((-40, 0), (-40, -10))
                Line((-40, -10), (-38.5, -10))
                Line((-38.5, -10), (-38.5, 0))
                Line((-38.5, 0), (-40, 0))
            make_face()
        # OneSide extrude, distance=6
        extrude(amount=6, mode=Mode.ADD)

        # Sketch7 -> Extrude6 (Join)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 15, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 15, perimeter: 23
            with BuildLine():
                Line((-40, 0), (-40, -10))
                Line((-40, -10), (-38.5, -10))
                Line((-38.5, -10), (-38.5, 0))
                Line((-38.5, 0), (-40, 0))
            make_face()
            # Profile area: 385, perimeter: 97
            with BuildLine():
                Line((-38.5, -10), (-38.5, 0))
                Line((-38.5, -10), (0, -10))
                Line((0, -10), (0, 0))
                Line((0, 0), (-38.5, 0))
            make_face()
        # OneSide extrude, distance=1.5
        extrude(amount=1.5, mode=Mode.ADD)

        # Sketch9 -> Extrude7 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 9, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 15, perimeter: 23
            with BuildLine():
                Line((-9.5, -10), (-9.5, 0))
                Line((-8, -10), (-9.5, -10))
                Line((-8, 0), (-8, -10))
                Line((-9.5, 0), (-8, 0))
            make_face()
        # OneSide extrude, distance=6
        extrude(amount=6, mode=Mode.ADD)
    return part.part


# Description: This is a rectangular frame or structural assembly with a hexagonal-like overall shape, featuring multiple internal partitions, rectangular openings/slots on the sides, and a wireframe construction with interconnected geometric elements.
def model_57889_662c9748_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 87.5, perimeter: 39
            with BuildLine():
                Line((12.5, -7), (0, -7))
                Line((12.5, 0), (12.5, -7))
                Line((0, 0), (12.5, 0))
                Line((0, -7), (0, 0))
            make_face()
        # OneSide extrude, distance=7.5
        extrude(amount=7.5)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 20 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 7), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 13.75, perimeter: 16
            with BuildLine():
                Line((6, 4.5), (0.5, 4.5))
                Line((6, 7), (6, 4.5))
                Line((0.5, 7), (6, 7))
                Line((0.5, 4.5), (0.5, 7))
            make_face()
        # OneSide extrude, distance=-6.5
        extrude(amount=-6.5, mode=Mode.SUBTRACT)

        # Sketch2 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 20 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 7), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 12.6285778656, perimeter: 15.1028622925
            with BuildLine():
                Line((12.0514311463, 4.5), (7, 4.5))
                Line((12.0514311463, 7), (12.0514311463, 4.5))
                Line((7, 7), (12.0514311463, 7))
                Line((7, 4.5), (7, 7))
            make_face()
        # OneSide extrude, distance=-6.5
        extrude(amount=-6.5, mode=Mode.SUBTRACT)

        # Sketch2 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 20 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 7), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 11, perimeter: 15
            with BuildLine():
                Line((6, 2), (0.5, 2))
                Line((6, 4), (6, 2))
                Line((0.5, 4), (6, 4))
                Line((0.5, 2), (0.5, 4))
            make_face()
        # OneSide extrude, distance=-6.5
        extrude(amount=-6.5, mode=Mode.SUBTRACT)

        # Sketch2 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 20 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 7), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 10.1028622925, perimeter: 14.1028622925
            with BuildLine():
                Line((12.0514311463, 2), (7, 2))
                Line((12.0514311463, 4), (12.0514311463, 2))
                Line((7, 4), (12.0514311463, 4))
                Line((7, 2), (7, 4))
            make_face()
        # OneSide extrude, distance=-6.5
        extrude(amount=-6.5, mode=Mode.SUBTRACT)

        # Sketch2 -> Extrude6 (Cut)
        # Sketch on BRepFace
        # Sketch has 20 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 7), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 9.5, perimeter: 21
            with BuildLine():
                Line((11, 0.5), (1.5, 0.5))
                Line((11, 1.5), (11, 0.5))
                Line((1.5, 1.5), (11, 1.5))
                Line((1.5, 0.5), (1.5, 1.5))
            make_face()
        # OneSide extrude, distance=-6
        extrude(amount=-6, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude7 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(12.5, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 2.5, perimeter: 11
            with BuildLine():
                Line((-1, 0.5), (-6, 0.5))
                Line((-1, 1), (-1, 0.5))
                Line((-6, 1), (-1, 1))
                Line((-6, 0.5), (-6, 1))
            make_face()
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude8 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 5.25, perimeter: 22
            with BuildLine():
                Line((-1, 0.5), (-11.5, 0.5))
                Line((-1, 1), (-1, 0.5))
                Line((-11.5, 1), (-1, 1))
                Line((-11.5, 0.5), (-11.5, 1))
            make_face()
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude9 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 2.5, perimeter: 11
            with BuildLine():
                Line((6, 0.5), (1, 0.5))
                Line((6, 1), (6, 0.5))
                Line((1, 1), (6, 1))
                Line((1, 0.5), (1, 1))
            make_face()
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a hammer or mallet with a long tapered handle and a compact rectangular head, featuring a dark finish with visible surface details and markings.
def model_57975_464a2e4e_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 13.9528259028, perimeter: 25.8900954093
            with BuildLine():
                Line((-3.3699571265, 2.7950997744), (0.5, 2.7950997744))
                Line((-3.3699571265, 2.7950997744), (-3.3699571265, 1.116972857))
                Line((-3.3699571265, 1.116972857), (0.5, 1.116972857))
                Line((0.5, 1.116972857), (1.5, 1.4120726314))
                Line((1.5, 1.4120726314), (2.5014040014, 1.2645227442))
                Line((2.5014040014, 1.2645227442), (3.5699499437, 1.5798504107))
                Line((3.5699499437, 1.5798504107), (4.5, 1.4120726314))
                Line((4.5, 1.4120726314), (5.6246005129, 1.7439419891))
                Line((5.6246005129, 1.7439419891), (6.5, 1.4120726314))
                Line((6.5, 1.4120726314), (7.0623002565, 1.5780073102))
                Line((7.0623002565, 1.5780073102), (7.9268389677, 1.5780073102))
                Line((8.3433212473, 1.9560363157), (7.9268389677, 1.5780073102))
                Line((7.9268389677, 2.3340653212), (8.3433212473, 1.9560363157))
                Line((7.0623002565, 2.3340653212), (7.9268389677, 2.3340653212))
                Line((6.5, 2.5), (7.0623002565, 2.3340653212))
                Line((5.6246005129, 2.1681306423), (6.5, 2.5))
                Line((4.5, 2.5), (5.6246005129, 2.1681306423))
                Line((3.5699499437, 2.3322222207), (4.5, 2.5))
                Line((2.5014040014, 2.6475498872), (3.5699499437, 2.3322222207))
                Line((1.5, 2.5), (2.5014040014, 2.6475498872))
                Line((0.5, 2.7950997744), (1.5, 2.5))
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)

        # Sketch3 -> Extrude2 (NewBody)
        # Sketch on BRepFace
        # Sketch has 14 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.2, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 17.365989245, perimeter: 15.4113259795
            with BuildLine():
                CenterArc((-4.384155621, 1.0517740428), 1, -90, 90)
                Line((-3.384155621, 3), (-3.384155621, 1.0517740428))
                CenterArc((-4.384155621, 3), 1, 0, 90)
                Line((-7, 4), (-4.384155621, 4))
                CenterArc((-7, 3), 1, 90, 90)
                Line((-8, 1.0517740428), (-8, 3))
                CenterArc((-7, 1.0517740428), 1, 180, 90)
                Line((-4.384155621, 0.0517740428), (-7, 0.0517740428))
            make_face()
        # Symmetric extrude, each_side=0.5
        extrude(amount=0.5, both=True)

        # Sketch4 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 13 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0.7, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.7018974276, perimeter: 3.3688297341
            with BuildLine():
                Line((-6.0716767522, 2.2439083808), (-7, 2.2439083808))
                Line((-6.0716767522, 3), (-6.0716767522, 2.2439083808))
                Line((-7, 3), (-6.0716767522, 3))
                Line((-7, 2.2439083808), (-7, 3))
            make_face()
            # Profile area: 0.6341748159, perimeter: 3.2229266515
            with BuildLine():
                Line((-6.0716767522, 0.8168599221), (-7, 0.8168599221))
                Line((-6.0716767522, 1.5), (-6.0716767522, 0.8168599221))
                Line((-7, 1.5), (-6.0716767522, 1.5))
                Line((-7, 0.8168599221), (-7, 1.5))
            make_face()
            # Profile area: 0.6929845207, perimeter: 3.3509078049
            with BuildLine():
                Line((-4.2085857088, 1.5), (-5.1401312305, 1.5))
                Line((-4.2085857088, 2.2439083808), (-4.2085857088, 1.5))
                Line((-5.1401312305, 2.2439083808), (-4.2085857088, 2.2439083808))
                Line((-5.1401312305, 1.5), (-5.1401312305, 2.2439083808))
            make_face()
        # OneSide extrude, distance=0.1
        extrude(amount=0.1, mode=Mode.ADD)

        # Sketch5 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0.2, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 4.5047717438, perimeter: 23.7934828738
            with BuildLine():
                Line((8.1350801075, 2.1450508184), (8.1350801075, 1.767021813))
                Line((8.1350801075, 2.1450508184), (-3.3699571265, 2.1001173653))
                Line((-3.3699571265, 2.1001173653), (-3.3699571265, 1.6950508184))
                Line((-3.3699571265, 1.6950508184), (8.1350801075, 1.767021813))
            make_face()
        # OneSide extrude, distance=0.3
        extrude(amount=0.3, mode=Mode.ADD)

        # Sketch6 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.8, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0841138209, perimeter: 1.0281077024
            with Locations((-6.5358383761, 2.6219541904)):
                Circle(0.1636284229)
            # Profile area: 0.0839818402, perimeter: 1.0273007977
            with Locations((-4.6743584697, 1.9230493736)):
                Circle(0.1635)
            # Profile area: 0.0839818402, perimeter: 1.0273007977
            with Locations((-6.5358383761, 1.1608106967)):
                Circle(0.1635)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)

        # Sketch7 -> Extrude6 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0.7, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.1822309528, perimeter: 1.7790794014
            with BuildLine():
                Line((-3.9303731637, 3.1800871356), (-4.5, 3.1800871356))
                Line((-3.9303731637, 3.5), (-3.9303731637, 3.1800871356))
                Line((-4.5, 3.5), (-3.9303731637, 3.5))
                Line((-4.5, 3.1800871356), (-4.5, 3.5))
            make_face()
            # Profile area: 0.1503583486, perimeter: 1.5975114903
            with BuildLine():
                Line((-3.8891517241, 0.7480221947), (-4.384155621, 0.7480221947))
                Line((-3.8891517241, 1.0517740428), (-3.8891517241, 0.7480221947))
                Line((-4.384155621, 1.0517740428), (-3.8891517241, 1.0517740428))
                Line((-4.384155621, 0.7480221947), (-4.384155621, 1.0517740428))
            make_face()
        # OneSide extrude, distance=0.02
        extrude(amount=0.02, mode=Mode.ADD)
    return part.part


# Description: This is a pyramidal hopper or funnel assembly featuring a rectangular box base with a tapered pyramid-shaped top that narrows to a central opening, designed to funnel or direct material downward through the pointed apex.
def model_60295_e0b2e08b_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 21 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.2950025664, perimeter: 10.5180010266
            with BuildLine():
                Line((-3.7409994867, -2.5), (-4, -2.5))
                Line((-3.7409994867, 2.5), (-3.7409994867, -2.5))
                Line((-4, 2.5), (-3.7409994867, 2.5))
                Line((-4, -2.5), (-4, 2.5))
            make_face()
        # OneSide extrude, distance=5
        extrude(amount=5)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 21 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 11.931829679, perimeter: 46.9126833126
            with BuildLine():
                Line((4, -2.5), (-3.7409994867, -2.5))
                Line((4, 2.5), (4, -2.5))
                Line((-3.7409994867, 2.5), (4, 2.5))
                Line((-3.7409994867, 2.5), (-3.7409994867, -2.5))
            make_face()
            with BuildLine():
                Line((3.5, 1.967897111), (3.5, -2))
                Line((3.5, -2), (0, -2))
                Line((-3.2474450586, -2), (0, -2))
                Line((-3.2474450586, 1.967897111), (-3.2474450586, -2))
                Line((0, 1.967897111), (-3.2474450586, 1.967897111))
                Line((0, 1.967897111), (3.5, 1.967897111))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=2
        extrude(amount=2, mode=Mode.ADD)

        # Sketch1 -> Extrude3 (Join)
        # Sketch on XZ construction plane
        # Sketch has 21 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 13.8876398885, perimeter: 14.935794222
            with BuildLine():
                Line((0, 1.967897111), (3.5, 1.967897111))
                Line((0, -2), (0, 1.967897111))
                Line((3.5, -2), (0, -2))
                Line((3.5, 1.967897111), (3.5, -2))
            make_face()
            # Profile area: 12.8855278661, perimeter: 14.4306843392
            with BuildLine():
                Line((0, 1.967897111), (-3.2474450586, 1.967897111))
                Line((-3.2474450586, 1.967897111), (-3.2474450586, -2))
                Line((-3.2474450586, -2), (0, -2))
                Line((0, -2), (0, 1.967897111))
            make_face()
        # OneSide extrude, distance=1.5
        extrude(amount=1.5, mode=Mode.ADD)

        # Sketch7 -> Extrude8 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(-3.7409994867, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 5.3618195856, perimeter: 10.6980377212
            with BuildLine():
                Line((2.012859574, 2.1638407134), (-2, 2.1638407134))
                Line((2.012859574, 3.5), (2.012859574, 2.1638407134))
                Line((-2, 3.5), (2.012859574, 3.5))
                Line((-2, 2.1638407134), (-2, 3.5))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)

        # Sketch8 -> Extrude9 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 26.7002231305, perimeter: 21.3939169422
            with BuildLine():
                Line((-3.5, 2), (-3.5, -1.967897111))
                Line((-3.5, -1.967897111), (3.2290613601, -1.967897111))
                Line((3.2290613601, 2), (3.2290613601, -1.967897111))
                Line((3.2290613601, 2), (-3.5, 2))
            make_face()
            # Profile area: 1.2377832072, perimeter: 35.2855850827
            with BuildLine():
                Line((3.2290613601, 2), (-3.5, 2))
                Line((3.2290613601, 2.058650584), (3.2290613601, 2))
                Line((-3.584040101, 2.058650584), (3.2290613601, 2.058650584))
                Line((-3.584040101, -2.0419791362), (-3.584040101, 2.058650584))
                Line((3.2290613601, -2.0419791362), (-3.584040101, -2.0419791362))
                Line((3.2290613601, -1.967897111), (3.2290613601, -2.0419791362))
                Line((-3.5, -1.967897111), (3.2290613601, -1.967897111))
                Line((-3.5, 2), (-3.5, -1.967897111))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)

        # Sketch9 -> Extrude10 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(4, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 3.967897111, perimeter: 9.935794222
            with BuildLine():
                Line((1.967897111, 1), (1.967897111, 0))
                Line((-2, 1), (1.967897111, 1))
                Line((-2, 0), (-2, 1))
                Line((1.967897111, 0), (-2, 0))
            make_face()
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.SUBTRACT)

        # Sketch10 -> Extrude11 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -2.5), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 5.7957197018, perimeter: 15.8387881796
            with BuildLine():
                Line((3.6034974498, 0.18410336), (-3.5, 0.18410336))
                Line((3.6034974498, 1), (3.6034974498, 0.18410336))
                Line((-3.5, 1), (3.6034974498, 1))
                Line((-3.5, 0.18410336), (-3.5, 1))
            make_face()
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2, mode=Mode.SUBTRACT)

        # Sketch11 -> Extrude12 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 2.5), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 5.7957197018, perimeter: 15.8387881796
            with BuildLine():
                Line((3.5, 0.18410336), (-3.6034974498, 0.18410336))
                Line((3.5, 1), (3.5, 0.18410336))
                Line((-3.6034974498, 1), (3.5, 1))
                Line((-3.6034974498, 0.18410336), (-3.6034974498, 1))
            make_face()
        # OneSide extrude, distance=-0.3
        extrude(amount=-0.3, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a jaw or clamping fixture with an angular, irregular polygonal upper body, two parallel slot openings on the sides, and a cylindrical stem or mounting post extending downward for attachment.
def model_60567_4422df95_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 13 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 26.3783236591, perimeter: 19.0812026385
            with BuildLine():
                CenterArc((-1.2792407799, 4), 1, 90, 71.5650511771)
                Line((-2.227924078, 4.316227766), (-3, 2))
                Line((-3, 2), (-3, 1))
                CenterArc((-2, 1), 1, -180, 90)
                Line((-2, 0), (2, 0))
                CenterArc((2, 1), 1, -90, 90)
                Line((3, 1), (3, 2))
                Line((2.227924078, 4.316227766), (3, 2))
                CenterArc((1.2792407799, 4), 1, 18.4349488229, 71.5650511771)
                Line((-1.2792407799, 5), (1.2792407799, 5))
            make_face()
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 15 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1.5), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 7.5707963268, perimeter: 17.1415926536
            with BuildLine():
                Line((-2, 1), (-2, 2))
                Line((-3, 2), (-2, 2))
                Line((-3, 2), (-3, 1))
                CenterArc((-2, 1), 1, -180, 90)
                Line((2, 0), (-2, 0))
                CenterArc((2, 1), 1, -90, 90)
                Line((3, 2), (3, 1))
                Line((3, 2), (2, 2))
                Line((2, 1), (2, 2))
                Line((-2, 1), (2, 1))
            make_face()
        # OneSide extrude, distance=3.5
        extrude(amount=3.5, mode=Mode.ADD)

        # Sketch4 -> Extrude3 (Join)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 1.1309733553, perimeter: 3.7699111843
            with Locations((0.0013291675, 2.4)):
                Circle(0.6)
        # OneSide extrude, distance=2.8
        extrude(amount=2.8, mode=Mode.ADD)
    return part.part


# Description: This is an oval or egg-shaped enclosure with a ribbed or finned exterior surface, featuring an internal skeletal framework visible through semi-transparent walls, suggesting it may be a structural housing, air intake manifold, or aerodynamic component.
def model_60728_99f07543_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 19.6349540849, perimeter: 15.7079632679
            with Locations((-4, 2.5)):
                Circle(2.5)
        # OneSide extrude, distance=1.2
        extrude(amount=1.2)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.6832318219, perimeter: 3.3057689884
            with BuildLine():
                Line((3.5000000522, 4.3000000641), (3.5000000522, 4.9494897534))
                Line((4.5000000671, 4.3000000641), (3.5000000522, 4.3000000641))
                Line((4.5000000671, 4.9494897291), (4.5000000671, 4.3000000641))
                CenterArc((4, 2.5), 2.5, 78.4630393987, 23.0739184142)
            make_face()
        # OneSide extrude, distance=0.1
        extrude(amount=0.1, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.6832318964, perimeter: 3.3057691374
            with BuildLine():
                Line((4.5000000671, 0.0505102709), (4.5000000671, 0.7000000104))
                Line((4.5000000671, 0.7000000104), (3.5000000522, 0.7000000104))
                Line((3.5000000522, 0.7000000104), (3.5000000522, 0.0505102466))
                CenterArc((4, 2.5), 2.5, -101.5369578129, 23.0739184142)
            make_face()
        # OneSide extrude, distance=0.1
        extrude(amount=0.1, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.6832319188, perimeter: 3.3057691822
            with BuildLine():
                Line((2.2000000328, 2.0000000298), (1.5505102511, 2.0000000298))
                Line((2.2000000328, 3.0000000447), (2.2000000328, 2.0000000298))
                Line((1.5505102663, 3.0000000447), (2.2000000328, 3.0000000447))
                CenterArc((4, 2.5), 2.5, 168.4630399215, 23.0739184142)
            make_face()
        # OneSide extrude, distance=0.1
        extrude(amount=0.1, mode=Mode.ADD)

        # Sketch5 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.6832317996, perimeter: 3.3057689437
            with BuildLine():
                Line((6.4494897337, 3.0000000447), (5.8000000864, 3.0000000447))
                Line((5.8000000864, 3.0000000447), (5.8000000864, 2.0000000298))
                Line((5.8000000864, 2.0000000298), (6.4494897489, 2.0000000298))
                CenterArc((4, 2.5), 2.5, -11.5369583357, 23.0739184142)
            make_face()
        # OneSide extrude, distance=0.1
        extrude(amount=0.1, mode=Mode.ADD)
    return part.part


# Description: This is a balance scale or weighing platform featuring a central rectangular tray supported by a pedestal base, with two smaller hexagonal or octagonal pans positioned on either side for comparison weighing.
def model_60766_fb8715eb_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 46.25, perimeter: 42
            with BuildLine():
                Line((12, -1.5), (-6.5, -1.5))
                Line((12, 1), (12, -1.5))
                Line((-6.5, 1), (12, 1))
                Line((-6.5, -1.5), (-6.5, 1))
            make_face()
        # OneSide extrude, distance=5
        extrude(amount=5)

        # Sketch2 -> Extrude2 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 6.75, perimeter: 12.1097722286
            with BuildLine():
                Line((-12, 2), (-12, 1))
                Line((-12, 1), (-7.5, 1))
                Line((-7.5, 1), (-7.5, 3))
                Line((-7.5, 3), (-12, 2))
            make_face()
        # OneSide extrude, distance=2.5
        extrude(amount=2.5)

        # Sketch3 -> Extrude3 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 5.5273702174, perimeter: 12.1884549492
            with BuildLine():
                Line((6.5, 6.5), (11.3698269565, 5.75))
                Line((6.5, 5), (6.5, 6.5))
                Line((11.5, 5), (6.5, 5))
                Line((11.3698269565, 5.75), (11.5, 5))
            make_face()
        # OneSide extrude, distance=2.5
        extrude(amount=2.5)

        # Sketch4 -> Extrude5 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 7.5, perimeter: 13.0990195136
            with BuildLine():
                Line((12.5, 2.5), (17.5, 2.5))
                Line((17.5, 2.5), (17.5, 4.5))
                Line((17.5, 4.5), (12.5, 3.5))
                Line((12.5, 2.5), (12.5, 3.5))
            make_face()
        # OneSide extrude, distance=2.5
        extrude(amount=2.5)

        # Sketch5 -> Extrude6 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 13.6587385212, perimeter: 14.853981634
            with BuildLine():
                CenterArc((2.5, -5.25), 1.25, 90, 180)
                Line((2.5, -6.5), (6, -6.5))
                CenterArc((6, -5.25), 1.25, -90, 180)
                Line((2.5, -4), (6, -4))
            make_face()
        # OneSide extrude, distance=2.5
        extrude(amount=2.5)
    return part.part


# Description: This is a hexagonal or polygonal structural frame/enclosure with an open interior design featuring multiple internal bracing members, cross-supports, and triangulated reinforcement elements throughout its hollow body.
def model_60973_07d73016_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 19 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 30, perimeter: 34
            with BuildLine():
                Line((1.5, 2.5), (5, 2.5))
                Line((8.5, 2.5), (5, 2.5))
                Line((8.5, 0), (8.5, 2.5))
                Line((8.5, 0), (9.5, 0))
                Line((9.5, 0), (9.5, 5))
                Line((9.5, 5), (0, 5))
                Line((0, 5), (0, 0))
                Line((0, 0), (1.5, 0))
                Line((1.5, 0), (1.5, 2.5))
            make_face()
        # OneSide extrude, distance=5
        extrude(amount=5)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 19 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 8.75, perimeter: 12
            with BuildLine():
                Line((1.5, 0), (1.5, 2.5))
                Line((5, 0), (1.5, 0))
                Line((5, 2.5), (5, 0))
                Line((1.5, 2.5), (5, 2.5))
            make_face()
        # OneSide extrude, distance=1.5
        extrude(amount=1.5, mode=Mode.ADD)

        # Sketch1 -> Extrude3 (Join)
        # Sketch on XZ construction plane
        # Sketch has 19 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 8.75, perimeter: 12
            with BuildLine():
                Line((5, 0), (8.5, 0))
                Line((8.5, 0), (8.5, 2.5))
                Line((8.5, 2.5), (5, 2.5))
                Line((5, 2.5), (5, 0))
            make_face()
        # OneSide extrude, distance=1.5
        extrude(amount=1.5, mode=Mode.ADD)

        # Sketch2 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 8 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 6.4419532795, perimeter: 10.3497399702
            with BuildLine():
                Line((-4.7698665077, -0.2341633511), (-1.6795731244, -0.2341633511))
                Line((-4.7698665077, -2.3187399529), (-4.7698665077, -0.2341633511))
                Line((-1.6795731244, -2.3187399529), (-4.7698665077, -2.3187399529))
                Line((-1.6795731244, -0.2341633511), (-1.6795731244, -2.3187399529))
            make_face()
            # Profile area: 6.3275990793, perimeter: 10.2400254122
            with BuildLine():
                Line((-8.2807323633, -0.2341633511), (-5.245296259, -0.2341633511))
                Line((-8.2807323633, -2.3187399529), (-8.2807323633, -0.2341633511))
                Line((-5.245296259, -2.3187399529), (-8.2807323633, -2.3187399529))
                Line((-5.245296259, -0.2341633511), (-5.245296259, -2.3187399529))
            make_face()
        # OneSide extrude, distance=1.5
        extrude(amount=1.5, mode=Mode.ADD)

        # Sketch6 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.2042908051, perimeter: 14.7802627531
            with BuildLine():
                Line((1.2703758287, 0.9208731304), (1.2703758287, 0.7541526116))
                Line((8.4937866866, 0.7541526116), (1.2703758287, 0.7541526116))
                Line((8.4937866866, 0.9208731304), (8.4937866866, 0.7541526116))
                Line((1.2703758287, 0.9208731304), (8.4937866866, 0.9208731304))
            make_face()
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude6 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 2.3780761433, perimeter: 7.6817372056
            with BuildLine():
                Line((-0.9350169829, 0.2241144143), (-4, 0.2241144143))
                Line((-0.9350169829, 1), (-0.9350169829, 0.2241144143))
                Line((-4, 1), (-0.9350169829, 1))
                Line((-4, 0.2241144143), (-4, 1))
            make_face()
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude7 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -5), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 8.1197716699, perimeter: 16.3372205478
            with BuildLine():
                Line((-1.2703758287, 0.3417462607), (-8.2807323633, 0.3417462607))
                Line((-1.2703758287, 1.5), (-1.2703758287, 0.3417462607))
                Line((-8.2807323633, 1.5), (-1.2703758287, 1.5))
                Line((-8.2807323633, 0.3417462607), (-8.2807323633, 1.5))
            make_face()
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude8 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(9.5, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 2.3780761433, perimeter: 7.6817372056
            with BuildLine():
                Line((4, 0.2241144143), (0.9350169829, 0.2241144143))
                Line((4, 1), (4, 0.2241144143))
                Line((0.9350169829, 1), (4, 1))
                Line((0.9350169829, 0.2241144143), (0.9350169829, 1))
            make_face()
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a hollow rectangular duct or channel housing with a trapezoidal cross-section, featuring multiple internal and external walls, reinforcing ribs, and open apertures on the sides and bottom, designed for airflow or cable routing applications.
def model_61767_6afe5575_0002():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 300, perimeter: 80
            with BuildLine():
                Line((15, -5), (-15, -5))
                Line((15, 5), (15, -5))
                Line((-15, 5), (15, 5))
                Line((-15, -5), (-15, 5))
            make_face()
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)

        # Sketch3 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 9, perimeter: 13
            with BuildLine():
                Line((13, -5), (13, -0.5))
                Line((15, -5), (13, -5))
                Line((15, -0.5), (15, -5))
                Line((13, -0.5), (15, -0.5))
            make_face()
        # OneSide extrude, distance=8
        extrude(amount=8, mode=Mode.ADD)

        # Sketch4 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 9, perimeter: 13
            with BuildLine():
                Line((-13, -0.5), (-15, -0.5))
                Line((-15, -0.5), (-15, -5))
                Line((-15, -5), (-13, -5))
                Line((-13, -5), (-13, -0.5))
            make_face()
        # OneSide extrude, distance=8
        extrude(amount=8, mode=Mode.ADD)

        # Sketch5 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 25, perimeter: 30.6
            with BuildLine():
                Line((13, 1.5), (5, 1.5))
                Line((5, 1.5), (5, -0.3))
                Line((5, -0.3), (15, -0.3))
                Line((15, -0.3), (15, 5))
                Line((15, 5), (13, 5))
                Line((13, 5), (13, 1.5))
            make_face()
        # OneSide extrude, distance=8
        extrude(amount=8, mode=Mode.ADD)

        # Sketch6 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 8 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 25, perimeter: 30.6
            with BuildLine():
                Line((-13, 5), (-13, 1.5))
                Line((-15, 5), (-13, 5))
                Line((-15, -0.3), (-15, 5))
                Line((-5, -0.3), (-15, -0.3))
                Line((-5, 1.5), (-5, -0.3))
                Line((-13, 1.5), (-5, 1.5))
            make_face()
        # OneSide extrude, distance=8
        extrude(amount=8, mode=Mode.ADD)

        # Sketch7 -> Extrude6 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 42.4, perimeter: 26.6
            with BuildLine():
                Line((-4, 5), (-4, -0.3))
                Line((-4, -0.3), (4, -0.3))
                Line((4, -0.3), (4, 5))
                Line((4, 5), (-4, 5))
            make_face()
        # OneSide extrude, distance=8
        extrude(amount=8, mode=Mode.ADD)
    return part.part


# Description: This is a long, flat rectangular panel or mounting bracket with a dark gray finish and blue accent details, featuring a horizontal elongated shape with angled edges at both ends and what appears to be mounting slots or channels along its length.
def model_63930_357170ca_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 28, perimeter: 32
            with BuildLine():
                Line((15, 1), (1, 1))
                Line((15, 3), (15, 1))
                Line((1, 3), (15, 3))
                Line((1, 1), (1, 3))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 2.5132744599, perimeter: 5.6198521617
            with Locations((3, 2)):
                Circle(0.894427251)
        # OneSide extrude, distance=-1.4
        extrude(amount=-1.4, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 3, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((-2.9863740839, 0.4910080221)):
                Circle(0.15)
        # OneSide extrude, distance=-2
        extrude(amount=-2, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 9 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1.0927763677, perimeter: 6.7438620398
            with BuildLine():
                Line((10.108729137, 2.5367980545), (7.1000001058, 2.5367980545))
                Line((10.108729137, 2.9000000432), (10.108729137, 2.5367980545))
                Line((7.1000001058, 2.9000000432), (10.108729137, 2.9000000432))
                Line((7.1000001058, 2.5367980545), (7.1000001058, 2.9000000432))
            make_face()
        # OneSide extrude, distance=-2.5
        extrude(amount=-2.5, mode=Mode.SUBTRACT)

        # Sketch6 -> Extrude5 (Join)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(7.1000001058, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0609526423, perimeter: 0.8751876899
            with Locations((-0.5000000075, 2.7000000402)):
                Circle(0.139290447)
        # OneSide extrude, distance=3
        extrude(amount=3, mode=Mode.ADD)

        # Sketch7 -> Extrude6 (Cut)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 0, 1), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 2.0178636154, perimeter: 5.0355955
            with Locations((13.3920941807, 2)):
                Circle(0.8014399152)
        # OneSide extrude, distance=-5
        extrude(amount=-5, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a rectangular frame or chassis component with a hollow box structure, featuring three horizontal shelves or levels separated by vertical walls, with rectangular cutout openings on the sides and a ribbed/latticed internal support structure for reinforcement.
def model_65715_433564a6_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 26 constraints, 22 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 18000, perimeter: 580
            with BuildLine():
                Line((210, 200), (90, 200))
                Line((10, 200), (90, 200))
                Line((10, 110), (10, 200))
                Line((210, 110), (10, 110))
                Line((210, 200), (210, 110))
            make_face()
            # Profile area: 6900, perimeter: 1400
            with BuildLine():
                Line((490, 10), (360, 10))
                Line((360, 10), (160, 10))
                Line((160, 10), (100, 10))
                Line((100, 10), (100, 0))
                Line((100, 0), (500, 0))
                Line((500, 0), (500, 300))
                Line((500, 300), (490, 300))
                Line((490, 300), (490, 210))
                Line((490, 210), (490, 200))
                Line((490, 10), (490, 200))
            make_face()
            # Profile area: 20000, perimeter: 900
            with BuildLine():
                Line((10, 310), (10, 360))
                Line((410, 310), (10, 310))
                Line((410, 310), (410, 360))
                Line((410, 360), (10, 360))
            make_face()
            # Profile area: 4000, perimeter: 820
            with BuildLine():
                Line((210, 110), (10, 110))
                Line((10, 100), (10, 110))
                Line((10, 100), (160, 100))
                Line((160, 100), (360, 100))
                Line((360, 100), (410, 100))
                Line((410, 100), (410, 110))
                Line((410, 110), (210, 110))
            make_face()
            # Profile area: 18000, perimeter: 580
            with BuildLine():
                Line((360, 100), (360, 10))
                Line((160, 100), (360, 100))
                Line((160, 10), (160, 100))
                Line((360, 10), (160, 10))
            make_face()
            # Profile area: 3600, perimeter: 740
            with BuildLine():
                Line((10, 100), (10, 110))
                Line((10, 110), (10, 200))
                Line((10, 300), (10, 200))
                Line((10, 300), (10, 310))
                Line((10, 310), (10, 360))
                Line((10, 360), (0, 360))
                Line((0, 360), (0, 0))
                Line((0, 0), (10, 0))
                Line((10, 0), (10, 100))
            make_face()
            # Profile area: 4000, perimeter: 820
            with BuildLine():
                Line((410, 310), (10, 310))
                Line((10, 300), (10, 310))
                Line((10, 300), (160, 300))
                Line((160, 300), (360, 300))
                Line((360, 300), (410, 300))
                Line((410, 300), (410, 310))
            make_face()
            # Profile area: 4000, perimeter: 820
            with BuildLine():
                Line((360, 210), (490, 210))
                Line((160, 210), (360, 210))
                Line((90, 210), (160, 210))
                Line((90, 200), (90, 210))
                Line((210, 200), (90, 200))
                Line((490, 200), (210, 200))
                Line((490, 210), (490, 200))
            make_face()
            # Profile area: 18000, perimeter: 580
            with BuildLine():
                Line((160, 300), (360, 300))
                Line((160, 210), (160, 300))
                Line((160, 210), (360, 210))
                Line((360, 300), (360, 210))
            make_face()
        # OneSide extrude, distance=100
        extrude(amount=100)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 100), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 20000, perimeter: 900
            with BuildLine():
                Line((410, 310), (410, 360))
                Line((410, 360), (10, 360))
                Line((10, 310), (10, 360))
                Line((10, 310), (410, 310))
            make_face()
        # OneSide extrude, distance=-40
        extrude(amount=-40, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 20000, perimeter: 900
            with BuildLine():
                Line((-10, 310), (-410, 310))
                Line((-10, 360), (-10, 310))
                Line((-10, 360), (-410, 360))
                Line((-410, 310), (-410, 360))
            make_face()
        # OneSide extrude, distance=-40
        extrude(amount=-40, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 8 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 16200, perimeter: 540
            with BuildLine():
                Line((-170, 300), (-350, 300))
                Line((-350, 300), (-350, 210))
                Line((-350, 210), (-170, 210))
                Line((-170, 210), (-170, 300))
            make_face()
            # Profile area: 16200, perimeter: 540
            with BuildLine():
                Line((-350, 100), (-350, 10))
                Line((-350, 10), (-170, 10))
                Line((-170, 100), (-170, 10))
                Line((-170, 100), (-350, 100))
            make_face()
        # OneSide extrude, distance=-90
        extrude(amount=-90, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 100), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 15200, perimeter: 540
            with BuildLine():
                Line((200, 190), (200, 110))
                Line((200, 190), (10, 190))
                Line((10, 110), (10, 190))
                Line((200, 110), (10, 110))
            make_face()
        # OneSide extrude, distance=-90
        extrude(amount=-90, mode=Mode.SUBTRACT)

        # Sketch6 -> Extrude6 (Cut)
        # Sketch on BRepFace
        # Sketch has 9 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 100), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 16200, perimeter: 540
            with BuildLine():
                Line((170, 300), (350, 300))
                Line((170, 300), (170, 210))
                Line((350, 210), (170, 210))
                Line((350, 300), (350, 210))
            make_face()
            # Profile area: 16200, perimeter: 540
            with BuildLine():
                Line((170, 10), (350, 10))
                Line((350, 100), (350, 10))
                Line((170, 100), (350, 100))
                Line((170, 10), (170, 100))
            make_face()
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.SUBTRACT)

        # Sketch7 -> Extrude7 (Cut)
        # Sketch on BRepFace
        # Sketch has 7 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 15200, perimeter: 540
            with BuildLine():
                Line((-10, 110), (-10, 190))
                Line((-10, 190), (-200, 190))
                Line((-200, 190), (-200, 110))
                Line((-200, 110), (-10, 110))
            make_face()
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a sheet metal component consisting of three dark panels with a bent/folded configuration, featuring a rectangular box-like structure with an open top and angled side walls, designed for containment or structural support purposes.
def model_66164_21e5e959_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 13 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 140, perimeter: 144
            with BuildLine():
                Line((148, 0), (148, -70))
                Line((150, -70), (148, -70))
                Line((150, 0), (150, -70))
                Line((148, 0), (150, 0))
            make_face()
            # Profile area: 140, perimeter: 144
            with BuildLine():
                Line((0, 0), (2, 0))
                Line((0, -70), (0, 0))
                Line((2, -70), (0, -70))
                Line((2, -70), (2, 0))
            make_face()
        # OneSide extrude, distance=80
        extrude(amount=80)

        # Sketch5 -> Extrude7 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1413.75, perimeter: 184
            with BuildLine():
                Line((100, 139.5), (100, 120))
                Line((100, 120), (172.5, 120))
                Line((172.5, 120), (172.5, 139.5))
                Line((172.5, 139.5), (100, 139.5))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch6 -> Extrude8 (Join)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.5), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 9.5, perimeter: 39
            with BuildLine():
                Line((100.5, 120.5), (100, 120.5))
                Line((100.5, 139.5), (100.5, 120.5))
                Line((100.5, 139.5), (100, 139.5))
                Line((100, 139.5), (100, 120.5))
            make_face()
            # Profile area: 45.5, perimeter: 183
            with BuildLine():
                Line((172.5, 120), (172.5, 139.5))
                Line((172.5, 139.5), (172, 139.5))
                Line((172, 120.5), (172, 139.5))
                Line((172, 120.5), (100.5, 120.5))
                Line((100.5, 120.5), (100.5, 120))
                Line((172.5, 120), (100.5, 120))
            make_face()
            # Profile area: 0.25, perimeter: 2
            with BuildLine():
                Line((100.5, 120.5), (100.5, 120))
                Line((100.5, 120.5), (100, 120.5))
                Line((100, 120.5), (100, 120))
                Line((100.5, 120), (100, 120))
            make_face()
        # OneSide extrude, distance=68.5
        extrude(amount=68.5, mode=Mode.ADD)

        # Sketch7 -> Extrude9 (NewBody)
        # Sketch on BRepFace
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 69), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1358.5, perimeter: 181
            with BuildLine():
                Line((100.5, 139.5), (172, 139.5))
                Line((100.5, 120.5), (100.5, 139.5))
                Line((172, 120.5), (100.5, 120.5))
                Line((172, 139.5), (172, 120.5))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch8 -> Extrude10 (Join)
        # Sketch on BRepFace
        # Sketch has 13 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 69.5), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 81.5, perimeter: 326
            with BuildLine():
                Line((102.5, 137.5), (102.5, 122.5))
                Line((102.5, 122.5), (170, 122.5))
                Line((170, 122.5), (170, 137.5))
                Line((170, 137.5), (102.5, 137.5))
            make_face()
            with BuildLine():
                Line((169.5, 137), (103, 137))
                Line((169.5, 123), (169.5, 137))
                Line((103, 123), (169.5, 123))
                Line((103, 137), (103, 123))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)

        # Sketch8 -> Extrude11 (Join)
        # Sketch on BRepFace
        # Sketch has 13 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 69.5), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 71.5, perimeter: 286
            with BuildLine():
                Line((167.5, 125), (105, 125))
                Line((167.5, 135), (167.5, 125))
                Line((105, 135), (167.5, 135))
                Line((105, 125), (105, 135))
            make_face()
            with BuildLine():
                Line((167, 134.5), (167, 125.5))
                Line((167, 125.5), (105.5, 125.5))
                Line((105.5, 125.5), (105.5, 134.5))
                Line((105.5, 134.5), (167, 134.5))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.4
        extrude(amount=0.4, mode=Mode.ADD)
    return part.part


# Description: This is a water pump or fluid impeller assembly featuring a rectangular block base with an integrated spiral/curved impeller mechanism and a protruding cylindrical shaft, designed for rotational fluid movement or circulation applications.
def model_69074_564a84c7_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 10 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 32.25, perimeter: 32
            with BuildLine():
                Line((-3, -1.5), (-5, -1.5))
                Line((-3, 0), (-3, -1.5))
                Line((3.5, 0), (-3, 0))
                Line((3.5, -1.5), (3.5, 0))
                Line((5.5, -1.5), (3.5, -1.5))
                Line((5.5, 2.5), (5.5, -1.5))
                Line((-5, 2.5), (5.5, 2.5))
                Line((-5, -1.5), (-5, 2.5))
            make_face()
        # OneSide extrude, distance=10
        extrude(amount=10)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 2.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 31.4159265359, perimeter: 19.8691765316
            with Locations((0, 5)):
                Circle(3.1622776602)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)

        # Sketch4 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 3, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 12.5663706144, perimeter: 12.5663706144
            with Locations((0, 5)):
                Circle(2)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)

        # Sketch5 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 3.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.7328323218, perimeter: 5.8601863266
            with Locations((0, 5)):
                Circle(0.9326776213)
        # OneSide extrude, distance=0.25
        extrude(amount=0.25, mode=Mode.ADD)

        # Sketch6 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 3.75, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2670844321, perimeter: 1.8320158184
            with Locations((0, 5)):
                Circle(0.2915743733)
        # OneSide extrude, distance=3.5
        extrude(amount=3.5, mode=Mode.ADD)

        # Sketch7 -> Extrude6 (Cut)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 3, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2513274198, perimeter: 1.7771532017
            with Locations((2.7000000402, 5.0000000745)):
                Circle(0.2828427167)
        # OneSide extrude, distance=-4.6
        extrude(amount=-4.6, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude7 (Join)
        # Sketch on BRepFace
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.3557142963, perimeter: 2.6436895216
            with BuildLine():
                Line((-3.2000000477, 3.1000000462), (-2.9000000432, 3.3571429072))
                Line((-2.6000000387, 2.4000000358), (-3.2000000477, 3.1000000462))
                Line((-2.3000000343, 2.6000000387), (-2.6000000387, 2.4000000358))
                Line((-2.9000000432, 3.3571429072), (-2.3000000343, 2.6000000387))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical housing or sleeve with a rounded rectangular cross-section, featuring a central longitudinal slot or channel running through its length, curved end caps, and what appears to be a mounting or access opening on the right side.
def model_69456_81a21eaf_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 15.7079632679, perimeter: 14.0496294621
            with Locations((-1.5, 1.5)):
                Circle(2.2360679775)
        # OneSide extrude, distance=9
        extrude(amount=9)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(9, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.2172917654, perimeter: 4.3674255544
            with BuildLine():
                CenterArc((-1.5, 1.5), 2.2360679775, 167.0790336184, 25.8419327632)
                Line((-2.5, 1), (-3.6794494718, 1))
                Line((-2.5, 2), (-2.5, 1))
                Line((-3.6794494718, 2), (-2.5, 2))
            make_face()
        # OneSide extrude, distance=-11
        extrude(amount=-11, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 0, 2.5), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with BuildLine():
                CenterArc((3.5, 1.5), 0.5, 90, 180)
                CenterArc((3.5, 1.5), 0.5, -90, 180)
            make_face()
        # OneSide extrude, distance=-1.2
        extrude(amount=-1.2, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 0, 2.5), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.7690598784, perimeter: 3.1087443537
            with Locations((8, 1.5)):
                Circle(0.4947720307)
        # OneSide extrude, distance=-0.9
        extrude(amount=-0.9, mode=Mode.SUBTRACT)

        # Sketch6 -> Extrude5 (Cut)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(9, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.493535046, perimeter: 4.3322413269
            with Locations((-1.5, 1.5)):
                Circle(0.6894976218)
        # OneSide extrude, distance=-14
        extrude(amount=-14, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a bracket or mounting assembly with a complex angular geometry featuring multiple internal slots, reinforcing ribs, and a protruding extension arm, designed for structural support or component attachment in a mechanical assembly.
def model_69474_78efa298_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 13.5, perimeter: 15
            with BuildLine():
                Line((4.5, -3), (0, -3))
                Line((4.5, 0), (4.5, -3))
                Line((0, 0), (4.5, 0))
                Line((0, -3), (0, 0))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((-1, 0.5)):
                Circle(0.2)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 13.3743362939, perimeter: 16.2566370614
            with BuildLine():
                Line((-4.5, 3), (0, 3))
                Line((-4.5, 0), (-4.5, 3))
                Line((0, 0), (-4.5, 0))
                Line((0, 3), (0, 0))
            make_face()
            with BuildLine():
                CenterArc((-1, 0.5), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((-1, 0.5)):
                Circle(0.2)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.4398229715, perimeter: 4.398229715
            with BuildLine():
                CenterArc((-1, 2.5), 0.45, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-1, 2.5), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((-1, 2.5)):
                Circle(0.25)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1, mode=Mode.ADD)

        # Sketch4 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((-1, 2.5)):
                Circle(0.25)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)

        # Sketch5 -> Extrude6 (Join)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            with Locations((-4, 2.5)):
                Circle(0.3)
        # OneSide extrude, distance=1.4
        extrude(amount=1.4, mode=Mode.ADD)

        # Sketch6 -> Extrude7 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.9, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.3927564304, perimeter: 4.9443671969
            with BuildLine():
                Line((-4.4830127066, 2.3366026082), (-4.1000000611, 2.0000000298))
                Line((-4.1000000611, 2.0000000298), (-3.6169873545, 2.1633974216))
                Line((-3.6169873545, 2.1633974216), (-3.5169872934, 2.6633973918))
                Line((-3.5169872934, 2.6633973918), (-3.8999999389, 2.9999999702))
                Line((-3.8999999389, 2.9999999702), (-4.3830126455, 2.8366025784))
                Line((-4.3830126455, 2.8366025784), (-4.4830127066, 2.3366026082))
            make_face()
            with BuildLine():
                CenterArc((-4, 2.5), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            with Locations((-4, 2.5)):
                Circle(0.3)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)
    return part.part


# Description: This is a plastic junction box or electrical enclosure featuring a rectangular main body with an attached cylindrical connector port on the left side and an open top compartment on the right, designed for housing electrical components or cable connections.
def model_69648_e2f48460_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.9008845396, perimeter: 16.3362817987
            with BuildLine():
                CenterArc((0, 0), 1.6, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=1
        extrude(amount=1, both=True)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.3634705491, perimeter: 2.4483260896
            with BuildLine():
                CenterArc((0, 0), 1, -17.4576033922, 34.9152067844)
                Line((1.5716233637, -0.3000000045), (0.9539392, -0.3000000045))
                CenterArc((0, 0), 1.6, -10.8069230378, 21.6138460757)
                Line((0.9539392, 0.3000000045), (1.5716233637, 0.3000000045))
            make_face()
        # Symmetric extrude, each_side=-3
        extrude(amount=-3, both=True, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 13 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.5027098156, perimeter: 3.0787079114
            with BuildLine():
                Line((1.5716233637, -0.3000000045), (2.5000000373, -0.3000000045))
                CenterArc((0, 0), 1.6, -30.0000004929, 19.1930774551)
                Line((2.5000000373, -0.8000000119), (1.3856406392, -0.8000000119))
                Line((2.5000000373, -0.3000000045), (2.5000000373, -0.8000000119))
            make_face()
        # OneSide extrude, distance=-2
        extrude(amount=-2, mode=Mode.ADD)

        # Sketch3 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 13 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.5027098156, perimeter: 3.0787079114
            with BuildLine():
                CenterArc((0, 0), 1.6, 10.8069230378, 19.1930774551)
                Line((1.5716233637, 0.3000000045), (2.5000000373, 0.3000000045))
                Line((2.5000000373, 0.3000000045), (2.5000000373, 0.8000000119))
                Line((2.5000000373, 0.8000000119), (1.3856406392, 0.8000000119))
            make_face()
            # Profile area: 0.5027098156, perimeter: 3.0787079114
            with BuildLine():
                Line((1.5716233637, -0.3000000045), (2.5000000373, -0.3000000045))
                CenterArc((0, 0), 1.6, -30.0000004929, 19.1930774551)
                Line((2.5000000373, -0.8000000119), (1.3856406392, -0.8000000119))
                Line((2.5000000373, -0.3000000045), (2.5000000373, -0.8000000119))
            make_face()
        # OneSide extrude, distance=-2
        extrude(amount=-2, mode=Mode.ADD)

        # Sketch4 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 15.1540030418, perimeter: 16.2931675877
            with BuildLine():
                CenterArc((0, 0), 1.6, 132.5245945193, 94.9508109615)
                Line((-1.081450601, 2), (-1.081450601, 1.1791796291))
                Line((-5.081450601, 2), (-1.081450601, 2))
                Line((-5.081450601, -2), (-5.081450601, 2))
                Line((-1.081450601, -2), (-5.081450601, -2))
                Line((-1.081450601, -1.1791796291), (-1.081450601, -2))
            make_face()
        # OneSide extrude, distance=-2
        extrude(amount=-2, mode=Mode.ADD)

        # Sketch5 -> Extrude6 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 9.0000002682, perimeter: 12.0000001788
            with BuildLine():
                Line((-1.6000000238, -1.5000000224), (-4.6000000685, -1.5000000224))
                Line((-1.6000000238, 1.5000000224), (-1.6000000238, -1.5000000224))
                Line((-4.6000000685, 1.5000000224), (-1.6000000238, 1.5000000224))
                Line((-4.6000000685, -1.5000000224), (-4.6000000685, 1.5000000224))
            make_face()
        # OneSide extrude, distance=-2
        extrude(amount=-2, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a complex injection-molded plastic housing or enclosure with an overall rectangular box shape featuring multiple internal ribbing structures, recessed cavities, mounting flanges on the sides, and internal channels or slots designed for component assembly and structural reinforcement.
def model_70583_7a55f383_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 6, perimeter: 14
            with BuildLine():
                Line((0, -2.5), (0, -1.5))
                Line((6, -2.5), (0, -2.5))
                Line((6, -1.5), (6, -2.5))
                Line((0, -1.5), (6, -1.5))
            make_face()
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 24, perimeter: 20
            with BuildLine():
                Line((6, -4), (0, -4))
                Line((6, 0), (6, -4))
                Line((0, 0), (6, 0))
                Line((0, -4), (0, 0))
            make_face()
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 6, perimeter: 14
            with BuildLine():
                Line((0, -2.5), (0, -1.5))
                Line((6, -2.5), (0, -2.5))
                Line((6, -1.5), (6, -2.5))
                Line((0, -1.5), (6, -1.5))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.SUBTRACT)

        # Sketch6 -> Extrude6 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 4), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 2.550000038, perimeter: 11.2000001222
            with BuildLine():
                Line((0.5000000075, 1), (0.5000000075, 1.5))
                Line((0.5000000075, 1), (5.6000000834, 1))
                Line((5.6000000834, 1.5), (5.6000000834, 1))
                Line((5.6000000834, 1.5), (0.5000000075, 1.5))
            make_face()
        # OneSide extrude, distance=-1.1
        extrude(amount=-1.1, mode=Mode.SUBTRACT)

        # Sketch7 -> Extrude7 (Join)
        # Sketch on BRepFace
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.140695767, perimeter: 8.5824676047
            with BuildLine():
                CenterArc((-3, 0.5), 1.0639764284, -28.0300917928, 98.0599026258)
                Line((-3.3633811226, 1.5), (-2.6366188774, 1.5))
                CenterArc((-3, 0.5), 1.0639764284, 109.970189167, 98.0599026258)
                Line((-3.9391729554, 0), (-3.5805352919, 0))
                CenterArc((-3, 0.5), 0.7661731039, -40.7374679759, 261.4749359517)
                Line((-2.4194647081, 0), (-2.0608270446, 0))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)

        # Sketch7 -> Extrude8 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.6297322502, perimeter: 4.6575770453
            with BuildLine():
                CenterArc((-3, 0.5), 0.7661731039, -40.7374679759, 261.4749359517)
                Line((-3.5805352919, 0), (-2.4194647081, 0))
            make_face()
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.SUBTRACT)

        # Sketch7 -> Extrude9 (Join)
        # Sketch on BRepFace
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2873321172, perimeter: 4.3390262063
            with BuildLine():
                CenterArc((-1, 2), 0.4115091497, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-1, 2), 0.2790683192, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.2545296257, perimeter: 4.0053609658
            with BuildLine():
                CenterArc((-5, 2), 0.3822837361, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-5, 2), 0.2551892605, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1, mode=Mode.ADD)

        # Sketch7 -> Extrude10 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2045854103, perimeter: 1.6034014122
            with Locations((-5, 2)):
                Circle(0.2551892605)
            # Profile area: 0.2446644926, perimeter: 1.753437963
            with Locations((-1, 2)):
                Circle(0.2790683192)
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a structural bracket or mounting frame with an angular, wedge-like shape featuring a large hollow rectangular slot cut through its center and a complex lattice of internal ribbing and support structures visible through the opening.
def model_74051_f60f9282_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 8 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.5643737378, perimeter: 4.9453958172
            with BuildLine():
                Line((7.7455802687, -2.5), (7.7455802687, -0.2817218227))
                Line((8, -2.5), (7.7455802687, -2.5))
                Line((8, -0.2817218227), (8, -2.5))
                Line((8, -0.2817218227), (7.7455802687, -0.2817218227))
            make_face()
            # Profile area: 0.7127546272, perimeter: 6.1962770601
            with BuildLine():
                Line((0.2817218227, -8.0000001277), (3.129583147, -8.0000014189))
                Line((3.129583147, -8.0000014189), (3.1295832605, -7.7497236244))
                Line((3.1295832605, -7.7497236244), (0.2817218227, -7.7497236244))
                Line((0.2817218227, -7.7497236244), (0.2817218227, -8.0000001277))
            make_face()
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 8 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.4281819957, perimeter: 32.0000001277
            with BuildLine():
                Line((0.2817218227, -0.2817218227), (0.2817218227, -8.0000001277))
                Line((8, -0.2817218227), (0.2817218227, -0.2817218227))
                Line((8, 0), (8, -0.2817218227))
                Line((0, 0), (8, 0))
                Line((0, -8), (0, 0))
                Line((0.2817218227, -8.0000001277), (0, -8))
            make_face()
        # OneSide extrude, distance=7
        extrude(amount=7)

        # Sketch3 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 7.7497236244), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.5533698472, perimeter: 6.0502982068
            with BuildLine():
                Line((-0.2817218227, 3.7000000551), (-3.1113050787, 3.7000000551))
                Line((-0.2817218227, 3.8955659025), (-0.2817218227, 3.7000000551))
                Line((-3.1113050787, 3.8955659025), (-0.2817218227, 3.8955659025))
                Line((-3.1113050787, 3.7000000551), (-3.1113050787, 3.8955659025))
            make_face()
        # OneSide extrude, distance=7.7
        extrude(amount=7.7, mode=Mode.ADD)

        # Sketch4 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(3.1113050787, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.4274798781, perimeter: 4.7628549155
            with BuildLine():
                Line((-2.4675834331, 3.7000000551), (-2.4675834331, 3.8955659025))
                Line((-0.2817218227, 3.7000000551), (-2.4675834331, 3.7000000551))
                Line((-0.2817218227, 3.8955659025), (-0.2817218227, 3.7000000551))
                Line((-2.4675834331, 3.8955659025), (-0.2817218227, 3.8955659025))
            make_face()
        # OneSide extrude, distance=4.8
        extrude(amount=4.8, mode=Mode.ADD)

        # Sketch5 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0.2817218227, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 6.6064153498, perimeter: 11.616665496
            with BuildLine():
                Line((-3.4936079251, 7), (-3.4936079251, 5.4477829513))
                Line((-7.7497236244, 7), (-3.4936079251, 7))
                Line((-7.7497236244, 5.4477829513), (-7.7497236244, 7))
                Line((-3.4936079251, 5.4477829513), (-7.7497236244, 5.4477829513))
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2, mode=Mode.ADD)

        # Sketch6 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 12 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(2.2817218227, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 3.3032076749, perimeter: 7.3605497968
            with BuildLine():
                Line((-5.6216657747, 5.4477829513), (-5.6216657747, 7))
                Line((-3.4936079251, 5.4477829513), (-5.6216657747, 5.4477829513))
                Line((-3.4936079251, 7), (-3.4936079251, 5.4477829513))
                Line((-5.6216657747, 7), (-3.4936079251, 7))
            make_face()
            # Profile area: 3.0799978446, perimeter: 7.0729484841
            with BuildLine():
                Line((-7.7497236244, 7), (-5.765466431, 7))
                Line((-7.7497236244, 5.4477829513), (-7.7497236244, 7))
                Line((-5.765466431, 5.4477829513), (-7.7497236244, 5.4477829513))
                Line((-5.765466431, 7), (-5.765466431, 5.4477829513))
            make_face()
        # OneSide extrude, distance=-0.1
        extrude(amount=-0.1, mode=Mode.SUBTRACT)

        # Sketch7 -> Extrude6 (Join)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(2.1817218227, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0628318549, perimeter: 0.8885766009
            with Locations((-5.300000079, 6.7000000998)):
                Circle(0.1414213583)
            # Profile area: 0.0805458387, perimeter: 1.0060660316
            with Locations((-7.4601204908, 6.7000000998)):
                Circle(0.160120382)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1, mode=Mode.ADD)
    return part.part


# Description: This is a handheld inspection mirror or borescope consisting of a rectangular blue mirror head mounted on an angled black handle, featuring a reflective viewing surface and a tapered shaft for access to confined spaces.
def model_74824_79f48f27_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 7, perimeter: 11
            with BuildLine():
                Line((0, 2), (0, 0))
                Line((0, 0), (3.5, 0))
                Line((3.5, 0), (3.5, 2))
                Line((3.5, 2), (0, 2))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.5), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1.4437654768, perimeter: 5.1993856069
            with BuildLine():
                Line((0.8389024903, 1.3485448884), (2.6345665917, 1.3485448884))
                Line((0.8389024903, 0.5445161863), (0.8389024903, 1.3485448884))
                Line((2.6345665917, 0.5445161863), (0.8389024903, 0.5445161863))
                Line((2.6345665917, 1.3485448884), (2.6345665917, 0.5445161863))
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 0, 0.7), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.3006655306, perimeter: 1.9437784051
            with Locations((1.736734541, 0.9627721388)):
                Circle(0.3093619414)
        # OneSide extrude, distance=4
        extrude(amount=4, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 0, 4.7), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0375735557, perimeter: 0.6871413437
            with Locations((1.736734541, 0.9627721388)):
                Circle(0.1093619414)
        # OneSide extrude, distance=1.9
        extrude(amount=1.9, mode=Mode.ADD)

        # Sketch5 -> Extrude5 (Join)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.0000785049, perimeter: 0.0314089507
            with Locations((-0.2213695756, 1.7849433147)):
                Circle(0.0049988898)
        # OneSide extrude, distance=0.7
        extrude(amount=0.7, mode=Mode.ADD)

        # Sketch6 -> Extrude6 (Cut)
        # Sketch on BRepFace
        # Sketch has 12 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.7), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.064400502, perimeter: 1.1882914049
            with BuildLine():
                Line((2.2786837119, 1.225756543), (2.4213163582, 1.225756543))
                Line((2.2786837119, 0.7742434868), (2.2786837119, 1.225756543))
                Line((2.4213163582, 0.7742434868), (2.2786837119, 0.7742434868))
                Line((2.4213163582, 1.225756543), (2.4213163582, 0.7742434868))
            make_face()
            # Profile area: 0.064400502, perimeter: 1.1882914049
            with BuildLine():
                Line((1.078683694, 1.225756543), (1.2213163403, 1.225756543))
                Line((1.078683694, 0.7742434868), (1.078683694, 1.225756543))
                Line((1.2213163403, 0.7742434868), (1.078683694, 0.7742434868))
                Line((1.2213163403, 1.225756543), (1.2213163403, 0.7742434868))
            make_face()
        # OneSide extrude, distance=-0.05
        extrude(amount=-0.05, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a mobile device holder/stand with a rectangular frame featuring a tilted display surface, rounded corner accents, and a compact folding base for stable tabletop support.
def model_77781_397e2e96_0000():
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
        # Sketch has 26 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 60.7776033502, perimeter: 31.3255645237
            with BuildLine():
                CenterArc((4.5479791111, 1.0011911554), 1, -90, 90)
                Line((5.5479791111, 4.6924639047), (5.5479791111, 1.0011911554))
                CenterArc((4.5479791111, 4.6924639047), 1, 0, 90)
                Line((-4.2819377479, 5.6924639047), (4.5479791111, 5.6924639047))
                CenterArc((-4.2819377479, 4.6924639047), 1, 90, 90)
                Line((-5.2819377479, 1.0011911554), (-5.2819377479, 4.6924639047))
                CenterArc((-4.2819377479, 1.0011911554), 1, -180, 90)
                Line((-1.0002262448, 0.0011911554), (-4.2819377479, 0.0011911554))
                Line((1, 0.0011911554), (-1.0002262448, 0.0011911554))
                Line((4.5479791111, 0.0011911554), (1, 0.0011911554))
            make_face()
        # Symmetric extrude, each_side=0.3
        extrude(amount=0.3, both=True)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0.3, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.9485029519, perimeter: 6.7740669224
            with BuildLine():
                Line((-0.7425624624, 0.0011911554), (0.6501385697, 0.0011911554))
                _nurbs_edge([(-0.7425624624, 0.0011911554), (-0.7191647661, -0.0178213387), (-0.6750476034, -0.0568794106), (-0.6169067702, -0.118565855), (-0.555717956, -0.2071143661), (-0.508099099, -0.3289350442), (-0.4912569049, -0.4626273208), (-0.5065042067, -0.6086976002), (-0.5527501251, -0.7667250933), (-0.6273376391, -0.9356848974), (-0.7273760287, -1.1144619639), (-0.8257834468, -1.2645721337), (-0.9092111254, -1.3808663358), (-0.9690359447, -1.4600183418), (-1, -1.5)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1, 1, 1, 1, 1], 5)
                Line((-1, -1.5), (1, -1.5))
                _nurbs_edge([(0.6501385697, 0.0011911554), (0.6329124432, -0.0185150797), (0.6007466469, -0.058901433), (0.559357438, -0.1224026616), (0.5181155244, -0.2130100833), (0.4911887533, -0.3367582877), (0.4904699566, -0.4716694001), (0.5169608999, -0.6181701081), (0.569574549, -0.7757974051), (0.646000406, -0.943567168), (0.7437586134, -1.1204231372), (0.8373501432, -1.2684609157), (0.9155952169, -1.3829186382), (0.9712784102, -1.4607229992), (1, -1.5)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1, 1, 1, 1, 1], 5)
            make_face()
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(-0.3, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 38.25, perimeter: 26
            with BuildLine():
                Line((-4.5, 0.5), (-4.5, 5))
                Line((4, 0.5), (-4.5, 0.5))
                Line((4, 5), (4, 0.5))
                Line((-4.5, 5), (4, 5))
            make_face()
        # OneSide extrude, distance=-0.1
        extrude(amount=-0.1, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude4 (NewBody)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -1.5, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 5.6000001788, perimeter: 14.400000149
            with BuildLine():
                Line((1.0000000149, -1.5000000224), (-1.0000000149, -1.5000000224))
                Line((1.0000000149, 1.5000000224), (1.0000000149, -1.5000000224))
                Line((-1.0000000149, 1.5000000224), (1.0000000149, 1.5000000224))
                Line((-1.0000000149, -1.5000000224), (-1.0000000149, 1.5000000224))
            make_face()
            with BuildLine():
                Line((0.1, 1), (0.1, -1))
                Line((0.3, 1), (0.1, 1))
                Line((0.3, -1), (0.3, 1))
                Line((0.1, -1), (0.3, -1))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)

        # Sketch6 -> Extrude5 (Join)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, -1.7, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.0628318549, perimeter: 0.8885766009
            with Locations((-0.8000000119, 1.3000000194)):
                Circle(0.1414213583)
            # Profile area: 0.0628318549, perimeter: 0.8885766009
            with Locations((0.8000000119, 1.3000000194)):
                Circle(0.1414213583)
            # Profile area: 0.0628318549, perimeter: 0.8885766009
            with Locations((-0.8000000119, -1.3000000194)):
                Circle(0.1414213583)
            # Profile area: 0.0655133786, perimeter: 0.9073397358
            with Locations((0.8000000119, -1.3000000194)):
                Circle(0.144407604)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)
    return part.part


# Description: This is a dumbbell or weight with cylindrical end caps connected by a curved, textured grip handle in the middle, designed for fitness training.
def model_77782_3a7b7a3e_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch2 -> Extrude2 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.926990934, perimeter: 15.707963502
            with BuildLine():
                CenterArc((-1.5000000224, 0.5000000075), 1.5000000224, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-1.5000000224, 0.5000000075), 1.0000000149, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=2
        extrude(amount=2)

        # Sketch3 -> Extrude3 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.926990817, perimeter: 15.7079632679
            with BuildLine():
                CenterArc((11.5, 0.5), 1.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((11.5, 0.5), 1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=2
        extrude(amount=2)

        # Sketch4 -> Extrude4 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.926990817, perimeter: 15.7079632679
            with BuildLine():
                CenterArc((5, 7.5), 1.5, -180, 52.8527481003)
                CenterArc((5, 7.5), 1.5, -127.1472518997, 74.2945038559)
                CenterArc((5, 7.5), 1.5, -52.8527480438, 52.8527480438)
                CenterArc((5, 7.5), 1.5, 0, 180)
            make_face()
            with BuildLine():
                CenterArc((5, 7.5), 1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=2
        extrude(amount=2)

        # Sketch4 -> Extrude5 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 6.5982435178, perimeter: 17.2092263462
            with BuildLine():
                Line((-1.5, 2), (-0.36202279, 1.4768504862))
                CenterArc((-3.2804793301, 8.6413448456), 7.7361080656, -67.8364768355, 50.2535079862)
                CenterArc((5, 7.5), 1.5, -180, 52.8527481003)
                CenterArc((-3.7318859821, 9.0517145292), 7.3964851679, -72.4372852259, 60.3271924397)
            make_face()
        # OneSide extrude, distance=1.5
        extrude(amount=1.5, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude6 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 6.6060618647, perimeter: 17.2081111788
            with BuildLine():
                CenterArc((5, 7.5), 1.5, -52.8527480438, 52.8527480438)
                CenterArc((13.2804789951, 8.6413446324), 7.7361076803, -162.4170319096, 50.2523520893)
                Line((11.5000001714, 2.0000000298), (10.3618779679, 1.4769095475))
                CenterArc((13.7402412239, 9.0593103116), 7.4062501732, -167.846013168, 60.2394066121)
            make_face()
        # OneSide extrude, distance=1.5
        extrude(amount=1.5, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude7 (Join)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 6.5982435178, perimeter: 17.2092263462
            with BuildLine():
                Line((-1.5, 2), (-0.36202279, 1.4768504862))
                CenterArc((-3.2804793301, 8.6413448456), 7.7361080656, -67.8364768355, 50.2535079862)
                CenterArc((5, 7.5), 1.5, -180, 52.8527481003)
                CenterArc((-3.7318859821, 9.0517145292), 7.3964851679, -72.4372852259, 60.3271924397)
            make_face()
        # OneSide extrude, distance=1.5
        extrude(amount=1.5, mode=Mode.ADD)

        # Sketch4 -> Extrude8 (Join)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 6.6060618647, perimeter: 17.2081111788
            with BuildLine():
                CenterArc((5, 7.5), 1.5, -52.8527480438, 52.8527480438)
                CenterArc((13.2804789951, 8.6413446324), 7.7361076803, -162.4170319096, 50.2523520893)
                Line((11.5000001714, 2.0000000298), (10.3618779679, 1.4769095475))
                CenterArc((13.7402412239, 9.0593103116), 7.4062501732, -167.846013168, 60.2394066121)
            make_face()
        # OneSide extrude, distance=1.5
        extrude(amount=1.5, mode=Mode.ADD)

        # Sketch5 -> Extrude9 (NewBody)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 10.6308088667, perimeter: 24.0925793526
            with BuildLine():
                Line((-10.5, 0.5048097144), (-10.5, -0.4951902856))
                CenterArc((-5.0568566782, 13.7437912693), 15.2438973016, -110.9203831126, 40.318365414)
                CenterArc((1.5000000224, -0.5000000075), 1.5000000224, 137.9427257203, 47.2123039648)
                CenterArc((-5.0568566782, 14.8187143252), 15.3139046108, -110.8202895485, 41.6405790969)
            make_face()
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)
    return part.part


# Description: This is a small rectangular block or connector housing with a compact cubic shape and what appears to be internal mounting features or contact points.
def model_77805_33a58782_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch21 -> Extrude12 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.1500000045, perimeter: 1.6000000238
            with BuildLine():
                Line((-3.4000000507, 4.0000000596), (-3.7000000551, 4.0000000596))
                Line((-3.7000000551, 4.0000000596), (-3.7000000551, 3.5000000522))
                Line((-3.7000000551, 3.5000000522), (-3.4000000507, 3.5000000522))
                Line((-3.4000000507, 3.5000000522), (-3.4000000507, 4.0000000596))
            make_face()
        # Symmetric extrude, each_side=0.1
        extrude(amount=0.1, both=True)

        # Sketch23 -> Extrude13 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 3.5000000522, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.021999999, perimeter: 0.6199999861
            with BuildLine():
                Line((-2.5299999435, -3.2299999278), (-2.639999941, -3.2299999278))
                Line((-2.5299999435, -3.0299999323), (-2.5299999435, -3.2299999278))
                Line((-2.639999941, -3.0299999323), (-2.5299999435, -3.0299999323))
                Line((-2.639999941, -3.2299999278), (-2.639999941, -3.0299999323))
            make_face()
        # OneSide extrude, distance=0.001
        extrude(amount=0.001, mode=Mode.ADD)
    return part.part


# Description: This is a duct or air intake manifold featuring a rectangular flanged top section with ventilation slots and a cylindrical curved body below, designed to direct and distribute airflow.
def model_78975_6555cbf0_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 7 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 814.1390043476, perimeter: 180.0713475605
            with BuildLine():
                Line((0, 0), (0, -3.2))
                Line((0, -3.2), (20, -3.2))
                Line((20, -3.2), (20, -16.4))
                Line((20, -16.4), (20.2327700087, -16.4))
                CenterArc((32.4846909757, -17.8957494753), 12.3428859622, 173.0396110872, 193.9207778256)
                Line((44.7366119428, -16.4), (45, -16.4))
                Line((45, -3.2), (45, -16.4))
                Line((65, -3.2), (45, -3.2))
                Line((65, 0), (65, -3.2))
                Line((0, 0), (65, 0))
            make_face()
        # OneSide extrude, distance=30
        extrude(amount=30)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 30), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 176.7145867644, perimeter: 47.1238898038
            with Locations((32.4846909757, -17.8957494753)):
                Circle(7.5)
        # OneSide extrude, distance=-30
        extrude(amount=-30, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -3.2, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 44.1786466911, perimeter: 23.5619449019
            with Locations((54.8474701551, 22.7331759374)):
                Circle(3.75)
        # OneSide extrude, distance=-20
        extrude(amount=-20, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -3.2, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 44.1786466911, perimeter: 23.5619449019
            with Locations((54.509746293, 7.1978864028)):
                Circle(3.75)
        # OneSide extrude, distance=-35
        extrude(amount=-35, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -3.2, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 44.1786466911, perimeter: 23.5619449019
            with Locations((10, 22.7331759374)):
                Circle(3.75)
        # OneSide extrude, distance=-20
        extrude(amount=-20, mode=Mode.SUBTRACT)

        # Sketch6 -> Extrude6 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -3.2, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 44.1786466911, perimeter: 23.5619449019
            with Locations((10, 7.1978864028)):
                Circle(3.75)
        # OneSide extrude, distance=-20
        extrude(amount=-20, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a structural bracket or frame assembly with a complex hexagonal/angular body featuring multiple rectangular openings and windows, accompanied by a cylindrical fastening bolt or pin for assembly.
def model_79695_fd8bae0e_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 10 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 130, perimeter: 66
            with BuildLine():
                Line((3, 5), (-3, 5))
                Line((3, 0), (3, 5))
                Line((10, 0), (3, 0))
                Line((10, 8), (10, 0))
                Line((-10, 8), (10, 8))
                Line((-10, 0), (-10, 8))
                Line((-3, 0), (-10, 0))
                Line((-3, 5), (-3, 0))
            make_face()
        # OneSide extrude, distance=10
        extrude(amount=10)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(10, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.9509445679, perimeter: 4.9513929846
            with Locations((-3, 6)):
                Circle(0.7880386687)
        # OneSide extrude, distance=-23
        extrude(amount=-23, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 8, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            with Locations((5, 5)):
                Circle(1)
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            with Locations((-5, 5)):
                Circle(1)
        # OneSide extrude, distance=-17
        extrude(amount=-17, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(10, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.8208940765, perimeter: 4.7835164696
            with Locations((-2.9822791174, 2.4667096887)):
                Circle(0.7613202915)
        # OneSide extrude, distance=-41
        extrude(amount=-41, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude5 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 7.0685834706, perimeter: 9.4247779608
            with Locations((-20, -2.5)):
                Circle(1.5)
        # OneSide extrude, distance=-1
        extrude(amount=-1)

        # Sketch6 -> Extrude6 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((20, 2.5)):
                Circle(0.5)
        # OneSide extrude, distance=8
        extrude(amount=8, mode=Mode.ADD)
    return part.part


# Description: This is a compact pump or motor housing with an overall blocky, angular shape featuring a cylindrical inlet/outlet port on the left, a rectangular body with mounting flanges on the bottom, and various internal passages visible through the semi-transparent rendering.
def model_79797_415c0747_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 9 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 21.3003986156, perimeter: 23.9407074755
            with BuildLine():
                CenterArc((7.6, 0), 1.7, 90, 179.9999994008)
                Line((0, 1.7), (7.6, 1.7))
                Line((0, -1.7), (0, 1.7))
                Line((7.5999999822, -1.7), (0, -1.7))
            make_face()
            # Profile area: 4.5396013542, perimeter: 8.7407074933
            with BuildLine():
                CenterArc((7.6, 0), 1.7, 90, 179.9999994008)
                Line((7.6, 1.7), (7.5999999822, -1.7))
            make_face()
            # Profile area: 4.5396014147, perimeter: 8.7407075289
            with BuildLine():
                Line((7.6, 1.7), (7.5999999822, -1.7))
                CenterArc((7.6, 0), 1.7, -90.0000005992, 180.0000005992)
            make_face()
        # OneSide extrude, distance=3.8
        extrude(amount=3.8)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 9.3213182461, perimeter: 19.8642903486
            with BuildLine():
                CenterArc((0, 3.8), 2.05, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 3.8), 1.1115, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 3.8812248806, perimeter: 6.9837604689
            with Locations((0, 3.8)):
                Circle(1.1115)
        # Symmetric extrude, each_side=2.2
        extrude(amount=2.2, both=True, mode=Mode.ADD)

        # Sketch2 -> Extrude6 (Cut)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY) as sk:
            # Profile area: 3.8812248806, perimeter: 6.9837604689
            with Locations((0, 3.8)):
                Circle(1.1115)
        # TwoSides extrude, along=6, against=-7.5
        extrude(amount=6, mode=Mode.SUBTRACT)
        extrude(sk.sketch, amount=-7.5, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on XY construction plane
        # Sketch has 5 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 9.9, perimeter: 13.4
            with BuildLine():
                Line((5.1, 2.2), (9.6, 2.2))
                Line((5.1, 0), (5.1, 2.2))
                Line((9.6, 0), (5.1, 0))
                Line((9.6, 2.2), (9.6, 0))
            make_face()
        # Symmetric extrude, full_length=True, total=3.5
        extrude(amount=1.75, both=True, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 3.8, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.9087385212, perimeter: 7.853981634
            with Locations((-7.6, 0)):
                Circle(1.25)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3, mode=Mode.ADD)

        # Sketch5 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 3.8, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))) as sk:
            # Profile area: 0.9503317777, perimeter: 3.4557519189
            with Locations((-3.5, 0)):
                Circle(0.55)
            # Profile area: 0.9503317777, perimeter: 3.4557519189
            with Locations((-7.6, 0)):
                Circle(0.55)
        # TwoSides extrude, along=3, against=-6
        extrude(amount=3, mode=Mode.SUBTRACT)
        extrude(sk.sketch, amount=-6, mode=Mode.SUBTRACT)

        # Sketch6 -> Extrude7 (Cut)
        # Sketch on BRepFace
        # Sketch has 8 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(5.1, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.96, perimeter: 4.4
            with BuildLine():
                Line((-0.8, 0.6), (0.8, 0.6))
                Line((-0.8, 0), (-0.8, 0.6))
                Line((0.8, 0), (-0.8, 0))
                Line((0.8, 0.6), (0.8, 0))
            make_face()
        # OneSide extrude, distance=-12
        extrude(amount=-12, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical capsule or barrel-shaped component with a rounded end and a smaller cylindrical pin or plug displayed separately, likely designed for assembly or as a fastening element.
def model_80754_9c3b58fa_0002():
    """Model: ARRD v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 7.7911341986, perimeter: 9.8947602217
            Circle(1.5748)
        # OneSide extrude, distance=4.5593
        extrude(amount=4.5593)

        # Sketch12 -> Extrude8 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0953522146, perimeter: 1.2667856059
            with BuildLine():
                Line((-6.6116199156, 0), (-7.1043799187, 0))
                CenterArc((-6.8579999171, 0), 0.2463800015, 0, 180)
            make_face()
            # Profile area: 0.0953522146, perimeter: 1.2667856059
            with BuildLine():
                CenterArc((-6.8579999171, 0), 0.2463800015, -180, 180)
                Line((-6.6116199156, 0), (-7.1043799187, 0))
            make_face()
        # Symmetric extrude, each_side=0.889
        extrude(amount=0.889, both=True)
    return part.part


# Description: This is a U-shaped bracket or support structure with two vertical flanges connected by a base, featuring curved handles on each side and a rectangular slot or opening along the bottom edge.
def model_81145_b0dd48d9_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.1, perimeter: 7.4
            with BuildLine():
                Line((-1.5, -0.35), (-1.5, 0.35))
                Line((1.5, -0.35), (-1.5, -0.35))
                Line((1.5, 0.35), (1.5, -0.35))
                Line((-1.5, 0.35), (1.5, 0.35))
            make_face()
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 11 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0699999854, perimeter: 1.5999999583
            with BuildLine():
                Line((-1.4000000209, 0.35), (-1.4000000209, -0.35))
                Line((-1.5, 0.35), (-1.4000000209, 0.35))
                Line((-1.5, 0.35), (-1.5, -0.35))
                Line((-1.5, -0.35), (-1.4000000209, -0.35))
            make_face()
            # Profile area: 0.0699999927, perimeter: 1.5999999791
            with BuildLine():
                Line((1.5, -0.35), (1.5, 0.35))
                Line((1.5, 0.35), (1.4000000209, 0.35))
                Line((1.4000000209, 0.35), (1.4, -0.35))
                Line((1.5, -0.35), (1.4, -0.35))
            make_face()
        # OneSide extrude, distance=2.5
        extrude(amount=2.5, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -0.35), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.1699999816, perimeter: 3.5999999657
            with BuildLine():
                Line((1.5, 0.9), (1.4000000209, 0.9000000134))
                Line((1.5, 0.9), (1.5, 2.6))
                Line((1.5, 2.6), (1.4, 2.6))
                Line((1.4, 2.6), (1.4000000209, 0.9000000134))
            make_face()
            # Profile area: 0.1699999645, perimeter: 3.5999999583
            with BuildLine():
                Line((-1.5, 0.9), (-1.4000000209, 0.9))
                Line((-1.4000000209, 0.9), (-1.4000000209, 2.6))
                Line((-1.4000000209, 2.6), (-1.5, 2.6))
                Line((-1.5, 2.6), (-1.5, 0.9))
            make_face()
        # OneSide extrude, distance=0.9
        extrude(amount=0.9, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(1.5, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.3114321884, perimeter: 2.8841565889
            with BuildLine():
                CenterArc((0, 1.6), 0.8, -20, 65)
                CenterArc((0.8692156781, 1.2836313781), 0.125, 160.0000052158, 180)
                CenterArc((0, 1.6), 1.05, -19.9999987581, 65)
                CenterArc((0.6540737646, 2.2540737806), 0.125, 45.0000052158, 180)
            make_face()
        # OneSide extrude, distance=-0.1
        extrude(amount=-0.1, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(-1.5, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.3114321884, perimeter: 2.8841565889
            with BuildLine():
                CenterArc((-0.6540737726, 2.2540737726), 0.125, -45, 180)
                CenterArc((0, 1.6), 1.05, 135, 65)
                CenterArc((-0.8692156742, 1.2836313674), 0.125, -160, 180)
                CenterArc((0, 1.6), 0.8, 135, 65)
            make_face()
        # OneSide extrude, distance=-0.1
        extrude(amount=-0.1, mode=Mode.SUBTRACT)

        # Sketch6 -> Extrude6 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.27, perimeter: 2.4
            with BuildLine():
                Line((-0.35, -0.15), (-0.35, 0.15))
                Line((-0.35, 0.15), (-1.25, 0.15))
                Line((-1.25, 0.15), (-1.25, -0.15))
                Line((-1.25, -0.15), (-0.35, -0.15))
            make_face()
            # Profile area: 0.27, perimeter: 2.4
            with BuildLine():
                Line((1.25, -0.15), (0.35, -0.15))
                Line((1.25, 0.15), (1.25, -0.15))
                Line((0.35, 0.15), (1.25, 0.15))
                Line((0.35, -0.15), (0.35, 0.15))
            make_face()
        # OneSide extrude, distance=-0.1
        extrude(amount=-0.1, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a trapezoidal or wedge-shaped container or enclosure with an angled top surface, featuring a recessed interior cavity, side flanges, and what appears to be a mounting or drainage feature at the bottom rear.
def model_81145_f989cf29_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 7.92, perimeter: 11.4
            with BuildLine():
                Line((1.3857321322, -1.910673847), (-1.0142678678, -1.910673847))
                Line((1.3857321322, 1.389326153), (1.3857321322, -1.910673847))
                Line((-1.0142678678, 1.389326153), (1.3857321322, 1.389326153))
                Line((-1.0142678678, -1.910673847), (-1.0142678678, 1.389326153))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1.910673847), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.301907054, perimeter: 1.9477874452
            with Locations((-0.4473188021, 0.5)):
                Circle(0.31)
        # OneSide extrude, distance=0.8
        extrude(amount=0.8, mode=Mode.ADD)

        # Sketch5 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            with Locations((-0.9857759905, 0.7606542647)):
                Circle(0.3)
        # OneSide extrude, distance=-0.1
        extrude(amount=-0.1, mode=Mode.SUBTRACT)

        # Sketch6 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.9, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            with Locations((-0.9857759905, 0.7606542647)):
                Circle(0.1)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1, mode=Mode.ADD)

        # Sketch7 -> Extrude6 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.9425, perimeter: 4.2
            with BuildLine():
                Line((0.8142306174, 0.010665028), (0.8142306174, 1.460665028))
                Line((0.8142306174, 1.460665028), (0.1642306174, 1.460665028))
                Line((0.1642306174, 1.460665028), (0.1642306174, 0.010665028))
                Line((0.1642306174, 0.010665028), (0.8142306174, 0.010665028))
            make_face()
        # OneSide extrude, distance=-0.025
        extrude(amount=-0.025, mode=Mode.SUBTRACT)

        # Sketch9 -> Extrude8 (Join)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.33, perimeter: 2.3
            with BuildLine():
                Line((-1.6142678678, -0.035673847), (-1.0142678678, -0.035673847))
                Line((-1.6142678678, -0.585673847), (-1.6142678678, -0.035673847))
                Line((-1.0142678678, -0.585673847), (-1.6142678678, -0.585673847))
                Line((-1.0142678678, -0.035673847), (-1.0142678678, -0.585673847))
            make_face()
            # Profile area: 0.33, perimeter: 2.3
            with BuildLine():
                Line((1.9857321322, -0.585673847), (1.9857321322, -0.035673847))
                Line((1.9857321322, -0.035673847), (1.3857321322, -0.035673847))
                Line((1.3857321322, -0.585673847), (1.3857321322, -0.035673847))
                Line((1.3857321322, -0.585673847), (1.9857321322, -0.585673847))
            make_face()
        # OneSide extrude, distance=0.1
        extrude(amount=0.1, mode=Mode.ADD)

        # Sketch10 -> Extrude9 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.7741683667, perimeter: 4.3407482963
            with BuildLine():
                Line((-0.845692464, -1.2959298402), (0.8725270199, -1.2098584705))
                Line((0.8500132422, -0.7604220125), (0.8725270199, -1.2098584705))
                Line((-0.8682066679, -0.8464934035), (0.8500132422, -0.7604220125))
                Line((-0.8682066679, -0.8464934035), (-0.845692464, -1.2959298402))
            make_face()
        # OneSide extrude, distance=-0.45
        extrude(amount=-0.45, mode=Mode.SUBTRACT)
    return part.part


MODELS = {
    "model_53619_db3904ac_0000": {"func": model_53619_db3904ac_0000, "volume": 6.4422321272, "area": 99.1644608532},
    "model_53704_b0cfbbcc_0000": {"func": model_53704_b0cfbbcc_0000, "volume": 0.8016186692, "area": 11.597958412},
    "model_54482_a0855783_0000": {"func": model_54482_a0855783_0000, "volume": 0.4959789402, "area": 4.1508292936},
    "model_54508_46ea0fd2_0000": {"func": model_54508_46ea0fd2_0000, "volume": 78.5398163397, "area": 102.1017612417},
    "model_54612_ac95f0d2_0000": {"func": model_54612_ac95f0d2_0000, "volume": 252.7078027371, "area": 261.7586691009},
    "model_54748_098dc1a6_0000": {"func": model_54748_098dc1a6_0000, "volume": 1153.6203291843, "area": 828.229031583},
    "model_54751_d9d0d87b_0000": {"func": model_54751_d9d0d87b_0000, "volume": 4.99905931, "area": 27.2376083066},
    "model_54759_5a7a83c9_0000": {"func": model_54759_5a7a83c9_0000, "volume": 4.8056957824, "area": 26.4906215843},
    "model_54780_39d5176d_0000": {"func": model_54780_39d5176d_0000, "volume": 24.9523867832, "area": 116.1958857372},
    "model_54843_a145d131_0000": {"func": model_54843_a145d131_0000, "volume": 556.142581803, "area": 1244.5907264531},
    "model_54976_69951f7f_0000": {"func": model_54976_69951f7f_0000, "volume": 462.7522407168, "area": 936.2659518846},
    "model_54980_620ee8ed_0000": {"func": model_54980_620ee8ed_0000, "volume": 178.7079602535, "area": 287.0022038129},
    "model_55051_83f272e3_0000": {"func": model_55051_83f272e3_0000, "volume": 604.7260836334, "area": 820.3804970502},
    "model_55104_4bb0d5c8_0000": {"func": model_55104_4bb0d5c8_0000, "volume": 1645.5, "area": 1327},
    "model_55119_643f4796_0000": {"func": model_55119_643f4796_0000, "volume": 248.4479297467, "area": 429.3901585341},
    "model_55232_aeefe2c8_0000": {"func": model_55232_aeefe2c8_0000, "volume": 4901.8710284308, "area": 2613.9980379218},
    "model_55279_5d386bad_0000": {"func": model_55279_5d386bad_0000, "volume": 6.5736747259, "area": 38.0347591109},
    "model_55327_eb2ad109_0000": {"func": model_55327_eb2ad109_0000, "volume": 131.2567669671, "area": 292.1345327133},
    "model_55373_ddd74d2f_0000": {"func": model_55373_ddd74d2f_0000, "volume": 8280.6858347058, "area": 4949.3982238415},
    "model_55376_85564033_0000": {"func": model_55376_85564033_0000, "volume": 3.4359628912, "area": 28.6690111725},
    "model_55472_b5c56340_0000": {"func": model_55472_b5c56340_0000, "volume": 22578.5218345998, "area": 9400.232576587},
    "model_55611_69142616_0008": {"func": model_55611_69142616_0008, "volume": 90.3389197255, "area": 186.2691879981},
    "model_55611_69142616_0010": {"func": model_55611_69142616_0010, "volume": 265.923278777, "area": 363.5891978441},
    "model_56047_f7d96d9b_0000": {"func": model_56047_f7d96d9b_0000, "volume": 172.5294924199, "area": 214.8881802489},
    "model_56065_00bbe5da_0018": {"func": model_56065_00bbe5da_0018, "volume": 4.2959316042, "area": 28.7141568538},
    "model_56127_3a60f829_0000": {"func": model_56127_3a60f829_0000, "volume": 128.5065748531, "area": 435.8135442243},
    "model_56252_f65e7429_0005": {"func": model_56252_f65e7429_0005, "volume": 426.9649128465, "area": 553.9623684401},
    "model_56482_33e4f73c_0009": {"func": model_56482_33e4f73c_0009, "volume": 1059.8159869065, "area": 808.7535282108},
    "model_57736_91b94db5_0000": {"func": model_57736_91b94db5_0000, "volume": 2160, "area": 3282},
    "model_57889_662c9748_0000": {"func": model_57889_662c9748_0000, "volume": 285.495638972, "area": 1006.8372098027},
    "model_57975_464a2e4e_0000": {"func": model_57975_464a2e4e_0000, "volume": 21.7679589114, "area": 92.0433603156},
    "model_60295_e0b2e08b_0000": {"func": model_60295_e0b2e08b_0000, "volume": 81.6476367736, "area": 181.8086968395},
    "model_60567_4422df95_0000": {"func": model_60567_4422df95_0000, "volume": 69.2319980272, "area": 151.9297768795},
    "model_60728_99f07543_0000": {"func": model_60728_99f07543_0000, "volume": 23.8352376456, "area": 59.4417717166},
    "model_60766_fb8715eb_0000": {"func": model_60766_fb8715eb_0000, "volume": 314.8402718465, "area": 500.0002882909},
    "model_60973_07d73016_0000": {"func": model_60973_07d73016_0000, "volume": 188.725508399, "area": 307.1910481038},
    "model_61767_6afe5575_0002": {"func": model_61767_6afe5575_0002, "volume": 1333.2, "area": 1630.4},
    "model_63930_357170ca_0000": {"func": model_63930_357170ca_0000, "volume": 22.6849291124, "area": 98.3091054189},
    "model_65715_433564a6_0000": {"func": model_65715_433564a6_0000, "volume": 3718400, "area": 726420},
    "model_66164_21e5e959_0000": {"func": model_66164_21e5e959_0000, "volume": 27615.65, "area": 44713.6},
    "model_69074_564a84c7_0000": {"func": model_69074_564a84c7_0000, "volume": 345.7108842049, "area": 416.0673698064},
    "model_69456_81a21eaf_0000": {"func": model_69456_81a21eaf_0000, "volume": 116.416309533, "area": 211.9198144681},
    "model_69474_78efa298_0000": {"func": model_69474_78efa298_0000, "volume": 14.0356530172, "area": 72.3451826271},
    "model_69648_e2f48460_0000": {"func": model_69648_e2f48460_0000, "volume": 23.3936727904, "area": 110.1183426545},
    "model_70583_7a55f383_0000": {"func": model_70583_7a55f383_0000, "volume": 26.9148179103, "area": 96.0647583169},
    "model_74051_f60f9282_0000": {"func": model_74051_f60f9282_0000, "volume": 58.6396468502, "area": 383.5992266503},
    "model_74824_79f48f27_0000": {"func": model_74824_79f48f27_0000, "volume": 5.0564198767, "area": 29.7613747006},
    "model_77781_397e2e96_0000": {"func": model_77781_397e2e96_0000, "volume": 34.2020644057, "area": 162.4398999535},
    "model_77782_3a7b7a3e_0000": {"func": model_77782_3a7b7a3e_0000, "volume": 58.967811304, "area": 236.8454478524},
    "model_77805_33a58782_0000": {"func": model_77805_33a58782_0000, "volume": 0.0300220009, "area": 0.6646200117},
    "model_78975_6555cbf0_0000": {"func": model_78975_6555cbf0_0000, "volume": 18557.2458498483, "area": 8038.8696773123},
    "model_79695_fd8bae0e_0000": {"func": model_79695_fd8bae0e_0000, "volume": 1198.5748778906, "area": 1211.470905257},
    "model_79797_415c0747_0000": {"func": model_79797_415c0747_0000, "volume": 108.2769303303, "area": 231.3993290178},
    "model_80754_9c3b58fa_0002": {"func": model_80754_9c3b58fa_0002, "volume": 35.8611906268, "area": 63.8292925783},
    "model_81145_b0dd48d9_0000": {"func": model_81145_b0dd48d9_0000, "volume": 0.7497134815, "area": 18.151102252},
    "model_81145_f989cf29_0000": {"func": model_81145_f989cf29_0000, "volume": 7.830454637, "area": 32.6678941018},
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
