"""Batch 007 - passing/04_6to7ops
88 models bundled from Fusion360 Gallery reconstructions.
"""

from build123d import *


# Description: This is a thin, elongated rectangular plate or strap with a hexagonal or bow-tie shaped slot cut through its center, featuring tapered ends and a flat profile.
def model_39306_ee445998_0006():
    """Model: Base v6"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 125, perimeter: 60
            with BuildLine():
                Line((12.5, -2.5), (-12.5, -2.5))
                Line((12.5, 2.5), (12.5, -2.5))
                Line((-12.5, 2.5), (12.5, 2.5))
                Line((-12.5, -2.5), (-12.5, 2.5))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            Circle(0.5)
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
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
        extrude(amount=-0.2, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a satellite or spacecraft component featuring a hexagonal/polygonal body with angled solar panels or antenna arrays extending from the top, designed for space applications.
def model_39306_ee445998_0025():
    """Model: Corner Clip v2 (2)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.5625000168, perimeter: 3.0000000447
            with BuildLine():
                Line((-0.5000000075, 0.5000000075), (0.2500000037, 0.5000000075))
                Line((-0.5000000075, -0.2500000037), (-0.5000000075, 0.5000000075))
                Line((0.2500000037, -0.2500000037), (-0.5000000075, -0.2500000037))
                Line((0.2500000037, 0.5000000075), (0.2500000037, -0.2500000037))
            make_face()
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-0.5000000075, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.040000001, perimeter: 0.8000000097
            with BuildLine():
                Line((0.2500000037, 0.0499999944), (0.0499999989, 0.0499999944))
                Line((0.2500000037, 0.2499999944), (0.2500000037, 0.0499999944))
                Line((0.0499999989, 0.2499999944), (0.2500000037, 0.2499999944))
                Line((0.0499999989, 0.0499999944), (0.0499999989, 0.2499999944))
            make_face()
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.3, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0021205749, perimeter: 0.2827433346
            with BuildLine():
                CenterArc((-0.1999999955, -0.4499999899), 0.0299999993, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-0.1999999955, -0.4499999899), 0.015, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.03
        extrude(amount=0.03, mode=Mode.ADD)
    return part.part


# Description: This is a parallelogram-shaped flat plate or bracket with internal diagonal ribbing or bracing elements that provide structural reinforcement across the surface.
def model_39306_ee445998_0027():
    """Model: Surface v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 5000, perimeter: 300
            with BuildLine():
                Line((50, -25), (50, 25))
                Line((50, 25), (-50, 25))
                Line((-50, 25), (-50, -25))
                Line((-50, -25), (50, -25))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch4 -> Extrude2 (Cut)
        # Sketch on Profile plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 125, perimeter: 60
            with BuildLine():
                Line((12.5, -2.5), (-12.5, -2.5))
                Line((12.5, 2.5), (12.5, -2.5))
                Line((-12.5, 2.5), (12.5, 2.5))
                Line((-12.5, -2.5), (-12.5, 2.5))
            make_face()
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a tapered duct or airflow channel with an elongated wedge-like shape, featuring a curved upper surface, a flat base, and a narrow pointed end, designed to direct or transition fluid flow.
def model_39306_ee445998_0031():
    """Model: Top Clip v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.5707963736, perimeter: 5.1415927302
            with BuildLine():
                CenterArc((0, 0), 1.0000000149, 0, 180)
                Line((-1.0000000149, 0), (1.0000000149, 0))
            make_face()
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.400000006, perimeter: 4.4000000596
            with BuildLine():
                Line((1.0000000149, 0.0482227331), (-1.0000000149, 0.0482227331))
                Line((1.0000000149, 0.0482227331), (1.0000000149, 0.2482227331))
                Line((-1.0000000149, 0.2482227331), (1.0000000149, 0.2482227331))
                Line((-1.0000000149, 0.0482227331), (-1.0000000149, 0.2482227331))
            make_face()
        # OneSide extrude, distance=-0.1
        extrude(amount=-0.1, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.3, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0021205749, perimeter: 0.2827433325
            with BuildLine():
                CenterArc((0, -0.9499999788), 0.0299999993, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, -0.9499999788), 0.0149999997, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.03
        extrude(amount=0.03, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical container or tube with a rolled-over rim at the top and a slightly tapered design, featuring a seamed or wrapped construction around its body.
def model_39389_d641313f_0063():
    """Model: Arm Pin 30mm (1) (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.0106192983, perimeter: 5.0265482457
            Circle(0.8)
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.5393804003, perimeter: 4.398229715
            Circle(0.7)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.7, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.471238898, perimeter: 9.4247779608
            with BuildLine():
                CenterArc((0, 0), 0.8, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.7, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 1.5393804003, perimeter: 4.398229715
            Circle(0.7)
        # OneSide extrude, distance=0.4
        extrude(amount=0.4, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical mesh or perforated filter component with a solid base and open mesh top surface, featuring a smaller cylindrical protrusion or mounting boss on the upper section.
def model_39390_61cd2601_0001():
    """Model: Clamp Base Spacer"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            Circle(0.4)
        # OneSide extrude, distance=0.26
        extrude(amount=0.26)

        # Sketch3 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 2.638937829, perimeter: 8.7964594301
            with BuildLine():
                CenterArc((0, 0), 1, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            Circle(0.4)
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)
    return part.part


# Description: This is an inflatable catamaran-style boat or raft featuring two parallel black pontoons connected by a blue deck platform, with a curved, tapered hull design and open cockpit area for passenger seating.
def model_39390_61cd2601_0005():
    """Model: Clamp Elbow left"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 10 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 9.6915973075, perimeter: 19.8615078373
            with BuildLine():
                CenterArc((0, 0), 1.2, 101.4638719532, 163.5752795537)
                Line((-0.2385, 1.1760602663), (-4.5697559027, 0.7969530187))
                CenterArc((-4.5, 0), 0.8, 95.0022508766, 84.9977491234)
                Line((-5.3, 0), (-5.3, -2.1867048252))
                Line((-3.6991538164, -2.1867048252), (-5.3, -2.1867048252))
                Line((-3.6991538164, -1.5357048252), (-3.6991538164, -2.1867048252))
                CenterArc((-3.09917, -1.5357048252), 0.5999838164, 84.9992364874, 95.0007635126)
                Line((-0.10377, -1.1955048252), (-3.04687, -0.9380048252))
            make_face()
            with BuildLine():
                CenterArc((-4.5, 0), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 4.0212385966, perimeter: 10.0530964915
            with BuildLine():
                CenterArc((0, 0), 1.2, 101.4638719532, 163.5752795537)
                CenterArc((0, 0), 1.2, -94.9608484931, 196.4247204463)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.25
        extrude(amount=0.25)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-5.3, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.6118703829, perimeter: 5.3951037713
            with BuildLine():
                Line((2.4341795714, 0.1025), (2.5523795714, 0.2207))
                CenterArc((2.6230795714, 0.15), 0.0999848989, 90, 45)
                Line((2.6230795714, 0.2499848989), (4.5500795714, 0.2499848989))
                Line((4.5500795714, 0.2499848989), (4.5500795714, 0.4999763702))
                Line((2.6230795714, 0.4999763702), (4.5500795714, 0.4999763702))
                CenterArc((2.6230795714, 0.15), 0.3499763702, 90, 44.9979118916)
                Line((2.2574118955, 0.2792857143), (2.3756179259, 0.3974796834))
                CenterArc((2.1867048252, 0.35), 0.1, -90, 44.9970767459)
                Line((2.1867048252, 0), (2.1867048252, 0.25))
                CenterArc((2.1867048252, 0.35), 0.35, -90, 44.9970767459)
            make_face()
        # OneSide extrude, distance=-1.6
        extrude(amount=-1.6, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.4999763702, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.8639379797, perimeter: 4.4557519189
            with BuildLine():
                Line((5.3, 4.5500795714), (4.8, 4.5500795714))
                CenterArc((4.5, 4.5500795714), 0.3, 180, 180)
                Line((4.2, 4.5500795714), (3.7, 4.5500795714))
                CenterArc((4.5, 4.5500795714), 0.8, 180, 180)
            make_face()
            # Profile area: 0.8639379797, perimeter: 4.4557519189
            with BuildLine():
                CenterArc((4.5, 4.5500795714), 0.8, 0, 180)
                Line((4.2, 4.5500795714), (3.7, 4.5500795714))
                CenterArc((4.5, 4.5500795714), 0.3, 0, 180)
                Line((5.3, 4.5500795714), (4.8, 4.5500795714))
            make_face()
        # OneSide extrude, distance=-0.25
        extrude(amount=-0.25, mode=Mode.ADD)

        # Sketch3 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.4999763702, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1413716694, perimeter: 1.5424777961
            with BuildLine():
                Line((4.8, 4.5500795714), (4.2, 4.5500795714))
                CenterArc((4.5, 4.5500795714), 0.3, 180, 180)
            make_face()
        # OneSide extrude, distance=-1.05
        extrude(amount=-1.05, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a sheet metal duct or air channel component with a curved, bird-like profile featuring a horizontal base section, a vertical rising section, and a curved upper portion with a pointed outlet end.
def model_39850_b2aa4f1e_0009():
    """Model: trigger v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude3 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 5 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.6129000257, perimeter: 7.0749113379
            with BuildLine():
                Line((1.27, 2.54), (2.54, 2.54))
                Line((1.2700000405, 0), (1.27, 2.54))
                CenterArc((1.2700000608, 0.6349999848), 0.6349999848, -90.0000018286, 90.0000032)
                Line((1.9050000456, 0.635), (1.9050000152, 1.905))
                CenterArc((2.54, 1.9050000152), 0.6349999848, 90, 90.0000013714)
            make_face()
        # OneSide extrude, distance=1.27
        extrude(amount=1.27)

        # Sketch1 -> Extrude4 (Join)
        # Sketch on XY construction plane
        # Sketch has 5 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 3.2258000515, perimeter: 7.6200000405
            with BuildLine():
                Line((0, 2.54), (1.27, 2.54))
                Line((0, 0), (0, 2.54))
                Line((0, 0), (1.2700000405, 0))
                Line((1.2700000405, 0), (1.27, 2.54))
            make_face()
        # OneSide extrude, distance=1.27
        extrude(amount=1.27, mode=Mode.ADD)

        # Sketch2 -> Extrude5 (Join)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.5220079028, perimeter: 12.1549113756
            with BuildLine():
                Line((0, 0), (-3.81, 0))
                Line((-3.81, 0), (-3.81, -1.2700000405))
                Line((0, -1.27), (-3.81, -1.2700000405))
                Line((0, 0), (0, -1.27))
            make_face()
            with BuildLine():
                CenterArc((-2.2224999572, -0.6350000257), 0.3175, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.3175
        extrude(amount=0.3175, mode=Mode.ADD)

        # Sketch2 -> Extrude6 (Join)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.3166921744, perimeter: 1.994911335
            with Locations((-2.2224999572, -0.6350000257)):
                Circle(0.3175)
        # OneSide extrude, distance=0.3175
        extrude(amount=0.3175, mode=Mode.ADD)
    return part.part


# Description: This is a kiteboard or hydrofoil wing featuring an elongated, tapered planform shape with a streamlined profile, internal structural ribs for reinforcement, and curved edges designed for hydrodynamic performance.
def model_40064_137c5d61_0001():
    """Model: Component1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 14 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 23.2495706734, perimeter: 23.0944460574
            with BuildLine():
                CenterArc((1.5, 3.7018220082), 1, 0, 86.3207373738)
                CenterArc((0, -19.625), 24.375, 86.3207373738, 3.6792626262)
                Line((0, 4.75), (0, -4.75))
                Line((0, -4.75), (1.5, -4.75))
                CenterArc((1.5, -3.75), 1, -90, 90)
                Line((2.5, -3.75), (2.5, 3.7018220082))
            make_face()
            # Profile area: 23.2495706734, perimeter: 23.0944460574
            with BuildLine():
                Line((0, 4.75), (0, -4.75))
                CenterArc((0, -19.625), 24.375, 90, 3.6792626262)
                CenterArc((-1.5, 3.7018220082), 1, 93.6792626262, 86.3207373738)
                Line((-2.5, 3.7018220082), (-2.5, -3.75))
                CenterArc((-1.5, -3.75), 1, 180, 90)
                Line((-1.5, -4.75), (0, -4.75))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch6 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-2.5, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.3, perimeter: 2.6
            with BuildLine():
                Line((3.75, 0), (3.75, 0.3))
                Line((4.75, 0), (3.75, 0))
                Line((4.75, 0), (4.75, 0.3))
                Line((3.75, 0.3), (4.75, 0.3))
            make_face()
            # Profile area: 0.6, perimeter: 4.6
            with BuildLine():
                Line((1.75, 0.3), (3.75, 0.3))
                Line((1.75, 0), (1.75, 0.3))
                Line((3.75, 0), (1.75, 0))
                Line((3.75, 0), (3.75, 0.3))
            make_face()
            # Profile area: 0.2778621141, perimeter: 2.4524140941
            with BuildLine():
                Line((5.676207047, 0), (4.75, 0))
                Line((5.676207047, 0.3), (5.676207047, 0))
                Line((4.75, 0.3), (5.676207047, 0.3))
                Line((4.75, 0), (4.75, 0.3))
            make_face()
        # OneSide extrude, distance=-5.2
        extrude(amount=-5.2, mode=Mode.SUBTRACT)

        # Sketch7 -> Extrude6 (Cut)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-2.5, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.9493011715, perimeter: 4.4941122773
            with BuildLine():
                Line((-3.7018220082, 1), (-3.7018220082, 0.3551473206))
                Line((-5.1491115553, 1), (-3.7018220082, 1))
                Line((-5.1491115553, 1), (-5.1491115553, 0.3000000045))
                Line((-5.1491115553, 0.3000000045), (-4.8000000715, 0.5000000075))
                Line((-4.8000000715, 0.5000000075), (-4.8000000715, 0.3000000045))
                Line((-4.8000000715, 0.3000000045), (-4.7495741271, 0.3))
                Line((-4.7495741271, 0.3), (-3.7018220082, 0.3551473206))
            make_face()
            # Profile area: 3.3439552657, perimeter: 15.8114455038
            with BuildLine():
                Line((-3.7018220082, 0.3551473206), (3.75, 0.7473660615))
                Line((3.75, 0.7473660615), (3.75, 1))
                Line((-3.7018220082, 1), (3.75, 1))
                Line((-3.7018220082, 1), (-3.7018220082, 0.3551473206))
            make_face()
            # Profile area: 0.2263169692, perimeter: 2.4540181462
            with BuildLine():
                Line((3.75, 0.7473660615), (3.75, 1))
                Line((3.75, 0.7473660615), (4.75, 0.8))
                Line((4.75, 1), (4.75, 0.8))
                Line((3.75, 1), (4.75, 1))
            make_face()
        # OneSide extrude, distance=-5.7
        extrude(amount=-5.7, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical container or barrel with a curved, slightly tapered body and an open top with a flat or beveled rim, appearing to be a storage vessel or industrial drum.
def model_40070_be9c502b_0013():
    """Model: czubek v11"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 11.3411494795, perimeter: 11.9380520836
            Circle(1.9)
        # OneSide extrude, distance=-4
        extrude(amount=-4)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 7.3400002784, perimeter: 11.811644871
            with BuildLine():
                Line((2.6000000387, -4.70000007), (-0.1000000015, -4.900000073))
                Line((2.6000000387, -1.7000000253), (2.6000000387, -4.70000007))
                Line((1.9000000283, -0.6000000089), (2.6000000387, -1.7000000253))
                Line((0, -4), (1.9000000283, -0.6000000089))
                Line((-0.1000000015, -4.900000073), (0, -4))
            make_face()
        # Symmetric extrude, each_side=4.3
        extrude(amount=4.3, both=True, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical sleeve or bushing with a hollow center, featuring a rectangular slot or opening cut through the top portion and a mesh or perforated pattern on the upper outer surface.
def model_40072_b44084ae_0013():
    """Model: ustnik dol v5"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.6283185644, perimeter: 6.2831853634
            with BuildLine():
                CenterArc((0, 0), 0.6000000089, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.2199114773, perimeter: 4.3982297431
            with BuildLine():
                CenterArc((0, 0), 0.4, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.3000000045, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.2827433472, perimeter: 1.8849556202
            Circle(0.3000000045)
        # OneSide extrude, distance=0.7
        extrude(amount=0.7)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.7, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            Circle(0.3)
        # OneSide extrude, distance=-1.8
        extrude(amount=-1.8, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical sleeve or tube with a slightly tapered design, featuring an open top with a mesh or perforated circular opening and a solid curved sidewall body.
def model_40072_b44084ae_0016():
    """Model: wejscie wezyk v5"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.3561944902, perimeter: 9.4247779608
            with BuildLine():
                CenterArc((0, 0), 1, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            Circle(0.5)
        # OneSide extrude, distance=3
        extrude(amount=3)
    return part.part


# Description: This is a ring or collar-shaped component with an oval/elliptical cross-section, featuring a central longitudinal slot or opening along the top surface and vertical ribbing or fluting around its outer walls for structural reinforcement.
def model_40074_4615c9d1_0002():
    """Model: mocowanie sufit v4"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 113.0973355292, perimeter: 37.6991118431
            Circle(6)
        # OneSide extrude, distance=3
        extrude(amount=3)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 78.5398163397, perimeter: 31.4159265359
            Circle(5)
        # OneSide extrude, distance=-2
        extrude(amount=-2, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude3 (Cut)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 2, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            Circle(0.5)
        # OneSide extrude, distance=-4.5
        extrude(amount=-4.5, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a truncated rectangular box or beveled container with a trapezoidal profile, featuring angled/chamfered top edges, internal cross-bracing or ribbing for structural support, and a hollow interior cavity.
def model_40074_4615c9d1_0003():
    """Model: gora przyrywka v3"""
    with BuildPart() as part:
        # Sketch3 -> Extrude2 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 221.7025033688, perimeter: 55.4256258422
            with BuildLine():
                Line((8, -4.6188021535), (8, 4.6188021535))
                Line((8, 4.6188021535), (0, 9.237604307))
                Line((0, 9.237604307), (-8, 4.6188021535))
                Line((-8, 4.6188021535), (-8, -4.6188021535))
                Line((-8, -4.6188021535), (0, -9.237604307))
                Line((0, -9.237604307), (8, -4.6188021535))
            make_face()
        # OneSide extrude, distance=7
        extrude(amount=7)

        # Sketch4 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 7, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            Circle(0.5)
        # OneSide extrude, distance=-12
        extrude(amount=-12, mode=Mode.SUBTRACT)
    return part.part


# Description: This is an oval or elliptical boat hull featuring a shallow, streamlined shape with a curved bottom, reinforced rim flange around the perimeter, and internal longitudinal ribs or stringers for structural support.
def model_40074_4615c9d1_0011():
    """Model: dol 3 v5"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 113.0973355292, perimeter: 37.6991118431
            Circle(6)
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


# Description: This is a cylindrical sleeve or tube with a curved, tapered top edge and vertical ribbed or fluted surface details running along its length.
def model_40074_4615c9d1_0012():
    """Model: na zarowke v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 9.6211275016, perimeter: 10.9955742876
            Circle(1.75)
        # OneSide extrude, distance=4.5
        extrude(amount=4.5)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 4.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 5.7255526112, perimeter: 8.4823001647
            Circle(1.35)
        # OneSide extrude, distance=-2.7
        extrude(amount=-2.7, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.8, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            Circle(0.5)
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical housing or drum component with a ribbed/finned exterior surface and a large central hollow cavity, featuring vertical slots or fins around the outer perimeter and what appears to be mounting points or openings along the base.
def model_40159_583632c6_0002():
    """Model: opona v2 (3)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.3561948179, perimeter: 9.4247773054
            with BuildLine():
                CenterArc((-7.5, 5), 1, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-7.5, 5), 0.4999998957, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.7
        extrude(amount=0.7)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.7, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0050416728, perimeter: 0.3025430889
            with BuildLine():
                CenterArc((7.5, -5), 1, 33.1340202489, 5.7319680507)
                Line((8.3373943125, -4.4534007269), (8.3788569856, -4.4232763316))
                Line((8.3788569856, -4.4232763316), (8.3200784595, -4.342374631))
                Line((8.3200784595, -4.342374631), (8.2786157804, -4.3724990307))
            make_face()
            # Profile area: 0.0049583275, perimeter: 0.2975403473
            with BuildLine():
                Line((8.2786157804, -4.3724990307), (8.2391767588, -4.4011531571))
                Line((8.2391767588, -4.4011531571), (8.297955285, -4.4820548577))
                Line((8.297955285, -4.4820548577), (8.3373943125, -4.4534007269))
                CenterArc((7.5, -5), 1, 33.1340202489, 5.7319680507)
            make_face()
            # Profile area: 0.0050416728, perimeter: 0.3025430889
            with BuildLine():
                CenterArc((7.5, -5), 1, 47.5340202489, 5.7319680507)
                Line((8.1751523188, -4.2623216511), (8.2078207333, -4.2228323216))
                Line((8.2078207333, -4.2228323216), (8.1307694079, -4.1590899217))
                Line((8.1307694079, -4.1590899217), (8.0981009886, -4.1985792569))
            make_face()
            # Profile area: 0.0049583275, perimeter: 0.2975403473
            with BuildLine():
                Line((8.0981009886, -4.1985792569), (8.0670270079, -4.2361412471))
                Line((8.0670270079, -4.2361412471), (8.1440783334, -4.299883647))
                Line((8.1440783334, -4.299883647), (8.1751523188, -4.2623216511))
                CenterArc((7.5, -5), 1, 47.5340202489, 5.7319680507)
            make_face()
            # Profile area: 0.0050416728, perimeter: 0.3025430889
            with BuildLine():
                CenterArc((7.5, -5), 1, 61.9340202489, 5.7319680507)
                Line((7.9704880218, -4.117593619), (7.9923095011, -4.071220615))
                Line((7.9923095011, -4.071220615), (7.9018267945, -4.0286426853))
                Line((7.9018267945, -4.0286426853), (7.8800053121, -4.0750156959))
            make_face()
            # Profile area: 0.0049583275, perimeter: 0.2975403473
            with BuildLine():
                Line((7.8800053121, -4.0750156959), (7.8592488647, -4.1191253919))
                Line((7.8592488647, -4.1191253919), (7.9497315713, -4.1617033216))
                Line((7.9497315713, -4.1617033216), (7.9704880218, -4.117593619))
                CenterArc((7.5, -5), 1, 61.9340202489, 5.7319680507)
            make_face()
            # Profile area: 0.0049583275, perimeter: 0.2975403473
            with BuildLine():
                Line((7.6380325042, -4.0095723006), (7.6288977941, -4.0574581279))
                Line((7.6288977941, -4.0574581279), (7.7271265206, -4.0761962596))
                Line((7.7271265206, -4.0761962596), (7.7362612321, -4.028310425))
                CenterArc((7.5, -5), 1, 76.3340202489, 5.7319680507)
            make_face()
            # Profile area: 0.0050416728, perimeter: 0.3025430889
            with BuildLine():
                CenterArc((7.5, -5), 1, 76.3340202489, 5.7319680507)
                Line((7.7362612321, -4.028310425), (7.7458646524, -3.9779675331))
                Line((7.7458646524, -3.9779675331), (7.6476359259, -3.9592294013))
                Line((7.6476359259, -3.9592294013), (7.6380325042, -4.0095723006))
            make_face()
            # Profile area: 0.0049583275, perimeter: 0.2975403473
            with BuildLine():
                Line((7.3873866064, -4.0063611201), (7.3904476011, -4.0550142361))
                Line((7.3904476011, -4.0550142361), (7.4902502754, -4.0487351841))
                Line((7.4902502754, -4.0487351841), (7.4871892803, -4.0000820606))
                CenterArc((7.5, -5), 1, 90.7340202489, 5.7319680507)
            make_face()
            # Profile area: 0.0050416728, perimeter: 0.3025430889
            with BuildLine():
                CenterArc((7.5, -5), 1, 90.7340202489, 5.7319680507)
                Line((7.4871892803, -4.0000820606), (7.4839712233, -3.9489325097))
                Line((7.4839712233, -3.9489325097), (7.384168549, -3.9552115618))
                Line((7.384168549, -3.9552115618), (7.3873866064, -4.0063611201))
            make_face()
            # Profile area: 0.0049583275, perimeter: 0.2975403473
            with BuildLine():
                Line((7.1438166224, -4.0655839248), (7.1588809881, -4.1119472753))
                Line((7.1588809881, -4.1119472753), (7.2539866412, -4.0810455754))
                Line((7.2539866412, -4.0810455754), (7.2389222731, -4.0346822179))
                CenterArc((7.5, -5), 1, 105.1340202489, 5.7319680507)
            make_face()
            # Profile area: 0.0050416728, perimeter: 0.3025430889
            with BuildLine():
                CenterArc((7.5, -5), 1, 105.1340202489, 5.7319680507)
                Line((7.2389222731, -4.0346822179), (7.2230849413, -3.9859399224))
                Line((7.2230849413, -3.9859399224), (7.1279792882, -4.0168416223))
                Line((7.1279792882, -4.0168416223), (7.1438166224, -4.0655839248))
            make_face()
            # Profile area: 0.0049583275, perimeter: 0.2975403473
            with BuildLine():
                Line((6.9226269499, -4.1835195281), (6.9487481373, -4.2246799333))
                Line((6.9487481373, -4.2246799333), (7.0331809311, -4.171097253))
                Line((7.0331809311, -4.171097253), (7.0070597397, -4.1299368415))
                CenterArc((7.5, -5), 1, 119.5340202489, 5.7319680507)
            make_face()
            # Profile area: 0.0050416728, perimeter: 0.3025430889
            with BuildLine():
                CenterArc((7.5, -5), 1, 119.5340202489, 5.7319680507)
                Line((7.0070597397, -4.1299368415), (6.9795982508, -4.0866644591))
                Line((6.9795982508, -4.0866644591), (6.895165457, -4.1402471394))
                Line((6.895165457, -4.1402471394), (6.9226269499, -4.1835195281))
            make_face()
            # Profile area: 0.0049583275, perimeter: 0.2975403473
            with BuildLine():
                Line((6.7377157495, -4.3527576022), (6.7732524683, -4.3861288024))
                Line((6.7732524683, -4.3861288024), (6.8417071799, -4.3132319386))
                Line((6.8417071799, -4.3132319386), (6.8061704557, -4.2798607333))
                CenterArc((7.5, -5), 1, 133.9340202489, 5.7319680507)
            make_face()
            # Profile area: 0.0050416728, perimeter: 0.3025430889
            with BuildLine():
                CenterArc((7.5, -5), 1, 133.9340202489, 5.7319680507)
                Line((6.8061704557, -4.2798607333), (6.7688103161, -4.244777227))
                Line((6.7688103161, -4.244777227), (6.7003556045, -4.3176740908))
                Line((6.7003556045, -4.3176740908), (6.7377157495, -4.3527576022))
            make_face()
            # Profile area: 0.0050416728, perimeter: 0.3025430889
            with BuildLine():
                CenterArc((7.5, -5), 1, 148.3340202489, 5.7319680507)
                Line((6.6488770337, -4.4750336237), (6.6039657183, -4.4503434191))
                Line((6.6039657183, -4.4503434191), (6.5557903502, -4.5379740884))
                Line((6.5557903502, -4.5379740884), (6.6007016721, -4.5626642966))
            make_face()
            # Profile area: 0.0049583275, perimeter: 0.2975403473
            with BuildLine():
                Line((6.6007016721, -4.5626642966), (6.6434210195, -4.5861494566))
                Line((6.6434210195, -4.5861494566), (6.6915963877, -4.4985187873))
                Line((6.6915963877, -4.4985187873), (6.6488770337, -4.4750336237))
                CenterArc((7.5, -5), 1, 148.3340202489, 5.7319680507)
            make_face()
            # Profile area: 0.0049583275, perimeter: 0.2975403473
            with BuildLine():
                Line((6.5201938161, -4.8000504016), (6.5674115784, -4.8121738624))
                Line((6.5674115784, -4.8121738624), (6.5922805675, -4.7153155449))
                Line((6.5922805675, -4.7153155449), (6.5450627979, -4.7031920822))
                CenterArc((7.5, -5), 1, 162.7340202489, 5.7319680507)
            make_face()
            # Profile area: 0.0050416728, perimeter: 0.3025430889
            with BuildLine():
                CenterArc((7.5, -5), 1, 162.7340202489, 5.7319680507)
                Line((6.5450627979, -4.7031920822), (6.4954222499, -4.6904465558))
                Line((6.4954222499, -4.6904465558), (6.4705532608, -4.7873048733))
                Line((6.4705532608, -4.7873048733), (6.5201938161, -4.8000504016))
            make_face()
            # Profile area: 0.0050416728, perimeter: 0.3025430889
            with BuildLine():
                CenterArc((7.5, -5), 1, 177.1340202489, 5.7319680507)
                Line((6.5012507785, -4.9500000738), (6.4500000961, -4.9500000738))
                Line((6.4500000961, -4.9500000738), (6.4500000961, -5.0500000753))
                Line((6.4500000961, -5.0500000753), (6.501250786, -5.0500000753))
            make_face()
            # Profile area: 0.0049583275, perimeter: 0.2975403473
            with BuildLine():
                Line((6.501250786, -5.0500000753), (6.5500000976, -5.0500000753))
                Line((6.5500000976, -5.0500000753), (6.5500000976, -4.9500000738))
                Line((6.5500000976, -4.9500000738), (6.5012507785, -4.9500000738))
                CenterArc((7.5, -5), 1, 177.1340202489, 5.7319680507)
            make_face()
            # Profile area: 0.0050416728, perimeter: 0.3025430889
            with BuildLine():
                CenterArc((7.5, -5), 1, -168.4659797511, 5.7319680507)
                Line((6.5201938459, -5.1999497446), (6.4705532979, -5.212695271))
                Line((6.4705532979, -5.212695271), (6.495422287, -5.3095535886))
                Line((6.495422287, -5.3095535886), (6.5450628422, -5.2968080603))
            make_face()
            # Profile area: 0.0049583275, perimeter: 0.2975403473
            with BuildLine():
                Line((6.5450628422, -5.2968080603), (6.5922806045, -5.2846845995))
                Line((6.5922806045, -5.2846845995), (6.5674116154, -5.1878262819))
                Line((6.5674116154, -5.1878262819), (6.5201938459, -5.1999497446))
                CenterArc((7.5, -5), 1, -168.4659797511, 5.7319680507)
            make_face()
            # Profile area: 0.0049583275, perimeter: 0.2975403473
            with BuildLine():
                Line((6.648877112, -5.5249665033), (6.6915964594, -5.5014813433))
                Line((6.6915964594, -5.5014813433), (6.6434210913, -5.413850674))
                Line((6.6434210913, -5.413850674), (6.6007017374, -5.4373358376))
                CenterArc((7.5, -5), 1, -154.0659797511, 5.7319680507)
            make_face()
            # Profile area: 0.0050416728, perimeter: 0.3025430889
            with BuildLine():
                CenterArc((7.5, -5), 1, -154.0659797511, 5.7319680507)
                Line((6.6007017374, -5.4373358376), (6.555790422, -5.4620260421))
                Line((6.555790422, -5.4620260421), (6.6039657901, -5.5496567114))
                Line((6.6039657901, -5.5496567114), (6.648877112, -5.5249665033))
            make_face()
            # Profile area: 0.0049583275, perimeter: 0.2975403473
            with BuildLine():
                Line((6.8061705631, -5.7201393702), (6.8417072819, -5.68676817))
                Line((6.8417072819, -5.68676817), (6.7732525703, -5.6138713062))
                Line((6.7732525703, -5.6138713062), (6.7377158461, -5.6472425115))
                CenterArc((7.5, -5), 1, -139.6659797511, 5.7319680507)
            make_face()
            # Profile area: 0.0050416728, perimeter: 0.3025430889
            with BuildLine():
                CenterArc((7.5, -5), 1, -139.6659797511, 5.7319680507)
                Line((6.7377158461, -5.6472425115), (6.7003557065, -5.6823260178))
                Line((6.7003557065, -5.6823260178), (6.7688104181, -5.7552228817))
                Line((6.7688104181, -5.7552228817), (6.8061705631, -5.7201393702))
            make_face()
            # Profile area: 0.0049583275, perimeter: 0.2975403473
            with BuildLine():
                Line((7.0070598695, -5.870063232), (7.0331810569, -5.8289028269))
                Line((7.0331810569, -5.8289028269), (6.9487482631, -5.7753201466))
                Line((6.9487482631, -5.7753201466), (6.9226270717, -5.816480558))
                CenterArc((7.5, -5), 1, -125.2659797511, 5.7319680507)
            make_face()
            # Profile area: 0.0050416728, perimeter: 0.3025430889
            with BuildLine():
                CenterArc((7.5, -5), 1, -125.2659797511, 5.7319680507)
                Line((6.9226270717, -5.816480558), (6.8951655828, -5.8597529404))
                Line((6.8951655828, -5.8597529404), (6.9795983766, -5.9133356207))
                Line((6.9795983766, -5.9133356207), (7.0070598695, -5.870063232))
            make_face()
            # Profile area: 0.0049583275, perimeter: 0.2975403473
            with BuildLine():
                Line((7.2389224171, -5.9653178211), (7.2539867829, -5.9189544706))
                Line((7.2539867829, -5.9189544706), (7.1588811298, -5.8880527707))
                Line((7.1588811298, -5.8880527707), (7.1438167618, -5.9344161283))
                CenterArc((7.5, -5), 1, -110.8659797511, 5.7319680507)
            make_face()
            # Profile area: 0.0050416728, perimeter: 0.3025430889
            with BuildLine():
                CenterArc((7.5, -5), 1, -110.8659797511, 5.7319680507)
                Line((7.1438167618, -5.9344161283), (7.1279794299, -5.9831584238))
                Line((7.1279794299, -5.9831584238), (7.223085083, -6.0140601237))
                Line((7.223085083, -6.0140601237), (7.2389224171, -5.9653178211))
            make_face()
            # Profile area: 0.0049583275, perimeter: 0.2975403473
            with BuildLine():
                Line((7.4871894295, -5.9999179413), (7.4902504241, -5.9512648253))
                Line((7.4902504241, -5.9512648253), (7.3904477498, -5.9449857733))
                Line((7.3904477498, -5.9449857733), (7.3873867547, -5.9936388967))
                CenterArc((7.5, -5), 1, -96.4659797511, 5.7319680507)
            make_face()
            # Profile area: 0.0050416728, perimeter: 0.3025430889
            with BuildLine():
                CenterArc((7.5, -5), 1, -96.4659797511, 5.7319680507)
                Line((7.3873867547, -5.9936388967), (7.3841686977, -6.0447884476))
                Line((7.3841686977, -6.0447884476), (7.4839713721, -6.0510674996))
                Line((7.4839713721, -6.0510674996), (7.4871894295, -5.9999179413))
            make_face()
            # Profile area: 0.0050416728, perimeter: 0.3025430889
            with BuildLine():
                Line((7.9923096359, -5.9287793215), (7.9704881535, -5.8824063108))
                CenterArc((7.5, -5), 1, -67.6659797511, 5.7319680507)
                Line((7.8800054501, -5.9249842474), (7.9018269293, -5.9713572513))
                Line((7.9018269293, -5.9713572513), (7.9923096359, -5.9287793215))
            make_face()
            # Profile area: 0.0049583275, perimeter: 0.2975403473
            with BuildLine():
                CenterArc((7.5, -5), 1, -67.6659797511, 5.7319680507)
                Line((7.9704881535, -5.8824063108), (7.9497317061, -5.8382966149))
                Line((7.9497317061, -5.8382966149), (7.8592489995, -5.8808745447))
                Line((7.8592489995, -5.8808745447), (7.8800054501, -5.9249842474))
            make_face()
            # Profile area: 0.0050416728, perimeter: 0.3025430889
            with BuildLine():
                CenterArc((7.5, -5), 1, -53.2659797511, 5.7319680507)
                Line((8.0981011082, -5.8014206538), (8.1307695227, -5.8409099833))
                Line((8.1307695227, -5.8409099833), (8.2078208481, -5.7771675834))
                Line((8.2078208481, -5.7771675834), (8.1751524289, -5.7376782481))
            make_face()
            # Profile area: 0.0049583275, perimeter: 0.2975403473
            with BuildLine():
                Line((8.1751524289, -5.7376782481), (8.1440784482, -5.700116258))
                Line((8.1440784482, -5.700116258), (8.0670271227, -5.7638586579))
                Line((8.0670271227, -5.7638586579), (8.0981011082, -5.8014206538))
                CenterArc((7.5, -5), 1, -53.2659797511, 5.7319680507)
            make_face()
            # Profile area: 0.0049583275, perimeter: 0.2975403473
            with BuildLine():
                Line((8.3373943941, -5.5465991481), (8.2979553725, -5.5179450217))
                Line((8.2979553725, -5.5179450217), (8.2391768464, -5.5988467224))
                Line((8.2391768464, -5.5988467224), (8.278615874, -5.6275008532))
                CenterArc((7.5, -5), 1, -38.8659797511, 5.7319680507)
            make_face()
            # Profile area: 0.0050416728, perimeter: 0.3025430889
            with BuildLine():
                CenterArc((7.5, -5), 1, -38.8659797511, 5.7319680507)
                Line((8.278615874, -5.6275008532), (8.3200785471, -5.6576252485))
                Line((8.3200785471, -5.6576252485), (8.3788570732, -5.5767235478))
                Line((8.3788570732, -5.5767235478), (8.3373943941, -5.5465991481))
            make_face()
            # Profile area: 0.0049583275, perimeter: 0.2975403473
            with BuildLine():
                Line((8.4470197898, -5.3211752134), (8.4016938262, -5.3032293949))
                Line((8.4016938262, -5.3032293949), (8.3648813704, -5.3962070448))
                Line((8.3648813704, -5.3962070448), (8.4102073409, -5.4141528661))
                CenterArc((7.5, -5), 1, -24.4659797511, 5.7319680507)
            make_face()
            # Profile area: 0.0050416728, perimeter: 0.3025430889
            with BuildLine():
                CenterArc((7.5, -5), 1, -24.4659797511, 5.7319680507)
                Line((8.4102073409, -5.4141528661), (8.4578590203, -5.4330195007))
                Line((8.4578590203, -5.4330195007), (8.4946714762, -5.3400418507))
                Line((8.4946714762, -5.3400418507), (8.4470197898, -5.3211752134))
            make_face()
            # Profile area: 0.0050416728, perimeter: 0.3025430889
            with BuildLine():
                CenterArc((7.5, -5), 1, -10.0659797511, 5.7319680507)
                Line((8.4846071331, -5.1747821313), (8.5354536886, -5.1812055451))
                Line((8.5354536886, -5.1812055451), (8.5479870121, -5.0819940735))
                Line((8.5479870121, -5.0819940735), (8.4971404492, -5.0755706588))
            make_face()
            # Profile area: 0.0049583275, perimeter: 0.2975403473
            with BuildLine():
                Line((8.4971404492, -5.0755706588), (8.4487755405, -5.0694607499))
                Line((8.4487755405, -5.0694607499), (8.436242217, -5.1686722215))
                Line((8.436242217, -5.1686722215), (8.4846071331, -5.1747821313))
                CenterArc((7.5, -5), 1, -10.0659797511, 5.7319680507)
            make_face()
            # Profile area: 0.0049583275, perimeter: 0.2975403473
            with BuildLine():
                Line((8.484607107, -4.8252177218), (8.4362421983, -4.8313276306))
                Line((8.4362421983, -4.8313276306), (8.4487755218, -4.9305391022))
                Line((8.4487755218, -4.9305391022), (8.497140438, -4.9244291924))
                CenterArc((7.5, -5), 1, 4.3340202489, 5.7319680507)
            make_face()
            # Profile area: 0.0050416728, perimeter: 0.3025430889
            with BuildLine():
                CenterArc((7.5, -5), 1, 4.3340202489, 5.7319680507)
                Line((8.497140438, -4.9244291924), (8.5479869935, -4.9180057787))
                Line((8.5479869935, -4.9180057787), (8.5354536699, -4.8187943071))
                Line((8.5354536699, -4.8187943071), (8.484607107, -4.8252177218))
            make_face()
            # Profile area: 0.0049583275, perimeter: 0.2975403473
            with BuildLine():
                Line((8.4102072791, -4.5858469981), (8.3648813155, -4.6037928166))
                Line((8.3648813155, -4.6037928166), (8.4016937713, -4.6967704666))
                Line((8.4016937713, -4.6967704666), (8.4470197419, -4.6788246453))
                CenterArc((7.5, -5), 1, 18.7340202489, 5.7319680507)
            make_face()
            # Profile area: 0.0050416728, perimeter: 0.3025430889
            with BuildLine():
                CenterArc((7.5, -5), 1, 18.7340202489, 5.7319680507)
                Line((8.4470197419, -4.6788246453), (8.4946714213, -4.6599580108))
                Line((8.4946714213, -4.6599580108), (8.4578589655, -4.5669803608))
                Line((8.4578589655, -4.5669803608), (8.4102072791, -4.5858469981))
            make_face()
        # OneSide extrude, distance=-0.25
        extrude(amount=-0.25, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.0050416728, perimeter: 0.3025430889
            with BuildLine():
                Line((-6.4500000961, -5.0500000753), (-6.501250786, -5.0500000753))
                Line((-6.4500000961, -4.9500000738), (-6.4500000961, -5.0500000753))
                Line((-6.5012507785, -4.9500000738), (-6.4500000961, -4.9500000738))
                CenterArc((-7.5, -5), 1, -2.8659882996, 5.7319680507)
            make_face()
            # Profile area: 0.0049583275, perimeter: 0.2975403473
            with BuildLine():
                CenterArc((-7.5, -5), 1, -2.8659882996, 5.7319680507)
                Line((-6.5500000976, -4.9500000738), (-6.5012507785, -4.9500000738))
                Line((-6.5500000976, -5.0500000753), (-6.5500000976, -4.9500000738))
                Line((-6.501250786, -5.0500000753), (-6.5500000976, -5.0500000753))
            make_face()
            # Profile area: 0.0050416728, perimeter: 0.3025430889
            with BuildLine():
                Line((-6.4705532608, -4.7873048733), (-6.5201938161, -4.8000504016))
                Line((-6.4954222499, -4.6904465558), (-6.4705532608, -4.7873048733))
                Line((-6.5450627979, -4.7031920822), (-6.4954222499, -4.6904465558))
                CenterArc((-7.5, -5), 1, 11.5340117004, 5.7319680507)
            make_face()
            # Profile area: 0.0049583275, perimeter: 0.2975403473
            with BuildLine():
                CenterArc((-7.5, -5), 1, 11.5340117004, 5.7319680507)
                Line((-6.5922805675, -4.7153155449), (-6.5450627979, -4.7031920822))
                Line((-6.5674115784, -4.8121738624), (-6.5922805675, -4.7153155449))
                Line((-6.5201938161, -4.8000504016), (-6.5674115784, -4.8121738624))
            make_face()
            # Profile area: 0.0050416728, perimeter: 0.3025430889
            with BuildLine():
                Line((-6.495422287, -5.3095535886), (-6.5450628422, -5.2968080603))
                Line((-6.4705532979, -5.212695271), (-6.495422287, -5.3095535886))
                Line((-6.5201938459, -5.1999497446), (-6.4705532979, -5.212695271))
                CenterArc((-7.5, -5), 1, -17.2659882996, 5.7319680507)
            make_face()
            # Profile area: 0.0049583275, perimeter: 0.2975403473
            with BuildLine():
                CenterArc((-7.5, -5), 1, -17.2659882996, 5.7319680507)
                Line((-6.5674116154, -5.1878262819), (-6.5201938459, -5.1999497446))
                Line((-6.5922806045, -5.2846845995), (-6.5674116154, -5.1878262819))
                Line((-6.5450628422, -5.2968080603), (-6.5922806045, -5.2846845995))
            make_face()
            # Profile area: 0.0049583275, perimeter: 0.2975403473
            with BuildLine():
                CenterArc((-7.5, -5), 1, 25.9340117004, 5.7319680507)
                Line((-6.6915963877, -4.4985187873), (-6.6488770337, -4.4750336237))
                Line((-6.6434210195, -4.5861494566), (-6.6915963877, -4.4985187873))
                Line((-6.6007016721, -4.5626642966), (-6.6434210195, -4.5861494566))
            make_face()
            # Profile area: 0.0050416728, perimeter: 0.3025430889
            with BuildLine():
                Line((-6.5557903502, -4.5379740884), (-6.6007016721, -4.5626642966))
                Line((-6.6039657183, -4.4503434191), (-6.5557903502, -4.5379740884))
                Line((-6.6488770337, -4.4750336237), (-6.6039657183, -4.4503434191))
                CenterArc((-7.5, -5), 1, 25.9340117004, 5.7319680507)
            make_face()
            # Profile area: 0.0049583275, perimeter: 0.2975403473
            with BuildLine():
                CenterArc((-7.5, -5), 1, -31.6659882996, 5.7319680507)
                Line((-6.6434210913, -5.413850674), (-6.6007017374, -5.4373358376))
                Line((-6.6915964594, -5.5014813433), (-6.6434210913, -5.413850674))
                Line((-6.648877112, -5.5249665033), (-6.6915964594, -5.5014813433))
            make_face()
            # Profile area: 0.0050416728, perimeter: 0.3025430889
            with BuildLine():
                Line((-6.6039657901, -5.5496567114), (-6.648877112, -5.5249665033))
                Line((-6.555790422, -5.4620260421), (-6.6039657901, -5.5496567114))
                Line((-6.6007017374, -5.4373358376), (-6.555790422, -5.4620260421))
                CenterArc((-7.5, -5), 1, -31.6659882996, 5.7319680507)
            make_face()
            # Profile area: 0.0049583275, perimeter: 0.2975403473
            with BuildLine():
                CenterArc((-7.5, -5), 1, -46.0659882996, 5.7319680507)
                Line((-6.7732525703, -5.6138713062), (-6.7377158461, -5.6472425115))
                Line((-6.8417072819, -5.68676817), (-6.7732525703, -5.6138713062))
                Line((-6.8061705631, -5.7201393702), (-6.8417072819, -5.68676817))
            make_face()
            # Profile area: 0.0050416728, perimeter: 0.3025430889
            with BuildLine():
                Line((-6.7688104181, -5.7552228817), (-6.8061705631, -5.7201393702))
                Line((-6.7003557065, -5.6823260178), (-6.7688104181, -5.7552228817))
                Line((-6.7377158461, -5.6472425115), (-6.7003557065, -5.6823260178))
                CenterArc((-7.5, -5), 1, -46.0659882996, 5.7319680507)
            make_face()
            # Profile area: 0.0049583275, perimeter: 0.2975403473
            with BuildLine():
                CenterArc((-7.5, -5), 1, -60.4659882996, 5.7319680507)
                Line((-6.9487482631, -5.7753201466), (-6.9226270717, -5.816480558))
                Line((-7.0331810569, -5.8289028269), (-6.9487482631, -5.7753201466))
                Line((-7.0070598695, -5.870063232), (-7.0331810569, -5.8289028269))
            make_face()
            # Profile area: 0.0050416728, perimeter: 0.3025430889
            with BuildLine():
                Line((-6.9795983766, -5.9133356207), (-7.0070598695, -5.870063232))
                Line((-6.8951655828, -5.8597529404), (-6.9795983766, -5.9133356207))
                Line((-6.9226270717, -5.816480558), (-6.8951655828, -5.8597529404))
                CenterArc((-7.5, -5), 1, -60.4659882996, 5.7319680507)
            make_face()
            # Profile area: 0.0049583275, perimeter: 0.2975403473
            with BuildLine():
                Line((-7.2389224171, -5.9653178211), (-7.2539867829, -5.9189544706))
                CenterArc((-7.5, -5), 1, -74.8659882996, 5.7319680507)
                Line((-7.1588811298, -5.8880527707), (-7.1438167618, -5.9344161283))
                Line((-7.2539867829, -5.9189544706), (-7.1588811298, -5.8880527707))
            make_face()
            # Profile area: 0.0050416728, perimeter: 0.3025430889
            with BuildLine():
                Line((-7.223085083, -6.0140601237), (-7.2389224171, -5.9653178211))
                Line((-7.1279794299, -5.9831584238), (-7.223085083, -6.0140601237))
                Line((-7.1438167618, -5.9344161283), (-7.1279794299, -5.9831584238))
                CenterArc((-7.5, -5), 1, -74.8659882996, 5.7319680507)
            make_face()
            # Profile area: 0.0049583275, perimeter: 0.2975403473
            with BuildLine():
                CenterArc((-7.5, -5), 1, -89.2659882996, 5.7319680507)
                Line((-7.3904477498, -5.9449857733), (-7.3873867547, -5.9936388967))
                Line((-7.4902504241, -5.9512648253), (-7.3904477498, -5.9449857733))
                Line((-7.4871894295, -5.9999179413), (-7.4902504241, -5.9512648253))
            make_face()
            # Profile area: 0.0050416728, perimeter: 0.3025430889
            with BuildLine():
                Line((-7.4839713721, -6.0510674996), (-7.4871894295, -5.9999179413))
                Line((-7.3841686977, -6.0447884476), (-7.4839713721, -6.0510674996))
                Line((-7.3873867547, -5.9936388967), (-7.3841686977, -6.0447884476))
                CenterArc((-7.5, -5), 1, -89.2659882996, 5.7319680507)
            make_face()
            # Profile area: 0.0050416728, perimeter: 0.3025430889
            with BuildLine():
                Line((-7.7458647988, -6.022032439), (-7.7362613771, -5.9716895398))
                Line((-7.6476360722, -6.0407705708), (-7.7458647988, -6.022032439))
                Line((-7.638032652, -5.9904276788), (-7.6476360722, -6.0407705708))
                CenterArc((-7.5, -5), 1, -103.6659882996, 5.7319680507)
            make_face()
            # Profile area: 0.0049583275, perimeter: 0.2975403473
            with BuildLine():
                CenterArc((-7.5, -5), 1, -103.6659882996, 5.7319680507)
                Line((-7.6288979405, -5.9425418442), (-7.638032652, -5.9904276788))
                Line((-7.727126667, -5.9238037125), (-7.6288979405, -5.9425418442))
                Line((-7.7362613771, -5.9716895398), (-7.727126667, -5.9238037125))
            make_face()
            # Profile area: 0.0049583275, perimeter: 0.2975403473
            with BuildLine():
                CenterArc((-7.5, -5), 1, -118.0659882996, 5.7319680507)
                Line((-7.8592489995, -5.8808745447), (-7.8800054501, -5.9249842474))
                Line((-7.9497317061, -5.8382966149), (-7.8592489995, -5.8808745447))
                Line((-7.9704881535, -5.8824063108), (-7.9497317061, -5.8382966149))
            make_face()
            # Profile area: 0.0050416728, perimeter: 0.3025430889
            with BuildLine():
                Line((-7.9923096359, -5.9287793215), (-7.9704881535, -5.8824063108))
                Line((-7.9018269293, -5.9713572513), (-7.9923096359, -5.9287793215))
                Line((-7.8800054501, -5.9249842474), (-7.9018269293, -5.9713572513))
                CenterArc((-7.5, -5), 1, -118.0659882996, 5.7319680507)
            make_face()
            # Profile area: 0.0050416728, perimeter: 0.3025430889
            with BuildLine():
                Line((-8.2078208481, -5.7771675834), (-8.1751524289, -5.7376782481))
                Line((-8.1307695227, -5.8409099833), (-8.2078208481, -5.7771675834))
                Line((-8.0981011082, -5.8014206538), (-8.1307695227, -5.8409099833))
                CenterArc((-7.5, -5), 1, -132.4659882996, 5.7319680507)
            make_face()
            # Profile area: 0.0049583275, perimeter: 0.2975403473
            with BuildLine():
                CenterArc((-7.5, -5), 1, -132.4659882996, 5.7319680507)
                Line((-8.0670271227, -5.7638586579), (-8.0981011082, -5.8014206538))
                Line((-8.1440784482, -5.700116258), (-8.0670271227, -5.7638586579))
                Line((-8.1751524289, -5.7376782481), (-8.1440784482, -5.700116258))
            make_face()
            # Profile area: 0.0049583275, perimeter: 0.2975403473
            with BuildLine():
                CenterArc((-7.5, -5), 1, -146.8659882996, 5.7319680507)
                Line((-8.2391768464, -5.5988467224), (-8.278615874, -5.6275008532))
                Line((-8.2979553725, -5.5179450217), (-8.2391768464, -5.5988467224))
                Line((-8.3373943941, -5.5465991481), (-8.2979553725, -5.5179450217))
            make_face()
            # Profile area: 0.0050416728, perimeter: 0.3025430889
            with BuildLine():
                Line((-8.3788570732, -5.5767235478), (-8.3373943941, -5.5465991481))
                Line((-8.3200785471, -5.6576252485), (-8.3788570732, -5.5767235478))
                Line((-8.278615874, -5.6275008532), (-8.3200785471, -5.6576252485))
                CenterArc((-7.5, -5), 1, -146.8659882996, 5.7319680507)
            make_face()
            # Profile area: 0.0049583275, perimeter: 0.2975403473
            with BuildLine():
                CenterArc((-7.5, -5), 1, -161.2659882996, 5.7319680507)
                Line((-8.3648813704, -5.3962070448), (-8.4102073409, -5.4141528661))
                Line((-8.4016938262, -5.3032293949), (-8.3648813704, -5.3962070448))
                Line((-8.4470197898, -5.3211752134), (-8.4016938262, -5.3032293949))
            make_face()
            # Profile area: 0.0050416728, perimeter: 0.3025430889
            with BuildLine():
                Line((-8.4946714762, -5.3400418507), (-8.4470197898, -5.3211752134))
                Line((-8.4578590203, -5.4330195007), (-8.4946714762, -5.3400418507))
                Line((-8.4102073409, -5.4141528661), (-8.4578590203, -5.4330195007))
                CenterArc((-7.5, -5), 1, -161.2659882996, 5.7319680507)
            make_face()
            # Profile area: 0.0050416728, perimeter: 0.3025430889
            with BuildLine():
                Line((-8.5479870121, -5.0819940735), (-8.4971404492, -5.0755706588))
                Line((-8.5354536886, -5.1812055451), (-8.5479870121, -5.0819940735))
                Line((-8.4846071331, -5.1747821313), (-8.5354536886, -5.1812055451))
                CenterArc((-7.5, -5), 1, -175.6659882996, 5.7319680507)
            make_face()
            # Profile area: 0.0049583275, perimeter: 0.2975403473
            with BuildLine():
                CenterArc((-7.5, -5), 1, -175.6659882996, 5.7319680507)
                Line((-8.436242217, -5.1686722215), (-8.4846071331, -5.1747821313))
                Line((-8.4487755405, -5.0694607499), (-8.436242217, -5.1686722215))
                Line((-8.4971404492, -5.0755706588), (-8.4487755405, -5.0694607499))
            make_face()
            # Profile area: 0.0050416728, perimeter: 0.3025430889
            with BuildLine():
                Line((-8.5354536699, -4.8187943071), (-8.484607107, -4.8252177218))
                Line((-8.5479869935, -4.9180057787), (-8.5354536699, -4.8187943071))
                Line((-8.497140438, -4.9244291924), (-8.5479869935, -4.9180057787))
                CenterArc((-7.5, -5), 1, 169.9340117004, 5.7319680507)
            make_face()
            # Profile area: 0.0049583275, perimeter: 0.2975403473
            with BuildLine():
                CenterArc((-7.5, -5), 1, 169.9340117004, 5.7319680507)
                Line((-8.4487755218, -4.9305391022), (-8.497140438, -4.9244291924))
                Line((-8.4362421983, -4.8313276306), (-8.4487755218, -4.9305391022))
                Line((-8.484607107, -4.8252177218), (-8.4362421983, -4.8313276306))
            make_face()
            # Profile area: 0.0049583275, perimeter: 0.2975403473
            with BuildLine():
                CenterArc((-7.5, -5), 1, 155.5340117004, 5.7319680507)
                Line((-8.4016937713, -4.6967704666), (-8.4470197419, -4.6788246453))
                Line((-8.3648813155, -4.6037928166), (-8.4016937713, -4.6967704666))
                Line((-8.4102072791, -4.5858469981), (-8.3648813155, -4.6037928166))
            make_face()
            # Profile area: 0.0050416728, perimeter: 0.3025430889
            with BuildLine():
                Line((-8.4578589655, -4.5669803608), (-8.4102072791, -4.5858469981))
                Line((-8.4946714213, -4.6599580108), (-8.4578589655, -4.5669803608))
                Line((-8.4470197419, -4.6788246453), (-8.4946714213, -4.6599580108))
                CenterArc((-7.5, -5), 1, 155.5340117004, 5.7319680507)
            make_face()
            # Profile area: 0.0050416728, perimeter: 0.3025430889
            with BuildLine():
                Line((-7.9018267945, -4.0286426853), (-7.8800053121, -4.0750156959))
                Line((-7.9923095011, -4.071220615), (-7.9018267945, -4.0286426853))
                Line((-7.9704880218, -4.117593619), (-7.9923095011, -4.071220615))
                CenterArc((-7.5, -5), 1, 112.3340117004, 5.7319680507)
            make_face()
            # Profile area: 0.0049583275, perimeter: 0.2975403473
            with BuildLine():
                CenterArc((-7.5, -5), 1, 112.3340117004, 5.7319680507)
                Line((-7.9497315713, -4.1617033216), (-7.9704880218, -4.117593619))
                Line((-7.8592488647, -4.1191253919), (-7.9497315713, -4.1617033216))
                Line((-7.8800053121, -4.0750156959), (-7.8592488647, -4.1191253919))
            make_face()
            # Profile area: 0.0049583275, perimeter: 0.2975403473
            with BuildLine():
                CenterArc((-7.5, -5), 1, 126.7340117004, 5.7319680507)
                Line((-8.1440783334, -4.299883647), (-8.1751523188, -4.2623216511))
                Line((-8.0670270079, -4.2361412471), (-8.1440783334, -4.299883647))
                Line((-8.0981009886, -4.1985792569), (-8.0670270079, -4.2361412471))
            make_face()
            # Profile area: 0.0050416728, perimeter: 0.3025430889
            with BuildLine():
                Line((-8.1307694079, -4.1590899217), (-8.0981009886, -4.1985792569))
                Line((-8.2078207333, -4.2228323216), (-8.1307694079, -4.1590899217))
                Line((-8.1751523188, -4.2623216511), (-8.2078207333, -4.2228323216))
                CenterArc((-7.5, -5), 1, 126.7340117004, 5.7319680507)
            make_face()
            # Profile area: 0.0049583275, perimeter: 0.2975403473
            with BuildLine():
                CenterArc((-7.5, -5), 1, 141.1340117004, 5.7319680507)
                Line((-8.297955285, -4.4820548577), (-8.3373943125, -4.4534007269))
                Line((-8.2391767588, -4.4011531571), (-8.297955285, -4.4820548577))
                Line((-8.2786157804, -4.3724990307), (-8.2391767588, -4.4011531571))
            make_face()
            # Profile area: 0.0050416728, perimeter: 0.3025430889
            with BuildLine():
                Line((-8.3200784595, -4.342374631), (-8.2786157804, -4.3724990307))
                Line((-8.3788569856, -4.4232763316), (-8.3200784595, -4.342374631))
                Line((-8.3373943125, -4.4534007269), (-8.3788569856, -4.4232763316))
                CenterArc((-7.5, -5), 1, 141.1340117004, 5.7319680507)
            make_face()
            # Profile area: 0.0050416728, perimeter: 0.3025430889
            with BuildLine():
                Line((-7.6476359259, -3.9592294013), (-7.6380325042, -4.0095723006))
                Line((-7.7458646524, -3.9779675331), (-7.6476359259, -3.9592294013))
                Line((-7.7362612321, -4.028310425), (-7.7458646524, -3.9779675331))
                CenterArc((-7.5, -5), 1, 97.9340117004, 5.7319680507)
            make_face()
            # Profile area: 0.0049583275, perimeter: 0.2975403473
            with BuildLine():
                CenterArc((-7.5, -5), 1, 97.9340117004, 5.7319680507)
                Line((-7.7271265206, -4.0761962596), (-7.7362612321, -4.028310425))
                Line((-7.6288977941, -4.0574581279), (-7.7271265206, -4.0761962596))
                Line((-7.6380325042, -4.0095723006), (-7.6288977941, -4.0574581279))
            make_face()
            # Profile area: 0.0050416728, perimeter: 0.3025430889
            with BuildLine():
                Line((-7.384168549, -3.9552115618), (-7.3873866064, -4.0063611201))
                Line((-7.4839712233, -3.9489325097), (-7.384168549, -3.9552115618))
                Line((-7.4871892803, -4.0000820606), (-7.4839712233, -3.9489325097))
                CenterArc((-7.5, -5), 1, 83.5340117004, 5.7319680507)
            make_face()
            # Profile area: 0.0049583275, perimeter: 0.2975403473
            with BuildLine():
                CenterArc((-7.5, -5), 1, 83.5340117004, 5.7319680507)
                Line((-7.4902502754, -4.0487351841), (-7.4871892803, -4.0000820606))
                Line((-7.3904476011, -4.0550142361), (-7.4902502754, -4.0487351841))
                Line((-7.3873866064, -4.0063611201), (-7.3904476011, -4.0550142361))
            make_face()
            # Profile area: 0.0050416728, perimeter: 0.3025430889
            with BuildLine():
                Line((-7.1279792882, -4.0168416223), (-7.1438166224, -4.0655839248))
                Line((-7.2230849413, -3.9859399224), (-7.1279792882, -4.0168416223))
                Line((-7.2389222731, -4.0346822179), (-7.2230849413, -3.9859399224))
                CenterArc((-7.5, -5), 1, 69.1340117004, 5.7319680507)
            make_face()
            # Profile area: 0.0049583275, perimeter: 0.2975403473
            with BuildLine():
                CenterArc((-7.5, -5), 1, 69.1340117004, 5.7319680507)
                Line((-7.2539866412, -4.0810455754), (-7.2389222731, -4.0346822179))
                Line((-7.1588809881, -4.1119472753), (-7.2539866412, -4.0810455754))
                Line((-7.1438166224, -4.0655839248), (-7.1588809881, -4.1119472753))
            make_face()
            # Profile area: 0.0050416728, perimeter: 0.3025430889
            with BuildLine():
                Line((-6.7003556045, -4.3176740908), (-6.7377157495, -4.3527576022))
                Line((-6.7688103161, -4.244777227), (-6.7003556045, -4.3176740908))
                Line((-6.8061704557, -4.2798607333), (-6.7688103161, -4.244777227))
                CenterArc((-7.5, -5), 1, 40.3340117004, 5.7319680507)
            make_face()
            # Profile area: 0.0049583275, perimeter: 0.2975403473
            with BuildLine():
                CenterArc((-7.5, -5), 1, 40.3340117004, 5.7319680507)
                Line((-6.8417071799, -4.3132319386), (-6.8061704557, -4.2798607333))
                Line((-6.7732524683, -4.3861288024), (-6.8417071799, -4.3132319386))
                Line((-6.7377157495, -4.3527576022), (-6.7732524683, -4.3861288024))
            make_face()
            # Profile area: 0.0050416728, perimeter: 0.3025430889
            with BuildLine():
                Line((-6.895165457, -4.1402471394), (-6.9226269499, -4.1835195281))
                Line((-6.9795982508, -4.0866644591), (-6.895165457, -4.1402471394))
                Line((-7.0070597397, -4.1299368415), (-6.9795982508, -4.0866644591))
                CenterArc((-7.5, -5), 1, 54.7340117004, 5.7319680507)
            make_face()
            # Profile area: 0.0049583275, perimeter: 0.2975403473
            with BuildLine():
                CenterArc((-7.5, -5), 1, 54.7340117004, 5.7319680507)
                Line((-7.0331809311, -4.171097253), (-7.0070597397, -4.1299368415))
                Line((-6.9487481373, -4.2246799333), (-7.0331809311, -4.171097253))
                Line((-6.9226269499, -4.1835195281), (-6.9487481373, -4.2246799333))
            make_face()
        # OneSide extrude, distance=-0.25
        extrude(amount=-0.25, mode=Mode.SUBTRACT)

        # Sketch2 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.7, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0049583275, perimeter: 0.2975403473
            with BuildLine():
                Line((7.7362613771, -5.9716895398), (7.727126667, -5.9238037125))
                Line((7.727126667, -5.9238037125), (7.6288979405, -5.9425418442))
                Line((7.6288979405, -5.9425418442), (7.638032652, -5.9904276788))
                CenterArc((7.5, -5), 1, -82.0659797511, 5.7319680507)
            make_face()
            # Profile area: 0.0050416728, perimeter: 0.3025430889
            with BuildLine():
                CenterArc((7.5, -5), 1, -82.0659797511, 5.7319680507)
                Line((7.638032652, -5.9904276788), (7.6476360722, -6.0407705708))
                Line((7.6476360722, -6.0407705708), (7.7458647988, -6.022032439))
                Line((7.7458647988, -6.022032439), (7.7362613771, -5.9716895398))
            make_face()
        # OneSide extrude, distance=-0.25
        extrude(amount=-0.25, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a rectangular frame or bezel with a parallelogram shape, featuring a hollow center opening and dark outer walls with blue-highlighted edges, appearing to be a mounting frame or window assembly component.
def model_40417_b8d98f73_0016():
    """Model: Component23"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 80, perimeter: 48
            with BuildLine():
                Line((2, -10), (-2, -10))
                Line((2, 10), (2, -10))
                Line((-2, 10), (2, 10))
                Line((-2, -10), (-2, 10))
            make_face()
        # OneSide extrude, distance=35
        extrude(amount=35)

        # Sketch2 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -2), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 594, perimeter: 102
            with BuildLine():
                Line((-34, 9), (-1, 9))
                Line((-34, -9), (-34, 9))
                Line((-1, -9), (-34, -9))
                Line((-1, 9), (-1, -9))
            make_face()
        # OneSide extrude, distance=-4
        extrude(amount=-4, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -2), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 646, perimeter: 106
            with BuildLine():
                Line((-34.5, 9.5), (-0.5, 9.5))
                Line((-34.5, -9.5), (-34.5, 9.5))
                Line((-0.5, -9.5), (-34.5, -9.5))
                Line((-0.5, 9.5), (-0.5, -9.5))
            make_face()
        # OneSide extrude, distance=-3.5
        extrude(amount=-3.5, mode=Mode.SUBTRACT)
    return part.part


# Description: A flat rectangular plate with a blue anodized finish featuring three cylindrical holes or bosses protruding from its right edge.
def model_40623_278320ef_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 13 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 3.6992253496, perimeter: 49.3230046614
            with BuildLine():
                CenterArc((0, 4.6188021535), 4, -120.0000000022, 60.0000000026)
                CenterArc((0, 4.6188021535), 4, -59.9999999996, 299.9999999974)
            make_face()
            with BuildLine():
                CenterArc((0, 4.6188021535), 3.85, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 3.6992253496, perimeter: 49.3230046309
            with BuildLine():
                CenterArc((4, -2.3094010768), 4, 119.9999999996, 60.0000000004)
                CenterArc((4, -2.3094010768), 4, -179.9999995641, 299.9999995637)
            make_face()
            with BuildLine():
                CenterArc((4, -2.3094010768), 3.85, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 3.6992253496, perimeter: 49.3230046614
            with BuildLine():
                CenterArc((-4, -2.3094010768), 4, 60.0000000022, 299.999999562)
                CenterArc((-4, -2.3094010768), 4, -0.0000004359, 60.000000438)
            make_face()
            with BuildLine():
                CenterArc((-4, -2.3094010768), 3.85, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-10
        extrude(amount=-10)

        # Sketch2 -> Extrude2 (NewBody)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -10), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 574.7345175426, perimeter: 125.1327412287
            with BuildLine():
                Line((12.5, -12.5), (-12.5, -12.5))
                Line((12.5, 12.5), (12.5, -12.5))
                Line((-12.5, 12.5), (12.5, 12.5))
                Line((-12.5, -12.5), (-12.5, 12.5))
            make_face()
            with BuildLine():
                CenterArc((0, 4.6188021535), 4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 3.6992253496, perimeter: 49.3230046614
            with BuildLine():
                CenterArc((0, 4.6188021535), 4, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 4.6188021535), 3.85, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 46.5662571078, perimeter: 24.1902634326
            with Locations((0, 4.6188021535)):
                Circle(3.85)
        # OneSide extrude, distance=0.6
        extrude(amount=0.6)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 12 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -10.6), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            with Locations((-10, 10)):
                Circle(0.3)
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            with Locations((10, 10)):
                Circle(0.3)
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            with Locations((-10, -10)):
                Circle(0.3)
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            with Locations((10, -10)):
                Circle(0.3)
        # OneSide extrude, distance=-1.27
        extrude(amount=-1.27, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical connector or coupling component with a stepped bore design, featuring two different diameter sections and mesh-patterned surfaces indicating internal threading or helical features.
def model_40782_3383cd58_0009():
    """Model: Srubadociskajaca_nakretka v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.5393804003, perimeter: 4.398229715
            Circle(0.7)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.6361725124, perimeter: 2.8274333882
            Circle(0.45)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            Circle(0.25)
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a complex injection-molded or cast connector/bracket assembly featuring an angular, asymmetrical shape with multiple internal cavities, mounting bosses, and a ribbed structure designed for structural rigidity while minimizing weight.
def model_40800_7fa2d7a5_0000():
    """Model: Enganche 1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 17 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.5828318769, perimeter: 10.4283184354
            with BuildLine():
                CenterArc((-1.8, -8.8), 0.2, 180, 90)
                Line((-1.8, -9), (0, -9))
                Line((0, -9), (0, -6.5))
                Line((0, -6.5), (-1.8, -6.5))
                CenterArc((-1.8, -6.7), 0.2, 90, 90)
                Line((-2, -6.7), (-1.6000000238, -6.7))
                Line((-1.6000000238, -6.7), (-1.6000000238, -7.2))
                Line((-1.6000000238, -7.2), (-2, -7.2))
                Line((-2, -7.2), (-2, -8.3))
                Line((-1.6000000238, -8.3), (-2, -8.3))
                Line((-1.6000000238, -8.8), (-1.6000000238, -8.3))
                Line((-2, -8.8), (-1.6000000238, -8.8))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 15 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.0000000129, 0, -0.0000002135), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.6514159462, perimeter: 3.2283185814
            with BuildLine():
                CenterArc((-1.2000000194, 7.3000001073), 0.1, 180, 90)
                Line((-0.8000000104, 7.2000001073), (-1.2000000194, 7.2000001073))
                CenterArc((-0.8000000104, 7.3000001073), 0.1, -90, 90)
                Line((-0.7000000104, 8.2000001237), (-0.7000000104, 7.3000001073))
                CenterArc((-0.8000000104, 8.2000001237), 0.1, 0, 90)
                Line((-1.2000000194, 8.3000001237), (-0.8000000104, 8.3000001237))
                CenterArc((-1.2000000194, 8.2000001237), 0.1, 90, 90)
                Line((-1.3000000194, 7.3000001073), (-1.3000000194, 8.2000001237))
            make_face()
        # OneSide extrude, distance=-0.1
        extrude(amount=-0.1, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.0000000129, 0.1, -0.0000002135), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.12322551, perimeter: 1.610800053
            with BuildLine():
                Line((-0.7000000104, 7.6949493427), (-0.7000000104, 7.4949493427))
                Line((-1.3000000194, 7.7000001147), (-0.7000000104, 7.6949493427))
                Line((-1.3000000194, 7.7000001147), (-1.3000000194, 7.4892484209))
                Line((-0.7000000104, 7.4949493427), (-1.3000000194, 7.4892484209))
            make_face()
        # OneSide extrude, distance=-0.3
        extrude(amount=-0.3, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a curved support bracket or clamp with a dark gray/black finish, featuring a central ribbed or textured section flanked by two rounded cylindrical flanges on either end, designed to grip or hold an object securely.
def model_40815_80519d37_0000():
    """Model: Soft Jaws From 2013_P2"""
    with BuildPart() as part:
        # CAD_Outline -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 20 constraints, 15 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.4412168396, perimeter: 4.4620169558
            with BuildLine():
                CenterArc((2.2, -3.6), 0.75, 50.6891801901, 144.4871408148)
                CenterArc((9.9527350028, 0.971115835), 8.3, -154.2113889137, 2.9505128129)
                CenterArc((2.2, -3.6), 1, 73.7773149089, 98.3108713771)
                CenterArc((-5.1414845805, -8.8060161501), 8.3, 37.1263772958, 2.9505128129)
            make_face()
            # Profile area: 0.9332299464, perimeter: 8.2432299503
            with BuildLine():
                CenterArc((-5.1414845805, -8.8060161501), 8.3, 37.1263772958, 2.9505128129)
                CenterArc((2.2, -3.6), 1, 172.088186286, 43.2531471191)
                CenterArc((2.2, -3.6), 1, -144.6586665949, 175.1828343848)
                CenterArc((2.2, -3.6), 1, 30.5241677899, 43.2531471191)
                CenterArc((9.9527350028, 0.971115835), 8.3, -154.2113889137, 2.9505128129)
                CenterArc((2.2, -3.6), 0.75, -164.8236789951, 215.5128591852)
            make_face()
            # Profile area: 5.41917285, perimeter: 21.9759397348
            with BuildLine():
                CenterArc((0, 0), 2, -23.0550062582, 28.6278729553)
                CenterArc((0, 0), 2, 5.5728666971, 113.4864143709)
                CenterArc((0, 0), 2, 119.059281068, 28.6278729553)
                CenterArc((0, 0), 2, 147.6871540234, 75.4454471499)
                CenterArc((-5.1414845805, -8.8060161501), 8.3, 55.7763154358, 7.8894372519)
                CenterArc((0, 0), 2, -103.6905330497, 80.6355267915)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0786142938, perimeter: 2.3009733329
            with BuildLine():
                CenterArc((-5.1414845805, -8.8060161501), 8.3, 55.7763154358, 7.8894372519)
                CenterArc((0, 0), 2, -136.8673988267, 33.176865777)
            make_face()
            # Profile area: 0.3247373054, perimeter: 3.5301806822
            with BuildLine():
                CenterArc((-7, 0), 1, -34.8294308247, 67.8021367076)
                CenterArc((-4.8571428571, 8.741176309), 8.3, -101.9891031073, 2.9505128129)
                CenterArc((-7, 0), 0.75, -57.9175655436, 113.9784061453)
                CenterArc((-5.1414845805, -8.8060161501), 8.3, 97.1818653527, 2.9505128129)
            make_face()
            # Profile area: 1.0497094806, perimeter: 9.1750662238
            with BuildLine():
                CenterArc((-5.1414845805, -8.8060161501), 8.3, 97.1818653527, 2.9505128129)
                CenterArc((-7, 0), 0.75, 56.0608406018, 246.0215938547)
                CenterArc((-4.8571428571, 8.741176309), 8.3, -101.9891031073, 2.9505128129)
                CenterArc((-7, 0), 1, 32.9727058829, 43.2531471191)
                CenterArc((-7, 0), 1, 76.225853002, 205.6915690543)
                CenterArc((-7, 0), 1, -78.0825779438, 43.2531471191)
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2)

        # CAD_Outline -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 20 constraints, 15 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.4806729928, perimeter: 19.0931637484
            with BuildLine():
                CenterArc((-5.1414845805, -8.8060161501), 8.3, 40.0768901086, 15.6994253272)
                CenterArc((0, 0), 2, -136.8673988267, 33.176865777)
                CenterArc((-5.1414845805, -8.8060161501), 8.3, 63.6657526877, 33.5161126649)
                CenterArc((-7, 0), 1, -78.0825779438, 43.2531471191)
                CenterArc((-5.1414845805, -8.8060161501), 8, 35.3413334051, 66.5760886512)
                CenterArc((2.2, -3.6), 1, 172.088186286, 43.2531471191)
            make_face()
            # Profile area: 0.7302006993, perimeter: 7.2061903612
            with BuildLine():
                CenterArc((9.9527350028, 0.971115835), 8, -174.4271333029, 24.9513010927)
                CenterArc((0, 0), 2, -23.0550062582, 28.6278729553)
                CenterArc((9.9527350028, 0.971115835), 8.3, -167.7975325634, 13.5861436497)
                CenterArc((2.2, -3.6), 1, 30.5241677899, 43.2531471191)
            make_face()
            # Profile area: 1.493290072, perimeter: 12.2934528462
            with BuildLine():
                CenterArc((-7, 0), 1, 32.9727058829, 43.2531471191)
                CenterArc((-4.8571428571, 8.741176309), 8.3, -99.0385902945, 31.468270623)
                CenterArc((0, 0), 2, 119.059281068, 28.6278729553)
                CenterArc((-4.8571428571, 8.741176309), 8, -103.774146998, 42.8334280661)
            make_face()
        # OneSide extrude, distance=1.2
        extrude(amount=1.2, mode=Mode.ADD)

        # CAD_Outline -> Extrude3 (Join)
        # Sketch on XZ construction plane
        # Sketch has 20 constraints, 15 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.7765310134, perimeter: 8.7729349655
            with BuildLine():
                CenterArc((2.2, -3.6), 1, 73.7773149089, 98.3108713771)
                CenterArc((9.9527350028, 0.971115835), 8.3, -167.7975325634, 13.5861436497)
                CenterArc((0, 0), 2, -103.6905330497, 80.6355267915)
                CenterArc((-5.1414845805, -8.8060161501), 8.3, 40.0768901086, 15.6994253272)
            make_face()
        # OneSide extrude, distance=0.3
        extrude(amount=0.3, mode=Mode.ADD)

        # CAD_SecondPocketProjection -> Extrude11 (Join)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 1.2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 5.253305697, perimeter: 13.2307024835
            with BuildLine():
                CenterArc((7, 0), 1, 145.1705691753, 67.8021367076)
                CenterArc((5.1414845805, 8.8060161501), 8.3, -116.3342473123, 33.5161126649)
                CenterArc((0, 0), 2, -32.3128459766, 75.4454471499)
                CenterArc((4.8571428571, -8.741176309), 8.3, 80.9614097055, 31.468270623)
            make_face()
        # OneSide extrude, distance=-0.3
        extrude(amount=-0.3, mode=Mode.ADD)
    return part.part


# Description: This is a rectangular box or enclosure with a hinged or removable top lid featuring two parallel slot openings or vents on the upper surface, designed for ventilation or access to internal components.
def model_40999_cad6be09_0004():
    """Model: Emergency brake"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 48.3870209214, perimeter: 27.9400066352
            with BuildLine():
                Line((121.9199981689, 68.57999897), (121.9199981689, 62.2299990845))
                Line((121.9199981689, 62.2299990845), (129.5399990678, 62.2299990845))
                Line((129.5400041342, 68.57999897), (129.5399990678, 62.2299990845))
                Line((121.9199981689, 68.57999897), (129.5400041342, 68.57999897))
            make_face()
        # OneSide extrude, distance=7.62
        extrude(amount=7.62)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(7.62, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 6.4516004118, perimeter: 10.1600003242
            with BuildLine():
                Line((127.0000040531, 66.0400021076), (124.4600039721, 66.0400021076))
                Line((124.4600039721, 66.0400021076), (124.4600039721, 63.5000020266))
                Line((124.4600039721, 63.5000020266), (127.0000040531, 63.5000020266))
                Line((127.0000040531, 63.5000020266), (127.0000040531, 66.0400021076))
            make_face()
        # OneSide extrude, distance=-2.54
        extrude(amount=-2.54, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 8 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 68.57999897, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 7.7419204942, perimeter: 13.2080004215
            with BuildLine():
                Line((-1.0160000324, -123.4440039396), (-2.5400000811, -123.4440039396))
                Line((-2.5400000811, -123.4440039396), (-2.5400000811, -128.5240041018))
                Line((-2.5400000811, -128.5240041018), (-1.0160000324, -128.5240041018))
                Line((-1.0160000324, -128.5240041018), (-1.0160000324, -123.4440039396))
            make_face()
            # Profile area: 7.7419204942, perimeter: 13.2080004215
            with BuildLine():
                Line((-6.3500002027, -124.4600039721), (-6.3500002027, -123.4440039396))
                Line((-6.3500002027, -128.5240041018), (-6.3500002027, -124.4600039721))
                Line((-4.826000154, -128.5240041018), (-6.3500002027, -128.5240041018))
                Line((-4.826000154, -123.4440039396), (-4.826000154, -128.5240041018))
                Line((-6.3500002027, -123.4440039396), (-4.826000154, -123.4440039396))
            make_face()
        # OneSide extrude, distance=-0.508
        extrude(amount=-0.508, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical duct or manifold assembly featuring a central tubular body with two large circular mesh-covered openings or flanges on either end, designed to direct or filter airflow between connected components.
def model_41031_57b1ef09_0013():
    """Model: Handle Separator Front R"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 27 constraints, 11 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.7186147673, perimeter: 8.6566370614
            with BuildLine():
                CenterArc((0.45, -1.9), 0.1, 180, 90)
                Line((0.95, -2), (0.45, -2))
                CenterArc((0.95, -1.9), 0.1, -90, 90)
                Line((1.05, -0.8), (1.05, -1.9))
                CenterArc((1.15, -0.8), 0.1, 90, 90)
                Line((1.4, -0.7), (1.15, -0.7))
                Line((1.4, 0), (1.4, -0.7))
                Line((0, 0), (1.4, 0))
                Line((0, -0.7000876968), (0, 0))
                Line((0.25, -0.7000876968), (0, -0.7000876968))
                CenterArc((0.25, -0.8000876968), 0.1, 0, 90)
                Line((0.35, -1.9), (0.35, -0.8000876968))
            make_face()
            with BuildLine():
                Line((0.8, -1.4), (0.8, -0.7))
                CenterArc((0.7, -1.4), 0.1, -180, 180)
                Line((0.6, -0.7), (0.6, -1.4))
                CenterArc((0.7, -0.7), 0.1, 0, 180)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)

        # Sketch3 -> Extrude2 (Join)
        # Sketch on YZ construction plane
        # Sketch has 11 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 2.3807368194, perimeter: 6.6546262199
            with BuildLine():
                CenterArc((-1.8, 0.775), 0.6, 32.7971682958, 237.2028317042)
                Line((-1.8, 0.175), (-0.7, 0.175))
                Line((-0.7, 0.175), (-0.7, 0.1))
                Line((-0.7, 0.1), (0, 0.1))
                Line((0, 0.1), (0, 1.1))
                Line((0, 1.1), (-1.295643975, 1.1))
            make_face()
        # OneSide extrude, distance=1.4
        extrude(amount=1.4, mode=Mode.ADD)

        # Sketch4 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))) as sk:
            # Profile area: 2.9046079891, perimeter: 7.2410133151
            with BuildLine():
                Line((-1.3, 0), (-0.1, 0))
                Line((-0.1, 0), (-0.1, 2.4205066576))
                Line((-0.1, 2.4205066576), (-1.3, 2.4205066576))
                Line((-1.3, 2.4205066576), (-1.3, 0))
            make_face()
        # TwoSides extrude, along=0.3, against=-1
        extrude(amount=0.3, mode=Mode.SUBTRACT)
        extrude(sk.sketch, amount=-1, mode=Mode.SUBTRACT)
    return part.part


# Description: A rectangular box-shaped housing with multiple circular holes along its sides, an open top with a hinged or removable lid, and internal triangular bracing or support structures visible through the openings.
def model_41113_e7d93a39_0000():
    """Model: Component12"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 30.25, perimeter: 22
            with BuildLine():
                Line((-7.75, -2.25), (-2.25, -2.25))
                Line((-7.75, -7.75), (-7.75, -2.25))
                Line((-2.25, -7.75), (-7.75, -7.75))
                Line((-2.25, -2.25), (-2.25, -7.75))
            make_face()
        # OneSide extrude, distance=9
        extrude(amount=9)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 9, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 25, perimeter: 20
            with BuildLine():
                Line((7.5, 2.5), (2.5, 2.5))
                Line((7.5, 7.5), (7.5, 2.5))
                Line((2.5, 7.5), (7.5, 7.5))
                Line((2.5, 2.5), (2.5, 7.5))
            make_face()
        # OneSide extrude, distance=-9
        extrude(amount=-9, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 7.75), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1.7671458676, perimeter: 4.7123889804
            with Locations((-5, 8)):
                Circle(0.75)
            # Profile area: 1.7671458676, perimeter: 4.7123889804
            with Locations((-5, 5)):
                Circle(0.75)
            # Profile area: 1.7671458676, perimeter: 4.7123889804
            with Locations((-5, 2)):
                Circle(0.75)
        # OneSide extrude, distance=-6
        extrude(amount=-6, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a scooter kickstand featuring a T-shaped design with a vertical dark gray support column mounted on a horizontal blue platform base with integrated grip texture.
def model_41125_711db4bf_0010():
    """Model: rotor_assembly_try3 v4"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 17 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.7931435995, perimeter: 9.3762893392
            with BuildLine():
                Line((-1.1137772058, 0.2), (1.0862227942, 0.2000000001))
                CenterArc((-1.1017199595, 0.0000246568), 0.2003385013, 93.4503954596, 173.3420848129)
                Line((1.0853749998, -0.2), (-1.1129294083, -0.2000000001))
                CenterArc((1.0741655479, 0.0000246568), 0.2003385014, -86.7924793642, 173.3420839046)
            make_face()
            with BuildLine():
                Line((1.0724456047, 0.06), (0.3224456047, 0.06))
                CenterArc((1.0741655479, 0.0000246568), 0.06, -89.765001528, 181.4076512617)
                Line((0.3199883484, -0.0599748385), (1.074411637, -0.0599748386))
                CenterArc((0.3212160517, 0.0000125997), 0.06, 88.8257811613, 180.0017666986)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((-1.1000000164, 0.06), (-0.3500000164, 0.06))
                CenterArc((-0.3487704634, 0.0000125997), 0.06, -88.8275478598, 180.0017666986)
                Line((-0.34754276, -0.0599748386), (-1.1019660487, -0.0599748386))
                CenterArc((-1.1017199595, 0.0000246568), 0.06, 88.3573502663, 181.4076512617)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))) as sk:
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with BuildLine():
                CenterArc((0, 0), 0.2, 90, 180)
                CenterArc((0, 0), 0.2, -90, 180)
            make_face()
        # TwoSides extrude, along=1.65, against=-0.15
        extrude(amount=1.65, mode=Mode.ADD)
        extrude(sk.sketch, amount=-0.15, mode=Mode.ADD)

        # Sketch5 -> Extrude9 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -0.05, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            Circle(0.15)
        # OneSide extrude, distance=-0.6
        extrude(amount=-0.6, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a stepped cylindrical shaft or connector featuring a smaller diameter cylindrical body on the left transitioning to a larger diameter flanged or collar section on the right, with internal threaded or grooved features visible in the bore.
def model_41128_ee74f244_0011():
    """Model: 14-Clamp Plate Screw"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 2.8502295699, perimeter: 5.9847340051
            with Locations((14.892982826, 11.7922937909)):
                Circle(0.9525)
        # OneSide extrude, distance=0.635
        extrude(amount=0.635)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.635, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.1072248948, perimeter: 1.681247183
            with BuildLine():
                CenterArc((14.892982826, 11.7922937909), 0.9525, -94.7418624062, 9.4837248124)
                Line((14.814242826, 10.1600003242), (14.814242826, 10.8430539569))
                Line((14.971722826, 10.1600003242), (14.814242826, 10.1600003242))
                Line((14.971722826, 10.8430539569), (14.971722826, 10.1600003242))
            make_face()
            # Profile area: 0.2996573607, perimeter: 4.1122791713
            with BuildLine():
                Line((14.971722826, 12.7415336248), (14.971722826, 10.8430539569))
                CenterArc((14.892982826, 11.7922937909), 0.9525, 85.2581375938, 9.4837248124)
                Line((14.814242826, 10.8430539569), (14.814242826, 12.7415336248))
                CenterArc((14.892982826, 11.7922937909), 0.9525, -94.7418624062, 9.4837248124)
            make_face()
            # Profile area: 0.0731167999, perimeter: 1.2480735111
            with BuildLine():
                Line((14.971722826, 13.2080004215), (14.971722826, 12.7415336248))
                Line((14.814242826, 13.2080004215), (14.971722826, 13.2080004215))
                Line((14.814242826, 12.7415336248), (14.814242826, 13.2080004215))
                CenterArc((14.892982826, 11.7922937909), 0.9525, 85.2581375938, 9.4837248124)
            make_face()
        # OneSide extrude, distance=-0.23622
        extrude(amount=-0.23622, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 1.2667686977, perimeter: 3.9898226701
            with Locations((-14.892982826, 11.7922937909)):
                Circle(0.635)
        # OneSide extrude, distance=2.54
        extrude(amount=2.54, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical spacer or standoff with a larger diameter flange on one end and a textured or knurled surface along the main barrel, designed for fastening or alignment purposes.
def model_41128_ee74f244_0012():
    """Model: 13-Sec Base Screw (3)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.9793260902, perimeter: 4.9872783376
            with Locations((11.4299998283, 6.3499999046)):
                Circle(0.79375)
        # OneSide extrude, distance=0.635
        extrude(amount=0.635)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.635), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0168632346, perimeter: 0.5346057356
            with BuildLine():
                CenterArc((11.4299998283, 6.3499999046), 0.79375, 84.3068952066, 11.3862095868)
                Line((11.5087398283, 7.2495278954), (11.5087398283, 7.1398347449))
                Line((11.3512598283, 7.2495278954), (11.5087398283, 7.2495278954))
                Line((11.3512598283, 7.1398347449), (11.3512598283, 7.2495278954))
            make_face()
            # Profile area: 0.2495888668, perimeter: 3.4748182301
            with BuildLine():
                Line((11.5087398283, 7.1398347449), (11.5087398283, 5.5601650644))
                CenterArc((11.4299998283, 6.3499999046), 0.79375, 84.3068952066, 11.3862095868)
                Line((11.3512598283, 5.5601650644), (11.3512598283, 7.1398347449))
                CenterArc((11.4299998283, 6.3499999046), 0.79375, -95.6931047934, 11.3862095868)
            make_face()
            # Profile area: 0.0129582019, perimeter: 0.4850117206
            with BuildLine():
                Line((11.5087398283, 5.5601650644), (11.5087398283, 5.4752689213))
                CenterArc((11.4299998283, 6.3499999046), 0.79375, -95.6931047934, 11.3862095868)
                Line((11.3512598283, 5.4752689213), (11.3512598283, 5.5601650644))
                Line((11.5087398283, 5.4752689213), (11.3512598283, 5.4752689213))
            make_face()
        # OneSide extrude, distance=-0.23622
        extrude(amount=-0.23622, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.9676542058, perimeter: 3.4871050136
            with Locations((-11.4299998283, 6.3499999046)):
                Circle(0.55499)
        # OneSide extrude, distance=2.54
        extrude(amount=2.54, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical shaft or axle with a radial flange, featuring a long smooth cylindrical body on the left and a larger diameter disk-like flange on the right, with internal geometric details visible in the cross-section rendering.
def model_41128_ee74f244_0013():
    """Model: 18-Jaw Plate Screw (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.4932493285, perimeter: 2.4896493461
            Circle(0.39624)
        # OneSide extrude, distance=0.15748
        extrude(amount=0.15748)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.15748, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0343123016, perimeter: 0.7623400416
            with BuildLine():
                Line((0.07874, 0.6115000397), (0.07874, 0.3883376752))
                Line((-0.07874, 0.6115000397), (0.07874, 0.6115000397))
                Line((-0.07874, 0.3883376752), (-0.07874, 0.6115000397))
                CenterArc((0, 0), 0.39624, 78.5380018254, 22.9239963492)
            make_face()
            # Profile area: 0.1239734493, perimeter: 1.870421326
            with BuildLine():
                Line((0.07874, 0.3883376752), (0.07874, -0.3883376752))
                CenterArc((0, 0), 0.39624, 78.5380018254, 22.9239963492)
                Line((-0.07874, -0.3883376752), (-0.07874, 0.3883376752))
                CenterArc((0, 0), 0.39624, -101.4619981746, 22.9239963492)
            make_face()
            # Profile area: 0.0500960517, perimeter: 0.9627940693
            with BuildLine():
                CenterArc((0, 0), 0.39624, -101.4619981746, 22.9239963492)
                Line((-0.07874, -0.7117270536), (-0.07874, -0.3883376752))
                Line((0.07874, -0.7117270536), (-0.07874, -0.7117270536))
                Line((0.07874, -0.3883376752), (0.07874, -0.7117270536))
            make_face()
        # OneSide extrude, distance=-0.0762
        extrude(amount=-0.0762, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.1829214, perimeter: 1.5161326146
            Circle(0.2413)
        # OneSide extrude, distance=1.27
        extrude(amount=1.27, mode=Mode.ADD)
    return part.part


# Description: This is a knurled handwheel or control knob with a cylindrical grip handle, featuring a large textured circular face with radial knurling patterns and an extending shaft or lever arm for manual operation.
def model_41142_1bf94ee2_0013():
    """Model: Knob v21"""
    with BuildPart() as part:
        # Sketch5 -> Extrude2 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 15 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.7756637061, perimeter: 3.2566370614
            with BuildLine():
                CenterArc((-0.75, -0.25), 0.2, 180, 90)
                Line((-0.25, -0.45), (-0.75, -0.45))
                CenterArc((-0.25, -0.25), 0.2, -90, 90)
                Line((-0.05, 0.25), (-0.05, -0.25))
                CenterArc((-0.25, 0.25), 0.2, 0, 90)
                Line((-0.75, 0.45), (-0.25, 0.45))
                CenterArc((-0.75, 0.25), 0.2, 90, 90)
                Line((-0.95, -0.25), (-0.95, 0.25))
            make_face()
        # OneSide extrude, distance=5.6
        extrude(amount=5.6)

        # Sketch1 -> Extrude3 (Cut)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 21.2371663383, perimeter: 16.3362817987
            Circle(2.6)
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.SUBTRACT)

        # Sketch1 -> Extrude4 (Join)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 21.2371663383, perimeter: 16.3362817987
            Circle(2.6)
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)
    return part.part


# Description: This is a rectangular housing or enclosure with a hexagonal or multi-faceted cross-section, featuring internal cavities and cutouts (visible as darker recessed areas), designed as a structural component or casing with complex internal geometry.
def model_41227_90e1c07c_0016():
    """Model: Handle Bar Block"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 258.064, perimeter: 71.12
            with BuildLine():
                Line((92.5864436057, 53.1116299718), (117.9864436057, 53.1116299718))
                Line((92.5864436057, 42.9516299718), (92.5864436057, 53.1116299718))
                Line((117.9864436057, 42.9516299718), (92.5864436057, 42.9516299718))
                Line((117.9864436057, 53.1116299718), (117.9864436057, 42.9516299718))
            make_face()
        # OneSide extrude, distance=10.16
        extrude(amount=10.16)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 11.5534372309, perimeter: 12.0492644636
            with Locations((-112.2714436057, 48.0316299718)):
                Circle(1.9177)
            # Profile area: 11.5534372309, perimeter: 12.0492644636
            with Locations((-98.3014436057, 48.0316299718)):
                Circle(1.9177)
        # OneSide extrude, distance=-5.08
        extrude(amount=-5.08, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 10.16), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 45.9082043137, perimeter: 24.0187324738
            with Locations((105.2864436057, 48.0316299718)):
                Circle(3.8227)
        # OneSide extrude, distance=-5.08
        extrude(amount=-5.08, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a tall, rectangular metal channel or duct component with a trapezoidal cross-section, featuring a large rectangular opening along its length, flanged edges, and mesh or perforated sections at the top and bottom ends.
def model_41229_16283ae1_0017():
    """Model: Side Panel v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 3 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 18, perimeter: 18
            with BuildLine():
                Line((3, 6), (3, 0))
                Line((0, 6), (3, 6))
                Line((0, 0), (0, 6))
                Line((3, 0), (0, 0))
            make_face()
        # OneSide extrude, distance=-3
        extrude(amount=-3)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 6, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 7.1974655488, perimeter: 10.7561234045
            with BuildLine():
                CenterArc((-0.0961538785, -2.9038461215), 2.9054376375, 91.8965189626, 86.2069620749)
                Line((-3, -2.8076922429), (-3, -3))
                Line((-3, -3), (0, -3))
                Line((0, -3), (0, 0))
                Line((0, 0), (-0.1923077571, 0))
            make_face()
        # OneSide extrude, distance=-6
        extrude(amount=-6, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 7.5, perimeter: 13
            with BuildLine():
                Line((2.5, 0.5), (1, 0.5))
                Line((2.5, 5.5), (2.5, 0.5))
                Line((1, 5.5), (2.5, 5.5))
                Line((1, 0.5), (1, 5.5))
            make_face()
        # OneSide extrude, distance=-0.1
        extrude(amount=-0.1, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a simple rounded rectangular bar or shaft with a uniform cylindrical profile and gently rounded ends, featuring no holes, slots, or additional features.
def model_41234_74275eb0_0000():
    """Model: Middle bar"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.2667686977, perimeter: 3.9898226701
            with Locations((0.27989582, 31.9102736074)):
                Circle(0.635)
        # OneSide extrude, distance=32.91078
        extrude(amount=32.91078)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(32.91078, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.1231863599, perimeter: 1.2441886726
            with Locations((0.27989582, 31.9102736074)):
                Circle(0.1980187774)
        # OneSide extrude, distance=0.635
        extrude(amount=0.635, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.3166921744, perimeter: 1.994911335
            with Locations((-0.27989582, 31.9102736074)):
                Circle(0.3175)
        # OneSide extrude, distance=0.635
        extrude(amount=0.635, mode=Mode.ADD)
    return part.part


# Description: A black, cylindrical handlebar grip with a gentle arc or curve, featuring textured ribbing along its length and rubber end caps for comfortable gripping on bicycles or similar equipment.
def model_41234_74275eb0_0001():
    """Model: Rocker"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 284.9880394809, perimeter: 134.1620827639
            with BuildLine():
                CenterArc((-54.8256245798, -9.492628307), 2.54, 48.0127875042, 182.5865518323)
                CenterArc((-28.6300903312, 56.1909904753), 73.1389088628, -112.3463759333, 48.7353486063)
                CenterArc((2.2841404925, -7.3485123149), 2.54, -51.1502501479, 210.0176496163)
                CenterArc((-27.9659746681, 54.5471618566), 67.0514640747, -112.0392283052, 46.6098132888)
            make_face()
        # OneSide extrude, distance=3.81
        extrude(amount=3.81)

        # Sketch6 -> Extrude2 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 5.067074791, perimeter: 7.9796453401
            with Locations((1.905, -2.9773799351)):
                Circle(1.27)
        # OneSide extrude, distance=-8.89
        extrude(amount=-8.89, mode=Mode.SUBTRACT)

        # Sketch7 -> Extrude3 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 5.067074791, perimeter: 7.9796453401
            with Locations((1.905, -28.0250408257)):
                Circle(1.27)
        # OneSide extrude, distance=-13.97
        extrude(amount=-13.97, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a flat rectangular panel or plate with a parallelogram shape, featuring a dark blue surface with a slightly beveled or rounded edge frame and what appears to be a recessed or slightly curved center area.
def model_41234_74275eb0_0002():
    """Model: Back"""
    with BuildPart() as part:
        # Sketch2 -> Extrude3 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 206.4512, perimeter: 60.96
            with BuildLine():
                Line((113.7259742664, 57.7614410096), (113.7259742664, 67.9214410096))
                Line((113.7259742664, 67.9214410096), (93.4059742664, 67.9214410096))
                Line((93.4059742664, 67.9214410096), (93.4059742664, 57.7614410096))
                Line((93.4059742664, 57.7614410096), (113.7259742664, 57.7614410096))
            make_face()
        # OneSide extrude, distance=0.635
        extrude(amount=0.635)

        # Sketch1 -> Extrude1 (Cut)
        # Sketch on XY construction plane
        # Sketch has 12 constraints, 15 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.3166921744, perimeter: 1.994911335
            with Locations((105.7450850788, 66.5640451374)):
                Circle(0.3175)
            # Profile area: 0.3166921744, perimeter: 1.994911335
            with Locations((101.4539020625, 66.6001054989)):
                Circle(0.3175)
            # Profile area: 0.3166921744, perimeter: 1.994911335
            with Locations((102.5110832221, 64.7329536563)):
                Circle(0.3175)
            # Profile area: 0.3166921744, perimeter: 1.994911335
            with Locations((104.6566747302, 64.7149234756)):
                Circle(0.3175)
            # Profile area: 0.3166921744, perimeter: 1.994911335
            with Locations((105.7138558897, 62.847771633)):
                Circle(0.3175)
            # Profile area: 0.3166921744, perimeter: 1.994911335
            with Locations((103.5682643816, 62.8658018138)):
                Circle(0.3175)
            # Profile area: 0.3166921744, perimeter: 1.994911335
            with Locations((101.4226728734, 62.8838319945)):
                Circle(0.3175)
            # Profile area: 0.3166921744, perimeter: 1.994911335
            with Locations((99.2770813653, 62.9018621752)):
                Circle(0.3175)
            # Profile area: 0.3166921744, perimeter: 1.994911335
            with Locations((107.8594473979, 62.8297414523)):
                Circle(0.3175)
            # Profile area: 0.3166921744, perimeter: 1.994911335
            with Locations((104.6254455411, 60.9986499712)):
                Circle(0.3175)
            # Profile area: 0.3166921744, perimeter: 1.994911335
            with Locations((102.479854033, 61.0166801519)):
                Circle(0.3175)
            # Profile area: 0.3166921744, perimeter: 1.994911335
            with Locations((105.6826267006, 59.1314981286)):
                Circle(0.3175)
            # Profile area: 0.3166921744, perimeter: 1.994911335
            with Locations((101.3914436843, 59.1675584901)):
                Circle(0.3175)
        # OneSide extrude, distance=0.635
        extrude(amount=0.635, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 12 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.635), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0791730436, perimeter: 0.9974556675
            with Locations((112.8369742664, 67.2864410096)):
                Circle(0.15875)
            # Profile area: 0.0791730436, perimeter: 0.9974556675
            with Locations((94.1552742664, 67.2864410096)):
                Circle(0.15875)
            # Profile area: 0.0791730436, perimeter: 0.9974556675
            with Locations((94.1552742664, 58.3202410096)):
                Circle(0.15875)
            # Profile area: 0.0791730436, perimeter: 0.9974556675
            with Locations((112.8369742664, 58.3202410096)):
                Circle(0.15875)
        # OneSide extrude, distance=-0.635
        extrude(amount=-0.635, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a rectangular bar or rod with rounded ends, featuring a long, flat horizontal profile with symmetrical chamfered or rounded corners at both extremities.
def model_41234_74275eb0_0005():
    """Model: Side Bar Support"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.2667686977, perimeter: 3.9898226701
            with Locations((21.7397227799, 0.2623224411)):
                Circle(0.635)
        # OneSide extrude, distance=21.23694
        extrude(amount=21.23694)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.3166921744, perimeter: 1.994911335
            with Locations((-21.7397227799, 0.2623224411)):
                Circle(0.3175)
        # OneSide extrude, distance=0.635
        extrude(amount=0.635, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(21.23694, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.3166921744, perimeter: 1.994911335
            with Locations((21.7397227799, 0.2623224411)):
                Circle(0.3175)
        # OneSide extrude, distance=0.635
        extrude(amount=0.635, mode=Mode.ADD)
    return part.part


# Description: This is a stylus or pen with a long, slender cylindrical shaft that tapers slightly toward both ends, featuring a pointed tip at one end and a textured grip section.
def model_41234_74275eb0_0012():
    """Model: Front Seat Support"""
    with BuildPart() as part:
        # Sketch1 -> Extrude2 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.2667686977, perimeter: 3.9898226701
            with Locations((-5.578007363, 1.3280969912)):
                Circle(0.635)
        # OneSide extrude, distance=33.02
        extrude(amount=33.02)

        # Sketch2 -> Extrude3 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.3166921744, perimeter: 1.994911335
            with Locations((-5.578007363, 1.3280969912)):
                Circle(0.3175)
        # OneSide extrude, distance=-1.27
        extrude(amount=-1.27)

        # Sketch3 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 33.02, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.3166921744, perimeter: 1.994911335
            with Locations((5.578007363, -1.3280969912)):
                Circle(0.3175)
        # OneSide extrude, distance=1.27
        extrude(amount=1.27, mode=Mode.ADD)
    return part.part


# Description: This is a stylus or pen with a long, tapered cylindrical shaft that gradually narrows from a thicker grip section at the top to a fine pointed tip at the bottom, designed for precision writing or digital input.
def model_41234_74275eb0_0014():
    """Model: Back Seat Support"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.2667686977, perimeter: 3.9898226701
            with Locations((-12.5177587374, 3.8453245795)):
                Circle(0.635)
        # OneSide extrude, distance=33.02
        extrude(amount=33.02)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 33.02), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.3166921744, perimeter: 1.994911335
            with Locations((-12.5177587374, 3.8453245795)):
                Circle(0.3175)
        # OneSide extrude, distance=1.27
        extrude(amount=1.27, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.3166921744, perimeter: 1.994911335
            with Locations((12.5177587374, 3.8453245795)):
                Circle(0.3175)
        # OneSide extrude, distance=1.27
        extrude(amount=1.27, mode=Mode.ADD)
    return part.part


# Description: This is a channel or trough-shaped bracket with a U-shaped cross-section, featuring two vertical flanges on the sides, a central web base, and a rectangular cutout or slot through the middle section, designed for mounting or alignment applications.
def model_41319_418c7ab8_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 11 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 6, perimeter: 10
            with BuildLine():
                Line((3.5, -1.5), (1.5, -1.5))
                Line((3.5, 1.5), (3.5, -1.5))
                Line((1.5, 1.5), (3.5, 1.5))
                Line((1.5, 1.5), (1.5, -1.5))
            make_face()
            # Profile area: 6, perimeter: 10
            with BuildLine():
                Line((-1.5, -1.5), (-1.5, 1.5))
                Line((-1.5, 1.5), (-3.5, 1.5))
                Line((-3.5, 1.5), (-3.5, -1.5))
                Line((-3.5, -1.5), (-1.5, -1.5))
            make_face()
            # Profile area: 3.5342917353, perimeter: 7.7123889804
            with BuildLine():
                CenterArc((-3.5, 0), 1.5, 90, 180)
                Line((-3.5, 1.5), (-3.5, -1.5))
            make_face()
            # Profile area: 3.5342917353, perimeter: 7.7123889804
            with BuildLine():
                Line((3.5, 1.5), (3.5, -1.5))
                CenterArc((3.5, 0), 1.5, -90, 180)
            make_face()
            # Profile area: 9, perimeter: 12
            with BuildLine():
                Line((-1.5, -1.5), (-1.5, 1.5))
                Line((1.5, -1.5), (-1.5, -1.5))
                Line((1.5, 1.5), (1.5, -1.5))
                Line((-1.5, 1.5), (1.5, 1.5))
            make_face()
        # OneSide extrude, distance=3
        extrude(amount=3)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 3, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.9087385212, perimeter: 7.853981634
            with Locations((-3.5, 0)):
                Circle(1.25)
            # Profile area: 4.9087385212, perimeter: 7.853981634
            with Locations((3.5, 0)):
                Circle(1.25)
        # OneSide extrude, distance=-1.5
        extrude(amount=-1.5, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 3, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 8.9817507883, perimeter: 11.9878458521
            with BuildLine():
                Line((-1.5386626638, -1.5), (-1.5386626638, 1.5))
                Line((0, -1.5), (-1.5386626638, -1.5))
                Line((1.449183188, -1.4999753793), (0, -1.5))
                Line((1.4613373362, 1.5), (1.449183188, -1.4999753793))
                Line((-1.5386626638, 1.5), (1.4613373362, 1.5))
            make_face()
        # OneSide extrude, distance=-2
        extrude(amount=-2, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a curved, elongated pod or duct component with a smooth, organic shape that tapers from a wider central body to narrower ends, featuring a small rectangular opening or slot at the upper end.
def model_41353_16ac5969_0003():
    """Model: leftFlap"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 8 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 117.2032714924, perimeter: 43.7506257582
            with BuildLine():
                Line((-4.6, -0.0354101926), (-4.6098263202, -2.5201095167))
                CenterArc((-4.6098263202, -5.0201095167), 2.5, 90, 134.4270040008)
                CenterArc((-8.1805405345, -8.5201095167), 2.5, -44.4270040008, 88.8540080016)
                CenterArc((-4.6098263202, -12.0201095167), 2.5, 135.5729959992, 132.542824396)
                CenterArc((-4.0481426335, -7.2962612919), 7.2511406115, -95.0944204707, 136.5049127864)
                Line((1.4, -0.0354101926), (1.3901399803, -2.5))
                Line((-4.6, -0.0354101926), (1.4, -0.0354101926))
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))) as sk:
            # Profile area: 0.1884955592, perimeter: 3.7699111843
            with BuildLine():
                CenterArc((-0.400000006, 0.200000003), 0.35, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-0.400000006, 0.200000003), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # TwoSides extrude, along=1.4, against=-4.6
        extrude(amount=1.4, mode=Mode.ADD)
        extrude(sk.sketch, amount=-4.6, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on XY construction plane
        # Sketch has 3 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 3.9549348334, perimeter: 8.0957878392
            with BuildLine():
                Line((-2.8, -0.3511419628), (-2.8, 1.3000000194))
                Line((-0.4, -0.3446370282), (-2.8, -0.3511419628))
                Line((-0.4, 0.5553629718), (-0.4, -0.3446370282))
                Line((-0.400000006, 1.3000000194), (-0.4, 0.5553629718))
                Line((-2.8, 1.3000000194), (-0.400000006, 1.3000000194))
            make_face()
        # Symmetric extrude, each_side=1
        extrude(amount=1, both=True, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a flat, parallelogram-shaped structural frame or panel with an internal ribbed reinforcement structure consisting of multiple parallel diagonal and cross-bracing members that provide lateral stiffening while maintaining a lightweight design.
def model_41353_16ac5969_0017():
    """Model: standBase"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 256, perimeter: 64
            with BuildLine():
                Line((-8, 8), (8, 8))
                Line((-8, -8), (-8, 8))
                Line((8, -8), (-8, -8))
                Line((8, 8), (8, -8))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 196, perimeter: 56
            with BuildLine():
                Line((7, -7), (-7, -7))
                Line((7, 7), (7, -7))
                Line((-7, 7), (7, 7))
                Line((-7, -7), (-7, 7))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            Circle(0.25)
        # OneSide extrude, distance=2
        extrude(amount=2, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical power adapter or connector featuring a large hollow barrel body with a blue textured top rim and a tapered cylindrical stem extending downward.
def model_41501_b627682a_0028():
    """Model: Axle No. 2 v10"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0314159275, perimeter: 0.6283185401
            Circle(0.1000000015)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0942477824, perimeter: 1.8849556202
            with BuildLine():
                CenterArc((0, 0), 0.200000003, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.1000000015, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0314159275, perimeter: 0.6283185401
            Circle(0.1000000015)
        # OneSide extrude, distance=0.4
        extrude(amount=0.4, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.9, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.6597344535, perimeter: 4.3982297338
            with BuildLine():
                CenterArc((0, 0), 0.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.200000003, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.1256637099, perimeter: 1.2566370802
            Circle(0.200000003)
        # OneSide extrude, distance=1.55
        extrude(amount=1.55, mode=Mode.ADD)
    return part.part


# Description: This is a flat, elongated rectangular bar or plate with a slightly tapered or beveled edge on the right end, featuring a simple geometric design with no holes or complex features.
def model_41593_d3d842f7_0005():
    """Model: 14:Foam Lining"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.8584073464, perimeter: 7.1415926536
            with BuildLine():
                Line((-2, 2), (0, 2))
                Line((-2, 0), (-2, 2))
                CenterArc((0, 0), 2, 90, 90)
            make_face()
        # OneSide extrude, distance=100
        extrude(amount=100)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2, perimeter: 6.8284271247
            with BuildLine():
                Line((0, -2), (2, 0))
                Line((0, 0), (2, 0))
                Line((0, -2), (0, 0))
            make_face()
        # OneSide extrude, distance=5
        extrude(amount=5, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2, perimeter: 6.8284271247
            with BuildLine():
                Line((-100, 2), (-100, 0))
                Line((-98, 0), (-100, 0))
                Line((-100, 2), (-98, 0))
            make_face()
        # OneSide extrude, distance=-4.2
        extrude(amount=-4.2, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a toroidal or donut-shaped component featuring a hollow center hole with a smooth curved outer surface and internal radial ribbing or spoke-like structural elements that provide reinforcement while maintaining a lightweight design.
def model_41599_f66b4e5b_0010():
    """Model: fan string insert v1"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0078539816, perimeter: 0.3141592654
            Circle(0.05)
        # OneSide extrude, distance=0.06
        extrude(amount=0.06)

        # Sketch3 -> Extrude2 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((0.5449999878, 0)):
                Circle(0.5)
        # Symmetric extrude, each_side=0.1
        extrude(amount=0.1, both=True, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.0004908739, perimeter: 0.0785398163
            Circle(0.0125)
        # OneSide extrude, distance=-0.01
        extrude(amount=-0.01, mode=Mode.SUBTRACT)
    return part.part


# Description: This is an oval or elliptical disk-shaped component with a flat base and a curved, ribbed or finned top surface featuring a central slot or opening, resembling a ventilation cover or filter housing.
def model_41599_f66b4e5b_0012():
    """Model: new1.2 v6"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 12.5663706144, perimeter: 12.5663706144
            Circle(2)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch3 -> Extrude2 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.7671458676, perimeter: 4.7123889804
            Circle(0.75)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.1735128443, perimeter: 2.0318764254
            with BuildLine():
                Line((-1.7000000253, -0.125), (-1.682300232, -0.1237405242))
                Line((-1.682300232, -0.1237405242), (-0.9946766507, -0.0748108401))
                CenterArc((-1.0000000149, 0), 0.075, -85.929826884, 171.859653768)
                Line((-1.682300232, 0.1237405242), (-0.9946766507, 0.0748108401))
                Line((-1.7000000253, 0.125), (-1.682300232, 0.1237405242))
                CenterArc((-1.7000000253, 0), 0.125, 90, 180)
            make_face()
        # OneSide extrude, distance=-0.1
        extrude(amount=-0.1, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a speaker or audio driver assembly consisting of a rectangular mounting bracket with two circular speaker cones and a flat base plate featuring dual fan-like vent patterns for acoustic output or cooling.
def model_41624_a15f83c1_0026():
    """Model: Pitch Bend buttons v2 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.5, perimeter: 9
            with BuildLine():
                Line((3, -1.5), (0, -1.5))
                Line((3, 0), (3, -1.5))
                Line((0, 0), (3, 0))
                Line((0, -1.5), (0, 0))
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.6361725124, perimeter: 2.8274333882
            with Locations((-2.2000000328, 0.8000000119)):
                Circle(0.45)
            # Profile area: 0.6361725124, perimeter: 2.8274333882
            with Locations((-0.8000000119, 0.8000000119)):
                Circle(0.45)
        # OneSide extrude, distance=-0.05
        extrude(amount=-0.05, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude3 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.6361725124, perimeter: 2.8274333882
            with Locations((0.6000000089, -2.3000000343)):
                Circle(0.45)
            # Profile area: 0.6361725124, perimeter: 2.8274333882
            with Locations((2.3000000343, -2.2000000328)):
                Circle(0.45)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)
    return part.part


# Description: This is a cylindrical rod or shaft with a slightly tapered or rounded end, featuring a smooth, uniform circular cross-section throughout its length.
def model_41648_577daf16_0004():
    """Model: Medium Leg"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.0106192983, perimeter: 5.0265482457
            Circle(0.8)
        # OneSide extrude, distance=20
        extrude(amount=20)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.0049261262, perimeter: 0.2960682782
            with BuildLine():
                CenterArc((0, 0), 0.8, 176.5270632841, 7.1345810831)
                Line((-0.7500000112, -0.0510914057), (-0.7983668757, -0.0510914057))
                Line((-0.7500000112, 0.0484616563), (-0.7500000112, -0.0510914057))
                Line((-0.7985308184, 0.0484616563), (-0.7500000112, 0.0484616563))
            make_face()
        # OneSide extrude, distance=-20
        extrude(amount=-20, mode=Mode.SUBTRACT)

        # Sketch2 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.0049261262, perimeter: 0.2960682782
            with BuildLine():
                Line((0.7985308184, 0.0484616563), (0.7500000112, 0.0484616563))
                Line((0.7500000112, 0.0484616563), (0.7500000112, -0.0510914057))
                Line((0.7500000112, -0.0510914057), (0.7983668757, -0.0510914057))
                CenterArc((0, 0), 0.8, -3.6616443672, 7.1345810831)
            make_face()
        # OneSide extrude, distance=-20
        extrude(amount=-20, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a linear guide rail or slide track, featuring an elongated rectangular profile with a grooved channel running along its length and a raised mounting flange or lip on one side.
def model_41650_9417da80_0002():
    """Model: Wheel connector v6"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.8000000536, perimeter: 7.2000001073
            with BuildLine():
                Line((-0.3000000045, 1.5000000224), (0.3000000045, 1.5000000224))
                Line((-0.3000000045, -1.5000000224), (-0.3000000045, 1.5000000224))
                Line((0.3000000045, -1.5000000224), (-0.3000000045, -1.5000000224))
                Line((0.3000000045, 1.5000000224), (0.3000000045, -1.5000000224))
            make_face()
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0000103064, perimeter: 0.1004122574
            with BuildLine():
                Line((-0.0126030636, 1.4500000216), (-0.0123969364, 1.4500000216))
                Line((-0.0126030636, 1.4000000201), (-0.0126030636, 1.4500000216))
                Line((-0.0123969364, 1.4000000201), (-0.0126030636, 1.4000000201))
                Line((-0.0123969364, 1.4500000216), (-0.0123969364, 1.4000000201))
            make_face()
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0078539816, perimeter: 0.3141592654
            with Locations((0, -1.3000000179)):
                Circle(0.05)
        # OneSide extrude, distance=-0.7
        extrude(amount=-0.7, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a lathe tool holder or cutting tool with a long, slender hexagonal prismatic body featuring a central longitudinal groove or slot running along its length, and beveled or chamfered ends for tool mounting and positioning.
def model_41650_9417da80_0008():
    """Model: Top connector v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.3200000095, perimeter: 3.6000000536
            with BuildLine():
                Line((0.1000000015, -0.8000000119), (-0.1000000015, -0.8000000119))
                Line((0.1000000015, 0.8000000119), (0.1000000015, -0.8000000119))
                Line((-0.1000000015, 0.8000000119), (0.1000000015, 0.8000000119))
                Line((-0.1000000015, -0.8000000119), (-0.1000000015, 0.8000000119))
            make_face()
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0078539816, perimeter: 0.3141592654
            with Locations((0.0000000015, -0.7000000119)):
                Circle(0.05)
        # OneSide extrude, distance=-0.1
        extrude(amount=-0.1, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0078539816, perimeter: 0.3141592654
            with Locations((-0.0000000015, 0.7000000119)):
                Circle(0.05)
        # OneSide extrude, distance=-0.1
        extrude(amount=-0.1, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a structural bracket or frame component with an elongated, tapered body featuring a central elongated slot and reinforcing ribs or webs on the upper surface for structural stiffness.
def model_41650_9417da80_0013():
    """Model: smallest connector v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.6000000179, perimeter: 3.2000000477
            with BuildLine():
                Line((0.3000000045, -0.5000000075), (0.3000000045, 0.5000000075))
                Line((0.3000000045, 0.5000000075), (-0.3000000045, 0.5000000075))
                Line((-0.3000000045, 0.5000000075), (-0.3000000045, -0.5000000075))
                Line((-0.3000000045, -0.5000000075), (0.3000000045, -0.5000000075))
            make_face()
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((0, 0.1999999955)):
                Circle(0.25)
        # OneSide extrude, distance=-0.14
        extrude(amount=-0.14, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0200000051, perimeter: 0.6000000462
            with BuildLine():
                Line((0.0999999978, -0.4500000197), (-0.0999999978, -0.4500000197))
                Line((0.0999999978, -0.3499999922), (0.0999999978, -0.4500000197))
                Line((-0.0999999978, -0.3499999922), (0.0999999978, -0.3499999922))
                Line((-0.0999999978, -0.4500000197), (-0.0999999978, -0.3499999922))
            make_face()
        # OneSide extrude, distance=-0.21
        extrude(amount=-0.21, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a dark blue plastic enclosure or housing with a rounded rectangular shape, featuring a mesh or perforated panel on the left side, an open front cavity, and internal ribbing or support structures visible through the design.
def model_41672_5364f9b6_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 15 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 3.6126548246, perimeter: 7.3132741229
            with BuildLine():
                CenterArc((0.4, 1.4), 0.4, 180, 90)
                Line((0.4, 1), (2.1, 1))
                CenterArc((2.1, 1.4), 0.4, -90, 90)
                Line((2.5, 1.4), (2.5, 2.1))
                CenterArc((2.1, 2.1), 0.4, 0, 90)
                Line((2.1, 2.5), (0.4, 2.5))
                CenterArc((0.4, 2.1), 0.4, 90, 90)
                Line((0, 2.1), (0, 1.4))
            make_face()
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)

        # Sketch4 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.3), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1.710000051, perimeter: 5.6000000834
            with BuildLine():
                Line((2.2000000328, 1.3000000194), (0.3000000045, 1.3000000194))
                Line((2.2000000328, 2.2000000328), (2.2000000328, 1.3000000194))
                Line((0.3000000045, 2.2000000328), (2.2000000328, 2.2000000328))
                Line((0.3000000045, 1.3000000194), (0.3000000045, 2.2000000328))
            make_face()
        # OneSide extrude, distance=0.1
        extrude(amount=0.1, mode=Mode.ADD)
    return part.part


# Description: This is a hexagonal box or container with open rectangular cutouts on two opposing sides, featuring a trapezoidal top opening and reinforced structural frame edges.
def model_41693_a737c734_0006():
    """Model: Body"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 8 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 18.5806075388, perimeter: 32.0040003729
            with BuildLine():
                Line((-5.0799999237, 8.8899999428), (-5.0799999237, 3.8099999428))
                Line((-5.0799999237, 3.8099999428), (0.0000000763, 3.8099999428))
                Line((0.0000000763, 3.8099999428), (0.0000000763, 8.8899999428))
                Line((0.0000000763, 8.8899999428), (-5.0799999237, 8.8899999428))
            make_face()
            with BuildLine():
                Line((-4.5720001459, 6.6040002108), (-4.5720001459, 8.3820002675))
                Line((-4.5720001459, 8.3820002675), (-0.5080000162, 8.3820002675))
                Line((-0.5080000162, 8.3820002675), (-0.5080000162, 6.6040002108))
                Line((-0.5080000162, 6.6040002108), (-4.5720001459, 6.6040002108))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=6.35
        extrude(amount=6.35)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -0.0000000763), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 24.6353721237, perimeter: 19.9206281096
            with BuildLine():
                Line((-0.4683655553, 8.3820002675), (-0.4683655553, 3.8099999428))
                Line((-0.4683655553, 8.3820002675), (-5.8566792853, 8.3820002675))
                Line((-5.8566792853, 3.8099999428), (-5.8566792853, 8.3820002675))
                Line((-0.4683655553, 3.8099999428), (-5.8566792853, 3.8099999428))
            make_face()
        # OneSide extrude, distance=-4.572
        extrude(amount=-4.572, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 5.0799999237), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 9.5804221179, perimeter: 14.3326275737
            with BuildLine():
                Line((5.8566792853, 6.6040002108), (0.4683655553, 6.6040002108))
                Line((5.8566792853, 8.3820002675), (5.8566792853, 6.6040002108))
                Line((0.4683655553, 8.3820002675), (5.8566792853, 8.3820002675))
                Line((0.4683655553, 6.6040002108), (0.4683655553, 8.3820002675))
            make_face()
        # OneSide extrude, distance=-0.508
        extrude(amount=-0.508, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical spool or drum with a solid circular base and a wireframe mesh or perforated cylindrical wall, featuring an open top design.
def model_41699_b8a7150b_0000():
    """Model: roller"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            with Locations((-2.5, -1)):
                Circle(1)
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch3 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((-2.5, -1)):
                Circle(0.15)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3, mode=Mode.ADD)
    return part.part


# Description: This is an elongated hexagonal prism or beam with a central longitudinal slot or groove running along its entire length, featuring chamfered or beveled edges at both ends.
def model_41737_3696185a_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch3 -> Extrude3 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 6.5, perimeter: 15
            with BuildLine():
                Line((6.5, -1), (0, -1))
                Line((6.5, 0), (6.5, -1))
                Line((0, 0), (6.5, 0))
                Line((0, -1), (0, 0))
            make_face()
        # OneSide extrude, distance=7
        extrude(amount=7)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 19.002775304, perimeter: 21.2881451854
            with BuildLine():
                Line((6.5, 7), (1.0706356274, 0))
                Line((6.5, 0), (1.0706356274, 0))
                Line((6.5, 0), (6.5, 7))
            make_face()
            # Profile area: 19.216801555, perimeter: 21.3869045596
            with BuildLine():
                Line((0, 7), (0, 0))
                Line((0, 0), (5.49051473, 7))
                Line((0, 7), (5.49051473, 7))
            make_face()
        # OneSide extrude, distance=-4
        extrude(amount=-4, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a elongated hexagonal or coffin-shaped housing component with a central rectangular slot running lengthwise, two opposing cylindrical boss features on the top surface, and angled end faces, likely designed as a mounting bracket or structural frame element.
def model_41739_1bc15d9f_0008():
    """Model: Frame bar"""
    with BuildPart() as part:
        # Sketch1 -> Extrude2 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 25.8063996124, perimeter: 25.3999999237
            with BuildLine():
                Line((86.3599988556, 2.5399999619), (86.3599988556, 0))
                Line((76.1999988556, 2.5399999619), (86.3599988556, 2.5399999619))
                Line((76.1999988556, 0), (76.1999988556, 2.5399999619))
                Line((86.3599988556, 0), (76.1999988556, 0))
            make_face()
        # OneSide extrude, distance=2.54
        extrude(amount=2.54)

        # Sketch2 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2.54, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.7316855998, perimeter: 3.0322652292
            with Locations((-85.1153988556, -1.2699999809)):
                Circle(0.4826)
            # Profile area: 0.7316855998, perimeter: 3.0322652292
            with Locations((-77.4445988556, -1.2699999809)):
                Circle(0.4826)
        # OneSide extrude, distance=-1.143
        extrude(amount=-1.143, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude4 (Cut)
        # Sketch on Profile plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.1043305807, perimeter: 7.1816808061
            with Locations((81.2799988556, 1.2699999809)):
                Circle(1.143)
        # OneSide extrude, distance=1.143
        extrude(amount=1.143, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical hub or pulley with a solid central disc and radial fins or blades extending outward from the top and sides, featuring a central bore and designed for rotational applications like cooling or power transmission.
def model_41753_9b4f8d8a_0008():
    """Model: wheel with rod v1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 5.1069802731, perimeter: 8.0110053571
            Circle(1.2749911017)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.5), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.2827433472, perimeter: 1.8849556202
            Circle(0.3000000045)
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.5), x_dir=(1, 0, 0), z_dir=(0, 0, 1))) as sk:
            # Profile area: 1.0505415114, perimeter: 16.8074649183
            with BuildLine():
                CenterArc((0, 0), 1.4000000209, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.2749911017, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # TwoSides extrude, along=-0.9, against=0.4
        extrude(amount=-0.9, mode=Mode.ADD)
        extrude(sk.sketch, amount=0.4, mode=Mode.ADD)
    return part.part


# Description: A circular flat washer with a large central hole, featuring a disk-like shape with a smooth outer diameter and a concentric inner hole for fastener passage.
def model_41757_c1173a7e_0003():
    """Model: Gear 1 v9"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 162.1463920175, perimeter: 63.8371632303
            with BuildLine():
                CenterArc((0, 0), 7.62, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 2.5400000811, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.762
        extrude(amount=0.762)

        # Sketch7 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.762), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.2026829916, perimeter: 1.595929068
            with Locations((0, 7.2798025828)):
                Circle(0.254)
        # OneSide extrude, distance=1.27
        extrude(amount=1.27, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical battery or cell with a dark metal cap on top and a blue-black cylindrical body, featuring a slightly tapered upper section where the cap connects.
def model_41757_c1173a7e_0007():
    """Model: Vertical Shaft v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 25.8064, perimeter: 20.32
            with BuildLine():
                Line((2.5399999189, -2.5399999189), (-2.5400000811, -2.5399999189))
                Line((2.5399999189, 2.5400000811), (2.5399999189, -2.5399999189))
                Line((-2.5400000811, 2.5400000811), (2.5399999189, 2.5400000811))
                Line((-2.5400000811, -2.5399999189), (-2.5400000811, 2.5400000811))
            make_face()
        # OneSide extrude, distance=20.32
        extrude(amount=20.32)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 20.32, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 11.4009182797, perimeter: 11.9694680102
            Circle(1.905)
        # OneSide extrude, distance=1.905
        extrude(amount=1.905, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 22.225, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 34.2027548391, perimeter: 35.9084040305
            with BuildLine():
                CenterArc((0, 0), 3.81, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.905, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 11.4009182797, perimeter: 11.9694680102
            Circle(1.905)
        # OneSide extrude, distance=0.0254
        extrude(amount=0.0254, mode=Mode.ADD)
    return part.part


# Description: This is a hexagonal shaft or rod with a longitudinal slot or groove running along its length, featuring a dark metallic finish with subtle blue highlights on its faceted surfaces.
def model_41759_269be149_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 7 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0719999968, perimeter: 1.4399999678
            with BuildLine():
                Line((0.2999999933, -0.0599999987), (0.2999999933, 0.0599999987))
                Line((0.2999999933, 0.0599999987), (-0.2999999933, 0.0599999987))
                Line((-0.2999999933, 0.0599999987), (-0.2999999933, -0.0599999987))
                Line((-0.2999999933, -0.0599999987), (0.2999999933, -0.0599999987))
            make_face()
        # TwoSides extrude (symmetric), distance=0.06
        extrude(amount=0.06, both=True)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 7 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.2999999933), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0134560013, perimeter: 0.464000022
            with BuildLine():
                Line((0.0580000028, -0.0580000028), (0.0580000028, 0.0580000028))
                Line((0.0580000028, 0.0580000028), (-0.0580000028, 0.0580000028))
                Line((-0.0580000028, 0.0580000028), (-0.0580000028, -0.0580000028))
                Line((-0.0580000028, -0.0580000028), (0.0580000028, -0.0580000028))
            make_face()
        # OneSide extrude, distance=-0.59
        extrude(amount=-0.59, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -0.2900000067), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0095033178, perimeter: 0.3455751919
            Circle(0.055)
        # OneSide extrude, distance=-0.005
        extrude(amount=-0.005, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a hollow cylindrical bushing or spacer with a coaxial bore, featuring concentric inner and outer cylindrical surfaces with what appears to be a flanged or stepped design at one end.
def model_41759_77eaa071_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0962112707, perimeter: 1.0995574042
            Circle(0.1749999961)
        # OneSide extrude, distance=0.06
        extrude(amount=0.06)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.0530929158, perimeter: 0.8168140899
            Circle(0.13)
        # OneSide extrude, distance=0.15
        extrude(amount=0.15, mode=Mode.ADD)
    return part.part


# Description: This is a snow shovel consisting of a wide, flat rectangular blade with a slight curve and two long parallel handles extending upward at an angle for snow removal and pushing.
def model_41759_9ee337cf_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.067199997, perimeter: 1.1599999741
            with BuildLine():
                Line((0.2099999953, -0.0799999982), (0.2099999953, 0.0799999982))
                Line((0.2099999953, 0.0799999982), (-0.2099999953, 0.0799999982))
                Line((-0.2099999953, 0.0799999982), (-0.2099999953, -0.0799999982))
                Line((-0.2099999953, -0.0799999982), (0.2099999953, -0.0799999982))
            make_face()
        # OneSide extrude, distance=0.15
        extrude(amount=0.15)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.15, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0009621128, perimeter: 0.1099557429
            with Locations((-0.0999999978, -0.0549999988)):
                Circle(0.0175)
            # Profile area: 0.0009621128, perimeter: 0.1099557429
            with Locations((-0.1649999963, -0.0549999988)):
                Circle(0.0175)
        # OneSide extrude, distance=0.05
        extrude(amount=0.05, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0001767146, perimeter: 0.0471238898
            with Locations((-0.1649999963, -0.0549999988)):
                Circle(0.0075)
            # Profile area: 0.0001767146, perimeter: 0.0471238898
            with Locations((-0.0999999978, -0.0549999988)):
                Circle(0.0075)
        # OneSide extrude, distance=1.3
        extrude(amount=1.3, mode=Mode.ADD)
    return part.part


# Description: This is a stepped cylindrical shaft or post with two different diameters connected by a shoulder, featuring a smaller diameter upper section and a larger diameter lower section.
def model_41785_e22ea270_0000():
    """Model: Smallest hexagonal screw"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.7391931082, perimeter: 3.2004
            with BuildLine():
                Line((0.4117974414, 0.339025703), (-0.0877061506, 0.5261398969))
                Line((-0.0877061506, 0.5261398969), (-0.499503592, 0.187114194))
                Line((-0.499503592, 0.187114194), (-0.4117974414, -0.339025703))
                Line((-0.4117974414, -0.339025703), (0.0877061506, -0.5261398969))
                Line((0.0877061506, -0.5261398969), (0.499503592, -0.187114194))
                Line((0.499503592, -0.187114194), (0.4117974414, 0.339025703))
            make_face()
        # OneSide extrude, distance=2.54
        extrude(amount=2.54)

        # Sketch3 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2.54, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.4225009338, perimeter: 5.195311335
            with BuildLine():
                Line((-0.499503592, 0.187114194), (-0.4117974414, -0.339025703))
                Line((-0.4117974414, -0.339025703), (0.0877061506, -0.5261398969))
                Line((0.0877061506, -0.5261398969), (0.499503592, -0.187114194))
                Line((0.499503592, -0.187114194), (0.4117974414, 0.339025703))
                Line((0.4117974414, 0.339025703), (-0.0877061506, 0.5261398969))
                Line((-0.0877061506, 0.5261398969), (-0.499503592, 0.187114194))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.3175, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.889
        extrude(amount=-0.889, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2.54, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0614621526, perimeter: 3.8754886197
            with BuildLine():
                CenterArc((0, 0), 0.3175, 0, 360)
            make_face()
            with BuildLine():
                Line((-0.2935117825, 0.1099496009), (-0.2419750388, -0.1992138595))
                Line((-0.0515367437, 0.3091634604), (-0.2935117825, 0.1099496009))
                Line((0.2419750388, 0.1992138595), (-0.0515367437, 0.3091634604))
                Line((0.2935117825, -0.1099496009), (0.2419750388, 0.1992138595))
                Line((0.0515367437, -0.3091634604), (0.2935117825, -0.1099496009))
                Line((-0.2419750388, -0.1992138595), (0.0515367437, -0.3091634604))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.889
        extrude(amount=-0.889, mode=Mode.SUBTRACT)
    return part.part


# Description: A circular steering wheel with a three-spoke design featuring a textured grip rim, a central hub, and three evenly-spaced radial spokes connecting the rim to the center boss.
def model_41852_ca66b6b4_0004():
    """Model: Component6"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 10 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0.8576141197, -2, -3.649922979), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.1134023493, perimeter: 4.1718207015
            with BuildLine():
                CenterArc((5.5245000683, 3.0480000377), 0.3591658826, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((5.5245000683, 3.0480000377), 0.3048000038, 80.5082287124, 18.9835425753)
                CenterArc((5.5245000683, 3.0480000377), 0.3048000038, 8.9980703245, 71.5101583878)
                CenterArc((5.5245000683, 3.0480000377), 0.3048000038, -5.9946255248, 14.9926958494)
                CenterArc((5.5245000683, 3.0480000377), 0.3048000038, -174.5210818811, 168.5264563562)
                CenterArc((5.5245000683, 3.0480000377), 0.3048000038, 171.0019296755, 14.4769884435)
                CenterArc((5.5245000683, 3.0480000377), 0.3048000038, 99.4917712876, 71.5101583878)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0114168376, perimeter: 0.5271401783
            with BuildLine():
                Line((5.6197942397, 3.0368801416), (5.827633333, 3.0161681961))
                CenterArc((5.5245000683, 3.0480000377), 0.3048000038, -5.9946255248, 14.9926958494)
                Line((5.618677209, 3.0663111645), (5.8255490839, 3.0956711241))
                CenterArc((5.5245000683, 3.0480000377), 0.0959407692, -6.6557554097, 17.6586543689)
            make_face()
            # Profile area: 0.0133588149, perimeter: 0.5457290262
            with BuildLine():
                CenterArc((5.5245000683, 3.0480000377), 0.0959407692, 81.9578154028, 16.0843691943)
                Line((5.5379223889, 3.1429972613), (5.5747634042, 3.3486271146))
                CenterArc((5.5245000683, 3.0480000377), 0.3048000038, 80.5082287124, 18.9835425753)
                Line((5.5110777476, 3.1429972613), (5.4742367324, 3.3486271146))
            make_face()
            # Profile area: 0.0289172017, perimeter: 0.6028136315
            with BuildLine():
                CenterArc((5.5245000683, 3.0480000377), 0.0959407692, 98.0421845972, 70.9549164437)
                CenterArc((5.5245000683, 3.0480000377), 0.0959407692, 168.9971010408, 17.6586543689)
                CenterArc((5.5245000683, 3.0480000377), 0.0959407692, -173.3442445903, 166.6884891806)
                CenterArc((5.5245000683, 3.0480000377), 0.0959407692, -6.6557554097, 17.6586543689)
                CenterArc((5.5245000683, 3.0480000377), 0.0959407692, 11.0028989592, 70.9549164437)
                CenterArc((5.5245000683, 3.0480000377), 0.0959407692, 81.9578154028, 16.0843691943)
            make_face()
            # Profile area: 0.0111303236, perimeter: 0.5244169469
            with BuildLine():
                CenterArc((5.5245000683, 3.0480000377), 0.3048000038, 171.0019296755, 14.4769884435)
                Line((5.4292058969, 3.0368801416), (5.2210925746, 3.0188978882))
                CenterArc((5.5245000683, 3.0480000377), 0.0959407692, 168.9971010408, 17.6586543689)
                Line((5.4303229276, 3.0663111645), (5.2234510526, 3.0956711241))
            make_face()
        # OneSide extrude, distance=0.04572
        extrude(amount=0.04572)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 0, -3.604202979), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0069185728, perimeter: 0.2948581872
            with Locations((6.382114188, 1.0480000377)):
                Circle(0.046928138)
        # OneSide extrude, distance=0.01524
        extrude(amount=0.01524, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -3.649922979), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.0182414697, perimeter: 0.4787787263
            with Locations((-6.382114188, 1.0480000377)):
                Circle(0.0762000009)
        # OneSide extrude, distance=-0.01905
        extrude(amount=-0.01905, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a jet aircraft with a sleek, angular fuselage, swept-back wings, rear stabilizer fins, and blue-highlighted air intake and panel details, shown in an isometric 3D view.
def model_41859_173a686e_0004():
    """Model: Plane v4"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 20 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.5915639678, perimeter: 7.1979695814
            with BuildLine():
                CenterArc((0.7829717004, 1.496068073), 0.1958328488, -1.1196514825, 42.2121139115)
                CenterArc((0.8999999799, 1.7199999616), 0.0999999978, -72.2050600551, 324.6911103947)
                CenterArc((1.0190052371, 1.4920792435), 0.1995036693, 138.3613401256, 41.6386598744)
                Line((0.8195015678, 1.1904152936), (0.8195015678, 1.4920792435))
                Line((0.6770361574, 1.0801295484), (0.8195015678, 1.1904152936))
                Line((0.6770361574, 1.1407327087), (0.6770361574, 1.0801295484))
                CenterArc((0.6493184329, 1.1389559383), 0.0277746137, 3.667774166, 86.332225834)
                Line((0.5872125758, 1.1667305519), (0.6493184329, 1.1667305519))
                CenterArc((0.5885308289, 1.1351598732), 0.031598189, 92.3910315219, 72.2119448067)
                Line((0.5580667242, 1.0699269592), (0.5580667242, 1.1435493831))
                CenterArc((0.631387417, 1.0631305709), 0.0736350113, 174.7041580458, 56.4558847835)
                Line((0.1879662037, 0.6924244283), (0.5852074291, 1.0057762023))
                Line((0.1879662037, 0.6110023138), (0.1879662037, 0.6924244283))
                Line((0.5949743759, 0.7798282412), (0.1879662037, 0.6110023138))
                Line((0.8170390166, 0.8383332799), (0.5949743759, 0.7798282412))
                Line((0.8172899488, 0.5150971972), (0.8170390166, 0.8383332799))
                CenterArc((1.4465517495, 0.5155857008), 0.6292619903, -179.9555205937, 11.0893326248)
                Line((0.6359425512, 0.2124423558), (0.8291331746, 0.3940745659))
                Line((0.6359425512, 0.1422662747), (0.6359425512, 0.2124423558))
                Line((0.8649642561, 0.228128774), (0.6359425512, 0.1422662747))
                CenterArc((0.935566618, 0.2411423873), 0.0717916962, -169.5563122584, 52.9706163205)
                CenterArc((0.8649642561, 0.239356947), 0.0733202445, -58.3502317689, 48.8879095608)
                Line((1.1670267868, 0.1431904041), (0.9372868997, 0.227303173))
                Line((1.1670267868, 0.2175114777), (1.1670267868, 0.1431904041))
                Line((0.9683049943, 0.4010224116), (1.1670267868, 0.2175114777))
                CenterArc((0.3826578329, 0.5454479272), 0.603192612, -13.8532050624, 13.8532050624)
                Line((0.9858504449, 0.8362426839), (0.9858504449, 0.5454479272))
                Line((1.1891622071, 0.7863560015), (0.9858504449, 0.8362426839))
                Line((1.6073790845, 0.6103744396), (1.1891622071, 0.7863560015))
                Line((1.6073790845, 0.6885431673), (1.6073790845, 0.6103744396))
                Line((1.2207057942, 1.0044158351), (1.6073790845, 0.6885431673))
                CenterArc((1.1582666415, 1.0564655196), 0.0812884829, -39.8148072115, 39.8148072115)
                Line((1.2395551244, 1.1441314154), (1.2395551244, 1.0564655196))
                CenterArc((1.2090288735, 1.1361924921), 0.0315416946, 14.5779046472, 75.4220953528)
                Line((1.154270444, 1.1677341867), (1.2090288735, 1.1677341867))
                CenterArc((1.151257594, 1.136326623), 0.0315517405, 84.5205238182, 95.4794761818)
                Line((1.1197058535, 1.0783455143), (1.1197058535, 1.136326623))
                Line((0.9787671586, 1.1943077316), (1.1197058535, 1.0783455143))
                Line((0.9787671586, 1.4922414284), (0.9787671586, 1.1943077316))
            make_face()
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)

        # Sketch3 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.3), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0201061921, perimeter: 0.5026548133
            with Locations((0.8999999799, 1.7199999616)):
                Circle(0.0799999982)
        # OneSide extrude, distance=-0.31
        extrude(amount=-0.31, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a multi-flanged connector or junction block with an irregular, star-like shape featuring multiple rectangular flanges extending from a central dark core, with grid-like surface patterns and mounting holes distributed across its faces.
def model_41859_173a686e_0007():
    """Model: Flower v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 0.881739098, perimeter: 5.7800814279
            with BuildLine():
                CenterArc((0.9099999797, 1.5999999642), 0.0999999978, -70.4488787855, 319.6263719432)
                CenterArc((1.345687472, 1.1474658179), 0.5924444255, 142.6937887021, 26.7997647888)
                CenterArc((0.3710692489, 0.6820279209), 0.6947034483, 55.6377789121, 28.1419145364)
                CenterArc((1.0729132055, 1.3798379711), 0.6266129898, -179.3419497639, 30.6631790024)
                CenterArc((0.6723482558, 0.4085214215), 0.6594896026, 101.7881406588, 28.3725066072)
                CenterArc((0.6382852981, 1.2910836961), 0.5444177713, -135.9458244165, 35.290137301)
                CenterArc((1.0616017415, 0.3934064228), 0.637237154, 145.3129777073, 30.1530262696)
                CenterArc((0.3996828987, 1.102895808), 0.6596550033, -87.6823781965, 28.8762542514)
                CenterArc((1.4267084969, 0.6997486107), 0.7040539906, -166.7696308189, 26.9340091544)
                CenterArc((0.224207337, 0.7869131906), 0.8570204575, -39.1659471375, 22.3245265323)
                CenterArc((1.4365401972, 1.1511563171), 0.7272735488, -122.622073406, 26.134959805)
                CenterArc((0.7378623145, 0.4146906572), 0.6166662223, 1.286814224, 30.9378694104)
                CenterArc((1.0841034505, 1.4530703802), 0.7309147431, -76.1121310682, 25.6221012908)
                CenterArc((1.1511819542, 0.4843837928), 0.5676253096, 45.4880060374, 33.5069067231)
                CenterArc((0.4670285948, 1.5115317176), 0.9213777114, -30.6680573151, 20.7709964524)
                CenterArc((1.3951629636, 0.7009725786), 0.6525151712, 91.7975815173, 30.0098619434)
                CenterArc((0.4282269604, 1.1355341129), 0.6344614799, 10.8988865185, 24.8007915129)
            make_face()
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.0201061921, perimeter: 0.5026548133
            with Locations((-0.9099999797, 1.5999999642)):
                Circle(0.0799999982)
        # OneSide extrude, distance=-0.46
        extrude(amount=-0.46, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.0706858368, perimeter: 0.9424778101
            with Locations((-0.9000000134, 0.9000000134)):
                Circle(0.1500000022)
        # OneSide extrude, distance=-0.6
        extrude(amount=-0.6, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a telescope or microscope eyepiece assembly featuring a cylindrical dark barrel with a curved top section, a flat blue base plate, and a small perpendicular adjustment knob or focus mechanism protruding from the left side.
def model_41859_173a686e_0010():
    """Model: ClaspBase v5"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1063081215, perimeter: 3.9415421341
            with BuildLine():
                Line((-0.3258379945, -0.4500000067), (0.5000000075, -0.4500000067))
                CenterArc((-0.3999999911, -0.4199999906), 0.0800000168, -22.024320392, 292.024320392)
                Line((0.5000000075, -0.5000000075), (-0.3999999911, -0.5000000075))
                CenterArc((0.5000000075, -0.3000000045), 0.200000003, -90, 285.1367197192)
                Line((0.3593849748, -0.3522246467), (0.3069389085, -0.3522246467))
                CenterArc((0.5000000075, -0.3000000045), 0.1500000022, -90, 290.3750750878)
            make_face()
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.3, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0182950874, perimeter: 0.720092208
            with BuildLine():
                Line((0.3258379945, 0.4500000067), (0.3261472519, 0.5000000075))
                CenterArc((0.3999999911, 0.4199999906), 0.0800000168, 157.975679608, 292.024320392)
                Line((0.3999999911, 0.5000000075), (0.3261472519, 0.5000000075))
            make_face()
            with BuildLine():
                CenterArc((0.3999999911, 0.4199999906), 0.0299999993, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.1
        extrude(amount=-0.1, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.0182950874, perimeter: 0.720092208
            with BuildLine():
                Line((-0.3261472519, 0.5000000075), (-0.3999999911, 0.5000000075))
                CenterArc((-0.3999999911, 0.4199999906), 0.0800000168, 90, 292.024320392)
                Line((-0.3258379945, 0.4500000067), (-0.3261472519, 0.5000000075))
            make_face()
            with BuildLine():
                CenterArc((-0.3999999911, 0.4199999906), 0.0299999993, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.1
        extrude(amount=-0.1, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a protective dome or cover with a semi-elliptical/hemispherical shape, featuring a perforated mesh or textured top surface, a solid curved body, and a flat rectangular base or flange for mounting.
def model_41896_7d8659e6_0003():
    """Model: Brake Hinge v5"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 3 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 4.2331579856, perimeter: 9.0265482457
            with BuildLine():
                Line((2.5, 0.75), (2.5, 0))
                CenterArc((1.25, 0.75), 1.25, 0, 180)
                Line((0, 0), (0, 0.75))
                Line((2.5, 0), (0, 0))
            make_face()
            with BuildLine():
                CenterArc((1.25, 1.2772267791), 0.175, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=3.25
        extrude(amount=3.25)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 6.8750001024, perimeter: 10.500000082
            with BuildLine():
                Line((2.5, 0.2500000037), (0, 0.2500000037))
                Line((2.5, 0.2500000037), (2.5, 3.0000000447))
                Line((0, 3.0000000447), (2.5, 3.0000000447))
                Line((0, 3.0000000447), (0, 0.2500000037))
            make_face()
            # Profile area: 0.4125001147, perimeter: 5.8000001609
            with BuildLine():
                Line((2.6500000395, 0.2500000037), (2.5, 0.2500000037))
                Line((2.6500000395, 3.0000000447), (2.6500000395, 0.2500000037))
                Line((2.5, 3.0000000447), (2.6500000395, 3.0000000447))
                Line((2.5, 0.2500000037), (2.5, 3.0000000447))
            make_face()
            # Profile area: 0.5500000164, perimeter: 5.9000000879
            with BuildLine():
                Line((0, 3.0000000447), (0, 0.2500000037))
                Line((-0.200000003, 3.0000000447), (0, 3.0000000447))
                Line((-0.200000003, 0.2500000037), (-0.200000003, 3.0000000447))
                Line((0, 0.2500000037), (-0.200000003, 0.2500000037))
            make_face()
        # OneSide extrude, distance=-2.5
        extrude(amount=-2.5, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 1.2700000565, perimeter: 9.6000001431
            with BuildLine():
                Line((-2.5, 0.5000000075), (-2.5, 0))
                Line((-3.0000000447, 0.5000000075), (-2.5, 0.5000000075))
                Line((-3.0000000447, -0.200000003), (-3.0000000447, 0.5000000075))
                Line((0.6000000089, -0.200000003), (-3.0000000447, -0.200000003))
                Line((0.6000000089, 0.5000000075), (0.6000000089, -0.200000003))
                Line((0, 0.5000000075), (0.6000000089, 0.5000000075))
                Line((0, 0), (0, 0.5000000075))
                Line((-2.5, 0), (0, 0))
            make_face()
            # Profile area: 1.2500000186, perimeter: 6.0000000149
            with BuildLine():
                Line((-2.5, 0), (0, 0))
                Line((0, 0), (0, 0.5000000075))
                Line((-2.5, 0.5000000075), (0, 0.5000000075))
                Line((-2.5, 0.5000000075), (-2.5, 0))
            make_face()
        # OneSide extrude, distance=-3.8
        extrude(amount=-3.8, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical sleeve or barrel with a knurled or textured surface pattern, featuring a hollow bore through its center and slightly tapered ends.
def model_41896_7d8659e6_0009():
    """Model: Base Neck Clamp Pin v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            Circle(0.15)
        # OneSide extrude, distance=1.2
        extrude(amount=1.2)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on XY construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.016627687, perimeter: 0.4799999893
            with BuildLine():
                Line((0.0799999982, 0.0007179677), (0.0399999991, 0.0699999984))
                Line((0.0399999991, 0.0699999984), (-0.0399999991, 0.0699999984))
                Line((-0.0399999991, 0.0699999984), (-0.0799999982, 0.0007179677))
                Line((-0.0799999982, 0.0007179677), (-0.0399999991, -0.0685640631))
                Line((-0.0399999991, -0.0685640631), (0.0399999991, -0.0685640631))
                Line((0.0399999991, -0.0685640631), (0.0799999982, 0.0007179677))
            make_face()
        # OneSide extrude, distance=0.1
        extrude(amount=0.1, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1.2), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.016627687, perimeter: 0.4799999893
            with BuildLine():
                Line((0.0399999991, 0.0699999984), (-0.0399999991, 0.0699999984))
                Line((-0.0399999991, 0.0699999984), (-0.0799999982, 0.0007179677))
                Line((-0.0799999982, 0.0007179677), (-0.0399999991, -0.0685640631))
                Line((-0.0399999991, -0.0685640631), (0.0399999991, -0.0685640631))
                Line((0.0399999991, -0.0685640631), (0.0799999982, 0.0007179677))
                Line((0.0799999982, 0.0007179677), (0.0399999991, 0.0699999984))
            make_face()
        # OneSide extrude, distance=-0.1
        extrude(amount=-0.1, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a curved cylindrical shell or band with a ribbed/corrugated exterior surface and an open latticed or mesh-like interior structure, featuring a tapered oval cross-section and angled orientation.
def model_41924_ac7400c0_0003():
    """Model: Power Button"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.5359435214, perimeter: 3.1407183854
            with Locations((3, -5)):
                Ellipse(0.6999999359, 0.243708767, rotation=90)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch4 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.010988249, perimeter: 0.9404203791
            with BuildLine():
                CenterArc((-3.0000000447, 5.0000000745), 0.1, -59.0339188793, 298.0678377586)
                Line((-3.0514530992, 4.9142528694), (-3.0514530992, 4.9454328391))
                CenterArc((-3.0000000447, 5.0000000745), 0.075, -46.6824905378, 273.3649810755)
                Line((-2.9485469902, 4.9142528694), (-2.9485469902, 4.9454328391))
            make_face()
        # OneSide extrude, distance=-0.05
        extrude(amount=-0.05, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0035999998, perimeter: 0.2599999942
            with BuildLine():
                Line((-3.0199999325, 4.9899998885), (-2.9799999334, 4.9899998885))
                Line((-3.0199999325, 4.8999998905), (-3.0199999325, 4.9899998885))
                Line((-2.9799999334, 4.8999998905), (-3.0199999325, 4.8999998905))
                Line((-2.9799999334, 4.9899998885), (-2.9799999334, 4.8999998905))
            make_face()
            # Profile area: 0.010988249, perimeter: 0.9404203791
            with BuildLine():
                CenterArc((-3.0000000447, 5.0000000745), 0.1, -59.0339188793, 298.0678377586)
                Line((-3.0514530992, 4.9142528694), (-3.0514530992, 4.9454328391))
                CenterArc((-3.0000000447, 5.0000000745), 0.075, -46.6824905378, 273.3649810755)
                Line((-2.9485469902, 4.9142528694), (-2.9485469902, 4.9454328391))
            make_face()
        # OneSide extrude, distance=-0.02
        extrude(amount=-0.02, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a dark blue metal bracket or mounting plate with a bent or angled L-shape design, featuring a small rectangular slot or cutout on the upper flange and appears to be a structural component for assembly or attachment purposes.
def model_41982_f75ceb8f_0010():
    """Model: bottom platform v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 202.5, perimeter: 63
            with BuildLine():
                Line((-4.5, 9), (-4.5, 0))
                Line((-4.5, 0), (18, 0))
                Line((18, 0), (18, 9))
                Line((18, 9), (-4.5, 9))
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0.2, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 3.5200001049, perimeter: 18.4000002742
            with BuildLine():
                Line((17.9000002667, 0.1000000015), (17.5000002608, 0.1000000015))
                Line((17.9000002667, 8.9000001326), (17.9000002667, 0.1000000015))
                Line((17.5000002608, 8.9000001326), (17.9000002667, 8.9000001326))
                Line((17.5000002608, 0.1000000015), (17.5000002608, 8.9000001326))
            make_face()
        # OneSide extrude, distance=5
        extrude(amount=5, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -17.9000002667), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 2.5200000751, perimeter: 17.4000002593
            with BuildLine():
                Line((-3.3000000492, 0.3000000045), (-3.3000000492, 8.7000001296))
                Line((-3.3000000492, 8.7000001296), (-3.6000000536, 8.7000001296))
                Line((-3.6000000536, 8.7000001296), (-3.6000000536, 0.3000000045))
                Line((-3.6000000536, 0.3000000045), (-3.3000000492, 0.3000000045))
            make_face()
        # OneSide extrude, distance=2.5
        extrude(amount=2.5, mode=Mode.ADD)
    return part.part


# Description: This is a long, slender drive shaft or axle with a cylindrical body and small flanged or squared-off ends at both terminals for coupling or mounting purposes.
def model_41982_f75ceb8f_0016():
    """Model: bottom frame 3 v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 22, perimeter: 46
            with BuildLine():
                Line((-10, 1), (-10, 0))
                Line((-10, 0), (12, 0))
                Line((12, 0), (12, 1))
                Line((12, 1), (-10, 1))
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 15 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.5276539133, perimeter: 6.6274121588
            with BuildLine():
                Line((-0.2, 8.1000214284), (-0.2000000045, 9.9000001475))
                Line((-0.2000000045, 9.9000001475), (-1.2000001475, 9.9))
                CenterArc((-1.2, 9), 0.9, -89.999992316, 180.0000017075)
                Line((-0.3000000045, 8.1000001207), (-1.1999998793, 8.1))
                Line((-0.3000000045, 8.1000001207), (-0.2, 8.1000214284))
            make_face()
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 11 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.527654986, perimeter: 6.6274334642
            with BuildLine():
                Line((-0.3000000045, -10.1000001505), (-1.1999998495, -10.1))
                CenterArc((-1.2, -11), 0.9, -90.0000112888, 180.0000017075)
                Line((-0.3000000045, -11.9000001773), (-1.2000001773, -11.9))
                Line((-0.3000000045, -11.9000001773), (-0.2000000045, -11.9000001773))
                Line((-0.2000000045, -11.9000001773), (-0.2, -10.1000001505))
                Line((-0.3000000045, -10.1000001505), (-0.2, -10.1000001505))
            make_face()
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical axle or shaft assembly with two large circular flanges or wheels at each end and a smaller diameter central shaft, featuring horizontal slot details along the middle section.
def model_41982_f75ceb8f_0026():
    """Model: hinge pin v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            Circle(0.25)
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(1.5, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0863938064, perimeter: 3.455751947
            with BuildLine():
                CenterArc((0, 0), 0.3000000045, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            Circle(0.25)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.0863938064, perimeter: 3.455751947
            with BuildLine():
                CenterArc((0, 0), 0.3000000045, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            Circle(0.25)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1, mode=Mode.ADD)
    return part.part


# Description: This is an elongated hexagonal or octagonal prism-shaped component with a recessed central channel or slot running along its length, featuring angled faceted surfaces and what appears to be mounting flanges at the ends.
def model_41985_727bc619_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 7 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.1100000033, perimeter: 1.5000000224
            with BuildLine():
                Line((0.2500000037, 0.3500000052), (0.2500000037, 0))
                Line((0.1500000022, 0.3500000052), (0.2500000037, 0.3500000052))
                Line((0.1500000022, 0.5000000075), (0.1500000022, 0.3500000052))
                Line((0, 0.5000000075), (0.1500000022, 0.5000000075))
                Line((0, 0), (0, 0.5000000075))
                Line((0.2500000037, 0), (0, 0))
            make_face()
        # OneSide extrude, distance=1.8
        extrude(amount=1.8)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.1500000022, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.030107975, perimeter: 0.7014396709
            with BuildLine():
                Line((0, 0.3500000052), (0, 0.5000000075))
                Line((-0.2007396612, 0.5000000075), (0, 0.5000000075))
                Line((-0.2007396612, 0.5000000075), (-0.2007, 0.3500000052))
                Line((0, 0.3500000052), (-0.2007, 0.3500000052))
            make_face()
        # OneSide extrude, distance=-0.15
        extrude(amount=-0.15, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.1500000022, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0301050004, perimeter: 0.7014000045
            with BuildLine():
                Line((-1.5993, 0.5000000075), (-1.5993, 0.3500000052))
                Line((-1.8, 0.5000000075), (-1.5993, 0.5000000075))
                Line((-1.8, 0.5000000075), (-1.8, 0.3500000052))
                Line((-1.8, 0.3500000052), (-1.5993, 0.3500000052))
            make_face()
        # OneSide extrude, distance=-0.15
        extrude(amount=-0.15, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a toroidal or dumbbell-shaped mechanical component with two opposing cylindrical flanges connected by a narrower central section, featuring a continuous hollow core running through its center and displaying a mesh surface structure typical of CAD visualization.
def model_41998_654ac923_0007():
    """Model: Clamp Connector v2 (2)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            Circle(0.2)
        # OneSide extrude, distance=0.4
        extrude(amount=0.4)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0.4, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.3769911334, perimeter: 3.7699112218
            with BuildLine():
                CenterArc((0, 0), 0.400000006, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            Circle(0.2)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.3769911334, perimeter: 3.7699112218
            with BuildLine():
                CenterArc((0, 0), 0.400000006, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            Circle(0.2)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)
    return part.part


# Description: A simple cylindrical fastener with a pointed tip at one end and a flat head at the other, used for fastening materials together.
def model_42005_1f6ccfca_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            Circle(0.2)
        # Symmetric extrude, each_side=5
        extrude(amount=5, both=True)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            Circle(0.4)
        # Symmetric extrude, each_side=5.2
        extrude(amount=5.2, both=True, mode=Mode.ADD)

        # Sketch2 -> Extrude3 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            Circle(0.4)
        # Symmetric extrude, each_side=5
        extrude(amount=5, both=True, mode=Mode.SUBTRACT)

        # Sketch1 -> Extrude4 (Join)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            Circle(0.2)
        # Symmetric extrude, each_side=5
        extrude(amount=5, both=True, mode=Mode.ADD)
    return part.part


# Description: This is a twisted or warped rectangular prism with a trapezoidal cross-section, featuring a tapered form that transitions from a wider base to a narrower top, with internal geometric subdivisions and curved surfaces creating a complex, organically-twisted geometry.
def model_42143_51b31600_0002():
    """Model: Keypad Base"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 26.3718103123, perimeter: 24.8638634405
            with BuildLine():
                Line((2, 6), (-3, 6))
                Line((-3, 6), (-3, -2))
                Line((-3, -2), (-0.5968819623, -2))
                CenterArc((3, -0.2500171004), 4, 104.4775121859, 101.4666951893)
                Line((2, 3.6229662458), (2, 6))
            make_face()
        # OneSide extrude, distance=5
        extrude(amount=5)
    return part.part


# Description: This is a cable tie (or zip tie) featuring a flat rectangular head with ratcheting teeth on one side and an elongated loop with a sliding locking mechanism for bundling and securing cables or wires together.
def model_42333_53c85dac_0020():
    """Model: fix"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 20 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.4837166689, perimeter: 22.7899531831
            with BuildLine():
                CenterArc((0.8, 2.135), 0.4, 180, 68.7379488982)
                Line((0.4, 2.135), (-0.4, 2.135))
                CenterArc((-0.8, 2.135), 0.4, -68.7379488982, 68.7379488982)
                CenterArc((-0.8, 2.135), 0.4, -70.1793732798, 1.4414243816)
                CenterArc((0, 0), 1.88, 110.6946780696, 318.6106438608)
                CenterArc((0.8, 2.135), 0.4, -111.2620511018, 1.4414243816)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.68, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)

        # Sketch3 -> Extrude2 (Join)
        # Sketch on YZ construction plane
        # Sketch has 14 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0646906706, perimeter: 1.0434185526
            with BuildLine():
                Line((1.9694, 0), (2.3723368375, 0))
                CenterArc((2.1694, 0), 0.2029368375, 0, 180)
                Line((1.9694, 0), (1.9664631625, 0))
            make_face()
            # Profile area: 0.8242656014, perimeter: 8.7588053791
            with BuildLine():
                Line((2.1694, -0.2), (2.1694, -1.36))
                CenterArc((2.3723368375, -1.36), 0.2029368375, 180, 90)
                Line((2.3723368375, -1.5629368375), (4.8723368375, -1.5629368375))
                Line((4.8723368375, -1.36), (4.8723368375, -1.5629368375))
                Line((2.3723368375, -1.36), (4.8723368375, -1.36))
                Line((2.3723368375, 0), (2.3723368375, -1.36))
                Line((1.9694, 0), (2.3723368375, 0))
                CenterArc((1.9694, -0.2), 0.2, 0, 90)
            make_face()
        # Symmetric extrude, each_side=0.5
        extrude(amount=0.5, both=True, mode=Mode.ADD)

        # Sketch2 -> Extrude3 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 20 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 255.8673459568, perimeter: 92.0303014993
            with BuildLine():
                CenterArc((0, 0), 1.88, 69.3053219304, 0.3066783172)
                CenterArc((0, 0), 1.88, 110.6946780696, 318.6106438608)
                CenterArc((0, 0), 1.88, 110.3879997524, 0.3066783172)
                CenterArc((-0.8, 2.135), 0.4, -68.7379488982, 68.7379488982)
                Line((-0.4, 2.135), (-0.4, 10))
                Line((-0.4, 10), (-8.2133365563, 10))
                Line((-8.2133365563, 10), (-8.2133365563, -5))
                Line((-8.2133365563, -5), (7.1297054919, -7.7222683835))
                Line((7.1297054919, -7.7222683835), (8.7749769371, 1.5506854212))
                Line((9, 10), (8.7749769371, 1.5506854212))
                Line((0.4, 10), (9, 10))
                Line((0.4, 2.135), (0.4, 10))
                CenterArc((0.8, 2.135), 0.4, 180, 68.7379488982)
            make_face()
        # OneSide extrude, distance=-2
        extrude(amount=-2, mode=Mode.SUBTRACT)

        # Sketch2 -> Extrude4 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 20 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 255.8673459568, perimeter: 92.0303014993
            with BuildLine():
                CenterArc((0, 0), 1.88, 69.3053219304, 0.3066783172)
                CenterArc((0, 0), 1.88, 110.6946780696, 318.6106438608)
                CenterArc((0, 0), 1.88, 110.3879997524, 0.3066783172)
                CenterArc((-0.8, 2.135), 0.4, -68.7379488982, 68.7379488982)
                Line((-0.4, 2.135), (-0.4, 10))
                Line((-0.4, 10), (-8.2133365563, 10))
                Line((-8.2133365563, 10), (-8.2133365563, -5))
                Line((-8.2133365563, -5), (7.1297054919, -7.7222683835))
                Line((7.1297054919, -7.7222683835), (8.7749769371, 1.5506854212))
                Line((9, 10), (8.7749769371, 1.5506854212))
                Line((0.4, 10), (9, 10))
                Line((0.4, 2.135), (0.4, 10))
                CenterArc((0.8, 2.135), 0.4, 180, 68.7379488982)
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a waist bag or fanny pack with an elongated, curved oval shape featuring ventilation mesh panels on the sides and top, and a structured base with flanged edges for durability and support.
def model_42429_a80ffa77_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 16 constraints, 10 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.925778968, perimeter: 13.2045487487
            with BuildLine():
                CenterArc((0, 0), 1.0625932035, -152.4922204503, 35.1176987839)
                Line((0.4885856093, -0.9436039522), (-0.4885856093, -0.9436039522))
                CenterArc((0, 0), 1.0625932035, -62.6254783336, 33.1470680931)
                Line((0.925031147, 0.5228974022), (0.925031147, -0.5228974022))
                CenterArc((0, 0), 1.0625932035, 29.4784102405, 39.1073836254)
                Line((-0.3879608784, 0.9892374199), (0.3879608784, 0.9892374199))
                CenterArc((0, 0), 1.0625932035, 111.414206134, 41.0780143163)
                Line((-0.9424650541, -0.4907789094), (-0.9424650541, 0.4907789094))
            make_face()
            with BuildLine():
                CenterArc((0.6096, -0.6096), 0.11303, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0.6096, 0.6096), 0.11303, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-0.6096, 0.6096), 0.11303, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-0.6096, -0.6096), 0.11303, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0, 0), 0.6096, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.1524
        extrude(amount=0.1524)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 16 constraints, 10 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.1674540318, perimeter: 3.8302297633
            Circle(0.6096)
        # OneSide extrude, distance=0.3048
        extrude(amount=0.3048, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.2667686977, perimeter: 3.9898226701
            Circle(0.635)
        # OneSide extrude, distance=-0.0762
        extrude(amount=-0.0762, mode=Mode.ADD)
    return part.part


# Description: This is a hexagonal or octagonal prism-shaped cutting tool or insert, featuring a elongated body with beveled or chamfered edges and a tapered end, commonly used as a lathe tool bit or cutting insert in machining operations.
def model_42567_5ec3afc1_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch11 -> Extrude10 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1070.0604423017, perimeter: 156.4851156401
            with BuildLine():
                Line((55, -30.578539249), (55, 30))
                Line((55, 30), (37.3359814289, 30))
                Line((37.3359814289, 30), (37.3359814289, -30.578539249))
                Line((37.3359814289, -30.578539249), (55, -30.578539249))
            make_face()
        # OneSide extrude, distance=10
        extrude(amount=10)

        # Sketch12 -> Extrude11 (Join)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 30.578539249), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1.5393804003, perimeter: 4.398229715
            with Locations((42, 6)):
                Circle(0.7)
        # OneSide extrude, distance=1.4
        extrude(amount=1.4, mode=Mode.ADD)

        # Sketch13 -> Extrude12 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 31.978539249), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.3848451001, perimeter: 2.1991148575
            with Locations((42, 6)):
                Circle(0.35)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)
    return part.part


# Description: A dumbbell consisting of a cylindrical handle shaft with circular weighted plates or flanges fixed at each end, designed for strength training exercises.
def model_42586_517832f9_0000():
    """Model: WheelRod"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 5.067074791, perimeter: 7.9796453401
            Circle(1.27)
        # OneSide extrude, distance=11.43
        extrude(amount=11.43)

        # Sketch3 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 15.2012243729, perimeter: 23.9389360204
            with BuildLine():
                CenterArc((0, 0), 2.54, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.27, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 5.067074791, perimeter: 7.9796453401
            Circle(1.27)
        # OneSide extrude, distance=1.27
        extrude(amount=1.27, mode=Mode.ADD)

        # Sketch2 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 11.43, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 15.2012243729, perimeter: 23.9389360204
            with BuildLine():
                CenterArc((0, 0), 2.54, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.27, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 5.067074791, perimeter: 7.9796453401
            Circle(1.27)
        # OneSide extrude, distance=1.27
        extrude(amount=1.27, mode=Mode.ADD)
    return part.part


# Description: This is a stamped steel mounting bracket with a rectangular U-shaped frame featuring two angled legs with mounting flanges at the base, designed to attach components at a fixed offset distance.
def model_42586_517832f9_0027():
    """Model: Handle"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 13 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.6129, perimeter: 5.08
            with BuildLine():
                Line((-6.9849999046, 0.635), (-5.7149999046, 0.635))
                Line((-6.9849999046, -0.635), (-6.9849999046, 0.635))
                Line((-5.7149999046, -0.635), (-6.9849999046, -0.635))
                Line((-5.7149999046, 0.635), (-5.7149999046, -0.635))
            make_face()
            # Profile area: 1.6129, perimeter: 5.08
            with BuildLine():
                Line((3.1749999428, 0.635), (3.1749999428, -0.635))
                Line((4.4449999428, -0.635), (3.1749999428, -0.635))
                Line((4.4449999428, 0.635), (4.4449999428, -0.635))
                Line((3.1749999428, 0.635), (4.4449999428, 0.635))
            make_face()
        # OneSide extrude, distance=-7.62
        extrude(amount=-7.62)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 13 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.6129, perimeter: 5.08
            with BuildLine():
                Line((-6.9849999046, 0.635), (-5.7149999046, 0.635))
                Line((-6.9849999046, -0.635), (-6.9849999046, 0.635))
                Line((-5.7149999046, -0.635), (-6.9849999046, -0.635))
                Line((-5.7149999046, 0.635), (-5.7149999046, -0.635))
            make_face()
            # Profile area: 1.6129, perimeter: 5.08
            with BuildLine():
                Line((3.1749999428, 0.635), (3.1749999428, -0.635))
                Line((4.4449999428, -0.635), (3.1749999428, -0.635))
                Line((4.4449999428, 0.635), (4.4449999428, -0.635))
                Line((3.1749999428, 0.635), (4.4449999428, 0.635))
            make_face()
            # Profile area: 11.2902998062, perimeter: 20.3199996948
            with BuildLine():
                Line((-5.7149999046, 0.635), (-5.7149999046, -0.635))
                Line((3.1749999428, -0.635), (-5.7149999046, -0.635))
                Line((3.1749999428, 0.635), (3.1749999428, -0.635))
                Line((-5.7149999046, 0.635), (3.1749999428, 0.635))
            make_face()
        # OneSide extrude, distance=1.27
        extrude(amount=1.27, mode=Mode.ADD)

        # Sketch2 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 9 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -7.62, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 6.4516, perimeter: 12.7
            with BuildLine():
                Line((8.2549999428, -0.635), (8.2549999428, 0.635))
                Line((8.2549999428, 0.635), (3.1749999428, 0.635))
                Line((3.1749999428, -0.635), (3.1749999428, 0.635))
                Line((3.1749999428, -0.635), (8.2549999428, -0.635))
            make_face()
            # Profile area: 4.8387, perimeter: 10.16
            with BuildLine():
                Line((-10.7949999046, -0.635), (-10.7949999046, 0.635))
                Line((-6.9849999046, -0.635), (-10.7949999046, -0.635))
                Line((-6.9849999046, 0.635), (-6.9849999046, -0.635))
                Line((-10.7949999046, 0.635), (-6.9849999046, 0.635))
            make_face()
            # Profile area: 1.6129, perimeter: 5.08
            with BuildLine():
                Line((-5.7149999046, -0.635), (-6.9849999046, -0.635))
                Line((-5.7149999046, 0.635), (-5.7149999046, -0.635))
                Line((-6.9849999046, 0.635), (-5.7149999046, 0.635))
                Line((-6.9849999046, 0.635), (-6.9849999046, -0.635))
            make_face()
        # OneSide extrude, distance=1.27
        extrude(amount=1.27, mode=Mode.ADD)

        # Sketch3 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -7.62, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.8107319666, perimeter: 3.191858136
            with Locations((-6.9849999428, 0.0014200177)):
                Circle(0.508)
            # Profile area: 0.8107319666, perimeter: 3.191858136
            with Locations((9.5249999046, 0.0031810839)):
                Circle(0.508)
        # OneSide extrude, distance=-2.032
        extrude(amount=-2.032, mode=Mode.SUBTRACT)
    return part.part


# Description: This is an L-shaped bracket or angle iron with a vertical flange featuring an X-pattern cutout and a horizontal leg with two oval mounting holes.
def model_42601_bfe96b47_0011():
    """Model: Guy Tab v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 6 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 12.9739382907, perimeter: 44.4464609691
            with BuildLine():
                Line((0, 0), (0.6, 0))
                Line((0.6, 0), (0.6, 13.6392304845))
                Line((4.5116152423, 20.4143468238), (0.6, 13.6392304845))
                Line((3.992, 20.7143468238), (4.5116152423, 20.4143468238))
                Line((0, 13.8), (3.992, 20.7143468238))
                Line((0, 0), (0, 13.8))
            make_face()
        # OneSide extrude, distance=5
        extrude(amount=5)

        # Sketch3 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 3.45, 5.9755752861), x_dir=(1, 0, 0), z_dir=(0, 0.5, 0.8660254038))):
            # Profile area: 3.1730871199, perimeter: 6.3146012337
            with Locations((2.4457722014, 16.0981505722)):
                Circle(1.005)
        # OneSide extrude, distance=-7
        extrude(amount=-7, mode=Mode.SUBTRACT)

        # Sketch2 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 3.1730871199, perimeter: 6.3146012337
            with Locations((2.5, 4.32)):
                Circle(1.005)
            # Profile area: 3.1730871199, perimeter: 6.3146012337
            with Locations((2.5, 11.82)):
                Circle(1.005)
        # OneSide extrude, distance=-5
        extrude(amount=-5, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical rivet nut (threaded insert) with a flanged head at one end and a hollow barrel body designed for installation into thin materials.
def model_42811_6a61f75c_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            Circle(0.4)
        # OneSide extrude, distance=0.15
        extrude(amount=0.15)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.15), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            Circle(0.3)
        # OneSide extrude, distance=1.2
        extrude(amount=1.2, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.2165063509, perimeter: 1.7320508076
            with BuildLine():
                Line((0.25, -0.1443375673), (0.25, 0.1443375673))
                Line((0.25, 0.1443375673), (0, 0.2886751346))
                Line((0, 0.2886751346), (-0.25, 0.1443375673))
                Line((-0.25, 0.1443375673), (-0.25, -0.1443375673))
                Line((-0.25, -0.1443375673), (0, -0.2886751346))
                Line((0, -0.2886751346), (0.25, -0.1443375673))
            make_face()
        # OneSide extrude, distance=-0.1
        extrude(amount=-0.1, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a shoulder bolt (or shoulder screw) featuring a cylindrical shaft with a larger diameter undercut shoulder and a flanged base, designed for pivot or hinge applications.
def model_42811_82a43e7c_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            Circle(0.3)
        # OneSide extrude, distance=0.15
        extrude(amount=0.15)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.15, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            Circle(0.2)
        # OneSide extrude, distance=1.2
        extrude(amount=1.2, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.1385640646, perimeter: 1.3856406461
            with BuildLine():
                Line((0.1154700538, -0.2), (0.2309401077, 0))
                Line((0.2309401077, 0), (0.1154700538, 0.2))
                Line((0.1154700538, 0.2), (-0.1154700538, 0.2))
                Line((-0.1154700538, 0.2), (-0.2309401077, 0))
                Line((-0.2309401077, 0), (-0.1154700538, -0.2))
                Line((-0.1154700538, -0.2), (0.1154700538, -0.2))
            make_face()
        # OneSide extrude, distance=-0.1
        extrude(amount=-0.1, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a parallelogram-shaped structural frame or bracket with a large central oval opening, featuring blue reinforcing ribs along the perimeter and small circular holes at the corners.
def model_43009_6aa4e085_0022():
    """Model: gasket of water outlet/inlet housing"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 15.3162, perimeter: 15.66
            with BuildLine():
                Line((2.7100000104, -2.5050000089), (2.7100000104, 1.3049999911))
                Line((2.7100000104, 1.3049999911), (-1.3099999896, 1.3049999911))
                Line((-1.3099999896, 1.3049999911), (-1.3099999896, -2.5050000089))
                Line((-1.3099999896, -2.5050000089), (2.7100000104, -2.5050000089))
            make_face()
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            with Locations((0.7000000104, 0.6000000089)):
                Circle(1)
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((1.9500000104, 1.8500000089)):
                Circle(0.25)
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((1.9500000104, -0.6499999911)):
                Circle(0.25)
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((-0.5499999896, -0.6499999911)):
                Circle(0.25)
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((-0.5499999896, 1.8500000089)):
                Circle(0.25)
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical rod or pin with a tapered end, featuring a uniform round shaft that gradually narrows to a pointed tip.
def model_43280_cfba044a_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch5 -> Extrude3 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane.XY) as sk:
            # Profile area: 0.8842630439, perimeter: 3.3334632337
            Circle(0.5305371513)
        # TwoSides extrude, along=15, against=-1
        extrude(amount=15)
        extrude(sk.sketch, amount=-1)
    return part.part


# Description: This is a cylindrical mesh or perforated filter component with an oval or elliptical cross-section, featuring a solid lower half and an open mesh/latticed upper half with a central rectangular opening or slot.
def model_43529_4804941b_0001():
    """Model: Solid45_arandela gruesa"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.428136962, perimeter: 8.2309727524
            with BuildLine():
                CenterArc((0, 0), 0.95, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.36, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.4071504079, perimeter: 2.2619467106
            Circle(0.36)
        # OneSide extrude, distance=0.78
        extrude(amount=0.78)

        # Sketch1 -> Extrude2 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.4071504079, perimeter: 2.2619467106
            Circle(0.36)
        # OneSide extrude, distance=0.16
        extrude(amount=0.16, mode=Mode.SUBTRACT)

        # Sketch2 -> Extrude3 (Cut)
        # Sketch on Profile plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2042820623, perimeter: 1.6022122533
            Circle(0.255)
        # OneSide extrude, distance=0.8
        extrude(amount=0.8, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.78, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.4384101659, perimeter: 4.4440969678
            with BuildLine():
                CenterArc((0, 0), 0.4523, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.255, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.03
        extrude(amount=0.03, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical connector or coupling with a stepped diameter design, featuring two different-sized tubular sections joined together at an offset angle.
def model_43529_4804941b_0034():
    """Model: Solid50_tubito"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.3848451001, perimeter: 2.1991148575
            Circle(0.35)
        # OneSide extrude, distance=1.555
        extrude(amount=1.555)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.555, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2290221044, perimeter: 1.6964600329
            Circle(0.27)
        # OneSide extrude, distance=0.175
        extrude(amount=0.175, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.73, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1558229956, perimeter: 3.8955748905
            with BuildLine():
                CenterArc((0, 0), 0.35, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.27, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.2290221044, perimeter: 1.6964600329
            Circle(0.27)
        # OneSide extrude, distance=0.73
        extrude(amount=0.73, mode=Mode.ADD)
    return part.part


MODELS = {
    "model_39306_ee445998_0006": {"func": model_39306_ee445998_0006, "volume": 124.0182522958, "area": 311.8849555922},
    "model_39306_ee445998_0025": {"func": model_39306_ee445998_0025, "volume": 0.1608136221, "area": 2.1134823489},
    "model_39306_ee445998_0027": {"func": model_39306_ee445998_0027, "volume": 4937.5, "area": 10330},
    "model_39306_ee445998_0031": {"func": model_39306_ee445998_0031, "volume": 0.4313692958, "area": 5.0498132084},
    "model_39389_d641313f_0063": {"func": model_39389_d641313f_0063, "volume": 4.1280527468, "area": 15.3938040026},
    "model_39390_61cd2601_0001": {"func": model_39390_61cd2601_0001, "volume": 3.272282908, "area": 13.2198218863},
    "model_39390_61cd2601_0005": {"func": model_39390_61cd2601_0005, "volume": 4.5878517403, "area": 44.3919984986},
    "model_39850_b2aa4f1e_0009": {"func": model_39850_b2aa4f1e_0009, "volume": 7.6814363726, "area": 33.9850877724},
    "model_40064_137c5d61_0001": {"func": model_40064_137c5d61_0001, "volume": 21.2371381076, "area": 106.5025358946},
    "model_40070_be9c502b_0013": {"func": model_40070_be9c502b_0013, "volume": 37.1819313946, "area": 63.4682181357},
    "model_40072_b44084ae_0013": {"func": model_40072_b44084ae_0013, "volume": 0.5937610351, "area": 5.6548668832},
    "model_40072_b44084ae_0016": {"func": model_40072_b44084ae_0016, "volume": 9.4247779608, "area": 25.1327412287},
    "model_40074_4615c9d1_0002": {"func": model_40074_4615c9d1_0002, "volume": 181.4269757448, "area": 403.6946559863},
    "model_40074_4615c9d1_0003": {"func": model_40074_4615c9d1_0003, "volume": 1546.4197364379, "area": 851.8047398814},
    "model_40074_4615c9d1_0011": {"func": model_40074_4615c9d1_0011, "volume": 113.0973355292, "area": 263.8937829015},
    "model_40074_4615c9d1_0012": {"func": model_40074_4615c9d1_0012, "volume": 27.4433826254, "area": 93.1953460687},
    "model_40159_583632c6_0002": {"func": model_40159_583632c6_0002, "volume": 1.5873572784, "area": 12.5279452128},
    "model_40417_b8d98f73_0016": {"func": model_40417_b8d98f73_0016, "volume": 242, "area": 1074},
    "model_40623_278320ef_0000": {"func": model_40623_278320ef_0000, "volume": 485.2981764749, "area": 2814.147438649},
    "model_40782_3383cd58_0009": {"func": model_40782_3383cd58_0009, "volume": 0.8914269155, "area": 7.8696895972},
    "model_40800_7fa2d7a5_0000": {"func": model_40800_7fa2d7a5_0000, "volume": 2.1893066908, "area": 15.1858948455},
    "model_40815_80519d37_0000": {"func": model_40815_80519d37_0000, "volume": 24.5473089614, "area": 154.8130346733},
    "model_40999_cad6be09_0004": {"func": model_40999_cad6be09_0004, "volume": 344.4562431529, "area": 348.9026216548},
    "model_41031_57b1ef09_0013": {"func": model_41031_57b1ef09_0013, "volume": 0.6480088406, "area": 14.8767657625},
    "model_41113_e7d93a39_0000": {"func": model_41113_e7d93a39_0000, "volume": 44.5992811985, "area": 374.3628330588},
    "model_41125_711db4bf_0010": {"func": model_41125_711db4bf_0010, "volume": 0.2505311596, "area": 5.2256858151},
    "model_41128_ee74f244_0011": {"func": model_41128_ee74f244_0011, "volume": 4.9567032074, "area": 20.4573476978},
    "model_41128_ee74f244_0012": {"func": model_41128_ee74f244_0012, "volume": 3.6557558678, "area": 16.6545973849},
    "model_41128_ee74f244_0013": {"func": model_41128_ee74f244_0013, "volume": 0.3005403053, "area": 3.3982615983},
    "model_41142_1bf94ee2_0013": {"func": model_41142_1bf94ee2_0013, "volume": 23.5736171573, "area": 68.6557096991},
    "model_41227_90e1c07c_0016": {"func": model_41227_90e1c07c_0016, "volume": 2271.3336398204, "area": 1483.1428879166},
    "model_41229_16283ae1_0017": {"func": model_41229_16283ae1_0017, "volume": 10.0652067069, "area": 64.8264231599},
    "model_41234_74275eb0_0000": {"func": model_41234_74275eb0_0000, "volume": 41.9696687916, "area": 135.8985420337},
    "model_41234_74275eb0_0001": {"func": model_41234_74275eb0_0001, "volume": 1072.1814676375, "area": 1102.2470169004},
    "model_41234_74275eb0_0002": {"func": model_41234_74275eb0_0002, "volume": 128.2811185693, "area": 461.746149582},
    "model_41234_74275eb0_0005": {"func": model_41234_74275eb0_0005, "volume": 27.3044898894, "area": 89.7986994457},
    "model_41234_74275eb0_0012": {"func": model_41234_74275eb0_0012, "volume": 42.6331005226, "area": 139.9779411007},
    "model_41234_74275eb0_0014": {"func": model_41234_74275eb0_0014, "volume": 42.6331005226, "area": 139.3445567518},
    "model_41319_418c7ab8_0000": {"func": model_41319_418c7ab8_0000, "volume": 51.5160332715, "area": 155.7944867743},
    "model_41353_16ac5969_0003": {"func": model_41353_16ac5969_0003, "volume": 23.9633284918, "area": 255.4186179918},
    "model_41353_16ac5969_0017": {"func": model_41353_16ac5969_0017, "volume": 353.7054756887, "area": 605.9634954085},
    "model_41501_b627682a_0028": {"func": model_41501_b627682a_0028, "volume": 1.283340601, "area": 7.257079042},
    "model_41593_d3d842f7_0005": {"func": model_41593_d3d842f7_0005, "volume": 85.073771922, "area": 708.0208373673},
    "model_41599_f66b4e5b_0010": {"func": model_41599_f66b4e5b_0010, "volume": 0.0003533498, "area": 0.0310338084},
    "model_41599_f66b4e5b_0012": {"func": model_41599_f66b4e5b_0012, "volume": 6.089119436, "area": 32.0903530765},
    "model_41624_a15f83c1_0026": {"func": model_41624_a15f83c1_0026, "volume": 1.2180862562, "area": 15.3238934212},
    "model_41648_577daf16_0004": {"func": model_41648_577daf16_0004, "volume": 40.0153409175, "area": 108.4058265741},
    "model_41650_9417da80_0002": {"func": model_41650_9417da80_0002, "volume": 0.1792135766, "area": 4.3457286943},
    "model_41650_9417da80_0008": {"func": model_41650_9417da80_0008, "volume": 0.0304292046, "area": 1.031415951},
    "model_41650_9417da80_0013": {"func": model_41650_9417da80_0013, "volume": 0.0383650472, "area": 1.304380586},
    "model_41672_5364f9b6_0000": {"func": model_41672_5364f9b6_0000, "volume": 1.2547964525, "area": 9.9792918944},
    "model_41693_a737c734_0006": {"func": model_41693_a737c734_0006, "volume": 39.4219188153, "area": 192.9044744323},
    "model_41699_b8a7150b_0000": {"func": model_41699_b8a7150b_0000, "volume": 3.162798404, "area": 12.8491139532},
    "model_41737_3696185a_0000": {"func": model_41737_3696185a_0000, "volume": 7.280423141, "area": 34.3961378218},
    "model_41739_1bc15d9f_0008": {"func": model_41739_1bc15d9f_0008, "volume": 59.1843718807, "area": 131.2692185065},
    "model_41753_9b4f8d8a_0008": {"func": model_41753_9b4f8d8a_0008, "volume": 3.7778224278, "area": 30.5362363999},
    "model_41757_c1173a7e_0003": {"func": model_41757_c1173a7e_0003, "volume": 123.8129581167, "area": 374.9635323329},
    "model_41757_c1173a7e_0007": {"func": model_41757_c1173a7e_0007, "volume": 547.26313062, "area": 556.3305952125},
    "model_41759_269be149_0000": {"func": model_41759_269be149_0000, "volume": 0.0006534423, "area": 0.5922878787},
    "model_41759_77eaa071_0000": {"func": model_41759_77eaa071_0000, "volume": 0.0137366136, "area": 0.3809180992},
    "model_41759_9ee337cf_0000": {"func": model_41759_9ee337cf_0000, "volume": 0.0106356687, "area": 0.4419176779},
    "model_41785_e22ea270_0000": {"func": model_41785_e22ea270_0000, "volume": 1.447307311, "area": 8.4340798224},
    "model_41852_ca66b6b4_0004": {"func": model_41852_ca66b6b4_0004, "volume": 0.0079064102, "area": 0.6299497335},
    "model_41859_173a686e_0004": {"func": model_41859_173a686e_0004, "volume": 0.1714373327, "area": 3.4531028699},
    "model_41859_173a686e_0007": {"func": model_41859_173a686e_0007, "volume": 0.2372841207, "area": 3.7494583536},
    "model_41859_173a686e_0010": {"func": model_41859_173a686e_0010, "volume": 0.028233419, "area": 1.3464590465},
    "model_41896_7d8659e6_0003": {"func": model_41896_7d8659e6_0003, "volume": 1.4915788612, "area": 15.9459056544},
    "model_41896_7d8659e6_0009": {"func": model_41896_7d8659e6_0009, "volume": 0.0814974642, "area": 1.3683450226},
    "model_41924_ac7400c0_0003": {"func": model_41924_ac7400c0_0003, "volume": 0.2673503482, "area": 2.6944672543},
    "model_41982_f75ceb8f_0010": {"func": model_41982_f75ceb8f_0010, "volume": 64.4000007123, "area": 553.1000020191},
    "model_41982_f75ceb8f_0016": {"func": model_41982_f75ceb8f_0016, "volume": 5.4553088099, "area": 61.3655059458},
    "model_41982_f75ceb8f_0026": {"func": model_41982_f75ceb8f_0026, "volume": 0.3510729807, "area": 3.4714599215},
    "model_41985_727bc619_0000": {"func": model_41985_727bc619_0000, "volume": 0.1889680594, "area": 2.7995681426},
    "model_41998_654ac923_0007": {"func": model_41998_654ac923_0007, "volume": 0.2513274183, "area": 3.2672564346},
    "model_42005_1f6ccfca_0000": {"func": model_42005_1f6ccfca_0000, "volume": 1.4576989913, "area": 15.3309721495},
    "model_42143_51b31600_0002": {"func": model_42143_51b31600_0002, "volume": 131.8590515617, "area": 177.0629378272},
    "model_42333_53c85dac_0020": {"func": model_42333_53c85dac_0020, "volume": 1.187619146, "area": 17.9276512956},
    "model_42429_a80ffa77_0000": {"func": model_42429_a80ffa77_0000, "volume": 0.7458564784, "area": 8.5028637164},
    "model_42567_5ec3afc1_0000": {"func": model_42567_5ec3afc1_0000, "volume": 10702.9519781277, "area": 3712.2291200344},
    "model_42586_517832f9_0000": {"func": model_42586_517832f9_0000, "volume": 109.3981447371, "area": 202.682991639},
    "model_42586_517832f9_0027": {"func": model_42586_517832f9_0027, "volume": 57.3438475588, "area": 195.1865910242},
    "model_42601_bfe96b47_0011": {"func": model_42601_bfe96b47_0011, "volume": 59.1581346377, "area": 240.5079409279},
    "model_42811_6a61f75c_0000": {"func": model_42811_6a61f75c_0000, "volume": 0.3930395952, "area": 3.8174525589},
    "model_42811_82a43e7c_0000": {"func": model_42811_82a43e7c_0000, "volume": 0.1793515417, "area": 2.4947585548},
    "model_43009_6aa4e085_0022": {"func": model_43009_6aa4e085_0022, "volume": 1.1389209183, "area": 25.6010554275},
    "model_43280_cfba044a_0000": {"func": model_43280_cfba044a_0000, "volume": 14.1482087023, "area": 55.1039378264},
    "model_43529_4804941b_0001": {"func": model_43529_4804941b_0001, "volume": 2.0328775096, "area": 11.4064569075},
    "model_43529_4804941b_0034": {"func": model_43529_4804941b_0034, "volume": 0.9194499219, "area": 6.4031941465},
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
