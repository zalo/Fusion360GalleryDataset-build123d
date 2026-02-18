"""Batch 008 - passing/03_4to5ops
116 models bundled from Fusion360 Gallery reconstructions.
"""

from build123d import *
from build123d import Edge, BuildLine
from collections import Counter
from OCP.BRepBuilderAPI import BRepBuilderAPI_MakeEdge
from OCP.Geom import Geom_BSplineCurve
from OCP.TColStd import TColStd_Array1OfReal, TColStd_Array1OfInteger
from OCP.TColgp import TColgp_Array1OfPnt
from OCP.gp import gp_Pnt


# Description: This is a cylindrical sleeve or collar with a mesh or perforated upper section and a solid lower section, featuring an open-ended tubular design with curved geometry.
def model_30297_fd93a92a_0002():
    """Model: Part 9 v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.9793260902, perimeter: 4.9872783376
            Circle(0.79375)
        # OneSide extrude, distance=0.71374
        extrude(amount=0.71374)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.4964162502, perimeter: 2.4976289915
            Circle(0.39751)
        # OneSide extrude, distance=-1.3
        extrude(amount=-1.3, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a mounting bracket or stand featuring a blue hexagonal base with internal cross-bracing and a dark gray cylindrical post that extends upward at an angle, designed to support or hold equipment in an elevated, tilted position.
def model_30379_f1d5e193_0001():
    """Model: 2M Mounting Screws"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            Circle(0.1)
        # OneSide extrude, distance=1.2
        extrude(amount=1.2)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1850904244, perimeter: 2.3603693383
            with BuildLine():
                Line((0.1443375673, -0.25), (0.2886751346, 0))
                Line((0.2886751346, 0), (0.1443375673, 0.25))
                Line((0.1443375673, 0.25), (-0.1443375673, 0.25))
                Line((-0.1443375673, 0.25), (-0.2886751346, 0))
                Line((-0.2886751346, 0), (-0.1443375673, -0.25))
                Line((-0.1443375673, -0.25), (0.1443375673, -0.25))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1, mode=Mode.ADD)

        # Sketch2 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.0093530739, perimeter: 0.359999992
            with BuildLine():
                Line((0.0299999993, -0.0519615231), (0.0599999987, 0))
                Line((0.0599999987, 0), (0.0299999993, 0.0519615231))
                Line((0.0299999993, 0.0519615231), (-0.0299999993, 0.0519615231))
                Line((-0.0299999993, 0.0519615231), (-0.0599999987, 0))
                Line((-0.0599999987, 0), (-0.0299999993, -0.0519615231))
                Line((-0.0299999993, -0.0519615231), (0.0299999993, -0.0519615231))
            make_face()
        # OneSide extrude, distance=-0.05
        extrude(amount=-0.05, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a hexagonal socket (hex key) or Allen wrench tool, featuring a cylindrical body with a recessed hexagonal cavity on one end for driving fasteners.
def model_30379_f1d5e193_0003():
    """Model: 1M Spline Set Screw"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0078539816, perimeter: 0.3141592654
            Circle(0.05)
        # OneSide extrude, distance=-0.09
        extrude(amount=-0.09)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0023382685, perimeter: 0.179999996
            with BuildLine():
                Line((0.0149999997, -0.0259807615), (0.0299999993, 0))
                Line((0.0299999993, 0), (0.0149999997, 0.0259807615))
                Line((0.0149999997, 0.0259807615), (-0.0149999997, 0.0259807615))
                Line((-0.0149999997, 0.0259807615), (-0.0299999993, 0))
                Line((-0.0299999993, 0), (-0.0149999997, -0.0259807615))
                Line((-0.0149999997, -0.0259807615), (0.0149999997, -0.0259807615))
            make_face()
        # OneSide extrude, distance=-0.03
        extrude(amount=-0.03, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical fastener or spacer with a large knurled flanged head at the top and a threaded or grooved cylindrical shaft, designed for assembly or mechanical fastening applications.
def model_30379_f1d5e193_0011():
    """Model: 1M Low Profile"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0235619449, perimeter: 0.9424777961
            with BuildLine():
                CenterArc((0, 0), 0.1, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.05, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0078539816, perimeter: 0.3141592654
            Circle(0.05)
        # OneSide extrude, distance=0.025
        extrude(amount=0.025)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0078539816, perimeter: 0.3141592654
            Circle(0.05)
        # OneSide extrude, distance=-0.3
        extrude(amount=-0.3, mode=Mode.ADD)

        # Sketch2 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.025, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0023382685, perimeter: 0.179999996
            with BuildLine():
                Line((-0.0149999997, 0.0259807615), (-0.0299999993, 0))
                Line((-0.0299999993, 0), (-0.0149999997, -0.0259807615))
                Line((-0.0149999997, -0.0259807615), (0.0149999997, -0.0259807615))
                Line((0.0149999997, -0.0259807615), (0.0299999993, 0))
                Line((0.0299999993, 0), (0.0149999997, 0.0259807615))
                Line((0.0149999997, 0.0259807615), (-0.0149999997, 0.0259807615))
            make_face()
        # OneSide extrude, distance=-0.04
        extrude(amount=-0.04, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a blind rivet (or pop rivet) featuring a cylindrical shaft with a large flanged head, designed for fastening two materials together by deformation of the mandrel inside the hollow body.
def model_30379_f1d5e193_0012():
    """Model: .5M Low Profile"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0019634954, perimeter: 0.1570796327
            Circle(0.025)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0058904862, perimeter: 0.471238898
            with BuildLine():
                CenterArc((0, 0), 0.05, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.025, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.01
        extrude(amount=0.01, mode=Mode.ADD)

        # Sketch2 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.0004500339, perimeter: 0.0789674187
            with BuildLine():
                Line((0.0065806182, -0.0113979651), (0.0131612365, 0))
                Line((0.0131612365, 0), (0.0065806182, 0.0113979651))
                Line((0.0065806182, 0.0113979651), (-0.0065806182, 0.0113979651))
                Line((-0.0065806182, 0.0113979651), (-0.0131612365, 0))
                Line((-0.0131612365, 0), (-0.0065806182, -0.0113979651))
                Line((-0.0065806182, -0.0113979651), (0.0065806182, -0.0113979651))
            make_face()
        # OneSide extrude, distance=-0.02
        extrude(amount=-0.02, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical shaft or axle with a long tubular body featuring two hexagonal end caps or flanges on opposite ends, designed for rotational applications or as a connector component.
def model_30380_4d422f95_0001():
    """Model: Piston Rod"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 11 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.2857775566, perimeter: 18.7206963954
            with BuildLine():
                Line((-1, -7.8138593384), (1, -7.8138593384))
                CenterArc((0, -9.25), 1.75, 124.8499045792, 290.3001908419)
            make_face()
            with BuildLine():
                CenterArc((0, -9.25), 1.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 4.2857775566, perimeter: 18.7206963954
            with BuildLine():
                CenterArc((0, 9.25), 1.75, -55.1500954208, 290.3001908418)
                Line((1, 7.8138593384), (-1, 7.8138593384))
            make_face()
            with BuildLine():
                CenterArc((0, 9.25), 1.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 30.4022145059, perimeter: 35.5131564058
            with BuildLine():
                CenterArc((0, 9.25), 1.75, -124.8499045789, 69.6998091581)
                Line((-1, 7.8138593384), (-1, -7.8138593384))
                CenterArc((0, -9.25), 1.75, 55.1500954211, 69.6998091581)
                Line((1, -7.8138593384), (1, 7.8138593384))
            make_face()
            # Profile area: 0.4266114238, perimeter: 4.1288595262
            with BuildLine():
                Line((1, 7.8138593384), (-1, 7.8138593384))
                CenterArc((0, 9.25), 1.75, -124.8499045789, 69.6998091581)
            make_face()
            # Profile area: 0.4266114238, perimeter: 4.1288595262
            with BuildLine():
                CenterArc((0, -9.25), 1.75, 55.1500954211, 69.6998091581)
                Line((-1, -7.8138593384), (1, -7.8138593384))
            make_face()
        # Symmetric extrude, each_side=1.25
        extrude(amount=1.25, both=True)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 8 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.25, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 14.2853981635, perimeter: 30.1415926536
            with BuildLine():
                CenterArc((0, 6.75), 0.5, 0, 180)
                Line((-0.5, 6.75), (-0.5, -6.75))
                CenterArc((0, -6.75), 0.5, 180, 180)
                Line((0.5, -6.75), (0.5, 6.75))
            make_face()
        # OneSide extrude, distance=-0.75
        extrude(amount=-0.75, mode=Mode.SUBTRACT)
    return part.part


# Description: A sledgehammer consisting of a long cylindrical dark gray handle with a large flat rectangular head at the bottom, featuring a slight blue-tinted striking surface on the lower face.
def model_30380_4d422f95_0003():
    """Model: Crank Shaft"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 9 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 52.5841839562, perimeter: 68.3318560862
            with BuildLine():
                Line((-2.75, 7.5), (2.75, 7.5))
                Line((-2.75, -7.5), (-2.75, 7.5))
                Line((2.75, -7.5), (-2.75, -7.5))
                Line((2.75, 7.5), (2.75, -7.5))
            make_face()
            with BuildLine():
                CenterArc((0, 4.875), 2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0, 0), 2.35, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=2.5
        extrude(amount=2.5)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 9 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 17.3494454294, perimeter: 14.7654854719
            Circle(2.35)
        # OneSide extrude, distance=35.5
        extrude(amount=35.5, mode=Mode.ADD)

        # Sketch1 -> Extrude3 (Join)
        # Sketch on XZ construction plane
        # Sketch has 9 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 5.4977871438, perimeter: 21.9911485751
            with BuildLine():
                CenterArc((0, 4.875), 2, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 4.875), 1.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=2.5
        extrude(amount=2.5, mode=Mode.ADD)

        # Sketch1 -> Extrude4 (Join)
        # Sketch on XZ construction plane
        # Sketch has 9 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 5.4977871438, perimeter: 21.9911485751
            with BuildLine():
                CenterArc((0, 4.875), 2, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 4.875), 1.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.15
        extrude(amount=-0.15, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical mesh or perforated filter component with a dark body featuring ventilation holes or mesh panels on opposing sides, designed for airflow or fluid passage.
def model_30400_8824ce97_0013():
    """Model: 18-03-001100-1_18-03-001104-1-solid1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 7.3120569012, perimeter: 15.3938040026
            with BuildLine():
                CenterArc((0, 0), 1.7, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.75, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.1
        extrude(amount=1.1)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.0681415022, perimeter: 10.6814150222
            with BuildLine():
                CenterArc((0, 0), 0.95, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.75, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.4
        extrude(amount=0.4, mode=Mode.ADD)
    return part.part


# Description: This is a horizontal cylindrical air or hydraulic tank with a rounded end cap on the left, a straight cylindrical body, and rounded end on the right, featuring a small flange or bracket attachment point on the lower left side.
def model_30402_c83c8794_0007():
    """Model: Rear Hub"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))) as sk:
            # Profile area: 0.7466191291, perimeter: 3.0630528373
            Circle(0.4875)
        # TwoSides extrude, along=3, against=-2.4
        extrude(amount=3)
        extrude(sk.sketch, amount=-2.4)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(-2.4, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.1585899224, perimeter: 7.90478389
            with BuildLine():
                Line((-0.6469584864, 0.2417534216), (-0.6654995061, 0.1846900306))
                CenterArc((-0.6559889409, 0.1815998607), 0.01, 162, 90)
                Line((-0.6590791109, 0.1720892955), (-0.5305555853, 0.1303294706))
                CenterArc((-0.5413711801, 0.0970424926), 0.035, -10.1625202369, 82.1625202369)
                CenterArc((0, 0), 0.515, 169.8374797631, 56.3250404738)
                CenterArc((-0.380938339, -0.3967190213), 0.035, -36, 82.1625202369)
                Line((-0.4320546513, -0.5266201461), (-0.3526227442, -0.4172915052))
                CenterArc((-0.4239644814, -0.5324979986), 0.01, 144, 90)
                Line((-0.4298423339, -0.5405881685), (-0.3813013143, -0.5758552837))
                CenterArc((-0.3754234617, -0.5677651137), 0.01, -126, 90)
                Line((-0.3673332918, -0.5736429663), (-0.2879013846, -0.4643143254))
                CenterArc((-0.2595857898, -0.4848868092), 0.035, 61.8374797631, 82.1625202369)
                CenterArc((0, 0), 0.515, -118.1625202369, 56.3250404738)
                CenterArc((0.2595857898, -0.4848868092), 0.035, 36, 82.1625202369)
                Line((0.3673332918, -0.5736429663), (0.2879013846, -0.4643143254))
                CenterArc((0.3754234617, -0.5677651137), 0.01, -144, 90)
                Line((0.3813013143, -0.5758552837), (0.4298423339, -0.5405881685))
                CenterArc((0.4239644814, -0.5324979986), 0.01, -54, 90)
                Line((0.4320546513, -0.5266201461), (0.3526227442, -0.4172915052))
                CenterArc((0.380938339, -0.3967190213), 0.035, 133.8374797631, 82.1625202369)
                CenterArc((0, 0), 0.515, -46.1625202369, 56.3250404738)
                CenterArc((0.5413711801, 0.0970424926), 0.035, 108, 82.1625202369)
                Line((0.6590791109, 0.1720892955), (0.5305555853, 0.1303294706))
                CenterArc((0.6559889409, 0.1815998607), 0.01, -72, 90)
                Line((0.6469584864, 0.2417534216), (0.6654995061, 0.1846900306))
                CenterArc((0.6374479212, 0.2386632517), 0.01, 18, 90)
                Line((0.6343577513, 0.2481738168), (0.5058342257, 0.2064139919))
                CenterArc((0.4950186309, 0.23970097), 0.035, -154.1625202369, 82.1625202369)
                CenterArc((0, 0), 0.515, 25.8374797631, 56.3250404738)
                CenterArc((0.075, 0.5448623679), 0.035, 180, 82.1625202369)
                Line((0.04, 0.68), (0.04, 0.5448623679))
                CenterArc((0.03, 0.68), 0.01, 0, 90)
                Line((-0.03, 0.69), (0.03, 0.69))
                CenterArc((-0.03, 0.68), 0.01, 90, 90)
                Line((-0.04, 0.68), (-0.04, 0.5448623679))
                CenterArc((-0.075, 0.5448623679), 0.035, -82.1625202369, 82.1625202369)
                CenterArc((0, 0), 0.515, 97.8374797631, 56.3250404738)
                CenterArc((-0.4950186309, 0.23970097), 0.035, -108, 82.1625202369)
                Line((-0.6343577513, 0.2481738168), (-0.5058342257, 0.2064139919))
                CenterArc((-0.6374479212, 0.2386632517), 0.01, 72, 90)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.4875, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.4
        extrude(amount=-0.4, mode=Mode.ADD)
    return part.part


# Description: This is a long, rectangular channel or tray with a shallow U-shaped cross-section, featuring rounded end caps and a slight upward curve along its length, commonly used as a cable management or wire routing component.
def model_30417_0010bc7c_0003():
    """Model: Tube guide"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 13 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 19.02, perimeter: 37.8
            with BuildLine():
                Line((-8.5, -0.4), (-8.5, 0.3))
                Line((8.5, -0.4), (-8.5, -0.4))
                Line((8.5, 0.3), (8.5, -0.4))
                Line((8.9, 0.3), (8.5, 0.3))
                Line((8.9, 0.7), (8.9, 0.3))
                Line((-8.9, 0.7), (8.9, 0.7))
                Line((-8.9, 0.3), (-8.9, 0.7))
                Line((-8.5, 0.3), (-8.9, 0.3))
            make_face()
        # TwoSides extrude (symmetric), distance=0.2
        extrude(amount=0.2, both=True)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XY construction plane
        # Sketch has 8 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 7.12, perimeter: 36.4
            with BuildLine():
                Line((8.9, 0.3), (-8.9, 0.3))
                Line((8.9, 0.7), (8.9, 0.3))
                Line((-8.9, 0.7), (8.9, 0.7))
                Line((-8.9, 0.3), (-8.9, 0.7))
            make_face()
        # TwoSides extrude (symmetric), distance=0.3
        extrude(amount=0.3, both=True, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical container or vessel with a curved, tapered top opening and a ribbed or fluted surface texture on its sides, featuring a slightly wider base that narrows toward the top.
def model_30424_e6ca5ede_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 17671.4586764426, perimeter: 471.2388980385
            Circle(75)
        # OneSide extrude, distance=70
        extrude(amount=70)

        # Sketch2 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 70, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2488.495032468, perimeter: 258.1727308221
            with BuildLine():
                Line((-74.2139944667, -10.8297287731), (30.6521977254, -68.4502941893))
                CenterArc((0, 0), 75, -171.6976733274, 105.8206172713)
            make_face()
        # OneSide extrude, distance=-80
        extrude(amount=-80, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a flat, elongated metal bar or beam with a slightly trapezoidal profile, featuring beveled or angled edges on both ends and a horizontal slot or groove running along its length.
def model_30426_2cde26de_0027():
    """Model: Stecca1 (2)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 227.5, perimeter: 137
            with BuildLine():
                Line((32.5, -1.75), (32.5, 1.75))
                Line((32.5, 1.75), (-32.5, 1.75))
                Line((-32.5, 1.75), (-32.5, -1.75))
                Line((-32.5, -1.75), (32.5, -1.75))
            make_face()
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)

        # Sketch3 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1.5), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((-30.5, 0)):
                Circle(0.2)
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((30.5, 0)):
                Circle(0.2)
        # OneSide extrude, distance=-1.5
        extrude(amount=-1.5, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical sleeve or coupling component with two coaxial circular openings on opposite ends, featuring a mesh-textured surface and a hollow tubular body with visible internal ribbing or reinforcement structures.
def model_30445_791b6800_0012():
    """Model: Component10"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.5026548246, perimeter: 5.0265482457
            with BuildLine():
                CenterArc((-6.9722804083, 2.824297797), 0.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-6.9722804083, 2.824297797), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.15
        extrude(amount=0.15)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.2199114858, perimeter: 4.398229715
            with BuildLine():
                CenterArc((6.9722804083, 2.824297797), 0.4, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((6.9722804083, 2.824297797), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)
    return part.part


# Description: This is a pneumatic or hydraulic cylinder actuator with a dark gray rod extending through a blue anodized aluminum body, featuring a compact single-acting or double-acting design with end ports for fluid connection.
def model_30447_4ed3b778_0002():
    """Model: Valve Stem Offset Post"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0445235977, perimeter: 1.8485408733
            with BuildLine():
                Line((-0.1663335373, 0.0796152966), (-0.152115638, -0.1042414205))
                Line((-0.152115638, -0.1042414205), (0.0142178993, -0.1838567171))
                Line((0.0142178993, -0.1838567171), (0.1663335373, -0.0796152966))
                Line((0.1663335373, -0.0796152966), (0.152115638, 0.1042414205))
                Line((0.152115638, 0.1042414205), (-0.0142178993, 0.1838567171))
                Line((-0.0142178993, 0.1838567171), (-0.1663335373, 0.0796152966))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.11811, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0160778283, perimeter: 1.3326007718
            with BuildLine():
                CenterArc((0, 0), 0.11811, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.09398, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0277473016, perimeter: 0.5904937552
            Circle(0.09398)
        # OneSide extrude, distance=0.635
        extrude(amount=0.635)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0160778283, perimeter: 1.3326007718
            with BuildLine():
                CenterArc((0, 0), 0.11811, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.09398, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.15748
        extrude(amount=-0.15748, mode=Mode.ADD)

        # Sketch1 -> Extrude3 (Join)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0277473016, perimeter: 0.5904937552
            Circle(0.09398)
        # OneSide extrude, distance=-0.36068
        extrude(amount=-0.36068, mode=Mode.ADD)

        # Sketch1 -> Extrude4 (Join)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0277473016, perimeter: 0.5904937552
            Circle(0.09398)
        # OneSide extrude, distance=0.9525
        extrude(amount=0.9525, mode=Mode.ADD)
    return part.part


# Description: This is a curved cylindrical sleeve or ring component with a hollow center, featuring a C-shaped cross-section with mesh or latticed surface texturing on the outer walls, likely designed for structural support, containment, or rotational applications.
def model_30447_4ed3b778_0004():
    """Model: Eccentric Strap Back"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.2426190193, perimeter: 7.0296630106
            with BuildLine():
                CenterArc((0, 0), 1.19126, 0, 180)
                Line((-0.79248, 0), (-1.19126, 0))
                CenterArc((0, 0), 0.79248, 0, 180)
                Line((0.79248, 0), (1.19126, 0))
            make_face()
        # Symmetric extrude, each_side=0.238125
        extrude(amount=0.238125, both=True)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.238125, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.212736068, perimeter: 5.3972073431
            with BuildLine():
                Line((0.79248, 0), (0.87376, 0))
                CenterArc((0, 0), 0.87376, 0, 180)
                Line((-0.87376, 0), (-0.79248, 0))
                CenterArc((0, 0), 0.79248, 0, 180)
            make_face()
        # OneSide extrude, distance=-0.16129
        extrude(amount=-0.16129, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a mounting bracket or stand featuring an angular, diamond-shaped base with a cylindrical post rising from its center, designed to hold or support a vertical component.
def model_30447_4ed3b778_0009():
    """Model: Bellcrank Mounting post"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1974757462, perimeter: 1.6541778033
            with BuildLine():
                Line((0.1378481503, -0.23876), (0.2756963005, 0))
                Line((0.2756963005, 0), (0.1378481503, 0.23876))
                Line((0.1378481503, 0.23876), (-0.1378481503, 0.23876))
                Line((-0.1378481503, 0.23876), (-0.2756963005, 0))
                Line((-0.2756963005, 0), (-0.1378481503, -0.23876))
                Line((-0.1378481503, -0.23876), (0.1378481503, -0.23876))
            make_face()
        # OneSide extrude, distance=0.15875
        extrude(amount=0.15875)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.15875, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0277473016, perimeter: 0.5904937552
            Circle(0.09398)
        # OneSide extrude, distance=0.39624
        extrude(amount=0.39624, mode=Mode.ADD)
    return part.part


# Description: This is a blue anodized aluminum louver or vent component with a streamlined, wing-like shape featuring hinged upper panels, a flat base platform, and angular geometric facets designed for directional airflow control or aesthetic styling.
def model_30447_4ed3b778_0012():
    """Model: Frame"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 22 constraints, 13 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 6.2130708899, perimeter: 10.297580621
            with BuildLine():
                Line((-2.4065112827, 5.3519963712), (0, 4.1619949869))
                Line((0, 7.62), (0, 4.1619949869))
                Line((0, 7.62), (-1.8097033214, 7.62))
                Line((-1.8097033214, 7.62), (-2.4065112827, 5.3519963712))
            make_face()
            # Profile area: 8.8728632651, perimeter: 12.0642201865
            with BuildLine():
                Line((2.7287282199, 4.1275), (3.4806576823, 1.27))
                Line((2.7287282199, 4.1275), (0.0697583853, 4.1275))
                Line((0, 4.1619949869), (0.0697583853, 4.1275))
                Line((0, 4.1619949869), (0, 1.27))
                Line((0, 1.27), (3.4806576823, 1.27))
            make_face()
            # Profile area: 17.83899658, perimeter: 34.29
            with BuildLine():
                Line((6.604, 1.27), (6.604, 0.47498))
                Line((3.4806576823, 1.27), (6.604, 1.27))
                Line((0, 1.27), (3.4806576823, 1.27))
                Line((-3.4806576823, 1.27), (0, 1.27))
                Line((-6.35, 1.27), (-3.4806576823, 1.27))
                Line((-6.35, 0.47498), (-6.35, 1.27))
                Line((-7.62, 0.47498), (-6.35, 0.47498))
                Line((-7.62, 0), (-7.62, 0.47498))
                Line((-7.62, 0), (8.255, 0))
                Line((8.255, 0.47498), (8.255, 0))
                Line((6.604, 0.47498), (8.255, 0.47498))
            make_face()
            # Profile area: 10.583825297, perimeter: 13.2782705818
            with BuildLine():
                Line((0, 4.1619949869), (0, 1.27))
                Line((-2.4065112827, 5.3519963712), (0, 4.1619949869))
                Line((-2.4065112827, 5.3519963712), (-3.4806576823, 1.27))
                Line((-3.4806576823, 1.27), (0, 1.27))
            make_face()
            # Profile area: 9.9992698921, perimeter: 12.810890598
            with BuildLine():
                Line((6.604, 1.27), (6.604, 4.1275))
                Line((6.604, 4.1275), (2.7287282199, 4.1275))
                Line((2.7287282199, 4.1275), (3.4806576823, 1.27))
                Line((3.4806576823, 1.27), (6.604, 1.27))
            make_face()
            # Profile area: 5.6497951559, perimeter: 11.0880757513
            with BuildLine():
                Line((-1.8097033214, 7.62), (-2.4065112827, 5.3519963712))
                Line((-1.8097033214, 7.62), (-6.0325, 7.62))
                Line((-6.0325, 7.62), (-6.0325, 7.14502))
                Line((-6.0325, 7.14502), (-2.4065112827, 5.3519963712))
            make_face()
            # Profile area: 12.1855467434, perimeter: 16.9573702808
            with BuildLine():
                Line((0, 10.63625), (0, 7.62))
                Line((0, 7.62), (0, 4.1619949869))
                Line((0, 4.1619949869), (0.0697583853, 4.1275))
                Line((2.7287282199, 4.1275), (0.0697583853, 4.1275))
                Line((1.016, 10.63625), (2.7287282199, 4.1275))
                Line((0, 10.63625), (1.016, 10.63625))
            make_face()
            # Profile area: 4.2615138216, perimeter: 8.9608840717
            with BuildLine():
                Line((0, 7.62), (-1.8097033214, 7.62))
                Line((0, 10.63625), (0, 7.62))
                Line((0, 10.63625), (-1.016, 10.63625))
                Line((-1.016, 10.63625), (-1.8097033214, 7.62))
            make_face()
        # Symmetric extrude, each_side=0.23749
        extrude(amount=0.23749, both=True)
    return part.part


# Description: This is a shaft or rod assembly with a long cylindrical body and a polygonal (likely hexagonal or octagonal) head or flange at one end, commonly used as a fastener, pivot pin, or drive shaft component.
def model_30447_4ed3b778_0015():
    """Model: Piston Rod"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2628322282, perimeter: 2.4037278338
            with BuildLine():
                CenterArc((0.47625, 0), 0.15875, 90, 180)
                Line((0.47625, 0.3175), (0.47625, 0.15875))
                Line((0, 0.3175), (0.47625, 0.3175))
                Line((0, -0.3175), (0, 0.3175))
                Line((0.47625, -0.3175), (0, -0.3175))
                Line((0.47625, -0.15875), (0.47625, -0.3175))
            make_face()
            # Profile area: 0.1187595654, perimeter: 1.8136835013
            with BuildLine():
                CenterArc((0.47625, 0), 0.15875, -90, 180)
                Line((0.47625, -0.15875), (0.47625, -0.3175))
                CenterArc((0.47625, 0), 0.3175, -90, 180)
                Line((0.47625, 0.3175), (0.47625, 0.15875))
            make_face()
        # Symmetric extrude, each_side=0.3175
        extrude(amount=0.3175, both=True)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.0847620271, perimeter: 1.9629927537
            with BuildLine():
                CenterArc((0, 0), 0.19939, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.11303, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=5.08
        extrude(amount=5.08, mode=Mode.ADD)

        # Sketch2 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.0401362994, perimeter: 0.7101884353
            Circle(0.11303)
        # OneSide extrude, distance=5.87375
        extrude(amount=5.87375, mode=Mode.ADD)
    return part.part


# Description: This is a rectangular box-shaped bracket or housing with an open interior cavity, featuring multiple vertical slots or grooves along its sides and reinforcing ribs or gussets for structural support.
def model_30447_4ed3b778_0021():
    """Model: Slide Valve"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 16 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1641302031, perimeter: 1.6138548546
            with BuildLine():
                Line((0, 0.32004), (0, 0))
                CenterArc((0, 0.39878), 0.07874, 180, 90)
                Line((-0.07874, 0.39878), (-0.07874, 0.47625))
                Line((-0.23622, 0.47625), (-0.07874, 0.47625))
                Line((-0.3937, 0.31877), (-0.23622, 0.47625))
                Line((-0.3937, 0), (-0.3937, 0.31877))
                Line((0, 0), (-0.3937, 0))
            make_face()
            # Profile area: 0.1641302031, perimeter: 1.6138548546
            with BuildLine():
                Line((0.3937, 0), (0.3937, 0.31877))
                Line((0.3937, 0.31877), (0.23622, 0.47625))
                Line((0.23622, 0.47625), (0.07874, 0.47625))
                Line((0.07874, 0.39878), (0.07874, 0.47625))
                CenterArc((0, 0.39878), 0.07874, -90, 90)
                Line((0, 0.32004), (0, 0))
                Line((0, 0), (0.3937, 0))
            make_face()
        # Symmetric extrude, each_side=0.3937
        extrude(amount=0.3937, both=True)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 18 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.2146154801, perimeter: 1.7180785307
            with BuildLine():
                CenterArc((-0.13622, 0.13622), 0.1, 90, 90)
                Line((-0.23622, -0.13622), (-0.23622, 0.13622))
                CenterArc((-0.13622, -0.13622), 0.1, -180, 90)
                Line((0.13622, -0.23622), (-0.13622, -0.23622))
                CenterArc((0.13622, -0.13622), 0.1, -90, 90)
                Line((0.23622, 0.13622), (0.23622, -0.13622))
                CenterArc((0.13622, 0.13622), 0.1, 0, 90)
                Line((-0.13622, 0.23622), (0.13622, 0.23622))
            make_face()
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical roller or spacer with a knurled or textured surface pattern running along its length, featuring a smooth cylindrical body with rounded ends.
def model_30643_be4a0dae_0000():
    """Model: Component1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 0.0121908231, perimeter: 0.411
            with BuildLine():
                Line((0.03425, 0.0593227402), (0.0685, 0))
                Line((-0.03425, 0.0593227402), (0.03425, 0.0593227402))
                Line((-0.0685, 0), (-0.03425, 0.0593227402))
                Line((-0.03425, -0.0593227402), (-0.0685, 0))
                Line((0.03425, -0.0593227402), (-0.03425, -0.0593227402))
                Line((0.0685, 0), (0.03425, -0.0593227402))
            make_face()
        # OneSide extrude, distance=0.313
        extrude(amount=0.313)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            Circle(0.25)
        # OneSide extrude, distance=2
        extrude(amount=2, mode=Mode.ADD)
    return part.part


# Description: This is a long, slender metal shaft or rod with a hexagonal or angular cross-section, featuring a notch or slot cut into the upper end and tapered or beveled edges along its length.
def model_30708_4282508b_0001():
    """Model: Component18"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 3.2258, perimeter: 7.62
            with BuildLine():
                Line((2.54, 5.0800001216), (2.54, 3.8100001216))
                Line((0, 5.0800001216), (2.54, 5.0800001216))
                Line((0, 3.8100001216), (0, 5.0800001216))
                Line((2.54, 3.8100001216), (0, 3.8100001216))
            make_face()
        # OneSide extrude, distance=30.48
        extrude(amount=30.48)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.3340559098, perimeter: 3.3280380593
            with BuildLine():
                Line((0, 5.0800001216), (-0.3760337396, 5.0800001216))
                CenterArc((-0.3809294474, 4.826024016), 0.2540232867, -89.9940303673, 178.8897191775)
                Line((-0.3809029807, 4.5720007307), (-0.6349029595, 4.5719742665))
                Line((-0.6349029595, 4.5719742665), (-0.6348632726, 4.1909742686))
                Line((-0.6348632726, 4.1909742686), (0, 4.1909742686))
                Line((0, 4.1909742686), (0, 5.0800001216))
            make_face()
        # OneSide extrude, distance=-30.48
        extrude(amount=-30.48, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a long, narrow metal strip or beam with a slightly tapered hexagonal cross-section, featuring multiple evenly-spaced holes or mounting points along its length and angled end caps.
def model_30729_b4d83b07_0015():
    """Model: 4 Structure v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 26 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 10.9446900494, perimeter: 72.9646003294
            with BuildLine():
                CenterArc((-3.5, 3.5), 1.5, 90, 90)
                Line((-5, -3.5), (-5, 3.5))
                CenterArc((-3.5, -3.5), 1.5, -180, 90)
                Line((3.5, -5), (-3.5, -5))
                CenterArc((3.5, -3.5), 1.5, -90, 90)
                Line((5, 3.5), (5, -3.5))
                CenterArc((3.5, 3.5), 1.5, 0, 90)
                Line((-3.5, 5), (3.5, 5))
            make_face()
            with BuildLine():
                Line((-3.5, 4.7), (3.5, 4.7))
                CenterArc((3.5, 3.5), 1.2, 0, 90)
                Line((4.7, 3.5), (4.7, -3.5))
                CenterArc((3.5, -3.5), 1.2, -90, 90)
                Line((3.5, -4.7), (-3.5, -4.7))
                CenterArc((-3.5, -3.5), 1.2, -180, 90)
                Line((-4.7, -3.5), (-4.7, 3.5))
                CenterArc((-3.5, 3.5), 1.2, 90, 90)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=76
        extrude(amount=76, both=True)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -5), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 7.0685834706, perimeter: 9.4247779608
            with Locations((-17.5, 0)):
                Circle(1.5)
            # Profile area: 7.0685834706, perimeter: 9.4247779608
            with Locations((17.5, 0)):
                Circle(1.5)
        # OneSide extrude, distance=-30
        extrude(amount=-30, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical rod or tube with a smooth, tapered surface, featuring a slightly knurled or textured finish along its length.
def model_30729_b4d83b07_0016():
    """Model: 5 Structure v5 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 26 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 10.9446900494, perimeter: 72.9646003294
            with BuildLine():
                CenterArc((-3.5, -3.5), 1.5, -180, 90)
                Line((-3.5, -5), (3.5, -5))
                CenterArc((3.5, -3.5), 1.5, -90, 90)
                Line((5, -3.5), (5, 3.5))
                CenterArc((3.5, 3.5), 1.5, 0, 90)
                Line((3.5, 5), (-3.5, 5))
                CenterArc((-3.5, 3.5), 1.5, 90, 90)
                Line((-5, 3.5), (-5, -3.5))
            make_face()
            with BuildLine():
                Line((3.5, 4.7), (-3.5, 4.7))
                CenterArc((3.5, 3.5), 1.2, 0, 90)
                Line((4.7, -3.5), (4.7, 3.5))
                CenterArc((3.5, -3.5), 1.2, -90, 90)
                Line((-3.5, -4.7), (3.5, -4.7))
                CenterArc((-3.5, -3.5), 1.2, -180, 90)
                Line((-4.7, 3.5), (-4.7, -3.5))
                CenterArc((-3.5, 3.5), 1.2, 90, 90)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=220.5
        extrude(amount=220.5)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -5), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            with Locations((0, 45)):
                Circle(1)
        # OneSide extrude, distance=-14
        extrude(amount=-14, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a long, narrow rectangular bar or rail with a flat top surface, beveled or chamfered edges at both ends, and what appears to be a central slot or groove running along its length, commonly used as a linear guide, support beam, or mounting rail in mechanical assemblies.
def model_30729_b4d83b07_0019():
    """Model: 2 Structure v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 26 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 12.1446900494, perimeter: 80.9646003294
            with BuildLine():
                CenterArc((-4.5, -3.5), 1.5, -180, 90)
                Line((-4.5, -5), (4.5, -5))
                CenterArc((4.5, -3.5), 1.5, -90, 90)
                Line((6, -3.5), (6, 3.5))
                CenterArc((4.5, 3.5), 1.5, 0, 90)
                Line((4.5, 5), (-4.5, 5))
                CenterArc((-4.5, 3.5), 1.5, 90, 90)
                Line((-6, 3.5), (-6, -3.5))
            make_face()
            with BuildLine():
                Line((4.5, 4.7), (-4.5, 4.7))
                CenterArc((4.5, 3.5), 1.2, 0, 90)
                Line((5.7, -3.5), (5.7, 3.5))
                CenterArc((4.5, -3.5), 1.2, -90, 90)
                Line((-4.5, -4.7), (4.5, -4.7))
                CenterArc((-4.5, -3.5), 1.2, -180, 90)
                Line((-5.7, 3.5), (-5.7, -3.5))
                CenterArc((-4.5, 3.5), 1.2, 90, 90)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=62.93
        extrude(amount=62.93, both=True)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 7.0685834706, perimeter: 9.4247779608
            with Locations((58.93, 0)):
                Circle(1.5)
        # OneSide extrude, distance=-4
        extrude(amount=-4, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical rod or pin with a simple, elongated tubular shape, featuring a slight head or collar at the top end and a tapered or pointed tip at the bottom.
def model_30845_630b097e_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch9 -> Extrude8 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((24, 0)):
                Circle(0.2)
        # OneSide extrude, distance=6.8188211043
        extrude(amount=6.8188211043)

        # Sketch10 -> Extrude9 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 6.8188211043, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1570803152, perimeter: 3.1415949287
            with BuildLine():
                CenterArc((-24, 0), 0.3000003621, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-24, 0), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((-24, 0)):
                Circle(0.2)
        # OneSide extrude, distance=0.1296
        extrude(amount=0.1296, mode=Mode.ADD)
    return part.part


# Description: This is a curved blade or fin-shaped component with a tapered, elongated form that features a smooth, aerodynamic profile with rounded edges and a slight twist or bend along its length.
def model_30855_9deadbdd_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 17 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 4752.1108419241, perimeter: 289.1336783062
            with BuildLine():
                Line((-24.3313390995, 20.2206137363), (24.3313390995, 20.2206137363))
                CenterArc((275, 0.2018866816), 300, 176.1738616846, 3.8261383154)
                Line((-25, 0.2018866816), (-25, -75))
                Line((-25, -75), (25, -75))
                Line((25, -75), (25, 0.2018866816))
                CenterArc((-274.9999999999, 0.2018866816), 299.9999999999, 0, 3.8261383154)
            make_face()
            # Profile area: 2327.8388638839, perimeter: 194.3662752425
            with BuildLine():
                CenterArc((275, 0.2018866816), 300, 172.3647288043, 3.8091328803)
                Line((-24.3313390995, 20.2206137363), (24.3313390995, 20.2206137363))
                CenterArc((-274.9999999999, 0.2018866816), 299.9999999999, 3.8261383154, 3.8091328803)
                Line((22.3401806817, 40.0618534679), (17.6565440566, 75))
                Line((17.6565440566, 75), (-17.6565440566, 75))
                Line((-22.3401806817, 40.0618534679), (-17.6565440566, 75))
            make_face()
            # Profile area: 481.2996831813, perimeter: 90.318766191
            with BuildLine():
                Line((17.6565440566, 75), (-17.6565440566, 75))
                Line((17.6565440566, 75), (17.3448438731, 77.3251647292))
                CenterArc((0, 75), 17.5, 7.6352711957, 164.7294576086)
                Line((-17.6565440566, 75), (-17.3448438731, 77.3251647292))
            make_face()
        # Symmetric extrude, each_side=1.5
        extrude(amount=1.5, both=True)
    return part.part


# Description: These are two cylindrical fastening pins or dowels with flat heads, featuring smooth shafts and slightly tapered or rounded head tops.
def model_30904_54099e05_0002():
    """Model: Sujecion de proyector v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((0, 7.5)):
                Circle(0.5)
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            Circle(0.5)
        # OneSide extrude, distance=20
        extrude(amount=20)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 20, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            Circle(1)
            # Profile area: 2.3561944902, perimeter: 9.4247779608
            with BuildLine():
                CenterArc((0, -7.5), 1, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, -7.5), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((0, -7.5)):
                Circle(0.5)
        # OneSide extrude, distance=0.8
        extrude(amount=0.8, mode=Mode.ADD)
    return part.part


# Description: This is a triangular bracket or support structure featuring a blue triangular frame with internal ribbing and a dark gray flat mounting flange or base extending diagonally beneath it.
def model_30904_54099e05_0010():
    """Model: Embellecedor soporte v7"""
    with BuildPart() as part:
        # Sketch1 -> Extrude3 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 14 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 11.5324484677, perimeter: 15.542950408
            with BuildLine():
                Line((-2.7727782058, 1.2), (2.7727782058, 1.2))
                Line((0, -2.9591673087), (-2.7727782058, 1.2))
                Line((2.7727782058, 1.2), (0, -2.9591673087))
            make_face()
        # OneSide extrude, distance=2.5
        extrude(amount=2.5)

        # Sketch3 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 31.7975009131, perimeter: 45.6707067853
            with BuildLine():
                Line((-5.3746286309, -3.3), (5.3746286309, -3.3))
                Line((5.3746286309, -3.3), (0, 4.7619429464))
                Line((0, 4.7619429464), (-5.3746286309, -3.3))
            make_face()
            with BuildLine():
                Line((2.7727782058, -1.2), (0, 2.9591673087))
                Line((-2.7727782058, -1.2), (2.7727782058, -1.2))
                Line((0, 2.9591673087), (-2.7727782058, -1.2))
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 11.5324484677, perimeter: 15.542950408
            with BuildLine():
                Line((0, 2.9591673087), (-2.7727782058, -1.2))
                Line((-2.7727782058, -1.2), (2.7727782058, -1.2))
                Line((2.7727782058, -1.2), (0, 2.9591673087))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical pen or marker with a dark gray barrel, a tapered grip section, and a blue cap or tip at the top end.
def model_30904_54099e05_0014():
    """Model: Rotulador azul v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            Circle(1)
        # OneSide extrude, distance=20
        extrude(amount=20)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 20, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.7812544346, perimeter: 12.9284023409
            with BuildLine():
                CenterArc((0, 0), 1, -120.0000004929, 240.0000009859)
                Line((-0.5000000075, -0.8660253995), (-0.5000000075, -1.0000000149))
                Line((-0.5000000075, -1.0000000149), (-1.1180339754, -1.0000000149))
                CenterArc((0, 0), 1.5, -138.1896843406, 276.3793686812)
                Line((-1.1180339754, 1.0000000149), (-0.5000000075, 1.0000000149))
                Line((-0.5000000075, 1.0000000149), (-0.5000000075, 0.8660253995))
            make_face()
            # Profile area: 1.1457363824, perimeter: 5.7875952606
            with BuildLine():
                CenterArc((0, 0), 1, 120.0000004929, 119.9999990141)
                Line((-0.5000000075, 1.0000000149), (-0.5000000075, 0.8660253995))
                Line((-1.1180339754, 1.0000000149), (-0.5000000075, 1.0000000149))
                CenterArc((0, 0), 1.5, 138.1896843406, 83.6206313188)
                Line((-0.5000000075, -1.0000000149), (-1.1180339754, -1.0000000149))
                Line((-0.5000000075, -0.8660253995), (-0.5000000075, -1.0000000149))
            make_face()
            # Profile area: 1.2400788706, perimeter: 5.9531151472
            with BuildLine():
                Line((-2.0000000298, 1.0000000149), (-1.1180339754, 1.0000000149))
                Line((-2.0000000298, -1.0000000149), (-2.0000000298, 1.0000000149))
                Line((-1.1180339754, -1.0000000149), (-2.0000000298, -1.0000000149))
                CenterArc((0, 0), 1.5, 138.1896843406, 83.6206313188)
            make_face()
            # Profile area: 2.5274078172, perimeter: 5.920841021
            with BuildLine():
                Line((-0.5000000075, 0.8660253995), (-0.5000000075, -0.8660253995))
                CenterArc((0, 0), 1, -120.0000004929, 240.0000009859)
            make_face()
            # Profile area: 0.6141848364, perimeter: 3.8264458842
            with BuildLine():
                CenterArc((0, 0), 1, 120.0000004929, 119.9999990141)
                Line((-0.5000000075, 0.8660253995), (-0.5000000075, -0.8660253995))
            make_face()
        # OneSide extrude, distance=8
        extrude(amount=8, mode=Mode.ADD)
    return part.part


# Description: This is a straight cylindrical rod or shaft with a slight taper, featuring a smooth, elongated body with a rounded or pointed end.
def model_30904_54099e05_0019():
    """Model: Soporte vertical v12"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 11 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 24.2128129211, perimeter: 28
            with BuildLine():
                Line((1.5, 2.5), (4, 2.5))
                Line((1.5, 2), (1.5, 2.5))
                Line((2, 2), (1.5, 2))
                Line((2, 1.5), (2, 2))
                Line((-2, 1.5), (2, 1.5))
                Line((-2, 2), (-2, 1.5))
                Line((-1.5, 2), (-2, 2))
                Line((-1.5, 2.5), (-1.5, 2))
                Line((-4, 2.5), (-1.5, 2.5))
                Line((0, -4.4282032303), (-4, 2.5))
                Line((4, 2.5), (0, -4.4282032303))
            make_face()
        # OneSide extrude, distance=200
        extrude(amount=200)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 11 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -1.5), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 1.1963495408, perimeter: 5.5707963268
            with BuildLine():
                CenterArc((-1, 25.25), 0.25, 90, 180)
                Line((1, 25), (-1, 25))
                CenterArc((1, 25.25), 0.25, -90, 180)
                Line((-1, 25.5), (1, 25.5))
            make_face()
        # OneSide extrude, distance=-0.6
        extrude(amount=-0.6, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a duct connector or air intake component with an elongated body featuring a rectangular main chamber, a tapered/curved inlet section at the top, internal mesh or baffle structures for airflow management, and a protruding mounting flange or outlet at the bottom.
def model_30905_511b96bf_0001():
    """Model: gotowa raczka v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 15 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 11.1559335082, perimeter: 14.6468993372
            with BuildLine():
                CenterArc((-0.4645850778, 0.793219535), 0.3, -130.5953080831, 141.9052405572)
                Line((-0.1704108751, 0.8520543755), (-0.839223227, 4.1961161351))
                CenterArc((-1.8198039027, 4), 1, 11.309932474, 78.690067526)
                Line((-1.8198039027, 5), (-2.1801960973, 5))
                CenterArc((-2.1801960973, 4), 1, 90, 78.690067526)
                Line((-3.8295891249, 0.8520543755), (-3.160776773, 4.1961161351))
                CenterArc((-3.5354149222, 0.793219535), 0.3, 168.690067526, 141.9052405572)
                Line((-2.6507120388, 1.1562880018), (-3.3402013105, 0.5654221561))
                CenterArc((-2, 0.3969634055), 1, 49.4046919169, 81.1906161663)
                Line((-0.6597986895, 0.5654221561), (-1.3492879612, 1.1562880018))
            make_face()
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -5), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.0401624861, perimeter: 1.0355924601
            with BuildLine():
                Line((2.1801960973, 0.4601471863), (2.1801960973, 0.9398528346))
                CenterArc((2.0000000298, 0.7000000104), 0.3, -53.0832803376, 106.1665606753)
            make_face()
            # Profile area: 0.0401624575, perimeter: 1.0355922215
            with BuildLine():
                CenterArc((2.0000000298, 0.7000000104), 0.3, 126.9167339006, 106.1665321987)
                Line((1.8198039027, 0.9398527898), (1.8198039027, 0.460147231))
            make_face()
            # Profile area: 0.2024183953, perimeter: 1.7325933248
            with BuildLine():
                Line((1.8198039027, 0.9398527898), (1.8198039027, 0.460147231))
                CenterArc((2.0000000298, 0.7000000104), 0.3, -126.9167339006, 73.833453563)
                Line((2.1801960973, 0.4601471863), (2.1801960973, 0.9398528346))
                CenterArc((2.0000000298, 0.7000000104), 0.3, 53.0832803376, 73.833453563)
            make_face()
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a hex head bolt or machine screw featuring a cylindrical shaft with a rounded head at the top and a threaded or smooth cylindrical body, angled at approximately 45 degrees.
def model_30905_511b96bf_0005():
    """Model: dysza srodek v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 12.5663706144, perimeter: 12.5663706144
            Circle(2)
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 7.0685834706, perimeter: 9.4247779608
            Circle(1.5)
        # OneSide extrude, distance=24
        extrude(amount=24, mode=Mode.ADD)
    return part.part


# Description: This is a trapezoidal duct or channel component with a tapered wedge shape, featuring a ribbed or corrugated interior surface and raised flanges along the sides for structural reinforcement and assembly.
def model_30905_511b96bf_0014():
    """Model: Oparcie v5"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 9 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3500.5470561781, perimeter: 252.2435849951
            with BuildLine():
                CenterArc((-5.188823465, 70), 10, -19.8481714738, 109.8481714738)
                Line((-5.188823465, 80), (-39.311176535, 80))
                CenterArc((-39.311176535, 70), 10, 90, 109.8481714738)
                CenterArc((-161.0475554596, 26.0565555676), 119.4247745304, -12.6023833803, 32.4505548542)
                Line((0, 0), (-44.5, 0))
                CenterArc((116.5475554596, 26.0565555676), 119.4247745304, 160.1518285262, 32.4505548542)
            make_face()
        # OneSide extrude, distance=7.5
        extrude(amount=7.5)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on XY construction plane
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 93.7990148018, perimeter: 107.7729126394
            with BuildLine():
                CenterArc((-21.8585664788, 144.1613642247), 139.2756657319, -101.1188412483, 22.2376824966)
                Line((-48.7171329577, 7.5), (5, 7.5))
            make_face()
        # OneSide extrude, distance=-105
        extrude(amount=-105, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical rod or shaft with a slightly tapered or beveled end, featuring a simple elongated tubular shape with no holes, slots, or flanges.
def model_30974_a9e13c20_0001():
    """Model: Straw"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.5542113053, perimeter: 6.9821896726
            with BuildLine():
                CenterArc((0, 0), 0.635, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.47625, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=19.05
        extrude(amount=19.05)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on XY construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.8064499956, perimeter: 4.3360512174
            with BuildLine():
                Line((0.635, 17.78), (-0.635, 19.05))
                Line((0.6349999931, 19.05), (0.635, 17.78))
                Line((0.6349999931, 19.05), (-0.635, 19.05))
            make_face()
        # Symmetric extrude, each_side=0.7112
        extrude(amount=0.7112, both=True, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a shoe sole or footwear component with an elongated, curved anatomical profile featuring a textured upper surface, a ribbed or grooved midsole section, and a contoured heel-to-toe design typical of athletic or casual footwear construction.
def model_30993_b95934d0_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 51.9232555787, perimeter: 28.9601150966
            with BuildLine():
                Line((4.567258537, 2.567258537), (3.5, 1.5))
                CenterArc((0.4971544798, 1.2093539022), 4.2906470413, 18.4501924622, 143.0395585608)
                Line((-3.5715240079, 2.5715240079), (-2.5, 1.5))
                Line((-2.5, 1.5), (-1, -4))
                CenterArc((0.5, -3.375), 1.625, -157.380135052, 134.7602701039)
                Line((3.5, 1.5), (2, -4))
            make_face()
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 6.5077552442, perimeter: 13.3653503206
            with BuildLine():
                Line((1.5910742356, 1.8327278027), (1, 4))
                CenterArc((-0.5, 3.375), 1.625, 22.619864948, 134.7602701039)
                Line((-2, 4), (-2.5977819952, 1.8081326843))
                CenterArc((-0.495898674, 0.5507154628), 2.449287971, 31.5621047562, 117.5486139062)
            make_face()
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a 3D bracket or angle connector with an L-shaped profile, featuring a long flat base section and a perpendicular vertical flange, designed for structural support or mounting applications.
def model_30999_4fe3a732_0001():
    """Model: Base"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 11 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 689.8792958319, perimeter: 113.5371399616
            with BuildLine():
                Line((0, 0), (6.4950389153, 0))
                CenterArc((15.1114877171, -5.0751167521), 10, 30.4982253598, 119.0035492804)
                Line((25, 0), (23.7279365188, 0))
                Line((25, 30), (25, 0))
                Line((0, 30), (25, 30))
                Line((0, 0), (0, 30))
            make_face()
        # OneSide extrude, distance=-2
        extrude(amount=-2)

        # Sketch1 -> Extrude2 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 11 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 25.8702565739, perimeter: 40.2776903918
            with BuildLine():
                Line((8.1690083798, 0), (6.4950389153, 0))
                CenterArc((15.1114877171, -5.0751167521), 8.5996993782, 36.1676877432, 107.6646245136)
                Line((22.0539670544, 0), (23.7279365188, 0))
                CenterArc((15.1114877171, -5.0751167521), 10, 30.4982253598, 119.0035492804)
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2)

        # Sketch2 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(-2, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 34.9166560196, perimeter: 62.327777068
            with BuildLine():
                Line((-23.836111466, 30), (-25, 30))
                Line((-25, 30), (-25, 0))
                Line((-25, 0), (-23.836111466, 0))
                Line((-23.836111466, 0), (-23.836111466, 30))
            make_face()
        # OneSide extrude, distance=80
        extrude(amount=80, mode=Mode.ADD)
    return part.part


# Description: This is a cutting tool or end mill holder featuring an elongated shaft with a tapered or angled cutting head at one end, designed for machining operations with a streamlined profile and what appears to be a mounting flange or connection point.
def model_31008_8fa25b35_0014():
    """Model: 2 v4"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 10 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 9.086609705, perimeter: 37.3464388202
            with BuildLine():
                Line((-9.68, 0.5), (-9.68, 0))
                Line((-9.68, 0), (0, 0))
                Line((0, 0), (0.4627005068, 0.25))
                Line((0.4627005068, 0.25), (8.43, 0.25))
                Line((8.43, 0.25), (8.43, 0.75))
                Line((8.43, 0.75), (0.3362616866, 0.75))
                Line((0.3362616866, 0.75), (-0.1264388202, 0.5))
                Line((-0.1264388202, 0.5), (-9.68, 0.5))
            make_face()
        # OneSide extrude, distance=6
        extrude(amount=6)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 18 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.25, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 1.7671458676, perimeter: 4.7123889804
            with Locations((7.03, 1.22)):
                Circle(0.75)
            # Profile area: 167.3454192437, perimeter: 80.2763918402
            with BuildLine():
                CenterArc((3.8709669813, 1.1678843624), 3.6379332809, 95.0722043498, 64.4599993278)
                Line((5.9203360593, 5.0021397061), (3.5493333659, 4.7915717625))
                CenterArc((5.9647993532, 4.5041206142), 0.5000000004, 0, 95.1018574856)
                CenterArc((8.5589955122, 4.3472571433), 2.1000627846, 175.7163217312, 69.540160657)
                CenterArc((7.68, 1.69), 0.75, -0.0000166651, 90.0000504621)
                Line((8.43, 1.6899997819), (8.43, 0.75))
                CenterArc((7.68, 0.75), 0.75, -90, 90)
                Line((13.5462506957, -4.1897890727), (7.68, 0))
                Line((11.6208077119, 9.1184197859), (13.5462506957, -4.1897890727))
                Line((-8.9927583498, 8.6936897159), (11.6208077119, 9.1184197859))
                Line((-16, 2.44), (-8.9927583498, 8.6936897159))
                Line((0.4627005068, 2.44), (-16, 2.44))
            make_face()
        # Symmetric extrude, each_side=1
        extrude(amount=1, both=True, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a polygonal wedge or beveled block with a trapezoidal profile, featuring multiple internal triangulated faces and a dark shadowed base surface, designed as a geometric solid component with faceted surfaces.
def model_31011_7f51c882_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> 押し出し3 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1720477401, perimeter: 2.0388417686
            with BuildLine():
                Line((0, 0), (0, -0.6881909602))
                Line((0, 0), (-0.5, -0.6881909602))
                Line((-0.5, -0.6881909602), (0, -0.6881909602))
            make_face()
            # Profile area: 0.1720477401, perimeter: 2.0388417686
            with BuildLine():
                Line((0, 0), (0.5, -0.6881909602))
                Line((0, 0), (0, -0.6881909602))
                Line((0, -0.6881909602), (0.5, -0.6881909602))
            make_face()
            # Profile area: 1.3763819205, perimeter: 5.7013016167
            with BuildLine():
                Line((0.5, -0.6881909602), (0.8090169944, 0.2628655561))
                Line((0.8090169944, 0.2628655561), (0, 0.8506508084))
                Line((0, 0.8506508084), (-0.8090169944, 0.2628655561))
                Line((-0.8090169944, 0.2628655561), (-0.5, -0.6881909602))
                Line((0, 0), (-0.5, -0.6881909602))
                Line((0, 0), (0.5, -0.6881909602))
            make_face()
        # OneSide extrude, distance=0.25
        extrude(amount=0.25)

        # Sketch2 -> 押し出し4 (Cut)
        # Sketch on YZ construction plane
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.383155948, perimeter: 3.1107243191
            with BuildLine():
                Line((0, 1.1135163644), (-0.6881909602, 1.1135163644))
                Line((-0.6881909602, 1.1135163644), (-0.6881909602, 0))
                Line((0, 1.1135163644), (-0.6881909602, 0))
            make_face()
        # Symmetric extrude, each_side=1
        extrude(amount=1, both=True, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a curved elbow or arm rest component with an organic, flowing shape that features a tapered design, smooth contours, and appears to have textured or ribbed surface details along its length.
def model_31013_d34d1b29_0007():
    """Model: Siodelko"""
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
            # Profile area: 210.3377273156, perimeter: 77.8378808867
            with BuildLine():
                _nurbs_edge([(12.4613683168, 72.2634806587), (12.4529500474, 72.3289319131), (12.4215092009, 72.4602491627), (12.330529036, 72.6585048352), (12.1214777196, 72.9250999427), (11.716250531, 73.2454970931), (11.1768051389, 73.4966521444), (10.517621355, 73.6019786655), (9.7536371829, 73.4943301136), (8.8958620808, 73.147125063), (7.9491779853, 72.5898309678), (6.9152111702, 71.887824933), (5.7941141472, 71.1301784017), (4.5867385627, 70.4147434582), (3.2967764022, 69.8339636053), (1.9326802764, 69.461644094), (0.510403399, 69.335978616), (-0.9469966539, 69.4574205092), (-2.4123305755, 69.7987190295), (-3.856455859, 70.3111988434), (-5.2507938941, 70.9323995848), (-6.5696218381, 71.5928689792), (-7.7926762667, 72.2234510043), (-8.9072308655, 72.7617970129), (-9.9115939893, 73.1606093189), (-10.8124297097, 73.3882993114), (-11.6191506711, 73.425852079), (-12.3389770324, 73.2650343068), (-12.8866177523, 72.954715143), (-13.2528915888, 72.610651868), (-13.4774965639, 72.3208339824), (-13.5942863357, 72.1402341963), (-13.6221137735, 72.0952377543)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0333333333, 0.0666666667, 0.1, 0.1333333333, 0.1666666667, 0.2, 0.2333333333, 0.2666666667, 0.3, 0.3333333333, 0.3666666667, 0.4, 0.4333333333, 0.4666666667, 0.5, 0.5333333333, 0.5666666667, 0.6, 0.6333333333, 0.6666666667, 0.7, 0.7333333333, 0.7666666667, 0.8, 0.8333333333, 0.8666666667, 0.9, 0.9107616824, 0.9107616824, 0.9107616824, 0.9107616824, 0.9107616824, 0.9107616824], 5)
                _nurbs_edge([(-20.7330100798, 70.5510390266), (-20.749048956, 70.6503489843), (-20.7679391829, 70.8423643952), (-20.7567122642, 71.110574145), (-20.662040463, 71.4282710544), (-20.4096211143, 71.7577183455), (-20.0254830068, 72.0190898193), (-19.5194380611, 72.2140946188), (-18.9129876051, 72.3481000299), (-18.2352200471, 72.428795935), (-17.5191802816, 72.4650864732), (-16.7985318794, 72.4661386533), (-16.1041894784, 72.4405260827), (-15.4612539578, 72.3955044019), (-14.8848477995, 72.3361733072), (-14.3820709582, 72.2657168726), (-14.0404909933, 72.2018508523), (-13.818211331, 72.1500502298), (-13.6849861247, 72.1137954328), (-13.622113773, 72.095237756)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0666666667, 0.1333333333, 0.2, 0.2666666667, 0.3333333333, 0.4, 0.4666666667, 0.5333333333, 0.6, 0.6666666667, 0.7333333333, 0.8, 0.8666666667, 0.9333333333, 0.9999999999, 0.9999999999, 0.9999999999, 0.9999999999, 0.9999999999, 0.9999999999], 5)
                Line((-14.2789570106, 67.8089902066), (-20.7330100798, 70.5510390266))
                Line((-14.2607882781, 67.8103489592), (-14.2789570106, 67.8089902066))
                _nurbs_edge([(-14.2607882781, 67.8103489592), (-13.9828139774, 67.6589727792), (-13.4272901221, 67.3593079839), (-12.5952797426, 66.9190730648), (-11.4884837631, 66.3506968893), (-10.1071573152, 65.6730860214), (-8.7214271493, 65.0331979184), (-7.3183185562, 64.4400837152), (-5.8752203753, 63.9086098849), (-4.3602974547, 63.4598265689), (-2.818243575, 63.1338600093), (-1.5120272646, 62.9696407144), (-0.5045286524, 62.9073881416), (0.1561996527, 62.8930952063), (0.4459178001, 62.8918028454)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.4883310475, 0.4883310475, 0.4883310475, 0.4883310475, 0.4883310475, 0.4883310475], 5)
                Line((0.4459178001, 62.8918028454), (0.5508954708, 62.891592794))
                _nurbs_edge([(0.5508954708, 62.891592794), (0.6183279509, 62.8916235272), (1.065842431, 62.8935866157), (1.9057945053, 62.9188718148), (3.1594670683, 63.0161544045), (4.8311591479, 63.2647786948), (6.7833494589, 63.7491408837), (8.5926217599, 64.421273186), (10.1662035827, 65.2794069288), (11.4233904971, 66.3200358251), (12.3101803095, 67.5387588665), (12.8002704526, 68.9310555474), (12.8673769064, 70.1806322127), (12.7351036236, 71.1929543629), (12.566085707, 71.9010953017), (12.4613683168, 72.2634806587)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0.4911047298, 0.4911047298, 0.4911047298, 0.4911047298, 0.4911047298, 0.4911047298, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1, 1, 1, 1, 1, 1], 5)
            make_face()
        # OneSide extrude, distance=-13
        extrude(amount=-13)

        # Sketch2 -> Extrude4 (Intersect)
        # Sketch on BRepFace
        # Sketch has 12 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 62.892443289, -0.1258424294), x_dir=(1, 0, 0), z_dir=(0, -0.9999979982, 0.0020009109))):
            # Profile area: 48.545755791, perimeter: 36.3734555048
            with BuildLine():
                Line((-3.9687513358, 6.9455571023), (-3.9687513358, 14.0474549463))
                Line((-6.5, 6.9455571023), (-3.9687513358, 6.9455571023))
                Line((-6.5, 6.9455571023), (-6.5, -0.3200760114))
                Line((-3.0479821651, -0.3200760114), (-6.5, -0.3200760114))
                _nurbs_edge([(-3.9687513358, 14.0474549463), (-3.7919177558, 13.9969760127), (-3.3315289019, 13.8445133796), (-2.6619280592, 13.5263270538), (-1.9162682577, 12.9292190221), (-1.2811514029, 11.9001821264), (-0.9541606379, 10.4913526547), (-0.9520773334, 8.8587952535), (-1.2074705075, 7.1046101599), (-1.6322542992, 5.3550825729), (-2.1291786393, 3.7352171484), (-2.6012568781, 2.3479181902), (-2.9622518078, 1.248545953), (-3.1141207645, 0.5698405461), (-3.1258671623, 0.1361205995), (-3.0861092354, -0.1496459293), (-3.0520427356, -0.3025801989), (-3.0479821651, -0.3200760114)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0.0565737654, 0.0565737654, 0.0565737654, 0.0565737654, 0.0565737654, 0.0565737654, 0.08, 0.12, 0.16, 0.2, 0.24, 0.28, 0.32, 0.36, 0.4, 0.44, 0.48, 0.52, 0.5251591095, 0.5251591095, 0.5251591095, 0.5251591095, 0.5251591095, 0.5251591095], 5)
            make_face()
            # Profile area: 0.3637450938, perimeter: 7.143986676
            with BuildLine():
                _nurbs_edge([(-9.9520178349, -0.3200760114), (-9.9568699672, -0.3409824325), (-9.9619630018, -0.3619233395), (-9.9672956818, -0.3829088793), (-9.9728666004, -0.4039490995), (-9.9786741995, -0.4250538923)], [1, 1, 1, 1, 1, 1], [0.5251591095, 0.5251591095, 0.5251591095, 0.5251591095, 0.5251591095, 0.5251591095, 0.5313239283, 0.5313239283, 0.5313239283, 0.5313239283, 0.5313239283, 0.5313239283], 5)
                Line((-9.9786741995, -0.4250538923), (-6.5, -0.4250538923))
                Line((-6.5, -0.3200760114), (-6.5, -0.4250538923))
                Line((-6.5, -0.3200760114), (-9.9520178349, -0.3200760114))
            make_face()
            # Profile area: 56.9584726193, perimeter: 31.1309914125
            with BuildLine():
                Line((-6.5, -0.4250538923), (-6.5, -12.047069019))
                Line((-9.9786741995, -0.4250538923), (-6.5, -0.4250538923))
                _nurbs_edge([(-9.9786741995, -0.4250538923), (-10.0056886395, -0.5232242628), (-10.0826497052, -0.7616776715), (-10.2494926305, -1.160734073), (-10.5645811741, -1.7971119908), (-11.0633919475, -2.8207326955), (-11.6151042427, -4.1328271573), (-12.0873886364, -5.5952597667), (-12.376511171, -7.0970811829), (-12.3881878726, -8.5197972218), (-12.0504527845, -9.7656221509), (-11.3200772628, -10.7743164377), (-10.1737392508, -11.5110725027), (-8.9168445412, -11.8707557359), (-7.7826907782, -12.0096624294), (-6.9417101004, -12.04426706), (-6.5, -12.047069019)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0.5313239283, 0.5313239283, 0.5313239283, 0.5313239283, 0.5313239283, 0.5313239283, 0.56, 0.6, 0.64, 0.68, 0.72, 0.76, 0.8, 0.84, 0.88, 0.92, 0.96, 1, 1, 1, 1, 1, 1], 5)
            make_face()
            # Profile area: 48.545755791, perimeter: 36.3734555048
            with BuildLine():
                Line((-6.5, -0.3200760114), (-9.9520178349, -0.3200760114))
                Line((-6.5, 6.9455571023), (-6.5, -0.3200760114))
                Line((-9.0312486642, 6.9455571023), (-6.5, 6.9455571023))
                Line((-9.0312486642, 14.0474549463), (-9.0312486642, 6.9455571023))
                _nurbs_edge([(-9.0312486642, 14.0474549463), (-9.2080822442, 13.9969760127), (-9.6684710981, 13.8445133796), (-10.3380719408, 13.5263270538), (-11.0837317423, 12.9292190221), (-11.7188485971, 11.9001821264), (-12.0458393621, 10.4913526547), (-12.0479226665, 8.8587952535), (-11.7925294925, 7.1046101599), (-11.3677457008, 5.3550825729), (-10.8708213607, 3.7352171484), (-10.3987431219, 2.3479181902), (-10.0377481922, 1.248545953), (-9.8858792355, 0.5698405461), (-9.8741328377, 0.1361205995), (-9.9138907646, -0.1496459293), (-9.9479572644, -0.3025801989), (-9.9520178349, -0.3200760114)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0.0565737654, 0.0565737654, 0.0565737654, 0.0565737654, 0.0565737654, 0.0565737654, 0.08, 0.12, 0.16, 0.2, 0.24, 0.28, 0.32, 0.36, 0.4, 0.44, 0.48, 0.52, 0.5251591095, 0.5251591095, 0.5251591095, 0.5251591095, 0.5251591095, 0.5251591095], 5)
            make_face()
            # Profile area: 0.3637450938, perimeter: 7.143986676
            with BuildLine():
                Line((-3.0479821651, -0.3200760114), (-6.5, -0.3200760114))
                Line((-6.5, -0.3200760114), (-6.5, -0.4250538923))
                Line((-6.5, -0.4250538923), (-3.0213258005, -0.4250538923))
                _nurbs_edge([(-3.0479821651, -0.3200760114), (-3.0431300328, -0.3409824325), (-3.0380369982, -0.3619233395), (-3.0327043182, -0.3829088793), (-3.0271333996, -0.4039490995), (-3.0213258005, -0.4250538923)], [1, 1, 1, 1, 1, 1], [0.5251591095, 0.5251591095, 0.5251591095, 0.5251591095, 0.5251591095, 0.5251591095, 0.5313239283, 0.5313239283, 0.5313239283, 0.5313239283, 0.5313239283, 0.5313239283], 5)
            make_face()
            # Profile area: 37.6697674525, perimeter: 25.4507751116
            with BuildLine():
                _nurbs_edge([(-6.5, 14.3160542813), (-6.9138985208, 14.3263042051), (-7.4713327645, 14.3166919165), (-7.9892213339, 14.2729815782), (-8.4674900973, 14.1951082183), (-8.906141138, 14.0831681548), (-9.0312486642, 14.0474549463)], [1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.04, 0.0565737654, 0.0565737654, 0.0565737654, 0.0565737654, 0.0565737654, 0.0565737654], 5)
                _nurbs_edge([(-6.5, 14.3160542813), (-6.0861014792, 14.3263042051), (-5.5286672355, 14.3166919165), (-5.0107786661, 14.2729815782), (-4.5325099027, 14.1951082183), (-4.093858862, 14.0831681548), (-3.9687513358, 14.0474549463)], [1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.04, 0.0565737654, 0.0565737654, 0.0565737654, 0.0565737654, 0.0565737654, 0.0565737654], 5)
                Line((-3.9687513358, 14.0474549463), (-3.9687513358, 21.6865514602))
                Line((-3.9687513358, 21.6865514602), (-9.0312486642, 21.6865514602))
                Line((-9.0312486642, 21.6865514602), (-9.0312486642, 14.0474549463))
            make_face()
            # Profile area: 56.9584726193, perimeter: 31.1309914125
            with BuildLine():
                Line((-6.5, -0.4250538923), (-3.0213258005, -0.4250538923))
                Line((-6.5, -0.4250538923), (-6.5, -12.047069019))
                _nurbs_edge([(-3.0213258005, -0.4250538923), (-2.9943113605, -0.5232242628), (-2.9173502948, -0.7616776715), (-2.7505073695, -1.160734073), (-2.4354188259, -1.7971119908), (-1.9366080525, -2.8207326955), (-1.3848957573, -4.1328271573), (-0.9126113636, -5.5952597667), (-0.623488829, -7.0970811829), (-0.6118121274, -8.5197972218), (-0.9495472155, -9.7656221509), (-1.6799227372, -10.7743164377), (-2.8262607492, -11.5110725027), (-4.0831554588, -11.8707557359), (-5.2173092218, -12.0096624294), (-6.0582898996, -12.04426706), (-6.5, -12.047069019)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0.5313239283, 0.5313239283, 0.5313239283, 0.5313239283, 0.5313239283, 0.5313239283, 0.56, 0.6, 0.64, 0.68, 0.72, 0.76, 0.8, 0.84, 0.88, 0.92, 0.96, 1, 1, 1, 1, 1, 1], 5)
            make_face()
            # Profile area: 18.478238551, perimeter: 19.5586860648
            with BuildLine():
                _nurbs_edge([(-6.5, 14.3160542813), (-6.0861014792, 14.3263042051), (-5.5286672355, 14.3166919165), (-5.0107786661, 14.2729815782), (-4.5325099027, 14.1951082183), (-4.093858862, 14.0831681548), (-3.9687513358, 14.0474549463)], [1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.04, 0.0565737654, 0.0565737654, 0.0565737654, 0.0565737654, 0.0565737654, 0.0565737654], 5)
                Line((-6.5, 14.3160542813), (-6.5, 6.9455571023))
                Line((-6.5, 6.9455571023), (-3.9687513358, 6.9455571023))
                Line((-3.9687513358, 6.9455571023), (-3.9687513358, 14.0474549463))
            make_face()
            # Profile area: 18.478238551, perimeter: 19.5586860648
            with BuildLine():
                Line((-9.0312486642, 14.0474549463), (-9.0312486642, 6.9455571023))
                Line((-9.0312486642, 6.9455571023), (-6.5, 6.9455571023))
                Line((-6.5, 14.3160542813), (-6.5, 6.9455571023))
                _nurbs_edge([(-6.5, 14.3160542813), (-6.9138985208, 14.3263042051), (-7.4713327645, 14.3166919165), (-7.9892213339, 14.2729815782), (-8.4674900973, 14.1951082183), (-8.906141138, 14.0831681548), (-9.0312486642, 14.0474549463)], [1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.04, 0.0565737654, 0.0565737654, 0.0565737654, 0.0565737654, 0.0565737654, 0.0565737654], 5)
            make_face()
        # OneSide extrude, distance=-13
        extrude(amount=-13, mode=Mode.INTERSECT)

        # Sketch2 -> Extrude3 (Intersect)
        # Sketch on BRepFace
        # Sketch has 12 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 62.892443289, -0.1258424294), x_dir=(1, 0, 0), z_dir=(0, -0.9999979982, 0.0020009109))):
            # Profile area: 48.545755791, perimeter: 36.3734555048
            with BuildLine():
                Line((-3.9687513358, 6.9455571023), (-3.9687513358, 14.0474549463))
                Line((-6.5, 6.9455571023), (-3.9687513358, 6.9455571023))
                Line((-6.5, 6.9455571023), (-6.5, -0.3200760114))
                Line((-3.0479821651, -0.3200760114), (-6.5, -0.3200760114))
                _nurbs_edge([(-3.9687513358, 14.0474549463), (-3.7919177558, 13.9969760127), (-3.3315289019, 13.8445133796), (-2.6619280592, 13.5263270538), (-1.9162682577, 12.9292190221), (-1.2811514029, 11.9001821264), (-0.9541606379, 10.4913526547), (-0.9520773334, 8.8587952535), (-1.2074705075, 7.1046101599), (-1.6322542992, 5.3550825729), (-2.1291786393, 3.7352171484), (-2.6012568781, 2.3479181902), (-2.9622518078, 1.248545953), (-3.1141207645, 0.5698405461), (-3.1258671623, 0.1361205995), (-3.0861092354, -0.1496459293), (-3.0520427356, -0.3025801989), (-3.0479821651, -0.3200760114)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0.0565737654, 0.0565737654, 0.0565737654, 0.0565737654, 0.0565737654, 0.0565737654, 0.08, 0.12, 0.16, 0.2, 0.24, 0.28, 0.32, 0.36, 0.4, 0.44, 0.48, 0.52, 0.5251591095, 0.5251591095, 0.5251591095, 0.5251591095, 0.5251591095, 0.5251591095], 5)
            make_face()
            # Profile area: 0.3637450938, perimeter: 7.143986676
            with BuildLine():
                _nurbs_edge([(-9.9520178349, -0.3200760114), (-9.9568699672, -0.3409824325), (-9.9619630018, -0.3619233395), (-9.9672956818, -0.3829088793), (-9.9728666004, -0.4039490995), (-9.9786741995, -0.4250538923)], [1, 1, 1, 1, 1, 1], [0.5251591095, 0.5251591095, 0.5251591095, 0.5251591095, 0.5251591095, 0.5251591095, 0.5313239283, 0.5313239283, 0.5313239283, 0.5313239283, 0.5313239283, 0.5313239283], 5)
                Line((-9.9786741995, -0.4250538923), (-6.5, -0.4250538923))
                Line((-6.5, -0.3200760114), (-6.5, -0.4250538923))
                Line((-6.5, -0.3200760114), (-9.9520178349, -0.3200760114))
            make_face()
            # Profile area: 56.9584726193, perimeter: 31.1309914125
            with BuildLine():
                Line((-6.5, -0.4250538923), (-6.5, -12.047069019))
                Line((-9.9786741995, -0.4250538923), (-6.5, -0.4250538923))
                _nurbs_edge([(-9.9786741995, -0.4250538923), (-10.0056886395, -0.5232242628), (-10.0826497052, -0.7616776715), (-10.2494926305, -1.160734073), (-10.5645811741, -1.7971119908), (-11.0633919475, -2.8207326955), (-11.6151042427, -4.1328271573), (-12.0873886364, -5.5952597667), (-12.376511171, -7.0970811829), (-12.3881878726, -8.5197972218), (-12.0504527845, -9.7656221509), (-11.3200772628, -10.7743164377), (-10.1737392508, -11.5110725027), (-8.9168445412, -11.8707557359), (-7.7826907782, -12.0096624294), (-6.9417101004, -12.04426706), (-6.5, -12.047069019)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0.5313239283, 0.5313239283, 0.5313239283, 0.5313239283, 0.5313239283, 0.5313239283, 0.56, 0.6, 0.64, 0.68, 0.72, 0.76, 0.8, 0.84, 0.88, 0.92, 0.96, 1, 1, 1, 1, 1, 1], 5)
            make_face()
            # Profile area: 48.545755791, perimeter: 36.3734555048
            with BuildLine():
                Line((-6.5, -0.3200760114), (-9.9520178349, -0.3200760114))
                Line((-6.5, 6.9455571023), (-6.5, -0.3200760114))
                Line((-9.0312486642, 6.9455571023), (-6.5, 6.9455571023))
                Line((-9.0312486642, 14.0474549463), (-9.0312486642, 6.9455571023))
                _nurbs_edge([(-9.0312486642, 14.0474549463), (-9.2080822442, 13.9969760127), (-9.6684710981, 13.8445133796), (-10.3380719408, 13.5263270538), (-11.0837317423, 12.9292190221), (-11.7188485971, 11.9001821264), (-12.0458393621, 10.4913526547), (-12.0479226665, 8.8587952535), (-11.7925294925, 7.1046101599), (-11.3677457008, 5.3550825729), (-10.8708213607, 3.7352171484), (-10.3987431219, 2.3479181902), (-10.0377481922, 1.248545953), (-9.8858792355, 0.5698405461), (-9.8741328377, 0.1361205995), (-9.9138907646, -0.1496459293), (-9.9479572644, -0.3025801989), (-9.9520178349, -0.3200760114)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0.0565737654, 0.0565737654, 0.0565737654, 0.0565737654, 0.0565737654, 0.0565737654, 0.08, 0.12, 0.16, 0.2, 0.24, 0.28, 0.32, 0.36, 0.4, 0.44, 0.48, 0.52, 0.5251591095, 0.5251591095, 0.5251591095, 0.5251591095, 0.5251591095, 0.5251591095], 5)
            make_face()
            # Profile area: 0.3637450938, perimeter: 7.143986676
            with BuildLine():
                Line((-3.0479821651, -0.3200760114), (-6.5, -0.3200760114))
                Line((-6.5, -0.3200760114), (-6.5, -0.4250538923))
                Line((-6.5, -0.4250538923), (-3.0213258005, -0.4250538923))
                _nurbs_edge([(-3.0479821651, -0.3200760114), (-3.0431300328, -0.3409824325), (-3.0380369982, -0.3619233395), (-3.0327043182, -0.3829088793), (-3.0271333996, -0.4039490995), (-3.0213258005, -0.4250538923)], [1, 1, 1, 1, 1, 1], [0.5251591095, 0.5251591095, 0.5251591095, 0.5251591095, 0.5251591095, 0.5251591095, 0.5313239283, 0.5313239283, 0.5313239283, 0.5313239283, 0.5313239283, 0.5313239283], 5)
            make_face()
            # Profile area: 37.6697674525, perimeter: 25.4507751116
            with BuildLine():
                _nurbs_edge([(-6.5, 14.3160542813), (-6.9138985208, 14.3263042051), (-7.4713327645, 14.3166919165), (-7.9892213339, 14.2729815782), (-8.4674900973, 14.1951082183), (-8.906141138, 14.0831681548), (-9.0312486642, 14.0474549463)], [1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.04, 0.0565737654, 0.0565737654, 0.0565737654, 0.0565737654, 0.0565737654, 0.0565737654], 5)
                _nurbs_edge([(-6.5, 14.3160542813), (-6.0861014792, 14.3263042051), (-5.5286672355, 14.3166919165), (-5.0107786661, 14.2729815782), (-4.5325099027, 14.1951082183), (-4.093858862, 14.0831681548), (-3.9687513358, 14.0474549463)], [1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.04, 0.0565737654, 0.0565737654, 0.0565737654, 0.0565737654, 0.0565737654, 0.0565737654], 5)
                Line((-3.9687513358, 14.0474549463), (-3.9687513358, 21.6865514602))
                Line((-3.9687513358, 21.6865514602), (-9.0312486642, 21.6865514602))
                Line((-9.0312486642, 21.6865514602), (-9.0312486642, 14.0474549463))
            make_face()
            # Profile area: 56.9584726193, perimeter: 31.1309914125
            with BuildLine():
                Line((-6.5, -0.4250538923), (-3.0213258005, -0.4250538923))
                Line((-6.5, -0.4250538923), (-6.5, -12.047069019))
                _nurbs_edge([(-3.0213258005, -0.4250538923), (-2.9943113605, -0.5232242628), (-2.9173502948, -0.7616776715), (-2.7505073695, -1.160734073), (-2.4354188259, -1.7971119908), (-1.9366080525, -2.8207326955), (-1.3848957573, -4.1328271573), (-0.9126113636, -5.5952597667), (-0.623488829, -7.0970811829), (-0.6118121274, -8.5197972218), (-0.9495472155, -9.7656221509), (-1.6799227372, -10.7743164377), (-2.8262607492, -11.5110725027), (-4.0831554588, -11.8707557359), (-5.2173092218, -12.0096624294), (-6.0582898996, -12.04426706), (-6.5, -12.047069019)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0.5313239283, 0.5313239283, 0.5313239283, 0.5313239283, 0.5313239283, 0.5313239283, 0.56, 0.6, 0.64, 0.68, 0.72, 0.76, 0.8, 0.84, 0.88, 0.92, 0.96, 1, 1, 1, 1, 1, 1], 5)
            make_face()
            # Profile area: 18.478238551, perimeter: 19.5586860648
            with BuildLine():
                _nurbs_edge([(-6.5, 14.3160542813), (-6.0861014792, 14.3263042051), (-5.5286672355, 14.3166919165), (-5.0107786661, 14.2729815782), (-4.5325099027, 14.1951082183), (-4.093858862, 14.0831681548), (-3.9687513358, 14.0474549463)], [1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.04, 0.0565737654, 0.0565737654, 0.0565737654, 0.0565737654, 0.0565737654, 0.0565737654], 5)
                Line((-6.5, 14.3160542813), (-6.5, 6.9455571023))
                Line((-6.5, 6.9455571023), (-3.9687513358, 6.9455571023))
                Line((-3.9687513358, 6.9455571023), (-3.9687513358, 14.0474549463))
            make_face()
            # Profile area: 18.478238551, perimeter: 19.5586860648
            with BuildLine():
                Line((-9.0312486642, 14.0474549463), (-9.0312486642, 6.9455571023))
                Line((-9.0312486642, 6.9455571023), (-6.5, 6.9455571023))
                Line((-6.5, 14.3160542813), (-6.5, 6.9455571023))
                _nurbs_edge([(-6.5, 14.3160542813), (-6.9138985208, 14.3263042051), (-7.4713327645, 14.3166919165), (-7.9892213339, 14.2729815782), (-8.4674900973, 14.1951082183), (-8.906141138, 14.0831681548), (-9.0312486642, 14.0474549463)], [1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.04, 0.0565737654, 0.0565737654, 0.0565737654, 0.0565737654, 0.0565737654, 0.0565737654], 5)
            make_face()
        # OneSide extrude, distance=-13
        extrude(amount=-13, mode=Mode.INTERSECT)
    return part.part


# Description: This is a cylindrical rod or shaft with a slightly tapered or pointed end, featuring a simple linear geometry with a smooth surface and minimal features.
def model_31108_e89804a2_0001():
    """Model: Part 13"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2242173742, perimeter: 5.7971539461
            with BuildLine():
                CenterArc((17.9039062203, 0.0201305002), 0.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((17.9039062203, 0.0201305002), 0.4226457064, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=42
        extrude(amount=42)

        # Sketch3 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.2242173742, perimeter: 5.7971539461
            with BuildLine():
                CenterArc((17.9039062203, -0.0201305002), 0.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((17.9039062203, -0.0201305002), 0.4226457064, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.596934039, perimeter: 7.8445047615
            with BuildLine():
                Line((17.8074041194, -0.8416179688), (17.0741667092, 0.0748369544))
                Line((18.7270560787, -0.1058226734), (17.8074041194, -0.8416179688))
                Line((17.9938186685, 0.8106322498), (18.7270560787, -0.1058226734))
                Line((17.0741667092, 0.0748369544), (17.9938186685, 0.8106322498))
            make_face()
            with BuildLine():
                CenterArc((17.9039062203, -0.0201305002), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.4
        extrude(amount=0.4, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical sleeve or spacer with a rounded end cap, featuring a smooth tubular body and a domed hemispherical end on one side.
def model_31136_987852a4_0006():
    """Model: Component15"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((-18.9000002816, 2.9000000432)):
                Circle(0.25)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.1256637061, perimeter: 2.5132741229
            with BuildLine():
                CenterArc((18.9000002816, 2.9000000432), 0.25, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((18.9000002816, 2.9000000432), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.5
        extrude(amount=1.5, mode=Mode.ADD)
    return part.part


# Description: This is an oval or elliptical cylindrical basket or container with a mesh or perforated textured surface, featuring curved sides and an open top design, commonly used for drainage, filtering, or storage applications.
def model_31277_b1263495_0001():
    """Model: BALL BEARING"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.3432154105, perimeter: 15.3049597623
            with BuildLine():
                CenterArc((0, 0), 1.43637, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.99949, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.39954
        extrude(amount=1.39954)

        # Sketch1 -> Extrude2 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 5.8497554315, perimeter: 26.7796897614
            with BuildLine():
                CenterArc((0, 0), 2.3495, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.91262, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.397
        extrude(amount=1.397)
    return part.part


# Description: This is a ring or collar-shaped component with an oval/elliptical cross-section featuring a central band, curved outer walls, and internal ribbed or fluted details along the top surface.
def model_31277_b1263495_0003():
    """Model: AXLE"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 6.333458391, perimeter: 8.9212434903
            Circle(1.41986)
        # OneSide extrude, distance=0.47752
        extrude(amount=0.47752)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.47752, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.8794791368, perimeter: 6.9821896726
            Circle(1.11125)
        # OneSide extrude, distance=0.35814
        extrude(amount=0.35814, mode=Mode.ADD)
    return part.part


# Description: This is a rectangular boat or utility bin with sloped side walls, an open top, internal cross-bracing ribs for structural reinforcement, and flanged edges along the perimeter for mounting or stacking.
def model_31280_c8bd4b11_0001():
    """Model: Stand"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 30 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 47.6397346431, perimeter: 27.3982298432
            with BuildLine():
                Line((1.45, 3.8), (1.45, 4.2000000641))
                CenterArc((1.35, 4.2000000641), 0.1, 0, 90)
                Line((1.35, 4.3000000641), (-1.35, 4.3000000641))
                CenterArc((-1.35, 4.2000000641), 0.1, 90, 90)
                Line((-1.45, 3.8), (-1.45, 4.2000000641))
                CenterArc((-1.75, 3.8), 0.3, -90, 90)
                Line((-1.75, 3.5), (-2.75, 3.5))
                CenterArc((-2.75, 3), 0.5, 90, 90)
                Line((-3.25, 3), (-3.25, -3))
                CenterArc((-2.75, -3), 0.5, 180, 90)
                Line((-2.75, -3.5), (2.75, -3.5))
                CenterArc((2.75, -3), 0.5, -90, 90)
                Line((3.25, -3), (3.25, 3))
                CenterArc((2.75, 3), 0.5, 0, 90)
                Line((2.75, 3.5), (1.75, 3.5))
                CenterArc((1.75, 3.8), 0.3, 180, 90)
            make_face()
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 26 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 31.7045330462, perimeter: 22.0350916298
            with BuildLine():
                Line((1, -2.5687670047), (2.5187670047, -2.5687670047))
                CenterArc((2.5187670047, -2.2687670047), 0.3, -90, 90)
                Line((2.8187670047, -2.2687670047), (2.8187670047, 2.7687670047))
                CenterArc((2.5187670047, 2.7687670047), 0.3, 0, 90)
                Line((2.5187670047, 3.0687670047), (-2.5187670047, 3.0687670047))
                CenterArc((-2.5187670047, 2.7687670047), 0.3, 90, 90)
                Line((-2.8187670047, 2.7687670047), (-2.8187670047, -2.2687670047))
                CenterArc((-2.5187670047, -2.2687670047), 0.3, 180, 90)
                Line((-2.5187670047, -2.5687670047), (-1, -2.5687670047))
                Line((-1, -2.5687670047), (1, -2.5687670047))
            make_face()
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.SUBTRACT)
    return part.part


# Description: This is an elliptical composite structure featuring a dark outer rim or frame with an internal framework of parallel ribs or stringers supporting a lighter central panel, resembling an aerospace fuselage section or boat hull component.
def model_31280_c8bd4b11_0008():
    """Model: Magnifier"""
    with BuildPart() as part:
        # Sketch5 -> Extrude4 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.7960174617, perimeter: 55.9203492339
            with BuildLine():
                CenterArc((8.5, 0), 4.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((8.5, 0), 4.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=0.6
        extrude(amount=0.6, both=True)

        # Sketch5 -> Extrude5 (Join)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 60.8212337735, perimeter: 27.6460153516
            with Locations((8.5, 0)):
                Circle(4.4)
        # Symmetric extrude, each_side=0.25
        extrude(amount=0.25, both=True, mode=Mode.ADD)
    return part.part


# Description: A long, slender tweezers tool with a tapered cylindrical shaft, a rounded dome-shaped head at the top with textured gripping surface, and a pointed tip at the bottom, designed for precision picking and manipulation tasks.
def model_31360_a1accb4b_0006():
    """Model: 7-Connecting Rod V"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 9 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.1482416746, perimeter: 7.5690882185
            with BuildLine():
                CenterArc((-0.005683641, 2.8), 0.25, -2.4423894868, 185.1173848255)
                Line((-0.2554112254, 2.7883323707), (-0.1248637922, -0.0058338146))
                CenterArc((0, 0), 0.125, -177.3250046612, 174.8826151745)
                Line((0.2440892529, 2.7893462927), (0.1248864469, -0.0053268537))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.075, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-0.005683641, 2.8), 0.05, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on YZ construction plane
        # Sketch has 14 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.3605933196, perimeter: 4.3550561562
            with BuildLine():
                Line((-0.1169329514, 2.4972638397), (-0.0634390583, 0.5008750608))
                CenterArc((0, 2.8), 2.3, -91.5805440579, 3.1610881158)
                Line((0.1169329514, 2.4972638397), (0.0634390583, 0.5008750608))
                CenterArc((0, 0), 2.5, 87.3191160435, 5.361767913)
            make_face()
        # OneSide extrude, distance=0.1
        extrude(amount=0.1, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a boat hull or watercraft fuselage with an elongated, streamlined shape featuring a curved bottom surface, radiating internal ribbing or stringers for structural reinforcement, and darkened end caps or bulkheads at both the bow and stern.
def model_31462_84375249_0002():
    """Model: table v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 25 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1676.0347838775, perimeter: 174.3432816347
            with BuildLine():
                Line((20.1210309462, 30), (0, 30))
                Line((0, 30), (0, -30))
                Line((0, -30), (15.0118744946, -30))
                CenterArc((15.0118744946, -15.011834111), 14.988165889, -90, 89.8669955728)
                Line((30, -15.046627086), (30, -14.9770411359))
                Line((30, -14.9770411359), (30, 23.772625223))
                CenterArc((25.4963646663, 27.5777340926), 5.8958955832, 155.74242765, 164.0631990756)
            make_face()
            # Profile area: 1703.5826994168, perimeter: 167.1341289964
            with BuildLine():
                Line((0, 30), (-14.9770411359, 30))
                Line((-14.9770411359, 30), (-15.046627086, 30))
                CenterArc((-15.011834111, 15.0118744946), 14.988165889, 90.1330044272, 89.8669955728)
                Line((-30, 15.0118744946), (-30, -14.9770411359))
                Line((-30, -14.9770411359), (-30, -15.046627086))
                CenterArc((-15.0118744946, -15.011834111), 14.988165889, -179.8669955728, 89.8669955728)
                Line((-15.0118744946, -30), (0, -30))
                Line((0, 30), (0, -30))
            make_face()
        # OneSide extrude, distance=5
        extrude(amount=5)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 19.6349540849, perimeter: 15.7079632679
            with Locations((20.006959031, 20.0139301858)):
                Circle(2.5)
            # Profile area: 19.6349540849, perimeter: 15.7079632679
            with Locations((19.8984227923, -19.9904461618)):
                Circle(2.5)
            # Profile area: 19.6349540849, perimeter: 15.7079632679
            with Locations((-19.9829631271, -19.9567124793)):
                Circle(2.5)
            # Profile area: 19.6349540849, perimeter: 15.7079632679
            with Locations((-20, 20)):
                Circle(2.5)
        # OneSide extrude, distance=-2.5
        extrude(amount=-2.5, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical elbow or 90-degree pipe connector featuring a curved main barrel with a perpendicular tubular extension at the bottom, designed to redirect fluid or air flow at a right angle.
def model_31463_c4c75dd7_0003():
    """Model: plug v4"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.1309733553, perimeter: 3.7699111843
            Circle(0.6)
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XY construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 2.2661551219, perimeter: 5.3364168813
            with Locations((0, 1.5)):
                Circle(0.8493171251)
        # TwoSides extrude (symmetric), distance=1
        extrude(amount=1, both=True, mode=Mode.ADD)
    return part.part


# Description: This is a lathe tool holder or cutting tool insert with an elongated rectangular body, featuring a sloped top surface with multiple parallel grooves or flutes, a mounting flange on the left end, and a smaller right-side extension for tool positioning.
def model_31464_b2855e3a_0006():
    """Model: Track"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 13 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 263.22528, perimeter: 98.1112754014
            with BuildLine():
                Line((30.48, 8.636), (0, 8.636))
                Line((0, 8.636), (0, 5.08))
                Line((0, 5.08), (-0.9335629486, 5.08))
                CenterArc((-2.54, 4.318), 1.778, 25.3769335252, 309.2461329497)
                Line((0, 3.556), (-0.9335629486, 3.556))
                Line((0, 3.556), (0, 0))
                Line((0, 0), (30.48, 0))
                Line((30.48, 0), (30.48, 3.556))
                Line((30.48, 3.556), (29.5464370514, 3.556))
                CenterArc((27.94, 4.318), 1.778, 25.3769335252, 309.2461329497)
                Line((30.48, 5.08), (29.5464370514, 5.08))
                Line((30.48, 5.08), (30.48, 8.636))
            make_face()
        # OneSide extrude, distance=2.54
        extrude(amount=2.54)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 16 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2.54, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 27.09672, perimeter: 62.738
            with BuildLine():
                Line((-30.48, -7.62), (-30.48, -6.731))
                Line((0, -7.62), (-30.48, -7.62))
                Line((0, -6.731), (0, -7.62))
                Line((-30.48, -6.731), (0, -6.731))
            make_face()
            # Profile area: 27.09672, perimeter: 62.738
            with BuildLine():
                Line((0, -1.016), (0, -1.905))
                Line((0, -1.016), (-30.48, -1.016))
                Line((-30.48, -1.905), (-30.48, -1.016))
                Line((-30.48, -1.905), (0, -1.905))
            make_face()
        # OneSide extrude, distance=-0.635
        extrude(amount=-0.635, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a circular disc or wheel with a mesh/perforated section featuring a flat, oval-shaped body with a textured or vented area on one side, likely designed for airflow or weight reduction.
def model_31615_bab70c5e_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 201.0619298297, perimeter: 50.2654824574
            Circle(8)
        # OneSide extrude, distance=3
        extrude(amount=3)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 3), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 3.8013271108, perimeter: 6.9115038379
            with Locations((0, 6)):
                Circle(1.1)
        # OneSide extrude, distance=-3
        extrude(amount=-3, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a polyhedron or truncated geometric solid with an irregular multi-faced structure, featuring a pyramidal top section (shown in lighter blue) and a larger polyhedral base (shown in darker blue), creating an asymmetrical, faceted form.
def model_31627_2cb7b72a_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 3 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.8660254038, perimeter: 3.4641016151
            with BuildLine():
                Line((0.5, -0.2886751346), (0.5, 0.2886751346))
                Line((0.5, 0.2886751346), (0, 0.5773502692))
                Line((0, 0.5773502692), (-0.5, 0.2886751346))
                Line((-0.5, 0.2886751346), (-0.5, -0.2886751346))
                Line((-0.5, -0.2886751346), (0, -0.5773502692))
                Line((0, -0.5773502692), (0.5, -0.2886751346))
            make_face()
        # OneSide extrude, distance=-0.42
        extrude(amount=-0.42)
    return part.part


# Description: This is a curved reinforcement bracket or deflector with a tubular, asymmetrical C-shaped profile that curves upward and features a textured ribbed surface on the upper portion and a flat panel section on the lower side.
def model_31664_1e85c690_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch21 -> Extrude17 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 6 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 179.960538008, perimeter: 72.0018727294
            with BuildLine():
                CenterArc((10.5096153846, 44), 13.5096153846, 92.1618483733, 87.8381516267)
                Line((-3, 30), (-3, 44))
                Line((3, 30), (-3, 30))
                Line((3, 44), (3, 30))
                CenterArc((10.5178571429, 44), 7.5178571429, 93.9498680218, 86.0501319782)
                Line((10, 57.5), (10, 51.5))
            make_face()
        # Symmetric extrude, each_side=3
        extrude(amount=3, both=True)
    return part.part


# Description: This is a bent sheet metal or plastic bracket with two angled arms that form an irregular "Z" or zigzag shape, featuring curved edges, internal reinforcement ribs or webs, and dark edges indicating thickness or material transitions.
def model_31730_e8a4bbd6_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 39 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 101.0545974539, perimeter: 58.1586271248
            with BuildLine():
                CenterArc((0.2856003103, 7), 1, 0, 90)
                Line((-8, 8), (0.2856003103, 8))
                CenterArc((-8, 7), 1, 90, 90)
                Line((-9, 7), (-9, 6))
                CenterArc((-8, 6), 1, 180, 90)
                Line((-8, 5), (-2.65, 5))
                CenterArc((-2.65, 4.35), 0.65, 0, 90)
                Line((-2, 0.65), (-2, 4.35))
                CenterArc((-2.65, 0.65), 0.65, -90, 90)
                Line((-7, 0), (-2.65, 0))
                CenterArc((-7, -1), 1, 90, 90)
                Line((-8, -4), (-8, -1))
                CenterArc((-7, -4), 1, 180, 90)
                Line((2, -5), (-7, -5))
                CenterArc((2, -4), 1, -90, 90)
                Line((3, -1), (3, -4))
                CenterArc((2, -1), 1, 0, 90)
                Line((1.9356003103, 0), (2, 0))
                CenterArc((1.9356003103, 0.65), 0.65, -180, 90)
                Line((1.2856003103, 7), (1.2856003103, 0.65))
            make_face()
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


# Description: This is a spherical or ball-shaped component with a cylindrical stem or shaft protruding from one side, featuring a mesh or lattice pattern on the upper hemisphere and a solid lower half, resembling a buoy, float, or sensor housing.
def model_31744_086479d0_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 22.3618556018, perimeter: 16.7632742958
            Circle(2.6679579666)
        # Symmetric extrude, each_side=1.5
        extrude(amount=1.5, both=True)

        # Sketch6 -> Extrude6 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0295714631, perimeter: 15.5791448832
            with BuildLine():
                Line((0, -1.2000000179), (0.0021123744, -1.2031565578))
                Line((0.0021123744, -1.2031565578), (6.4726757032, 3.1269810472))
                Line((6.4726757032, 3.1269810472), (6.4705633289, 3.1301375871))
                Line((0, -1.2000000179), (6.4705633289, 3.1301375871))
            make_face()
        # OneSide extrude, distance=0.15
        extrude(amount=0.15)
    return part.part


# Description: A horizontal cylindrical connector or adapter with a rounded rectangular body featuring a tapered male connector end on the right side and alignment slots or markings on the main barrel.
def model_31866_a5b1db64_0002():
    """Model: SA-1-108 Motor Valve"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            Circle(0.3)
        # OneSide extrude, distance=3
        extrude(amount=3)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(3, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            Circle(0.2)
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)
    return part.part


# Description: This is an electric motor or rotary actuator featuring a large cylindrical stator housing with radial cooling fins on the outer surface, a central shaft, and a smaller cylindrical rotor section, designed for efficient heat dissipation during operation.
def model_31866_a5b1db64_0008():
    """Model: 4-10-COUPLING SPRING RETAINER"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(3.6171766229, -1.5, -2.4087134383), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 0.4398229715, perimeter: 8.7964594301
            with BuildLine():
                CenterArc((1.5, -3.1500000954), 0.75, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((1.5, -3.1500000954), 0.65, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(3.6171766229, -1.5, -2.4087134383), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 0.4398229715, perimeter: 8.7964594301
            with BuildLine():
                CenterArc((1.5, -3.1500000954), 0.75, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((1.5, -3.1500000954), 0.65, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.225801972, perimeter: 3.6128315516
            with BuildLine():
                CenterArc((1.5, -3.1500000954), 0.35, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((1.5, -3.1500000954), 0.225, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.5096663597, perimeter: 7.2895306462
            with BuildLine():
                CenterArc((1.5, -3.1500000954), 0.65, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((1.5, -3.1500000954), 0.5101648352, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.4328114363, perimeter: 5.4045750541
            with BuildLine():
                CenterArc((1.5, -3.1500000954), 0.5101648352, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((1.5, -3.1500000954), 0.35, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)

        # Sketch1 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(3.6171766229, -1.5, -2.4087134383), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 0.225801972, perimeter: 3.6128315516
            with BuildLine():
                CenterArc((1.5, -3.1500000954), 0.35, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((1.5, -3.1500000954), 0.225, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.9
        extrude(amount=0.9, mode=Mode.ADD)
    return part.part


# Description: A cylindrical capsule or rounded rectangular tube with hemispherical ends, featuring a smooth, seamless surface design with no visible holes, slots, or flanges.
def model_31962_e5291336_0013():
    """Model: din"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((14.900000222, 1.3000000194)):
                Circle(0.2)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch3 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0.5, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0346410162, perimeter: 0.692820323
            with BuildLine():
                Line((14.9577352489, 1.4000000194), (14.8422651951, 1.4000000194))
                Line((14.8422651951, 1.4000000194), (14.7845301682, 1.3000000194))
                Line((14.7845301682, 1.3000000194), (14.8422651951, 1.2000000194))
                Line((14.8422651951, 1.2000000194), (14.9577352489, 1.2000000194))
                Line((14.9577352489, 1.2000000194), (15.0154702759, 1.3000000194))
                Line((15.0154702759, 1.3000000194), (14.9577352489, 1.4000000194))
            make_face()
        # OneSide extrude, distance=-0.3
        extrude(amount=-0.3, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a rectangular bracket or frame with a large central rectangular opening, featuring reinforced corner triangulations and mounting points at the four corners.
def model_31962_e5291336_0017():
    """Model: rectangulo"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 7 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 3.4372566612, perimeter: 13.4849555922
            with BuildLine():
                Line((41.3729174256, -3.2496060462), (38.3729174256, -3.2496060462))
                Line((38.3729174256, -3.2496060462), (38.3729174256, -4.7496060462))
                Line((38.3729174256, -4.7496060462), (41.3729174256, -4.7496060462))
                Line((41.3729174256, -4.7496060462), (41.3729174256, -3.2496060462))
            make_face()
            with BuildLine():
                Line((40.5229174256, -3.6996060462), (39.2229174256, -3.6996060462))
                CenterArc((40.5229174256, -3.9996060462), 0.3, -90, 180)
                Line((39.2229174256, -4.2996060462), (40.5229174256, -4.2996060462))
                CenterArc((39.2229174256, -3.9996060462), 0.3, 90, 180)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.3, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0490873852, perimeter: 0.7853981634
            with Locations((38.6729174256, -4.4496060462)):
                Circle(0.125)
        # OneSide extrude, distance=-0.8
        extrude(amount=-0.8, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a bearing or spacer ring with a cylindrical body, a central circular hole, and four symmetrically-spaced rectangular slots or cutouts around its circumference for weight reduction and material efficiency.
def model_31962_e5291336_0043():
    """Model: ISOrotator"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 3 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.3905443067, perimeter: 12.415574167
            with BuildLine():
                CenterArc((9.5, 1.5), 1.1, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((9.5, 1.5), 0.876, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.7206059565, perimeter: 6.4339817546
            with BuildLine():
                CenterArc((9.5, 1.5), 0.624, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((9.5, 1.5), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.7
        extrude(amount=0.7)
    return part.part


# Description: This is a curved elastomeric or rubber component with a boomerang-like shape, featuring two dark cylindrical end sections and a tapered blue mesh body with a curved, twisted profile.
def model_31962_e5291336_0047():
    """Model: DIN 315"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 8 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.4492513245, perimeter: 9.8856170501
            with BuildLine():
                Line((-8.3791102692, 7.9997835124), (-9.3551665037, 8.9743676427))
                CenterArc((-9.7791102692, 8.5497835124), 0.6, -104.6765041089, 149.7197439309)
                Line((-9.3791102692, 7.8247835124), (-9.9311270285, 7.9693604728))
                Line((-9.3791102692, 7.8247835124), (-9.3791102692, 6.5747835124))
                Line((-9.3791102692, 6.5747835124), (-9.9311270285, 6.430206552))
                CenterArc((-9.7791102692, 5.8497835124), 0.6, -45.043239822, 149.7197439309)
                Line((-8.3791102692, 6.3997835124), (-9.3551665037, 5.4251993821))
                Line((-8.3791102692, 7.9997835124), (-8.3791102692, 6.3997835124))
            make_face()
            # Profile area: 1.1309733553, perimeter: 3.7699111843
            with BuildLine():
                CenterArc((-9.7791102692, 5.8497835124), 0.6, 104.6765041089, 210.2802560691)
                CenterArc((-9.7791102692, 5.8497835124), 0.6, -45.043239822, 149.7197439309)
            make_face()
            # Profile area: 1.1309733553, perimeter: 3.7699111843
            with BuildLine():
                CenterArc((-9.7791102692, 8.5497835124), 0.6, 45.043239822, 210.2802560691)
                CenterArc((-9.7791102692, 8.5497835124), 0.6, -104.6765041089, 149.7197439309)
            make_face()
        # OneSide extrude, distance=0.28
        extrude(amount=0.28)
    return part.part


# Description: This is a cylindrical filter or strainer with a hollow, perforated mesh body that allows fluid or air to pass through while capturing particles, featuring solid end caps on both sides.
def model_31962_e5291336_0052():
    """Model: DIN 2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((4.2995287518, -4.0472089893)):
                Circle(0.2)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.0541265877, perimeter: 0.8660254038
            with BuildLine():
                Line((-4.1798059426, -3.9665877621), (-4.3094873781, -3.9032153815))
                Line((-4.3094873781, -3.9032153815), (-4.4292101873, -3.9838366088))
                Line((-4.4292101873, -3.9838366088), (-4.419251561, -4.1278302166))
                Line((-4.419251561, -4.1278302166), (-4.2895701255, -4.1912025972))
                Line((-4.2895701255, -4.1912025972), (-4.1698473163, -4.1105813699))
                Line((-4.1698473163, -4.1105813699), (-4.1798059426, -3.9665877621))
            make_face()
        # OneSide extrude, distance=-0.3
        extrude(amount=-0.3, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical bowl or container with an elliptical/oval shape, featuring a flat bottom and curved sides, with a wireframe mesh visible on the top interior surface suggesting an open top design.
def model_31968_b384541d_0001():
    """Model: Waxinelicht"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.9087385212, perimeter: 7.853981634
            with Locations((-3.131849293, -2.6258919789)):
                Circle(1.25)
        # OneSide extrude, distance=0.7
        extrude(amount=0.7)
    return part.part


# Description: This is a circular grinding wheel or abrasive disc with a flat, disc-like shape featuring a central axial hole for mounting and radial grooves or flutes across its face for material removal or grinding operations.
def model_32161_15a0a149_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 25.1327412287, perimeter: 25.1327412287
            with BuildLine():
                CenterArc((-2.5, 2.5), 3, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-2.5, 2.5), 1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.5, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((-2.5, 4.5)):
                Circle(0.25)
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a fastener or mounting stud featuring a cylindrical shaft with a polygonal (likely hexagonal) base or head, designed for threaded insertion or mechanical fastening applications.
def model_32169_c6811fb2_0000():
    """Model: Component5"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0310749441, perimeter: 0.6561913262
            with BuildLine():
                Line((0.4389509664, -0.5746930437), (0.5467076082, -0.5560046056))
                Line((0.5467076082, -0.5560046056), (0.584401267, -0.4533403974))
                Line((0.584401267, -0.4533403974), (0.514338284, -0.3693646272))
                Line((0.514338284, -0.3693646272), (0.4065816422, -0.3880530652))
                Line((0.4065816422, -0.3880530652), (0.3688879834, -0.4907172735))
                Line((0.3688879834, -0.4907172735), (0.4389509664, -0.5746930437))
            make_face()
        # OneSide extrude, distance=0.08
        extrude(amount=0.08)

        # Sketch3 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.08, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0078539816, perimeter: 0.3141592654
            with Locations((-0.475676672, 0.472165874)):
                Circle(0.05)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical post or standoff with an angled rectangular base plate, featuring a hollow tubular shaft mounted at an angle to a flat, flanged foundation block with beveled or chamfered edges.
def model_32169_c6811fb2_0001():
    """Model: Component4"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.066510751, perimeter: 0.96
            with BuildLine():
                Line((0.7325881212, 0.1913056734), (0.8854260934, 0.1439711801))
                Line((0.8854260934, 0.1439711801), (1.0028379532, 0.2526655))
                Line((1.0028379532, 0.2526655), (0.9674118408, 0.4086943132))
                Line((0.9674118408, 0.4086943132), (0.8145738686, 0.4560288065))
                Line((0.8145738686, 0.4560288065), (0.6971620088, 0.3473344866))
                Line((0.6971620088, 0.3473344866), (0.7325881212, 0.1913056734))
            make_face()
        # OneSide extrude, distance=0.08
        extrude(amount=0.08)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.08, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0078539816, perimeter: 0.3141592654
            with Locations((-0.8500000127, -0.3000000045)):
                Circle(0.05)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical sleeve or tube with a curved/tapered shape, featuring a solid dark gray body and a blue-textured top rim or flange.
def model_32219_e5edc7ce_0034():
    """Model: ZAKRETKA OD CHAMBER v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.9817477042, perimeter: 7.853981634
            with BuildLine():
                CenterArc((0, 0), 0.75, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.8
        extrude(amount=-0.8)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.7671458676, perimeter: 4.7123889804
            Circle(0.75)
        # OneSide extrude, distance=0.7
        extrude(amount=0.7, mode=Mode.ADD)
    return part.part


# Description: This is a curved composite or laminated structural component with an arch-like shape, featuring a hollow central opening and horizontal linear striations or reinforcing ribs across its outer surfaces.
def model_32219_e5edc7ce_0039():
    """Model: nakladka dookola kola v8"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 9 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 17.081977818, perimeter: 36.3398140599
            with BuildLine():
                CenterArc((0, 0), 4, -15.6210400617, 211.2420801233)
                Line((3.8522549983, -1.0770939738), (4.6612172689, -1.8091582496))
                CenterArc((0, 0), 5, -21.2127265999, 222.4254531998)
                Line((-3.8522549983, -1.0770939738), (-4.6612172689, -1.8091582496))
            make_face()
        # OneSide extrude, distance=5
        extrude(amount=5)
    return part.part


# Description: This is a cylindrical mesh or perforated container with a curved slot or opening cut through its side and a ribbed or corrugated surface pattern throughout its walls.
def model_32220_1fd19c5e_0003():
    """Model: KOLO2 v5"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 13.8544236023, perimeter: 13.1946891451
            Circle(2.1)
        # OneSide extrude, distance=2
        extrude(amount=2)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 9.6211275016, perimeter: 10.9955742876
            Circle(1.75)
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical container or barrel with a curved top surface and a flat or slightly tapered bottom, featuring a mesh-like grid pattern indicating a hollow interior structure.
def model_32220_1fd19c5e_0025():
    """Model: Zarowka czerwona v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            Circle(0.15)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            Circle(0.15)
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a parallelogram-shaped frame or flat bracket with a hollow rectangular opening, featuring uniform dark material (likely steel or aluminum) with beveled or rounded edges along its perimeter.
def model_32220_1fd19c5e_0027():
    """Model: obramowka ekran v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 25 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.2077318531, perimeter: 22.4773185307
            with BuildLine():
                CenterArc((6.3, -4.8245), 0.2, -90, 90)
                Line((6.5, -0.2), (6.5, -4.8245))
                CenterArc((6.3, -0.2), 0.2, 0, 90)
                Line((3.25, 0), (6.3, 0))
                Line((3.25, 0), (3.25, -0.2))
                Line((3.25, -0.2), (6.3, -0.2))
                Line((6.3, -0.2), (6.3, -4.8245))
                Line((6.3, -4.8245), (3.25, -4.8245))
                Line((3.25, -4.8245), (3.25, -5.0245))
                Line((6.3, -5.0245), (3.25, -5.0245))
            make_face()
            # Profile area: 2.2077318531, perimeter: 22.4773185307
            with BuildLine():
                Line((3.25, -4.8245), (3.25, -5.0245))
                Line((3.25, -4.8245), (0.2, -4.8245))
                Line((0.2, -4.8245), (0.2, -0.2))
                Line((0.2, -0.2), (3.25, -0.2))
                Line((3.25, 0), (3.25, -0.2))
                Line((0.2, 0), (3.25, 0))
                CenterArc((0.2, -0.2), 0.2, 90, 90)
                Line((0, -4.8245), (0, -0.2))
                CenterArc((0.2, -4.8245), 0.2, 180, 90)
                Line((3.25, -5.0245), (0.2, -5.0245))
            make_face()
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)
    return part.part


# Description: This is a cylindrical sleeve or tube with a slightly tapered, curved upper edge and a flat bottom base, featuring vertical ribbing or fluting along its exterior surface.
def model_32220_1fd19c5e_0036():
    """Model: stopa v4"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.6597345705, perimeter: 13.1946892481
            with BuildLine():
                CenterArc((0, 0), 1.1000000164, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.6597345705, perimeter: 13.1946892481
            with BuildLine():
                CenterArc((0, 0), 1.1000000164, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            Circle(1)
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)
    return part.part


# Description: This is a dumbbell or weight training handle with a curved connecting bar between two cylindrical end weights, featuring a textured grip section in the middle for ergonomic handling.
def model_32439_3d5a17cf_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 11 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 12.5663706144, perimeter: 12.5663706144
            with BuildLine():
                CenterArc((0, 0), 2, 67, 178)
                CenterArc((0, 0), 2, -115, 182)
            make_face()
            # Profile area: 55.4975176257, perimeter: 47.8682465848
            with BuildLine():
                Line((-11.0728536925, 2.9566006365), (-0.8452365235, -1.8126155741))
                CenterArc((0, 0), 2, 67, 178)
                Line((-9.5668304858, 6.233599367), (0.781462257, 1.8410097069))
                Line((-17.5252029375, 5.955686877), (-9.5668304858, 6.233599367))
                CenterArc((-17.4728536925, 4.4566006365), 1.5, -90, 182)
                Line((-17.4728536925, 2.9566006365), (-11.0728536925, 2.9566006365))
            make_face()
            # Profile area: 7.0685834706, perimeter: 9.4247779608
            with BuildLine():
                CenterArc((-17.4728536925, 4.4566006365), 1.5, -90, 182)
                CenterArc((-17.4728536925, 4.4566006365), 1.5, 92, 178)
            make_face()
        # Symmetric extrude, each_side=0.5
        extrude(amount=0.5, both=True)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 18.0955736847, perimeter: 15.0796447372
            with Locations((-17.4728536925, 4.4566006365)):
                Circle(2.4)
            # Profile area: 30.190705401, perimeter: 19.4778744523
            Circle(3.1)
        # Symmetric extrude, each_side=0.8
        extrude(amount=0.8, both=True, mode=Mode.ADD)
    return part.part


# Description: A cylindrical fastener or standoff with a hexagonal base flange, featuring a threaded or knurled cylindrical shaft extending upward at an angle.
def model_32879_49552f2f_0012():
    """Model: Pieza 9"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.3926990817, perimeter: 2.5707963268
            with BuildLine():
                Line((0, 0.5), (0, -0.5))
                CenterArc((0, 0), 0.5, -90, 180)
            make_face()
            # Profile area: 0.3926990817, perimeter: 2.5707963268
            with BuildLine():
                CenterArc((0, 0), 0.5, 90, 180)
                Line((0, 0.5), (0, -0.5))
            make_face()
        # OneSide extrude, distance=3.5
        extrude(amount=3.5)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.3393517259, perimeter: 6.3442990187
            with BuildLine():
                CenterArc((0, 0), 0.5, -90, 180)
                Line((0, -0.5), (0, -1.1547005384))
                Line((0, -1.1547005384), (1, -0.5773502692))
                Line((1, -0.5773502692), (1, 0.5773502692))
                Line((1, 0.5773502692), (0, 1.1547005384))
                Line((0, 1.1547005384), (0, 0.5))
            make_face()
            # Profile area: 1.3393517259, perimeter: 6.3442990187
            with BuildLine():
                CenterArc((0, 0), 0.5, 90, 180)
                Line((0, 1.1547005384), (0, 0.5))
                Line((0, 1.1547005384), (-1, 0.5773502692))
                Line((-1, 0.5773502692), (-1, -0.5773502692))
                Line((-1, -0.5773502692), (0, -1.1547005384))
                Line((0, -0.5), (0, -1.1547005384))
            make_face()
            # Profile area: 0.3926990817, perimeter: 2.5707963268
            with BuildLine():
                Line((0, 0.5), (0, -0.5))
                CenterArc((0, 0), 0.5, -90, 180)
            make_face()
            # Profile area: 0.3926990817, perimeter: 2.5707963268
            with BuildLine():
                CenterArc((0, 0), 0.5, 90, 180)
                Line((0, 0.5), (0, -0.5))
            make_face()
        # OneSide extrude, distance=-0.7
        extrude(amount=-0.7, mode=Mode.ADD)
    return part.part


# Description: This is a polyhedron-shaped structural component with an irregular faceted geometry, featuring multiple triangular and rectangular faces with internal void passages or slots running through its body, creating a latticed or skeletal internal structure.
def model_32879_49552f2f_0013():
    """Model: Pieza 10"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.3393517259, perimeter: 6.3442990187
            with BuildLine():
                CenterArc((0, 0), 0.5, 90, 180)
                Line((0, 1.1547005384), (0, 0.5))
                Line((0, 1.1547005384), (-1, 0.5773502692))
                Line((-1, 0.5773502692), (-1, -0.5773502692))
                Line((-1, -0.5773502692), (0, -1.1547005384))
                Line((0, -0.5), (0, -1.1547005384))
            make_face()
            # Profile area: 1.3393517259, perimeter: 6.3442990187
            with BuildLine():
                CenterArc((0, 0), 0.5, -90, 180)
                Line((0, -0.5), (0, -1.1547005384))
                Line((0, -1.1547005384), (1, -0.5773502692))
                Line((1, -0.5773502692), (1, 0.5773502692))
                Line((1, 0.5773502692), (0, 1.1547005384))
                Line((0, 1.1547005384), (0, 0.5))
            make_face()
        # OneSide extrude, distance=0.7
        extrude(amount=0.7)
    return part.part


# Description: This is a fastener or mounting component featuring a cylindrical shaft extending from an angular, multi-faceted base with geometric faces, likely designed for insertion into a mating pocket or assembly.
def model_32879_49552f2f_0018():
    """Model: Pieza 15"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.3926990817, perimeter: 2.5707963268
            with BuildLine():
                CenterArc((0, 0), 0.5, 90, 180)
                Line((0, 0.5), (0, -0.5))
            make_face()
            # Profile area: 0.3926990817, perimeter: 2.5707963268
            with BuildLine():
                Line((0, 0.5), (0, -0.5))
                CenterArc((0, 0), 0.5, -90, 180)
            make_face()
        # OneSide extrude, distance=2.05
        extrude(amount=2.05)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.8587076268, perimeter: 5.4782736149
            with BuildLine():
                CenterArc((0, 0), 0.5, 90, 180)
                Line((0, 0.9814954576), (0, 0.5))
                Line((0, 0.9814954576), (-0.85, 0.4907477288))
                Line((-0.85, 0.4907477288), (-0.85, -0.4907477288))
                Line((-0.85, -0.4907477288), (0, -0.9814954576))
                Line((0, -0.5), (0, -0.9814954576))
            make_face()
            # Profile area: 0.8587076268, perimeter: 5.4782736149
            with BuildLine():
                CenterArc((0, 0), 0.5, -90, 180)
                Line((0, -0.5), (0, -0.9814954576))
                Line((0, -0.9814954576), (0.85, -0.4907477288))
                Line((0.85, -0.4907477288), (0.85, 0.4907477288))
                Line((0.85, 0.4907477288), (0, 0.9814954576))
                Line((0, 0.9814954576), (0, 0.5))
            make_face()
            # Profile area: 0.3926990817, perimeter: 2.5707963268
            with BuildLine():
                CenterArc((0, 0), 0.5, 90, 180)
                Line((0, 0.5), (0, -0.5))
            make_face()
            # Profile area: 0.3926990817, perimeter: 2.5707963268
            with BuildLine():
                Line((0, 0.5), (0, -0.5))
                CenterArc((0, 0), 0.5, -90, 180)
            make_face()
        # OneSide extrude, distance=-0.7
        extrude(amount=-0.7, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical connector or adapter with an angled mounting base featuring a faceted/geometric design, housing a central cylindrical bore or post that extends upward at an incline.
def model_32879_49552f2f_0019():
    """Model: Pieza 14"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.3926990817, perimeter: 2.5707963268
            with BuildLine():
                CenterArc((0, 0), 0.5, 90, 180)
                Line((0, 0.5), (0, -0.5))
            make_face()
            # Profile area: 0.3926990817, perimeter: 2.5707963268
            with BuildLine():
                Line((0, 0.5), (0, -0.5))
                CenterArc((0, 0), 0.5, -90, 180)
            make_face()
        # OneSide extrude, distance=1.9
        extrude(amount=1.9)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.3393517259, perimeter: 6.3442990187
            with BuildLine():
                CenterArc((0, 0), 0.5, 90, 180)
                Line((0, 1.1547005384), (0, 0.5))
                Line((0, 1.1547005384), (-1, 0.5773502692))
                Line((-1, 0.5773502692), (-1, -0.5773502692))
                Line((-1, -0.5773502692), (0, -1.1547005384))
                Line((0, -0.5), (0, -1.1547005384))
            make_face()
            # Profile area: 1.3393517259, perimeter: 6.3442990187
            with BuildLine():
                CenterArc((0, 0), 0.5, -90, 180)
                Line((0, -0.5), (0, -1.1547005384))
                Line((0, -1.1547005384), (1, -0.5773502692))
                Line((1, -0.5773502692), (1, 0.5773502692))
                Line((1, 0.5773502692), (0, 1.1547005384))
                Line((0, 1.1547005384), (0, 0.5))
            make_face()
            # Profile area: 0.3926990817, perimeter: 2.5707963268
            with BuildLine():
                CenterArc((0, 0), 0.5, 90, 180)
                Line((0, 0.5), (0, -0.5))
            make_face()
            # Profile area: 0.3926990817, perimeter: 2.5707963268
            with BuildLine():
                Line((0, 0.5), (0, -0.5))
                CenterArc((0, 0), 0.5, -90, 180)
            make_face()
        # OneSide extrude, distance=-0.7
        extrude(amount=-0.7, mode=Mode.ADD)
    return part.part


# Description: This is a black plastic connector or clip housing with a vertical U-shaped channel, featuring dual parallel slots, ventilation openings, and a topped mounting head designed for securing or guiding components.
def model_33265_e489d292_0000():
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
        # Sketch4 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 65 constraints, 15 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 2.0629151344, perimeter: 16.6862263168
            with BuildLine():
                Line((0.7311191125, 2.2812891779), (0.7311191125, 5.4000000805))
                CenterArc((1.2811191125, 2.2812891779), 0.55, 180, 90)
                Line((2.4205069633, 1.7312891779), (1.2811191125, 1.7312891779))
                CenterArc((2.4205069633, 2.2812891779), 0.55, -90, 89.4595875252)
                Line((3.0000000447, 5.405527286), (2.9704824989, 2.2761016675))
                Line((2.9653436876, 5.405527286), (3.0000000447, 5.405527286))
                Line((2.8498702809, 2.9048509851), (2.9653436876, 5.405527286))
                CenterArc((2.3504025057, 2.9279148441), 0.5, -90, 87.3561382895)
                Line((1.363370085, 2.4279148441), (2.3504025057, 2.4279148441))
                CenterArc((1.363370085, 2.9279148441), 0.5, -177.6155998399, 87.6155998399)
                Line((0.759999983, 5.4000000805), (0.8638029877, 2.9071130329))
                Line((0.7311191125, 5.4000000805), (0.759999983, 5.4000000805))
            make_face()
            # Profile area: 2.4171498506, perimeter: 17.5413457715
            with BuildLine():
                CenterArc((0.8591451939, 1.2609183792), 0.45, 178.8473502231, 91.1526497769)
                Line((2.8915529513, 0.8109183792), (0.8591451939, 0.8109183792))
                CenterArc((2.8915529513, 1.2609183792), 0.45, -90, 91.3740253353)
                Line((3.2690594274, 4.2886580273), (3.3414235597, 1.2717089146))
                Line((3.2399999276, 4.2899999041), (3.2690594274, 4.2886580273))
                Line((3.1182962542, 1.7569504671), (3.2399999276, 4.2899999041))
                CenterArc((2.718757146, 1.7761468462), 0.4, -90, 87.2492646739)
                Line((1.0317862079, 1.3761468462), (2.718757146, 1.3761468462))
                CenterArc((1.0317862079, 1.7761468462), 0.4, -177.0290578206, 87.0290578206)
                Line((0.5008129633, 4.2893799394), (0.6323238284, 1.7554150502))
                Line((0.4699999895, 4.2899999041), (0.5008129633, 4.2893799394))
                Line((0.4092362517, 1.2699706587), (0.4699999895, 4.2899999041))
            make_face()
            # Profile area: 0.6785250639, perimeter: 9.2685542526
            with BuildLine():
                Line((3.1501152157, 0.2398199962), (3.14398456, 0.2396812715))
                CenterArc((3.1399352081, 0.6897048342), 0.45, -88.703730601, 90)
                Line((3.5337366061, 3.1783790058), (3.5898200461, 0.6998848417))
                Line((3.4999999218, 3.1799999289), (3.5337366061, 3.1783790058))
                Line((3.4611506194, 1.1291531911), (3.4999999218, 3.1799999289))
                CenterArc((2.8612582422, 1.1405169853), 0.6, -90, 88.914772697)
                Line((1.5064157326, 0.5405169853), (2.8612582422, 0.5405169853))
                Line((1.5000000224, 0.5000000075), (1.5064157326, 0.5405169853))
                Line((3.14398456, 0.2396812715), (1.5000000224, 0.5000000075))
            make_face()
            # Profile area: 0.2180322313, perimeter: 3.7484374959
            with BuildLine():
                _nurbs_edge([(2.271047818, 6.3500000946), (2.2696105079, 6.3346996663), (2.2662817879, 6.3045371879), (2.2599264198, 6.2606085969), (2.2487081212, 6.2046865838), (2.2299742588, 6.139356102), (2.2063264021, 6.0788663076), (2.177527936, 6.0235930976), (2.1433498669, 5.9740051376), (2.1036319302, 5.9306378491), (2.058268869, 5.8940509103), (2.0072062248, 5.8647646342), (1.950447959, 5.8431921749), (1.8880928249, 5.8295195038), (1.8203415431, 5.8236611947), (1.7474177074, 5.8254128929), (1.6851022934, 5.8327118985), (1.6361921226, 5.8414192163), (1.6026263126, 5.8486505549), (1.5856036474, 5.8526228444)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0666666667, 0.1333333333, 0.2, 0.2666666667, 0.3333333333, 0.4, 0.4666666667, 0.5333333333, 0.6, 0.6666666667, 0.7333333333, 0.8, 0.8666666667, 0.9333333333, 1, 1, 1, 1, 1, 1], 5)
                Line((2.271047818, 7.2000001073), (2.271047818, 6.3500000946))
                Line((2.150000032, 7.2000001073), (2.271047818, 7.2000001073))
                _nurbs_edge([(1.5882830817, 5.9755011072), (1.5983087753, 5.9739152079), (1.6182901798, 5.9708067135), (1.6480523427, 5.9663337084), (1.6873142044, 5.960751686), (1.7356583372, 5.9546396097), (1.7831850503, 5.9500995204), (1.8297352148, 5.9484915122), (1.8750474207, 5.9522069368), (1.9187501366, 5.9641468691), (1.9603592672, 5.9866083812), (1.9992821757, 6.0204938429), (2.0347985625, 6.0640251865), (2.0661284355, 6.1129679202), (2.0925878512, 6.1623538051), (2.113729743, 6.2078399262), (2.1294810642, 6.2471093136), (2.1403240903, 6.2815552711), (2.1471264417, 6.3152435298), (2.1509165856, 6.3534256656), (2.1526723072, 6.4011587763), (2.1531343655, 6.4620755307), (2.1528566086, 6.5387354886), (2.152228855, 6.6327864237), (2.1515088956, 6.7451824178), (2.150849255, 6.8763616508), (2.1504298755, 6.9964138893), (2.1501871132, 7.094922067), (2.1500570896, 7.1643483927), (2.150000032, 7.2000001073)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.04, 0.08, 0.12, 0.16, 0.2, 0.24, 0.28, 0.32, 0.36, 0.4, 0.44, 0.48, 0.52, 0.56, 0.6, 0.64, 0.68, 0.72, 0.76, 0.8, 0.84, 0.88, 0.92, 0.96, 1, 1, 1, 1, 1, 1], 5)
                Line((1.5856036474, 5.8526228444), (1.5882830817, 5.9755011072))
            make_face()
            # Profile area: 0.2561567703, perimeter: 1.8001448756
            with Locations((1.8642515184, 7.4341092084)):
                Ellipse(0.3052628514, 0.267104995, rotation=-90)
            # Profile area: 2.148411134, perimeter: 16.8492747395
            with BuildLine():
                CenterArc((1.45222772, 3.0500000387), 0.45, 179.7170606991, 90.2829393009)
                Line((2.2508320118, 2.6000000387), (1.45222772, 2.6000000387))
                CenterArc((2.2508320118, 3.0500000387), 0.45, -90, 90)
                Line((2.7008320118, 6.654317711), (2.7008320118, 3.0500000387))
                Line((2.6780182957, 6.6554065254), (2.7008320118, 6.654317711))
                Line((2.5430268054, 3.8269560993), (2.6780182957, 6.6554065254))
                CenterArc((2.1934247407, 3.8436413144), 0.35, -90.3671496835, 87.6347071763)
                Line((1.5316474768, 3.4978748358), (2.1911819663, 3.4936485002))
                CenterArc((1.5338902513, 3.84786765), 0.35, -177.2838290756, 86.9166793921)
                Line((1.0505680592, 6.6498039693), (1.1842834623, 3.83128172))
                Line((1.0199999772, 6.6499998514), (1.0505680592, 6.6498039693))
                Line((1.0022332068, 3.0522222298), (1.0199999772, 6.6499998514))
            make_face()
            # Profile area: 0.2580303118, perimeter: 4.2594859641
            with BuildLine():
                Line((1.5798524501, 6.5298521976), (1.579189885, 7.2029174901))
                Line((1.579189885, 7.2029174901), (1.4500000216, 7.2029174901))
                Line((1.4500000216, 7.2029174901), (1.4500000216, 6.5000000931))
                CenterArc((1.7000000216, 6.5000000931), 0.25, -180, 90)
                Line((1.7000000216, 6.2500000931), (1.9270997525, 6.2500000931))
                Line((1.9270997525, 6.2500000931), (1.9270997525, 6.9500001036))
                Line((1.9270997525, 6.9500001036), (2.0729974388, 6.9500001036))
                Line((2.0729974388, 6.9500001036), (2.0729974388, 7.0199998431))
                Line((2.0729974388, 7.0199998431), (1.78999996, 7.0199998431))
                Line((1.78999996, 7.0199998431), (1.78999996, 6.3799998574))
                Line((1.78999996, 6.3799998574), (1.7298523775, 6.3799998574))
                CenterArc((1.7298523775, 6.5299998574), 0.15, -179.9435980864, 89.9435980864)
            make_face()
        # OneSide extrude, distance=0.6
        extrude(amount=0.6)

        # Sketch5 -> Extrude2 (Cut)
        # Sketch on XY construction plane
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0237910754, perimeter: 0.6240209562
            with BuildLine():
                Line((1.8642515184, 7.6230005417), (1.8642515184, 7.4341092084))
                Line((1.8642515184, 7.4341092084), (2.0246174678, 7.4341092084))
                EllipticalCenterArc((1.8642515184, 7.4341092084), 0.1888913333, 0.1603659494, -90, 0, 90)
            make_face()
            # Profile area: 0.0237910754, perimeter: 0.6240209562
            with BuildLine():
                EllipticalCenterArc((1.8642515184, 7.4341092084), 0.1888913333, 0.1603659494, 0, 90, 90)
                Line((1.7038855689, 7.4341092084), (1.8642515184, 7.4341092084))
                Line((1.8642515184, 7.6230005417), (1.8642515184, 7.4341092084))
            make_face()
            # Profile area: 0.0237910754, perimeter: 0.6240209562
            with BuildLine():
                Line((1.8642515184, 7.4341092084), (1.8642515184, 7.2452178751))
                EllipticalCenterArc((1.8642515184, 7.4341092084), 0.1888913333, 0.1603659494, -180, 0, 90)
                Line((1.8642515184, 7.4341092084), (2.0246174678, 7.4341092084))
            make_face()
            # Profile area: 0.0237910754, perimeter: 0.6240209562
            with BuildLine():
                Line((1.7038855689, 7.4341092084), (1.8642515184, 7.4341092084))
                EllipticalCenterArc((1.8642515184, 7.4341092084), 0.1888913333, 0.1603659494, 0, 0, 90)
                Line((1.8642515184, 7.4341092084), (1.8642515184, 7.2452178751))
            make_face()
        # OneSide extrude, distance=0.6
        extrude(amount=0.6, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical tube or pipe with rounded ends, featuring a uniform hollow or solid cylindrical body tilted at an angle.
def model_33607_c6f31fa6_0036():
    """Model: valve pipe (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.6092597612, perimeter: 14.2676058681
            with BuildLine():
                CenterArc((0, 0), 1.31826, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.9525, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=16.764
        extrude(amount=16.764)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on XY construction plane
        # Sketch has 3 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.3562786962, perimeter: 2.4486835013
            with BuildLine():
                Line((0, 13.42898), (0, 12.47648))
                CenterArc((0, 12.95273), 0.47625, 90, 180)
            make_face()
            # Profile area: 0.3562786962, perimeter: 2.4486835013
            with BuildLine():
                CenterArc((0, 12.95273), 0.47625, -90, 180)
                Line((0, 13.42898), (0, 12.47648))
            make_face()
        # Symmetric extrude, each_side=3.81
        extrude(amount=3.81, both=True, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a flat parallelogram or skewed rectangular plate with a uniform dark gray color and simple geometric form, featuring no holes, slots, or additional features—essentially a basic planar shear or slanted panel component.
def model_33625_c9ff9be8_0000():
    """Model: Back door v5"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1200, perimeter: 146
            with BuildLine():
                Line((0, 25), (0, 0))
                Line((0, 0), (48, 0))
                Line((48, 0), (48, 25))
                Line((48, 25), (0, 25))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            with Locations((0.5000000075, 0.4)):
                Circle(0.3)
        # OneSide extrude, distance=-66
        extrude(amount=-66, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a channel or U-shaped bracket with a uniform rectangular cross-section, featuring two perpendicular flanges connected by a web, designed for structural support or assembly mounting applications.
def model_33625_c9ff9be8_0002():
    """Model: Front support v10"""
    with BuildPart() as part:
        # Sketch1 -> Extrude4 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 48, perimeter: 32
            with BuildLine():
                Line((6, -2), (-6, -2))
                Line((6, 2), (6, -2))
                Line((-6, 2), (6, 2))
                Line((-6, -2), (-6, 2))
            make_face()
        # OneSide extrude, distance=20
        extrude(amount=20)

        # Sketch4 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-6, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 40, perimeter: 28
            with BuildLine():
                Line((-2, 10), (-2, 0))
                Line((-2, 0), (2, 0))
                Line((2, 0), (2, 10))
                Line((2, 10), (-2, 10))
            make_face()
        # OneSide extrude, distance=17
        extrude(amount=17, mode=Mode.ADD)
    return part.part


# Description: This is a rectangular box or enclosure with an open interior cavity, featuring angled side walls, a top opening with a recessed rim, and internal structural elements or reinforcements visible through the hollow section.
def model_33625_c9ff9be8_0003():
    """Model: Support v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 48, perimeter: 32
            with BuildLine():
                Line((6, -2), (-6, -2))
                Line((6, 2), (6, -2))
                Line((-6, 2), (6, 2))
                Line((-6, -2), (-6, 2))
            make_face()
        # OneSide extrude, distance=17
        extrude(amount=17)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 2), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 12.5663706144, perimeter: 12.5663706144
            with Locations((0, 6)):
                Circle(2)
        # OneSide extrude, distance=-10.5
        extrude(amount=-10.5, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical pipe or tube assembly with a dark gray cylindrical body and a blue polygonal geometric head or connector piece at the top, featuring angular faceted surfaces.
def model_33655_f8991a06_0000():
    """Model: pieza 15 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.233826859, perimeter: 1.8
            with BuildLine():
                Line((-0.2598076211, -0.15), (0, -0.3))
                Line((0, -0.3), (0.2598076211, -0.15))
                Line((0.2598076211, -0.15), (0.2598076211, 0.15))
                Line((0.2598076211, 0.15), (0, 0.3))
                Line((0, 0.3), (-0.2598076211, 0.15))
                Line((-0.2598076211, 0.15), (-0.2598076211, -0.15))
            make_face()
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)

        # Sketch3 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.0939703848, perimeter: 1.0866768989
            Circle(0.17295)
        # OneSide extrude, distance=1.3
        extrude(amount=1.3, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical shaft or rod with an octagonal or polygonal head at the top, featuring a dark gray cylindrical body and a blue-shaded geometric head with multiple faceted surfaces, resembling a bolt or fastener component.
def model_33655_f8991a06_0001():
    """Model: pieza 15"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.233826859, perimeter: 1.8
            with BuildLine():
                Line((-0.2598076211, -0.15), (0, -0.3))
                Line((0, -0.3), (0.2598076211, -0.15))
                Line((0.2598076211, -0.15), (0.2598076211, 0.15))
                Line((0.2598076211, 0.15), (0, 0.3))
                Line((0, 0.3), (-0.2598076211, 0.15))
                Line((-0.2598076211, 0.15), (-0.2598076211, -0.15))
            make_face()
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)

        # Sketch3 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.0825497766, perimeter: 1.0185043383
            Circle(0.1621)
        # OneSide extrude, distance=1.3
        extrude(amount=1.3, mode=Mode.ADD)
    return part.part


# Description: This is a fan impeller or blower wheel featuring a circular disk-shaped body with curved blade fins extending radially outward, a central hub for mounting, and mesh-textured surfaces indicating aerodynamic blade geometry.
def model_33785_a4c23f61_0002():
    """Model: Component1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 7 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 2.4224629967, perimeter: 9.4734107456
            with BuildLine():
                CenterArc((-0.6000000089, -0.2392571753), 0.8333919646, -90, 180)
                Line((-0.6000000089, 0.5941347893), (-1.7805076863, 0.5941347893))
                Line((-1.7805076863, 0.5941347893), (-1.7805076863, -1.0726491399))
                Line((-1.7805076863, -1.0726491399), (-0.6000000089, -1.0726491399))
            make_face()
            with BuildLine():
                CenterArc((-0.6000000089, -0.2392571753), 0.45, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=2
        extrude(amount=2)

        # Sketch3 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1.7805076863), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 24.9407660239, perimeter: 26.1831237799
            with BuildLine():
                CenterArc((1, -0.2392571753), 3, 0, 360)
            make_face()
            with BuildLine():
                Line((2, -1.0726491399), (2, 0.5941347893))
                Line((0, -1.0726491399), (2, -1.0726491399))
                Line((0, 0.5941347893), (0, -1.0726491399))
                Line((2, 0.5941347893), (0, 0.5941347893))
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 3.3335678584, perimeter: 7.3335678584
            with BuildLine():
                Line((2, 0.5941347893), (0, 0.5941347893))
                Line((0, 0.5941347893), (0, -1.0726491399))
                Line((0, -1.0726491399), (2, -1.0726491399))
                Line((2, -1.0726491399), (2, 0.5941347893))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)
    return part.part


# Description: This is a camera lens or optical assembly featuring a polygonal mounting flange on one end and a cylindrical barrel with internal mesh/lens elements visible through the transparent rendering on the other end.
def model_33967_0741e236_0001():
    """Model: Component4"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 1.2730573436, perimeter: 4.2
            with BuildLine():
                Line((0.35, 0.6062177826), (0.7, 0))
                Line((-0.35, 0.6062177826), (0.35, 0.6062177826))
                Line((-0.7, 0), (-0.35, 0.6062177826))
                Line((-0.35, -0.6062177826), (-0.7, 0))
                Line((0.35, -0.6062177826), (-0.35, -0.6062177826))
                Line((0.7, 0), (0.35, -0.6062177826))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            Circle(0.5)
        # OneSide extrude, distance=2
        extrude(amount=2, mode=Mode.ADD)
    return part.part


# Description: This is a hexagonal block with a cylindrical bore featuring a threaded hole or shaft extending through one side, commonly used as a fastening component or connector in mechanical assemblies.
def model_33967_0741e236_0002():
    """Model: Component5"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 2.5980762114, perimeter: 6
            with BuildLine():
                Line((0.5, 0.8660254038), (1, 0))
                Line((-0.5, 0.8660254038), (0.5, 0.8660254038))
                Line((-1, 0), (-0.5, 0.8660254038))
                Line((-0.5, -0.8660254038), (-1, 0))
                Line((0.5, -0.8660254038), (-0.5, -0.8660254038))
                Line((1, 0), (0.5, -0.8660254038))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            Circle(0.25)
        # OneSide extrude, distance=2
        extrude(amount=2, mode=Mode.ADD)
    return part.part


# Description: This is a fastening bolt featuring a hexagonal head at one end and a cylindrical threaded shaft extending from it, used for securing components together.
def model_33967_0741e236_0003():
    """Model: Component2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 0.9353074361, perimeter: 3.6
            with BuildLine():
                Line((0.3, 0.5196152423), (0.6, 0))
                Line((-0.3, 0.5196152423), (0.3, 0.5196152423))
                Line((-0.6, 0), (-0.3, 0.5196152423))
                Line((-0.3, -0.5196152423), (-0.6, 0))
                Line((0.3, -0.5196152423), (-0.3, -0.5196152423))
                Line((0.6, 0), (0.3, -0.5196152423))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            Circle(0.4)
        # OneSide extrude, distance=8.5
        extrude(amount=8.5, mode=Mode.ADD)
    return part.part


# Description: This is a tapered metal wedge or shim with an elongated triangular profile, featuring a gradual thickness reduction from one end to the other, commonly used for alignment, leveling, or spacing applications.
def model_33991_aaf84876_0014():
    """Model: Gryf"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 22.3586283306, perimeter: 22.8849555922
            with BuildLine():
                Line((7.5, -3), (0, -3))
                Line((7.5, 0), (7.5, -3))
                Line((0, 0), (7.5, 0))
                Line((0, -3), (0, 0))
            make_face()
            with BuildLine():
                CenterArc((6.5, -1.5), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1, -1.5), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((6.5, -1.5)):
                Circle(0.15)
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((1, -1.5)):
                Circle(0.15)
        # OneSide extrude, distance=0.02
        extrude(amount=0.02)

        # Sketch2 -> Extrude2 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 5 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 3.75, perimeter: 16
            with BuildLine():
                Line((0, 0.52), (7.5, 0.52))
                Line((0, 0.02), (0, 0.52))
                Line((7.5, 0.02), (0, 0.02))
                Line((7.5, 0.52), (7.5, 0.02))
            make_face()
        # OneSide extrude, distance=-65
        extrude(amount=-65)
    return part.part


# Description: This is a cylindrical rod or shaft with a uniform diameter and smooth surface, featuring a slight taper or point at one end.
def model_34063_0ca1585e_0001():
    """Model: Main Shaft"""
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
        # OneSide extrude, distance=-15
        extrude(amount=-15)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            with Locations((0, -2)):
                Circle(0.1)
        # Symmetric extrude, each_side=0.3
        extrude(amount=0.3, both=True, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical shaft or axle with two enlarged end caps featuring a central ribbed or lattice-reinforced section that tapers along its length, designed to provide structural support while minimizing weight.
def model_34063_0ca1585e_0002():
    """Model: Swashplate Follower Arm"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 13 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.3121150204, perimeter: 7.9153150879
            with BuildLine():
                CenterArc((-1.5, 0), 0.4, -78.578813725, 157.15762745)
                CenterArc((0, -7.425), 7.175, 78.578813725, 22.84237255)
                CenterArc((1.5, 0), 0.4, 101.421186275, 157.15762745)
                CenterArc((0, 7.425), 7.175, -101.421186275, 22.84237255)
            make_face()
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            with BuildLine():
                CenterArc((-1.5, 0), 0.4, 78.578813725, 202.84237255)
                CenterArc((-1.5, 0), 0.4, -78.578813725, 157.15762745)
            make_face()
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            with BuildLine():
                CenterArc((1.5, 0), 0.4, -101.421186275, 202.84237255)
                CenterArc((1.5, 0), 0.4, 101.421186275, 157.15762745)
            make_face()
        # OneSide extrude, distance=-0.25
        extrude(amount=-0.25)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on YZ construction plane
        # Sketch has 13 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            with BuildLine():
                CenterArc((1.5, 0), 0.4, -101.421186275, 202.84237255)
                CenterArc((1.5, 0), 0.4, 101.421186275, 157.15762745)
            make_face()
        # OneSide extrude, distance=-0.7
        extrude(amount=-0.7, mode=Mode.ADD)

        # Sketch1 -> Extrude3 (Join)
        # Sketch on YZ construction plane
        # Sketch has 13 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            with BuildLine():
                CenterArc((-1.5, 0), 0.4, 78.578813725, 202.84237255)
                CenterArc((-1.5, 0), 0.4, -78.578813725, 157.15762745)
            make_face()
        # OneSide extrude, distance=0.45
        extrude(amount=0.45, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical connector or adapter assembly featuring a large circular base with a rectangular upper section that includes a slot opening, designed to join or mount two components together.
def model_34222_5121da73_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 8.8278756197, perimeter: 10.5325380025
            Circle(1.6763054864)
        # OneSide extrude, distance=3
        extrude(amount=3)

        # Sketch5 -> Extrude5 (Join)
        # Sketch on XY construction plane
        # Sketch has 7 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 6.3437170506, perimeter: 18.5209694173
            with BuildLine():
                Line((1.2000000179, 7.7000001147), (-1.2000000179, 7.7000001147))
                Line((-1.2000000179, 7.7000001147), (-1.2000000179, 5.300000079))
                CenterArc((-1.4285714499, 4.4000000656), 0.9285714424, 0, 75.7499673022)
                Line((-0.5000000075, 3.0000000447), (-0.5000000075, 4.4000000656))
                Line((-0.5000000075, 3.0000000447), (0.5000000075, 3.0000000447))
                Line((0.5000000075, 3.0000000447), (0.5000000075, 4.4000000656))
                CenterArc((1.4285714499, 4.4000000656), 0.9285714424, 104.2500326978, 75.7499673022)
                Line((1.2000000179, 5.300000079), (1.2000000179, 7.7000001147))
            make_face()
            with BuildLine():
                CenterArc((0, 6.5000000969), 0.8062257868, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=0.5
        extrude(amount=0.5, both=True, mode=Mode.ADD)
    return part.part


# Description: This is a U-shaped bracket or clamp with two parallel cylindrical arms connected by a curved base section, featuring internal geometry and mounting surfaces for fastening or holding components.
def model_34226_dbed877f_0005():
    """Model: wieszak v1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 17 constraints, 12 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 12.5615044408, perimeter: 20.0849555922
            with BuildLine():
                Line((-1, -2.5), (0.5, -2.5))
                Line((0.5, 2.5), (0.5, -2.5))
                Line((0.5, 2.5), (-0.25, 2.5))
                Line((-0.25, 2.5), (-0.25, 1.2))
                CenterArc((-0.25, 1), 0.2, 180, 270)
                Line((-1.55, 1), (-0.45, 1))
                CenterArc((-1.75, 1), 0.2, 90, 270)
                Line((-1.75, 2.5), (-1.75, 1.2))
                Line((-2.5, 2.5), (-1.75, 2.5))
                Line((-2.5, 2.5), (-2.5, -2.5))
                Line((-2.5, -2.5), (-1, -2.5))
            make_face()
            # Profile area: 4.8822847484, perimeter: 11.4496034248
            with BuildLine():
                Line((-4.5, -3.5), (-3.5, -3.5))
                CenterArc((-4.5, -4.25), 0.75, -90, 180)
                Line((-2.5, -5), (-4.5, -5))
                CenterArc((-4.25, -2.25), 3.2596012026, -57.5288077092, 53.1301023542)
                Line((-2.5, -2.5), (-1, -2.5))
                CenterArc((-3.5, -2.5), 1, -90, 90)
            make_face()
            # Profile area: 2.1871681469, perimeter: 5.8283185307
            with BuildLine():
                Line((-1.75, 2.5), (-1.75, 1.2))
                CenterArc((-1.75, 1), 0.2, 0, 90)
                Line((-1.55, 1), (-0.45, 1))
                CenterArc((-0.25, 1), 0.2, 90, 90)
                Line((-0.25, 2.5), (-0.25, 1.2))
                Line((-1.75, 2.5), (-0.25, 2.5))
            make_face()
            # Profile area: 4.8822847484, perimeter: 11.4496034248
            with BuildLine():
                CenterArc((2.25, -2.25), 3.2596012026, -175.601294645, 53.1301023542)
                Line((0.5, -5), (2.5, -5))
                CenterArc((2.5, -4.25), 0.75, 90, 180)
                Line((2.5, -3.5), (1.5, -3.5))
                CenterArc((1.5, -2.5), 1, 180, 90)
                Line((-1, -2.5), (0.5, -2.5))
            make_face()
        # OneSide extrude, distance=0.4
        extrude(amount=0.4)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 17 constraints, 12 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.7671458676, perimeter: 4.7123889804
            with BuildLine():
                CenterArc((2.5, -4.25), 0.75, 90, 180)
                CenterArc((2.5, -4.25), 0.75, -90, 180)
            make_face()
            # Profile area: 1.7671458676, perimeter: 4.7123889804
            with BuildLine():
                CenterArc((-4.5, -4.25), 0.75, 90, 180)
                CenterArc((-4.5, -4.25), 0.75, -90, 180)
            make_face()
        # OneSide extrude, distance=5
        extrude(amount=5, mode=Mode.ADD)

        # Sketch2 -> Extrude3 (Join)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 1.7671458676, perimeter: 4.7123889804
            with Locations((2.5, 4.25)):
                Circle(0.75)
            # Profile area: 1.7671458676, perimeter: 4.7123889804
            with Locations((-4.5, 4.25)):
                Circle(0.75)
        # OneSide extrude, distance=4
        extrude(amount=4, mode=Mode.ADD)
    return part.part


# Description: This is a two-sided A-frame ladder with vertical side rails, three horizontal rungs/steps, and rectangular cross-bracing connecting the frame structure for structural stability.
def model_34227_48203345_0008():
    """Model: part station"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 8 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1000, perimeter: 140
            with BuildLine():
                Line((120, -200), (100, -200))
                Line((120, -150), (120, -200))
                Line((100, -150), (120, -150))
                Line((100, -200), (100, -150))
            make_face()
            # Profile area: 1000, perimeter: 140
            with BuildLine():
                Line((270, -200), (250, -200))
                Line((270, -150), (270, -200))
                Line((250, -150), (270, -150))
                Line((250, -200), (250, -150))
            make_face()
        # OneSide extrude, distance=210
        extrude(amount=210)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 18 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(270, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 250, perimeter: 110
            with BuildLine():
                Line((-200, 190), (-150, 190))
                Line((-200, 185), (-200, 190))
                Line((-150, 185), (-200, 185))
                Line((-150, 185), (-150, 190))
            make_face()
            # Profile area: 250, perimeter: 110
            with BuildLine():
                Line((-200, 125), (-150, 125))
                Line((-200, 120), (-200, 125))
                Line((-150, 120), (-200, 120))
                Line((-150, 125), (-150, 120))
            make_face()
            # Profile area: 250, perimeter: 110
            with BuildLine():
                Line((-200, 60), (-150, 60))
                Line((-200, 55), (-200, 60))
                Line((-150, 55), (-200, 55))
                Line((-150, 60), (-150, 55))
            make_face()
        # OneSide extrude, distance=-160
        extrude(amount=-160, mode=Mode.ADD)
    return part.part


# Description: This is a metal bracket or mounting clip with a rectangular tubular body and an angled flange at the top, designed for structural support or component attachment with a bent/inclined mounting surface.
def model_34227_48203345_0011():
    """Model: welding station"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1000, perimeter: 140
            with BuildLine():
                Line((200, 200), (200, 150))
                Line((200, 150), (220, 150))
                Line((220, 150), (220, 200))
                Line((220, 200), (200, 200))
            make_face()
        # OneSide extrude, distance=130
        extrude(amount=130)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 130, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2600, perimeter: 400
            with BuildLine():
                Line((-230, -130), (-190, -130))
                Line((-230, -220), (-230, -130))
                Line((-190, -220), (-230, -220))
                Line((-190, -130), (-190, -220))
            make_face()
            with BuildLine():
                Line((-220, -150), (-220, -200))
                Line((-200, -150), (-220, -150))
                Line((-200, -200), (-200, -150))
                Line((-220, -200), (-200, -200))
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 1000, perimeter: 140
            with BuildLine():
                Line((-220, -200), (-200, -200))
                Line((-200, -200), (-200, -150))
                Line((-200, -150), (-220, -150))
                Line((-220, -150), (-220, -200))
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2, mode=Mode.ADD)
    return part.part


# Description: This is a cactus-shaped component featuring three rounded, bulbous segments arranged organically with a small leaf-like protrusion on top, resembling a stylized prickly pear or barrel cactus.
def model_34323_d1617369_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch29 -> Extrude3 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 3 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.6562496931, perimeter: 4.6786166112
            with BuildLine():
                CenterArc((-10.5, 1), 0.75, 0, 292.619864948)
                CenterArc((-9, 0), 1.25, 126.8698976458, 38.8800696564)
            make_face()
            # Profile area: 4.6869461721, perimeter: 7.9215263723
            with BuildLine():
                CenterArc((-10.5, 1), 0.75, -67.380135052, 67.380135052)
                CenterArc((-9, 0), 1.25, 165.7499673022, 208.5000653956)
                CenterArc((-7.5, 1), 0.75, -180, 67.380135052)
                CenterArc((-9, 0), 1.25, 53.1301023542, 8.1779044986)
                CenterArc((-9, 0), 1.25, 61.3080068527, 7.8777423487)
                CenterArc((-9, 0), 1.25, 69.1857492014, 42.197330799)
                CenterArc((-9, 0), 1.25, 111.3830800004, 7.3011180699)
                CenterArc((-9, 0), 1.25, 118.6841980704, 8.1856995755)
            make_face()
            # Profile area: 0.2017260137, perimeter: 3.3371846322
            with BuildLine():
                CenterArc((-9, 0), 1.25, 111.3830800004, 7.3011180699)
                CenterArc((-9.0051943222, 1.04639597), 0.4656419803, 15.192272771, 150.1842836599)
                CenterArc((-9, 0), 1.25, 61.3080068527, 7.8777423487)
                CenterArc((-8.9999290448, 1.0430767549), 0.6024301159, 5.0892315969, 169.8137417292)
            make_face()
            # Profile area: 1.6562496931, perimeter: 4.6786166112
            with BuildLine():
                CenterArc((-9, 0), 1.25, 14.2500326978, 38.8800696564)
                CenterArc((-7.5, 1), 0.75, -112.619864948, 292.619864948)
            make_face()
            # Profile area: 0.1108961746, perimeter: 1.7302354415
            with BuildLine():
                CenterArc((-9, 0), 1.25, 126.8698976458, 38.8800696564)
                CenterArc((-10.5, 1), 0.75, -67.380135052, 67.380135052)
            make_face()
            # Profile area: 0.1108961746, perimeter: 1.7302354415
            with BuildLine():
                CenterArc((-7.5, 1), 0.75, -180, 67.380135052)
                CenterArc((-9, 0), 1.25, 14.2500326978, 38.8800696564)
            make_face()
        # OneSide extrude, distance=0.6
        extrude(amount=0.6)
    return part.part


# Description: This is a long, narrow structural beam or rail with a horizontal, elongated rectangular profile featuring internal ribbing or reinforcing slots along its length and angled end flanges on both sides.
def model_34327_81dcda78_0001():
    """Model: Parte media"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 35 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 71, perimeter: 121
            with BuildLine():
                Line((-15, -1), (-15, -2))
                Line((-15, -2), (15, -2))
                Line((15, -2), (15, -1))
                Line((13, -1), (15, -1))
                Line((13, 1), (13, -1))
                Line((15, 1), (13, 1))
                Line((15, 1), (15, 2))
                Line((15, 2), (-15, 2))
                Line((-15, 2), (-15, 1))
                Line((-15, 1), (-13.5, 1))
                Line((-13.5, 1), (-13.5, -1))
                Line((-13.5, -1), (-15, -1))
            make_face()
            with BuildLine():
                Line((-10.5, -1), (-10.5, 1))
                Line((-10.5, 1), (10.5, 1))
                Line((10.5, 1), (10.5, -1))
                Line((10.5, -1), (-10.5, -1))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 35 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 31.9992805325, perimeter: 78.0180117218
            with BuildLine():
                Line((10.5, -1), (-10.5, -1))
                Line((10.5, 1), (10.5, -1))
                Line((-10.5, 1), (10.5, 1))
                Line((-10.5, -1), (-10.5, 1))
            make_face()
            with BuildLine():
                Line((-7.6789125761, -0.3255903544), (-7.6789125761, 0.3255903544))
                Line((-7.6789125761, 0.3255903544), (7.6789125761, 0.3255903544))
                Line((7.6789125761, 0.3255903544), (7.6789125761, -0.3255903544))
                Line((7.6789125761, -0.3255903544), (-7.6789125761, -0.3255903544))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)

        # Sketch1 -> Extrude3 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 35 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3, perimeter: 7
            with BuildLine():
                Line((-15, 1), (-15, -1))
                Line((-16.5, 1), (-15, 1))
                Line((-16.5, -1), (-16.5, 1))
                Line((-15, -1), (-16.5, -1))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch1 -> Extrude4 (Join)
        # Sketch on XZ construction plane
        # Sketch has 35 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3, perimeter: 7
            with BuildLine():
                Line((-13.5, -1), (-15, -1))
                Line((-13.5, 1), (-13.5, -1))
                Line((-15, 1), (-13.5, 1))
                Line((-15, 1), (-15, -1))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)
    return part.part


# Description: This is a hexagonal prism or box-like geometric solid with a rounded top edge and angular faceted surfaces, featuring a multi-sided structure with flat faces and subtle curved transitions along the upper perimeter.
def model_34327_81dcda78_0008():
    """Model: Sujeccion parte inf"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 9, perimeter: 12
            with BuildLine():
                Line((1.5, -1.5), (-1.5, -1.5))
                Line((1.5, 1.5), (1.5, -1.5))
                Line((-1.5, 1.5), (1.5, 1.5))
                Line((-1.5, -1.5), (-1.5, 1.5))
            make_face()
        # OneSide extrude, distance=3
        extrude(amount=3)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(1.5, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.2146018366, perimeter: 3.5707963268
            with BuildLine():
                Line((1.5, 2), (1.5, 3))
                Line((0.5, 3), (1.5, 3))
                CenterArc((0.5, 2), 1, 0, 90)
            make_face()
        # OneSide extrude, distance=-3
        extrude(amount=-3, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical threaded insert or coupling nut with a knurled hexagonal head and vertical fluting along the body, designed for fastening or joining applications.
def model_34330_5eff1ee1_0008():
    """Model: Component9"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0011044662, perimeter: 0.3534291735
            with BuildLine():
                CenterArc((0, 0), 0.03125, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.025, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0019634954, perimeter: 0.1570796327
            Circle(0.025)
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

        # Sketch1 -> Extrude3 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0019634954, perimeter: 0.1570796327
            Circle(0.025)
        # OneSide extrude, distance=0.15
        extrude(amount=0.15, mode=Mode.SUBTRACT)
    return part.part


# Description: This is an elongated rectangular base plate or mounting bracket with a dark finish, featuring a curved top surface, rounded corners, and what appears to be mounting holes or slots along its length for fastening purposes.
def model_34330_5eff1ee1_0014():
    """Model: Component3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0209817477, perimeter: 1.1141592654
            with BuildLine():
                CenterArc((0, -0.025), 0.025, 90, 180)
                Line((0.4, -0.05), (0, -0.05))
                CenterArc((0.4, -0.025), 0.025, -90, 180)
                Line((0, 0), (0.4, 0))
            make_face()
            with BuildLine():
                CenterArc((0.35, -0.025), 0.0125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0.4, -0.025), 0.0125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.025
        extrude(amount=-0.025)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0031309292, perimeter: 0.281681409
            with BuildLine():
                CenterArc((0, 0.025), 0.013, -90, 180)
                Line((0, 0.038), (-0.1, 0.038))
                CenterArc((-0.1, 0.025), 0.013, 90, 180)
                Line((0, 0.012), (-0.1, 0.012))
            make_face()
        # OneSide extrude, distance=-0.009
        extrude(amount=-0.009, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a hex bolt consisting of a hexagonal head (shown in blue) with a textured cylindrical shaft extending downward, featuring a threaded section along its length for fastening applications.
def model_34346_d3e86e1e_0000():
    """Model: Component1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 0.0259807621, perimeter: 0.6
            with BuildLine():
                Line((0.05, 0.0866025404), (0.1, 0))
                Line((-0.05, 0.0866025404), (0.05, 0.0866025404))
                Line((-0.1, 0), (-0.05, 0.0866025404))
                Line((-0.05, -0.0866025404), (-0.1, 0))
                Line((0.05, -0.0866025404), (-0.05, -0.0866025404))
                Line((0.1, 0), (0.05, -0.0866025404))
            make_face()
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 0.0078539816, perimeter: 0.3141592654
            Circle(0.05)
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)
    return part.part


# Description: This is a rectangular duct or channel component with a elongated box-like shape, featuring vertical slot openings or louvers along its sides and angled end caps at both the top and bottom.
def model_34436_ffc43a58_0001():
    """Model: columna"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 8 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(1, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.7500000313, perimeter: 4.0000000417
            with BuildLine():
                Line((0.3500000037, 0.2), (0.3700000037, 0.2))
                Line((0.3700000037, 0.2), (0.5500000037, 0.2))
                Line((0.5500000037, 0.2), (0.5500000037, 1.7))
                Line((0.0499999829, 1.7), (0.5500000037, 1.7))
                Line((0.0499999829, 0.2), (0.0499999829, 1.7))
                Line((0.2299999963, 0.2), (0.0499999829, 0.2))
                Line((0.2499999829, 0.2), (0.2299999963, 0.2))
                Line((0.2499999829, 0.2), (0.3500000037, 0.2))
            make_face()
            # Profile area: 0.020000001, perimeter: 0.6828427336
            with BuildLine():
                Line((0.2499999829, 0.2), (0.3500000037, 0.2))
                Line((0.2358578539, 0.1858578711), (0.2499999829, 0.2))
                Line((0.1499999844, 0.1000000015), (0.2358578539, 0.1858578711))
                Line((0.1499999844, 0.1000000015), (0.4500000022, 0.1000000015))
                Line((0.4500000022, 0.1000000015), (0.3641421393, 0.1858578644))
                Line((0.3641421393, 0.1858578644), (0.3500000037, 0.2))
            make_face()
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -0.5500000037), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            with Locations((-0.7500000112, 1.5000000224)):
                Circle(0.1)
        # OneSide extrude, distance=-0.6
        extrude(amount=-0.6, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a flat, parallelogram-shaped panel or plate with a blue surface featuring an internal triangulated or truss-like structural pattern, likely designed for lightweight rigidity.
def model_34520_035b5e9a_0002():
    """Model: WS2812_led_strip"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.5, perimeter: 5
            with BuildLine():
                Line((0, 1), (0, 0))
                Line((0, 0), (1.5, 0))
                Line((1.5, 0), (1.5, 1))
                Line((1.5, 1), (0, 1))
            make_face()
        # OneSide extrude, distance=0.03
        extrude(amount=0.03)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 27 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.03, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0176714587, perimeter: 0.471238898
            with BuildLine():
                CenterArc((-1.3000000194, -0.7500000119), 0.075, -89.9805323659, 179.9805323659)
                CenterArc((-1.3000000194, -0.7500000119), 0.075, 90, 180.0194676341)
            make_face()
            # Profile area: 0.0123218896, perimeter: 0.8648540013
            with BuildLine():
                CenterArc((-1.1000000194, -0.7500000119), 0.075, 90, 177.5802527548)
                Line((-1.3000000194, -0.6750000119), (-1.1000000194, -0.6750000119))
                CenterArc((-1.3000000194, -0.7500000119), 0.075, -89.9805323659, 179.9805323659)
                Line((-1.1031665196, -0.8249331373), (-1.2999745363, -0.8250000076))
            make_face()
            # Profile area: 0.0176711694, perimeter: 0.4712369693
            with BuildLine():
                CenterArc((-1.1000000194, -0.7500000119), 0.075, -87.5413174866, 177.5413174866)
                CenterArc((-1.1000000194, -0.7500000119), 0.075, 90, 177.5802527548)
                Line((-1.0967825992, -0.8249309682), (-1.1031665196, -0.8249331373))
            make_face()
            # Profile area: 0.0176714587, perimeter: 0.471238898
            with BuildLine():
                CenterArc((-1.1000000194, -0.5000000119), 0.075, 90, 180)
                CenterArc((-1.1000000194, -0.5000000119), 0.075, -90, 180)
            make_face()
            # Profile area: 0.0176714587, perimeter: 0.471238898
            with BuildLine():
                CenterArc((-1.3000000194, -0.5000000119), 0.075, -90, 180)
                CenterArc((-1.3000000194, -0.5000000119), 0.075, 90, 180)
            make_face()
            # Profile area: 0.0123285413, perimeter: 0.871238898
            with BuildLine():
                Line((-1.1000000194, -0.4250000119), (-1.3000000194, -0.4250000119))
                CenterArc((-1.3000000194, -0.5000000119), 0.075, -90, 180)
                Line((-1.3000000194, -0.5750000119), (-1.1000000194, -0.5750000119))
                CenterArc((-1.1000000194, -0.5000000119), 0.075, 90, 180)
            make_face()
            # Profile area: 0.0176714587, perimeter: 0.471238898
            with BuildLine():
                CenterArc((-1.1000000194, -0.2500000119), 0.075, 90, 180)
                CenterArc((-1.1000000194, -0.2500000119), 0.075, -90, 180)
            make_face()
            # Profile area: 0.0123285413, perimeter: 0.871238898
            with BuildLine():
                CenterArc((-1.3000000194, -0.2500000119), 0.075, -90, 180)
                Line((-1.1000000194, -0.3250000119), (-1.3000000194, -0.3250000119))
                CenterArc((-1.1000000194, -0.2500000119), 0.075, 90, 180)
                Line((-1.1000000194, -0.1750000119), (-1.3000000194, -0.1750000119))
            make_face()
            # Profile area: 0.0176714587, perimeter: 0.471238898
            with BuildLine():
                CenterArc((-1.3000000194, -0.2500000119), 0.075, 90, 180)
                CenterArc((-1.3000000194, -0.2500000119), 0.075, -90, 180)
            make_face()
        # OneSide extrude, distance=0.02
        extrude(amount=0.02, mode=Mode.ADD)

        # Sketch2 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 27 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.03, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.25, perimeter: 2
            with BuildLine():
                Line((-0.6054861337, -0.2479823584), (-0.1054861337, -0.2479823584))
                Line((-0.6054861337, -0.7479823584), (-0.6054861337, -0.2479823584))
                Line((-0.1054861337, -0.7479823584), (-0.6054861337, -0.7479823584))
                Line((-0.1054861337, -0.2479823584), (-0.1054861337, -0.7479823584))
            make_face()
        # OneSide extrude, distance=-0.005
        extrude(amount=-0.005, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a tapered, elongated coffin or casket-shaped CAD part with a hexagonal cross-section that narrows toward one end, featuring a curved lid section and a flat base with angular faceted surfaces throughout.
def model_34521_49e7972b_0003():
    """Model: Component4"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(1.6000000238, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))) as sk:
            # Profile area: 3.6231022746, perimeter: 11.7177655753
            with BuildLine():
                Line((1.2183338438, -3), (-0.0002482173, -3))
                Line((1.2183338438, -2), (1.2183338438, -3))
                Line((-4, -2), (1.2183338438, -2))
                Line((-4, -2.2023347168), (-4, -2))
                Line((-4, -2.2023347168), (-0.0002482173, -3))
            make_face()
        # TwoSides extrude, along=-1.4, against=0.2
        extrude(amount=-1.4)
        extrude(sk.sketch, amount=0.2)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 8 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -3, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.8199503382, perimeter: 8.5995036728
            with BuildLine():
                Line((0.400000006, 0.0002482173), (0.2000000238, 0.0002482173))
                Line((0.400000006, 4.1000000611), (0.400000006, 0.0002482173))
                Line((0.200000003, 4.1000000611), (0.400000006, 4.1000000611))
                Line((0.2000000238, 0.0002482173), (0.200000003, 4.1000000611))
            make_face()
            # Profile area: 0.2437163904, perimeter: 2.8371640863
            with BuildLine():
                Line((0.400000006, 0.0002482173), (0.400000006, -1.2183338438))
                Line((0.400000006, 0.0002482173), (0.2000000238, 0.0002482173))
                Line((0.2000000238, 0.0002482173), (0.2000000238, -1.2183338438))
                Line((0.2000000238, -1.2183338438), (0.400000006, -1.2183338438))
            make_face()
            # Profile area: 0.0363332341, perimeter: 0.7633323393
            with BuildLine():
                Line((0.2000000238, -1.2183338438), (0.400000006, -1.2183338438))
                Line((0.200000003, -1.4000000209), (0.2000000238, -1.2183338438))
                Line((0.400000006, -1.4000000209), (0.200000003, -1.4000000209))
                Line((0.400000006, -1.2183338438), (0.400000006, -1.4000000209))
            make_face()
            # Profile area: 0.2437164122, perimeter: 2.837164122
            with BuildLine():
                Line((1.8000000238, 0.0002482173), (1.6000000238, 0.0002482173))
                Line((1.6000000238, 0.0002482173), (1.6000000238, -1.2183338438))
                Line((1.6000000238, -1.2183338438), (1.8000000238, -1.2183338438))
                Line((1.8000000238, -1.2183338438), (1.8000000238, 0.0002482173))
            make_face()
            # Profile area: 0.8199503749, perimeter: 8.5995036907
            with BuildLine():
                Line((1.8000000268, 4.1000000611), (1.6000000238, 4.1000000611))
                Line((1.6000000238, 4.1000000611), (1.6000000238, 0.0002482173))
                Line((1.8000000238, 0.0002482173), (1.6000000238, 0.0002482173))
                Line((1.8000000238, 0.0002482173), (1.8000000268, 4.1000000611))
            make_face()
            # Profile area: 0.0363332357, perimeter: 0.7633323572
            with BuildLine():
                Line((1.6000000238, -1.2183338438), (1.8000000238, -1.2183338438))
                Line((1.6000000238, -1.2183338438), (1.6000000238, -1.4000000209))
                Line((1.6000000238, -1.4000000209), (1.8000000268, -1.4000000209))
                Line((1.8000000268, -1.4000000209), (1.8000000238, -1.2183338438))
            make_face()
        # OneSide extrude, distance=-0.8
        extrude(amount=-0.8, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical ring or bushing with a uniform circular cross-section, featuring a large central hollow bore and a textured or knurled surface finish on its outer walls.
def model_34532_066f48a3_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch3 -> Extrude3 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 6.1145981989, perimeter: 31.8041371591
            with BuildLine():
                CenterArc((11, 6), 2.7231507694, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((11, 6), 2.3386348702, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=1
        extrude(amount=1, both=True)
    return part.part


# Description: This is a hexagonal or octagonal box-like enclosure with a mesh or perforated panel on one side, featuring an open framework structure with reinforcing ribs and struts, designed for ventilation or cooling applications.
def model_34570_2041f80b_0003():
    """Model: Pieza 8"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.015784641, perimeter: 1.0862523404
            with BuildLine():
                CenterArc((0, 0), 0.551, -176.7247668747, 53.4495337494)
                Line((-0.5501, -0.0314799936), (-0.5501, -0.3176003831))
                Line((-0.5501, -0.3176003831), (-0.3023124742, -0.4606605778))
            make_face()
            # Profile area: 0.6401548545, perimeter: 5.4463733721
            with BuildLine():
                CenterArc((0, 0), 0.551, 123.2752331253, 53.4495337494)
                Line((-0.5501, 0.0314799936), (-0.5501, -0.0314799936))
                CenterArc((0, 0), 0.551, -176.7247668747, 53.4495337494)
                Line((-0.3023124742, -0.4606605778), (-0.2477875258, -0.4921405714))
                CenterArc((0, 0), 0.551, -116.7247668747, 53.4495337494)
                Line((0.2477875258, -0.4921405714), (0.3023124742, -0.4606605778))
                CenterArc((0, 0), 0.551, -56.7247668747, 53.4495337494)
                Line((0.5501, -0.0314799936), (0.5501, 0.0314799936))
                CenterArc((0, 0), 0.551, 3.2752331253, 53.4495337494)
                Line((0.3023124742, 0.4606605778), (0.2477875258, 0.4921405714))
                CenterArc((0, 0), 0.551, 63.2752331253, 53.4495337494)
                Line((-0.2477875258, 0.4921405714), (-0.3023124742, 0.4606605778))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.31585, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.015784641, perimeter: 1.0862523404
            with BuildLine():
                CenterArc((0, 0), 0.551, 3.2752331253, 53.4495337494)
                Line((0.5501, 0.0314799936), (0.5501, 0.3176003831))
                Line((0.5501, 0.3176003831), (0.3023124742, 0.4606605778))
            make_face()
            # Profile area: 0.015784641, perimeter: 1.0862523404
            with BuildLine():
                CenterArc((0, 0), 0.551, 63.2752331253, 53.4495337494)
                Line((0.2477875258, 0.4921405714), (0, 0.6352007662))
                Line((0, 0.6352007662), (-0.2477875258, 0.4921405714))
            make_face()
            # Profile area: 0.015784641, perimeter: 1.0862523404
            with BuildLine():
                Line((-0.5501, 0.3176003831), (-0.5501, 0.0314799936))
                CenterArc((0, 0), 0.551, 123.2752331253, 53.4495337494)
                Line((-0.3023124742, 0.4606605778), (-0.5501, 0.3176003831))
            make_face()
            # Profile area: 0.0384342445, perimeter: 3.8434244524
            with BuildLine():
                CenterArc((0, 0), 0.31585, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.29585, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.015784641, perimeter: 1.0862523404
            with BuildLine():
                CenterArc((0, 0), 0.551, -116.7247668747, 53.4495337494)
                Line((-0.2477875258, -0.4921405714), (0, -0.6352007662))
                Line((0, -0.6352007662), (0.2477875258, -0.4921405714))
            make_face()
            # Profile area: 0.015784641, perimeter: 1.0862523404
            with BuildLine():
                CenterArc((0, 0), 0.551, -56.7247668747, 53.4495337494)
                Line((0.3023124742, -0.4606605778), (0.5501, -0.3176003831))
                Line((0.5501, -0.3176003831), (0.5501, -0.0314799936))
            make_face()
        # OneSide extrude, distance=0.55
        extrude(amount=0.55)
    return part.part


# Description: This is a flexible hose or conduit connector with a U-shaped bend, featuring a ribbed/corrugated exterior surface with blue accent markings, and a rigid cylindrical attachment point at the top.
def model_34678_f709cdcc_0005():
    """Model: Gancho"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 14 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.29838957, perimeter: 7.4123064539
            with BuildLine():
                CenterArc((-10.0165813732, 0.8366185187), 0.75, 119.3068104777, 235.5479925041)
                CenterArc((-8.7716180827, 0.72451854), 0.5, 135.2141200464, 39.6406829354)
                CenterArc((-9.1619774839, 1.1119711666), 0.05, -44.7858799536, 140.5960258982)
                CenterArc((-9.1062996259, 0.5647966276), 0.6, 95.8101459447, 67.563549368)
                CenterArc((-10.0165813732, 0.8366185187), 0.35, 119.3068104777, 224.0668848349)
                CenterArc((-10.5550160909, 1.795830724), 0.75, -60.6931895223, 68.6769491427)
                Line((-10.2208772634, 1.9000000283), (-9.8122854829, 1.9000000283))
                CenterArc((-10.5550160909, 1.795830724), 0.35, -60.6931895223, 78.0082953972)
            make_face()
        # OneSide extrude, distance=0.4
        extrude(amount=0.4)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.9000000283, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0353429174, perimeter: 0.771238898
            with BuildLine():
                CenterArc((-0.2, 9.8122854829), 0.15, 0, 180)
                Line((-0.35, 9.8122854829), (-0.05, 9.8122854829))
            make_face()
            # Profile area: 0.0353429174, perimeter: 0.771238898
            with BuildLine():
                Line((-0.35, 9.8122854829), (-0.05, 9.8122854829))
                CenterArc((-0.2, 9.8122854829), 0.15, 180, 180)
            make_face()
        # OneSide extrude, distance=0.9
        extrude(amount=0.9, mode=Mode.ADD)
    return part.part


# Description: This is a hexagonal or polyhedron-shaped enclosure or housing with a complex geometric form featuring multiple flat faceted surfaces, internal geometric structures, and what appears to be cutouts or apertures on its surfaces.
def model_34678_f709cdcc_0007():
    """Model: Tuerca ranurada"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1753598559, perimeter: 1.5588
            with BuildLine():
                Line((1.7299000238, -1.4249934178), (1.8598000238, -1.2000000179))
                Line((1.8598000238, -1.2000000179), (1.7299000238, -0.975006618))
                Line((1.7299000238, -0.975006618), (1.4701000238, -0.975006618))
                Line((1.4701000238, -0.975006618), (1.3402000238, -1.2000000179))
                Line((1.3402000238, -1.2000000179), (1.4701000238, -1.4249934178))
                Line((1.4701000238, -1.4249934178), (1.7299000238, -1.4249934178))
            make_face()
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.3, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0490873852, perimeter: 0.7853981634
            with Locations((-1.6000000238, 1.2000000179)):
                Circle(0.125)
        # OneSide extrude, distance=-0.6
        extrude(amount=-0.6, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a complex geometric container or enclosure with an irregular pentagonal base, featuring multiple angled faceted surfaces, a recessed top opening, and internal structural geometry suggesting it may be a protective cover, housing, or vessel component.
def model_34689_969a9743_0005():
    """Model: Component12"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 23603.9546137589, perimeter: 650.6128622747
            with BuildLine():
                Line((-455.2719605092, 127.4657667061), (-239.2135586655, 127.4657667061))
                Line((-455.2719605092, 18.2177374125), (-455.2719605092, 127.4657667061))
                Line((-239.2135586655, 18.2177374125), (-455.2719605092, 18.2177374125))
                Line((-239.2135586655, 127.4657667061), (-239.2135586655, 18.2177374125))
            make_face()
        # TwoSides extrude (symmetric), distance=100
        extrude(amount=100, both=True)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(100, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))) as sk:
            # Profile area: 9762.8417783899, perimeter: 597.3659832337
            with BuildLine():
                Line((-239.2135586655, 127.4657667061), (-455.2719605092, 127.4657667061))
                Line((-246.1400140929, 190.0968512879), (-239.2135586655, 127.4657667061))
                CenterArc((-270.9885217494, 187.3488215856), 25, 6.3107724299, 109.1037892832)
                Line((-455.2719605092, 127.4657667061), (-281.7176393011, 209.929477833))
            make_face()
            with BuildLine():
                CenterArc((-270.9885217494, 187.3488215856), 12.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # TwoSides offset extrude, full=-150, trim=-50
        extrude(amount=-150, mode=Mode.ADD)
        extrude(sk.sketch, amount=-50, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical standoff or spacer with a threaded or knurled upper section and a broad rectangular base flange for mounting to a surface.
def model_34699_5d3a78f6_0004():
    """Model: short screw v1 (2)"""
    with BuildPart() as part:
        # Sketch4 -> Extrude2 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1514644313, perimeter: 3.2162288849
            with BuildLine():
                Line((0.0845299474, -0.3154700585), (0.3154700585, -0.0845299474))
                Line((0.3154700585, -0.0845299474), (0.2309401111, 0.2309401111))
                Line((0.2309401111, 0.2309401111), (-0.0845299474, 0.3154700585))
                Line((-0.0845299474, 0.3154700585), (-0.3154700585, 0.0845299474))
                Line((-0.3154700585, 0.0845299474), (-0.2309401111, -0.2309401111))
                Line((-0.2309401111, -0.2309401111), (0.0845299474, -0.3154700585))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)

        # Sketch5 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))) as sk:
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            Circle(0.2)
        # TwoSides extrude, along=0.9, against=-0.1
        extrude(amount=0.9, mode=Mode.ADD)
        extrude(sk.sketch, amount=-0.1, mode=Mode.ADD)
    return part.part


# Description: This is a hex head bolt featuring a long cylindrical shaft with a hexagonal head at the base, designed for fastening applications.
def model_34699_5d3a78f6_0007():
    """Model: short screw v1"""
    with BuildPart() as part:
        # Sketch4 -> Extrude2 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1514644313, perimeter: 3.2162288849
            with BuildLine():
                Line((0.0845299474, -0.3154700585), (0.3154700585, -0.0845299474))
                Line((0.3154700585, -0.0845299474), (0.2309401111, 0.2309401111))
                Line((0.2309401111, 0.2309401111), (-0.0845299474, 0.3154700585))
                Line((-0.0845299474, 0.3154700585), (-0.3154700585, 0.0845299474))
                Line((-0.3154700585, 0.0845299474), (-0.2309401111, -0.2309401111))
                Line((-0.2309401111, -0.2309401111), (0.0845299474, -0.3154700585))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)

        # Sketch5 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))) as sk:
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            Circle(0.2)
        # TwoSides extrude, along=3.2, against=-0.1
        extrude(amount=3.2, mode=Mode.ADD)
        extrude(sk.sketch, amount=-0.1, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical filter or strainer component with a mesh or perforated top section mounted on a rectangular base, designed for fluid filtration or separation applications.
def model_34699_5d3a78f6_0012():
    """Model: short screw v1 (4)"""
    with BuildPart() as part:
        # Sketch4 -> Extrude2 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1514644313, perimeter: 3.2162288849
            with BuildLine():
                Line((0.0845299474, -0.3154700585), (0.3154700585, -0.0845299474))
                Line((0.3154700585, -0.0845299474), (0.2309401111, 0.2309401111))
                Line((0.2309401111, 0.2309401111), (-0.0845299474, 0.3154700585))
                Line((-0.0845299474, 0.3154700585), (-0.3154700585, 0.0845299474))
                Line((-0.3154700585, 0.0845299474), (-0.2309401111, -0.2309401111))
                Line((-0.2309401111, -0.2309401111), (0.0845299474, -0.3154700585))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)

        # Sketch5 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))) as sk:
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            Circle(0.2)
        # TwoSides extrude, along=0.5, against=-0.1
        extrude(amount=0.5, mode=Mode.ADD)
        extrude(sk.sketch, amount=-0.1, mode=Mode.ADD)
    return part.part


# Description: This is a fastener bolt or stud with a cylindrical shaft and a hexagonal head at the base, featuring a threaded end for secure fastening applications.
def model_34699_5d3a78f6_0013():
    """Model: short screw v1 (1)"""
    with BuildPart() as part:
        # Sketch4 -> Extrude2 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1514644313, perimeter: 3.2162288849
            with BuildLine():
                Line((0.0845299474, -0.3154700585), (0.3154700585, -0.0845299474))
                Line((0.3154700585, -0.0845299474), (0.2309401111, 0.2309401111))
                Line((0.2309401111, 0.2309401111), (-0.0845299474, 0.3154700585))
                Line((-0.0845299474, 0.3154700585), (-0.3154700585, 0.0845299474))
                Line((-0.3154700585, 0.0845299474), (-0.2309401111, -0.2309401111))
                Line((-0.2309401111, -0.2309401111), (0.0845299474, -0.3154700585))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)

        # Sketch5 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))) as sk:
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            Circle(0.2)
        # TwoSides extrude, along=4.6, against=-0.1
        extrude(amount=4.6, mode=Mode.ADD)
        extrude(sk.sketch, amount=-0.1, mode=Mode.ADD)
    return part.part


# Description: This is a hammer consisting of a long cylindrical dark gray shaft with a geometric blue head at the top featuring an angular, faceted striking surface.
def model_34773_9f1fecc8_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.0106192983, perimeter: 5.0265482457
            Circle(0.8)
        # OneSide extrude, distance=8
        extrude(amount=8)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 8, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.9776870275, perimeter: 13.3403921221
            with BuildLine():
                Line((0.692820323, 1.2), (-0.692820323, 1.2))
                Line((-0.692820323, 1.2), (-1.3856406461, 0))
                Line((-1.3856406461, 0), (-0.692820323, -1.2))
                Line((-0.692820323, -1.2), (0.692820323, -1.2))
                Line((0.692820323, -1.2), (1.3856406461, 0))
                Line((1.3856406461, 0), (0.692820323, 1.2))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.8, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 2.0106192983, perimeter: 5.0265482457
            Circle(0.8)
        # OneSide extrude, distance=1.02
        extrude(amount=1.02, mode=Mode.ADD)
    return part.part


# Description: This is an aerodynamic housing or fairing with an elongated, streamlined shape featuring a dark gray outer shell, a blue transparent or translucent panel insert, and internal cross-bracing or support ribs visible through the transparent section.
def model_34781_4f8a4759_0008():
    """Model: Past v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 8.4106192983, perimeter: 13.0265482457
            with BuildLine():
                CenterArc((-4.9962435495, 0.7), 0.8, 90, 180)
                Line((-4.9962435495, -0.1), (-0.9962435495, -0.1))
                CenterArc((-0.9962435495, 0.7), 0.8, -90, 180)
                Line((-0.9962435495, 1.5), (-4.9962435495, 1.5))
            make_face()
        # OneSide extrude, distance=0.15
        extrude(amount=0.15)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.15, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((4.9962435495, -0.7)):
                Circle(0.25)
        # OneSide extrude, distance=0.05
        extrude(amount=0.05, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical socket or hollow bit with a tapered top end, a uniform tubular body, and a hexagonal or square drive shaft at the bottom for attachment to a power tool.
def model_34781_4f8a4759_0009():
    """Model: Ajs v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 4 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.3000000056, perimeter: 2.6000000373
            with BuildLine():
                Line((-0.15, 1.0000000373), (-0.15, 0.0000000373))
                Line((-0.15, 0.0000000373), (0.15, 0))
                Line((0.15, 0), (0.15, 1.0000000373))
                Line((0.15, 1.0000000373), (-0.15, 1.0000000373))
            make_face()
        # Symmetric extrude, each_side=0.1
        extrude(amount=0.1, both=True)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.0000000373, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.4426548246, perimeter: 3.5132741229
            with BuildLine():
                CenterArc((0, 0), 0.4, 0, 360)
            make_face()
            with BuildLine():
                Line((-0.15, 0.1), (-0.15, -0.1))
                Line((0.15, 0.1), (-0.15, 0.1))
                Line((0.15, -0.1), (0.15, 0.1))
                Line((-0.15, -0.1), (0.15, -0.1))
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.06, perimeter: 1
            with BuildLine():
                Line((-0.15, -0.1), (0.15, -0.1))
                Line((0.15, -0.1), (0.15, 0.1))
                Line((0.15, 0.1), (-0.15, 0.1))
                Line((-0.15, 0.1), (-0.15, -0.1))
            make_face()
        # OneSide extrude, distance=1.2
        extrude(amount=1.2, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical fastener or connector with a threaded head at the top and a smooth cylindrical shaft, appearing to be a bolt, stud, or similar mechanical component.
def model_34781_4f8a4759_0018():
    """Model: Tor v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1590431281, perimeter: 1.4137166941
            Circle(0.225)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            Circle(0.15)
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)
    return part.part


MODELS = {
    "model_30297_fd93a92a_0002": {"func": model_30297_fd93a92a_0002, "volume": 1.0584120692, "area": 8.3080974371},
    "model_30379_f1d5e193_0001": {"func": model_30379_f1d5e193_0001, "volume": 0.0557405006, "area": 1.315368166},
    "model_30379_f1d5e193_0003": {"func": model_30379_f1d5e193_0003, "volume": 0.0006367103, "area": 0.049382297},
    "model_30379_f1d5e193_0011": {"func": model_30379_f1d5e193_0011, "volume": 0.0030480619, "area": 0.1799875958},
    "model_30379_f1d5e193_0012": {"func": model_30379_f1d5e193_0012, "volume": 0.0002462537, "area": 0.0345660712},
    "model_30380_4d422f95_0001": {"func": model_30380_4d422f95_0001, "volume": 88.8534325441, "area": 264.002254784},
    "model_30380_4d422f95_0003": {"func": model_30380_4d422f95_0003, "volume": 761.934908567, "area": 767.4844708188},
    "model_30400_8824ce97_0013": {"func": model_30400_8824ce97_0013, "volume": 8.4705191922, "area": 35.8298642142},
    "model_30402_c83c8794_0007": {"func": model_30402_c83c8794_0007, "volume": 4.095179266, "area": 19.0623747103},
    "model_30417_0010bc7c_0003": {"func": model_30417_0010bc7c_0003, "volume": 9.032, "area": 60.44},
    "model_30424_e6ca5ede_0000": {"func": model_30424_e6ca5ede_0000, "volume": 1062807.45507822, "area": 62032.100335479},
    "model_30426_2cde26de_0027": {"func": model_30426_2cde26de_0027, "volume": 340.8730088816, "area": 663.7672563597},
    "model_30445_791b6800_0012": {"func": model_30445_791b6800_0012, "volume": 0.1853539666, "area": 3.9584067435},
    "model_30447_4ed3b778_0002": {"func": model_30447_4ed3b778_0002, "volume": 0.0774510434, "area": 1.3036200653},
    "model_30447_4ed3b778_0004": {"func": model_30447_4ed3b778_0004, "volume": 0.5574851075, "area": 5.8480809289},
    "model_30447_4ed3b778_0009": {"func": model_30447_4ed3b778_0009, "volume": 0.0423438655, "area": 0.8915294641},
    "model_30447_4ed3b778_0012": {"func": model_30447_4ed3b778_0012, "volume": 35.9108066838, "area": 177.7056631027},
    "model_30447_4ed3b778_0015": {"func": model_30447_4ed3b778_0015, "volume": 0.9086524753, "area": 9.9659727929},
    "model_30447_4ed3b778_0021": {"func": model_30447_4ed3b778_0021, "volume": 0.2155491479, "area": 3.0376361516},
    "model_30643_be4a0dae_0000": {"func": model_30643_be4a0dae_0000, "volume": 0.3926990817, "area": 3.5342917353},
    "model_30708_4282508b_0001": {"func": model_30708_4282508b_0001, "volume": 88.1403598701, "area": 262.3616554566},
    "model_30729_b4d83b07_0015": {"func": model_30729_b4d83b07_0015, "volume": 1655.1105873453, "area": 11067.2696959536},
    "model_30729_b4d83b07_0016": {"func": model_30729_b4d83b07_0016, "volume": 2411.4192003022, "area": 16101.7872932981},
    "model_30729_b4d83b07_0019": {"func": model_30729_b4d83b07_0019, "volume": 1526.4101145773, "area": 10203.1842440023},
    "model_30845_630b097e_0000": {"func": model_30845_630b097e_0000, "volume": 0.8935219567, "area": 9.3785618973},
    "model_30855_9deadbdd_0000": {"func": model_30855_9deadbdd_0000, "volume": 22683.7481669681, "area": 16340.1003393246},
    "model_30904_54099e05_0002": {"func": model_30904_54099e05_0002, "volume": 36.4424747816, "area": 148.2831732494},
    "model_30904_54099e05_0010": {"func": model_30904_54099e05_0010, "volume": 72.1610705501, "area": 155.645031159},
    "model_30904_54099e05_0014": {"func": model_30904_54099e05_0014, "volume": 129.3011518014, "area": 230.2772475513},
    "model_30904_54099e05_0019": {"func": model_30904_54099e05_0019, "volume": 4841.8447744959, "area": 5651.7681036383},
    "model_30905_511b96bf_0001": {"func": model_30905_511b96bf_0001, "volume": 16.5926712783, "area": 45.2203921223},
    "model_30905_511b96bf_0005": {"func": model_30905_511b96bf_0005, "volume": 182.2123739082, "area": 263.8937829015},
    "model_30905_511b96bf_0014": {"func": model_30905_511b96bf_0014, "volume": 19197.435683956, "area": 8589.4385989323},
    "model_30974_a9e13c20_0001": {"func": model_30974_a9e13c20_0001, "volume": 10.2058011864, "area": 129.9150072706},
    "model_30993_b95934d0_0000": {"func": model_30993_b95934d0_0000, "volume": 74.631005746, "area": 145.6289931784},
    "model_30999_4fe3a732_0001": {"func": model_30999_4fe3a732_0001, "volume": 4224.8315863792, "area": 6725.350930956},
    "model_31008_8fa25b35_0014": {"func": model_31008_8fa25b35_0014, "volume": 27.6243702997, "area": 134.4623072671},
    "model_31011_7f51c882_0000": {"func": model_31011_7f51c882_0000, "volume": 0.4101593907, "area": 4.5467214492},
    "model_31013_d34d1b29_0007": {"func": model_31013_d34d1b29_0007, "volume": 1906.4647286233, "area": 1106.3319597724},
    "model_31108_e89804a2_0001": {"func": model_31108_e89804a2_0001, "volume": 9.7455902834, "area": 248.0661579224},
    "model_31136_987852a4_0006": {"func": model_31136_987852a4_0006, "volume": 0.2474004215, "area": 4.633849164},
    "model_31277_b1263495_0001": {"func": model_31277_b1263495_0001, "volume": 12.8510720334, "area": 77.2170716665},
    "model_31277_b1263495_0003": {"func": model_31277_b1263495_0003, "volume": 4.413749709, "area": 19.4275903829},
    "model_31280_c8bd4b11_0001": {"func": model_31280_c8bd4b11_0001, "volume": 39.7550689184, "area": 158.4119056807},
    "model_31280_c8bd4b11_0008": {"func": model_31280_c8bd4b11_0008, "volume": 33.7658378408, "area": 180.5159138753},
    "model_31360_a1accb4b_0006": {"func": model_31360_a1accb4b_0006, "volume": 0.0787648355, "area": 2.7677111475},
    "model_31462_84375249_0002": {"func": model_31462_84375249_0002, "volume": 16701.737875622, "area": 8023.7016524236},
    "model_31463_c4c75dd7_0003": {"func": model_31463_c4c75dd7_0003, "volume": 5.3321335859, "area": 18.0171578674},
    "model_31464_b2855e3a_0006": {"func": model_31464_b2855e3a_0006, "volume": 634.1793768, "area": 850.8143395196},
    "model_31615_bab70c5e_0000": {"func": model_31615_bab70c5e_0000, "volume": 591.7818081567, "area": 566.0521643238},
    "model_31627_2cb7b72a_0000": {"func": model_31627_2cb7b72a_0000, "volume": 0.3637306696, "area": 3.1869734859},
    "model_31664_1e85c690_0000": {"func": model_31664_1e85c690_0000, "volume": 1079.7632280481, "area": 791.9323123923},
    "model_31730_e8a4bbd6_0000": {"func": model_31730_e8a4bbd6_0000, "volume": 10.1054597454, "area": 207.9250576203},
    "model_31744_086479d0_0000": {"func": model_31744_086479d0_0000, "volume": 67.0900025249, "area": 97.4095487498},
    "model_31866_a5b1db64_0002": {"func": model_31866_a5b1db64_0002, "volume": 0.9738937226, "area": 7.4769905155},
    "model_31866_a5b1db64_0008": {"func": model_31866_a5b1db64_0008, "volume": 0.699593414, "area": 11.3686384152},
    "model_31962_e5291336_0013": {"func": model_31962_e5291336_0013, "volume": 0.0524395482, "area": 1.0874920399},
    "model_31962_e5291336_0017": {"func": model_31962_e5291336_0017, "volume": 1.0164507828, "area": 11.0574446786},
    "model_31962_e5291336_0043": {"func": model_31962_e5291336_0043, "volume": 1.4778051842, "area": 17.4169896715},
    "model_31962_e5291336_0047": {"func": model_31962_e5291336_0047, "volume": 1.3191354498, "area": 12.5455142363},
    "model_31962_e5291336_0052": {"func": model_31962_e5291336_0052, "volume": 0.0465938768, "area": 1.1394535641},
    "model_31968_b384541d_0001": {"func": model_31968_b384541d_0001, "volume": 3.4361169649, "area": 15.3152641863},
    "model_32161_15a0a149_0000": {"func": model_32161_15a0a149_0000, "volume": 12.4681958439, "area": 63.2245521535},
    "model_32169_c6811fb2_0000": {"func": model_32169_c6811fb2_0000, "volume": 0.00484219, "area": 0.2088929739},
    "model_32169_c6811fb2_0001": {"func": model_32169_c6811fb2_0001, "volume": 0.0076770546, "area": 0.3040692816},
    "model_32219_e5edc7ce_0034": {"func": model_32219_e5edc7ce_0034, "volume": 2.0224002707, "area": 13.1161493287},
    "model_32219_e5edc7ce_0039": {"func": model_32219_e5edc7ce_0039, "volume": 85.4098890901, "area": 215.8630259354},
    "model_32220_1fd19c5e_0003": {"func": model_32220_1fd19c5e_0003, "volume": 18.087719703, "area": 65.0937997824},
    "model_32220_1fd19c5e_0025": {"func": model_32220_1fd19c5e_0025, "volume": 0.0212057504, "area": 0.4241150082},
    "model_32220_1fd19c5e_0027": {"func": model_32220_1fd19c5e_0027, "volume": 1.3246391118, "area": 22.0773185307},
    "model_32220_1fd19c5e_0036": {"func": model_32220_1fd19c5e_0036, "volume": 4.4610617947, "area": 27.7088476372},
    "model_32439_3d5a17cf_0000": {"func": model_32439_3d5a17cf_0000, "volume": 124.434736434, "area": 267.0601579372},
    "model_32879_49552f2f_0012": {"func": model_32879_49552f2f_0012, "volume": 5.1737647025, "area": 22.773519779},
    "model_32879_49552f2f_0013": {"func": model_32879_49552f2f_0013, "volume": 1.8750924162, "area": 12.4062640222},
    "model_32879_49552f2f_0018": {"func": model_32879_49552f2f_0018, "volume": 3.3620356268, "area": 15.5681726957},
    "model_32879_49552f2f_0019": {"func": model_32879_49552f2f_0019, "volume": 3.9171276411, "area": 17.7469715333},
    "model_33265_e489d292_0000": {"func": model_33265_e489d292_0000, "volume": 4.7664336216, "area": 58.6395729999},
    "model_33607_c6f31fa6_0036": {"func": model_33607_c6f31fa6_0036, "volume": 43.2076908958, "area": 243.7764915031},
    "model_33625_c9ff9be8_0000": {"func": model_33625_c9ff9be8_0000, "volume": 1186.4283197365, "area": 2635.9123817457},
    "model_33625_c9ff9be8_0002": {"func": model_33625_c9ff9be8_0002, "volume": 1640, "area": 1212},
    "model_33625_c9ff9be8_0003": {"func": model_33625_c9ff9be8_0003, "volume": 765.7345175426, "area": 665.1327412287},
    "model_33655_f8991a06_0000": {"func": model_33655_f8991a06_0000, "volume": 0.192309558, "area": 2.4203336866},
    "model_33655_f8991a06_0001": {"func": model_33655_f8991a06_0001, "volume": 0.1774627673, "area": 2.3317093578},
    "model_33785_a4c23f61_0002": {"func": model_33785_a4c23f61_0002, "volume": 33.1192598757, "area": 92.522835454},
    "model_33967_0741e236_0001": {"func": model_33967_0741e236_0001, "volume": 1.8146259169, "area": 9.3585036675},
    "model_33967_0741e236_0002": {"func": model_33967_0741e236_0002, "volume": 1.593562417, "area": 10.5523469129},
    "model_33967_0741e236_0003": {"func": model_33967_0741e236_0003, "volume": 4.4888923146, "area": 23.7768078551},
    "model_33991_aaf84876_0014": {"func": model_33991_aaf84876_0014, "volume": 244.2, "area": 1092.92},
    "model_34063_0ca1585e_0001": {"func": model_34063_0ca1585e_0001, "volume": 3.1711436542, "area": 42.9055982056},
    "model_34063_0ca1585e_0002": {"func": model_34063_0ca1585e_0002, "volume": 1.0317455095, "area": 9.0350946657},
    "model_34222_5121da73_0000": {"func": model_34222_5121da73_0000, "volume": 32.8273439543, "area": 78.4617688249},
    "model_34226_dbed877f_0005": {"func": model_34226_dbed877f_0005, "volume": 40.2439423452, "area": 148.2661262434},
    "model_34227_48203345_0008": {"func": model_34227_48203345_0008, "volume": 517500, "area": 104200},
    "model_34227_48203345_0011": {"func": model_34227_48203345_0011, "volume": 137200, "area": 25920},
    "model_34323_d1617369_0000": {"func": model_34323_d1617369_0000, "volume": 5.0537783526, "area": 26.741830212},
    "model_34327_81dcda78_0001": {"func": model_34327_81dcda78_0001, "volume": 92.9996402663, "area": 332.0075669259},
    "model_34327_81dcda78_0008": {"func": model_34327_81dcda78_0008, "volume": 26.3561944902, "area": 52.2831853072},
    "model_34330_5eff1ee1_0008": {"func": model_34330_5eff1ee1_0008, "volume": 0.0001549321, "area": 0.0495782591},
    "model_34330_5eff1ee1_0014": {"func": model_34330_5eff1ee1_0014, "volume": 0.0004963653, "area": 0.0723526097},
    "model_34346_d3e86e1e_0000": {"func": model_34346_d3e86e1e_0000, "volume": 0.0096666597, "area": 0.3947048631},
    "model_34436_ffc43a58_0001": {"func": model_34436_ffc43a58_0001, "volume": 0.3692920525, "area": 4.0327488366},
    "model_34520_035b5e9a_0002": {"func": model_34520_035b5e9a_0002, "volume": 0.0466101487, "area": 3.2122743144},
    "model_34521_49e7972b_0003": {"func": model_34521_49e7972b_0003, "volume": 4.7651893836, "area": 25.6421903303},
    "model_34532_066f48a3_0000": {"func": model_34532_066f48a3_0000, "volume": 12.2291963978, "area": 75.837470716},
    "model_34570_2041f80b_0003": {"func": model_34570_2041f80b_0003, "volume": 0.4253133199, "area": 4.665140624},
    "model_34678_f709cdcc_0005": {"func": model_34678_f709cdcc_0005, "volume": 0.5829730793, "area": 6.4806175728},
    "model_34678_f709cdcc_0007": {"func": model_34678_f709cdcc_0007, "volume": 0.0378817412, "area": 0.9558043904},
    "model_34689_969a9743_0005": {"func": model_34689_969a9743_0005, "volume": 5697075.1005907618, "area": 213381.0831938679},
    "model_34699_5d3a78f6_0004": {"func": model_34699_5d3a78f6_0004, "volume": 0.1408101493, "area": 1.8811888126},
    "model_34699_5d3a78f6_0007": {"func": model_34699_5d3a78f6_0007, "volume": 0.4298366734, "area": 4.7714540539},
    "model_34699_5d3a78f6_0012": {"func": model_34699_5d3a78f6_0012, "volume": 0.0905446668, "area": 1.378533988},
    "model_34699_5d3a78f6_0013": {"func": model_34699_5d3a78f6_0013, "volume": 0.605765862, "area": 6.5307459399},
    "model_34773_9f1fecc8_0000": {"func": model_34773_9f1fecc8_0000, "volume": 21.1730268387, "area": 58.6691193714},
    "model_34781_4f8a4759_0008": {"func": model_34781_4f8a4759_0008, "volume": 1.2714103718, "area": 18.8537606498},
    "model_34781_4f8a4759_0009": {"func": model_34781_4f8a4759_0009, "volume": 0.6631857906, "area": 5.0212386152},
    "model_34781_4f8a4759_0018": {"func": model_34781_4f8a4759_0018, "volume": 0.0865901475, "area": 1.4019357217},
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
