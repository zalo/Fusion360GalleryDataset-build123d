"""Batch 012 - passing/01_2ops
206 models bundled from Fusion360 Gallery reconstructions.
"""

from build123d import *
from build123d import Edge, BuildLine
from collections import Counter
from OCP.BRepBuilderAPI import BRepBuilderAPI_MakeEdge
from OCP.Geom import Geom_BSplineCurve
from OCP.TColStd import TColStd_Array1OfReal, TColStd_Array1OfInteger
from OCP.TColgp import TColgp_Array1OfPnt
from OCP.gp import gp_Pnt


# Description: This is a belt pulley or drive belt component with an oval/elliptical overall shape, featuring a textured outer surface, a central slot or groove running along its length, and a hollow interior cavity designed to interface with a shaft or drive mechanism.
def model_40999_cad6be09_0011():
    """Model: Steering wheel"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 17 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 684.0550967816, perimeter: 359.0840403053
            with BuildLine():
                CenterArc((-131.6053554604, 97.6364215289), 30.48, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-131.6053554604, 97.6364215289), 26.67, -75.8496898245, 64.399157196)
                CenterArc((-131.6053554604, 97.6364215289), 26.67, -98.1361823999, 22.2864925754)
                CenterArc((-131.6053554604, 97.6364215289), 26.67, -168.3084115105, 70.1722291106)
                CenterArc((-131.6053554604, 97.6364215289), 26.67, 173.5653981753, 18.1261903142)
                CenterArc((-131.6053554604, 97.6364215289), 26.67, 6.0478473848, 167.5175507905)
                CenterArc((-131.6053554604, 97.6364215289), 26.67, -11.4505326286, 17.4983800134)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 103.0030014604, perimeter: 61.8441666317
            with BuildLine():
                Line((-140.3909506672, 98.9948827397), (-158.1073456644, 100.6253034646))
                CenterArc((-131.6053554604, 97.6364215289), 26.67, 173.5653981753, 18.1261903142)
                Line((-140.0900769419, 94.9828199421), (-157.7220215284, 92.2319184534))
                CenterArc((-131.6053554604, 97.6364215289), 8.89, 171.2103229484, 26.1567807391)
            make_face()
            with BuildLine():
                Line((-154.9400049448, 96.5200030804), (-152.3999977112, 97.7899985313))
                Line((-152.3999977112, 97.7899985313), (-148.5899977684, 96.5199985504))
                Line((-148.5899977684, 96.5199985504), (-152.3999977112, 95.2499985695))
                Line((-152.3999977112, 95.2499985695), (-154.9400049448, 96.5200030804))
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 122.6085618763, perimeter: 64.0047672364
            with BuildLine():
                CenterArc((-131.6053554604, 97.6364215289), 8.89, -98.0564832247, 27.8883299291)
                Line((-132.8512823596, 88.8341623778), (-135.3798647012, 71.2348689232))
                CenterArc((-131.6053554604, 97.6364215289), 26.67, -98.1361823999, 22.2864925754)
                Line((-128.589326615, 89.2736665998), (-125.0854328054, 71.7756499129))
            make_face()
            with BuildLine():
                Line((-130.3400782248, 74.3848867537), (-131.6100782248, 77.5598867537))
                Line((-130.3400782248, 80.7348867537), (-131.6100782248, 77.5598867537))
                Line((-130.3400782248, 80.7348867537), (-129.0700782248, 77.5598867537))
                Line((-130.3400782248, 74.3848867537), (-129.0700782248, 77.5598867537))
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 104.4856454614, perimeter: 62.0573545947
            with BuildLine():
                Line((-123.2072326033, 94.7203226832), (-105.4661826755, 92.3418444804))
                CenterArc((-131.6053554604, 97.6364215289), 26.67, -11.4505326286, 17.4983800134)
                Line((-122.8501693153, 99.1787624655), (-105.0837938139, 100.4463446291))
                CenterArc((-131.6053554604, 97.6364215289), 8.89, -19.1486486683, 29.1395431695)
            make_face()
            with BuildLine():
                Line((-111.2520035505, 97.7900031209), (-108.2040034533, 96.5200030804))
                Line((-111.2520035505, 95.2500030398), (-108.2040034533, 96.5200030804))
                Line((-114.5540036559, 96.5200030804), (-111.2520035505, 95.2500030398))
                Line((-111.2520035505, 97.7900031209), (-114.5540036559, 96.5200030804))
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 121.6097949834, perimeter: 95.7557440814
            with BuildLine():
                CenterArc((-131.6053554604, 97.6364215289), 8.89, -19.1486486683, 29.1395431695)
                CenterArc((-131.6053554604, 97.6364215289), 8.89, 9.9908945012, 161.2194284473)
                CenterArc((-131.6053554604, 97.6364215289), 8.89, 171.2103229484, 26.1567807391)
                CenterArc((-131.6053554604, 97.6364215289), 8.89, -162.6328963125, 64.5764130878)
                CenterArc((-131.6053554604, 97.6364215289), 8.89, -98.0564832247, 27.8883299291)
                CenterArc((-131.6053554604, 97.6364215289), 8.89, -70.1681532956, 51.0195046273)
            make_face()
            with BuildLine():
                CenterArc((-131.6053554604, 97.6364215289), 6.35, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=5.08
        extrude(amount=5.08)
    return part.part


# Description: This is a cylindrical capsule or pill-shaped part with rounded hemispherical ends and a hollow cylindrical body, featuring a central axial hole or bore running through its entire length.
def model_40999_cad6be09_0012():
    """Model: Steering wheel axle"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 126.6768697744, perimeter: 39.8982267006
            with Locations((76.1999988556, 63.4999990463)):
                Circle(6.35)
        # OneSide extrude, distance=-27.94
        extrude(amount=-27.94)
    return part.part


# Description: This is a cylindrical rod or pin with rounded ends, featuring a simple linear shape with a uniform diameter throughout its length.
def model_40999_cad6be09_0013():
    """Model: Antenna"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 5.067074791, perimeter: 7.9796453401
            with Locations((108.1406176805, 54.0703088403)):
                Circle(1.27)
        # OneSide extrude, distance=76.2
        extrude(amount=76.2)
    return part.part


# Description: This is a cylindrical rod or shaft with a tapered end, featuring a uniform circular cross-section throughout its length with slightly rounded or beveled ends.
def model_40999_cad6be09_0015():
    """Model: Tire 1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 102.6082645172, perimeter: 35.9084040305
            with Locations((135.3975609666, 94.0628848203)):
                Circle(5.715)
        # OneSide extrude, distance=215.9
        extrude(amount=215.9)
    return part.part


# Description: These are two cylindrical rods or shafts with rounded ends, appearing to be simple mechanical components with a smooth, uniform diameter throughout their length.
def model_40999_cad6be09_0016():
    """Model: Headrest connector"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 5.067074791, perimeter: 7.9796453401
            with Locations((-66.3877151968, -58.6789150496)):
                Circle(1.27)
            # Profile area: 5.067074791, perimeter: 7.9796453401
            with Locations((-42.2577151968, -58.6789150496)):
                Circle(1.27)
        # OneSide extrude, distance=-25.4
        extrude(amount=-25.4)
    return part.part


# Description: This is a cylindrical tube or barrel with a solid circular end face and an open or mesh-patterned top surface, featuring a uniform diameter and smooth curved walls.
def model_40999_cad6be09_0020():
    """Model: Door Handle"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 151.672491064, perimeter: 43.6574476431
            with Locations((241.299996376, 139.6999979019)):
                Circle(6.9482985952)
        # OneSide extrude, distance=12.7
        extrude(amount=12.7)
    return part.part


# Description: This is a hexagonal prism or hex bar stock, a long structural component with a uniform hexagonal cross-section and no additional features or modifications.
def model_40999_cad6be09_0022():
    """Model: Gas pedal connector"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 6.4515890571, perimeter: 10.1599913836
            with BuildLine():
                Line((-55.8800017834, 73.6600023508), (-58.4199991226, 73.6599988937))
                Line((-58.4199991226, 73.6599988937), (-58.4199991226, 71.1200022697))
                Line((-58.4199991226, 71.1200022697), (-55.8800017834, 71.1200022697))
                Line((-55.8800017834, 71.1200022697), (-55.8800017834, 73.6600023508))
            make_face()
        # OneSide extrude, distance=-22.86
        extrude(amount=-22.86)
    return part.part


# Description: This is an ergonomic handle or grip component featuring an elongated teardrop shape with a thumb loop at the top, internal ribbing for structural support, and a tapered design that transitions from a wider grip section to a narrower tail end.
def model_41010_212b5129_0000():
    """Model: bottleopener_10"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 32 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.8772440726, perimeter: 14.2319544875
            with BuildLine():
                CenterArc((1.7394289564, -3.4000000522), 0.1, -90, 62.4074763696)
                Line((1.828055359, -3.4463180914), (2.1599969558, -2.8111705324))
                CenterArc((1.9827441506, -2.7185344539), 0.2, -27.5925236304, 27.5925236304)
                Line((2.1827441506, -0.3642797769), (2.1827441506, -2.7185344539))
                CenterArc((2.3827441506, -0.3642797769), 0.2, 160.7264550852, 19.2735449148)
                CenterArc((1.25, 0.0318145165), 1, -19.2735449148, 277.2488466072)
                CenterArc((1.0000000179, -1.1418549467), 0.2, 0, 77.9753016924)
                Line((1.2000000179, -1.7747139022), (1.2000000179, -1.1418549467))
                CenterArc((1.2190000179, -1.7747139022), 0.019, -180, 123.4504075436)
                Line((1.2705996599, -1.7633968924), (1.229473103, -1.7905668038))
                CenterArc((1.1603566584, -1.5965242444), 0.2, -56.5495924564, 66.3862090796)
                CenterArc((1.5329517636, -1.5319206448), 0.1781543832, -36.9518629155, 226.7884795386)
                CenterArc((1.9750000238, -1.864445993), 0.375, 143.0481370845, 36.9518629155)
                Line((1.6000000238, -2.7000000417), (1.6000000238, -1.864445993))
                CenterArc((1.5000000238, -2.7000000417), 0.1, -90, 90)
                Line((1.3000000179, -2.8000000417), (1.5000000238, -2.8000000417))
                CenterArc((1.3000000179, -2.9000000417), 0.1, 90, 90)
                Line((1.2000000179, -3.1585786908), (1.2000000179, -2.9000000417))
                CenterArc((1.3000000179, -3.1585786908), 0.1, -180, 44.9999999289)
                Line((1.2292893397, -3.2292893688), (1.4707107005, -3.4707107302))
                CenterArc((1.5414213787, -3.4000000522), 0.1, -135.0000000711, 45.0000000711)
                Line((1.7394289564, -3.5000000522), (1.5414213787, -3.5000000522))
            make_face()
            with BuildLine():
                CenterArc((1.25, 0.0318145165), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.05
        extrude(amount=0.05)
    return part.part


# Description: This is a ski or snowboard with an elongated, tapered oval shape featuring a blue central body with black tip and tail sections, designed for snow sports with curved edges and a streamlined profile.
def model_41010_212b5129_0003():
    """Model: knifeplate_3"""
    with BuildPart() as part:
        # Sketch3 -> Extrude2 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 17 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 16.9180253666, perimeter: 25.1154788234
            with BuildLine():
                CenterArc((2.2898398215, 0.0446164204), 0.01, -90, 90.5509294465)
                CenterArc((1.2498878995, 0.0346164204), 1.05, 0.5509294465, 179.4490705535)
                Line((0.1998878995, 0.0346164204), (0.1998878995, -7.4653835796))
                CenterArc((1.2498878995, -7.4653835796), 1.05, 180, 180)
                Line((2.2998878995, -7.4653835796), (2.2998878995, -6.4100000954))
                CenterArc((2.2898878995, -6.4100000954), 0.01, 0, 90)
                Line((2.2500000298, -6.4000000954), (2.2898878995, -6.4000000954))
                CenterArc((2.2500000298, -6.1500000954), 0.25, -180, 90)
                Line((2.0000000298, -0.2153835796), (2.0000000298, -6.1500000954))
                CenterArc((2.2500000298, -0.2153835796), 0.25, 90, 90)
                Line((2.2898398215, 0.0346164204), (2.2500000298, 0.0346164204))
            make_face()
            with BuildLine():
                CenterArc((1.2498878995, -7.4653835796), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1.2498878995, 0.0346164204), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.05
        extrude(amount=0.05)
    return part.part


# Description: This is a ski or snowboard featuring a long, tapered rectangular body with a blue core, black top and bottom surfaces, and upturned tips at both ends for snow performance.
def model_41010_212b5129_0004():
    """Model: sawbladeplate_5 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude3 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 13 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 15.2086671136, perimeter: 25.5277863374
            with BuildLine():
                CenterArc((1.25, 0), 1.05, 0, 180)
                Line((0.2, -7.5), (0.2, 0))
                CenterArc((1.25, -7.5), 1.05, 180, 180)
                Line((2.3, -6.5007337709), (2.3, -7.5))
                Line((2.1330465247, -6.5004409797), (2.3, -6.5007337709))
                CenterArc((2.1337480153, -6.1004415949), 0.4, 180, 89.8995188209)
                Line((1.7337480153, -0.3999999998), (1.7337480153, -6.1004415949))
                CenterArc((2.1337480153, -0.3999999998), 0.4, 90.0000000035, 89.9999999965)
                Line((2.3, 0), (2.1337480153, 0.0000000002))
            make_face()
            with BuildLine():
                CenterArc((1.25, -7.5), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1.25, 0), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.05
        extrude(amount=0.05)
    return part.part


# Description: This is a curved reinforcement bracket or duct connector with a bent rectangular profile, featuring a mesh or perforated pattern on one side and a smooth surface on the other, designed to bend at approximately 90 degrees.
def model_41010_212b5129_0006():
    """Model: keychainhook_15"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0195009947, perimeter: 1.2771072123
            with BuildLine():
                CenterArc((1.2468807641, 1.1446796812), 0.2605307129, 18.1570450013, 143.9981695941)
                CenterArc((1.25, 0), 1.25, 99.275466543, 2.3136991317)
                CenterArc((1.2488510621, 1.1656401394), 0.211559249, 18.8664953249, 142.3799589144)
                CenterArc((1.25, 0), 1.25, 78.723093922, 2.1143890992)
            make_face()
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


# Description: This is a flat, diamond-shaped structural frame or mounting plate featuring a perimeter flange with curved corners, internal cross-braced lattice framework, and multiple rectangular cutouts or slots arranged symmetrically across the central area.
def model_41010_212b5129_0007():
    """Model: logo_14"""
    with BuildPart() as part:
        # Sketch1 -> Extrude2 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 45 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.3294635052, perimeter: 5.6995575182
            with BuildLine():
                CenterArc((1.5250000238, -1.5250000238), 0.075, -90, 90)
                Line((1.6000000238, -0.9750000134), (1.6000000238, -1.5250000238))
                CenterArc((1.5250000238, -0.9750000134), 0.075, 0, 90)
                Line((0.9750000134, -0.9000000134), (1.5250000238, -0.9000000134))
                CenterArc((0.9750000134, -0.9750000134), 0.075, 90, 90)
                Line((0.9000000134, -1.5250000238), (0.9000000134, -0.9750000134))
                CenterArc((0.9750000134, -1.5250000238), 0.075, 180, 90)
                Line((1.5250000238, -1.6000000238), (0.9750000134, -1.6000000238))
            make_face()
            with BuildLine():
                Line((1.5500000231, -1.3500000201), (1.5500000231, -1.5000000231))
                CenterArc((1.5000000231, -1.5000000231), 0.05, -90, 90)
                Line((1.5000000231, -1.5500000231), (1.3500000201, -1.5500000231))
                Line((1.3500000201, -1.4000000201), (1.3500000201, -1.5500000231))
                CenterArc((1.4000000201, -1.4000000201), 0.05, 90, 90)
                Line((1.5500000231, -1.3500000201), (1.4000000201, -1.3500000201))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((1.3500000201, -0.9500000142), (1.5000000231, -0.9500000142))
                CenterArc((1.5000000231, -1.0000000142), 0.05, 0, 90)
                Line((1.5500000231, -1.0000000142), (1.5500000231, -1.1500000171))
                Line((1.4000000201, -1.1500000171), (1.5500000231, -1.1500000171))
                CenterArc((1.4000000201, -1.1000000171), 0.05, -180, 90)
                Line((1.3500000201, -0.9500000142), (1.3500000201, -1.1000000171))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((0.9500000142, -1.1500000171), (0.9500000142, -1.0000000142))
                CenterArc((1.0000000142, -1.0000000142), 0.05, 90, 90)
                Line((1.0000000142, -0.9500000142), (1.1500000171, -0.9500000142))
                Line((1.1500000171, -1.1000000171), (1.1500000171, -0.9500000142))
                CenterArc((1.1000000171, -1.1000000171), 0.05, -90, 90)
                Line((0.9500000142, -1.1500000171), (1.1000000171, -1.1500000171))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((1.1500000171, -1.5500000231), (1.0000000142, -1.5500000231))
                CenterArc((1.0000000142, -1.5000000231), 0.05, -180, 90)
                Line((0.9500000142, -1.5000000231), (0.9500000142, -1.3500000201))
                Line((1.1000000171, -1.3500000201), (0.9500000142, -1.3500000201))
                CenterArc((1.1000000171, -1.4000000201), 0.05, 0, 90)
                Line((1.1500000171, -1.5500000231), (1.1500000171, -1.4000000201))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.05
        extrude(amount=0.05)
    return part.part


# Description: This is a pen or stylus with an elongated tapered body featuring a dark oval grip section near the pointed tip and a blue-tinted shaft that narrows toward the fine point.
def model_41010_212b5129_0009():
    """Model: file_12"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 10 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.6000627175, perimeter: 15.8681254133
            with BuildLine():
                Line((1.6482274356, -5.0348857341), (1.6686404621, -4.9924301775))
                CenterArc((-1.2378531252, -3.5949610267), 3.225, -25.6786804862, 19.2096702753)
                Line((2.2000000328, -1.9000000283), (1.9666131031, -3.9583082324))
                Line((2.2000000328, -0.3122497152), (2.2000000328, -1.9000000283))
                CenterArc((1.2499999721, 0), 1, -18.1948611966, 301.3963593956)
                CenterArc((1.5240515653, -1.1682875178), 0.2, 5.1618927149, 98.0396054841)
                Line((1.7232404568, -1.1502934778), (1.7981673561, -1.9797128873))
                CenterArc((1.5989784645, -1.9977069272), 0.2, -6.4690102109, 11.6309029257)
                Line((1.5854498637, -3.8921812306), (1.7977050523, -2.0202400873))
                CenterArc((4.9886426798, -4.2780615963), 3.425, 173.5309897891, 18.8489968599)
                Line((1.6482274356, -5.0348857341), (1.6432834323, -5.0123616064))
            make_face()
            with BuildLine():
                CenterArc((1.2499999721, 0), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.025
        extrude(amount=0.025)
    return part.part


# Description: A long, slender pry bar with a curved claw head at one end and a flat, angled tip at the opposite end, designed for leverage and prying applications.
def model_41010_212b5129_0010():
    """Model: sidepanel_13"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 8 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.2225663103, perimeter: 22.6256631033
            with BuildLine():
                Line((1.25, 1.05), (1.25, 1.25))
                CenterArc((1.25, 0), 1.25, 90, 90)
                Line((0, -7.5), (0, 0))
                CenterArc((1.25, -7.5), 1.25, -180, 90)
                Line((1.25, -8.55), (1.25, -8.75))
                CenterArc((1.25, -7.5), 1.05, 180, 90)
                Line((0.2, 0), (0.2, -7.5))
                CenterArc((1.25, 0), 1.05, 90, 90)
            make_face()
        # OneSide extrude, distance=0.73
        extrude(amount=0.73)
    return part.part


# Description: This is a cylindrical rubber or foam roller/tube with a slightly tapered or rounded top end and a uniform hollow cylindrical body, commonly used as a protective sleeve, grip, or handling component.
def model_41010_212b5129_0011():
    """Model: pin2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((1.2500000186, 0)):
                Circle(0.15)
        # OneSide extrude, distance=1.2
        extrude(amount=1.2)
    return part.part


# Description: This is a streamlined elongated component with a tapered, pointed nose cone at one end, a flat bottom surface with two circular holes, and a curved aerodynamic profile typical of a skis or aircraft fairing.
def model_41010_212b5129_0012():
    """Model: midplate_7"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 10 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 18.8209068189, perimeter: 24.7389372261
            with BuildLine():
                CenterArc((1.25, -7.4681854835), 1.05, 180, 180)
                Line((2.3, -7.4681854835), (2.3, 0.0318145165))
                CenterArc((1.25, 0.0318145165), 1.05, 0, 180)
                Line((0.2, 0.0318145165), (0.2, -7.4681854835))
            make_face()
            with BuildLine():
                CenterArc((1.25, -7.4681854835), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1.25, 0.0318145165), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.05
        extrude(amount=0.05)
    return part.part


# Description: This is a streamlined pen or stylus featuring an elongated tapered body with a rounded grip section at the handle end, a pointed tip, and textured ribbed detailing along the barrel for ergonomic grip.
def model_41010_212b5129_0014():
    """Model: smallknife_8"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 9 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 5.6824055663, perimeter: 13.4148967819
            with BuildLine():
                Line((1.0639025221, -1.1396228937), (1.0011720645, -1.4077339262))
                CenterArc((3.0946344465, -1.8975453747), 2.15, 166.8312825318, 35.0839676766)
                Line((1.1000000164, -2.7000000402), (1.6687623407, -4.1137533193))
                CenterArc((1.6826783949, -4.1081547983), 0.015, -158.0847497916, 126.9687854744)
                CenterArc((-1.6375339289, -2.1040127076), 3.8931948629, -31.1159643172, 51.8966771829)
                CenterArc((2.189378801, -0.6517788616), 0.2, 145.7731176595, 55.0075952062)
                CenterArc((1.246228302, -0.0101673489), 0.9407007483, -34.2268823405, 284.6608641407)
                CenterArc((0.8616229536, -1.0922951512), 0.2077424826, -13.1687174682, 83.6026992684)
            make_face()
            with BuildLine():
                CenterArc((1.246228302, -0.0101673489), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.025
        extrude(amount=0.025)
    return part.part


# Description: This is an elongated ski or hydrofoil with a streamlined, tapered design featuring a blue central body, dark gray end caps with mounting holes, and vertical fin-like structures along the sides for hydrodynamic performance.
def model_41010_212b5129_0015():
    """Model: smallknifeplate_9"""
    with BuildPart() as part:
        # Sketch4 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 16 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 17.8945318428, perimeter: 25.0861513971
            with BuildLine():
                Line((2.2461264663, -0.5291937891), (2.2500000298, -0.5292647787))
                CenterArc((2.2470426472, -0.4792021837), 0.05, -91.0499247574, 90.7185231401)
                Line((2.2999999924, 0.0319407343), (2.2970418108, -0.4794913845))
                CenterArc((1.25, 0.0318145165), 1.05, 0.0068873748, 179.9931126251)
                Line((0.2, 0.0318145165), (0.2, -7.4681854835))
                CenterArc((1.25, -7.4681854835), 1.05, 180, 180)
                Line((2.3, -7.4681854835), (2.3, -3.7500000551))
                CenterArc((2.25, -3.7500000551), 0.05, 0, 90.0114250045)
                CenterArc((2.2500000298, -3.4500000551), 0.25, 180, 89.9977081689)
                Line((2.0000000298, -0.7792647787), (2.0000000298, -3.4500000551))
                CenterArc((2.2500000298, -0.7792647787), 0.25, 90, 90)
            make_face()
            with BuildLine():
                CenterArc((1.25, -7.4681854835), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1.25, 0.0318145165), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.05
        extrude(amount=0.05)
    return part.part


# Description: This is a fin or hydrofoil component with an elongated, streamlined shape featuring a tapered design, curved aerodynamic profile, and dark end caps or mounting points at both extremities.
def model_41010_212b5129_0016():
    """Model: fileplate_11"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 21 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 17.1802174652, perimeter: 25.5542699174
            with BuildLine():
                CenterArc((1.2502407333, -7.4999829623), 1.0502407333, -180, 181.7349734498)
                Line((2.3, -3.8999132476), (2.3, -7.4681854835))
                CenterArc((2.25, -3.8999132476), 0.05, 0, 90.0090433946)
                Line((2.1000631601, -3.8499369126), (2.2499921081, -3.8499132483))
                CenterArc((2.1000000253, -3.4499369176), 0.4, 180, 90.0090433946)
                Line((1.7000000253, -1.4000000149), (1.7000000253, -3.4499369176))
                CenterArc((2.1000000253, -1.4000000149), 0.4, 90, 90)
                Line((2.2500401694, -1.0000000149), (2.1000000253, -1.0000000149))
                CenterArc((2.2500401694, -0.9500000149), 0.05, -90, 90)
                Line((2.3000401694, 0.0000050305), (2.3000401694, -0.9500000149))
                CenterArc((1.2497791742, 0.0000050305), 1.0502609952, 0, 178.2644046907)
                Line((0.2, -7.4999829623), (0.2, 0.0318145165))
            make_face()
            with BuildLine():
                CenterArc((1.2502407333, -7.4999829623), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1.2497791742, 0.0000050305), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.05
        extrude(amount=0.05)
    return part.part


# Description: This is a hexagonal steel shaft or tool blank with a long, slender prismatic body featuring a uniform hexagonal cross-section and tapered or chamfered ends for tool insertion or connection purposes.
def model_41026_295d1dc8_0002():
    """Model: Component1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 3 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 696.7728, perimeter: 198.12
            with BuildLine():
                Line((0, 0), (91.44, 0))
                Line((91.44, 7.62), (91.44, 0))
                Line((0, 7.62), (91.44, 7.62))
                Line((0, 0), (0, 7.62))
            make_face()
        # OneSide extrude, distance=7.62
        extrude(amount=7.62)
    return part.part


# Description: This is a flexible connector or bellows-type coupling with an hourglass or figure-eight shape, featuring two enlarged cylindrical end sections connected by a narrow waisted middle section with vertical ribbing or fluting for flexibility and articulation.
def model_41032_ed481084_0003():
    """Model: Legs"""
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
            # Profile area: 319.631572736, perimeter: 93.8835005638
            with BuildLine():
                Line((45.7199998474, -7.62), (35.5599998474, -7.62))
                _nurbs_edge([(45.7199998474, -7.62), (45.58317685, -7.039692465), (45.2922257552, -5.9349749752), (44.8038836068, -4.4455991812), (44.0485078384, -2.7964679151), (42.9288881595, -1.2904531303), (41.6333540957, -0.3069676015), (40.164251575, 0.2290320006), (38.5290176195, 0.4593734536), (36.7415660562, 0.5912820329), (34.821757682, 0.8430144763), (32.7955499917, 1.4006706942), (30.6950488969, 2.3712470909), (28.5590503346, 3.7329060106), (26.4272803869, 5.3712489094), (24.3343913464, 7.1185349683), (22.304016022, 8.7903499191), (20.3425602545, 10.2228595949), (18.4328894832, 11.3096286478), (16.5273115516, 12.0406532794), (14.5622503063, 12.4682191833), (12.8909225967, 12.6317035976), (11.5586715453, 12.6875826867), (10.6325495968, 12.7), (10.1599998474, 12.7)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1, 1, 1, 1, 1, 1], 5)
                Line((10.1599998474, 0), (10.1599998474, 12.7))
                _nurbs_edge([(35.5599998474, -7.62), (35.5256347847, -7.4604833307), (35.4460232065, -7.1491460698), (35.2939608093, -6.7052279765), (35.0256604275, -6.1597050129), (34.5768889418, -5.554888761), (34.0051164105, -5.024691304), (33.2929835511, -4.5624887073), (32.4140232937, -4.1560139509), (31.3387578773, -3.7897523516), (30.0402746104, -3.4469030929), (28.5000795713, -3.1113928025), (26.7145110501, -2.7699178384), (24.7006476045, -2.4138109282), (22.504861548, -2.0415103146), (20.2047254462, -1.6593432513), (17.8983367671, -1.2791558791), (15.6968339976, -0.9167329135), (13.7160086222, -0.5899909234), (12.0681600788, -0.3172664689), (10.9818141957, -0.1368422025), (10.4480589154, -0.0479879212), (10.2379706315, -0.0129910895), (10.1741557987, -0.0023587048), (10.1599998474, 0)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 0.9736926401, 0.9736926401, 0.9736926401, 0.9736926401, 0.9736926401, 0.9736926401], 5)
            make_face()
        # Symmetric extrude, each_side=2.8575
        extrude(amount=2.8575, both=True)
    return part.part


# Description: This is a flat parallelogram or rhombus-shaped plate with a slightly beveled or chamfered edge, featuring a simple planar design with no holes or complex features.
def model_41032_ed481084_0004():
    """Model: Support"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 57.15, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3753.6072431543, perimeter: 334.4567382046
            with BuildLine():
                Line((29.21, -35.5599994659), (-29.21, -35.5599994659))
                Line((29.21, 35.5599994659), (29.21, -35.5599994659))
                Line((-29.21, 35.5599994659), (29.21, 35.5599994659))
                Line((-29.21, -35.5599994659), (-29.21, 35.5599994659))
            make_face()
            with BuildLine():
                Line((-10.1599998473, 7.6200002036), (-10.1599998473, -7.6200002036))
                CenterArc((0, 0), 12.7, 126.8698987932, 16.2602024127)
                Line((7.6200002035, 10.1599998474), (-7.6200002035, 10.1599998474))
                CenterArc((0, 0), 12.7, 36.8698987924, 16.2602024144)
                Line((10.1599998475, -7.6200002033), (10.1599998475, 7.6200002033))
                CenterArc((0, 0), 12.7, -53.1301012068, 16.2602024144)
                Line((-7.6200002035, -10.1599998474), (7.6200002035, -10.1599998474))
                CenterArc((0, 0), 12.7, -143.1301012059, 16.2602024127)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 401.2230944464, perimeter: 75.3767403409
            with BuildLine():
                CenterArc((0, 0), 12.7, -143.1301012059, 16.2602024127)
                Line((-7.6200002035, -10.1599998474), (7.6200002035, -10.1599998474))
                CenterArc((0, 0), 12.7, -53.1301012068, 16.2602024144)
                Line((10.1599998475, -7.6200002033), (10.1599998475, 7.6200002033))
                CenterArc((0, 0), 12.7, 36.8698987924, 16.2602024144)
                Line((7.6200002035, 10.1599998474), (-7.6200002035, 10.1599998474))
                CenterArc((0, 0), 12.7, 126.8698987932, 16.2602024127)
                Line((-10.1599998473, 7.6200002036), (-10.1599998473, -7.6200002036))
            make_face()
        # OneSide extrude, distance=2.54
        extrude(amount=2.54)
    return part.part


# Description: This is a long, slender extruded channel or rail with a rectangular profile, featuring parallel grooves or ribs running along its length and a notched end detail.
def model_41032_ed481084_0006():
    """Model: Shaft"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 22 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 35.5599994659), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 15.6239659971, perimeter: 23.5587105634
            with BuildLine():
                CenterArc((-23.1139998975, 61.5859338153), 0.254, -0.0000030978, 118.0310201656)
                Line((-23.2333670648, 61.8101379174), (-23.5026337229, 61.6667792636))
                CenterArc((-23.6220008902, 61.8909833657), 0.254, 179.9999969022, 118.0310201656)
                Line((-23.8760007849, 63.8390157386), (-23.8760008902, 61.8909833794))
                CenterArc((-23.6220007849, 63.8390157249), 0.254, 61.9689767366, 118.0310201656)
                Line((-23.2333669507, 63.9198611312), (-23.5026335933, 64.063219814))
                CenterArc((-23.1139997592, 64.1440652203), 0.254, -118.0310232634, 118.0310201656)
                Line((-22.8599996567, 66.0399990082), (-22.8599997592, 64.1440652066))
                Line((-22.8599996567, 66.0399990082), (-26.0349996567, 66.0399990082))
                Line((-26.0349996567, 66.0399990082), (-26.0349997821, 63.721079066))
                Line((-26.0349997821, 63.721079066), (-25.3923659338, 64.0632199162))
                CenterArc((-25.2729987665, 63.8390158142), 0.254, -0.0000030978, 118.0310201656)
                Line((-25.0189988718, 61.8909834412), (-25.0189987665, 63.8390158004))
                CenterArc((-25.2729988718, 61.8909834549), 0.254, -118.0310232634, 118.0310201656)
                Line((-25.6616327059, 61.8101380486), (-25.3923660634, 61.6667793658))
                CenterArc((-25.7809998975, 61.5859339595), 0.254, 61.9689767366, 118.0310201656)
                Line((-26.0349998975, 61.5859339733), (-26.035, 59.69))
                Line((-26.035, 59.69), (-22.86, 59.69))
                Line((-22.8599998975, 61.5859338016), (-22.86, 59.69))
            make_face()
        # OneSide extrude, distance=-71.12
        extrude(amount=-71.12)
    return part.part


# Description: This is a tapered cylindrical shaft or punch with a pointed conical tip at one end and a knurled or textured cylindrical body, commonly used as a center punch, drift pin, or similar hand tool.
def model_41032_ed481084_0008():
    """Model: Table Top Support"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 109.9595469186, perimeter: 94.5324640817
            with BuildLine():
                Line((-76.1999988556, 0), (-114.2999988556, 0))
                CenterArc((-76.1999988556, 12.7), 12.7, -90, 36.8698976458)
                Line((-114.2999988556, 2.54), (-68.5799988556, 2.54))
                Line((-114.2999988556, 0), (-114.2999988556, 2.54))
            make_face()
        # Symmetric extrude, each_side=1.27
        extrude(amount=1.27, both=True)
    return part.part


# Description: This is a cylindrical mesh or perforated filter sleeve with a rounded, slightly tapered barrel shape featuring vertical ribbing or fluting along its surface and an open top rim.
def model_41124_a5855c0d_0004():
    """Model: Hand Wheel Seat"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 10 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(12.4511514476, 5.9746568901, -18.425808749), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.471238898, perimeter: 9.4247779608
            with BuildLine():
                CenterArc((0, 0), 0.8, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.7, -180, 72)
                CenterArc((0, 0), 0.7, 108, 72)
                CenterArc((0, 0), 0.7, 36, 72)
                CenterArc((0, 0), 0.7, -36, 72)
                CenterArc((0, 0), 0.7, -108, 72)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0141371669, perimeter: 0.6654866776
            with BuildLine():
                Line((-0.0618033989, -0.1902113033), (-0.0772542486, -0.2377641291))
                CenterArc((0, 0), 0.2, -180, 72.0000000001)
                Line((-0.2, 0), (-0.25, 0))
                CenterArc((0, 0), 0.25, -180, 72.0000000001)
            make_face()
            # Profile area: 0.0141371669, perimeter: 0.6654866776
            with BuildLine():
                CenterArc((0, 0), 0.2, 108.0000000001, 71.9999999999)
                Line((-0.0618033989, 0.1902113033), (-0.0772542486, 0.2377641291))
                CenterArc((0, 0), 0.25, 108.0000000001, 71.9999999999)
                Line((-0.2, 0), (-0.25, 0))
            make_face()
            # Profile area: 0.0141371669, perimeter: 0.6654866776
            with BuildLine():
                CenterArc((0, 0), 0.25, -107.9999999999, 72)
                Line((0.1618033989, -0.1175570505), (0.2022542486, -0.1469463131))
                CenterArc((0, 0), 0.2, -107.9999999999, 72)
                Line((-0.0618033989, -0.1902113033), (-0.0772542486, -0.2377641291))
            make_face()
            # Profile area: 0.0141371669, perimeter: 0.6654866776
            with BuildLine():
                Line((0.1618033989, 0.1175570505), (0.2022542486, 0.1469463131))
                CenterArc((0, 0), 0.25, 36.0000000001, 72)
                Line((-0.0618033989, 0.1902113033), (-0.0772542486, 0.2377641291))
                CenterArc((0, 0), 0.2, 36.0000000001, 72)
            make_face()
            # Profile area: 0.0141371669, perimeter: 0.6654866776
            with BuildLine():
                CenterArc((0, 0), 0.25, -35.9999999999, 72)
                Line((0.1618033989, 0.1175570505), (0.2022542486, 0.1469463131))
                CenterArc((0, 0), 0.2, -35.9999999999, 72)
                Line((0.1618033989, -0.1175570505), (0.2022542486, -0.1469463131))
            make_face()
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with BuildLine():
                CenterArc((0, 0), 0.2, -107.9999999999, 72)
                CenterArc((0, 0), 0.2, -35.9999999999, 72)
                CenterArc((0, 0), 0.2, 36.0000000001, 72)
                CenterArc((0, 0), 0.2, 108.0000000001, 71.9999999999)
                CenterArc((0, 0), 0.2, -180, 72.0000000001)
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


# Description: This is an elliptical boat hull or watercraft shell featuring a curved, streamlined body with a flat interior deck, reinforced rim flanges, and internal structural ribs for structural support.
def model_41124_a5855c0d_0006():
    """Model: Mating Ring Top"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 196.0667975105, perimeter: 49.6371639267
            Circle(7.9)
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)
    return part.part


# Description: This is a cylindrical rod or shaft with a slight taper, featuring rounded ends and a dark gray finish, appearing to be a simple mechanical component such as a pin, axle, or dowel.
def model_41124_a5855c0d_0007():
    """Model: Stem"""
    with BuildPart() as part:
        # Sketch3 -> Extrude2 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            Circle(0.4)
        # OneSide extrude, distance=9
        extrude(amount=9)
    return part.part


# Description: This is a wakeboard or kiteboard with an elongated oval shape, featuring a dark navy base with blue geometric graphics, a curved hydrodynamic profile, and what appears to be integrated foot straps or binding areas along its surface.
def model_41124_a5855c0d_0010():
    """Model: Top Union"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 22.3446900494, perimeter: 30.1646003294
            with BuildLine():
                Line((-3.3, -1.5), (3.3, -1.5))
                CenterArc((3.3, 0), 1.5, -90, 180)
                Line((3.3, 1.5), (-3.3, 1.5))
                CenterArc((-3.3, 0), 1.5, 90, 180)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.8
        extrude(amount=0.8)
    return part.part


# Description: A long, flat parallelogram-shaped plate or trim piece with a dark textured surface and beveled edges on the left and right ends.
def model_41125_711db4bf_0007():
    """Model: main_rotor_blade v5 (1)"""
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
        # Sketch1 -> Extrude7 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 9 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0930327826, perimeter: 3.2294513158
            with BuildLine():
                Line((-2.100000019, 1.1748666951), (-2.0999999531, 1.0999999754))
                _nurbs_edge([(-2.0999999531, 1.0999999754), (-2.0823030967, 1.104521717), (-2.0454059295, 1.1129036403), (-1.9855499173, 1.1234919327), (-1.896825596, 1.133732866), (-1.7715009612, 1.1404998369), (-1.6322534616, 1.1416812478), (-1.47964936, 1.1376449716), (-1.3146272475, 1.1286550192), (-1.1382173235, 1.1148167664), (-0.9512446625, 1.0960556005), (-0.7936301438, 1.076935458), (-0.670988194, 1.0601624781), (-0.5872566477, 1.047877334), (-0.5448982897, 1.0414589588)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1, 1, 1, 1, 1], 5)
                Line((-0.542076922, 1.0561796295), (-0.5448982897, 1.0414589588))
                _nurbs_edge([(-2.100000019, 1.1748666951), (-2.0768971161, 1.1812560102), (-2.031272441, 1.1929940439), (-1.9645774658, 1.2074793565), (-1.8774357178, 1.2206114033), (-1.7626221029, 1.2270151342), (-1.6323020712, 1.2238177916), (-1.479569, 1.2116236722), (-1.3050440479, 1.1915309784), (-1.114925844, 1.1648740107), (-0.9179964091, 1.1329272668), (-0.7623903191, 1.1039777626), (-0.6501184614, 1.080669759), (-0.5776878584, 1.0644555928), (-0.542076922, 1.0561796295)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1, 1, 1, 1, 1], 5)
            make_face()
            # Profile area: 0.0024517206, perimeter: 0.201483707
            with BuildLine():
                _nurbs_edge([(-2.100000019, 1.1748666951), (-2.101229345, 1.1745267139), (-2.1036947928, 1.17372886), (-2.1074133473, 1.1721784266), (-2.1123926081, 1.1694508178), (-2.1185317396, 1.1651916279), (-2.1244169964, 1.1603863378), (-2.1298525857, 1.1553225826), (-2.1346386276, 1.1502118126), (-2.1386019427, 1.1451226125), (-2.1415868004, 1.1400265467), (-2.1430805166, 1.1358822374), (-2.1436484599, 1.1326985894), (-2.1437746737, 1.1305367854), (-2.1437746737, 1.1294460389)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1, 1, 1, 1, 1], 5)
                _nurbs_edge([(-2.0999999531, 1.0999999754), (-2.1014740158, 1.0996233362), (-2.1044328001, 1.0990486176), (-2.1089029476, 1.0987221882), (-2.1148715049, 1.099294602), (-2.1220349183, 1.1013520316), (-2.1285129677, 1.1043453441), (-2.1339401983, 1.1078915951), (-2.1380738497, 1.1117072196), (-2.1409365092, 1.1156944024), (-2.1427124952, 1.1198885224), (-2.1434524672, 1.1234927093), (-2.143716093, 1.1263875967), (-2.1437746737, 1.1284109799), (-2.1437746737, 1.1294460389)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1, 1, 1, 1, 1], 5)
                Line((-2.100000019, 1.1748666951), (-2.0999999531, 1.0999999754))
            make_face()
            # Profile area: 0.000083974, perimeter: 0.0379658156
            with BuildLine():
                CenterArc((-0.5437746737, 1.0488743136), 0.0075, -98.6162328424, 175.5329638244)
                Line((-0.542076922, 1.0561796295), (-0.5448982897, 1.0414589588))
            make_face()
        # OneSide extrude, distance=9.5
        extrude(amount=9.5)
    return part.part


# Description: This is a toroidal or ring-shaped component with a circular hollow center and a textured radial fin or ribbed pattern covering its outer and inner surfaces, commonly used as a heat dissipation element or structural reinforcement ring.
def model_41128_ee74f244_0008():
    """Model: 8-Washer"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 5.5389461309, perimeter: 13.9563996999
            with BuildLine():
                CenterArc((-15.7476389296, 10.877925272), 1.50749, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-15.7476389296, 10.877925272), 0.71374, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.23622
        extrude(amount=0.23622)
    return part.part


# Description: This is a hexagonal or polygonal prism with a pyramidal top section, featuring a dark base body with lighter blue faceted surfaces on the upper portion, creating a geometric solid with angular faces and no apparent holes or slots.
def model_41142_1bf94ee2_0000():
    """Model: Groove v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude2 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.8, perimeter: 3.6
            with BuildLine():
                Line((0, 1), (0, 0))
                Line((0, 0), (0.8, 0))
                Line((0.8, 0), (0.8, 1))
                Line((0.8, 1), (0, 1))
            make_face()
        # OneSide extrude, distance=0.7
        extrude(amount=0.7)
    return part.part


# Description: This is a cylindrical sleeve or spacer with a hollow tubular body featuring grooved or ribbed texture on its outer surface and two recessed slots or grooves running along its length.
def model_41142_1bf94ee2_0002():
    """Model: Bushing v5"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.2827433388, perimeter: 5.6548667765
            with BuildLine():
                CenterArc((0, 0), 0.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.8
        extrude(amount=1.8)
    return part.part


# Description: This is a toroidal ring or annular disc with a donut-like shape, featuring a large central hole and textured surface patterns on portions of its outer edge.
def model_41142_1bf94ee2_0004():
    """Model: Split Lock M6 v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 12 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.4342720262, perimeter: 5.4493711667
            with BuildLine():
                Line((0.0051299962, 0.32495951), (0.0164305846, 0.4947272338))
                CenterArc((0, 0), 0.325, 90.9044287341, 358.1911425317)
                Line((-0.0051299962, 0.32495951), (-0.0164305846, 0.4947272338))
                CenterArc((0, 0), 0.495, 91.9021739614, 356.1956520772)
            make_face()
        # OneSide extrude, distance=0.15
        extrude(amount=0.15)
    return part.part


# Description: This is a circular disc or plate with a slightly raised or beveled edge rim, featuring a flat face with a subtle curved or dished profile, commonly used as a cover, seal, or structural component.
def model_41142_1bf94ee2_0006():
    """Model: Cover v6"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 28.2743338823, perimeter: 18.8495559215
            Circle(3)
        # OneSide extrude, distance=0.274
        extrude(amount=0.274)
    return part.part


# Description: This is a ventilated disc brake rotor with a large flat circular friction surface and radial cooling fins on the reverse side for heat dissipation.
def model_41142_1bf94ee2_0009():
    """Model: Pad v6"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 11.6631627265, perimeter: 14.1371669412
            with BuildLine():
                CenterArc((0, 0), 1.95, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.7
        extrude(amount=0.7)
    return part.part


# Description: This is a polyhedron or geometric solid with an irregular multi-faced structure, featuring a combination of triangular and polygonal faces with a faceted, angular design and no apparent holes, slots, or curves.
def model_41142_1bf94ee2_0012():
    """Model: Special Screw v7 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 4 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.233826866, perimeter: 1.8000000268
            with BuildLine():
                Line((0.259807625, 0.1500000022), (0, 0.3000000045))
                Line((0, 0.3000000045), (-0.259807625, 0.1500000022))
                Line((-0.259807625, 0.1500000022), (-0.259807625, -0.1500000022))
                Line((-0.259807625, -0.1500000022), (0, -0.3000000045))
                Line((0, -0.3000000045), (0.259807625, -0.1500000022))
                Line((0.259807625, -0.1500000022), (0.259807625, 0.1500000022))
            make_face()
        # OneSide extrude, distance=0.23
        extrude(amount=0.23)
    return part.part


# Description: This is a cylindrical disk or washer with a flat, circular face and a curved edge, featuring a mesh-textured rim that suggests it may be a deformable or flexible component, possibly a diaphragm or compliance element.
def model_41142_1bf94ee2_0014():
    """Model: Spherical insert v5"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 6.6051985542, perimeter: 9.1106186954
            Circle(1.45)
        # OneSide extrude, distance=0.58
        extrude(amount=0.58)
    return part.part


# Description: This is a cylindrical tube or pipe with a textured mesh or perforated pattern visible on both the top and bottom edges, featuring a smooth main body with a slight diagonal orientation.
def model_41227_90e1c07c_0001():
    """Model: Outer Handle Bar"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 15.5179165474, perimeter: 13.9643793452
            with Locations((33.0232015865, 17.075736165)):
                Circle(2.2225)
        # OneSide extrude, distance=20.32
        extrude(amount=20.32)
    return part.part


# Description: This is a toroidal (doughnut-shaped) component with a large central hole, featuring a rounded, symmetrical geometry with smooth curved surfaces and a hollow interior cavity.
def model_41227_90e1c07c_0004():
    """Model: Wheel Nut"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 15.2012243729, perimeter: 23.9389360204
            with BuildLine():
                CenterArc((-64.6113702955, 79.6261168384), 2.54, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-64.6113702955, 79.6261168384), 1.27, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=2.54
        extrude(amount=2.54)
    return part.part


# Description: This is a cylindrical capsule or pressure vessel with hemispherical end caps, featuring a central longitudinal slot or opening running along its length, and appears to be designed for fluid containment or mechanical application.
def model_41227_90e1c07c_0005():
    """Model: Inner Handle bar"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 31.6692174436, perimeter: 19.9491133503
            with Locations((-86.9360584655, 44.2830060983)):
                Circle(3.175)
        # OneSide extrude, distance=15.24
        extrude(amount=15.24)
    return part.part


# Description: This is a cylindrical ring or bushing with a grooved or knurled textured surface on the outer diameter and internal slots or grooves running along its length.
def model_41227_90e1c07c_0007():
    """Model: Pedal"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 96.6454607743, perimeter: 88.4273500668
            with BuildLine():
                CenterArc((45.4292413758, 19.1512453579), 5.4066882765, -136.6833874471, 93.3238166791)
                CenterArc((42.4273347533, 20.5191502369), 8.5948449405, -36.2316944899, 72.4633889799)
                CenterArc((45.5502244502, 21.7802158677), 5.394474925, 45.0670999895, 89.8658000209)
                CenterArc((47.7869103912, 20.3719723603), 7.992859277, 139.1575730765, 78.9241457001)
            make_face()
            with BuildLine():
                CenterArc((26.854979713, 19.7994910534), 20.8832148759, -13.6623254788, 31.132900007)
                CenterArc((47.3931683816, 23.611331426), 2.5342153836, 75.8786157382, 28.2427685236)
                CenterArc((31.3337633433, 20.5486672551), 17.567561312, -18.8045511074, 37.1190359687)
                CenterArc((47.5425920645, 15.4285219506), 0.6867952117, -125.1392335635, 72.9496675123)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((65.91743432, 19.3127122736), 22.6064134561, 162.4353147207, 28.374702716)
                CenterArc((43.2355114726, 15.6397876218), 0.7407289677, -112.8859592589, 62.9405752645)
                CenterArc((64.8991076634, 20.0514354514), 22.5349747709, 164.5123480096, 28.5523758565)
                CenterArc((43.9992714813, 22.0581361872), 4.0931642543, 84.8736839003, 16.6377930752)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=6.35
        extrude(amount=6.35)
    return part.part


# Description: This is a boxing glove featuring a rounded, padded head with mesh ventilation panels, a cylindrical wrist cuff, and a rectangular thumb extension for hand protection and support during training or competition.
def model_41227_90e1c07c_0008():
    """Model: Wheel Stopper"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 3 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 80.8248844093, perimeter: 58.8419367798
            with BuildLine():
                Line((38.3556075623, 6.0172255592), (42.1656075623, 6.0172255592))
                Line((42.1656075623, 6.0172255592), (42.1656075623, 11.4669425727))
                CenterArc((40.2606075623, 16.1899255592), 5.0927, -68.0334740978, 316.0669481956)
                Line((38.3556075623, 6.0172255592), (38.3556075623, 11.4669425727))
            make_face()
            with BuildLine():
                CenterArc((40.2606075623, 16.1899255592), 2.5527, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=3.81
        extrude(amount=3.81)
    return part.part


# Description: This is a cylindrical foam roller with a textured surface pattern, featuring a hollow core and rounded ends, designed for muscle recovery and massage applications.
def model_41227_90e1c07c_0009():
    """Model: Center Pedal Bar"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 20.2682991639, perimeter: 15.9592906802
            with Locations((23.590942954, 9.172051888)):
                Circle(2.54)
        # OneSide extrude, distance=17.78
        extrude(amount=17.78)
    return part.part


# Description: This is a cylindrical roller or spacer with a solid circular end face and a hollow or meshed cylindrical body, featuring a uniform tubular geometry with rounded edges.
def model_41227_90e1c07c_0010():
    """Model: Pedal Spin"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 20.2682991639, perimeter: 15.9592906802
            with Locations((41.6051581748, 7.3030330839)):
                Circle(2.54)
        # OneSide extrude, distance=10.1854
        extrude(amount=10.1854)
    return part.part


# Description: This is a cylindrical shaft or spacer with a smooth, uniform circular cross-section and rounded ends, featuring a textured or knurled surface pattern along its body.
def model_41227_90e1c07c_0011():
    """Model: Pedal Bar"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 20.2682991639, perimeter: 15.9592906802
            with Locations((27.8060298142, 8.5289201629)):
                Circle(2.54)
        # OneSide extrude, distance=12.7
        extrude(amount=12.7)
    return part.part


# Description: This is a circular disk or plate with a flat, disc-like shape and a beveled or rounded edge around its perimeter.
def model_41227_90e1c07c_0012():
    """Model: Pedal Catch"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 25.6520661293, perimeter: 17.9542020153
            with Locations((63.2316633292, 24.3009910676)):
                Circle(2.8575)
        # OneSide extrude, distance=0.3175
        extrude(amount=0.3175)
    return part.part


# Description: This is a rectangular bar or rod with a simple elongated shape, featuring rounded ends and a uniform cross-section throughout its length.
def model_41227_90e1c07c_0014():
    """Model: Handle Bar Base"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 11.4009182797, perimeter: 11.9694680102
            with Locations((-79.3911978606, 27.0914889513)):
                Circle(1.905)
        # OneSide extrude, distance=60.96
        extrude(amount=60.96)
    return part.part


# Description: A rectangular flat bar or plate with rounded ends and a simple elongated shape, featuring no holes or cutouts.
def model_41227_90e1c07c_0015():
    """Model: Back Wheel spinner"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 4.9662400026, perimeter: 7.8998488867
            with Locations((-96.85719421, 53.5942938057)):
                Circle(1.2573)
        # OneSide extrude, distance=86.36
        extrude(amount=86.36)
    return part.part


# Description: This is a curved mounting bracket or deflector panel with a trapezoidal shape, featuring a smooth convex surface and rounded edges, designed for structural support or flow direction in an assembly.
def model_41234_74275eb0_0004():
    """Model: Seat"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 735.7054133193, perimeter: 104.0190934974
            with BuildLine():
                CenterArc((11.8765709811, 22.0654220549), 6.8475353061, 109.3097374328, 95.5910363573)
                CenterArc((-41.8201797423, 3.3883706941), 50.0434441046, -3.2081676524, 21.6054467089)
                CenterArc((19.6355940059, 35.0776460407), 36.3536876675, -108.4261647665, 36.8523295331)
                CenterArc((81.091367754, 3.3883706941), 50.0434441046, 161.6027209435, 21.6054467089)
                CenterArc((27.3946170306, 22.0654220549), 6.8475353061, -24.9007737902, 95.5910363573)
                Line((9.6122637012, 28.5277476665), (29.6589243105, 28.5277476665))
            make_face()
        # OneSide extrude, distance=0.635
        extrude(amount=0.635)
    return part.part


# Description: This is a spherical or dome-shaped pressure vessel or tank with a flat circular base and a hemispherical or rounded top, featuring a mesh-pattern surface texture on the upper portion indicating internal ribbing or structural reinforcement.
def model_41234_74275eb0_0016():
    """Model: Small Dowel"""
    with BuildPart() as part:
        # Sketch2 -> Extrude4 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.2667686977, perimeter: 3.9898226701
            with Locations((78.2561481965, 12.4371021055)):
                Circle(0.635)
        # OneSide extrude, distance=0.635
        extrude(amount=0.635)
    return part.part


# Description: This is a U-shaped pipe or tube bend with a smooth, continuous curved profile and uniform cylindrical cross-section throughout, designed to redirect fluid or cable flow at approximately 180 degrees.
def model_41319_7cc85fc8_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 42.7833231026, perimeter: 87.451357605
            with BuildLine():
                Line((6, 0), (6, 13))
                Line((6, 0), (7, 0))
                Line((7, 0), (7, 13))
                CenterArc((-0.1363636364, 10.4090909091), 7.5921338152, 19.9537992204, 69.0170459753)
                CenterArc((0.1363636364, 10.4090909091), 7.5921338152, 91.0291548043, 69.0170459753)
                Line((-7, 0), (-7, 13))
                Line((-7, 0), (-6, 0))
                Line((-6, 0), (-6, 13))
                CenterArc((0.3156900549, 10.0264649177), 6.980677027, 92.5919948392, 62.1961453735)
                CenterArc((-0.2873650051, 10.0689524924), 6.9370021046, 24.994019427, 62.631826094)
            make_face()
        # TwoSides extrude (symmetric), distance=0.75
        extrude(amount=0.75, both=True)
    return part.part


# Description: This is a cylindrical mesh or perforated filter sleeve with an open top end and a slightly tapered, mesh-covered upper rim, designed for filtration or straining applications.
def model_41321_43c99300_0001():
    """Model: push_hold3"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2.6805113849, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.024321959, perimeter: 0.9575574408
            with BuildLine():
                CenterArc((-3.4026642619, 5.8855075533), 0.1016, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-3.4026642619, 5.8855075533), 0.0508, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.35306
        extrude(amount=-0.35306)
    return part.part


# Description: This is a cylindrical rod or shaft with rounded ends, featuring a simple elongated tubular shape with a slight diagonal orientation.
def model_41321_43c99300_0002():
    """Model: push_hold1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0197615917, perimeter: 1.0373538942
            with BuildLine():
                CenterArc((4.0621639838, -5.1074392164), 0.1016, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((4.0621639838, -5.1074392164), 0.0635, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=2.44602
        extrude(amount=2.44602)
    return part.part


# Description: This is a straight cylindrical rod or shaft with a simple, uniform circular cross-section and tapered or pointed ends.
def model_41321_43c99300_0004():
    """Model: graphite"""
    with BuildPart() as part:
        # Sketch2 -> Extrude2 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0039725866, perimeter: 0.2234300695
            with Locations((1.4919288657, -0.8642271445)):
                Circle(0.03556)
        # OneSide extrude, distance=5.9944
        extrude(amount=5.9944)
    return part.part


# Description: This is a cylindrical rod or shaft with a uniform circular cross-section and slightly tapered or rounded ends, appearing to be a simple mechanical component such as a pin, dowel, or axle.
def model_41321_43c99300_0005():
    """Model: tube"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0635613862, perimeter: 1.7874405562
            with BuildLine():
                CenterArc((4.2079016214, -4.675497957), 0.1778, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((4.2079016214, -4.675497957), 0.10668, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=8.89
        extrude(amount=8.89)
    return part.part


# Description: This is a cylindrical rod or shaft with a smooth, uniform circular cross-section, tapered slightly at the ends, and positioned at an angle.
def model_41321_43c99300_0008():
    """Model: metal_hold"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0042753444, perimeter: 0.5386260605
            with BuildLine():
                CenterArc((1.1048498182, -2.0249275562), 0.0508, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((1.1048498182, -2.0249275562), 0.034925, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.94742
        extrude(amount=0.94742)
    return part.part


# Description: This is a cylindrical mesh or perforated filter component with an open top and bottom, featuring a fine lattice pattern throughout its walls and a slightly flared or curved upper rim.
def model_41321_43c99300_0011():
    """Model: hold1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.5236231785, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.024321959, perimeter: 0.9575574408
            with BuildLine():
                CenterArc((-0.2114717166, 2.3421024793), 0.1016, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-0.2114717166, 2.3421024793), 0.0508, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.1905
        extrude(amount=0.1905)
    return part.part


# Description: This is a segmented tubular or pipe-like component with an elongated hexagonal or polygonal cross-section that features a central curved bend or elbow, composed of multiple faceted geometric sections with darker and lighter shaded faces indicating internal geometry or hollow cavities.
def model_41401_1f3f8936_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 10 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 264.6482088753, perimeter: 86.6522218475
            with BuildLine():
                Line((34.29, 0), (34.29, 8.89))
                Line((34.29, 8.89), (6.35, 8.89))
                Line((6.35, 8.89), (6.35, 7.62))
                Line((6.35, 7.62), (0, 7.62))
                Line((0, 7.62), (0, 2.4632879205))
                Line((13.97, 0), (0, 2.4632879205))
                Line((20.15998, 0), (13.97, 0))
                Line((20.15998, 1.27), (20.15998, 0))
                Line((31.90748, 1.27), (20.15998, 1.27))
                Line((31.90748, 0), (31.90748, 1.27))
                Line((34.29, 0), (31.90748, 0))
            make_face()
        # OneSide extrude, distance=8.89
        extrude(amount=8.89)
    return part.part


# Description: This is a long, slender hexagonal prism or shaft with a dark blue-gray finish, featuring a uniform cross-section throughout its length and tapered or beveled edges at the top end.
def model_41401_3b4b3455_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.6129, perimeter: 5.08
            with BuildLine():
                Line((0, 1.27), (0, 0))
                Line((0, 0), (1.27, 0))
                Line((1.27, 0), (1.27, 1.27))
                Line((1.27, 1.27), (0, 1.27))
            make_face()
        # OneSide extrude, distance=11.7475
        extrude(amount=11.7475)
    return part.part


# Description: This is a flat parallelogram-shaped plate or panel with a beveled or chamfered edge on one corner and internal diagonal reinforcement ribs.
def model_41401_4ced1833_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 3 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 33.306385, perimeter: 54.991
            with BuildLine():
                Line((0, 0), (26.2255, 0))
                Line((26.2255, 0), (26.2255, 1.27))
                Line((0, 1.27), (26.2255, 1.27))
                Line((0, 0), (0, 1.27))
            make_face()
        # OneSide extrude, distance=11.7475
        extrude(amount=11.7475)
    return part.part


# Description: This is a dark blue wedge or triangular prism-shaped structural component with a tapered profile, featuring sharp edges and flat faceted surfaces typical of sheet metal or stamped parts.
def model_41401_63f271a2_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 12.3848953256, perimeter: 18.4410906198
            with BuildLine():
                Line((4.445, 5.08), (4.445, 4.445))
                Line((0, 5.08), (4.445, 5.08))
                Line((0, 0), (0, 5.08))
                Line((4.445, 4.445), (0, 0))
            make_face()
            with BuildLine():
                CenterArc((3.81, 4.572), 0.3175, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.27
        extrude(amount=1.27)
    return part.part


# Description: This is a two-bladed aircraft propeller with elongated, tapered composite blades connected at a central hub, designed for efficient aerodynamic rotation.
def model_41401_7a33a5db_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 14 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 20.6775088014, perimeter: 31.5143151982
            with BuildLine():
                CenterArc((-7.2840529632, -3.5874445986), 8.2373548198, -19.5949926183, 39.1899852366)
                CenterArc((0, 0), 0.9525, -60, 120)
                CenterArc((-7.2840529632, 3.5874445986), 8.2373548198, -19.5949926183, 39.1899852366)
                CenterArc((0, 6.35), 0.47625, 0, 180)
                CenterArc((7.2840529632, 3.5874445986), 8.2373548198, 160.4050073817, 39.1899852366)
                CenterArc((0, 0), 0.9525, 120, 120)
                CenterArc((7.2840529632, -3.5874445986), 8.2373548198, 160.4050073817, 39.1899852366)
                CenterArc((0, -6.35), 0.47625, 180, 180)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.3175, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.3175
        extrude(amount=0.3175)
    return part.part


# Description: This is a boat hull or ship hull component with an elongated, curved bottom surface, a flat or slightly angled top deck area, and a raised bow section on the left end, featuring a faceted/triangulated surface design typical of low-polygon 3D modeling.
def model_41401_92345581_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 20.8451821242, perimeter: 35.56
            with BuildLine():
                Line((0, 0), (-3.1267646158, 0.5513329641))
                Line((-3.1267646158, 0.5513329641), (-3.1267646158, -0.7186670359))
                Line((-3.1267646158, -0.7186670359), (0, -1.27))
                Line((0, -1.27), (10.16, -1.27))
                Line((13.2867646158, -0.7186670359), (10.16, -1.27))
                Line((13.2867646158, 0.5513329641), (13.2867646158, -0.7186670359))
                Line((10.16, 0), (13.2867646158, 0.5513329641))
                Line((0, 0), (10.16, 0))
            make_face()
        # OneSide extrude, distance=6.35
        extrude(amount=6.35)
    return part.part


# Description: This is a horizontal cylindrical rod or shaft with rounded ends and two rectangular slots or recesses positioned symmetrically on opposite sides near each end.
def model_41401_a4897785_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.3166921744, perimeter: 1.994911335
            Circle(0.3175)
        # OneSide extrude, distance=3.81
        extrude(amount=3.81)
    return part.part


# Description: This is a boat hull or marine vessel hull structure featuring an asymmetrical tapered design with a curved bottom, diagonal internal bracing/ribs for structural reinforcement, and a flat top deck surface with a pronounced bow (front end) that slopes downward.
def model_41401_a7e53916_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 14 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 32.9036928941, perimeter: 54.9436691097
            with BuildLine():
                CenterArc((0.513997648, 5.87502), 5.87502, -100, 10)
                Line((0.513997648, 0), (14.408502352, 0))
                CenterArc((14.408502352, 5.87502), 5.87502, -90, 10)
                Line((15.4286888688, 0.0892547549), (20.574, 0.9965119315))
                Line((20.574, 0.9965119315), (20.3631711878, 2.1921815414))
                Line((15.6394086466, 1.3592547549), (20.3631711878, 2.1921815414))
                CenterArc((14.6192221299, 7.14502), 5.87502, -90, 10)
                Line((0.5041887845, 1.27), (14.6192221299, 1.27))
                CenterArc((0.5041887845, 7.14375), 5.87375, -100, 10)
                Line((-0.515777199, 1.3592354607), (-5.498109632, 2.2377550955))
                Line((-5.715, 1.0077086947), (-5.498109632, 2.2377550955))
                Line((-0.5061888688, 0.0892547549), (-5.715, 1.0077086947))
            make_face()
        # OneSide extrude, distance=11.7475
        extrude(amount=11.7475)
    return part.part


# Description: This is a conical or pyramidal cover/shroud with a tapered shape that narrows toward the top, featuring a vertical slot or seam along one side and a rounded apex, likely designed as a protective enclosure or aesthetic housing component.
def model_41401_b70e852a_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 14.7563347083, perimeter: 17.3592840841
            with BuildLine():
                Line((0, 0), (4.52628, 0))
                Line((4.52628, 0), (0.9299147651, 5.3629347149))
                CenterArc((0.5080000162, 5.0800001621), 0.5080000162, 33.8456667965, 146.154351489)
                Line((0, 0), (0, 5.08))
            make_face()
        # OneSide extrude, distance=0.635
        extrude(amount=0.635)
    return part.part


# Description: This is a corner guard or edge protector with a tall, tapered cylindrical shape featuring a curved top, a vertical slot or channel running along one side, and a textured surface on the upper portion.
def model_41401_de8868e3_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 6 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 39.2474032766, perimeter: 26.5855474351
            with BuildLine():
                Line((0, 0), (6.35, 0))
                Line((6.35, 0), (3.0528846154, 7.9130769231))
                CenterArc((1.5875, 7.3025), 1.5875, 22.619864948, 157.380135052)
                Line((0, 0), (0, 7.3025))
            make_face()
        # OneSide extrude, distance=1.27
        extrude(amount=1.27)
    return part.part


# Description: This is a curved blade or airfoil-shaped component with a streamlined, elongated form featuring a pointed leading edge, a rounded upper surface, and a flatter lower surface with internal geometric structure visible through transparent shading.
def model_41401_f7b87ad7_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 3 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 66.5116433299, perimeter: 44.4869536206
            with BuildLine():
                Line((0, 0), (20.6375, 0))
                Line((20.6375, 0), (16.51, 4.1275))
                Line((4.9189629534, 4.1275), (16.51, 4.1275))
                Line((0, 0), (4.9189629534, 4.1275))
            make_face()
        # OneSide extrude, distance=8.89
        extrude(amount=8.89)
    return part.part


# Description: This is a yoke or connector bracket featuring an elongated curved central body with two cylindrical holes or ports on either side, designed for connecting or mounting two components.
def model_41468_264ed8e7_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch2 -> Extrude2 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 5 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 199.4981483936, perimeter: 96.5200139743
            with BuildLine():
                CenterArc((-43.9166676265, -24.9405272144), 10, -25.267669087, 109.7200148181)
                CenterArc((-21.308578737, -35.6117181867), 15, 59.1054434711, 95.6268874405)
                CenterArc((0, 0), 26.5, -179.9204470512, 59.0258904596)
                CenterArc((-41.4999600118, -0.0576109001), 15, -95.5471448639, 95.6266588204)
            make_face()
            # Profile area: 314.159265359, perimeter: 62.8318530718
            with BuildLine():
                CenterArc((-43.9166676265, -24.9405272144), 10, 84.4523457311, 250.2799851819)
                CenterArc((-43.9166676265, -24.9405272144), 10, -25.267669087, 109.7200148181)
            make_face()
            # Profile area: 2206.1834409834, perimeter: 166.5044106403
            with BuildLine():
                CenterArc((0, 0), 26.5, -120.8945565916, 61.789113183)
                CenterArc((0, 0), 26.5, -59.1054434086, 59.0259091034)
                CenterArc((0, 0), 26.5, -0.0795343052, 180.1590872539)
                CenterArc((0, 0), 26.5, -179.9204470512, 59.0258904596)
            make_face()
            # Profile area: 199.4981483936, perimeter: 96.5200278775
            with BuildLine():
                CenterArc((0, 0), 26.5, -59.1054434086, 59.0259091034)
                CenterArc((21.308578737, -35.6117181867), 15, 25.2676691342, 95.6268873952)
                CenterArc((43.9166676265, -24.9405272144), 10, 95.5476637767, 109.7200052416)
                CenterArc((41.4999600118, -0.0576109001), 15, 179.9204531066, 95.6266854188)
            make_face()
            # Profile area: 314.159265359, perimeter: 62.8318530718
            with BuildLine():
                CenterArc((43.9166676265, -24.9405272144), 10, 95.5476637767, 109.7200052416)
                CenterArc((43.9166676265, -24.9405272144), 10, -154.7323309816, 250.2799947584)
            make_face()
        # OneSide extrude, distance=2.5
        extrude(amount=2.5)
    return part.part


# Description: This is a dual-loop strap or handle assembly featuring two dark padded end caps connected by a long, flexible dark blue/navy webbing band, designed for carrying or securing objects.
def model_41469_4e88cdb5_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 21 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.6927065944, perimeter: 28.6188243493
            with BuildLine():
                CenterArc((1.6092218987, -2.6878912807), 1.016, -116.6443180553, 192.4630232058)
                Line((-0.275387301, -0.8269585909), (1.8581326342, -1.7028534917))
                Line((-0.1112428359, -0.4963935176), (-0.275387301, -0.8269585909))
                CenterArc((0, 0), 0.5087057036, -102.6314078362, 152.448760984)
                Line((0.5571316614, 0.8496236295), (0.3282303129, 0.3886468249))
                CenterArc((0, 0), 1.016, 56.7455668127, 193.6948116861)
                Line((-0.3401441844, -0.9573703222), (1.8153955697, -1.8176914235))
                Line((1.6788198202, -2.1846814543), (1.8153955697, -1.8176914235))
                CenterArc((1.6092218987, -2.6878912807), 0.508, 82.1254950724, 154.9233969504)
                Line((1.1535961109, -3.5959998323), (1.3329089249, -3.1141718696))
            make_face()
            with BuildLine():
                Line((0.2997931613, 0.8369259588), (0.1654631711, 0.5664032639))
                Line((0.1654631711, 0.5664032639), (0.1286073258, 0.4921805041))
                CenterArc((0, 0), 0.5087057036, 75.3559767051, 0.1218073136)
                CenterArc((0, 0), 0.5087057036, 75.4777840187, 154.770631246)
                Line((-0.325297085, -0.3911052279), (-0.5011784222, -0.7342623435))
                CenterArc((0, 0), 0.889, 70.2920946946, 165.3920066907)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((1.4034267664, -3.5527435013), (1.5380921187, -3.1908868616))
                CenterArc((1.6092218987, -2.6878912807), 0.508, -98.0489602728, 155.2723076409)
                Line((1.8842356459, -2.2607713457), (2.0189009982, -1.898914706))
                CenterArc((1.6092218987, -2.6878912807), 0.889, -103.3848447536, 165.9440766025)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1.6092218987, -2.6878912807), 0.254, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0, 0), 0.254, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.254
        extrude(amount=0.254)
    return part.part


# Description: This is a cast iron or metal retaining ring with an oval/elliptical loop design, featuring a cylindrical base flange and a curved upper loop with a slot or opening, typically used for securing or guiding components in mechanical assemblies.
def model_41469_b94cf3e4_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 8 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 6.9402462248, perimeter: 29.5388652778
            with BuildLine():
                CenterArc((0, 0), 1.8034, -106.6445875687, 274.1205919574)
                CenterArc((-4.0411037449, 0.7350652942), 2.30641323, -12.04080174, 3.4631500463)
                CenterArc((-4.0411037449, 0.7350652942), 2.30641323, -78.4084235703, 66.3676218302)
                CenterArc((-3.5560001135, -2.286000073), 0.762, 91.6293912456, 229.7796678833)
                CenterArc((-1.0036534874, -3.982228122), 2.30641323, 144.7482034591, 3.2894843386)
                CenterArc((-1.0036534874, -3.982228122), 2.30641323, 77.8077258228, 66.9404776363)
            make_face()
            with BuildLine():
                CenterArc((-3.5560001135, -2.286000073), 0.508, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0, 0), 1.43637, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.254
        extrude(amount=0.254)
    return part.part


# Description: This is a curved, hollow tubular duct or conduit with a twisted/helical geometry, featuring a longitudinal slot or opening along one side and tapering end sections at both extremities.
def model_41473_c2137170_0002():
    """Model: Component1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 3 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 117.1527611242, perimeter: 50.7329834753
            with BuildLine():
                Line((15.4, 14.6), (15.4, 19.9757660697))
                Line((15.4, 19.9757660697), (10.9182112248, 19.9757660697))
                CenterArc((15.4, 5), 15.6320184237, 106.6608334483, 63.4552294445)
                Line((0, 5), (0, 7.683281573))
                Line((0, 5), (5.8, 5))
                CenterArc((15.4, 5), 9.6, 90, 90)
            make_face()
        # OneSide extrude, distance=4.5
        extrude(amount=4.5)
    return part.part


# Description: This is a flexible mesh-reinforced belt or band with a curved, loop-like structure featuring a rectangular buckle or clasp mechanism on one end and a textured mesh surface on the outer edge.
def model_41473_c2137170_0009():
    """Model: handle bar clamp"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 14.7622390202, perimeter: 41.935997322
            with BuildLine():
                Line((32.2963055315, -5.5025298213), (30.7963055315, -5.5025298213))
                Line((30.7963055315, -5.5025298213), (30.7956398318, -6.0025293781))
                Line((30.7956398318, -6.0025293781), (31.6469922689, -6.0036628693))
                CenterArc((35, -5), 3.5, -163.3358699626, 326.777530678)
                Line((30.7953700029, -4.0025298213), (31.6451448254, -4.0025298213))
                Line((30.7953700029, -4.5025298213), (30.7953700029, -4.0025298213))
                Line((32.2953700029, -4.5025298213), (30.7953700029, -4.5025298213))
                CenterArc((35, -5), 2.75, -169.4707118398, 339.0486273352)
            make_face()
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)
    return part.part


# Description: This is a hexagonal ring or band with an organic, curved central void, featuring a faceted outer geometry with a smooth, flowing hollow passage through its center.
def model_41473_c2137170_0010():
    """Model: frontaxle_nut"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.0860516784, perimeter: 9.3124737685
            with BuildLine():
                Line((10.4618802154, -9.2), (9.5381197846, -9.2))
                Line((9.5381197846, -9.2), (9.0762395693, -10))
                Line((9.0762395693, -10), (9.5381197846, -10.8))
                Line((9.5381197846, -10.8), (10.4618802154, -10.8))
                Line((10.4618802154, -10.8), (10.9237604307, -10))
                Line((10.9237604307, -10), (10.4618802154, -9.2))
            make_face()
            with BuildLine():
                CenterArc((10, -10), 0.6, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.7
        extrude(amount=0.7)
    return part.part


# Description: This is a cylindrical sleeve or bushing with a hollow center bore, featuring a smooth outer curved surface and textured inner walls, designed for use as a mechanical component in assembly applications.
def model_41473_c2137170_0012():
    """Model: backwheel_spacer2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.408407045, perimeter: 8.1681408993
            with BuildLine():
                CenterArc((-20, -5), 0.7, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-20, -5), 0.6, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.8
        extrude(amount=0.8)
    return part.part


# Description: This is a flat oval or elliptical plate with diagonal striped surface texture, featuring a dark rim edge and a slightly curved, elongated disk shape.
def model_41473_c2137170_0015():
    """Model: grip_tape"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 102.1017612417, perimeter: 44.3738141218
            with Locations((-15, 10)):
                Ellipse(10, 3.25)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


# Description: This is a polyhedron-shaped connector or junction block with an octagonal overall form, featuring a large central circular aperture running through its center and multiple triangular faces with recessed or chamfered edges.
def model_41473_c2137170_0016():
    """Model: backaxle_nut"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 2.3331282598, perimeter: 10.6981144146
            with BuildLine():
                Line((6, -0.5773502692), (6, 0.5773502692))
                Line((6, 0.5773502692), (5, 1.1547005384))
                Line((5, 1.1547005384), (4, 0.5773502692))
                Line((4, 0.5773502692), (4, -0.5773502692))
                Line((4, -0.5773502692), (5, -1.1547005384))
                Line((5, -1.1547005384), (6, -0.5773502692))
            make_face()
            with BuildLine():
                CenterArc((5, 0), 0.6, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


# Description: This is an octagonal or cylindrical housing with a large central oval/elliptical cavity or bore running through its length, featuring reinforcing ribs or fins on the interior surfaces.
def model_41473_c2137170_0018():
    """Model: brake_bolt"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.7444217569, perimeter: 6.670196061
            with BuildLine():
                Line((-4.3073544443, -15.0155606632), (-4.6402012926, -14.4079316846))
                Line((-4.6402012926, -14.4079316846), (-5.3328468482, -14.3923710214))
                Line((-5.3328468482, -14.3923710214), (-5.6926455557, -14.9844393368))
                Line((-5.6926455557, -14.9844393368), (-5.3597987074, -15.5920683154))
                Line((-5.3597987074, -15.5920683154), (-4.6671531518, -15.6076289786))
                Line((-4.6671531518, -15.6076289786), (-4.3073544443, -15.0155606632))
            make_face()
            with BuildLine():
                CenterArc((-5, -15), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.7
        extrude(amount=-0.7)
    return part.part


# Description: This is a C-clamp or hose clamp with a curved U-shaped body, two threaded mounting posts on top, and textured gripping surfaces along the inner curves for secure fastening of components or hoses.
def model_41473_c2137170_0023():
    """Model: pin_clip"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 14 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.3268558714, perimeter: 9.5010855355
            with BuildLine():
                CenterArc((5, 10), 0.75, 119.2050380333, 301.5940297361)
                Line((5.3659053965, 10.8508556976), (5.3659053965, 10.6546856046))
                Line((5.4996607922, 10.8508556976), (5.3659053965, 10.8508556976))
                Line((5.4996607922, 11.0470257906), (5.4996607922, 10.8508556976))
                Line((5.1713523101, 11.0470257906), (5.4996607922, 11.0470257906))
                Line((5.1713523101, 10.3614393252), (5.1713523101, 11.0470257906))
                CenterArc((5, 10), 0.4, 115.3648438935, 309.270312213)
                Line((4.8286476899, 11.0470257906), (4.8286476899, 10.3614393252))
                Line((4.5002476899, 11.0470257906), (4.8286476899, 11.0470257906))
                Line((4.5002476899, 11.0470257906), (4.5002476899, 10.852071842))
                Line((4.6340476899, 10.8518838692), (4.5002476899, 10.852071842))
                Line((4.6340476899, 10.8518838692), (4.6340476899, 10.6546593822))
            make_face()
            with BuildLine():
                CenterArc((5.4327830943, 10.9447010195), 0.025, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((4.5459892411, 10.9495488163), 0.025, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)
    return part.part


# Description: This is a hexagonal nut or fastener collar featuring a central oval hole and six flat sides, with curved surfaces and internal geometry visible through cross-sectional shading.
def model_41473_c2137170_0025():
    """Model: Component11"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 22.0107989809, perimeter: 39.7300464798
            with BuildLine():
                Line((3.4672890522, -2.0018402677), (3.4672890522, 2.0018402677))
                Line((3.4672890522, 2.0018402677), (0, 4.0036805353))
                Line((0, 4.0036805353), (-3.4672890522, 2.0018402677))
                Line((-3.4672890522, 2.0018402677), (-3.4672890522, -2.0018402677))
                Line((-3.4672890522, -2.0018402677), (0, -4.0036805353))
                Line((0, -4.0036805353), (3.4672890522, -2.0018402677))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 2.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


# Description: This is a toroidal (doughnut-shaped) component with a central hole and a textured or mesh-patterned surface, featuring a curved, ring-like geometry with uniform thickness throughout.
def model_41473_c2137170_0028():
    """Model: bearing2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 3.7777651659, perimeter: 11.6238928183
            with BuildLine():
                CenterArc((-15, -5), 1.25, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-15, -5), 0.6, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


# Description: This is a toroidal (doughnut-shaped) ring with a smooth, curved outer surface and a hollow central bore, featuring a uniform cross-section throughout its circumference.
def model_41473_c2137170_0029():
    """Model: front_tire"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 44.7676953137, perimeter: 59.6902604182
            with BuildLine():
                CenterArc((-10.3014699194, -4.9402058455), 5.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-10.3014699194, -4.9402058455), 4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=3.7
        extrude(amount=3.7)
    return part.part


# Description: This is a long, rectangular hollow channel or box beam with a trapezoidal cross-section, featuring open sides and angled flanges, designed for structural support or framing applications.
def model_41474_57d78888_0004():
    """Model: center_Gear"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0174208908, perimeter: 0.6265518049
            with BuildLine():
                Line((0, 1.9315), (0.0788792972, 1.7193999615))
                Line((0, 1.9315), (-0.0809661872, 1.7137884836))
                CenterArc((0, 0), 1.7157, 87.2951306151, 5.4097387699)
                Line((0.0788792972, 1.7193999615), (0.0809661872, 1.7137884836))
            make_face()
        # OneSide extrude, distance=0.8
        extrude(amount=0.8)
    return part.part


# Description: This is a pentagonal prism or wedge-shaped structural component with a triangular cross-section, featuring five planar faces and sharp edges, suitable for use as a support bracket, spacer, or geometric building block in an assembly.
def model_41474_57d78888_0007():
    """Model: top gear (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.01742572, perimeter: 0.626614754
            with BuildLine():
                CenterArc((0, 0), 1.7157, 87.2943757705, 5.4112484591)
                Line((0, 1.9315), (0.0809887655, 1.7137874168))
                Line((0, 1.9315), (-0.0809887655, 1.7137874168))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


# Description: This is a dark gray elongated rectangular component with rounded ends, featuring a blue-highlighted top surface with multiple internal slots and recesses for fluid or cable routing.
def model_41501_b627682a_0016():
    """Model: Beam No. 5 v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 8 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.201733956, perimeter: 3.4959836953
            with BuildLine():
                CenterArc((-0.1499999966, 0.1499999966), 0.1494991314, 90, 180)
                Line((-0.1499999966, 0.0005008652), (0.5000079426, 0.0005008652))
                CenterArc((0.5000079426, 0.1499999966), 0.1494991314, -90, 180)
                Line((-0.1499999966, 0.2994991281), (0.5000079426, 0.2994991281))
            make_face()
            with BuildLine():
                CenterArc((-0.1499999966, 0.1499999966), 0.1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0.5000079426, 0.1499999966), 0.1000000015, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


# Description: This is a linear rail or guide bar with an elongated rectangular profile, featuring a dark gray body with a blue center channel or groove running its length, and rounded end caps for smooth integration into an assembly.
def model_41501_b627682a_0019():
    """Model: Beam No. 3 v14"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.0053540442, perimeter: 8.8491152062
            with BuildLine():
                CenterArc((-3.3250001579, 0.1500000022), 0.1500000023, 90, 180)
                Line((-3.3250001579, 0), (0, 0))
                CenterArc((0, 0.1500000022), 0.1500000022, -90, 180)
                Line((0, 0.3000000045), (-3.3250001579, 0.3000000045))
            make_face()
            with BuildLine():
                CenterArc((-3.3250001579, 0.1500000022), 0.1000000015, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0, 0.1500000022), 0.1000000015, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


# Description: This is a cylindrical rod or tube with rounded ends, featuring a smooth, tapered barrel shape that is tilted at an angle.
def model_41501_b627682a_0026():
    """Model: Double Gear v5"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0942477787, perimeter: 1.8849556015
            with BuildLine():
                CenterArc((0, 0), 0.2, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.1000000015, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=2.5
        extrude(amount=2.5)
    return part.part


# Description: This is a hexagonal or polygonal housing/enclosure with curved internal cylindrical surfaces and ventilation slots, featuring a complex geometric design with multiple faceted exterior walls and internal ribbed or slotted features for structural support or airflow management.
def model_41501_b627682a_0027():
    """Model: Floor Bracket No. 3 v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1493362979, perimeter: 3.35663711
            with BuildLine():
                Line((0.2500000037, -0.3000000037), (0.2500000037, 0.2500000037))
                Line((0.2500000037, 0.2500000037), (-0.2500000037, 0.2500000037))
                Line((-0.2500000037, 0.2500000037), (-0.2500000037, -0.3000000037))
                Line((-0.2500000037, -0.3000000037), (0.2500000037, -0.3000000037))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.200000003, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


# Description: This is a complex industrial manifold or valve body casting with an irregular, multi-chambered shape featuring internal passages, mounting flanges, and various port openings for fluid or gas distribution.
def model_41501_b627682a_0029():
    """Model: Gear No. 1 v7 (3)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 29 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1138482336, perimeter: 3.158713137
            with BuildLine():
                CenterArc((0, 0), 0.2500000037, 101.4783407829, 22.0433184342)
                Line((-0.1380630459, 0.2084192823), (-0.0966441307, 0.1458934954))
                CenterArc((0, 0), 0.175, 123.5216592171, 22.9566815658)
                Line((-0.2084192823, 0.1380630459), (-0.1458934954, 0.0966441307))
                CenterArc((0, 0), 0.2500000037, 146.4783407829, 22.0433208368)
                Line((-0.2450000059, 0.0497493616), (-0.1715000016, 0.0348245526))
                CenterArc((0, 0), 0.175, 168.5216616197, 22.9566767606)
                Line((-0.2450000059, -0.0497493616), (-0.1715000016, -0.0348245526))
                CenterArc((0, 0), 0.2500000037, -168.5216616197, 22.0433208368)
                Line((-0.2084192823, -0.1380630459), (-0.1458934954, -0.0966441307))
                CenterArc((0, 0), 0.175, -146.4783407829, 22.9566815658)
                Line((-0.1380630459, -0.2084192823), (-0.0966441307, -0.1458934954))
                CenterArc((0, 0), 0.2500000037, -123.5216592171, 22.0433184342)
                Line((-0.0497493719, -0.2450000038), (-0.0348245598, -0.1715000001))
                CenterArc((0, 0), 0.175, -101.4783407829, 22.9566815658)
                Line((0.0497493719, -0.2450000038), (0.0348245598, -0.1715000001))
                CenterArc((0, 0), 0.2500000037, -78.5216592171, 22.0433184342)
                Line((0.1380630459, -0.2084192823), (0.0966441307, -0.1458934954))
                CenterArc((0, 0), 0.175, -56.4783407829, 22.9566815658)
                Line((0.2084192823, -0.1380630459), (0.1458934954, -0.0966441307))
                CenterArc((0, 0), 0.2500000037, -33.5216592171, 22.0433184342)
                Line((0.2450000038, -0.0497493719), (0.1715000001, -0.0348245598))
                CenterArc((0, 0), 0.175, -11.4783407829, 22.9566815658)
                Line((0.2450000038, 0.0497493719), (0.1715000001, 0.0348245598))
                CenterArc((0, 0), 0.2500000037, 11.4783407829, 22.0433184342)
                Line((0.2084192823, 0.1380630459), (0.1458934954, 0.0966441307))
                CenterArc((0, 0), 0.175, 33.5216592171, 22.9566815658)
                Line((0.1380630459, 0.2084192823), (0.0966441307, 0.1458934954))
                CenterArc((0, 0), 0.2500000037, 56.4783407829, 22.0433184342)
                Line((0.0497493719, 0.2450000038), (0.0348245598, 0.1715000001))
                CenterArc((0, 0), 0.175, 78.5216592171, 22.9566815658)
                Line((-0.0497493719, 0.2450000038), (-0.0348245598, 0.1715000001))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.1000000015, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


# Description: This is a triangular prism or wedge-shaped block with a elongated rectangular body, featuring a pointed triangular cross-section and tapered geometry along its length.
def model_41508_534c7804_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 75, perimeter: 40
            with BuildLine():
                Line((9.0340963014, -0.688099876), (-5.9659036986, -0.688099876))
                Line((9.0340963014, 4.311900124), (9.0340963014, -0.688099876))
                Line((-5.9659036986, 4.311900124), (9.0340963014, 4.311900124))
                Line((-5.9659036986, -0.688099876), (-5.9659036986, 4.311900124))
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2)
    return part.part


# Description: This is a flat parallelogram-shaped plate or panel with a blue finish, featuring a simple geometric form with no holes, slots, or additional features—essentially a basic four-sided planar component.
def model_41508_aa38f8d5_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2150, perimeter: 186
            with BuildLine():
                Line((47, -40.5), (-3, -40.5))
                Line((47, 2.5), (47, -40.5))
                Line((-3, 2.5), (47, 2.5))
                Line((-3, -40.5), (-3, 2.5))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


# Description: This is a polyhedron or truncated geometric solid with an irregular, faceted structure featuring multiple planar surfaces in varying shades of blue and dark gray, appearing to be a chamfered or truncated cubic form without any holes, slots, or curves.
def model_41512_c1a779f2_0000():
    """Model: wine opener v5"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2500000019, perimeter: 2.0000000075
            with BuildLine():
                Line((0.2000000104, -0.0000000075), (0.200000003, -0.5000000075))
                Line((0.200000003, -0.5000000075), (0.7000000104, -0.5000000075))
                Line((0.7000000104, -0.5000000075), (0.7000000104, -0.0000000075))
                Line((0.7000000104, -0.0000000075), (0.2000000104, -0.0000000075))
            make_face()
        # OneSide extrude, distance=0.4
        extrude(amount=0.4)
    return part.part


# Description: This is a cylindrical sleeve or tube with a tapered or conical end on one side, featuring a threaded or grooved surface along its length, commonly used as a connector, adapter, or fastening component.
def model_41512_c1a779f2_0002():
    """Model: Scissors v11"""
    with BuildPart() as part:
        # Sketch2 -> Extrude2 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 6.7426990817, perimeter: 15.2707963268
            with BuildLine():
                Line((1.35, 2), (-5, 2))
                CenterArc((1.35, 2.5), 0.5, -90, 180)
                Line((-5, 3), (1.35, 3))
                Line((-5, 2), (-5, 3))
            make_face()
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


# Description: This is an oval or elliptical structural frame/shell featuring a mesh or lattice pattern with internal diagonal and radial bracing elements that provide structural support across the curved surface.
def model_41512_c1a779f2_0004():
    """Model: can opener v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 5.067074791, perimeter: 7.9796453401
            with Locations((-3, 2)):
                Circle(1.27)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)
    return part.part


# Description: This is a curved blade or hook-shaped component with a tapered rectangular body transitioning to a rounded, concave cutting edge at the top, typical of a scraper, hook tool, or similar implement.
def model_41512_c1a779f2_0005():
    """Model: rope cutter v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 14.7640968391, perimeter: 20.2942193175
            with BuildLine():
                Line((-1.8110024015, 2.9513176149), (0.4347550493, 1.7924172675))
                CenterArc((-2.2000000328, 1.7651034092), 2.6348966563, 0.5939499846, 89.4060500154)
                Line((-7.7000000328, 4.4000000656), (-2.2000000328, 4.4000000656))
                Line((-7.7000000328, 4.4000000656), (-7.0741919326, 1.7215818581))
                Line((-1.8110024015, 2.9513176149), (-7.0741919326, 1.7215818581))
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)
    return part.part


# Description: These are two tapered hexagonal or polygonal pencil-shaped rods with a pointed end, featuring a textured or knurled surface along their length, commonly used as stylus tips or marking tools in technical applications.
def model_41518_e3d1e89c_0000():
    """Model: Component1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 18 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 15), x_dir=(1, 0, 0), z_dir=(0, 0, 1))) as sk:
            # Profile area: 0.7720205937, perimeter: 4.5211015529
            with BuildLine():
                CenterArc((-0.1, 1.45), 0.05, 90, 90)
                Line((-0.15, 1.45), (-0.15, 1.3500000194))
                CenterArc((-0.2, 1.3500000194), 0.05, -90, 90)
                CenterArc((-0.2, 1.1500000194), 0.15, 90, 90)
                Line((-0.35, 1.1500000194), (-0.35, 0.9666666801))
                CenterArc((-0.85, 0.9666666801), 0.5, -22.0208314854, 22.0208314854)
                CenterArc((0.0749999863, 0.0125000076), 0.8948638138, 121.0438758328, 46.8613673545)
                Line((-0.8085410234, 0.1829179758), (-0.8000000119, 0.200000003))
                CenterArc((-0.9427051088, 0.2500000015), 0.15, -90, 63.4349546286)
                Line((-0.95, 0.1000000015), (-0.9427051088, 0.1000000015))
                CenterArc((-0.95, 0.0500000015), 0.05, 90, 90)
                Line((-1, 0), (-1, 0.0500000015))
                Line((0, 0), (-1, 0))
                Line((0, 0), (0, 1.5))
                Line((0, 1.5), (-0.1, 1.5))
            make_face()
            # Profile area: 0.7720205937, perimeter: 4.5211015529
            with BuildLine():
                Line((25, 0), (25, 1.5))
                Line((26, 0), (25, 0))
                Line((26, 0), (26, 0.0500000015))
                CenterArc((25.95, 0.0500000015), 0.05, 0, 90)
                Line((25.95, 0.1000000015), (25.9427051088, 0.1000000015))
                CenterArc((25.9427051088, 0.2500000015), 0.15, -153.4349546286, 63.4349546286)
                Line((25.8085410234, 0.1829179758), (25.8000000119, 0.200000003))
                CenterArc((24.9250000137, 0.0125000076), 0.8948638138, 12.0947568127, 46.8613673545)
                CenterArc((25.85, 0.9666666801), 0.5, -180, 22.0208314854)
                Line((25.35, 1.1500000194), (25.35, 0.9666666801))
                CenterArc((25.2, 1.1500000194), 0.15, 0, 90)
                CenterArc((25.2, 1.3500000194), 0.05, -180, 90)
                Line((25.15, 1.45), (25.15, 1.3500000194))
                CenterArc((25.1, 1.45), 0.05, 0, 90)
                Line((25.1, 1.5), (25, 1.5))
            make_face()
        # TwoSides extrude, along=1.5, against=-16.5
        extrude(amount=1.5)
        extrude(sk.sketch, amount=-16.5)
    return part.part


# Description: This is a 3D CAD mesh model of an oval or ellipsoidal shell structure with a smooth, curved surface and radiating linear patterns or ribs running across its body.
def model_41524_f2a1b892_0001():
    """Model: Component9"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-1.525, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((1.6000000238, 2.2000000328)):
                Circle(0.15)
        # OneSide extrude, distance=0.025
        extrude(amount=0.025)
    return part.part


# Description: This is an oval or elliptical shell with radial ribbing, featuring a domed surface with evenly-spaced linear ribs that radiate outward from a central point, creating a fan-like or gear-tooth aesthetic pattern across its curved surface.
def model_41524_f2a1b892_0002():
    """Model: Component11"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-1.525, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((2.0000000298, 1.5000000224)):
                Circle(0.25)
        # OneSide extrude, distance=0.025
        extrude(amount=0.025)
    return part.part


# Description: This is a parallelogram-shaped flat bar or shim with rounded corners, featuring a uniform rectangular cross-section and a slight trapezoidal profile suggesting a 3D wedge or angled plate design.
def model_41524_f2a1b892_0005():
    """Model: Component16"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 12 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 3), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.2978539906, perimeter: 2.5141593041
            with BuildLine():
                CenterArc((-1.2500000194, 0.250000003), 0.05, 180, 90)
                Line((-1.2500000194, 0.200000003), (-1.0500000149, 0.200000003))
                CenterArc((-1.0500000149, 0.250000003), 0.05, -90, 90)
                Line((-1.0000000149, 0.250000003), (-1.0000000149, 1.1500000179))
                CenterArc((-1.0500000149, 1.1500000179), 0.05, 0, 90)
                Line((-1.0500000149, 1.2000000179), (-1.2500000194, 1.2000000179))
                CenterArc((-1.2500000194, 1.1500000179), 0.05, 90, 90)
                Line((-1.3000000194, 1.1500000179), (-1.3000000194, 0.250000003))
            make_face()
        # OneSide extrude, distance=0.01
        extrude(amount=0.01)
    return part.part


# Description: This is a cylindrical capsule or rounded rectangular tube with hemispherical ends, featuring a smooth curved outer surface and an internal hollow cavity, commonly used as a structural component, container, or pressure vessel.
def model_41524_f2a1b892_0013():
    """Model: Component6"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(-0.45, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            with Locations((0, 1.5000000224)):
                Circle(0.3)
        # OneSide extrude, distance=0.775
        extrude(amount=0.775)
    return part.part


# Description: This is a long, slender rectangular tube or channel with a hollow interior cross-section, featuring sharp edges and a consistent profile along its length, angled diagonally in the view.
def model_41593_d3d842f7_0000():
    """Model: 15: Foam Legs"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.8584073464, perimeter: 7.1415926536
            with BuildLine():
                Line((0, 0), (2, 0))
                Line((0, -2), (0, 0))
                CenterArc((2, -2), 2, 90, 90)
            make_face()
        # OneSide extrude, distance=18
        extrude(amount=18)
    return part.part


# Description: This is a parallelogram-shaped structural bracket or frame with a hollow, latticed interior featuring internal cross-bracing and triangulated reinforcement patterns, designed for lightweight strength and rigidity.
def model_41593_d3d842f7_0001():
    """Model: 11: LED Cover"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints, 11 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 235.8340961091, perimeter: 76.550972451
            with BuildLine():
                Line((0.5, 0), (0.5, -11.43))
                Line((21.455, -11.43), (0.5, -11.43))
                Line((21.455, 0), (21.455, -11.43))
                Line((0.5, 0), (21.455, 0))
            make_face()
            with BuildLine():
                CenterArc((3.9925, -5.715), 0.625, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((10.9775, -5.715), 0.625, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((17.9625, -5.715), 0.625, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


# Description: This is a dark blue plastic or metal channel/duct component with an elongated rectangular profile, featuring a hollow central passage, a mounting flange on one side, and angled end caps for directional airflow or cable routing.
def model_41593_d3d842f7_0003():
    """Model: 13:Foam Sides"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 8 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 76, perimeter: 50
            with BuildLine():
                Line((-20, 4), (-17, 4))
                Line((-17, 4), (-17, 0))
                Line((-3, 0), (-17, 0))
                Line((-3, 4), (-3, 0))
                Line((0, 4), (-3, 4))
                Line((0, 5), (0, 4))
                Line((-20, 5), (0, 5))
                Line((-20, 4), (-20, 5))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


# Description: This is a U-shaped bracket or handle with two parallel vertical legs connected by a horizontal top bar, featuring a hollow rectangular opening and rounded corners throughout the structure.
def model_41593_d3d842f7_0004():
    """Model: 10 : Handle"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 13 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 21.4634954085, perimeter: 43.853981634
            with BuildLine():
                Line((11, 4), (11, 0))
                Line((11, 0), (12, 0))
                Line((12, 0), (12, 4.5))
                CenterArc((10.5, 4.5), 1.5, 0, 90)
                Line((10.5, 6), (1.5, 6))
                CenterArc((1.5, 4.5), 1.5, 90, 90)
                Line((0, 4.5), (0, 0))
                Line((0, 0), (1, 0))
                Line((1, 0), (1, 4))
                CenterArc((2, 4), 1, 90, 90)
                Line((2, 5), (10, 5))
                CenterArc((10, 4), 1, 0, 90)
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


# Description: This is a streamlined aerospace or marine fairing/cowling with an elongated, tapered diamond or lance-like shape, featuring internal ribbed reinforcement structure and dark edge frames for structural integrity.
def model_41593_d3d842f7_0007():
    """Model: 7:LightSwitchCover"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 11 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 77.0629213038, perimeter: 46.8073670025
            with BuildLine():
                Line((-12.5575, -11.43), (-19.5425, -11.43))
                Line((-12.5575, 0), (-12.5575, -11.43))
                Line((-19.5425, 0), (-12.5575, 0))
                Line((-19.5425, -11.43), (-19.5425, 0))
            make_face()
            with BuildLine():
                CenterArc((-16, -8.73125), 0.238125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-16, -2.69875), 0.238125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((-16.52625, -6.985), (-15.57375, -6.985))
                Line((-16.52625, -4.445), (-16.52625, -6.985))
                Line((-15.57375, -4.445), (-16.52625, -4.445))
                Line((-15.57375, -6.985), (-15.57375, -4.445))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


# Description: This is a trapezoidal or wedge-shaped prism with an asymmetrical form featuring angled faces, a rectangular main body, and beveled or chamfered edges that create a complex polyhedral geometry with no apparent holes or slots.
def model_41594_d49b5e5c_0000():
    """Model: keychain"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.6432007962, perimeter: 3.6258042431
            with BuildLine():
                Line((0, 1.6469615977), (-0.4840144035, 1.6469615977))
                Line((0, 2.9758493157), (0, 1.6469615977))
                Line((-0.4840144035, 2.9758493157), (0, 2.9758493157))
                Line((-0.4840144035, 1.6469615977), (-0.4840144035, 2.9758493157))
            make_face()
        # OneSide extrude, distance=-1.27
        extrude(amount=-1.27)
    return part.part


# Description: This is a tapered cylindrical rod or pin with a smooth, gradually narrowing shaft that transitions from a slightly thicker diameter at one end to a point or smaller diameter at the other end.
def model_41595_e15895be_0008():
    """Model: Back Walls"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 4.8386955474, perimeter: 9.189801224
            with BuildLine():
                Line((115.5700036883, 3.8100001216), (116.84, 1.27))
                Line((116.84, 1.27), (118.11, 1.27))
                Line((118.11, 1.27), (118.11, 3.8100001216))
                Line((118.11, 3.8100001216), (115.5700036883, 3.8100001216))
            make_face()
        # TwoSides extrude (symmetric), distance=53.34
        extrude(amount=53.34, both=True)
    return part.part


# Description: This is a shallow, elongated rectangular tray or pan with a tapered wedge shape, featuring a flat top surface, sloped sides, and a recessed base with subtle depth variation.
def model_41599_f66b4e5b_0013():
    """Model: new mount v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 25.0000003725, perimeter: 20.000000149
            with BuildLine():
                Line((0, 5), (0, 0))
                Line((-5.0000000745, 5), (0, 5))
                Line((-5.0000000745, 0), (-5.0000000745, 5))
                Line((0, 0), (-5.0000000745, 0))
            make_face()
        # OneSide extrude, distance=0.6
        extrude(amount=0.6)
    return part.part


# Description: This is a long, narrow rectangular trim or molding piece with a slightly tapered profile, featuring a curved upper surface and angled edges that give it a streamlined, aerodynamic appearance.
def model_41599_f66b4e5b_0015():
    """Model: wing v12 (2)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude3 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.7570216114, perimeter: 7.6572849297
            with BuildLine():
                CenterArc((6.9092156202, 4.8045688267), 0.1, 162.8485329649, 108.3960094767)
                Line((6.9113875857, 4.7045924167), (10.0049576047, 4.7717995451))
                CenterArc((10, 5), 0.2282543, -88.7554575585, 177.5109125348)
                Line((6.9113875932, 5.2954077226), (10.004957615, 5.2282004547))
                CenterArc((6.9092156231, 5.1954313127), 0.1, 88.7554549764, 108.3960102808)
                CenterArc((6.6761690771, 5.1235076274), 0.1438928231, -59.1297540935, 76.2812193507)
                CenterArc((6.6761694739, 4.8764923966), 0.1438924071, -17.1514670351, 76.2813061751)
            make_face()
        # OneSide extrude, distance=0.05
        extrude(amount=0.05)
    return part.part


# Description: This is a cylindrical filter or strainer basket with an open top and a mesh or perforated surface on the upper portion, featuring a solid curved sidewall body.
def model_41624_a15f83c1_0007():
    """Model: Button 3 v1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.1309733553, perimeter: 3.7699111843
            Circle(0.6)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


# Description: This is a cylindrical mesh container or filter housing with an open top, featuring a curved body with vertical ribbing and a mesh insert panel visible on the upper inner surface.
def model_41624_a15f83c1_0023():
    """Model: Scratch Toggle v2 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.1309733553, perimeter: 3.7699111843
            with Locations((2.4443096338, 1.330564949)):
                Circle(0.6)
        # OneSide extrude, distance=0.6
        extrude(amount=0.6)
    return part.part


# Description: This is a flat, quadrilateral plate or panel with a trapezoidal shape, featuring a thin profile with internal triangular reinforcement ribs or bracing elements visible on the top surface.
def model_41630_23cbce49_0000():
    """Model: buttonbase"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-7.1470300595, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.45161, perimeter: 9.779
            with BuildLine():
                Line((-3.086100073, -6.8199), (-3.086100073, -6.5024))
                Line((1.485899927, -6.8199), (-3.086100073, -6.8199))
                Line((1.485899927, -6.5024), (1.485899927, -6.8199))
                Line((-3.086100073, -6.5024), (1.485899927, -6.5024))
            make_face()
        # OneSide extrude, distance=4.572
        extrude(amount=4.572)
    return part.part


# Description: This is a flat, trapezoidal plate or bracket with a beveled top edge and internal triangular ribbing or reinforcement struts for structural support.
def model_41646_6c1f1ff1_0005():
    """Model: Board v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 38.9196919281, perimeter: 24.8059748638
            with BuildLine():
                Line((0, 0), (0, -5.715))
                Line((0, -5.715), (6.6675, -5.715))
                Line((6.6675, -5.715), (6.6675, -5.461))
                Line((6.6675, -5.461), (6.9029578147, -5.2256671016))
                Line((6.9029578147, -5.2256671016), (6.9029578147, -1.4791671016))
                Line((6.6040002108, -1.2700000405), (6.9029578147, -1.4791671016))
                Line((6.6040002108, -0.2540000081), (6.6040002108, -1.2700000405))
                Line((6.3500002027, 0), (6.6040002108, -0.2540000081))
                Line((0, 0), (6.3500002027, 0))
            make_face()
        # OneSide extrude, distance=0.3175
        extrude(amount=0.3175)
    return part.part


# Description: This is a simple cylindrical rod or shaft with rounded ends, featuring a smooth, elongated rectangular profile with no holes, slots, or other features.
def model_41648_577daf16_0002():
    """Model: XSmall Leg"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 9 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.607494946, perimeter: 3.1980359813
            with BuildLine():
                CenterArc((0, 0), 0.45, 5.9869394903, 167.877107184)
                Line((-0.4474219803, 0.0480996006), (-0.3500000052, 0.0480996006))
                Line((-0.3500000052, 0.0480996006), (-0.3500000052, -0.1000000015))
                Line((-0.3500000052, -0.1000000015), (-0.438748219, -0.1000000015))
                CenterArc((0, 0), 0.45, -167.1604113985, 154.320822797)
                Line((0.3500000052, -0.1000000015), (0.438748219, -0.1000000015))
                Line((0.3500000052, 0.0469357922), (0.3500000052, -0.1000000015))
                Line((0.4475455635, 0.0469357922), (0.3500000052, 0.0469357922))
            make_face()
        # OneSide extrude, distance=20
        extrude(amount=20)
    return part.part


# Description: This is a hexagonal prism or wedge-shaped block with a trapezoidal profile, featuring flat faces and angular edges, appearing to be a structural component or support element with no holes or slots.
def model_41648_577daf16_0006():
    """Model: Block"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 4 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 2, perimeter: 6
            with BuildLine():
                Line((0, 0), (0, 2))
                Line((0, 2), (-1, 2))
                Line((-1, 2), (-1, 0))
                Line((0, 0), (-1, 0))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


# Description: This is a cylindrical disc or pulley with a flat front face and a ribbed or grooved curved back surface, likely designed for power transmission or mechanical coupling applications.
def model_41649_4ed08803_0000():
    """Model: Component16"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 6.1575217845, perimeter: 8.7964595611
            with Locations((-11.9000001773, -2.2000000328)):
                Circle(1.4000000209)
        # Symmetric extrude, each_side=0.3
        extrude(amount=0.3, both=True)
    return part.part


# Description: This is a toroidal or ring-shaped component with a hollow center and uniform cross-section, featuring a smooth, curved outer surface with a defined inner bore, commonly used as a magnetic core, structural ring, or cylindrical sleeve.
def model_41649_4ed08803_0001():
    """Model: Component15"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(3.5, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))) as sk:
            # Profile area: 0.1605352311, perimeter: 4.5867248904
            with BuildLine():
                CenterArc((0, -4.5), 0.3999999389, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, -4.5), 0.33, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # TwoSides extrude, along=0.3, against=-0.05
        extrude(amount=0.3)
        extrude(sk.sketch, amount=-0.05)
    return part.part


# Description: This is an oval-shaped acoustic or structural enclosure featuring a curved elliptical dome with internal radial ribbing/bracing and a solid cylindrical base or flange ring at the bottom.
def model_41650_9417da80_0003():
    """Model: Disk v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2642079422, perimeter: 1.8221237391
            Circle(0.29)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


# Description: This is an elongated hexagonal prism or wedge-shaped component with a tapered left end, featuring a recessed slot or groove running along its top surface and a cutout cavity on the right side.
def model_41650_9417da80_0012():
    """Model: first screw v7"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0103446844, perimeter: 0.5137873762
            with BuildLine():
                Line((0.1034468441, -0.025), (0.1034468441, 0.025))
                Line((0.1034468441, 0.025), (-0.1034468441, 0.025))
                Line((-0.1034468441, 0.025), (-0.1034468441, -0.025))
                Line((-0.1034468441, -0.025), (0.1034468441, -0.025))
            make_face()
        # OneSide extrude, distance=0.05
        extrude(amount=0.05)
    return part.part


# Description: This is a cylindrical or semi-cylindrical housing or cover with a curved top surface, featuring longitudinal ribs or corrugations running along its length and an open rectangular slot or access opening on the upper surface.
def model_41653_71b50655_0003():
    """Model: Latch Piece 1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.1413716694, perimeter: 1.5424777961
            with BuildLine():
                Line((13.9815453035, 2.4482554471), (14.5725529219, 2.5517445529))
                CenterArc((14.2770491127, 2.5), 0.3, 9.9321501131, 180)
            make_face()
        # OneSide extrude, distance=0.6
        extrude(amount=0.6)
    return part.part


# Description: This is a triangular or wedge-shaped 3D part with a tapered profile, featuring a sloped top surface and angled sides that converge toward one end, resembling a bent or folded plate structure.
def model_41654_46b2965e_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 108.75, perimeter: 47.8234551885
            with BuildLine():
                Line((7.5, 5), (0, -10))
                Line((-7, 5), (7.5, 5))
                Line((0, -10), (-7, 5))
            make_face()
        # OneSide extrude, distance=4
        extrude(amount=4)
    return part.part


# Description: This is a cylindrical ring or bushing with an elliptical or slot-shaped opening through its center, featuring a mesh-textured outer surface and a solid dark body.
def model_41654_e75f89df_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
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
        # OneSide extrude, distance=2
        extrude(amount=2)
    return part.part


# Description: This is a cylindrical roller or spacer with a rounded hemispherical end on one side and a flat or slightly recessed end on the other, featuring a smooth cylindrical body with a uniform diameter throughout its length.
def model_41672_d0a1ce4a_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.12920692, perimeter: 1.2742299803
            Circle(0.2028)
        # OneSide extrude, distance=1.3
        extrude(amount=1.3)
    return part.part


# Description: This is a dark blue rectangular duct or channel with a long, slender box-like shape, featuring angled end caps and internal ribbed or structural reinforcement patterns along its length.
def model_41680_49185107_0006():
    """Model: Slate Connection brace"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 122.5804, perimeter: 58.42
            with BuildLine():
                Line((-35.5257982941, 0.310134095), (-35.5257982941, 24.440134095))
                Line((-35.5257982941, 24.440134095), (-40.6057982941, 24.440134095))
                Line((-40.6057982941, 24.440134095), (-40.6057982941, 0.310134095))
                Line((-40.6057982941, 0.310134095), (-35.5257982941, 0.310134095))
            make_face()
        # OneSide extrude, distance=88.9
        extrude(amount=88.9)
    return part.part


# Description: This is a long, narrow rectangular beam or rail with a trapezoidal cross-section, featuring angled end caps on both sides and what appears to be a central slot or channel running along its length.
def model_41680_49185107_0010():
    """Model: Side Bumper"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 11.5674607464), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 620.2374692, perimeter: 254.34798
            with BuildLine():
                Line((137.7074192147, 25.4), (137.7074192147, 30.48))
                Line((137.7074192147, 30.48), (15.6134292147, 30.48))
                Line((15.6134292147, 30.48), (15.6134292147, 25.4))
                Line((15.6134292147, 25.4), (137.7074192147, 25.4))
            make_face()
        # OneSide extrude, distance=6.35
        extrude(amount=6.35)
    return part.part


# Description: This is a hexagonal or square shaft/rod with a tapered or chamfered end, featuring a long, slender cylindrical body with a pointed or beveled tip at one end.
def model_41680_49185107_0011():
    """Model: End Bumber"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(279.3124192147, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 629.3185598735, perimeter: 268.0580086512
            with BuildLine():
                Line((148.8049469707, 25.6074718987), (19.6484707464, 25.6074718987))
                Line((148.8049469707, 30.48), (148.8049469707, 25.6074718987))
                Line((19.6484707464, 30.48), (148.8049469707, 30.48))
                Line((19.6484707464, 25.6074718987), (19.6484707464, 30.48))
            make_face()
        # OneSide extrude, distance=6.35
        extrude(amount=6.35)
    return part.part


# Description: This is a sundial or angle-measuring tool featuring a flat rectangular base plate with an angled gnomon (pointer) mounted perpendicular to it, designed to cast shadows for time or angle measurement.
def model_41681_321971ae_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 12.5806204015, perimeter: 20.3200002432
            with BuildLine():
                Line((0, 0), (0, 1.7780000567))
                Line((0, 1.7780000567), (-2.8575, 1.7780000567))
                Line((-2.8575, 3.8100001216), (-2.8575, 1.7780000567))
                Line((-3.4925, 3.8100001216), (-2.8575, 3.8100001216))
                Line((-3.4925, 1.7780000567), (-3.4925, 3.8100001216))
                Line((-6.35, 1.7780000567), (-3.4925, 1.7780000567))
                Line((-6.35, 0), (-6.35, 1.7780000567))
                Line((0, 0), (-6.35, 0))
            make_face()
        # OneSide extrude, distance=0.3175
        extrude(amount=0.3175)
    return part.part


# Description: This is a flat, elongated parallelogram-shaped panel or trim piece with a dark gray frame and blue recessed sections, featuring curved slot cutouts and a central oval opening for aerodynamic or aesthetic purposes.
def model_41681_3dc1aa23_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 12.0396567269, perimeter: 19.5473228322
            with BuildLine():
                Line((5.23875, 2.5400000811), (5.23875, 0))
                Line((0, 2.5400000811), (5.23875, 2.5400000811))
                Line((0, 0), (0, 2.5400000811))
                Line((5.23875, 0), (0, 0))
            make_face()
            with BuildLine():
                CenterArc((2.619375, 1.2700000405), 0.635, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.15875
        extrude(amount=0.15875)
    return part.part


# Description: This is a torus or ring-shaped gasket/seal with a smooth, rounded oval cross-section and continuous curved geometry, featuring a hollow center opening and textured surface finish.
def model_41681_607f4353_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 6.3338434887, perimeter: 19.9491133503
            with BuildLine():
                CenterArc((0, 0), 1.905, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.27, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.15875
        extrude(amount=0.15875)
    return part.part


# Description: This is a rectangular frame or bracket with an open center, featuring two parallel flanged rails with angled end caps and a hinged or pivoting top section.
def model_41681_bab3a334_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 13.4354569269, perimeter: 36.3220000486
            with BuildLine():
                Line((0, 0), (5.715, 0))
                Line((5.715, 0), (5.715, 3.81))
                Line((5.715, 3.81), (3.175, 3.81))
                Line((3.175, 3.81), (3.175, 5.715))
                Line((3.175, 5.715), (2.5400000811, 5.715))
                Line((2.5400000811, 5.715), (2.54, 3.8100001216))
                Line((0, 3.8100001216), (2.54, 3.8100001216))
                Line((0, 0), (0, 3.8100001216))
            make_face()
            with BuildLine():
                Line((0.5080000162, 3.3020001054), (5.2070000162, 3.3020001054))
                Line((5.2070000162, 3.3020001054), (5.2070000162, 1.2700000405))
                Line((0.5080000162, 1.2700000405), (5.2070000162, 1.2700000405))
                Line((0.5080000162, 3.3020001054), (0.5080000162, 1.2700000405))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.3175
        extrude(amount=0.3175)
    return part.part


# Description: This is a toroidal (donut-shaped) ring featuring a smooth, curved outer surface with a distinctive mesh or diamond-pattern texture applied to portions of its circumference, creating a ribbed or knurled appearance on alternating sections.
def model_41685_df8ac866_0004():
    """Model: Outer Wheel Edge"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 51.2472301617, perimeter: 45.5530934771
            with BuildLine():
                CenterArc((0, 0), 4.75, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 2.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=1.1
        extrude(amount=1.1, both=True)
    return part.part


# Description: This is a cylindrical tube or pipe with a uniform circular cross-section, featuring rounded ends and a slightly tapered or beveled edge at the top.
def model_41685_df8ac866_0015():
    """Model: Top Shaft"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 7.5476763502, perimeter: 9.7389372261
            Circle(1.55)
        # OneSide extrude, distance=28
        extrude(amount=28)
    return part.part


# Description: This is a tapered cylindrical rod or needle with a straight, elongated shape that gradually narrows from one end to a point, featuring a simple linear geometry with no holes, slots, or flanges.
def model_41685_df8ac866_0016():
    """Model: Brake Pin"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0078539816, perimeter: 0.3141592654
            Circle(0.05)
        # OneSide extrude, distance=9.7
        extrude(amount=9.7)
    return part.part


# Description: This is a suppressor or silencer with a cylindrical body, featuring a tapered rounded end cap and what appears to be internal baffling or spiral grooves along its length for sound dampening.
def model_41685_df8ac866_0017():
    """Model: Back Wheel Pin"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            Circle(0.4)
        # OneSide extrude, distance=5
        extrude(amount=5)
    return part.part


# Description: This is a twisted or curved blade-like component with a tapered, elongated shape that features a rectangular flange at the top and a pointed or sharp edge at the bottom, characteristic of an aerodynamic or hydrodynamic fin, rudder, or similar structural element.
def model_41691_96d262e4_0000():
    """Model: Component1"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 21.6049504338, perimeter: 25.5767039117
            with BuildLine():
                Line((-7.0923887594, 3.6280466591), (-7.0923887594, 7.2646130604))
                Line((-4.3180001378, 0), (-7.0923887594, 3.6280466591))
                Line((-4.3180001378, 11.938000381), (-4.3180001378, 0))
                Line((-7.0923887594, 7.2646130604), (-4.3180001378, 11.938000381))
            make_face()
        # Symmetric extrude, each_side=0.635
        extrude(amount=0.635, both=True)
    return part.part


# Description: This is a truncated wedge or chamfered rectangular block with a faceted top surface, featuring angular cuts on the left end and a tapered upper profile that transitions from a higher left side to a lower right side.
def model_41702_1533021d_0007():
    """Model: Attachment to Body"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.0000000894, perimeter: 8.0000000745
            with BuildLine():
                Line((-1.5000000224, -2.0000000298), (-1.5000000224, -1.0000000298))
                Line((1.5, -2.0000000298), (-1.5000000224, -2.0000000298))
                Line((1.5, -1), (1.5, -2.0000000298))
                Line((0, -1), (1.5, -1))
                Line((-1.5000000224, -1.0000000298), (0, -1))
            make_face()
        # OneSide extrude, distance=-1
        extrude(amount=-1)
    return part.part


# Description: This is a sleeping bag with an elongated, tapered mummy-style shape featuring a rounded hood at the head end, a zippered opening along one side, and a streamlined body that narrows toward the feet for thermal efficiency.
def model_41708_3a74f048_0008():
    """Model: ArmyKnifePlasticCover v6"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 13 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 24.9203046898, perimeter: 23.6557164342
            with BuildLine():
                CenterArc((-0.5080000486, 0.5080000486), 1.016, 90, 90)
                Line((-1.5240000486, 0.5080000486), (-1.5240000486, -7.6199999514))
                CenterArc((-0.5080000486, -7.6199999514), 1.016, 180, 90)
                Line((-0.5080000486, -8.6359999514), (0.0000000324, -8.6359999514))
                CenterArc((0.0000000324, -7.6199999514), 1.016, -90, 90)
                Line((1.0160000324, -7.6199999514), (1.0160000324, 0.5080000486))
                CenterArc((0.0000000324, 0.5080000486), 1.016, 0, 90)
                Line((0.0000000324, 1.5240000486), (-0.5080000486, 1.5240000486))
            make_face()
        # OneSide extrude, distance=0.254
        extrude(amount=0.254)
    return part.part


# Description: This is a rectangular storage box or container with a dark blue body and light blue top edge, topped with a cylindrical dark gray roll or handle, featuring a geometric faceted design on its front surface.
def model_41714_1d49f4d1_0002():
    """Model: letter_i"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0483870031, perimeter: 1.0160000324
            with BuildLine():
                Line((1.7805299774, 4.4444171438), (1.7805299774, 4.825417156))
                Line((1.9075299814, 4.4444171438), (1.7805299774, 4.4444171438))
                Line((1.9075299814, 4.825417156), (1.9075299814, 4.4444171438))
                Line((1.7805299774, 4.825417156), (1.9075299814, 4.825417156))
            make_face()
            # Profile area: 0.0101341493, perimeter: 0.356860584
            with Locations((1.8449854928, 4.9395409754)):
                Circle(0.0567961259)
        # OneSide extrude, distance=0.635
        extrude(amount=0.635)
    return part.part


# Description: This is a dual-chamber or folded box-like enclosure with an angular, V-shaped or chevron profile featuring two connected compartments with mesh or latticed side panels, solid top and bottom surfaces, and internal structural ribbing or bracing.
def model_41714_1d49f4d1_0007():
    """Model: Letter_W"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 25 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.1872384576, perimeter: 3.5421749724
            with BuildLine():
                Line((-6.3418228725, 5.0885069258), (-6.42311867, 5.1698027233))
                CenterArc((-6.4770002067, 5.1159211866), 0.0762, 45, 90)
                Line((-6.5308817434, 5.1698027233), (-6.612177541, 5.0885069258))
                CenterArc((-6.6660590777, 5.1423884625), 0.0762, -158.1985905136, 113.1985905136)
                Line((-6.7368090015, 5.114088493), (-6.8906669911, 5.498733467))
                Line((-6.8906669911, 5.498733467), (-6.9142502991, 5.4893001438))
                CenterArc((-6.8859503295, 5.41855022), 0.0762, 111.8014094864, 90)
                Line((-6.7739182227, 4.9332951738), (-6.9567002534, 5.3902502504))
                CenterArc((-6.7031682989, 4.9615951434), 0.0762, -158.1985905136, 113.1985905136)
                Line((-6.4770002067, 5.0800001621), (-6.6492867622, 4.9077136067))
                Line((-6.3047136512, 4.9077136067), (-6.4770002067, 5.0800001621))
                CenterArc((-6.2508321145, 4.9615951434), 0.0762, -135, 113.1985905136)
                Line((-5.99730016, 5.3902502504), (-6.1800821907, 4.9332951738))
                CenterArc((-6.0680500839, 5.41855022), 0.0762, -21.8014094864, 90)
                Line((-6.0633334223, 5.498733467), (-6.0397501143, 5.4893001438))
                Line((-6.0633334223, 5.498733467), (-6.2171914119, 5.114088493))
                CenterArc((-6.2879413357, 5.1423884625), 0.0762, -135, 113.1985905137)
            make_face()
        # OneSide extrude, distance=0.635
        extrude(amount=0.635)
    return part.part


# Description: This is a bracket or mounting clamp with a C-shaped profile featuring multiple rectangular slots or cutouts along its curved surfaces and a protruding flange or tab on the right side for attachment purposes.
def model_41714_1d49f4d1_0008():
    """Model: letter_g"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 46 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.1608584971, perimeter: 4.2645982849
            with BuildLine():
                Line((-5.9183988127, 4.2164001338), (-5.9183988127, 3.6289896595))
                CenterArc((-5.7913988127, 3.6289896595), 0.127, 180, 90)
                Line((-5.7913988127, 3.5019896595), (-5.5790896967, 3.5019896595))
                CenterArc((-5.5790896967, 3.6289896595), 0.127, -90, 83.235539281)
                CenterArc((-5.5028896967, 3.6045944429), 0.0508, 10.7049041764, 79.6968643728)
                Line((-5.5032459127, 3.655393194), (-5.5282896967, 3.6552175795))
                Line((-5.5282896967, 3.6289896595), (-5.5282896967, 3.6552175795))
                CenterArc((-5.5790896967, 3.6289896595), 0.0508, -90, 90)
                Line((-5.7913988127, 3.5781896595), (-5.5790896967, 3.5781896595))
                CenterArc((-5.7913988127, 3.6289896595), 0.0508, 180, 90)
                Line((-5.8421988127, 3.8192101458), (-5.8421988127, 3.6289896595))
                CenterArc((-5.7913988127, 3.8192101458), 0.0508, 90, 90)
                Line((-5.4918762513, 3.8700101458), (-5.7913988127, 3.8700101458))
                CenterArc((-5.4918762513, 3.9208101458), 0.0508, -90, 90)
                Line((-5.4410762513, 4.2164001338), (-5.4410762513, 3.9208101458))
                CenterArc((-5.4918762513, 4.2164001338), 0.0508, 0, 90)
                Line((-5.8675988127, 4.2672001338), (-5.4918762513, 4.2672001338))
                CenterArc((-5.8675988127, 4.2164001338), 0.0508, 90, 90)
            make_face()
            with BuildLine():
                Line((-5.7912001864, 4.1910001338), (-5.5497865263, 4.1910001338))
                CenterArc((-5.5497865263, 4.1402001338), 0.0508, 0, 90)
                Line((-5.4989865263, 4.1402001338), (-5.4989865263, 3.9878001256))
                CenterArc((-5.5497865263, 3.9878001256), 0.0508, -90, 90)
                Line((-5.5497865263, 3.9370001256), (-5.7912001864, 3.9370001256))
                CenterArc((-5.7912001864, 3.9878001256), 0.0508, 180, 90)
                Line((-5.8420001864, 3.9878001256), (-5.8420001864, 4.1402001338))
                CenterArc((-5.7912001864, 4.1402001338), 0.0508, 90, 90)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.635
        extrude(amount=0.635)
    return part.part


# Description: This is a rectangular mounting bracket or clamp with two parallel flanges connected by a central channel or slot, featuring mounting holes on the side flanges for fastening applications.
def model_41714_1d49f4d1_0009():
    """Model: letter_t"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 23 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0705582144, perimeter: 1.8312206726
            with BuildLine():
                Line((-7.5396702593, 4.0639999509), (-7.6199999076, 4.0639999509))
                Line((-7.5396702593, 4.1324387999), (-7.5396702593, 4.0639999509))
                Line((-7.6190033733, 4.1324387999), (-7.5396702593, 4.1324387999))
                CenterArc((-7.6190033733, 4.1578387999), 0.0254, -180, 90)
                Line((-7.6444033733, 4.3870252886), (-7.6444033733, 4.1578387999))
                Line((-7.7327489629, 4.3870252886), (-7.6444033733, 4.3870252886))
                Line((-7.7327489629, 4.1555022596), (-7.7327489629, 4.3870252886))
                CenterArc((-7.7581489629, 4.1555022596), 0.0254, -90, 90)
                Line((-7.8423887515, 4.1301022596), (-7.7581489629, 4.1301022596))
                Line((-7.8423887515, 4.0632598378), (-7.8423887515, 4.1301022596))
                Line((-7.7573322288, 4.0632598378), (-7.8423887515, 4.0632598378))
                CenterArc((-7.7573322288, 4.0378598378), 0.0254, 0, 90)
                Line((-7.7319322288, 3.7523298979), (-7.7319322288, 4.0378598378))
                Line((-7.6453999076, 3.7523298979), (-7.7319322288, 3.7523298979))
                Line((-7.6453999076, 4.0385999509), (-7.6453999076, 3.7523298979))
                CenterArc((-7.6199999076, 4.0385999509), 0.0254, 90, 90)
            make_face()
        # OneSide extrude, distance=0.635
        extrude(amount=0.635)
    return part.part


# Description: This is a tapered cylindrical rod or pin with a slightly conical shape, featuring a uniform diameter that gradually reduces toward one end, commonly used as a drift pin, alignment pin, or dowel in mechanical assemblies.
def model_41714_1d49f4d1_0010():
    """Model: Component18"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0005067075, perimeter: 0.0797964534
            with Locations((-7.8739999048, 3.7845999543)):
                Circle(0.0127)
        # OneSide extrude, distance=0.635
        extrude(amount=0.635)
    return part.part


# Description: This is a tubular suppressor or silencer component with a smooth cylindrical body, slightly tapered at one end, featuring minimal external features and designed for sound dampening applications.
def model_41714_1d49f4d1_0013():
    """Model: cyclinder_3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.3166921744, perimeter: 1.994911335
            with Locations((1.2699999809, 3.8099999428)):
                Circle(0.3175)
        # OneSide extrude, distance=3.937
        extrude(amount=3.937)
    return part.part


# Description: This is a long, slender rectangular prism or beam with a square or nearly-square cross-section, featuring a slight groove or channel running along its length and appearing to taper slightly toward the top end.
def model_41714_1d49f4d1_0016():
    """Model: supporting beam"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1290320082, perimeter: 1.5240000486
            with BuildLine():
                Line((0.7620000243, 2.286000073), (0.2540000081, 2.286000073))
                Line((0.2540000081, 2.286000073), (0.2540000081, 2.0320000648))
                Line((0.2540000081, 2.0320000648), (0.7620000243, 2.0320000648))
                Line((0.7620000243, 2.0320000648), (0.7620000243, 2.286000073))
            make_face()
        # OneSide extrude, distance=3.81
        extrude(amount=3.81)
    return part.part


# Description: This is a cylindrical rod or shaft with a long, slender tubular shape and slightly rounded ends, appearing to be a simple mechanical component used for structural support or rotational applications.
def model_41714_1d49f4d1_0017():
    """Model: cyclinder_4"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0506707479, perimeter: 0.797964534
            with Locations((0.7620000243, 1.7780000567)):
                Circle(0.127)
        # OneSide extrude, distance=2.54
        extrude(amount=2.54)
    return part.part


# Description: This is a parallelogram-shaped frame or bracket with a dark blue/gray finish, featuring an open rectangular center, angled side supports, and a small blue accent detail, likely designed as a mounting bracket or structural component.
def model_41715_e1936a52_0000():
    """Model: Sink Guard"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 33 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 739.1945754175, perimeter: 598.6427462458
            with BuildLine():
                Line((3.0480000973, -3.0480000973), (-86.0904732461, -3.0480000973))
                Line((3.0480000973, 45.7200014591), (3.0480000973, -3.0480000973))
                Line((-86.0904732461, 45.7200014591), (3.0480000973, 45.7200014591))
                Line((-86.0904732461, -3.0480000973), (-86.0904732461, 45.7200014591))
            make_face()
            with BuildLine():
                Line((-2.8940247963, -1.1756588075), (-57.7904736892, -1.1756588075))
                CenterArc((-57.7904736892, 1.8723411925), 3.048, 180, 90)
                Line((-60.8384736892, 1.8723411925), (-60.8384736892, 41.45280055))
                CenterArc((-57.7904736892, 41.45280055), 3.048, 90, 90)
                Line((-57.7904736892, 44.50080055), (-2.8940247963, 44.50080055))
                CenterArc((-2.8940247963, 41.45280055), 3.048, 0, 90)
                Line((0.1539752037, 41.45280055), (0.1539752037, 1.8723411925))
                CenterArc((-2.8940247963, 1.8723411925), 3.048, -90, 90)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((-79.8576010246, 42.6720005274), (-66.1416007609, 42.6720005274))
                CenterArc((-66.1416007609, 38.1000005274), 4.572, 0, 90)
                Line((-61.5696007609, 38.1000005274), (-61.5696007609, 7.6200000377))
                CenterArc((-66.1416007609, 7.6200000377), 4.572, -90, 90)
                Line((-66.1416007609, 3.0480000377), (-78.3336010246, 3.0480000377))
                CenterArc((-78.3336010246, 7.6200000377), 4.572, -180, 90)
                Line((-82.9056010246, 7.6200000377), (-82.9056010246, 39.6240005274))
                CenterArc((-79.8576010246, 39.6240005274), 3.048, 90, 90)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=3.048
        extrude(amount=3.048)
    return part.part


# Description: This is a cylindrical component with a fine mesh or perforated surface pattern, featuring a solid circular base and a hollow or latticed upper section, commonly used as a filter, strainer, or ventilation housing.
def model_41716_d55164d4_0002():
    """Model: Door knob"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 17.145), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.3166921744, perimeter: 1.994911335
            with Locations((11.1760003567, 5.0800001621)):
                Circle(0.3175)
        # OneSide extrude, distance=0.635
        extrude(amount=0.635)
    return part.part


# Description: This is a triangular pyramid or tetrahedral structure with a dark blue finish, featuring internal cross-bracing and triangulated geometric divisions across its faces, designed as a lightweight structural framework or lattice component.
def model_41716_d55164d4_0004():
    """Model: Side Walls"""
    with BuildPart() as part:
        # Sketch1 -> Extrude6 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 4 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 301.6968685297, perimeter: 80.6781149477
            with BuildLine():
                Line((0, 0), (0, 12.6999998093))
                Line((0, 12.6999998093), (-8.89, 21.5793530033))
                Line((-17.78, 12.7), (-8.89, 21.5793530033))
                Line((-17.78, 0), (-17.78, 12.7))
                Line((0, 0), (-17.78, 0))
            make_face()
            with BuildLine():
                CenterArc((-7.6200002432, 17.7800005674), 0.5080000162, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-10.1600003242, 17.7800005674), 0.5080000162, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-5.0800001907, 12.6999998093), 0.47625, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-12.6999998093, 12.6999998093), 0.47625, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.27
        extrude(amount=1.27)
    return part.part


# Description: This is a thin-walled, triangular pyramid or tetrahedral structure with a pointed apex at the top and a triangular base, featuring faceted surfaces with minimal internal geometry and no holes or slots.
def model_41716_d55164d4_0007():
    """Model: DORMER WALL1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.5, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 19.2573396, perimeter: 22.0554049654
            with BuildLine():
                Line((17.6499182404, 21.6099020062), (10.9106917837, 22.626057313))
                Line((10.9106917837, 22.626057313), (17.6499182404, 15.8949020062))
                Line((17.6499182404, 15.8949020062), (17.6499182404, 21.6099020062))
            make_face()
        # OneSide extrude, distance=-1.27
        extrude(amount=-1.27)
    return part.part


# Description: This is a wire or spring hook featuring a bent cylindrical shaft with a looped eye at the top and a tapered point at the bottom, designed for hanging or securing objects.
def model_41717_008d27ad_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 13 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 12.9165908562, perimeter: 131.877438993
            with BuildLine():
                Line((16.0036418163, 42.3916469569), (10.0036418163, 48.3916469569))
                Line((0.0379563914, 48.3916469569), (10.0036418163, 48.3916469569))
                Line((0.0379563914, 48.3916469569), (-0.4792008961, 47.8744896693))
                Line((-0.4792008961, 46.9916469569), (-0.4792008961, 47.8744896693))
                Line((-0.8792008961, 46.5916469569), (-0.4792008961, 46.9916469569))
                Line((-1.6792008961, 46.5916469569), (-0.8792008961, 46.5916469569))
                Line((-2.0792008961, 46.9916469569), (-1.6792008961, 46.5916469569))
                Line((-2.0792008961, 46.9916469569), (-2.0792008961, 47.7916469569))
                Line((-1.6792008961, 48.1916469569), (-2.0792008961, 47.7916469569))
                Line((-1.6792008961, 48.1916469569), (-1.8206222524, 48.3330683131))
                Line((-1.8206222524, 48.3330683131), (-2.2792008961, 47.8744896693))
                Line((-2.2792008961, 46.9088042444), (-2.2792008961, 47.8744896693))
                Line((-2.2792008961, 46.9088042444), (-1.7620436086, 46.3916469569))
                Line((-1.7620436086, 46.3916469569), (-0.7963581837, 46.3916469569))
                Line((-0.7963581837, 46.3916469569), (-0.2792008961, 46.9088042444))
                Line((-0.2792008961, 46.9088042444), (-0.2792008961, 47.7916469569))
                Line((0.1207991039, 48.1916469569), (-0.2792008961, 47.7916469569))
                Line((0.1207991039, 48.1916469569), (9.9207991039, 48.1916469569))
                Line((15.8036418163, 42.3088042444), (9.9207991039, 48.1916469569))
                Line((15.8036418163, 42.3088042444), (15.8036418163, 2.5075440499))
                Line((15.9036418163, 0), (15.8036418163, 2.5075440499))
                Line((15.9036418163, 0), (16.0036418163, 2.5075440499))
                Line((16.0036418163, 42.3916469569), (16.0036418163, 2.5075440499))
            make_face()
        # Symmetric extrude, each_side=0.2
        extrude(amount=0.2, both=True)
    return part.part


# Description: A double-ended wrench with hexagonal (or similar polygonal) socket heads at both ends connected by a long cylindrical shaft, designed for fastening or loosening nuts and bolts of two different sizes.
def model_41717_9450c6b4_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 12 constraints, 13 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.9641651672, perimeter: 20.1416516722
            with BuildLine():
                Line((3.6959623516, -1.0333793721), (4.1286860714, -0.9153638122))
                Line((4.4093446375, -0.4242113214), (4.1286860714, -0.9153638122))
                Line((4.2913290776, 0.0085123984), (4.4093446375, -0.4242113214))
                Line((4.2913290776, 0.0085123984), (3.8001765868, 0.2891709646))
                Line((3.4473765188, 0.1929527642), (3.8001765868, 0.2891709646))
                Line((3.4473765188, 0.1929527642), (3.3772118773, 0.0701646415))
                Line((3.3772118773, 0.0701646415), (0, 2))
                Line((0, 2), (-0.0992277877, 1.8263513716))
                Line((-0.3721042038, 1.7519305308), (-0.0992277877, 1.8263513716))
                Line((-0.3721042038, 1.7519305308), (-0.7194014606, 1.9503861062))
                Line((-0.7194014606, 1.9503861062), (-0.7938223014, 2.2232625223))
                Line((-0.595366726, 2.5705597791), (-0.7938223014, 2.2232625223))
                Line((-0.595366726, 2.5705597791), (-0.3224903099, 2.6449806199))
                Line((-0.3224903099, 2.6449806199), (0.0248069469, 2.4465250445))
                Line((0.0992277877, 2.1736486284), (0.0248069469, 2.4465250445))
                Line((0.0992277877, 2.1736486284), (0.2921805519, 2.2262721096))
                Line((0.2921805519, 2.2262721096), (0.1959623516, 2.5790721775))
                Line((-0.2951901392, 2.8597307437), (0.1959623516, 2.5790721775))
                Line((-0.727913859, 2.7417151838), (-0.2951901392, 2.8597307437))
                Line((-1.0085724252, 2.250562693), (-0.727913859, 2.7417151838))
                Line((-0.8905568653, 1.8178389732), (-1.0085724252, 2.250562693))
                Line((-0.3994043745, 1.537180407), (-0.8905568653, 1.8178389732))
                Line((-0.3994043745, 1.537180407), (0.0333193453, 1.6551959669))
                Line((0.0744208408, 1.7271235839), (0.0333193453, 1.6551959669))
                Line((0.0744208408, 1.7271235839), (3.4007722123, -0.1736486284))
                Line((3.4007722123, -0.1736486284), (3.5, 0))
                Line((3.5, 0), (3.7728764161, 0.0744208408))
                Line((4.1201736729, -0.1240347346), (3.7728764161, 0.0744208408))
                Line((4.1201736729, -0.1240347346), (4.1945945137, -0.3969111507))
                Line((3.9961389384, -0.7442084075), (4.1945945137, -0.3969111507))
                Line((3.7232625223, -0.8186292483), (3.9961389384, -0.7442084075))
                Line((3.7232625223, -0.8186292483), (3.3759652654, -0.6201736729))
                Line((3.3015444247, -0.3472972568), (3.3759652654, -0.6201736729))
                Line((3.1085916604, -0.399920738), (3.3015444247, -0.3472972568))
                Line((3.1085916604, -0.399920738), (3.2048098608, -0.752720806))
                Line((3.6959623516, -1.0333793721), (3.2048098608, -0.752720806))
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)
    return part.part


# Description: This is a flat steel plate or bracket with a parallelogram shape and three evenly-spaced circular holes drilled along its length for fastening or mounting purposes.
def model_41722_92ab0003_0002():
    """Model: knob faceplate"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 5 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 100.5671698064, perimeter: 57.4736808061
            with BuildLine():
                Line((0, 20.066), (0, 0))
                Line((0, 0), (5.08, 0))
                Line((5.08, 0), (5.08, 20.066))
                Line((5.08, 20.066), (0, 20.066))
            make_face()
            with BuildLine():
                CenterArc((2.5399999619, 16.509999752), 0.381, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((2.5399999619, 3.8099999428), 0.381, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((2.5399999619, 10.1599998474), 0.381, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.254
        extrude(amount=0.254)
    return part.part


# Description: This is a rectangular beam or rail component with a hollow rectangular cross-section, featuring two symmetrical cube-shaped end brackets or flanges on each end that appear to have angled faces for mounting or assembly purposes.
def model_41722_92ab0003_0003():
    """Model: door handle"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 11 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 40.3225000969, perimeter: 58.4199996948
            with BuildLine():
                Line((21.5899996948, 0), (24.1299996948, 0))
                Line((24.1299996948, 0), (24.13, 3.175))
                Line((24.13, 3.175), (0, 3.175))
                Line((0, 3.175), (0, 0))
                Line((0, 0), (2.54, 0))
                Line((2.54, 1.905), (2.54, 0))
                Line((21.5899996948, 1.905), (2.54, 1.905))
                Line((21.5899996948, 0), (21.5899996948, 1.905))
            make_face()
        # OneSide extrude, distance=2.54
        extrude(amount=2.54)
    return part.part


# Description: This is a corner guard or edge protector with an elongated L-shaped cross-section, featuring a long tapered body designed to protect and reinforce corner edges, with a notched or beveled end for installation.
def model_41722_92ab0003_0004():
    """Model: heat gaurd"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 7 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.6236987929, perimeter: 13.3353628014
            with BuildLine():
                Line((2.8428462676, 1.6607692285), (3.5348333313, 0))
                Line((3.5348333313, 0), (3.81, 0))
                Line((3.81, 0), (3.0773078193, 1.7584615255))
                CenterArc((1.9050000608, 1.2700000405), 1.2700000405, 22.6198615722, 134.7602734797)
                Line((0, 0), (0.7326923311, 1.7584615946))
                Line((0, 0), (0.2751666754, 0))
                Line((0.967153877, 1.6607692838), (0.2751666754, 0))
                CenterArc((1.9050000608, 1.2700000405), 1.0160000324, 22.6198615722, 134.7602734797)
            make_face()
        # OneSide extrude, distance=32.766
        extrude(amount=32.766)
    return part.part


# Description: A symmetrical structural component with two tall vertical towers or pylons connected by horizontal beams, featuring a central oval aperture and cable-like tensioning elements, resembling a bridge or suspension structure design.
def model_41722_92ab0003_0005():
    """Model: back spacer"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 5 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 3.3123328256, perimeter: 9.614911335
            with BuildLine():
                Line((-1.905, 1.905), (0, 1.905))
                Line((-1.905, 0), (-1.905, 1.905))
                Line((0, 0), (-1.905, 0))
                Line((0, 1.905), (0, 0))
            make_face()
            with BuildLine():
                CenterArc((-0.9525, 0.9525), 0.3175, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.905
        extrude(amount=1.905)
    return part.part


# Description: A flat, elongated parallelogram-shaped plate with a simple planar surface and no holes or additional features.
def model_41722_92ab0003_0006():
    """Model: back plate (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 15 constraints, 13 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 926.256212, perimeter: 132.3654680102
            with BuildLine():
                CenterArc((38.227, 23.241), 0.635, 0, 90)
                Line((38.227, 23.876), (0.635, 23.876))
                CenterArc((0.635, 23.241), 0.635, 90, 90)
                Line((0, 23.241), (0, 0.635))
                CenterArc((0.635, 0.635), 0.635, 180, 90)
                Line((0.635, 0), (38.227, 0))
                CenterArc((38.227, 0.635), 0.635, -90, 90)
                Line((38.862, 0.635), (38.862, 23.241))
            make_face()
            with BuildLine():
                CenterArc((0.635, 23.241), 0.3175, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0.635, 0.635), 0.3175, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((38.227, 0.635), 0.3175, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((38.227, 23.241), 0.3175, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.254
        extrude(amount=0.254)
    return part.part


# Description: This is a tetrahedron or triangular pyramid with a dark navy blue surface finish, featuring four triangular faces meeting at vertices with visible edge lines and a wireframe appearance.
def model_41722_92ab0003_0008():
    """Model: door"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 5 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 588.0428576511, perimeter: 102.7958226701
            with BuildLine():
                Line((0, 20.066), (0, 0))
                Line((0, 0), (29.337, 0))
                Line((29.337, 0), (29.337, 20.066))
                Line((29.337, 20.066), (0, 20.066))
            make_face()
            with BuildLine():
                CenterArc((3.81, 17.526), 0.3175, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((25.527, 17.526), 0.3175, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.254
        extrude(amount=0.254)
    return part.part


# Description: This is a simple cylindrical rod or shaft with rounded ends, featuring a smooth, uniform diameter throughout its length.
def model_41722_92ab0003_0009():
    """Model: heating element"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.2667686977, perimeter: 3.9898226701
            Circle(0.635)
        # OneSide extrude, distance=32.766
        extrude(amount=32.766)
    return part.part


# Description: A flat parallelogram-shaped plate with diagonal linear surface features or ribbing running across its face.
def model_41722_92ab0003_0010():
    """Model: rack"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 53 constraints, 50 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 166.45128, perimeter: 831.596
            with BuildLine():
                Line((0, 27.94), (0, 0))
                Line((0, 0), (32.766, 0))
                Line((32.766, 0), (32.766, 27.94))
                Line((32.766, 27.94), (0, 27.94))
            make_face()
            with BuildLine():
                Line((29.53385, 0.3175), (29.53385, 27.6225))
                Line((29.53385, 27.6225), (31.81985, 27.6225))
                Line((31.81985, 27.6225), (31.81985, 0.3175))
                Line((31.81985, 0.3175), (29.53385, 0.3175))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((29.21635, 27.6225), (26.93035, 27.6225))
                Line((29.21635, 0.3175), (29.21635, 27.6225))
                Line((26.93035, 0.3175), (29.21635, 0.3175))
                Line((26.93035, 27.6225), (26.93035, 0.3175))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((24.32685, 0.3175), (26.61285, 0.3175))
                Line((24.32685, 27.6225), (24.32685, 0.3175))
                Line((26.61285, 27.6225), (24.32685, 27.6225))
                Line((26.61285, 0.3175), (26.61285, 27.6225))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((24.00935, 27.6225), (21.72335, 27.6225))
                Line((24.00935, 0.3175), (24.00935, 27.6225))
                Line((21.72335, 0.3175), (24.00935, 0.3175))
                Line((21.72335, 27.6225), (21.72335, 0.3175))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((19.11985, 0.3175), (19.11985, 27.6225))
                Line((19.11985, 27.6225), (21.40585, 27.6225))
                Line((21.40585, 27.6225), (21.40585, 0.3175))
                Line((21.40585, 0.3175), (19.11985, 0.3175))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((18.80235, 27.6225), (16.51635, 27.6225))
                Line((18.80235, 0.3175), (18.80235, 27.6225))
                Line((16.51635, 0.3175), (18.80235, 0.3175))
                Line((16.51635, 27.6225), (16.51635, 0.3175))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((13.91285, 0.3175), (13.91285, 27.6225))
                Line((13.91285, 27.6225), (16.19885, 27.6225))
                Line((16.19885, 27.6225), (16.19885, 0.3175))
                Line((16.19885, 0.3175), (13.91285, 0.3175))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((13.59535, 27.6225), (11.30935, 27.6225))
                Line((13.59535, 0.3175), (13.59535, 27.6225))
                Line((11.30935, 0.3175), (13.59535, 0.3175))
                Line((11.30935, 27.6225), (11.30935, 0.3175))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((8.70585, 0.3175), (8.70585, 27.6225))
                Line((8.70585, 27.6225), (10.99185, 27.6225))
                Line((10.99185, 27.6225), (10.99185, 0.3175))
                Line((10.99185, 0.3175), (8.70585, 0.3175))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((6.10235, 0.3175), (6.10235, 27.6225))
                Line((6.10235, 27.6225), (8.38835, 27.6225))
                Line((8.38835, 27.6225), (8.38835, 0.3175))
                Line((8.38835, 0.3175), (6.10235, 0.3175))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((3.49885, 0.3175), (3.49885, 27.6225))
                Line((3.49885, 27.6225), (5.78485, 27.6225))
                Line((5.78485, 27.6225), (5.78485, 0.3175))
                Line((5.78485, 0.3175), (3.49885, 0.3175))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((0.89535, 0.3175), (0.89535, 27.6225))
                Line((0.89535, 27.6225), (3.18135, 27.6225))
                Line((3.18135, 27.6225), (3.18135, 0.3175))
                Line((3.18135, 0.3175), (0.89535, 0.3175))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.3175
        extrude(amount=0.3175)
    return part.part


# Description: This is a rectangular base plate with an integral mounting bracket featuring a curved, ribbed clamp or strap mechanism on top for securing or holding cylindrical or curved components.
def model_41722_92ab0003_0011():
    """Model: toast"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 12 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 60.5508386413, perimeter: 34.3956461832
            with BuildLine():
                Line((6.3500002432, 8.1280002594), (1.27, 8.1280002594))
                CenterArc((1.27, 6.8580002594), 1.27, 90, 180)
                Line((0, 5.5880001783), (1.27, 5.5880002594))
                Line((0, 5.5880001783), (0, 0))
                Line((0, 0), (7.6200002432, 0))
                Line((7.6200002432, 0), (7.6200002432, 5.5880001783))
                Line((6.3500002432, 5.5880002594), (7.6200002432, 5.5880001783))
                CenterArc((6.3500002432, 6.8580002594), 1.27, -90, 180)
            make_face()
        # OneSide extrude, distance=1.27
        extrude(amount=1.27)
    return part.part


# Description: This is a hollow rectangular tube or channel with a long, slender hexagonal or square cross-section, featuring vertical slots or grooves running along its length for mounting or alignment purposes.
def model_41729_b5092135_0008():
    """Model: Connector Bar v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 8 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.24, perimeter: 22.4
            with BuildLine():
                Line((-1.5, 1.5), (1.5, 1.5))
                Line((-1.5, -1.5), (-1.5, 1.5))
                Line((1.5, -1.5), (-1.5, -1.5))
                Line((1.5, 1.5), (1.5, -1.5))
            make_face()
            with BuildLine():
                Line((1.3, 1.3), (1.3, -1.3))
                Line((1.3, -1.3), (-1.3, -1.3))
                Line((-1.3, -1.3), (-1.3, 1.3))
                Line((-1.3, 1.3), (1.3, 1.3))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=20
        extrude(amount=20)
    return part.part


# Description: This is a long, slender hexagonal prism or shaft with a uniform cross-section, featuring a tapered or beveled top end and a flat bottom end, commonly used as a structural support or alignment pin in mechanical assemblies.
def model_41733_1ec9b00c_0000():
    """Model: leg2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 447.0204613582, perimeter: 153.7678412425
            with BuildLine():
                Line((-75, 19.1055041855), (-10, -7.8599799196))
                Line((-10, -7.8599799196), (-10, 0))
                Line((-10, 0), (-75, 25))
                Line((-75, 25), (-75, 19.1055041855))
            make_face()
        # OneSide extrude, distance=-5
        extrude(amount=-5)
    return part.part


# Description: This is a tall, slender rectangular prism or column with a tapered pyramidal top, featuring vertical grooves or channels running along its length and a narrow, elongated profile suitable for structural or architectural applications.
def model_41733_1ec9b00c_0008():
    """Model: arm rest 2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 315.251015538, perimeter: 144.9621706784
            with BuildLine():
                Line((0, 0), (-30, -60))
                Line((-24.9545450664, -60.7935638589), (-30, -60))
                Line((5, 0), (-24.9545450664, -60.7935638589))
                Line((0, 0), (5, 0))
            make_face()
        # OneSide extrude, distance=-10
        extrude(amount=-10)
    return part.part


# Description: This is a flat sheet metal or plastic parallelogram plate with a simple rectangular shape and minimal features, appearing to be a basic structural or mounting panel with clean edges and no holes or cutouts.
def model_41733_1ec9b00c_0009():
    """Model: desk"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 201.8181973424, perimeter: 90.0909098671
            with BuildLine():
                Line((0, -24.9545450664), (0, -30))
                Line((40, -30), (0, -30))
                Line((40, -24.9545450664), (40, -30))
                Line((0, -24.9545450664), (40, -24.9545450664))
            make_face()
        # OneSide extrude, distance=-40
        extrude(amount=-40)
    return part.part


# Description: This is a flat parallelogram-shaped plate or panel with a trapezoidal profile, featuring a thin recessed edge or flange along one side and internal diagonal reinforcement ribs for structural support.
def model_41733_1ec9b00c_0013():
    """Model: cover"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 8 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 125, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 33750, perimeter: 750
            with BuildLine():
                Line((50, -75), (50, 150))
                Line((50, 150), (-100, 150))
                Line((-100, 150), (-100, -75))
                Line((-100, -75), (50, -75))
            make_face()
        # OneSide extrude, distance=8
        extrude(amount=8)
    return part.part


# Description: This is an elongated hexagonal or rectangular prism-shaped structural member with a hollow channel or slot running along its length, featuring a tapered or angled top edge.
def model_41733_1ec9b00c_0019():
    """Model: foot steppe"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(50, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 172.6549700794, perimeter: 75.0385455792
            with BuildLine():
                Line((56.0550735541, -65.0374042902), (62.8135144812, -67.2440972938))
                Line((65.5766869545, -97.0178210384), (56.0550735541, -65.0374042902))
                Line((70.4974812649, -95.6885192849), (65.5766869545, -97.0178210384))
                Line((62.8135144812, -67.2440972938), (70.4974812649, -95.6885192849))
            make_face()
        # OneSide extrude, distance=-5
        extrude(amount=-5)
    return part.part


# Description: This is a cylindrical tube or pipe with a closed top end and an open bottom end, featuring a slightly tapered or rounded rim at the upper terminus.
def model_41737_3653024c_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1256214, perimeter: 1.2564255128
            Circle(0.199966331)
        # OneSide extrude, distance=1.8184
        extrude(amount=1.8184)
    return part.part


# Description: This is a cylindrical mesh or perforated filter component with open circular ends and a curved sidewall surface, designed for fluid or air filtration applications.
def model_41737_64cdca02_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 9.0792030395, perimeter: 10.6814151814
            Circle(1.7000000253)
        # OneSide extrude, distance=5
        extrude(amount=5)
    return part.part


# Description: This is a beveled rectangular box or housing with a elongated, tapered form featuring angled faceted surfaces on the top and sides, creating a streamlined, aerodynamic appearance with multiple triangulated faces and a central slot or channel running along its length.
def model_41737_7a3bf600_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 160.3876855319, perimeter: 62.1172830085
            with BuildLine():
                Line((0.0616109065, -3.9962279037), (24.5, -2.5))
                Line((24.5, 2.3968646924), (24.5, -2.5))
                Line((0.0616109065, 4.2327877488), (24.5, 2.3968646924))
                Line((0.0616109065, 4.2327877488), (0.0616109065, -3.9962279037))
            make_face()
        # OneSide extrude, distance=5
        extrude(amount=5)
    return part.part


# Description: This is a curved sheet metal channel or duct component with an elongated, tapered rectangular cross-section that bends at an angle, featuring an open top surface and closed sides that form a shallow trough or guide track.
def model_41737_a8d6ea5d_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.765532516, perimeter: 22.2939268782
            with BuildLine():
                Line((4.7325933005, -4.4131358955), (0, -0.6))
                Line((4.7325933005, -3.8959817138), (4.7325933005, -4.4131358955))
                Line((0.5177421261, -0.5), (4.7325933005, -3.8959817138))
                Line((4.8520824936, -0.5), (0.5177421261, -0.5))
                Line((4.8520824936, 0), (4.8520824936, -0.5))
                Line((0, 0), (4.8520824936, 0))
                Line((0, -0.6), (0, 0))
            make_face()
        # OneSide extrude, distance=0.4
        extrude(amount=0.4)
    return part.part


# Description: This is a curved protective guard or shield with a U-shaped cross-section, featuring a main curved body panel with a reinforcing flange or lip along the top edge and a small mounting tab or extension on the upper right side.
def model_41737_af56d74d_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.4672380556, perimeter: 7.5861540561
            with BuildLine():
                CenterArc((0, 0.6250000093), 1.6250000242, -157.380135052, 134.7602701039)
                Line((1.5000000224, 0), (1.3000000194, 0))
                CenterArc((0, 0.4888888962), 1.3888889096, -159.3903070625, 138.7806141249)
                Line((-1.5000000224, 0), (-1.3000000194, 0))
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2)
    return part.part


# Description: This is a cylindrical container or drum with a ribbed/corrugated exterior surface and an open top featuring internal cross-bracing or reinforcement ribs.
def model_41737_b6724677_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 8 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.8117897129, perimeter: 11.3516833897
            with BuildLine():
                CenterArc((0, 0), 2.4000000358, -44.5987253484, 3.448452186)
                CenterArc((3.4178, 0), 2.4, -135.4012738097, 44.6868869802)
                Line((3.3878766098, -2.3998134491), (3.4479877285, -2.3998101385))
                CenterArc((3.4178, 0), 2.4, -89.2793020637, 91.6673174735)
                CenterArc((3.4178, 0.1999999955), 2.4, -132.1517900479, 129.7637746381)
            make_face()
            # Profile area: 0.7584506988, perimeter: 7.1614807334
            with BuildLine():
                CenterArc((0, 0), 2.4000000358, -90, 45.4012746516)
                Line((0, -2.4000000358), (3.3878766098, -2.3998134491))
                CenterArc((3.4178, 0), 2.4, -135.4012738097, 44.6868869802)
            make_face()
            # Profile area: 0.8117974964, perimeter: 11.35168601
            with BuildLine():
                CenterArc((0, 0), 2.4000000358, 177.6119742825, 92.3880257175)
                CenterArc((0, 0), 2.4000000358, -90, 45.4012746516)
                CenterArc((3.4178, 0), 2.4, -138.8497269843, 3.4484531747)
                CenterArc((0, 0.200000003), 2.4, -177.6119947553, 129.7637855401)
            make_face()
            # Profile area: 0.8117971263, perimeter: 11.3516849929
            with BuildLine():
                CenterArc((3.4178, 0), 2.4, 2.3880154099, 129.7637753749)
                CenterArc((3.4178, 0.1999999955), 2.4, -2.3880154099, 92.2011444793)
                Line((3.4099746674, 2.599987238), (3.4256276174, 2.599987238))
                CenterArc((3.4178, 0.1999999955), 2.4, 90.1868163866, 45.214458152)
                CenterArc((0, 0.200000003), 2.4, 41.1502730157, 3.4484521959)
            make_face()
            # Profile area: 0.0196875988, perimeter: 0.561125054
            with BuildLine():
                CenterArc((3.4178, 0.1999999955), 2.4, -135.4012747884, 3.2494847405)
                CenterArc((0, 0.200000003), 2.4, -47.8482092152, 3.2494837539)
                CenterArc((3.4178, 0), 2.4, -138.8497269843, 3.4484531747)
                CenterArc((0, 0), 2.4000000358, -44.5987253484, 3.448452186)
            make_face()
            # Profile area: 0.1282372166, perimeter: 3.7279588396
            with BuildLine():
                CenterArc((0, 0), 2.4000000358, 2.3880257175, 42.210699631)
                CenterArc((0, 0.200000003), 2.4, -2.3880052447, 43.5382782603)
                CenterArc((3.4178, 0), 2.4, 132.1517907848, 3.2494830249)
            make_face()
            # Profile area: 0.1278201315, perimeter: 3.5360754558
            with BuildLine():
                CenterArc((0, 0.200000003), 2.4, -44.5987254614, 39.8185335428)
                CenterArc((3.4178, 0.1999999955), 2.4, -135.4012747884, 3.2494847405)
                CenterArc((0, 0), 2.4000000358, -41.1502731625, 41.1502731625)
                Line((2.3916521484, 0), (2.4000000358, 0))
            make_face()
            # Profile area: 0.1278200641, perimeter: 3.5360753433
            with BuildLine():
                Line((1.0178, 0), (1.026147851, 0))
                CenterArc((3.4178, 0), 2.4, -180, 41.1502730157)
                CenterArc((0, 0.200000003), 2.4, -47.8482092152, 3.2494837539)
                CenterArc((3.4178, 0.1999999955), 2.4, -175.2198082599, 39.8185334715)
            make_face()
            # Profile area: 13.9478682497, perimeter: 14.5185197548
            with BuildLine():
                CenterArc((0, 0), 2.4000000358, 0, 2.3880257175)
                CenterArc((0, 0), 2.4000000358, -41.1502731625, 41.1502731625)
                CenterArc((3.4178, 0.1999999955), 2.4, -132.1517900479, 129.7637746381)
                CenterArc((3.4178, 0), 2.4, 2.3880154099, 129.7637753749)
                CenterArc((0, 0.200000003), 2.4, -2.3880052447, 43.5382782603)
            make_face()
            # Profile area: 1.6030010569, perimeter: 5.1021470226
            with BuildLine():
                CenterArc((3.4178, 0), 2.4, 135.4012738097, 42.2107107805)
                CenterArc((3.4178, 0.1999999955), 2.4, -177.6119845901, 2.3921763302)
                Line((1.026147851, 0), (2.3916521484, 0))
                CenterArc((0, 0.200000003), 2.4, -4.7801919186, 2.3921866739)
                CenterArc((0, 0), 2.4000000358, 2.3880257175, 42.210699631)
            make_face()
            # Profile area: 0.7587250904, perimeter: 7.1900223642
            with BuildLine():
                CenterArc((3.4178, 0.1999999955), 2.4, 90.1868163866, 45.214458152)
                Line((0.0078276174, 2.599987238), (3.4099746674, 2.599987238))
                CenterArc((0, 0.200000003), 2.4, 44.5987252116, 45.2144038579)
            make_face()
            # Profile area: 0.0196875887, perimeter: 0.5611249111
            with BuildLine():
                CenterArc((3.4178, 0), 2.4, 132.1517907848, 3.2494830249)
                CenterArc((0, 0.200000003), 2.4, 41.1502730157, 3.4484521959)
                CenterArc((3.4178, 0.1999999955), 2.4, 135.4012745386, 3.4484514599)
                CenterArc((0, 0), 2.4000000358, 44.5987253484, 3.2494837647)
            make_face()
            # Profile area: 0.8117970963, perimeter: 11.351684228
            with BuildLine():
                CenterArc((3.4178, 0.1999999955), 2.4, 135.4012745386, 3.4484514599)
                CenterArc((0, 0.200000003), 2.4, 44.5987252116, 45.2144038579)
                CenterArc((0, 0.200000003), 2.4, 89.8131290695, 92.5748761752)
                CenterArc((0, 0), 2.4000000358, 47.8482091131, 129.7637651694)
            make_face()
            # Profile area: 1.3285076873, perimeter: 4.7013339598
            with BuildLine():
                CenterArc((3.4178, 0.1999999955), 2.4, -175.2198082599, 39.8185334715)
                CenterArc((0, 0.200000003), 2.4, -44.5987254614, 39.8185335428)
                Line((1.026147851, 0), (2.3916521484, 0))
            make_face()
            # Profile area: 13.9478684838, perimeter: 14.5185198669
            with BuildLine():
                CenterArc((3.4178, 0.1999999955), 2.4, 138.8497259985, 43.5382894113)
                CenterArc((0, 0), 2.4000000358, 47.8482091131, 129.7637651694)
                CenterArc((0, 0.200000003), 2.4, -177.6119947553, 129.7637855401)
                CenterArc((3.4178, 0), 2.4, -180, 41.1502730157)
                CenterArc((3.4178, 0), 2.4, 177.6119845901, 2.3880154099)
            make_face()
            # Profile area: 0.1282372803, perimeter: 3.7279597804
            with BuildLine():
                CenterArc((0, 0), 2.4000000358, 44.5987253484, 3.2494837647)
                CenterArc((3.4178, 0.1999999955), 2.4, 138.8497259985, 43.5382894113)
                CenterArc((3.4178, 0), 2.4, 135.4012738097, 42.2107107805)
            make_face()
        # OneSide extrude, distance=3.5
        extrude(amount=3.5)
    return part.part


# Description: This is a long, narrow structural channel or beam with a curved bend approximately midway along its length, featuring a rectangular hollow cross-section with flanged edges typical of sheet metal construction.
def model_41737_d80c34b9_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 7.4196428571, perimeter: 33.4162925834
            with BuildLine():
                Line((7.5, -5.5), (0, -0.6785714286))
                Line((7.5, -5), (7.5, -5.5))
                Line((0.5, -0.5), (7.5, -5))
                Line((7.5, -0.5), (0.5, -0.5))
                Line((7.5, 0), (7.5, -0.5))
                Line((0, 0), (7.5, 0))
                Line((0, -0.6785714286), (0, 0))
            make_face()
        # OneSide extrude, distance=0.4
        extrude(amount=0.4)
    return part.part


# Description: This is a boat hull or fin-shaped component with a tapered, wedge-like profile featuring a curved top surface, a flat bottom base, and a pointed bow section, designed for hydrodynamic or aerodynamic flow.
def model_41737_dd3de5eb_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 14.8392977546, perimeter: 15.6823099422
            with BuildLine():
                CenterArc((2.0121797169, 0.4479700588), 2.9841339561, -33.5210974588, 48.1175505015)
                Line((4.900000073, 1.2000000179), (0, 0))
                Line((0, 0), (0, -3))
                Line((0, -3), (2.2500000335, -3.0000000224))
                Line((4.5000000671, -1.2000000179), (2.2500000335, -3.0000000224))
            make_face()
        # OneSide extrude, distance=0.4
        extrude(amount=0.4)
    return part.part


# Description: A slender, tapered cylindrical shaft with a pointed tip at one end and a slightly rounded or blunt end at the other, resembling a stylus, pen, or writing instrument.
def model_41738_065c1320_0002():
    """Model: Fish tank1 v3_tank divider v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 8 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 11.2555580172, perimeter: 36.7205764322
            with BuildLine():
                Line((-12.6999998093, -11.9499702446), (-12.6999998093, -12.5849702446))
                Line((-12.6999998093, -12.5849702446), (-12.0649998093, -12.5849702446))
                Line((-12.0649998093, -12.5849702446), (0, -0.635))
                Line((0, -0.635), (0, 0))
                Line((0, 0), (-0.635, 0))
                Line((-0.635, 0), (-0.635, -0.3701909047))
                Line((-0.635, -0.3701909047), (-12.3262454732, -11.9499702446))
                Line((-12.3262454732, -11.9499702446), (-12.6999998093, -11.9499702446))
            make_face()
        # OneSide extrude, distance=55.88
        extrude(amount=55.88)
    return part.part


# Description: A solid torus (donut-shaped ring) with a circular cross-section, featuring a smooth outer curved surface and a hollow center opening.
def model_41739_1bc15d9f_0001():
    """Model: Frame Pt 1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 5.08), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 25.1321842558, perimeter: 39.978023154
            with BuildLine():
                CenterArc((0, 0), 3.81, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 2.5527, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=2.54
        extrude(amount=2.54)
    return part.part


# Description: This is a rounded rectangular bar or rod with a uniform cylindrical profile and smooth, curved end caps.
def model_41739_1bc15d9f_0005():
    """Model: Frame Pipe"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 2.7747301555, perimeter: 5.9049375517
            Circle(0.9398)
        # OneSide extrude, distance=30.48
        extrude(amount=30.48)
    return part.part


# Description: This is a cylindrical rod or shaft with a uniform circular cross-section, featuring a slightly tapered or rounded end at the top and a straight, elongated body.
def model_41739_1bc15d9f_0010():
    """Model: Seat Pipe"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.162361377, perimeter: 6.3039198187
            with Locations((50.7999992371, 0)):
                Circle(1.0033)
        # OneSide extrude, distance=35.56
        extrude(amount=35.56)
    return part.part


# Description: This is a cylindrical capsule or rounded rectangular tube with hemispherical ends, featuring internal parallel slots or ribs running lengthwise along its surface.
def model_41739_1bc15d9f_0012():
    """Model: Seat Clamp Part 2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.291863508, perimeter: 1.9151148816
            with Locations((38.0999994278, 0)):
                Circle(0.3048)
        # OneSide extrude, distance=1.905
        extrude(amount=1.905)
    return part.part


# Description: This is a satellite dish or parabolic reflector with an elliptical/oval dish shape, featuring a ribbed internal structure with radial support ribs and a reinforced rim flange for structural integrity.
def model_41757_c1173a7e_0008():
    """Model: Bottom Floor v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 856.3356396748, perimeter: 103.7353894215
            Circle(16.51)
        # OneSide extrude, distance=1.27
        extrude(amount=1.27)
    return part.part


# Description: This is a cylindrical or oval-shaped bowl-like component with a ribbed/finned interior surface and a smooth outer wall, featuring an open top and closed bottom structure.
def model_41757_c1173a7e_0010():
    """Model: Bowl v2"""
    with BuildPart() as part:
        # Sketch2 -> Extrude2 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 126.6768697744, perimeter: 39.8982267006
            Circle(6.35)
        # OneSide extrude, distance=3.81
        extrude(amount=3.81)
    return part.part


# Description: This is a flat parallelogram or skewed rectangular plate with a simple geometric shape, no holes or features, characterized by its four-sided structure with slanted edges.
def model_41757_c1173a7e_0023():
    """Model: Flag v4 (1)"""
    with BuildPart() as part:
        # Sketch3 -> Extrude3 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 9 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0774192, perimeter: 1.3208
            with BuildLine():
                Line((14.732, -0.1524), (14.732, 0))
                Line((14.732, 0), (14.224, 0))
                Line((14.224, 0), (14.224, -0.1524))
                Line((14.224, -0.1524), (14.732, -0.1524))
            make_face()
            # Profile area: 119.3675032, perimeter: 45.6692
            with BuildLine():
                Line((14.732, 0), (14.224, 0))
                Line((14.732, 0), (14.732, 8.1026))
                Line((14.732, 8.1026), (0, 8.1026))
                Line((0, 8.1026), (0, 0))
                Line((0, 0), (14.224, 0))
            make_face()
        # OneSide extrude, distance=0.127
        extrude(amount=0.127)
    return part.part


# Description: This is a hexagonal prism or shaft with an elongated, tapered design featuring a beveled or chamfered edge along the top surface, creating an asymmetrical cross-section.
def model_41764_6707e462_0000():
    """Model: Component7"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4, perimeter: 10
            with BuildLine():
                Line((3.5, -0.5), (2.5, -0.5))
                Line((3.5, 3.5), (3.5, -0.5))
                Line((2.5, 3.5), (3.5, 3.5))
                Line((2.5, -0.5), (2.5, 3.5))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


# Description: This is a rectangular prism or box-shaped component with a trapezoidal cross-section, featuring a sloped top surface and a flat bottom, with clean edges and no holes or slots visible.
def model_41764_6707e462_0001():
    """Model: Component12"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.25, perimeter: 4.5
            with BuildLine():
                Line((4, 0.75), (3, 0.75))
                Line((4, 2), (4, 0.75))
                Line((3, 2), (4, 2))
                Line((3, 0.75), (3, 2))
            make_face()
        # OneSide extrude, distance=0.25
        extrude(amount=0.25)
    return part.part


# Description: This is a rectangular prismatic block or base plate with a sloped or angled top surface, featuring a trapezoidal profile when viewed from the side.
def model_41764_6707e462_0002():
    """Model: Component9"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.9079937529, perimeter: 3.8479274193
            with BuildLine():
                Line((2.8300146766, 1.906050967), (2, 1.906050967))
                Line((2.8300146766, 3), (2.8300146766, 1.906050967))
                Line((2, 3), (2.8300146766, 3))
                Line((2, 1.906050967), (2, 3))
            make_face()
        # OneSide extrude, distance=0.25
        extrude(amount=0.25)
    return part.part


# Description: This is a flat, oval-shaped ring or collar with a mesh or perforated pattern on the upper surface and a solid base, resembling a strainer, filter basket, or decorative band component.
def model_41764_6707e462_0003():
    """Model: Component8"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.1014513684, perimeter: 8.8805707613
            with Locations((0, -2.6527662591)):
                Ellipse(2, 0.6527662591)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


# Description: Featuring a recessed central slot or channel running along its length and angled side flanges.
def model_41764_6707e462_0005():
    """Model: Component11"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2, perimeter: 6
            with BuildLine():
                Line((2, 0), (1, 0))
                Line((2, 2), (2, 0))
                Line((1, 2), (2, 2))
                Line((1, 0), (1, 2))
            make_face()
        # OneSide extrude, distance=0.25
        extrude(amount=0.25)
    return part.part


# Description: This is a bicycle or motorcycle tire featuring an elongated, elliptical cross-section with a textured tread pattern on the upper surface and a smooth sidewall, designed for rolling contact on a curved rim.
def model_41764_6707e462_0006():
    """Model: Component15"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.4374310591, perimeter: 8.9950472111
            with Locations((3, 0)):
                Ellipse(2, 0.7062390877, rotation=-90)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


# Description: This is a mounting bracket or connector plate with an elongated, rounded rectangular shape featuring three evenly-spaced holes for fastening or assembly purposes.
def model_41776_50aabc9d_0002():
    """Model: Top Base Plate Unfinished v4 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 17 constraints, 11 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 15.5331856019, perimeter: 23.4814150876
            with BuildLine():
                CenterArc((-3.2, 0), 1, 90, 180)
                Line((3.1999990631, -1), (-3.2, -1))
                CenterArc((3.2, 0), 1, -90.0000536822, 180.0000536724)
                Line((-3.2, 1), (3.2000000002, 1))
            make_face()
            with BuildLine():
                CenterArc((-3.38015193, -0.19824781), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0.1, 0.6), 0.1000000104, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0.9797958971, 0.2), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((3.3802792094, -0.1976174882), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)
    return part.part


# Description: This is a disk or wheel with a flat circular face and a ribbed cylindrical rim, featuring radial cooling fins or structural ribs on its outer edge for heat dissipation and reinforcement.
def model_41778_3d8cc892_0000():
    """Model: bottom_bun"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 71.2557392481, perimeter: 29.9236700254
            Circle(4.7625)
        # OneSide extrude, distance=1.651
        extrude(amount=1.651)
    return part.part


# Description: This is an elongated hexagonal or octagonal prism with a tapered pointed end, featuring a longitudinal slot or groove running along its length, commonly used as a tool holder, shaft, or structural component.
def model_41778_3d8cc892_0002():
    """Model: french_fry"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 3 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.6129, perimeter: 5.08
            with BuildLine():
                Line((-1.27, 1.27), (0, 1.27))
                Line((-1.27, 0), (-1.27, 1.27))
                Line((0, 0), (-1.27, 0))
                Line((0, 1.27), (0, 0))
            make_face()
        # OneSide extrude, distance=10.16
        extrude(amount=10.16)
    return part.part


# Description: This is a circular disc or wheel with an oblate spheroidal (flattened) shape, featuring a ribbed or textured rim edge around its perimeter and a smooth, flat or slightly curved central face.
def model_41778_3d8cc892_0004():
    """Model: patty"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 69.3682538884, perimeter: 29.5246877584
            Circle(4.699)
        # OneSide extrude, distance=0.889
        extrude(amount=0.889)
    return part.part


# Description: This is a toroidal (donut-shaped) ring or torus with a circular cross-section, featuring a uniform wall thickness and a centered axial hole, commonly used as a structural component, bearing surface, or connector in mechanical assemblies.
def model_41778_3d8cc892_0007():
    """Model: onion"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 7.6006121865, perimeter: 23.9389360204
            with BuildLine():
                CenterArc((0, 0), 2.2225, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.5875, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.508
        extrude(amount=0.508)
    return part.part


# Description: This is a paraglider wing featuring an elliptical planform shape with a ribbed internal structure, a curved aerodynamic profile, and openings at the leading edge for air intake.
def model_41785_37ab51ed_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 17.3420634721, perimeter: 14.7623438792
            Circle(2.3495)
        # OneSide extrude, distance=1.016
        extrude(amount=1.016)
    return part.part


# Description: This is a rectangular channel or tray-like component with an elongated box shape, featuring open top geometry, angled side walls, and two darker end flanges or caps at each end.
def model_41868_002280d0_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 21 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.5155854849, perimeter: 9.4266389755
            with BuildLine():
                CenterArc((4.5250000685, -0.2250000045), 0.075, -90, 90)
                Line((4.6000000685, 0.0250000015), (4.6000000685, -0.2250000045))
                CenterArc((4.5250000685, 0.0250000015), 0.075, 0, 90)
                Line((2.4750000358, 0.1000000015), (4.5250000685, 0.1000000015))
                CenterArc((2.4750000358, 0.0250000015), 0.075, 90, 90)
                Line((2.4000000358, -0.2250000045), (2.4000000358, 0.0250000015))
                CenterArc((2.4750000358, -0.2250000045), 0.075, -180, 90)
                Line((4.5250000685, -0.3000000045), (2.4750000358, -0.3000000045))
            make_face()
            with BuildLine():
                Line((2.5, -0.18), (2.5, 0))
                Line((2.5, 0), (4.4977, 0))
                Line((4.4977, 0), (4.4977, -0.18))
                Line((4.4977, -0.18), (2.5, -0.18))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)
    return part.part


# Description: This is a rounded rectangular bar or rod with a simple, uniform cylindrical profile and smooth, rounded ends.
def model_41868_4e7423ae_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.013273229, perimeter: 0.408407045
            with Locations((-2, 0)):
                Circle(0.065)
        # OneSide extrude, distance=2.5
        extrude(amount=2.5)
    return part.part


# Description: This is a tapered stylus or pen tool with an elongated, pointed cylindrical shape that gradually narrows from a thicker base to a sharp tip.
def model_41868_629410cd_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch2 -> Extrude2 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1215130914, perimeter: 2.678008731
            with BuildLine():
                Line((-0.0259620067, -0.0000317438), (-0.0259620067, 1.0999682562))
                CenterArc((0.0240379832, 0), 0.05, -179.9636242991, 182.0019791276)
                Line((0.0740063453, 0.001778425), (0.0740063453, 1.1000000164))
                Line((0.0740063453, 1.1000000164), (0.0239737205, 1.2524816191))
                Line((-0.0259620067, 1.0999682562), (0.0239737205, 1.2524816191))
            make_face()
        # OneSide extrude, distance=0.01
        extrude(amount=0.01)
    return part.part


# Description: This is an elongated rectangular bar or beam with rounded ends and a slightly curved or beveled top surface, featuring a dark gray border or edge detail along its perimeter.
def model_41868_6791916d_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch2 -> Extrude2 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0039269908, perimeter: 0.2570796327
            with BuildLine():
                Line((-1.9516810894, 0.0965507227), (-1.9516810894, -0.0034492773))
                CenterArc((-1.9516810894, 0.0465507227), 0.05, 90, 180)
            make_face()
            # Profile area: 0.1138502176, perimeter: 2.4556047626
            with BuildLine():
                CenterArc((-0.8524185111, 0.0465452845), 0.05, -89.1549463386, 179.251685918)
                Line((-1.9516810894, 0.0965507227), (-0.8525029323, 0.0965452132))
                Line((-1.9516810894, 0.0965507227), (-1.9516810894, -0.0034492773))
                Line((-0.8516810894, -0.0034492773), (-1.9516810894, -0.0034492773))
            make_face()
        # OneSide extrude, distance=0.02
        extrude(amount=0.02)
    return part.part


# Description: This is a rounded rectangular bar or shaft with a uniform cylindrical profile and slightly beveled or rounded edges at both ends.
def model_41868_8e597530_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0176714587, perimeter: 0.471238898
            with Locations((-1.5, 0)):
                Circle(0.075)
        # OneSide extrude, distance=3.5
        extrude(amount=3.5)
    return part.part


# Description: This is a tapered needle or cone-shaped pin with a simple, elongated cylindrical form that gradually tapers to a sharp point at one end.
def model_41868_a4a9d650_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1045475654, perimeter: 3.8797848813
            with BuildLine():
                Line((-0.0225846981, 0.0417023311), (-0.0225846981, 1.7500000261))
                CenterArc((0.0050000002, 0), 0.05, 123.4833039442, 293.0333921116)
                Line((0.0325846986, 0.0417023311), (0.0325846986, 1.7500000261))
                Line((0.0325846986, 1.7500000261), (0.0050000002, 1.85))
                Line((-0.0225846981, 1.7500000261), (0.0050000002, 1.85))
            make_face()
        # OneSide extrude, distance=0.01
        extrude(amount=0.01)
    return part.part


# Description: This is a tapered stylus or pen tool with an elongated, needle-like shape that gradually narrows from a thicker shaft to a sharp pointed tip.
def model_41868_c16c1f64_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1244228491, perimeter: 3.280197673
            with BuildLine():
                Line((-0.1000000015, 1.7500000261), (-0.1397633363, 1.6696871329))
                Line((-0.1397633363, 0.2303129903), (-0.1397633363, 1.6696871329))
                CenterArc((-0.1000000015, 0.200000003), 0.05, 142.680453087, 254.639093826)
                Line((-0.0602366667, 0.2303129903), (-0.0602366667, 1.6696871329))
                Line((-0.1000000015, 1.7500000261), (-0.0602366667, 1.6696871329))
            make_face()
        # OneSide extrude, distance=0.01
        extrude(amount=0.01)
    return part.part


# Description: This is a cylindrical rod or shaft with a uniform circular cross-section, tapered slightly at both ends, featuring a smooth surface with no holes, slots, or flanges.
def model_41896_7d8659e6_0001():
    """Model: Neck Part 2 v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.6597344573, perimeter: 13.1946891451
            with BuildLine():
                CenterArc((1, 1), 1.1, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((1, 1), 1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=25
        extrude(amount=25)
    return part.part


# Description: This is a cylindrical rod or shaft with a uniform circular cross-section, featuring a slightly tapered or rounded end on one side and a flat end on the other, designed as a simple mechanical component for fastening, alignment, or structural support.
def model_41896_7d8659e6_0013():
    """Model: Inner Neck v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.8717919614, perimeter: 11.6238928183
            with BuildLine():
                CenterArc((0, 0), 1, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.85, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=25
        extrude(amount=25)
    return part.part


# Description: This is a steering wheel cover with an oval/elliptical ring shape, featuring a textured grip surface with a woven or perforated pattern around the entire circumference for enhanced handling and comfort.
def model_41896_7d8659e6_0018():
    """Model: Wheel Edge v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 6 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 25.022690456, perimeter: 69.7431125478
            with BuildLine():
                CenterArc((0, 0), 5.75, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                EllipticalCenterArc((-3.0179218878, 4.4376215625), 0.4660057374, 0.2092898029, 0, 360, 35.8641191913)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.25
        extrude(amount=1.25)
    return part.part


# Description: This is a triangular wedge or pyramidal connector with a pointed, tapered geometry featuring flat faceted surfaces in light blue and dark blue/navy coloring, characterized by sharp edges and angular faces typical of a geometric solid or structural bracket component.
def model_41902_1001798c_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 52.2176375, perimeter: 35.3696368528
            with BuildLine():
                Line((0.9500802144, 1.9979628038), (0.9500802144, -9.7495371962))
                Line((9.8400802144, 1.9979628038), (0.9500802144, -9.7495371962))
                Line((0.9500802144, 1.9979628038), (9.8400802144, 1.9979628038))
            make_face()
        # OneSide extrude, distance=2.54
        extrude(amount=2.54)
    return part.part


# Description: This is a tapered cylindrical shaft or spindle with a streamlined, elongated body that gradually narrows from a wider hexagonal or multi-faceted head section to a pointed tip, featuring longitudinal ridges or grooves along its length for grip or structural reinforcement.
def model_41902_363c1593_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 246.0650571632, perimeter: 87.4623302977
            with BuildLine():
                Line((-2.2354828574, -4.4011068756), (-2.2354828574, 33.6988931244))
                CenterArc((-2.2354828574, -1.4556423323), 2.9454645433, -90, 76.7953753964)
                Line((6.6545171426, 23.5388931244), (0.6321049832, -2.1284731819))
                Line((6.6545171426, 33.6988931244), (6.6545171426, 23.5388931244))
                Line((-2.2354828574, 33.6988931244), (6.6545171426, 33.6988931244))
            make_face()
        # OneSide extrude, distance=1.905
        extrude(amount=1.905)
    return part.part


MODELS = {
    "model_40999_cad6be09_0011": {"func": model_40999_cad6be09_0011, "volume": 5769.6714708605, "area": 5131.6629861696},
    "model_40999_cad6be09_0012": {"func": model_40999_cad6be09_0012, "volume": 3539.351741496, "area": 1368.1101935632},
    "model_40999_cad6be09_0013": {"func": model_40999_cad6be09_0013, "volume": 386.1110990723, "area": 618.1831244989},
    "model_40999_cad6be09_0015": {"func": model_40999_cad6be09_0015, "volume": 22153.1243092728, "area": 7957.8409592262},
    "model_40999_cad6be09_0016": {"func": model_40999_cad6be09_0016, "volume": 257.4073993815, "area": 425.6342824419},
    "model_40999_cad6be09_0020": {"func": model_40999_cad6be09_0020, "volume": 1926.2406365123, "area": 857.7945671957},
    "model_40999_cad6be09_0022": {"func": model_40999_cad6be09_0022, "volume": 147.4833258457, "area": 245.1605811423},
    "model_41010_212b5129_0000": {"func": model_41010_212b5129_0000, "volume": 0.2438622036, "area": 10.4660858695},
    "model_41010_212b5129_0003": {"func": model_41010_212b5129_0003, "volume": 0.8459012683, "area": 35.0918246744},
    "model_41010_212b5129_0004": {"func": model_41010_212b5129_0004, "volume": 0.7604333557, "area": 31.693723544},
    "model_41010_212b5129_0006": {"func": model_41010_212b5129_0006, "volume": 0.0019500995, "area": 0.1667127106},
    "model_41010_212b5129_0007": {"func": model_41010_212b5129_0007, "volume": 0.0164731753, "area": 0.9439048864},
    "model_41010_212b5129_0009": {"func": model_41010_212b5129_0009, "volume": 0.1150015679, "area": 9.5968285704},
    "model_41010_212b5129_0010": {"func": model_41010_212b5129_0010, "volume": 1.6224734065, "area": 20.961866686},
    "model_41010_212b5129_0011": {"func": model_41010_212b5129_0011, "volume": 0.0848230016, "area": 1.2723450247},
    "model_41010_212b5129_0012": {"func": model_41010_212b5129_0012, "volume": 0.9410453409, "area": 38.8787604991},
    "model_41010_212b5129_0014": {"func": model_41010_212b5129_0014, "volume": 0.1420601392, "area": 11.7001835521},
    "model_41010_212b5129_0015": {"func": model_41010_212b5129_0015, "volume": 0.8947265921, "area": 37.0433712555},
    "model_41010_212b5129_0016": {"func": model_41010_212b5129_0016, "volume": 0.8590108733, "area": 35.6381484263},
    "model_41026_295d1dc8_0002": {"func": model_41026_295d1dc8_0002, "volume": 5309.408736, "area": 2903.22},
    "model_41032_ed481084_0003": {"func": model_41032_ed481084_0003, "volume": 1826.6927336114, "area": 1175.8067259462},
    "model_41032_ed481084_0004": {"func": model_41032_ed481084_0004, "volume": 10553.2690575058, "area": 8967.7238697754},
    "model_41032_ed481084_0006": {"func": model_41032_ed481084_0006, "volume": 1111.1764617127, "area": 1706.7434272619},
    "model_41032_ed481084_0008": {"func": model_41032_ed481084_0008, "volume": 279.2972491733, "area": 460.0315526047},
    "model_41124_a5855c0d_0004": {"func": model_41124_a5855c0d_0004, "volume": 0.6675884389, "area": 12.3307511653},
    "model_41124_a5855c0d_0006": {"func": model_41124_a5855c0d_0006, "volume": 294.1001962658, "area": 466.5893409112},
    "model_41124_a5855c0d_0007": {"func": model_41124_a5855c0d_0007, "volume": 4.5238934212, "area": 23.624776755},
    "model_41124_a5855c0d_0010": {"func": model_41124_a5855c0d_0010, "volume": 17.8757520395, "area": 68.8210603623},
    "model_41125_711db4bf_0007": {"func": model_41125_711db4bf_0007, "volume": 0.9079008759, "area": 31.4384496851},
    "model_41128_ee74f244_0008": {"func": model_41128_ee74f244_0008, "volume": 1.308409855, "area": 14.3746729989},
    "model_41142_1bf94ee2_0000": {"func": model_41142_1bf94ee2_0000, "volume": 0.56, "area": 4.12},
    "model_41142_1bf94ee2_0002": {"func": model_41142_1bf94ee2_0002, "volume": 0.5089380099, "area": 10.7442468753},
    "model_41142_1bf94ee2_0004": {"func": model_41142_1bf94ee2_0004, "volume": 0.0651408039, "area": 1.6859497274},
    "model_41142_1bf94ee2_0006": {"func": model_41142_1bf94ee2_0006, "volume": 7.7471674838, "area": 61.7134460871},
    "model_41142_1bf94ee2_0009": {"func": model_41142_1bf94ee2_0009, "volume": 8.1642139085, "area": 33.2223423117},
    "model_41142_1bf94ee2_0012": {"func": model_41142_1bf94ee2_0012, "volume": 0.0537801792, "area": 0.8816537381},
    "model_41142_1bf94ee2_0014": {"func": model_41142_1bf94ee2_0014, "volume": 3.8310151614, "area": 18.4945559517},
    "model_41227_90e1c07c_0001": {"func": model_41227_90e1c07c_0001, "volume": 315.3240642424, "area": 314.7920213893},
    "model_41227_90e1c07c_0004": {"func": model_41227_90e1c07c_0004, "volume": 38.6111099072, "area": 91.2073462375},
    "model_41227_90e1c07c_0005": {"func": model_41227_90e1c07c_0005, "volume": 482.6388738404, "area": 367.3629223457},
    "model_41227_90e1c07c_0007": {"func": model_41227_90e1c07c_0007, "volume": 613.6986759165, "area": 754.8045944727},
    "model_41227_90e1c07c_0008": {"func": model_41227_90e1c07c_0008, "volume": 307.9428095994, "area": 385.8375479496},
    "model_41227_90e1c07c_0009": {"func": model_41227_90e1c07c_0009, "volume": 360.3703591341, "area": 324.2927866224},
    "model_41227_90e1c07c_0010": {"func": model_41227_90e1c07c_0010, "volume": 206.440734304, "area": 203.0883576223},
    "model_41227_90e1c07c_0011": {"func": model_41227_90e1c07c_0011, "volume": 257.4073993815, "area": 243.2195899668},
    "model_41227_90e1c07c_0012": {"func": model_41227_90e1c07c_0012, "volume": 8.1445309961, "area": 57.0045913985},
    "model_41227_90e1c07c_0014": {"func": model_41227_90e1c07c_0014, "volume": 694.9999783301, "area": 752.4606064598},
    "model_41227_90e1c07c_0015": {"func": model_41227_90e1c07c_0015, "volume": 428.8844866275, "area": 692.1634298621},
    "model_41234_74275eb0_0004": {"func": model_41234_74275eb0_0004, "volume": 467.1729374577, "area": 1537.4629510094},
    "model_41234_74275eb0_0016": {"func": model_41234_74275eb0_0016, "volume": 0.8043981231, "area": 5.067074791},
    "model_41319_7cc85fc8_0000": {"func": model_41319_7cc85fc8_0000, "volume": 64.1749846539, "area": 216.7436826128},
    "model_41321_43c99300_0001": {"func": model_41321_43c99300_0001, "volume": 0.0085871108, "area": 0.386719148},
    "model_41321_43c99300_0002": {"func": model_41321_43c99300_0002, "volume": 0.0483372485, "area": 2.5769115557},
    "model_41321_43c99300_0004": {"func": model_41321_43c99300_0004, "volume": 0.0238132733, "area": 1.347274382},
    "model_41321_43c99300_0005": {"func": model_41321_43c99300_0005, "volume": 0.5650607231, "area": 16.0174693169},
    "model_41321_43c99300_0008": {"func": model_41321_43c99300_0008, "volume": 0.0040505467, "area": 0.5188557909},
    "model_41321_43c99300_0011": {"func": model_41321_43c99300_0011, "volume": 0.0046333332, "area": 0.2310586105},
    "model_41401_1f3f8936_0000": {"func": model_41401_1f3f8936_0000, "volume": 2352.7225769017, "area": 1299.6346699753},
    "model_41401_3b4b3455_0000": {"func": model_41401_3b4b3455_0000, "volume": 18.94754275, "area": 62.9031},
    "model_41401_4ced1833_0000": {"func": model_41401_4ced1833_0000, "volume": 391.2667577875, "area": 712.6195425},
    "model_41401_63f271a2_0000": {"func": model_41401_63f271a2_0000, "volume": 15.7288170635, "area": 48.1899757382},
    "model_41401_7a33a5db_0000": {"func": model_41401_7a33a5db_0000, "volume": 6.5651090444, "area": 51.3608126782},
    "model_41401_92345581_0000": {"func": model_41401_92345581_0000, "volume": 132.3669064885, "area": 267.4963642483},
    "model_41401_a4897785_0000": {"func": model_41401_a4897785_0000, "volume": 1.2065971846, "area": 8.2339965353},
    "model_41401_a7e53916_0000": {"func": model_41401_a7e53916_0000, "volume": 386.5361322737, "area": 711.2581386546},
    "model_41401_b70e852a_0000": {"func": model_41401_b70e852a_0000, "volume": 9.3702725398, "area": 40.53581481},
    "model_41401_de8868e3_0000": {"func": model_41401_de8868e3_0000, "volume": 49.8442021612, "area": 112.2584517957},
    "model_41401_f7b87ad7_0000": {"func": model_41401_f7b87ad7_0000, "volume": 591.2885092024, "area": 528.5123043471},
    "model_41468_264ed8e7_0000": {"func": model_41468_264ed8e7_0000, "volume": 8083.7456711692, "area": 7215.5173723212},
    "model_41469_4e88cdb5_0000": {"func": model_41469_4e88cdb5_0000, "volume": 0.683947475, "area": 12.6545945736},
    "model_41469_b94cf3e4_0000": {"func": model_41469_b94cf3e4_0000, "volume": 1.7628225411, "area": 21.3833642303},
    "model_41473_c2137170_0002": {"func": model_41473_c2137170_0002, "volume": 527.1874250589, "area": 462.6039478874},
    "model_41473_c2137170_0009": {"func": model_41473_c2137170_0009, "volume": 22.1433585303, "area": 92.4284740234},
    "model_41473_c2137170_0010": {"func": model_41473_c2137170_0010, "volume": 0.7602361749, "area": 8.6908349948},
    "model_41473_c2137170_0012": {"func": model_41473_c2137170_0012, "volume": 0.326725636, "area": 7.3513268094},
    "model_41473_c2137170_0015": {"func": model_41473_c2137170_0015, "volume": 10.2101761242, "area": 208.6409038955},
    "model_41473_c2137170_0016": {"func": model_41473_c2137170_0016, "volume": 2.3331282598, "area": 15.3643709343},
    "model_41473_c2137170_0018": {"func": model_41473_c2137170_0018, "volume": 0.5210952298, "area": 6.1579807565},
    "model_41473_c2137170_0023": {"func": model_41473_c2137170_0023, "volume": 0.3980567614, "area": 5.5040374035},
    "model_41473_c2137170_0025": {"func": model_41473_c2137170_0025, "volume": 22.0107989809, "area": 83.7516444415},
    "model_41473_c2137170_0028": {"func": model_41473_c2137170_0028, "volume": 3.7777651659, "area": 19.1794231502},
    "model_41473_c2137170_0029": {"func": model_41473_c2137170_0029, "volume": 165.6404726605, "area": 310.3893541747},
    "model_41474_57d78888_0004": {"func": model_41474_57d78888_0004, "volume": 0.0139367126, "area": 0.5360832255},
    "model_41474_57d78888_0007": {"func": model_41474_57d78888_0007, "volume": 0.00871286, "area": 0.348158817},
    "model_41501_b627682a_0016": {"func": model_41501_b627682a_0016, "volume": 0.0201733956, "area": 0.7530662815},
    "model_41501_b627682a_0019": {"func": model_41501_b627682a_0019, "volume": 0.1005354044, "area": 2.8956196089},
    "model_41501_b627682a_0026": {"func": model_41501_b627682a_0026, "volume": 0.2356194467, "area": 4.9008845611},
    "model_41501_b627682a_0027": {"func": model_41501_b627682a_0027, "volume": 0.074668149, "area": 1.9769911509},
    "model_41501_b627682a_0029": {"func": model_41501_b627682a_0029, "volume": 0.0113848234, "area": 0.5435677808},
    "model_41508_534c7804_0000": {"func": model_41508_534c7804_0000, "volume": 150, "area": 230},
    "model_41508_aa38f8d5_0000": {"func": model_41508_aa38f8d5_0000, "volume": 1075, "area": 4393},
    "model_41512_c1a779f2_0000": {"func": model_41512_c1a779f2_0000, "volume": 0.1000000007, "area": 1.3000000067},
    "model_41512_c1a779f2_0002": {"func": model_41512_c1a779f2_0002, "volume": 0.6742699082, "area": 15.0124777961},
    "model_41512_c1a779f2_0004": {"func": model_41512_c1a779f2_0004, "volume": 1.0134149582, "area": 11.73007865},
    "model_41512_c1a779f2_0005": {"func": model_41512_c1a779f2_0005, "volume": 2.9528193678, "area": 33.5870375417},
    "model_41518_e3d1e89c_0000": {"func": model_41518_e3d1e89c_0000, "volume": 27.7927413736, "area": 165.8477382787},
    "model_41524_f2a1b892_0001": {"func": model_41524_f2a1b892_0001, "volume": 0.0017671459, "area": 0.1649336143},
    "model_41524_f2a1b892_0002": {"func": model_41524_f2a1b892_0002, "volume": 0.0049087385, "area": 0.4319689899},
    "model_41524_f2a1b892_0005": {"func": model_41524_f2a1b892_0005, "volume": 0.0029785399, "area": 0.6208495742},
    "model_41524_f2a1b892_0013": {"func": model_41524_f2a1b892_0013, "volume": 0.2191260876, "area": 2.0263272616},
    "model_41593_d3d842f7_0000": {"func": model_41593_d3d842f7_0000, "volume": 15.4513322354, "area": 130.2654824574},
    "model_41593_d3d842f7_0001": {"func": model_41593_d3d842f7_0001, "volume": 117.9170480545, "area": 509.9436784436},
    "model_41593_d3d842f7_0003": {"func": model_41593_d3d842f7_0003, "volume": 76, "area": 202},
    "model_41593_d3d842f7_0004": {"func": model_41593_d3d842f7_0004, "volume": 21.4634954085, "area": 86.780972451},
    "model_41593_d3d842f7_0007": {"func": model_41593_d3d842f7_0007, "volume": 38.5314606519, "area": 177.5295261088},
    "model_41594_d49b5e5c_0000": {"func": model_41594_d49b5e5c_0000, "volume": 0.8168650112, "area": 5.8911729811},
    "model_41595_e15895be_0008": {"func": model_41595_e15895be_0008, "volume": 516.1920410019, "area": 990.0453856678},
    "model_41599_f66b4e5b_0013": {"func": model_41599_f66b4e5b_0013, "volume": 15.0000002235, "area": 62.0000008345},
    "model_41599_f66b4e5b_0015": {"func": model_41599_f66b4e5b_0015, "volume": 0.0878510806, "area": 3.8969074692},
    "model_41624_a15f83c1_0007": {"func": model_41624_a15f83c1_0007, "volume": 0.5654866776, "area": 4.1469023027},
    "model_41624_a15f83c1_0023": {"func": model_41624_a15f83c1_0023, "volume": 0.6785840132, "area": 4.5238934212},
    "model_41630_23cbce49_0000": {"func": model_41630_23cbce49_0000, "volume": 6.63676092, "area": 47.612808},
    "model_41646_6c1f1ff1_0005": {"func": model_41646_6c1f1ff1_0005, "volume": 12.3570021872, "area": 85.7152808754},
    "model_41648_577daf16_0002": {"func": model_41648_577daf16_0002, "volume": 12.1498989194, "area": 65.1757095178},
    "model_41648_577daf16_0006": {"func": model_41648_577daf16_0006, "volume": 2, "area": 10},
    "model_41649_4ed08803_0000": {"func": model_41649_4ed08803_0000, "volume": 3.6945130707, "area": 17.5929193058},
    "model_41649_4ed08803_0001": {"func": model_41649_4ed08803_0001, "volume": 0.0561873309, "area": 1.9264241737},
    "model_41650_9417da80_0003": {"func": model_41650_9417da80_0003, "volume": 0.0264207942, "area": 0.7106282582},
    "model_41650_9417da80_0012": {"func": model_41650_9417da80_0012, "volume": 0.0005172342, "area": 0.0463787376},
    "model_41653_71b50655_0003": {"func": model_41653_71b50655_0003, "volume": 0.0848230016, "area": 1.2082300165},
    "model_41654_46b2965e_0000": {"func": model_41654_46b2965e_0000, "volume": 435, "area": 408.793820754},
    "model_41654_e75f89df_0000": {"func": model_41654_e75f89df_0000, "volume": 51.8362787842, "area": 120.9513171632},
    "model_41672_d0a1ce4a_0000": {"func": model_41672_d0a1ce4a_0000, "volume": 0.167968996, "area": 1.9149128144},
    "model_41680_49185107_0006": {"func": model_41680_49185107_0006, "volume": 10897.39756, "area": 5438.6988},
    "model_41680_49185107_0010": {"func": model_41680_49185107_0010, "volume": 3938.50792942, "area": 2855.5846114},
    "model_41680_49185107_0011": {"func": model_41680_49185107_0011, "volume": 3996.1728551964, "area": 2960.8054746821},
    "model_41681_321971ae_0000": {"func": model_41681_321971ae_0000, "volume": 3.9943469775, "area": 31.6128408802},
    "model_41681_3dc1aa23_0000": {"func": model_41681_3dc1aa23_0000, "volume": 1.9112955054, "area": 27.1824509535},
    "model_41681_607f4353_0000": {"func": model_41681_607f4353_0000, "volume": 1.0054976538, "area": 15.8346087218},
    "model_41681_bab3a334_0000": {"func": model_41681_bab3a334_0000, "volume": 4.2657575743, "area": 38.4031488693},
    "model_41685_df8ac866_0004": {"func": model_41685_df8ac866_0004, "volume": 112.7439063557, "area": 202.7112659729},
    "model_41685_df8ac866_0015": {"func": model_41685_df8ac866_0015, "volume": 211.334937807, "area": 287.7855950321},
    "model_41685_df8ac866_0016": {"func": model_41685_df8ac866_0016, "volume": 0.0761836218, "area": 3.0630528373},
    "model_41685_df8ac866_0017": {"func": model_41685_df8ac866_0017, "volume": 2.5132741229, "area": 13.5716802635},
    "model_41691_96d262e4_0000": {"func": model_41691_96d262e4_0000, "volume": 27.438287051, "area": 75.6923148356},
    "model_41702_1533021d_0007": {"func": model_41702_1533021d_0007, "volume": 3.0000000894, "area": 14.0000002533},
    "model_41708_3a74f048_0008": {"func": model_41708_3a74f048_0008, "volume": 6.3297573912, "area": 55.8491613539},
    "model_41714_1d49f4d1_0002": {"func": model_41714_1d49f4d1_0002, "volume": 0.0371609318, "area": 0.9888087963},
    "model_41714_1d49f4d1_0007": {"func": model_41714_1d49f4d1_0007, "volume": 0.1188964206, "area": 2.6237580226},
    "model_41714_1d49f4d1_0008": {"func": model_41714_1d49f4d1_0008, "volume": 0.1021451456, "area": 3.029736905},
    "model_41714_1d49f4d1_0009": {"func": model_41714_1d49f4d1_0009, "volume": 0.0448044661, "area": 1.3039415558},
    "model_41714_1d49f4d1_0010": {"func": model_41714_1d49f4d1_0010, "volume": 0.0003217592, "area": 0.0516841629},
    "model_41714_1d49f4d1_0013": {"func": model_41714_1d49f4d1_0013, "volume": 1.2468170908, "area": 8.4873502749},
    "model_41714_1d49f4d1_0016": {"func": model_41714_1d49f4d1_0016, "volume": 0.4916119514, "area": 6.0645042018},
    "model_41714_1d49f4d1_0017": {"func": model_41714_1d49f4d1_0017, "volume": 0.1287036997, "area": 2.1281714122},
    "model_41715_e1936a52_0000": {"func": model_41715_e1936a52_0000, "volume": 2253.0650658726, "area": 3303.0522413923},
    "model_41716_d55164d4_0002": {"func": model_41716_d55164d4_0002, "volume": 0.2010995308, "area": 1.9001530466},
    "model_41716_d55164d4_0004": {"func": model_41716_d55164d4_0004, "volume": 383.1550230327, "area": 705.8549430431},
    "model_41716_d55164d4_0007": {"func": model_41716_d55164d4_0007, "volume": 24.456821292, "area": 66.5250435061},
    "model_41717_008d27ad_0000": {"func": model_41717_008d27ad_0000, "volume": 5.1666363425, "area": 78.5841573095},
    "model_41717_9450c6b4_0000": {"func": model_41717_9450c6b4_0000, "volume": 0.3928330334, "area": 7.9566606689},
    "model_41722_92ab0003_0002": {"func": model_41722_92ab0003_0002, "volume": 25.5440611308, "area": 215.7326545376},
    "model_41722_92ab0003_0003": {"func": model_41722_92ab0003_0003, "volume": 102.4191502461, "area": 229.0317994186},
    "model_41722_92ab0003_0004": {"func": model_41722_92ab0003_0004, "volume": 53.2021146479, "area": 440.1938951366},
    "model_41722_92ab0003_0005": {"func": model_41722_92ab0003_0005, "volume": 6.3099940327, "area": 24.9410717444},
    "model_41722_92ab0003_0006": {"func": model_41722_92ab0003_0006, "volume": 235.269077848, "area": 1886.1332528746},
    "model_41722_92ab0003_0008": {"func": model_41722_92ab0003_0008, "volume": 149.3628858434, "area": 1202.1958542605},
    "model_41722_92ab0003_0009": {"func": model_41722_92ab0003_0009, "volume": 41.5069431503, "area": 133.2640670026},
    "model_41722_92ab0003_0010": {"func": model_41722_92ab0003_0010, "volume": 52.8482814, "area": 596.93429},
    "model_41722_92ab0003_0011": {"func": model_41722_92ab0003_0011, "volume": 76.8995650744, "area": 164.7841479352},
    "model_41729_b5092135_0008": {"func": model_41729_b5092135_0008, "volume": 44.8, "area": 452.48},
    "model_41733_1ec9b00c_0000": {"func": model_41733_1ec9b00c_0000, "volume": 2235.102306791, "area": 1662.8801289288},
    "model_41733_1ec9b00c_0008": {"func": model_41733_1ec9b00c_0008, "volume": 3152.5101553804, "area": 2080.1237378604},
    "model_41733_1ec9b00c_0009": {"func": model_41733_1ec9b00c_0009, "volume": 8072.7278936951, "area": 4007.2727893695},
    "model_41733_1ec9b00c_0013": {"func": model_41733_1ec9b00c_0013, "volume": 270000.0000000005, "area": 73500},
    "model_41733_1ec9b00c_0019": {"func": model_41733_1ec9b00c_0019, "volume": 863.2748503971, "area": 720.502668055},
    "model_41737_3653024c_0000": {"func": model_41737_3653024c_0000, "volume": 0.2284299537, "area": 2.5359269525},
    "model_41737_64cdca02_0000": {"func": model_41737_64cdca02_0000, "volume": 45.3960151973, "area": 71.5654819858},
    "model_41737_7a3bf600_0000": {"func": model_41737_7a3bf600_0000, "volume": 801.9384276595, "area": 631.3617861063},
    "model_41737_a8d6ea5d_0000": {"func": model_41737_a8d6ea5d_0000, "volume": 1.9062130064, "area": 18.4486357832},
    "model_41737_af56d74d_0000": {"func": model_41737_af56d74d_0000, "volume": 0.9344761111, "area": 16.1067842234},
    "model_41737_b6724677_0000": {"func": model_41737_b6724677_0000, "volume": 126.5008239813, "area": 151.8500081118},
    "model_41737_d80c34b9_0000": {"func": model_41737_d80c34b9_0000, "volume": 2.9678571429, "area": 28.2058027477},
    "model_41737_dd3de5eb_0000": {"func": model_41737_dd3de5eb_0000, "volume": 5.9357191018, "area": 35.9515194861},
    "model_41738_065c1320_0002": {"func": model_41738_065c1320_0002, "volume": 628.960582003, "area": 2074.4569270674},
    "model_41739_1bc15d9f_0001": {"func": model_41739_1bc15d9f_0001, "volume": 63.8357480096, "area": 151.8085473227},
    "model_41739_1bc15d9f_0005": {"func": model_41739_1bc15d9f_0005, "volume": 84.5737751408, "area": 185.5319568865},
    "model_41739_1bc15d9f_0010": {"func": model_41739_1bc15d9f_0010, "volume": 112.4535705678, "area": 230.4921115068},
    "model_41739_1bc15d9f_0012": {"func": model_41739_1bc15d9f_0012, "volume": 0.5559999827, "area": 4.2320208654},
    "model_41757_c1173a7e_0008": {"func": model_41757_c1173a7e_0008, "volume": 1087.546262387, "area": 1844.4152239149},
    "model_41757_c1173a7e_0010": {"func": model_41757_c1173a7e_0010, "volume": 482.6388738404, "area": 405.365983278},
    "model_41757_c1173a7e_0023": {"func": model_41757_c1173a7e_0023, "volume": 15.1695051448, "area": 244.7285428},
    "model_41764_6707e462_0000": {"func": model_41764_6707e462_0000, "volume": 2, "area": 13},
    "model_41764_6707e462_0001": {"func": model_41764_6707e462_0001, "volume": 0.3125, "area": 3.625},
    "model_41764_6707e462_0002": {"func": model_41764_6707e462_0002, "volume": 0.2269984382, "area": 2.7779693606},
    "model_41764_6707e462_0003": {"func": model_41764_6707e462_0003, "volume": 2.0507256842, "area": 12.6431881174},
    "model_41764_6707e462_0005": {"func": model_41764_6707e462_0005, "volume": 0.5, "area": 5.5},
    "model_41764_6707e462_0006": {"func": model_41764_6707e462_0006, "volume": 2.2187155295, "area": 13.3723857236},
    "model_41776_50aabc9d_0002": {"func": model_41776_50aabc9d_0002, "volume": 1.5533185602, "area": 33.4145127126},
    "model_41778_3d8cc892_0000": {"func": model_41778_3d8cc892_0000, "volume": 117.6432254986, "area": 191.9154577082},
    "model_41778_3d8cc892_0002": {"func": model_41778_3d8cc892_0002, "volume": 16.387064, "area": 54.8386},
    "model_41778_3d8cc892_0004": {"func": model_41778_3d8cc892_0004, "volume": 61.6683777068, "area": 164.9839551941},
    "model_41778_3d8cc892_0007": {"func": model_41778_3d8cc892_0007, "volume": 3.8611109907, "area": 27.3622038713},
    "model_41785_37ab51ed_0000": {"func": model_41785_37ab51ed_0000, "volume": 17.6195364877, "area": 49.6826683255},
    "model_41868_002280d0_0000": {"func": model_41868_002280d0_0000, "volume": 0.1546756455, "area": 3.8591626625},
    "model_41868_4e7423ae_0000": {"func": model_41868_4e7423ae_0000, "volume": 0.0331830724, "area": 1.0475640703},
    "model_41868_629410cd_0000": {"func": model_41868_629410cd_0000, "volume": 0.0012151309, "area": 0.2698062701},
    "model_41868_6791916d_0000": {"func": model_41868_6791916d_0000, "volume": 0.0023555442, "area": 0.2858081047},
    "model_41868_8e597530_0000": {"func": model_41868_8e597530_0000, "volume": 0.0618501054, "area": 1.6846790605},
    "model_41868_a4a9d650_0000": {"func": model_41868_a4a9d650_0000, "volume": 0.0010454757, "area": 0.2478929796},
    "model_41868_c16c1f64_0000": {"func": model_41868_c16c1f64_0000, "volume": 0.0012442285, "area": 0.281647675},
    "model_41896_7d8659e6_0001": {"func": model_41896_7d8659e6_0001, "volume": 16.4933614313, "area": 331.1866975414},
    "model_41896_7d8659e6_0013": {"func": model_41896_7d8659e6_0013, "volume": 21.7947990343, "area": 292.3409043798},
    "model_41896_7d8659e6_0018": {"func": model_41896_7d8659e6_0018, "volume": 31.2783630699, "area": 137.2242715967},
    "model_41902_1001798c_0000": {"func": model_41902_1001798c_0000, "volume": 132.63279925, "area": 194.2741526061},
    "model_41902_363c1593_0000": {"func": model_41902_363c1593_0000, "volume": 468.753933896, "area": 658.7458535436},
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
