"""Batch 002 - passing/08_21plus
20 models bundled from Fusion360 Gallery reconstructions.
"""

from build123d import *


def model_28446_d757d32d_0017():
    """Model: gumaDrzwiLodowka v6"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 12 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 499.2, perimeter: 499.2
            with BuildLine():
                Line((0.8, -79.2), (0.8, -0.8))
                Line((51.2, -79.2), (0.8, -79.2))
                Line((51.2, -0.8), (51.2, -79.2))
                Line((0.8, -0.8), (51.2, -0.8))
            make_face()
            with BuildLine():
                Line((2.8, -2.8), (49.2, -2.8))
                Line((49.2, -2.8), (49.2, -77.2))
                Line((49.2, -77.2), (2.8, -77.2))
                Line((2.8, -77.2), (2.8, -2.8))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(51.2, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 31.36, perimeter: 157.6
            with BuildLine():
                Line((-79.2, 0.7), (-0.8, 0.7))
                Line((-79.2, 0.3), (-79.2, 0.7))
                Line((-79.2, 0.3), (-0.8, 0.3))
                Line((-0.8, 0.3), (-0.8, 0.7))
            make_face()
        # OneSide extrude, distance=-0.8
        extrude(amount=-0.8, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 79.2), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 19.84, perimeter: 100
            with BuildLine():
                Line((50.4, 0.3), (0.8, 0.3))
                Line((50.4, 0.3), (50.4, 0.7))
                Line((50.4, 0.7), (0.8, 0.7))
                Line((0.8, 0.7), (0.8, 0.3))
            make_face()
        # OneSide extrude, distance=-0.8
        extrude(amount=-0.8, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.8, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 31.04, perimeter: 156
            with BuildLine():
                Line((78.4, 0.3), (0.8, 0.3))
                Line((78.4, 0.3), (78.4, 0.7))
                Line((78.4, 0.7), (0.8, 0.7))
                Line((0.8, 0.7), (0.8, 0.3))
            make_face()
        # OneSide extrude, distance=-0.8
        extrude(amount=-0.8, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.8), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 19.52, perimeter: 98.4
            with BuildLine():
                Line((-1.6, 0.3), (-50.4, 0.3))
                Line((-1.6, 0.3), (-1.6, 0.7))
                Line((-1.6, 0.7), (-50.4, 0.7))
                Line((-50.4, 0.7), (-50.4, 0.3))
            make_face()
        # OneSide extrude, distance=-0.8
        extrude(amount=-0.8, mode=Mode.SUBTRACT)

        # Sketch6 -> Extrude6 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(2.8, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 29.76, perimeter: 149.6
            with BuildLine():
                Line((-2.8, 0.3), (-77.2, 0.3))
                Line((-2.8, 0.3), (-2.8, 0.7))
                Line((-2.8, 0.7), (-77.2, 0.7))
                Line((-77.2, 0.7), (-77.2, 0.3))
            make_face()
        # OneSide extrude, distance=-0.8
        extrude(amount=-0.8, mode=Mode.SUBTRACT)

        # Sketch7 -> Extrude7 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 2.8), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 18.88, perimeter: 95.2
            with BuildLine():
                Line((2, 0.7), (2, 0.3))
                Line((2, 0.3), (2.8, 0.3))
                Line((2.8, 0.3), (49.2, 0.3))
                Line((49.2, 0.3), (49.2, 0.7))
                Line((2.8, 0.7), (49.2, 0.7))
                Line((2, 0.7), (2.8, 0.7))
            make_face()
        # OneSide extrude, distance=-0.8
        extrude(amount=-0.8, mode=Mode.SUBTRACT)

        # Sketch8 -> Extrude8 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(49.2, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 30.08, perimeter: 151.2
            with BuildLine():
                Line((2, 0.7), (2, 0.3))
                Line((2, 0.3), (2.8, 0.3))
                Line((2.8, 0.3), (77.2, 0.3))
                Line((77.2, 0.3), (77.2, 0.7))
                Line((2.8, 0.7), (77.2, 0.7))
                Line((2, 0.7), (2.8, 0.7))
            make_face()
        # OneSide extrude, distance=-0.8
        extrude(amount=-0.8, mode=Mode.SUBTRACT)

        # Sketch9 -> Extrude9 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 77.2), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 19.2, perimeter: 96.8
            with BuildLine():
                Line((-50, 0.7), (-50, 0.3))
                Line((-50, 0.3), (-49.2, 0.3))
                Line((-49.2, 0.3), (-2.8, 0.3))
                Line((-2.8, 0.3), (-2, 0.3))
                Line((-2, 0.3), (-2, 0.7))
                Line((-2.8, 0.7), (-2, 0.7))
                Line((-49.2, 0.7), (-2.8, 0.7))
                Line((-50, 0.7), (-49.2, 0.7))
            make_face()
        # OneSide extrude, distance=-0.8
        extrude(amount=-0.8, mode=Mode.SUBTRACT)

        # Sketch10 -> Extrude10 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 37.12, perimeter: 94.4
            with BuildLine():
                Line((-2.8, 78), (-2.8, 77.2))
                Line((-2.8, 78), (-49.2, 78))
                Line((-49.2, 78), (-49.2, 77.2))
                Line((-49.2, 77.2), (-2.8, 77.2))
            make_face()
        # OneSide extrude, distance=-10
        extrude(amount=-10, mode=Mode.SUBTRACT)
    return part.part


def model_28934_b02386fd_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            Circle(1)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.7671458676, perimeter: 4.7123889804
            Circle(0.75)
        # OneSide extrude, distance=-1.9
        extrude(amount=-1.9, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((4, 0)):
                Circle(0.5)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch5 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((-4, 0)):
                Circle(0.25)
        # OneSide extrude, distance=-1.1
        extrude(amount=-1.1, mode=Mode.SUBTRACT)

        # Sketch6 -> Extrude6 (Join)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.0375640893, perimeter: 11.7690711845
            with BuildLine():
                CenterArc((4, 0), 0.5, 89.5951942083, 180.0355966678)
                Line((4.0035325676, 0.4999875208), (0.2521016175, 0.967700767))
                CenterArc((0, 0), 1, -75.7383050369, 151.1363950351)
                Line((0.2463511231, -0.9691806458), (3.9967780649, -0.499989619))
            make_face()
        # OneSide extrude, distance=0.4
        extrude(amount=0.4, mode=Mode.ADD)

        # Sketch7 -> Extrude7 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.4, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.5981821242, perimeter: 5.4388036966
            with BuildLine():
                Line((-1.4394461519, -0.455530113), (-3.3383717488, -0.2808289581))
                CenterArc((-1.773657057, -0.0149793745), 0.5529754807, -52.8152935468, 119.6003893223)
                Line((-3.3383717488, 0.3040401258), (-1.5556846352, 0.493223248))
                Line((-3.3383717488, -0.2808289581), (-3.3383717488, 0.3040401258))
            make_face()
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2, mode=Mode.SUBTRACT)

        # Sketch9 -> Extrude8 (Join)
        # Sketch on XZ construction plane
        # Sketch has 8 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.36, perimeter: 3
            with BuildLine():
                Line((0.6062777706, -1.2975914203), (-0.5937222294, -1.2975914203))
                Line((0.6062777706, -0.9975914203), (0.6062777706, -1.2975914203))
                Line((-0.5937222294, -0.9975914203), (0.6062777706, -0.9975914203))
                Line((-0.5937222294, -1.2975914203), (-0.5937222294, -0.9975914203))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)

        # Sketch10 -> Extrude9 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.36, perimeter: 3
            with BuildLine():
                Line((-0.6256314001, 1.3046904249), (-0.6256314001, 1.0046904249))
                Line((-0.6256314001, 1.0046904249), (0.5743685999, 1.0046904249))
                Line((0.5743685999, 1.0046904249), (0.5743685999, 1.3046904249))
                Line((0.5743685999, 1.3046904249), (-0.6256314001, 1.3046904249))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch11 -> Extrude10 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-0.6256314001, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.0176714587, perimeter: 0.471238898
            with Locations((-1.1574436071, 0.2290776275)):
                Circle(0.075)
        # OneSide extrude, distance=-6
        extrude(amount=-6, mode=Mode.SUBTRACT)

        # Sketch12 -> Extrude11 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-0.5937222294, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.0176714587, perimeter: 0.471238898
            with Locations((1.1397170505, 0.25)):
                Circle(0.075)
        # OneSide extrude, distance=-9.8
        extrude(amount=-9.8, mode=Mode.SUBTRACT)
    return part.part


def model_31360_a1accb4b_0002():
    """Model: Crank_Web"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 16 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.8945892025, perimeter: 4.3600517531
            with BuildLine():
                Line((-0.0549493316, -0.2170061679), (0.626388487, -0.2739844821))
                CenterArc((0.65, 0), 0.275, -94.9254827679, 189.8509655357)
                Line((-0.0549493316, 0.2170061679), (0.626388487, 0.2739844821))
                Line((-0.0549493316, 0.2170061679), (-0.4035740443, 0.5095370357))
                CenterArc((0, 0), 0.65, 128.3806551214, 103.2386897573)
                Line((-0.0549493316, -0.2170061679), (-0.4035740443, -0.5095370357))
            make_face()
        # OneSide extrude, distance=0.4
        extrude(amount=0.4)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.4, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0883572934, perimeter: 1.4137166941
            with BuildLine():
                CenterArc((-0.65, 0), 0.175, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-0.65, 0), 0.05, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.245
        extrude(amount=0.245, mode=Mode.ADD)

        # Sketch5 -> Extrude4 (Cut)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))) as sk:
            # Profile area: 0.0078539816, perimeter: 0.3141592654
            with Locations((0, 0.2)):
                Circle(0.05)
        # TwoSides extrude, along=0.75, against=-0.1
        extrude(amount=0.75, mode=Mode.SUBTRACT)
        extrude(sk.sketch, amount=-0.1, mode=Mode.SUBTRACT)

        # Sketch6 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.4, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0078539816, perimeter: 0.3141592654
            with Locations((-0.65, 0)):
                Circle(0.05)
        # OneSide extrude, distance=-0.3
        extrude(amount=-0.3, mode=Mode.SUBTRACT)

        # Sketch7 -> Extrude6 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0078539816, perimeter: 0.3141592654
            Circle(0.05)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3, mode=Mode.SUBTRACT)

        # Sketch8 -> Extrude7 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.009817477, perimeter: 0.7853981634
            with BuildLine():
                CenterArc((0, 0), 0.075, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.05, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.01
        extrude(amount=-0.01, mode=Mode.SUBTRACT)

        # Sketch9 -> Extrude8 (Cut)
        # Sketch on BRepFace
        # Sketch has 8 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.1644798287, perimeter: 1.625683309
            with BuildLine():
                Line((-0.0919253332, 0.0771345132), (-0.3830222216, 0.3213938048))
                CenterArc((0, 0), 0.5, 140, 80)
                Line((-0.0919253332, -0.0771345132), (-0.3830222216, -0.3213938048))
                CenterArc((0, 0), 0.12, 140, 80)
            make_face()
        # OneSide extrude, distance=-0.08
        extrude(amount=-0.08, mode=Mode.SUBTRACT)

        # Sketch10 -> Extrude9 (Cut)
        # Sketch on BRepFace
        # Sketch has 11 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.2443933103, perimeter: 1.8996452113
            with BuildLine():
                CenterArc((0.65, 0), 0.2, -94.7803570599, 189.5607141198)
                Line((0.6333327586, 0.1993042977), (0.2674352883, 0.1687053516))
                CenterArc((0.2815436284, 0), 0.1692942436, 94.7803570599, 170.4392858802)
                Line((0.6333327586, -0.1993042977), (0.2674352883, -0.1687053516))
            make_face()
        # OneSide extrude, distance=-0.04
        extrude(amount=-0.04, mode=Mode.SUBTRACT)

        # Sketch11 -> Extrude10 (Cut)
        # Sketch on BRepFace
        # Sketch has 10 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.4, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0680899974, perimeter: 1.148703126
            with BuildLine():
                Line((-0.0877488913, 0.087528973), (-0.428556786, 0.1160297505))
                CenterArc((-0.65, 0), 0.25, -27.6532202498, 55.3064404997)
                Line((-0.0877488913, -0.087528973), (-0.428556786, -0.1160297505))
                CenterArc((-0.0907180108, -0.0520247015), 0.0356282046, -85.2196429401, 76.2314034617)
                CenterArc((0, 0), 0.08, 133.9548508789, 92.0902982421)
                CenterArc((-0.0907180108, 0.0520247015), 0.0356282046, 8.9882394784, 76.2314034617)
            make_face()
        # OneSide extrude, distance=-0.04
        extrude(amount=-0.04, mode=Mode.SUBTRACT)

        # Sketch12 -> Extrude11 (Join)
        # Sketch on BRepFace
        # Sketch has 11 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.04, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.0992986203, perimeter: 1.3362593225
            with BuildLine():
                CenterArc((0.2815436284, 0), 0.08, 94.6702360779, 170.6595278441)
                Line((0.2750299671, -0.0797343854), (0.6410437157, -0.1096347799))
                CenterArc((0.65, 0), 0.11, -94.6702360779, 189.3404721559)
                Line((0.2750299671, 0.0797343854), (0.6410437157, 0.1096347799))
            make_face()
        # OneSide extrude, distance=0.02
        extrude(amount=0.02, mode=Mode.ADD)

        # Sketch13 -> Extrude12 (Cut)
        # Sketch on BRepFace
        # Sketch has 15 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.02, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.0371806762, perimeter: 1.0045577382
            with BuildLine():
                Line((0.6459434969, 0.0498351762), (0.65, 0.05))
                Line((0.2801226808, 0.0349711439), (0.6459434969, 0.0498351762))
                CenterArc((0.2815436284, 0), 0.035, 92.3267623421, 175.3464753158)
                Line((0.2801226808, -0.0349711439), (0.6459434969, -0.0498351762))
                Line((0.6459434969, -0.0498351762), (0.65, -0.05))
                CenterArc((0.65, 0), 0.05, -90, 180)
            make_face()
        # OneSide extrude, distance=-0.01
        extrude(amount=-0.01, mode=Mode.SUBTRACT)

        # Sketch17 -> Extrude13 (Join)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))) as sk:
            # Profile area: 0.0392699082, perimeter: 1.5707963268
            with BuildLine():
                CenterArc((0, 0), 0.15, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # TwoSides extrude, along=0.1, against=-0.2
        extrude(amount=0.1, mode=Mode.ADD)
        extrude(sk.sketch, amount=-0.2, mode=Mode.ADD)

        # Sketch20 -> Extrude14 (Cut)
        # Sketch on BRepFace
        # Sketch has 10 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -0.2, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.001143812, perimeter: 0.150536051
            with BuildLine():
                Line((-0.0968245837, -0.025), (-0.1218245837, -0.025))
                CenterArc((0, 0), 0.1, 165.5224878141, 28.9550243719)
                Line((-0.1218245837, 0.025), (-0.0968245837, 0.025))
                Line((-0.1218245837, -0.025), (-0.1218245837, 0.025))
            make_face()
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2, mode=Mode.SUBTRACT)
    return part.part


def model_31667_a38ff7b3_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 14 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 16.3797492296, perimeter: 82.4186476549
            with BuildLine():
                Line((6.381891735, -7), (6, -7))
                Line((6.381891735, -7), (6.381891735, 7.4455403575))
                Line((6.381891735, 7.4455403575), (-6.381891735, 7.4455403575))
                Line((-6.381891735, 7.4455403575), (-6.381891735, -7))
                Line((-6.381891735, -7), (-6, -7))
                Line((-6, 7), (-6, -7))
                Line((6, 7), (-6, 7))
                Line((6, -7), (6, 7))
            make_face()
        # OneSide extrude, distance=22
        extrude(amount=22)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(6.381891735, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 55.4778297353, perimeter: 49.614134174
            with BuildLine():
                Line((-7, 22), (-7, 0))
                Line((-7, 0), (-1.9565609332, 22))
                Line((-1.9565609332, 22), (-7, 22))
            make_face()
        # OneSide extrude, distance=-27
        extrude(amount=-27, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 14 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -7), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 15.7853981634, perimeter: 19.1415926536
            with BuildLine():
                CenterArc((-3.5, 17.5), 0.5, 90, 90)
                Line((-4, 16.5), (-4, 17.5))
                CenterArc((-3.5, 16.5), 0.5, 180, 90)
                Line((3.5, 16), (-3.5, 16))
                CenterArc((3.5, 16.5), 0.5, -90, 90)
                Line((4, 17.5), (4, 16.5))
                CenterArc((3.5, 17.5), 0.5, 0, 90)
                Line((-3.5, 18), (3.5, 18))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 0, -7.4455403575), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 15.7853981634, perimeter: 19.1415926536
            with BuildLine():
                CenterArc((-3.5, 16.5), 0.5, 180, 90)
                Line((3.5, 16), (-3.5, 16))
                CenterArc((3.5, 16.5), 0.5, -90, 90)
                Line((4, 17.5), (4, 16.5))
                CenterArc((3.5, 17.5), 0.5, 0, 90)
                Line((-3.5, 18), (3.5, 18))
                CenterArc((-3.5, 17.5), 0.5, 90, 90)
                Line((-4, 16.5), (-4, 17.5))
            make_face()
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude5 (Cut)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 0, -7.4455403575), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 2.1028957673, perimeter: 5.1405999237
            with Locations((0, 19.4410679257)):
                Circle(0.8181518883)
        # OneSide extrude, distance=-1.5
        extrude(amount=-1.5, mode=Mode.SUBTRACT)

        # Sketch6 -> Extrude6 (Cut)
        # Sketch on BRepFace
        # Sketch has 15 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -7.4455403575), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 1.8948451001, perimeter: 5.3991148575
            with BuildLine():
                CenterArc((-2.35, 19.85), 0.35, -90, 90)
                Line((-2, 20.15), (-2, 19.85))
                CenterArc((-2.35, 20.15), 0.35, 0, 90)
                Line((-3.65, 20.5), (-2.35, 20.5))
                CenterArc((-3.65, 20.15), 0.35, 90, 90)
                Line((-4, 19.85), (-4, 20.15))
                CenterArc((-3.65, 19.85), 0.35, 180, 90)
                Line((-2.35, 19.5), (-3.65, 19.5))
            make_face()
        # OneSide extrude, distance=-1.9
        extrude(amount=-1.9, mode=Mode.SUBTRACT)

        # Sketch7 -> Extrude7 (Cut)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 0, -7.4455403575), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.0628318549, perimeter: 0.8885766009
            with Locations((-4.6000000685, 21.0000003129)):
                Circle(0.1414213583)
        # OneSide extrude, distance=-1.9
        extrude(amount=-1.9, mode=Mode.SUBTRACT)

        # Sketch8 -> Extrude8 (Cut)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 0, -7.4455403575), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            with Locations((0, 13)):
                Circle(1)
        # OneSide extrude, distance=-1.5
        extrude(amount=-1.5, mode=Mode.SUBTRACT)

        # Sketch9 -> Extrude9 (Cut)
        # Sketch on BRepFace
        # Sketch has 15 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -7.4455403575), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 13.5793804003, perimeter: 16.798229715
            with BuildLine():
                CenterArc((-0.3, 9.3), 0.7, 90, 90)
                Line((-1, 3.7), (-1, 9.3))
                CenterArc((-0.3, 3.7), 0.7, -180, 90)
                Line((0.3, 3), (-0.3, 3))
                CenterArc((0.3, 3.7), 0.7, -90, 90)
                Line((1, 9.3), (1, 3.7))
                CenterArc((0.3, 9.3), 0.7, 0, 90)
                Line((-0.3, 10), (0.3, 10))
            make_face()
        # OneSide extrude, distance=-2.5
        extrude(amount=-2.5, mode=Mode.SUBTRACT)

        # Sketch10 -> Extrude10 (Cut)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(6.381891735, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 5.1914659982, perimeter: 8.0769973236
            with Locations((2, 14)):
                Circle(1.2854940494)
        # OneSide extrude, distance=-22
        extrude(amount=-22, mode=Mode.SUBTRACT)

        # Sketch11 -> Extrude11 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(6.381891735, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 3.3328470271, perimeter: 18.4268609318
            with BuildLine():
                CenterArc((2, 14), 1.6472319536, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((2, 14), 1.2854940494, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.4
        extrude(amount=0.4, mode=Mode.ADD)

        # Sketch12 -> Extrude12 (Join)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(-6.381891735, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 3.3328470271, perimeter: 18.4268609318
            with BuildLine():
                CenterArc((-2, 14), 1.6472319536, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-2, 14), 1.2854940494, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.4
        extrude(amount=0.4, mode=Mode.ADD)

        # Sketch13 -> Extrude13 (NewBody)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(-6.381891735, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 1.9485571585, perimeter: 5.1961524227
            with BuildLine():
                Line((1.210176319, 20.4956305034), (0.4258595527, 20.8628459851))
                Line((0.4258595527, 20.8628459851), (-0.2843167664, 20.3672154817))
                Line((-0.2843167664, 20.3672154817), (-0.210176319, 19.5043694966))
                Line((-0.210176319, 19.5043694966), (0.5741404473, 19.1371540149))
                Line((0.5741404473, 19.1371540149), (1.2843167664, 19.6327845183))
                Line((1.2843167664, 19.6327845183), (1.210176319, 20.4956305034))
            make_face()
        # OneSide extrude, distance=0.7
        extrude(amount=0.7)
    return part.part


def model_34317_e9c65aa6_0015():
    """Model: Pillar2 v8"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 36, perimeter: 24
            with BuildLine():
                Line((0.325507682, -2.7871153852), (-5.674492318, -2.7871153852))
                Line((0.325507682, 3.2128846148), (0.325507682, -2.7871153852))
                Line((-5.674492318, 3.2128846148), (0.325507682, 3.2128846148))
                Line((-5.674492318, -2.7871153852), (-5.674492318, 3.2128846148))
            make_face()
        # OneSide extrude, distance=6.5
        extrude(amount=6.5)

        # Sketch3 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 6 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(6.5, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 36, perimeter: 24
            with BuildLine():
                Line((-5.674492318, -2.7871153852), (-5.674492318, 3.2128846148))
                Line((-5.674492318, 3.2128846148), (-11.674492318, 3.2128846148))
                Line((-11.674492318, 3.2128846148), (-11.674492318, -2.7871153852))
                Line((-11.674492318, -2.7871153852), (-5.674492318, -2.7871153852))
            make_face()
            # Profile area: 36, perimeter: 24
            with BuildLine():
                Line((0.325507682, -2.7871153852), (0.325507682, 3.2128846148))
                Line((6.325507682, -2.7871153852), (0.325507682, -2.7871153852))
                Line((6.325507682, 3.2128846148), (6.325507682, -2.7871153852))
                Line((0.325507682, 3.2128846148), (6.325507682, 3.2128846148))
            make_face()
        # OneSide extrude, distance=-20
        extrude(amount=-20, mode=Mode.ADD)

        # Sketch4 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 11.674492318), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 36, perimeter: 24
            with BuildLine():
                Line((-7.5, 3.2128846148), (-7.5, -2.7871153852))
                Line((-13.5, 3.2128846148), (-7.5, 3.2128846148))
                Line((-13.5, -2.7871153852), (-13.5, 3.2128846148))
                Line((-7.5, -2.7871153852), (-13.5, -2.7871153852))
            make_face()
        # OneSide extrude, distance=26.3548
        extrude(amount=26.3548, mode=Mode.ADD)

        # Sketch6 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -6.325507682), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 36, perimeter: 24
            with BuildLine():
                Line((13.5, -2.7871153852), (13.5, 3.2128846148))
                Line((13.5, 3.2128846148), (7.5, 3.2128846148))
                Line((7.5, 3.2128846148), (7.5, -2.7871153852))
                Line((7.5, -2.7871153852), (13.5, -2.7871153852))
            make_face()
        # OneSide extrude, distance=26.3548
        extrude(amount=26.3548, mode=Mode.ADD)

        # Sketch7 -> Extrude5 (Cut)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 36, perimeter: 24
            with BuildLine():
                Line((5.674492318, -2.7871153852), (-0.325507682, -2.7871153852))
                Line((5.674492318, 3.2128846148), (5.674492318, -2.7871153852))
                Line((-0.325507682, 3.2128846148), (5.674492318, 3.2128846148))
                Line((-0.325507682, -2.7871153852), (-0.325507682, 3.2128846148))
            make_face()
        # OneSide extrude, distance=-7
        extrude(amount=-7, mode=Mode.SUBTRACT)

        # Sketch8 -> Extrude6 (Join)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(6.5, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 36, perimeter: 24
            with BuildLine():
                Line((-5.674492318, -2.7871153852), (-5.674492318, 3.2128846148))
                Line((-5.674492318, 3.2128846148), (-11.674492318, 3.2128846148))
                Line((-11.674492318, 3.2128846148), (-11.674492318, -2.7871153852))
                Line((-11.674492318, -2.7871153852), (-5.674492318, -2.7871153852))
            make_face()
            # Profile area: 36, perimeter: 24
            with BuildLine():
                Line((6.325507682, -2.7871153852), (6.325507682, 3.2128846148))
                Line((6.325507682, 3.2128846148), (0.325507682, 3.2128846148))
                Line((0.325507682, 3.2128846148), (0.325507682, -2.7871153852))
                Line((0.325507682, -2.7871153852), (6.325507682, -2.7871153852))
            make_face()
        # OneSide extrude, distance=10
        extrude(amount=10, mode=Mode.ADD)

        # Sketch9 -> Extrude7 (Join)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -0.325507682), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 36, perimeter: 24
            with BuildLine():
                Line((16.5, -2.7871153852), (16.5, 3.2128846148))
                Line((16.5, 3.2128846148), (10.5, 3.2128846148))
                Line((10.5, 3.2128846148), (10.5, -2.7871153852))
                Line((10.5, -2.7871153852), (16.5, -2.7871153852))
            make_face()
        # OneSide extrude, distance=6
        extrude(amount=6, mode=Mode.ADD)

        # Sketch10 -> Extrude8 (Join)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(16.5, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 36, perimeter: 24
            with BuildLine():
                Line((0.325507682, 3.2128846148), (0.325507682, -2.7871153852))
                Line((-5.674492318, 3.2128846148), (0.325507682, 3.2128846148))
                Line((-5.674492318, -2.7871153852), (-5.674492318, 3.2128846148))
                Line((0.325507682, -2.7871153852), (-5.674492318, -2.7871153852))
            make_face()
        # OneSide extrude, distance=17
        extrude(amount=17, mode=Mode.ADD)

        # Sketch11 -> Extrude9 (Cut)
        # Sketch on BRepFace
        # Sketch has 8 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-13.5, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 1.5, perimeter: 12.5
            with BuildLine():
                Line((-0.325507682, -2.7871153852), (-0.325507682, 3.2128846148))
                Line((-0.325507682, 3.2128846148), (-0.575507682, 3.2128846148))
                Line((-0.575507682, 3.2128846148), (-0.575507682, -2.7871153852))
                Line((-0.575507682, -2.7871153852), (-0.325507682, -2.7871153852))
            make_face()
            # Profile area: 1.5, perimeter: 12.5
            with BuildLine():
                Line((5.924492318, -2.7871153852), (5.674492318, -2.7871153852))
                Line((5.924492318, 3.2128846148), (5.924492318, -2.7871153852))
                Line((5.674492318, 3.2128846148), (5.924492318, 3.2128846148))
                Line((5.674492318, -2.7871153852), (5.674492318, 3.2128846148))
            make_face()
        # OneSide extrude, distance=-24
        extrude(amount=-24, mode=Mode.SUBTRACT)

        # Sketch12 -> Extrude10 (Join)
        # Sketch on BRepFace
        # Sketch has 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 5.924492318), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 7.0685834706, perimeter: 9.4247779608
            with Locations((11.5257, 0)):
                Circle(1.5)
        # OneSide extrude, distance=6.5
        extrude(amount=6.5, mode=Mode.ADD)
    return part.part


def model_36088_1ea9c8a9_0003():
    """Model: Shaft"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.1441991028, perimeter: 3.2044245067
            with BuildLine():
                CenterArc((0, 0), 0.3, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.21, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.62
        extrude(amount=0.62)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.62, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.1021017612, perimeter: 4.0840704497
            with BuildLine():
                CenterArc((0, 0), 0.35, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.1441991028, perimeter: 3.2044245067
            with BuildLine():
                CenterArc((0, 0), 0.3, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.21, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.04
        extrude(amount=0.04, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0.66, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.2140209995, perimeter: 3.4243359924
            with BuildLine():
                CenterArc((0, 0), 0.335, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.21, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.09
        extrude(amount=0.09, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.75, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0322798645, perimeter: 4.3039819354
            with BuildLine():
                CenterArc((0, 0), 0.35, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.335, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.2140209995, perimeter: 3.4243359924
            with BuildLine():
                CenterArc((0, 0), 0.335, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.21, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.35
        extrude(amount=0.35, mode=Mode.ADD)

        # Sketch5 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(1.1, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.2513274123, perimeter: 5.0265482457
            with BuildLine():
                CenterArc((0, 0), 0.45, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.35, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.246300864, perimeter: 3.518583772
            with BuildLine():
                CenterArc((0, 0), 0.35, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.21, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.27
        extrude(amount=0.27, mode=Mode.ADD)

        # Sketch6 -> Extrude6 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(1.37, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.2297289628, perimeter: 6.1261056745
            with BuildLine():
                CenterArc((0, 0), 0.525, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.45, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.4976282763, perimeter: 4.1469023027
            with BuildLine():
                CenterArc((0, 0), 0.45, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.21, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.33
        extrude(amount=0.33, mode=Mode.ADD)

        # Sketch7 -> Extrude7 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(1.7, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.7273572391, perimeter: 4.6181412008
            with BuildLine():
                CenterArc((0, 0), 0.525, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.21, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.1071283095, perimeter: 1.9477874452
            with BuildLine():
                CenterArc((0, 0), 0.21, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.01
        extrude(amount=0.01, mode=Mode.ADD)

        # Sketch8 -> Extrude8 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(1.71, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.6047565858, perimeter: 3.4557519189
            with BuildLine():
                CenterArc((0, 0), 0.45, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.64
        extrude(amount=0.64, mode=Mode.ADD)

        # Sketch9 -> Extrude9 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(2.35, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.5494645551, perimeter: 3.3300882128
            with BuildLine():
                CenterArc((0, 0), 0.43, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.11
        extrude(amount=0.11, mode=Mode.ADD)

        # Sketch10 -> Extrude10 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(2.46, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0552920307, perimeter: 5.5292030703
            with BuildLine():
                CenterArc((0, 0), 0.45, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.43, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.5494645551, perimeter: 3.3300882128
            with BuildLine():
                CenterArc((0, 0), 0.43, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.11
        extrude(amount=0.11, mode=Mode.ADD)

        # Sketch11 -> Extrude11 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(2.57, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.3534291735, perimeter: 2.8274333882
            with BuildLine():
                CenterArc((0, 0), 0.35, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.35
        extrude(amount=0.35, mode=Mode.ADD)

        # Sketch12 -> Extrude12 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(2.92, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.321149309, perimeter: 2.7331856086
            with BuildLine():
                CenterArc((0, 0), 0.335, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.09
        extrude(amount=0.09, mode=Mode.ADD)

        # Sketch13 -> Extrude13 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(3.01, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0322798645, perimeter: 4.3039819354
            with BuildLine():
                CenterArc((0, 0), 0.35, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.335, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.321149309, perimeter: 2.7331856086
            with BuildLine():
                CenterArc((0, 0), 0.335, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.29
        extrude(amount=0.29, mode=Mode.ADD)
    return part.part


def model_36920_08b32825_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 8 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.5124723016, perimeter: 4.5553093477
            with BuildLine():
                CenterArc((0, 0), 0.475, 39.1667107161, 281.6665778723)
                CenterArc((0, 0), 0.475, -39.1667114116, 78.3334221277)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0502835459, perimeter: 1.562862677
            with BuildLine():
                CenterArc((0, 0), 0.475, -39.1667114116, 78.3334221277)
                Line((0.525, -0.3000000045), (0.3682729929, -0.3000000045))
                Line((0.525, 0.3), (0.525, -0.3000000045))
                Line((0.3682729966, 0.3), (0.525, 0.3))
            make_face()
        # Symmetric extrude, each_side=0.25
        extrude(amount=0.25, both=True)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.525, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.4671458654, perimeter: 6.9123889893
            with BuildLine():
                CenterArc((0, 0), 0.75, 0, 360)
            make_face()
            with BuildLine():
                Line((-0.3000000045, -0.25), (0.3, -0.25))
                Line((-0.3000000045, 0.25), (-0.3000000045, -0.25))
                Line((0.3, 0.25), (-0.3000000045, 0.25))
                Line((0.3, -0.25), (0.3, 0.25))
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.3000000022, perimeter: 2.2000000089
            with BuildLine():
                Line((0.3, -0.25), (0.3, 0.25))
                Line((0.3, 0.25), (-0.3000000045, 0.25))
                Line((-0.3000000045, 0.25), (-0.3000000045, -0.25))
                Line((-0.3000000045, -0.25), (0.3, -0.25))
            make_face()
        # OneSide extrude, distance=0.7
        extrude(amount=0.7, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(1.225, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.7775441818, perimeter: 10.3672557568
            with BuildLine():
                CenterArc((0, 0), 0.9, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.75, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 1.7671458676, perimeter: 4.7123889804
            Circle(0.75)
        # OneSide extrude, distance=0.35
        extrude(amount=0.35, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(1.575, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.5393804003, perimeter: 4.398229715
            Circle(0.7)
        # OneSide extrude, distance=2.6
        extrude(amount=2.6, mode=Mode.ADD)

        # Sketch5 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(4.175, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.6361725124, perimeter: 2.8274333882
            Circle(0.45)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)

        # Sketch6 -> Extrude6 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(4.375, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.3141592654, perimeter: 6.2831853072
            with BuildLine():
                CenterArc((0, 0), 0.55, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.45, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.6361725124, perimeter: 2.8274333882
            Circle(0.45)
        # OneSide extrude, distance=0.45
        extrude(amount=0.45, mode=Mode.ADD)

        # Sketch7 -> Extrude7 (Join)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(4.825, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.096211275, perimeter: 1.0995574288
            Circle(0.175)
        # OneSide extrude, distance=2.54
        extrude(amount=2.54, mode=Mode.ADD)

        # Sketch8 -> Extrude8 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(7.365, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.9144080233, perimeter: 6.1261056745
            with BuildLine():
                CenterArc((0, 0), 0.8, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.175, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.25
        extrude(amount=-0.25, mode=Mode.ADD)

        # Sketch9 -> Extrude9 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(7.115, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 1.4431691252, perimeter: 5.4977871438
            with BuildLine():
                CenterArc((0, 0), 0.7, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.175, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.15
        extrude(amount=0.15, mode=Mode.ADD)

        # Sketch10 -> Extrude10 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(7.365, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            Circle(0.5)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)

        # Sketch12 -> Extrude11 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.9199422087, perimeter: 5.5679634611
            with BuildLine():
                Line((8.0000001192, -0.3000000045), (8.7729577855, -0.4861081361))
                CenterArc((8.89, 0), 0.5, -103.5376591573, 207.0753183146)
                Line((8.0000001192, 0.3000000045), (8.7729577855, 0.4861081361))
                Line((8.0000001192, -0.3000000045), (8.0000001192, 0.3000000045))
            make_face()
            with BuildLine():
                CenterArc((8.89, 0), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.1256637061, perimeter: 2.5132741229
            with BuildLine():
                CenterArc((8.89, 0), 0.25, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((8.89, 0), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=0.2
        extrude(amount=0.2, both=True)
    return part.part


def model_38757_2c865215_0008():
    """Model: 1 Cuerpo"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 51 constraints, 10 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 27.6678495647, perimeter: 35.516368586
            with BuildLine():
                Line((-0.2096463575, 5.5), (0, 5.5))
                Line((0, 5.5), (0, 8))
                Line((-0.25, 8), (0, 8))
                CenterArc((-0.25, 9.25), 1.25, -180, 90)
                Line((-1.5, 15.75), (-1.5, 9.25))
                CenterArc((-0.25, 15.75), 1.25, 90, 90)
                Line((0, 17), (-0.25, 17))
                Line((0, 17), (0, 20.5))
                Line((0, 20.5), (-1.2, 20.5))
                CenterArc((-1.2, 18.7), 1.8, 90, 90)
                Line((-3, 18.7), (-3, 8.8430749028))
                CenterArc((-1.2, 8.8430749028), 1.8, 180, 50.1944289077)
                Line((-0.6476680806, 6.0397234005), (-2.3523319194, 7.4602765995))
                CenterArc((-1.8, 4.6569250972), 1.8, 27.9288623714, 22.2655665363)
            make_face()
            # Profile area: 440.0921721117, perimeter: 86.1881047629
            with BuildLine():
                CenterArc((5.6059722115, 19.25), 1.25, 55.0079798014, 34.9920201986)
                Line((5.6059722115, 20.5), (0, 20.5))
                Line((0, 17), (0, 20.5))
                Line((0.25, 17), (0, 17))
                CenterArc((0.25, 15.75), 1.25, 0, 90)
                Line((1.5, 9.25), (1.5, 15.75))
                CenterArc((0.25, 9.25), 1.25, -90, 90)
                Line((0, 8), (0.25, 8))
                Line((0, 5.5), (0, 8))
                Line((-0.2096463575, 5.5), (0, 5.5))
                CenterArc((-1.8, 4.6569250972), 1.8, 0, 27.9288623714)
                Line((0, 4.6569250972), (0, 1.8))
                CenterArc((1.8, 1.8), 1.8, -180, 90)
                Line((1.8, 0), (20.7, 0))
                CenterArc((20.7, 1.8), 1.8, -90, 90)
                Line((22.5, 1.8), (22.5, 18.7))
                CenterArc((20.7, 18.7), 1.8, 0, 90)
                Line((20.7, 20.5), (16.4570722347, 20.5))
                CenterArc((16.4570722347, 19.05), 1.45, 90, 34.9920201986)
                Line((15.6255518354, 20.2378862848), (15.3744481646, 20.0621137152))
                CenterArc((14.5429277653, 21.25), 1.45, -90, 34.9920201986)
                Line((14.5429277653, 19.8), (7.3940277885, 19.8))
                CenterArc((7.3940277885, 21.05), 1.25, -124.9920201986, 34.9920201986)
                Line((6.6771998581, 20.0259600994), (6.3228001419, 20.2740399006))
            make_face()
        # Symmetric extrude, each_side=3.5
        extrude(amount=3.5, both=True)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 15 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 2.898059765, perimeter: 10.9850556483
            with BuildLine():
                Line((1.0981394103, 3.3217759974), (-3, 2.3))
                CenterArc((2.5496642074, -2.5), 6, 97.1775238612, 6.8224114153)
                Line((1.8, 3.5), (1.8, 3.4529827462))
                Line((1.8, 3.5), (-3, 3.5))
                Line((-3, 2.3), (-3, 3.5))
            make_face()
            # Profile area: 0.0117305751, perimeter: 1.5483100024
            with BuildLine():
                Line((1.8, 3.5), (1.8, 3.4529827462))
                CenterArc((2.5496642074, -2.5), 6, 90, 7.1775238612)
                Line((2.5496642074, 3.5), (1.8, 3.5))
            make_face()
            # Profile area: 2.898059765, perimeter: 10.9850556483
            with BuildLine():
                Line((1.8, -3.4529827462), (1.8, -3.5))
                CenterArc((2.5496642074, 2.5), 6, -103.9999352766, 6.8224114153)
                Line((1.0981394103, -3.3217759974), (-3, -2.3))
                Line((-3, -2.3), (-3, -3.5))
                Line((1.8, -3.5), (-3, -3.5))
            make_face()
            # Profile area: 0.0117305751, perimeter: 1.5483100024
            with BuildLine():
                CenterArc((2.5496642074, 2.5), 6, -97.1775238612, 7.1775238612)
                Line((1.8, -3.4529827462), (1.8, -3.5))
                Line((2.5496642074, -3.5), (1.8, -3.5))
            make_face()
        # OneSide extrude, distance=-27
        extrude(amount=-27, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 19.8, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))) as sk:
            # Profile area: 28.2743338823, perimeter: 18.8495559215
            with Locations((-10.9684777769, 0)):
                Circle(3)
        # TwoSides extrude, along=1.6, against=-1.2
        extrude(amount=1.6, mode=Mode.ADD)
        extrude(sk.sketch, amount=-1.2, mode=Mode.ADD)

        # Sketch4 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 21.4, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 9.6402481692, perimeter: 34.888240673
            with BuildLine():
                CenterArc((-10.9684777769, 0), 3.0526359589, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-10.9684777769, 0), 2.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.075
        extrude(amount=-0.075, mode=Mode.ADD)

        # Sketch5 -> Extrude6 (Join)
        # Sketch on BRepFace
        # Sketch has 6 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))) as sk:
            # Profile area: 0.3991713618, perimeter: 4.0394494087
            with BuildLine():
                Line((-0.9797958971, 1.8), (0.9797958971, 1.8))
                CenterArc((0, 3.25), 1.75, -124.04773237, 68.09546474)
            make_face()
            # Profile area: 8.7357124609, perimeter: 10.7276458877
            with BuildLine():
                CenterArc((0, 3.25), 1.75, 126.4903339482, 109.4619336818)
                Line((-0.9797958971, 1.8), (0.9797958971, 1.8))
                CenterArc((0, 3.25), 1.75, -55.95226763, 109.4619336818)
                Line((1.0407025371, 4.6569250972), (-1.0407025371, 4.6569250972))
            make_face()
            # Profile area: 0.4862436789, perimeter: 4.3104727282
            with BuildLine():
                Line((1.0407025371, 4.6569250972), (-1.0407025371, 4.6569250972))
                CenterArc((0, 3.25), 1.75, 53.5096660518, 72.9806678965)
            make_face()
        # TwoSides extrude, along=1.7, against=-0.05
        extrude(amount=1.7, mode=Mode.ADD)
        extrude(sk.sketch, amount=-0.05, mode=Mode.ADD)

        # Sketch6 -> Extrude7 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-1.7, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 8.8141308887, perimeter: 10.5243353895
            with Locations((0, 3.25)):
                Circle(1.675)
        # OneSide extrude, distance=-2.7
        extrude(amount=-2.7, mode=Mode.SUBTRACT)

        # Sketch7 -> Extrude8 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-1.7, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 1.9792033718, perimeter: 19.7920337176
            with BuildLine():
                CenterArc((0, 3.25), 1.675, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 3.25), 1.475, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.19104353, perimeter: 21.1621151951
            with BuildLine():
                CenterArc((0, 3.25), 1.6930552396, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 3.25), 1.675, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.075
        extrude(amount=-0.075, mode=Mode.ADD)

        # Sketch8 -> Extrude9 (Join)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 20.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))) as sk:
            # Profile area: 0.6783698911, perimeter: 5.4327424657
            with BuildLine():
                CenterArc((-18.5785361173, 0), 2.5, 148.0581580087, 63.8836839826)
                Line((-20.7, 1.3226454531), (-20.7, -1.3226454531))
            make_face()
            # Profile area: 0.6783698911, perimeter: 5.4327424657
            with BuildLine():
                Line((-16.4570722347, -1.3226454531), (-16.4570722347, 1.3226454531))
                CenterArc((-18.5785361173, 0), 2.5, -31.9418419913, 63.8836839826)
            make_face()
            # Profile area: 18.2782143028, perimeter: 15.4236419613
            with BuildLine():
                Line((-20.7, 1.3226454531), (-20.7, -1.3226454531))
                CenterArc((-18.5785361173, 0), 2.5, -148.0581580087, 116.1163160174)
                Line((-16.4570722347, -1.3226454531), (-16.4570722347, 1.3226454531))
                CenterArc((-18.5785361173, 0), 2.5, 31.9418419913, 116.1163160174)
            make_face()
        # TwoSides extrude, along=-0.075, against=0.7
        extrude(amount=-0.075, mode=Mode.ADD)
        extrude(sk.sketch, amount=0.7, mode=Mode.ADD)

        # Sketch9 -> Extrude10 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 21.2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 16.6190251375, perimeter: 14.4513262065
            with Locations((-18.5785361173, 0)):
                Circle(2.3)
        # OneSide extrude, distance=-3.5
        extrude(amount=-3.5, mode=Mode.SUBTRACT)

        # Sketch10 -> Extrude11 (Join)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 20.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.0106192983, perimeter: 5.0265482457
            with Locations((-4.0000000596, 0)):
                Circle(0.8)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3, mode=Mode.ADD)

        # Sketch11 -> Extrude12 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 20.8, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.5393804003, perimeter: 4.398229715
            with Locations((-4.0000000596, 0)):
                Circle(0.7)
        # OneSide extrude, distance=-0.7
        extrude(amount=-0.7, mode=Mode.SUBTRACT)
    return part.part


def model_48907_25974aa4_0011():
    """Model: right frame v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 13.5, perimeter: 22
            with BuildLine():
                Line((0, 0), (-3, 0))
                Line((-3, 0), (-3, -8))
                Line((-1.5, -8), (-3, -8))
                Line((-1.5, -1), (-1.5, -8))
                Line((0, -1), (-1.5, -1))
                Line((0, 0), (0, -1))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.75, perimeter: 3.5
            with BuildLine():
                Line((0, 0), (0, 1))
                Line((0, 1), (-0.75, 1))
                Line((-0.75, 1), (-0.75, 0))
                Line((-0.75, 0), (0, 0))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.5, perimeter: 3
            with BuildLine():
                Line((0.75, -0.75), (0.25, -0.75))
                Line((0.75, 0), (0.75, -0.75))
                Line((0.75, 0.25), (0.75, 0))
                Line((0.25, 0.25), (0.75, 0.25))
                Line((0.25, -0.75), (0.25, 0.25))
            make_face()
        # OneSide extrude, distance=1.25
        extrude(amount=1.25, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-0.25, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.2042820623, perimeter: 1.6022122533
            with Locations((0.75, -0.2514944591)):
                Circle(0.255)
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude5 (Cut)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.1963495467, perimeter: 1.5707963502
            with Locations((-0.5000000075, -0.5000000075)):
                Circle(0.2500000037)
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.SUBTRACT)

        # Sketch6 -> Extrude6 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.8, perimeter: 3.6
            with BuildLine():
                Line((-1.5, 2.9), (-2.5, 2.9))
                Line((-2.5, 2.9), (-2.5, 2.1))
                Line((-2.5, 2.1), (-1.5, 2.1))
                Line((-1.5, 2.9), (-1.5, 2.1))
            make_face()
        # OneSide extrude, distance=0.4
        extrude(amount=0.4, mode=Mode.ADD)

        # Sketch7 -> Extrude7 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-1.5, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((-2.5000000373, -0.2)):
                Circle(0.15)
        # OneSide extrude, distance=-0.8
        extrude(amount=-0.8, mode=Mode.SUBTRACT)

        # Sketch8 -> Extrude8 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-1.5, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.08, perimeter: 1.3656854249
            with BuildLine():
                Line((-3.3, 0), (-2.9, -0.4))
                Line((-2.9, -0.4), (-2.9, 0))
                Line((-2.9, 0), (-3.3, 0))
            make_face()
            # Profile area: 0.08, perimeter: 1.3656854249
            with BuildLine():
                Line((-2.1, -0.4), (-2.1, 0))
                Line((-1.7, 0), (-2.1, -0.4))
                Line((-2.1, 0), (-1.7, 0))
            make_face()
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2, mode=Mode.ADD)

        # Sketch9 -> Extrude9 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 8), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.14, perimeter: 1.8
            with BuildLine():
                Line((-1.5, 0.35), (-2.2, 0.35))
                Line((-2.2, 0.35), (-2.2, 0.15))
                Line((-2.2, 0.15), (-1.5, 0.15))
                Line((-1.5, 0.15), (-1.5, 0.35))
            make_face()
        # OneSide extrude, distance=-5
        extrude(amount=-5, mode=Mode.SUBTRACT)

        # Sketch10 -> Extrude10 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 1.5150000452, perimeter: 6.3000000939
            with BuildLine():
                Line((-2.7000000402, 0.2500000037), (-1.0000000149, 0.2500000037))
                Line((-1.0000000149, 0.2500000037), (-1.0000000149, 0.7500000112))
                Line((-1.0000000149, 0.7500000112), (-2.0000000298, 0.7500000112))
                Line((-2.0000000298, 0.7500000112), (-2.0000000298, 1.7000000253))
                Line((-2.0000000298, 1.7000000253), (-2.7000000402, 1.7000000253))
                Line((-2.7000000402, 1.7000000253), (-2.7000000402, 0.2500000037))
            make_face()
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2, mode=Mode.SUBTRACT)
    return part.part


def model_49896_6387ac02_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 7 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 373.0468073393, perimeter: 81.7622803298
            with BuildLine():
                Line((13.5658080929, -6.8747619896), (-13.5658080929, -6.8747619896))
                Line((13.5658080929, 6.8747619896), (13.5658080929, -6.8747619896))
                Line((-13.5658080929, 6.8747619896), (13.5658080929, 6.8747619896))
                Line((-13.5658080929, -6.8747619896), (-13.5658080929, 6.8747619896))
            make_face()
        # Symmetric extrude, each_side=1
        extrude(amount=1, both=True)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -6.8747619896, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 217.0529294862, perimeter: 70.2632323716
            with BuildLine():
                Line((-13.5658080929, 9), (-13.5658080929, 1))
                Line((-13.5658080929, 1), (13.5658080929, 1))
                Line((13.5658080929, 1), (13.5658080929, 9))
                Line((13.5658080929, 9), (-13.5658080929, 9))
            make_face()
        # OneSide extrude, distance=-0.35
        extrude(amount=-0.35, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 6.8747619896, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 217.0529294862, perimeter: 70.2632323716
            with BuildLine():
                Line((-13.5658080929, 9), (-13.5658080929, 1))
                Line((-13.5658080929, 1), (13.5658080929, 1))
                Line((13.5658080929, 1), (13.5658080929, 9))
                Line((13.5658080929, 9), (-13.5658080929, 9))
            make_face()
        # OneSide extrude, distance=-0.35
        extrude(amount=-0.35, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 9), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 312.0135861365, perimeter: 77.2632323716
            with BuildLine():
                Line((-13.5658080929, 18.3747619896), (-13.5658080929, 6.8747619896))
                Line((-13.5658080929, 6.8747619896), (13.5658080929, 6.8747619896))
                Line((13.5658080929, 6.8747619896), (13.5658080929, 18.3747619896))
                Line((13.5658080929, 18.3747619896), (-13.5658080929, 18.3747619896))
            make_face()
        # Symmetric extrude, each_side=1
        extrude(amount=1, both=True, mode=Mode.ADD)

        # Sketch5 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 9), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 302.5175204714, perimeter: 76.5632323716
            with BuildLine():
                Line((13.5658080929, -18.0247619896), (-13.5658080929, -18.0247619896))
                Line((13.5658080929, -6.8747619896), (13.5658080929, -18.0247619896))
                Line((-13.5658080929, -6.8747619896), (13.5658080929, -6.8747619896))
                Line((-13.5658080929, -18.0247619896), (-13.5658080929, -6.8747619896))
            make_face()
        # Symmetric extrude, each_side=1
        extrude(amount=1, both=True, mode=Mode.ADD)

        # Sketch6 -> Extrude6 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 8), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 3.4641016151, perimeter: 6.9282032303
            with BuildLine():
                Line((-10.7332524025, -15.7772151257), (-11.773774704, -15.2765688699))
                Line((-11.773774704, -15.2765688699), (-12.7276082306, -15.9273644883))
                Line((-12.7276082306, -15.9273644883), (-12.6409194557, -17.0788063624))
                Line((-12.6409194557, -17.0788063624), (-11.6003971542, -17.5794526183))
                Line((-11.6003971542, -17.5794526183), (-10.6465636277, -16.9286569999))
                Line((-10.6465636277, -16.9286569999), (-10.7332524025, -15.7772151257))
            make_face()
            # Profile area: 3.4641016151, perimeter: 6.9282032303
            with BuildLine():
                Line((12.0473160768, -15.277110682), (11.003803592, -15.771494164))
                Line((11.003803592, -15.771494164), (10.9101960042, -16.9223942261))
                Line((10.9101960042, -16.9223942261), (11.8601009013, -17.5789108061))
                Line((11.8601009013, -17.5789108061), (12.9036133861, -17.0845273241))
                Line((12.9036133861, -17.0845273241), (12.9972209739, -15.933627262))
                Line((12.9972209739, -15.933627262), (12.0473160768, -15.277110682))
            make_face()
        # OneSide extrude, distance=20
        extrude(amount=20, mode=Mode.ADD)

        # Sketch7 -> Extrude7 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 8), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 3.4641016151, perimeter: 6.9282032303
            with BuildLine():
                Line((11.9576247811, 17.0647998215), (10.8029242427, 17.0647998215))
                Line((10.8029242427, 17.0647998215), (10.2255739735, 16.0647998215))
                Line((10.2255739735, 16.0647998215), (10.8029242427, 15.0647998215))
                Line((10.8029242427, 15.0647998215), (11.9576247811, 15.0647998215))
                Line((11.9576247811, 15.0647998215), (12.5349750502, 16.0647998215))
                Line((12.5349750502, 16.0647998215), (11.9576247811, 17.0647998215))
            make_face()
            # Profile area: 3.4641016151, perimeter: 6.9282032303
            with BuildLine():
                Line((-10.4616430813, 17.0330727944), (-11.6147476265, 17.0937625073))
                Line((-11.6147476265, 17.0937625073), (-12.2438587322, 16.1254895344))
                Line((-12.2438587322, 16.1254895344), (-11.7198652927, 15.0965268487))
                Line((-11.7198652927, 15.0965268487), (-10.5667607475, 15.0358371358))
                Line((-10.5667607475, 15.0358371358), (-9.9376496418, 16.0041101086))
                Line((-9.9376496418, 16.0041101086), (-10.4616430813, 17.0330727944))
            make_face()
        # OneSide extrude, distance=20
        extrude(amount=20, mode=Mode.ADD)

        # Sketch8 -> Extrude8 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -1), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 13.8564064606, perimeter: 13.8564064606
            with BuildLine():
                Line((11.5455377071, 1.7159972405), (9.2866716504, 2.1964735371))
                Line((9.2866716504, 2.1964735371), (7.7411339434, 0.4804762966))
                Line((7.7411339434, 0.4804762966), (8.4544622929, -1.7159972405))
                Line((8.4544622929, -1.7159972405), (10.7133283496, -2.1964735371))
                Line((10.7133283496, -2.1964735371), (12.2588660566, -0.4804762966))
                Line((12.2588660566, -0.4804762966), (11.5455377071, 1.7159972405))
            make_face()
            # Profile area: 13.8564064606, perimeter: 13.8564064606
            with BuildLine():
                Line((-8.8452994616, 2), (-11.1547005384, 2))
                Line((-11.1547005384, 2), (-12.3094010768, 0))
                Line((-12.3094010768, 0), (-11.1547005384, -2))
                Line((-11.1547005384, -2), (-8.8452994616, -2))
                Line((-8.8452994616, -2), (-7.6905989232, 0))
                Line((-7.6905989232, 0), (-8.8452994616, 2))
            make_face()
        # OneSide extrude, distance=11.1
        extrude(amount=11.1, mode=Mode.ADD)

        # Sketch9 -> Extrude9 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(13.5658080929, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 44.6, perimeter: 30.3
            with BuildLine():
                Line((-10, -6.8747619896), (-10, -18.0247619896))
                Line((-14, -6.8747619896), (-10, -6.8747619896))
                Line((-14, -18.0247619896), (-14, -6.8747619896))
                Line((-10, -18.0247619896), (-14, -18.0247619896))
            make_face()
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.ADD)

        # Sketch10 -> Extrude10 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(13.5658080929, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 52.1980959166, perimeter: 34.0990479583
            with BuildLine():
                Line((-5, 6.5247619896), (-1, 6.5247619896))
                Line((-5, -6.5247619896), (-5, 6.5247619896))
                Line((-1, -6.5247619896), (-5, -6.5247619896))
                Line((-1, 6.5247619896), (-1, -6.5247619896))
            make_face()
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.ADD)

        # Sketch11 -> Extrude11 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(13.5658080929, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 46, perimeter: 31
            with BuildLine():
                Line((-10, 18.3747619896), (-10, 6.8747619896))
                Line((-14, 18.3747619896), (-10, 18.3747619896))
                Line((-14, 6.8747619896), (-14, 18.3747619896))
                Line((-10, 6.8747619896), (-14, 6.8747619896))
            make_face()
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.ADD)

        # Sketch12 -> Extrude12 (Join)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(-13.5658080929, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 23, perimeter: 27
            with BuildLine():
                Line((12, 6.8747619896), (12, 18.3747619896))
                Line((12, 18.3747619896), (10, 18.3747619896))
                Line((10, 18.3747619896), (10, 6.8747619896))
                Line((10, 6.8747619896), (12, 6.8747619896))
            make_face()
        # OneSide extrude, distance=-0.3
        extrude(amount=-0.3, mode=Mode.ADD)

        # Sketch13 -> Extrude13 (Join)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(-13.5658080929, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 22.3, perimeter: 26.3
            with BuildLine():
                Line((10, -18.0247619896), (10, -6.8747619896))
                Line((10, -18.0247619896), (12, -18.0247619896))
                Line((12, -6.8747619896), (12, -18.0247619896))
                Line((10, -6.8747619896), (12, -6.8747619896))
            make_face()
        # OneSide extrude, distance=-0.3
        extrude(amount=-0.3, mode=Mode.ADD)

        # Sketch16 -> Extrude14 (NewBody)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 18.3747619896, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 13.7828634293, perimeter: 73.4353927687
            with BuildLine():
                Line((-13.0658080929, 14), (-13.0658080929, 10))
                Line((-8, 10), (-13.0658080929, 10))
                Line((-8, 14), (-8, 10))
                Line((-13.0658080929, 14), (-8, 14))
            make_face()
            with BuildLine():
                CenterArc((-12.5, 13.5), 0.2473161171, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-11.5, 13.5), 0.2983151659, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-12, 13), 0.2391895252, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-10.7553540211, 13.5), 0.2553540211, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-8.3553540211, 13.5), 0.2553540211, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-9.1, 13.5), 0.2983151659, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-10.1, 13.5), 0.2473161171, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-9.6, 13), 0.2391895252, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-12, 12), 0.2391895252, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-12.5, 12.5), 0.2473161171, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-11.5, 12.5), 0.2983151659, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-10.7553540211, 12.5), 0.2553540211, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-10.1, 12.5), 0.2473161171, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-9.6, 12), 0.2391895252, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-9.1, 12.5), 0.2983151659, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-8.3553540211, 12.5), 0.2553540211, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-12, 11), 0.2391895252, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-11.5, 11.5), 0.2983151659, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-10.7553540211, 11.5), 0.2553540211, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-10.1, 11.5), 0.2473161171, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-9.6, 11), 0.2391895252, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-9.1, 11.5), 0.2983151659, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-8.3553540211, 11.5), 0.2553540211, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-11.1352085531, 12.0234558638), 0.1372280233, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-10.3735312275, 12.0234558638), 0.206935946, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-10.3735312275, 10.9519674735), 0.1652999512, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-11, 11), 0.208184769, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-11.5051683776, 10.9519674735), 0.1520551691, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-12.3000001833, 11.5000001714), 0.2236068011, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-12.8000001907, 11.9000001773), 0.2236068011, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-12.7000001892, 11.1000001654), 0.200000003, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-12.7000001892, 10.400000155), 0.2496534924, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-12.2000001818, 10.7000001594), 0.1000000015, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-11.3000001684, 10.7000001594), 0.1000000015, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-10.7000001594, 10.7000001594), 0.1000000015, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-11.7174352392, 10.7000001594), 0.1174350664, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-10.000000149, 10.7000001594), 0.1000000015, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-9.2000001371, 10.9000001624), 0.1414213583, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-8.7675502222, 11), 0.0805198766, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-8.3210401708, 11), 0.1021892905, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-8.7000001296, 10.7000001594), 0.200000003, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-1
        extrude(amount=-1)

        # Sketch22 -> Extrude17 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 6.8747619896, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 39.2487124277, perimeter: 55.3316165702
            with BuildLine():
                Line((12.9000001922, 11.5), (-13.2658080929, 11.5))
                Line((-13.2658080929, 11.5), (-13.2658080929, 10))
                Line((-13.2658080929, 10), (12.9000001922, 10))
                Line((12.9000001922, 10), (12.9000001922, 11.5))
            make_face()
        # OneSide extrude, distance=-0.3
        extrude(amount=-0.3, mode=Mode.ADD)

        # Sketch23 -> Extrude18 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -6.8747619896, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 39.4974242787, perimeter: 55.6632323716
            with BuildLine():
                Line((-13.0658080929, 11.5), (-13.0658080929, 10))
                Line((-13.0658080929, 10), (13.2658080929, 10))
                Line((13.2658080929, 10), (13.2658080929, 11.5))
                Line((13.2658080929, 11.5), (-13.0658080929, 11.5))
            make_face()
        # OneSide extrude, distance=-0.3
        extrude(amount=-0.3, mode=Mode.ADD)
    return part.part


def model_52221_3cdb5865_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1047.38435684, perimeter: 131.3688
            with BuildLine():
                Line((0, -38.4302), (0, 0))
                Line((0, 0), (-27.2542, 0))
                Line((-27.2542, 0), (-27.2542, -38.4302))
                Line((-27.2542, -38.4302), (0, -38.4302))
            make_face()
        # OneSide extrude, distance=1.905
        extrude(amount=1.905)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 29.032199564, perimeter: 34.2899995422
            with BuildLine():
                Line((15.2399997711, 1.905), (15.2399997711, 0))
                Line((0, 1.905), (15.2399997711, 1.905))
                Line((0, 0), (0, 1.905))
                Line((15.2399997711, 0), (0, 0))
            make_face()
        # OneSide extrude, distance=10.16
        extrude(amount=10.16, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 38.4302), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 29.032199564, perimeter: 34.2899995422
            with BuildLine():
                Line((0, 0), (0, 1.905))
                Line((0, 1.905), (-15.2399997711, 1.905))
                Line((-15.2399997711, 1.905), (-15.2399997711, 0))
                Line((-15.2399997711, 0), (0, 0))
            make_face()
        # OneSide extrude, distance=10.16
        extrude(amount=10.16, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 29.032199564, perimeter: 34.2899995422
            with BuildLine():
                Line((0, 46.6852), (-15.2399997711, 46.6852))
                Line((0, 48.5902), (0, 46.6852))
                Line((-15.2399997711, 48.5902), (0, 48.5902))
                Line((-15.2399997711, 46.6852), (-15.2399997711, 48.5902))
            make_face()
        # OneSide extrude, distance=22.86
        extrude(amount=22.86, mode=Mode.ADD)

        # Sketch5 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 29.032199564, perimeter: 34.2899995422
            with BuildLine():
                Line((-15.2399997711, -8.255), (-15.2399997711, -10.16))
                Line((-15.2399997711, -10.16), (0, -10.16))
                Line((0, -10.16), (0, -8.255))
                Line((0, -8.255), (-15.2399997711, -8.255))
            make_face()
        # OneSide extrude, distance=22.86
        extrude(amount=22.86, mode=Mode.ADD)

        # Sketch6 -> Extrude6 (Join)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(-15.2399997711, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 24.3517557959, perimeter: 29.3761478172
            with BuildLine():
                Line((-10.16, -10.0769260914), (-10.16, -22.86))
                Line((-10.16, -22.86), (-8.255, -22.86))
                Line((-8.255, -22.86), (-8.255, -10.0769260914))
                Line((-8.255, -10.0769260914), (-10.16, -10.0769260914))
            make_face()
        # OneSide extrude, distance=17.78
        extrude(amount=17.78, mode=Mode.ADD)

        # Sketch7 -> Extrude7 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-15.2399997711, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 24.1935002907, perimeter: 29.2100003052
            with BuildLine():
                Line((46.6852, -10.1599998474), (46.6852, -22.86))
                Line((46.6852, -22.86), (48.5902, -22.86))
                Line((48.5902, -22.86), (48.5902, -10.1599998474))
                Line((48.5902, -10.1599998474), (46.6852, -10.1599998474))
            make_face()
        # OneSide extrude, distance=17.78
        extrude(amount=17.78, mode=Mode.ADD)

        # Sketch8 -> Extrude8 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-15.2399997711, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 4.8387, perimeter: 8.89
            with BuildLine():
                Line((-10.16, -7.5369260914), (-10.16, -10.0769260914))
                Line((-10.16, -10.0769260914), (-8.255, -10.0769260914))
                Line((-8.255, -10.0769260914), (-8.255, -7.5369260914))
                Line((-8.255, -7.5369260914), (-10.16, -7.5369260914))
            make_face()
        # OneSide extrude, distance=2.54
        extrude(amount=2.54, mode=Mode.ADD)

        # Sketch9 -> Extrude9 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-15.2399997711, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 4.8387, perimeter: 8.89
            with BuildLine():
                Line((46.6852, -7.6199998474), (48.5902, -7.6199998474))
                Line((46.6852, -10.1599998474), (46.6852, -7.6199998474))
                Line((48.5902, -10.1599998474), (46.6852, -10.1599998474))
                Line((48.5902, -7.6199998474), (48.5902, -10.1599998474))
            make_face()
        # OneSide extrude, distance=2.54
        extrude(amount=2.54, mode=Mode.ADD)

        # Sketch10 -> Extrude10 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -10.16), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 5.067074791, perimeter: 9.0698226701
            with BuildLine():
                Line((17.7799997711, -7.5369260914), (15.2399997711, -7.5369260914))
                CenterArc((17.7799997711, -7.5369260914), 2.54, -180, 90)
                Line((17.7799997711, -10.0769260914), (17.7799997711, -7.5369260914))
            make_face()
        # OneSide extrude, distance=-2.54
        extrude(amount=-2.54, mode=Mode.SUBTRACT)

        # Sketch11 -> Extrude11 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 48.5902), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 5.067074791, perimeter: 9.0698226701
            with BuildLine():
                Line((-17.7799997711, -7.6199998474), (-17.7799997711, -10.1599998474))
                CenterArc((-17.7799997711, -7.6199998474), 2.54, -90, 90)
                Line((-15.2399997711, -7.6199998474), (-17.7799997711, -7.6199998474))
            make_face()
        # OneSide extrude, distance=-2.54
        extrude(amount=-2.54, mode=Mode.SUBTRACT)

        # Sketch12 -> Extrude12 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -10.16), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 1.384525209, perimeter: 9.0698226701
            with BuildLine():
                CenterArc((2.54, -20.32), 2.54, 180, 90)
                Line((0, -20.32), (0, -22.86))
                Line((0, -22.86), (2.54, -22.86))
            make_face()
        # OneSide extrude, distance=-2.54
        extrude(amount=-2.54, mode=Mode.SUBTRACT)

        # Sketch13 -> Extrude13 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 48.5902), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1.384525209, perimeter: 9.0698226701
            with BuildLine():
                CenterArc((-2.54, -20.32), 2.54, -90, 90)
                Line((-2.54, -22.86), (0, -22.86))
                Line((0, -22.86), (0, -20.32))
            make_face()
        # OneSide extrude, distance=-5.08
        extrude(amount=-5.08, mode=Mode.SUBTRACT)

        # Sketch14 -> Extrude14 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -10.16), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 1.384525209, perimeter: 9.0698226701
            with BuildLine():
                CenterArc((30.4799997711, -20.32), 2.54, -90, 90)
                Line((30.4799997711, -22.86), (33.0199997711, -22.86))
                Line((33.0199997711, -22.86), (33.0199997711, -20.32))
            make_face()
        # OneSide extrude, distance=-2.54
        extrude(amount=-2.54, mode=Mode.SUBTRACT)

        # Sketch15 -> Extrude15 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 48.5902), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1.384525209, perimeter: 9.0698226701
            with BuildLine():
                CenterArc((-30.4799997711, -20.32), 2.54, 180, 90)
                Line((-33.0199997711, -20.32), (-33.0199997711, -22.86))
                Line((-33.0199997711, -22.86), (-30.4799997711, -22.86))
            make_face()
        # OneSide extrude, distance=-2.54
        extrude(amount=-2.54, mode=Mode.SUBTRACT)

        # Sketch16 -> Extrude16 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.905, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.384525209, perimeter: 9.0698226701
            with BuildLine():
                CenterArc((24.7142, 2.54), 2.54, -90, 90)
                Line((24.7142, 0), (27.2542, 0))
                Line((27.2542, 0), (27.2542, 2.54))
            make_face()
        # OneSide extrude, distance=-2.54
        extrude(amount=-2.54, mode=Mode.SUBTRACT)

        # Sketch17 -> Extrude17 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.905, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.384525209, perimeter: 9.0698226701
            with BuildLine():
                CenterArc((24.7142, 35.8902), 2.54, 0, 90)
                Line((27.2542, 35.8902), (27.2542, 38.4302))
                Line((27.2542, 38.4302), (24.7142, 38.4302))
            make_face()
        # OneSide extrude, distance=-2.54
        extrude(amount=-2.54, mode=Mode.SUBTRACT)

        # Sketch20 -> Extrude19 (Join)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(-15.2399997711, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 4.8386999273, perimeter: 8.8899999237
            with BuildLine():
                Line((0, 0), (0, 1.905))
                Line((0, 1.905), (-2.5399999619, 1.905))
                Line((-2.5399999619, 1.905), (-2.5399999619, 0))
                Line((-2.5399999619, 0), (0, 0))
            make_face()
        # OneSide extrude, distance=2.54
        extrude(amount=2.54, mode=Mode.ADD)

        # Sketch21 -> Extrude20 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-15.2399997711, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 4.8387, perimeter: 8.89
            with BuildLine():
                Line((40.9702, 1.905), (40.9702, 0))
                Line((38.4302, 1.905), (40.9702, 1.905))
                Line((38.4302, 0), (38.4302, 1.905))
                Line((40.9702, 0), (38.4302, 0))
            make_face()
        # OneSide extrude, distance=2.54
        extrude(amount=2.54, mode=Mode.ADD)
    return part.part


def model_54273_21c2b38f_0019():
    """Model: core v6"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2199114858, perimeter: 4.398229715
            with BuildLine():
                CenterArc((0, 0), 0.4, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            Circle(0.3)
        # Symmetric extrude, each_side=0.9
        extrude(amount=0.9, both=True)

        # Sketch1 -> Extrude2 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            Circle(0.3)
        # Symmetric extrude, each_side=1.5
        extrude(amount=1.5, both=True)

        # Sketch2 -> Extrude3 (Join)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.2199114858, perimeter: 4.398229715
            with BuildLine():
                CenterArc((0, 0), 0.4, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            Circle(0.3)
        # Symmetric extrude, each_side=0.9
        extrude(amount=0.9, both=True, mode=Mode.ADD)

        # Sketch2 -> Extrude4 (Join)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            Circle(0.3)
        # Symmetric extrude, each_side=1.5
        extrude(amount=1.5, both=True, mode=Mode.ADD)

        # Sketch3 -> Extrude5 (Join)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.2199114858, perimeter: 4.398229715
            with BuildLine():
                CenterArc((0, 0), 0.4, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            Circle(0.3)
        # Symmetric extrude, each_side=0.9
        extrude(amount=0.9, both=True, mode=Mode.ADD)

        # Sketch3 -> Extrude6 (Join)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            Circle(0.3)
        # Symmetric extrude, each_side=1.5
        extrude(amount=1.5, both=True, mode=Mode.ADD)

        # Sketch4 -> Extrude7 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1.5), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            Circle(0.2)
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude8 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(1.5, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            Circle(0.2)
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.SUBTRACT)

        # Sketch6 -> Extrude9 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -1.5), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            Circle(0.2)
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.SUBTRACT)

        # Sketch7 -> Extrude10 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-1.5, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            Circle(0.2)
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.SUBTRACT)

        # Sketch8 -> Extrude11 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -1.5, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            Circle(0.2)
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.SUBTRACT)

        # Sketch9 -> Extrude12 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            Circle(0.2)
        # OneSide extrude, distance=-0.4
        extrude(amount=-0.4, mode=Mode.SUBTRACT)
    return part.part


def model_55556_429d33b3_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 40, perimeter: 28
            with BuildLine():
                Line((0, 4), (0, 0))
                Line((0, 0), (10, 0))
                Line((10, 0), (10, 4))
                Line((10, 4), (0, 4))
            make_face()
        # Symmetric extrude, each_side=3
        extrude(amount=3, both=True)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 3), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 4.9087385212, perimeter: 8.926990817
            with BuildLine():
                Line((0, 4), (0, 1.5))
                CenterArc((0, 4), 2.5, -90, 90)
                Line((2.5, 4), (0, 4))
            make_face()
            # Profile area: 14.7262155637, perimeter: 16.780972451
            with BuildLine():
                Line((2.5, 4), (0, 4))
                CenterArc((0, 4), 2.5, 0, 270)
                Line((0, 4), (0, 1.5))
            make_face()
        # OneSide extrude, distance=-6
        extrude(amount=-6, mode=Mode.ADD)

        # Sketch4 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 3), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 5, perimeter: 9
            with BuildLine():
                Line((10, 0), (10, 2))
                Line((12.5, 0), (10, 0))
                Line((12.5, 2), (12.5, 0))
                Line((10, 2), (12.5, 2))
            make_face()
            # Profile area: 8, perimeter: 12
            with BuildLine():
                Line((6, 2), (10, 2))
                Line((6, 0), (6, 2))
                Line((10, 0), (6, 0))
                Line((10, 0), (10, 2))
            make_face()
        # OneSide extrude, distance=-6
        extrude(amount=-6, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 4, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            with Locations((-7, 0)):
                Circle(1)
        # OneSide extrude, distance=-6
        extrude(amount=-6, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 3), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            with Locations((0, 4)):
                Circle(1)
        # OneSide extrude, distance=-11
        extrude(amount=-11, mode=Mode.SUBTRACT)

        # Sketch6 -> Extrude6 (Join)
        # Sketch on BRepFace
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 4, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 14.1371669412, perimeter: 15.4247779608
            with BuildLine():
                Line((-10, 3), (-10, -3))
                CenterArc((-10, 0), 3, 90, 180)
            make_face()
        # OneSide extrude, distance=-2
        extrude(amount=-2, mode=Mode.ADD)

        # Sketch7 -> Extrude7 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 4, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            with Locations((-7, 0)):
                Circle(1)
        # OneSide extrude, distance=-2
        extrude(amount=-2, mode=Mode.ADD)

        # Sketch8 -> Extrude8 (Cut)
        # Sketch on BRepFace
        # Sketch has 7 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 1.4456772578, perimeter: 5.3551393541
            with BuildLine():
                Line((0.9637848385, 0), (0.9637848385, 0.75))
                Line((0.9637848385, 0.75), (-0.9637848385, 0.75))
                Line((-0.9637848385, 0.75), (-0.9637848385, 0))
                Line((-0.9637848385, 0), (0.9637848385, 0))
            make_face()
            # Profile area: 1.4456772578, perimeter: 5.3551393541
            with BuildLine():
                Line((-0.9637848385, 0), (0.9637848385, 0))
                Line((-0.9637848385, 0), (-0.9637848385, -0.75))
                Line((-0.9637848385, -0.75), (0.9637848385, -0.75))
                Line((0.9637848385, -0.75), (0.9637848385, 0))
            make_face()
        # OneSide extrude, distance=-11
        extrude(amount=-11, mode=Mode.SUBTRACT)

        # Sketch9 -> Extrude9 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 4, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 11.7272216411, perimeter: 12.1395474965
            with Locations((-10, 0)):
                Circle(1.932068991)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)

        # Sketch10 -> Extrude10 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 4.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            with Locations((-10, 0)):
                Circle(1)
        # OneSide extrude, distance=-6
        extrude(amount=-6, mode=Mode.SUBTRACT)

        # Sketch11 -> Extrude11 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 4, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            with Locations((-4, 0)):
                Circle(1)
        # OneSide extrude, distance=-10
        extrude(amount=-10, mode=Mode.SUBTRACT)

        # Sketch12 -> Extrude12 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 3), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 3.926990817, perimeter: 15.7079632679
            with BuildLine():
                CenterArc((0, 4), 1.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 4), 1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-13
        extrude(amount=-13, mode=Mode.SUBTRACT)
    return part.part


def model_57629_0877c022_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch5 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            Circle(0.4)
        # OneSide extrude, distance=6
        extrude(amount=6)

        # Sketch6 -> Extrude2 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 4 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            with Locations((-0.9, 0)):
                Circle(0.3)
        # OneSide extrude, distance=-10
        extrude(amount=-10)

        # Sketch7 -> Extrude3 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            with Locations((0.9, 0)):
                Circle(0.3)
        # OneSide extrude, distance=-10
        extrude(amount=-10)

        # Sketch8 -> Extrude4 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.3848451001, perimeter: 2.1991148575
            Circle(0.35)
        # OneSide extrude, distance=0.6
        extrude(amount=0.6, mode=Mode.SUBTRACT)

        # Sketch9 -> Extrude5 (Join)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            Circle(0.4)
        # TwoSides extrude (symmetric), distance=1.2
        extrude(amount=1.2, both=True, mode=Mode.ADD)

        # Sketch10 -> Extrude6 (Join)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((-10, 0)):
                Circle(0.2)
        # Symmetric extrude, each_side=1.2
        extrude(amount=1.2, both=True, mode=Mode.ADD)

        # Sketch11 -> Extrude7 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((9.5, 0)):
                Circle(0.2)
        # Symmetric extrude, each_side=1.2
        extrude(amount=1.2, both=True)

        # Sketch16 -> Extrude8 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            with Locations((-5.8000000864, -2.6000000387)):
                Circle(0.4)
        # Symmetric extrude, each_side=0.9
        extrude(amount=0.9, both=True)
    return part.part


def model_60747_5e38b665_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 7 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 4940000, perimeter: 9000
            with BuildLine():
                Line((-1300, 950), (-1300, -950))
                Line((-1300, -950), (1300, -950))
                Line((1300, -950), (1300, 950))
                Line((1300, 950), (-1300, 950))
            make_face()
        # OneSide extrude, distance=400
        extrude(amount=400)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 400), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 240029.6758206157, perimeter: 2000.1483791031
            with BuildLine():
                Line((-600, 900), (-1200.0741895515, 900))
                Line((-1200.0741895515, 900), (-1200.0741895515, 500))
                Line((-1200.0741895515, 500), (-600, 500))
                Line((-600, 500), (-600, 900))
            make_face()
        # OneSide extrude, distance=-150
        extrude(amount=-150, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 400), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 237444.151783821, perimeter: 1991.5310311757
            with BuildLine():
                Line((-600, 50), (-1200.0741895515, 50))
                Line((-600, 445.6913260363), (-600, 50))
                Line((-1200.0741895515, 445.6913260363), (-600, 445.6913260363))
                Line((-1200.0741895515, 50), (-1200.0741895515, 445.6913260363))
            make_face()
        # OneSide extrude, distance=-150
        extrude(amount=-150, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 400), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1950000, perimeter: 6700
            with BuildLine():
                Line((-1300, -200), (1300, -200))
                Line((-1300, -200), (-1300, -950))
                Line((1300, -950), (-1300, -950))
                Line((1300, -950), (1300, -200))
            make_face()
        # OneSide extrude, distance=400
        extrude(amount=400, mode=Mode.ADD)

        # Sketch5 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 8 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 400), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 238429.5432873593, perimeter: 1996.5116382232
            with BuildLine():
                Line((1200, 50), (597.4355069247, 50))
                Line((1200, 445.6913260363), (1200, 50))
                Line((597.4355069247, 445.6913260363), (1200, 445.6913260363))
                Line((597.4355069247, 50), (597.4355069247, 445.6913260363))
            make_face()
            # Profile area: 240000, perimeter: 2000
            with BuildLine():
                Line((1200, 500), (1200, 900))
                Line((1200, 900), (600, 900))
                Line((600, 900), (600, 500))
                Line((600, 500), (1200, 500))
            make_face()
        # OneSide extrude, distance=-150
        extrude(amount=-150, mode=Mode.SUBTRACT)

        # Sketch6 -> Extrude6 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 400), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 700000, perimeter: 3400
            with BuildLine():
                Line((500, 100), (-500, 100))
                Line((500, 800), (500, 100))
                Line((-500, 800), (500, 800))
                Line((-500, 100), (-500, 800))
            make_face()
        # OneSide extrude, distance=100
        extrude(amount=100, mode=Mode.ADD)

        # Sketch7 -> Extrude7 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 500), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 555178.2869599069, perimeter: 3035.5018285757
            with BuildLine():
                Line((437.2417694893, 133.3814866882), (-463.7521547213, 133.3814866882))
                Line((437.2417694893, 748.3455936891), (437.2417694893, 133.3814866882))
                Line((-467.3275274364, 748.3455936891), (437.2417694893, 748.3455936891))
                Line((-463.7521547213, 133.3814866882), (-467.3275274364, 748.3455936891))
            make_face()
        # OneSide extrude, distance=-100
        extrude(amount=-100, mode=Mode.SUBTRACT)

        # Sketch8 -> Extrude8 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 800), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 117500, perimeter: 4800
            with BuildLine():
                Line((1150, -100), (-1200, -100))
                Line((1150, -50), (1150, -100))
                Line((-1200, -50), (1150, -50))
                Line((-1200, -100), (-1200, -50))
            make_face()
        # OneSide extrude, distance=-400
        extrude(amount=-400, mode=Mode.ADD)

        # Sketch9 -> Extrude9 (Join)
        # Sketch on BRepFace
        # Sketch has 8 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 800), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 422500, perimeter: 2600
            with BuildLine():
                Line((-1250, -900), (-1250, -250))
                Line((-600, -900), (-1250, -900))
                Line((-600, -250), (-600, -900))
                Line((-1250, -250), (-600, -250))
            make_face()
            # Profile area: 422500, perimeter: 2600
            with BuildLine():
                Line((1250, -250), (600, -250))
                Line((600, -250), (600, -900))
                Line((600, -900), (1250, -900))
                Line((1250, -900), (1250, -250))
            make_face()
        # OneSide extrude, distance=50
        extrude(amount=50, mode=Mode.ADD)

        # Sketch10 -> Extrude10 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -50, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 5925.2229576121, perimeter: 314.4975936056
            with Locations((0, 450)):
                Ellipse(68.1025150567, 27.6943816786)
        # OneSide extrude, distance=30
        extrude(amount=30, mode=Mode.ADD)

        # Sketch11 -> Extrude11 (Join)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, -20, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 5925.2229576121, perimeter: 314.4975936056
            with Locations((0, 450)):
                Ellipse(68.1025150567, 27.6943816786)
        # OneSide extrude, distance=120
        extrude(amount=120, mode=Mode.ADD)
    return part.part


def model_63411_46a912fc_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 7 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 9.7101085543, perimeter: 16.0093628295
            with BuildLine():
                Line((9, 4), (9, 0))
                Line((9, 4), (3.9054997826, 4))
                CenterArc((1.7274281862, -2.3251451601), 6.6896529936, 20.3389625349, 50.6598271083)
                Line((9, 0), (8, 0))
            make_face()
            # Profile area: 5.0964150113, perimeter: 12.189752145
            with BuildLine():
                Line((9, 5.0003758551), (9, 4))
                Line((3.9054997826, 5.0003758551), (9, 5.0003758551))
                Line((3.9054997826, 5.0003758551), (3.9054997826, 4))
                Line((9, 4), (3.9054997826, 4))
            make_face()
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 33 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.7689564647, perimeter: 5.7263764311
            with BuildLine():
                Line((3.5631882156, 6.7), (1, 6.7))
                Line((3.5631882156, 7), (3.5631882156, 6.7))
                Line((1, 7), (3.5631882156, 7))
                Line((1, 6.7), (1, 7))
            make_face()
            # Profile area: 3.4233729896, perimeter: 20.6861265545
            with BuildLine():
                Line((1, 8.7), (1, 9))
                Line((1, 10.0007517102), (1, 9))
                Line((0.657688433, 10.0007517102), (1, 10.0007517102))
                Line((0.657688433, 0), (0.657688433, 10.0007517102))
                Line((1, 0), (0.657688433, 0))
                Line((1, 2.7), (1, 0))
                Line((1, 2.7), (1, 3))
                Line((1, 3), (1, 4.7))
                Line((1, 4.7), (1, 5))
                Line((1, 6.7), (1, 5))
                Line((1, 6.7), (1, 7))
                Line((1, 8.7), (1, 7))
            make_face()
            # Profile area: 0.7689564647, perimeter: 5.7263764311
            with BuildLine():
                Line((3.5631882156, 2.7), (1, 2.7))
                Line((3.5631882156, 3), (3.5631882156, 2.7))
                Line((1, 3), (3.5631882156, 3))
                Line((1, 2.7), (1, 3))
            make_face()
            # Profile area: 1.722850715, perimeter: 10.5097882416
            with BuildLine():
                Line((1, 10.1681619039), (1, 10.0007517102))
                CenterArc((2.2815941078, 10.1681619039), 1.2815941078, 0, 180)
                Line((3.5631882156, 10.0007517102), (3.5631882156, 10.1681619039))
                Line((3.5631882156, 10.0007517102), (3.9054997826, 10.0007517102))
                CenterArc((2.2815941078, 10.1681619039), 1.6325121175, -5.8858913916, 191.7717827832)
                Line((0.657688433, 10.0007517102), (1, 10.0007517102))
            make_face()
            # Profile area: 0.7689564647, perimeter: 5.7263764311
            with BuildLine():
                Line((3.5631882156, 8.7), (1, 8.7))
                Line((3.5631882156, 9), (3.5631882156, 8.7))
                Line((1, 9), (3.5631882156, 9))
                Line((1, 8.7), (1, 9))
            make_face()
            # Profile area: 0.7689564647, perimeter: 5.7263764311
            with BuildLine():
                Line((1, 4.7), (3.5631882156, 4.7))
                Line((3.5631882156, 5), (3.5631882156, 4.7))
                Line((1, 5), (3.5631882156, 5))
                Line((1, 4.7), (1, 5))
            make_face()
            # Profile area: 3.4233729896, perimeter: 20.6861265545
            with BuildLine():
                Line((3.5631882156, 7), (3.5631882156, 8.7))
                Line((3.5631882156, 7), (3.5631882156, 6.7))
                Line((3.5631882156, 5), (3.5631882156, 6.7))
                Line((3.5631882156, 5), (3.5631882156, 4.7))
                Line((3.5631882156, 4.7), (3.5631882156, 3))
                Line((3.5631882156, 3), (3.5631882156, 2.7))
                Line((3.5631882156, 0), (3.5631882156, 2.7))
                Line((3.9054997826, 0), (3.5631882156, 0))
                Line((3.9054997826, 10.0007517102), (3.9054997826, 0))
                Line((3.5631882156, 10.0007517102), (3.9054997826, 10.0007517102))
                Line((3.5631882156, 9), (3.5631882156, 10.0007517102))
                Line((3.5631882156, 9), (3.5631882156, 8.7))
            make_face()
        # OneSide extrude, distance=6.9
        extrude(amount=6.9)

        # Sketch4 -> Extrude2 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.1997689767, perimeter: 5.3901506396
            with BuildLine():
                Line((2.7933342756, 11.1733770712), (1.9070018968, 9.2338509218))
                Line((2.4186976134, 9), (1.9070018968, 9.2338509218))
                Line((3.3050744435, 10.9395058347), (2.4186976134, 9))
                Line((3.3050744435, 10.9395058347), (2.7933342756, 11.1733770712))
            make_face()
        # OneSide extrude, distance=2.5
        extrude(amount=2.5)

        # Sketch5 -> Extrude3 (Join)
        # Sketch on XY construction plane
        # Sketch has 8 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.6309455041, perimeter: 3.7402421728
            with BuildLine():
                Line((1.8834241414, 9), (1.8834241414, 10.4284090157))
                Line((1.8834241414, 10.4284090157), (1.4417120707, 10.4284090157))
                Line((1.4417120707, 10.4284090157), (1.4417120707, 9))
                Line((1.4417120707, 9), (1.8834241414, 9))
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2, mode=Mode.ADD)

        # Sketch8 -> Extrude4 (Join)
        # Sketch on XY construction plane
        # Sketch has 11 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.108528601, perimeter: 5.2766658093
            with BuildLine():
                Line((1.2000336321, 7.5243887929), (1.2000336321, 7))
                Line((3.3139777439, 7), (1.2000336321, 7))
                Line((3.3139777439, 7), (3.3139777439, 7.5243887929))
                Line((3.3139777439, 7.5243887929), (2.8552917574, 7.5243887929))
                Line((2.8552917574, 7.5243887929), (1.2000336321, 7.5243887929))
            make_face()
        # OneSide extrude, distance=2.5
        extrude(amount=2.5, mode=Mode.ADD)

        # Sketch9 -> Extrude5 (Join)
        # Sketch on XY construction plane
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.4254797507, perimeter: 3.4210841147
            with BuildLine():
                Line((1.1711449808, 7.8264792165), (2.5795966145, 7.8264792165))
                Line((1.1711449808, 7.5243887929), (1.1711449808, 7.8264792165))
                Line((2.5795966145, 7.5243887929), (1.1711449808, 7.5243887929))
                Line((2.5795966145, 7.8264792165), (2.5795966145, 7.5243887929))
            make_face()
        # OneSide extrude, distance=1.5
        extrude(amount=1.5, mode=Mode.ADD)

        # Sketch15 -> Extrude6 (Cut)
        # Sketch on XY construction plane
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 4.3574199665, perimeter: 8.5263764311
            with BuildLine():
                Line((3.5631882156, 7), (3.5631882156, 8.7))
                Line((3.5631882156, 8.7), (1, 8.7))
                Line((1, 8.7), (1, 7))
                Line((1, 7), (3.5631882156, 7))
            make_face()
        # OneSide extrude, distance=10
        extrude(amount=10, mode=Mode.SUBTRACT)

        # Sketch16 -> Extrude7 (Cut)
        # Sketch on XY construction plane
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.6309455041, perimeter: 3.7402421728
            with BuildLine():
                Line((1.8834241414, 9), (1.8834241414, 10.4284090157))
                Line((1.8834241414, 10.4284090157), (1.4417120707, 10.4284090157))
                Line((1.4417120707, 10.4284090157), (1.4417120707, 9))
                Line((1.4417120707, 9), (1.8834241414, 9))
            make_face()
        # OneSide extrude, distance=26
        extrude(amount=26, mode=Mode.SUBTRACT)
    return part.part


def model_65810_620a5516_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 20825.8009935686, perimeter: 698.9700548531
            with BuildLine():
                Line((59.3005983079, 32.7204809849), (-15.2991382572, 32.5222275663))
                Line((-15.2991382572, 32.5222275663), (-15.4107554633, 74.5220792517))
                Line((-15.4107554633, 74.5220792517), (-80.1105269883, 74.3501356032))
                Line((-80.1105269883, 74.3501356032), (-79.9032378911, -3.6495889555))
                Line((-79.9032378911, -3.6495889555), (-73.2146535249, -3.6318136284))
                Line((-73.2146535249, -3.6318136284), (-73.2188665908, -15.1318128567))
                Line((-73.2188665908, -15.1318128567), (-89.2668276877, -15.0702851479))
                Line((-89.2668276877, -54.6302851479), (-89.2668276877, -15.0702851479))
                Line((-89.2668276877, -54.6302851479), (124.2331714337, -54.6496547055))
                Line((124.2331714337, -54.6496547055), (124.5106579381, 32.5128813403))
                Line((59.3005983079, 32.7204809849), (124.5106579381, 32.5128813403))
            make_face()
        # OneSide extrude, distance=30
        extrude(amount=30)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-0.0049570085, 0, 54.638383335), x_dir=(0.9999999959, 0, 0.0000907239), z_dir=(-0.0000907239, 0, 0.9999999959))):
            # Profile area: 103.810541579, perimeter: 46.2362431406
            with BuildLine():
                Line((-37.4937212615, 28.4420250969), (-37.4937212615, 11.4239035265))
                Line((-37.4937212615, 11.4239035265), (-31.3937212615, 11.4239035265))
                Line((-31.3937212615, 11.4239035265), (-31.3937212615, 28.4420250969))
                Line((-31.3937212615, 28.4420250969), (-37.4937212615, 28.4420250969))
            make_face()
        # OneSide extrude, distance=-3
        extrude(amount=-3, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(-0.0049570085, 0, 54.638383335), x_dir=(0.9999999959, 0, 0.0000907239), z_dir=(-0.0000907239, 0, 0.9999999959))):
            # Profile area: 200.4332975482, perimeter: 66.108324387
            with BuildLine():
                Line((9.3061674196, 3.2807093351), (1.3061674196, 3.2807093351))
                Line((9.3061674196, 28.3348715286), (9.3061674196, 3.2807093351))
                Line((1.3061674196, 28.3348715286), (9.3061674196, 28.3348715286))
                Line((1.3061674196, 3.2807093351), (1.3061674196, 28.3348715286))
            make_face()
        # OneSide extrude, distance=-3
        extrude(amount=-3, mode=Mode.SUBTRACT)

        # Sketch7 -> Extrude6 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(-73.2133131707, 0, -0.0268219595), x_dir=(-0.0003663536, 0, 0.9999999329), z_dir=(-0.9999999329, 0, -0.0003663536))):
            # Profile area: 250, perimeter: 70
            with BuildLine():
                Line((5, 27.5), (5, 2.5))
                Line((5, 2.5), (15, 2.5))
                Line((15, 2.5), (15, 27.5))
                Line((15, 27.5), (5, 27.5))
            make_face()
        # OneSide extrude, distance=-3
        extrude(amount=-3, mode=Mode.SUBTRACT)

        # Sketch8 -> Extrude7 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-79.9123725078, 0, 0.2123720775), x_dir=(0.0026575525, 0, 0.9999964687), z_dir=(-0.9999964687, 0, 0.0026575525))):
            # Profile area: 306.4001036068, perimeter: 74.8446452243
            with BuildLine():
                Line((-70.4527709841, 26.1053524442), (-70.4527709841, 28.1757310225))
                Line((-70.4527709841, 2.8534084104), (-70.4527709841, 26.1053524442))
                Line((-58.3527709841, 2.8534084104), (-70.4527709841, 2.8534084104))
                Line((-58.3527709841, 28.1757310225), (-58.3527709841, 2.8534084104))
                Line((-70.4527709841, 28.1757310225), (-58.3527709841, 28.1757310225))
            make_face()
        # OneSide extrude, distance=-3
        extrude(amount=-3, mode=Mode.SUBTRACT)

        # Sketch9 -> Extrude8 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(-79.9123725078, 0, 0.2123720775), x_dir=(0.0026575525, 0, 0.9999964687), z_dir=(-0.9999964687, 0, 0.0026575525))):
            # Profile area: 1280.6650494775, perimeter: 147.2570040133
            with BuildLine():
                Line((-5, 0), (-50.4527709841, 0))
                Line((-5, 28.1757310225), (-5, 0))
                Line((-50.4527709841, 28.1757310225), (-5, 28.1757310225))
                Line((-50.4527709841, 0), (-50.4527709841, 28.1757310225))
            make_face()
        # OneSide extrude, distance=-2
        extrude(amount=-2, mode=Mode.SUBTRACT)

        # Sketch10 -> Extrude9 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-0.0049570085, 0, 54.638383335), x_dir=(0.9999999959, 0, 0.0000907239), z_dir=(-0.0000907239, 0, 0.9999999959))):
            # Profile area: 289.3976991525, perimeter: 68.1552999058
            with BuildLine():
                Line((48.7881289535, 27.5447460925), (48.7881289535, 11.4670961396))
                Line((48.7881289535, 11.4670961396), (66.7881289535, 11.4670961396))
                Line((66.7881289535, 11.4670961396), (66.7881289535, 27.5447460925))
                Line((66.7881289535, 27.5447460925), (48.7881289535, 27.5447460925))
            make_face()
        # OneSide extrude, distance=-3
        extrude(amount=-3, mode=Mode.SUBTRACT)

        # Sketch11 -> Extrude10 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-0.0049570085, 0, 54.638383335), x_dir=(0.9999999959, 0, 0.0000907239), z_dir=(-0.0000907239, 0, 0.9999999959))):
            # Profile area: 306.9585133178, perimeter: 70.1065014798
            with BuildLine():
                Line((35.9461674196, 11.2816207887), (17.9461674196, 11.2816207887))
                Line((35.9461674196, 28.3348715286), (35.9461674196, 11.2816207887))
                Line((17.9461674196, 28.3348715286), (35.9461674196, 28.3348715286))
                Line((17.9461674196, 11.2816207887), (17.9461674196, 28.3348715286))
            make_face()
        # OneSide extrude, distance=-3
        extrude(amount=-3, mode=Mode.SUBTRACT)

        # Sketch13 -> Extrude12 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(124.4058906209, 0, 0.3960526768), x_dir=(0.0031835363, 0, -0.9999949325), z_dir=(0.9999949325, 0, 0.0031835363))):
            # Profile area: 197.2304797651, perimeter: 65.3076199413
            with BuildLine():
                Line((19.7461230417, 2.5575471879), (11.7461230417, 2.5575471879))
                Line((19.7461230417, 27.2113571586), (19.7461230417, 2.5575471879))
                Line((11.7461230417, 27.2113571586), (19.7461230417, 27.2113571586))
                Line((11.7461230417, 2.5575471879), (11.7461230417, 27.2113571586))
            make_face()
        # OneSide extrude, distance=-3
        extrude(amount=-3, mode=Mode.SUBTRACT)

        # Sketch14 -> Extrude13 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0.1047673172, 0, -32.9089340172), x_dir=(-0.9999949325, 0, -0.0031835363), z_dir=(0.0031835363, 0, -0.9999949325))):
            # Profile area: 553.0275017026, perimeter: 94.3702766546
            with BuildLine():
                Line((-99.2165210465, 1.7262188313), (-120.9165210465, 1.7262188313))
                Line((-99.2165210465, 27.2113571586), (-99.2165210465, 1.7262188313))
                Line((-120.9165210465, 27.2113571586), (-99.2165210465, 27.2113571586))
                Line((-120.9165210465, 1.7262188313), (-120.9165210465, 27.2113571586))
            make_face()
        # OneSide extrude, distance=-3
        extrude(amount=-3, mode=Mode.SUBTRACT)

        # Sketch16 -> Extrude14 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0.1047673172, 0, -32.9089340172), x_dir=(-0.9999949325, 0, -0.0031835363), z_dir=(0.0031835363, 0, -0.9999949325))):
            # Profile area: 557.4137348605, perimeter: 94.7745377752
            with BuildLine():
                Line((-63.3, 1.524088271), (-85, 1.524088271))
                Line((-63.3, 27.2113571586), (-63.3, 1.524088271))
                Line((-85, 27.2113571586), (-63.3, 27.2113571586))
                Line((-85, 1.524088271), (-85, 27.2113571586))
            make_face()
        # OneSide extrude, distance=-3
        extrude(amount=-3, mode=Mode.SUBTRACT)

        # Sketch17 -> Extrude15 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0.1047673172, 0, -32.9089340172), x_dir=(-0.9999949325, 0, -0.0031835363), z_dir=(0.0031835363, 0, -0.9999949325))):
            # Profile area: 210.4938795649, perimeter: 58.0430006407
            with BuildLine():
                Line((-59.196130965, 12.7732457722), (-59.196130965, 27.5447460925))
                Line((-44.946130965, 12.7732457722), (-59.196130965, 12.7732457722))
                Line((-44.946130965, 27.5447460925), (-44.946130965, 12.7732457722))
                Line((-59.196130965, 27.5447460925), (-44.946130965, 27.5447460925))
            make_face()
        # OneSide extrude, distance=-3.09
        extrude(amount=-3.09, mode=Mode.SUBTRACT)

        # Sketch18 -> Extrude16 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-0.0865372743, 0, -32.5626559953), x_dir=(-0.9999964687, 0, 0.0026575525), z_dir=(-0.0026575525, 0, -0.9999964687))):
            # Profile area: 90.7352910424, perimeter: 41.9492757516
            with BuildLine():
                Line((-35.3471021996, 12.6701082167), (-41.4471021996, 12.6701082167))
                Line((-35.3471021996, 27.5447460925), (-35.3471021996, 12.6701082167))
                Line((-41.4471021996, 27.5447460925), (-35.3471021996, 27.5447460925))
                Line((-41.4471021996, 12.6701082167), (-41.4471021996, 27.5447460925))
            make_face()
        # OneSide extrude, distance=-3
        extrude(amount=-3, mode=Mode.SUBTRACT)

        # Sketch19 -> Extrude17 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-0.0865372743, 0, -32.5626559953), x_dir=(-0.9999964687, 0, 0.0026575525), z_dir=(-0.0026575525, 0, -0.9999964687))):
            # Profile area: 218.1488183412, perimeter: 59.089492185
            with BuildLine():
                Line((-16.2071021996, 12.5), (-30.7071021996, 12.5))
                Line((-16.2071021996, 27.5447460925), (-16.2071021996, 12.5))
                Line((-30.7071021996, 27.5447460925), (-16.2071021996, 27.5447460925))
                Line((-30.7071021996, 12.5), (-30.7071021996, 27.5447460925))
            make_face()
        # OneSide extrude, distance=-3
        extrude(amount=-3, mode=Mode.SUBTRACT)

        # Sketch20 -> Extrude18 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(-0.0865372743, 0, -32.5626559953), x_dir=(-0.9999964687, 0, 0.0026575525), z_dir=(-0.0026575525, 0, -0.9999964687))):
            # Profile area: 467.1206430493, perimeter: 88.0384474005
            with BuildLine():
                Line((9.9528978004, 1.3755223923), (-7.8971021996, 1.3755223923))
                Line((9.9528978004, 27.5447460925), (9.9528978004, 1.3755223923))
                Line((-7.8971021996, 27.5447460925), (9.9528978004, 27.5447460925))
                Line((-7.8971021996, 1.3755223923), (-7.8971021996, 27.5447460925))
            make_face()
        # OneSide extrude, distance=-3
        extrude(amount=-3, mode=Mode.SUBTRACT)

        # Sketch21 -> Extrude19 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(-15.2126009828, 0, 0.040428429), x_dir=(-0.0026575525, 0, -0.9999964687), z_dir=(0.9999964687, 0, -0.0026575525))):
            # Profile area: 272.2342826186, perimeter: 70.5122627559
            with BuildLine():
                Line((52.8627709841, 2.8559975545), (52.8627709841, 26.6900617382))
                Line((52.8627709841, 26.6900617382), (41.4407037899, 26.6900617382))
                Line((41.4407037899, 26.6900617382), (41.4407037899, 2.8559975545))
                Line((41.4407037899, 2.8559975545), (52.8627709841, 2.8559975545))
            make_face()
        # OneSide extrude, distance=-3
        extrude(amount=-3, mode=Mode.SUBTRACT)

        # Sketch62 -> Extrude59 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2629.9233760015, perimeter: 209.8205646188
            with BuildLine():
                Line((60, 74.16033799), (60, 32.7332727127))
                Line((60, 32.7332727127), (123.4832170321, 32.7332727127))
                Line((123.4832170321, 32.7332727127), (123.4832170321, 74.16033799))
                Line((123.4832170321, 74.16033799), (60, 74.16033799))
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2)

        # Sketch63 -> Extrude60 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 25, perimeter: 20
            with BuildLine():
                Line((-65, -74.16033799), (-65, -69.16033799))
                Line((-60, -74.16033799), (-65, -74.16033799))
                Line((-60, -69.16033799), (-60, -74.16033799))
                Line((-65, -69.16033799), (-60, -69.16033799))
            make_face()
        # OneSide extrude, distance=27
        extrude(amount=27, mode=Mode.ADD)

        # Sketch64 -> Extrude61 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 25, perimeter: 20
            with BuildLine():
                Line((-118.4832170321, -69.16033799), (-123.4832170321, -69.16033799))
                Line((-123.4832170321, -69.16033799), (-123.4832170321, -74.16033799))
                Line((-123.4832170321, -74.16033799), (-118.4832170321, -74.16033799))
                Line((-118.4832170321, -74.16033799), (-118.4832170321, -69.16033799))
            make_face()
        # OneSide extrude, distance=27
        extrude(amount=27, mode=Mode.ADD)

        # Sketch65 -> Extrude62 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 25, perimeter: 20
            with BuildLine():
                Line((-94.24, -69.16033799), (-89.24, -69.16033799))
                Line((-94.24, -74.16033799), (-94.24, -69.16033799))
                Line((-89.24, -74.16033799), (-94.24, -74.16033799))
                Line((-89.24, -69.16033799), (-89.24, -74.16033799))
            make_face()
        # OneSide extrude, distance=27
        extrude(amount=27, mode=Mode.ADD)

        # Sketch66 -> Extrude63 (Join)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 29, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2629.9233760015, perimeter: 209.8205646188
            with BuildLine():
                Line((-123.4832170321, -32.7332727127), (-60, -32.7332727127))
                Line((-123.4832170321, -74.16033799), (-123.4832170321, -32.7332727127))
                Line((-60, -74.16033799), (-123.4832170321, -74.16033799))
                Line((-60, -32.7332727127), (-60, -74.16033799))
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2, mode=Mode.ADD)
    return part.part


def model_66233_25aede4b_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 12000, perimeter: 520
            with BuildLine():
                Line((3, -62.5), (3, -2.5))
                Line((3, -2.5), (-197, -2.5))
                Line((-197, -2.5), (-197, -62.5))
                Line((-197, -62.5), (3, -62.5))
            make_face()
        # OneSide extrude, distance=90
        extrude(amount=90)

        # Sketch5 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 7263.3944946442, perimeter: 1187.1431191431
            with BuildLine():
                Line((-241.0715595715, 10), (-241.0715595715, -2.5))
                Line((-241.0715595715, -2.5), (340, -2.5))
                Line((340, -2.5), (340, 10))
                Line((340, 10), (-241.0715595715, 10))
            make_face()
        # OneSide extrude, distance=300
        extrude(amount=300, mode=Mode.ADD)

        # Sketch2 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 85 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 62.5), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 126, perimeter: 252
            with BuildLine():
                Line((-153, 63), (-194, 63))
                Line((-153, 87), (-153, 63))
                Line((-194, 87), (-153, 87))
                Line((-194, 63), (-194, 87))
            make_face()
            with BuildLine():
                Line((-154, 86), (-193, 86))
                Line((-154, 64), (-154, 86))
                Line((-193, 64), (-154, 64))
                Line((-193, 86), (-193, 64))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=3
        extrude(amount=3, mode=Mode.ADD)

        # Sketch2 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 85 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 62.5), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 126, perimeter: 252
            with BuildLine():
                Line((-153, 33), (-194, 33))
                Line((-153, 57), (-153, 33))
                Line((-194, 57), (-153, 57))
                Line((-194, 33), (-194, 57))
            make_face()
            with BuildLine():
                Line((-154, 56), (-193, 56))
                Line((-154, 34), (-154, 56))
                Line((-193, 34), (-154, 34))
                Line((-193, 56), (-193, 34))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=3
        extrude(amount=3, mode=Mode.ADD)

        # Sketch2 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 85 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 62.5), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 126, perimeter: 252
            with BuildLine():
                Line((-153, 3), (-194, 3))
                Line((-153, 27), (-153, 3))
                Line((-194, 27), (-153, 27))
                Line((-194, 3), (-194, 27))
            make_face()
            with BuildLine():
                Line((-154, 26), (-193, 26))
                Line((-154, 4), (-154, 26))
                Line((-193, 4), (-154, 4))
                Line((-193, 26), (-193, 4))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=3
        extrude(amount=3, mode=Mode.ADD)

        # Sketch2 -> Extrude6 (Join)
        # Sketch on BRepFace
        # Sketch has 85 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 62.5), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 252, perimeter: 504
            with BuildLine():
                Line((-147, 87), (-147, 3))
                Line((-147, 3), (-103, 3))
                Line((-103, 3), (-103, 87))
                Line((-103, 87), (-147, 87))
            make_face()
            with BuildLine():
                Line((-104, 86), (-146, 86))
                Line((-104, 4), (-104, 86))
                Line((-146, 4), (-104, 4))
                Line((-146, 86), (-146, 4))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=3
        extrude(amount=3, mode=Mode.ADD)

        # Sketch2 -> Extrude7 (Join)
        # Sketch on BRepFace
        # Sketch has 85 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 62.5), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 252, perimeter: 504
            with BuildLine():
                Line((-53, 3), (-97, 3))
                Line((-53, 87), (-53, 3))
                Line((-97, 87), (-53, 87))
                Line((-97, 3), (-97, 87))
            make_face()
            with BuildLine():
                Line((-96, 4), (-96, 86))
                Line((-96, 86), (-54, 86))
                Line((-54, 86), (-54, 4))
                Line((-54, 4), (-96, 4))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=3
        extrude(amount=3, mode=Mode.ADD)

        # Sketch2 -> Extrude8 (Join)
        # Sketch on BRepFace
        # Sketch has 85 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 62.5), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 135.7915995462, perimeter: 275.8159666289
            with BuildLine():
                Line((-47, 87), (-47, 63))
                Line((-47, 63), (-0.0920166856, 63))
                Line((-0.0920166856, 63), (-0.0920166856, 87))
                Line((-0.0920166856, 87), (-47, 87))
            make_face()
            with BuildLine():
                Line((-1, 86), (-46, 86))
                Line((-1, 64), (-1, 86))
                Line((-46, 64), (-1, 64))
                Line((-46, 86), (-46, 64))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=3
        extrude(amount=3, mode=Mode.ADD)

        # Sketch2 -> Extrude9 (Join)
        # Sketch on BRepFace
        # Sketch has 85 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 62.5), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 138, perimeter: 276
            with BuildLine():
                Line((-47, 57), (-47, 33))
                Line((-47, 33), (0, 33))
                Line((0, 33), (0, 57))
                Line((0, 57), (-47, 57))
            make_face()
            with BuildLine():
                Line((-1, 56), (-46, 56))
                Line((-1, 34), (-1, 56))
                Line((-46, 34), (-1, 34))
                Line((-46, 56), (-46, 34))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=3
        extrude(amount=3, mode=Mode.ADD)

        # Sketch2 -> Extrude10 (Join)
        # Sketch on BRepFace
        # Sketch has 85 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 62.5), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 138, perimeter: 276
            with BuildLine():
                Line((-47, 27), (-47, 3))
                Line((-47, 3), (0, 3))
                Line((0, 3), (0, 27))
                Line((0, 27), (-47, 27))
            make_face()
            with BuildLine():
                Line((-1, 26), (-46, 26))
                Line((-1, 4), (-1, 26))
                Line((-46, 4), (-1, 4))
                Line((-46, 26), (-46, 4))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=3
        extrude(amount=3, mode=Mode.ADD)

        # Sketch7 -> Extrude11 (NewBody)
        # Sketch on BRepFace
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 90, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 431.6401927932, perimeter: 648.2000019699
            with BuildLine():
                Line((-4.3000000492, 63.8000009358), (198.5, 63.8000009358))
                Line((-4.3000000492, 2.5), (-4.3000000492, 63.8000009358))
                Line((-3, 2.5), (-4.3000000492, 2.5))
                Line((-3, 62.5), (-3, 2.5))
                Line((197, 62.5), (-3, 62.5))
                Line((197, 2.5), (197, 62.5))
                Line((198.5, 2.5), (197, 2.5))
                Line((198.5, 63.8000009358), (198.5, 2.5))
            make_face()
        # OneSide extrude, distance=5
        extrude(amount=5)

        # Sketch8 -> Extrude12 (Join)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 95, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 12000, perimeter: 520
            with BuildLine():
                Line((197, 2.5), (-3, 2.5))
                Line((197, 62.5), (197, 2.5))
                Line((-3, 62.5), (197, 62.5))
                Line((-3, 2.5), (-3, 62.5))
            make_face()
        # OneSide extrude, distance=-5
        extrude(amount=-5, mode=Mode.ADD)

        # Sketch6 -> Extrude13 (Join)
        # Sketch on BRepFace
        # Sketch has 8 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 2.5), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 2750, perimeter: 1100
            with BuildLine():
                Line((-180, 220), (-180, 100))
                Line((-180, 100), (-15, 100))
                Line((-15, 100), (-15, 220))
                Line((-15, 220), (-180, 220))
            make_face()
            with BuildLine():
                Line((-175, 105), (-175, 215))
                Line((-175, 215), (-20, 215))
                Line((-20, 215), (-20, 105))
                Line((-20, 105), (-175, 105))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=5
        extrude(amount=5, mode=Mode.ADD)

        # Sketch9 -> Extrude14 (Join)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 289100, perimeter: 2160
            with BuildLine():
                Line((320, -390), (-270, -390))
                Line((320, 100), (320, -390))
                Line((-270, 100), (320, 100))
                Line((-270, -390), (-270, 100))
            make_face()
        # OneSide extrude, distance=-20
        extrude(amount=-20, mode=Mode.ADD)
    return part.part


def model_69057_8b7468bb_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 324, perimeter: 72
            with BuildLine():
                Line((-9, 9), (9, 9))
                Line((-9, -9), (-9, 9))
                Line((9, -9), (-9, -9))
                Line((9, 9), (9, -9))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 19 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 5.0306266468, perimeter: 9.9591592843
            with BuildLine():
                Line((9, -2), (9, 1.5707277038))
                Line((7.5911480617, 1.5707277038), (9, 1.5707277038))
                Line((7.5911480617, -2), (7.5911480617, 1.5707277038))
                Line((9, -2), (7.5911480617, -2))
            make_face()
            # Profile area: 17.5557253397, perimeter: 16.786236434
            with BuildLine():
                Line((2, 9), (-2.4318950627, 9))
                Line((-2.4318950627, 9), (-2.4318950627, 5.0387768457))
                Line((-2.4318950627, 5.0387768457), (2, 5.0387768457))
                Line((2, 5.0387768457), (2, 9))
            make_face()
            # Profile area: 17.757538057, perimeter: 16.9422050639
            with BuildLine():
                Line((-9, 0.8085191012), (-9, -3))
                Line((-9, -3), (-4.3374165692, -3))
                Line((-4.3374165692, -3), (-4.3374165692, 0.8085191012))
                Line((-4.3374165692, 0.8085191012), (-9, 0.8085191012))
            make_face()
            # Profile area: 8.1673231928, perimeter: 13.6939814371
            with BuildLine():
                Line((-3.3084349557, -9), (-3.3084349557, -7.4614442372))
                Line((2, -9), (-3.3084349557, -9))
                Line((2, -7.4614442372), (2, -9))
                Line((-3.3084349557, -7.4614442372), (2, -7.4614442372))
            make_face()
        # OneSide extrude, distance=1.2
        extrude(amount=1.2, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 148.6926169129, perimeter: 48.7878470859
            with BuildLine():
                Line((-4.3374165692, -7.4614442372), (-4.3374165692, -3))
                Line((-3.3084349557, -7.4614442372), (-4.3374165692, -7.4614442372))
                Line((2, -7.4614442372), (-3.3084349557, -7.4614442372))
                Line((7.5911480617, -7.4614442372), (2, -7.4614442372))
                Line((7.5911480617, -2), (7.5911480617, -7.4614442372))
                Line((7.5911480617, 1.5707277038), (7.5911480617, -2))
                Line((7.5911480617, 4.968847531), (7.5911480617, 1.5707277038))
                Line((-4.3374165692, 5.0387768457), (7.5911480617, 4.968847531))
                Line((-4.3374165692, 0.8085191012), (-4.3374165692, 5.0387768457))
                Line((-4.3374165692, -3), (-4.3374165692, 0.8085191012))
            make_face()
        # OneSide extrude, distance=0.7
        extrude(amount=0.7, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2.2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            with Locations((0.807830926, 8.0704834661)):
                Circle(0.4)
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            with Locations((0.6492574402, 6.0090281508)):
                Circle(0.4)
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            with Locations((-1.5390566638, 6.0090281508)):
                Circle(0.4)
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            with Locations((-1.5390566638, 8.0704834661)):
                Circle(0.4)
        # OneSide extrude, distance=-0.1
        extrude(amount=-0.1, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude5 (Cut)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 2.2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2827433472, perimeter: 1.8849556202
            with Locations((8.3000001237, 1.0000000149)):
                Circle(0.3000000045)
            # Profile area: 0.3141592747, perimeter: 1.9869176828
            with Locations((8.3000001237, -1.0000000149)):
                Circle(0.3162277707)
        # OneSide extrude, distance=-0.1
        extrude(amount=-0.1, mode=Mode.SUBTRACT)

        # Sketch6 -> Extrude6 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2.2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            with Locations((-5.5, 0)):
                Circle(0.4)
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            with Locations((-5.5, -2)):
                Circle(0.4)
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            with Locations((-8, 0)):
                Circle(0.4)
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            with Locations((-8, -2)):
                Circle(0.4)
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.SUBTRACT)

        # Sketch11 -> Extrude10 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2.2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            with Locations((0.6000000089, -8.3000001237)):
                Circle(0.4)
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            with Locations((-2.0000000298, -8.3000001237)):
                Circle(0.4)
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2, mode=Mode.SUBTRACT)

        # Sketch7 -> Extrude11 (Join)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 1.7, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            with Locations((0, -5)):
                Circle(1)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1, mode=Mode.ADD)

        # Sketch12 -> Extrude12 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.8, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.755157754, perimeter: 4.9315493753
            with BuildLine():
                Line((0.4054679543, -4.2850480628), (-0.416432563, -4.2913784826))
                Line((-0.416432563, -4.2913784826), (-0.8219005173, -5.0063304198))
                Line((-0.8219005173, -5.0063304198), (-0.4054679543, -5.7149519372))
                Line((-0.4054679543, -5.7149519372), (0.416432563, -5.7086215174))
                Line((0.416432563, -5.7086215174), (0.8219005173, -4.9936695802))
                Line((0.8219005173, -4.9936695802), (0.4054679543, -4.2850480628))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)

        # Sketch13 -> Extrude13 (Join)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 2.3, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.439762609, perimeter: 2.3507913406
            with Locations((0, -5)):
                Circle(0.374140062)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)

        # Sketch14 -> Extrude14 (Join)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 1.7, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.2395188155, perimeter: 3.9466761736
            with Locations((6, -4)):
                Circle(0.6281330218)
            # Profile area: 1.2646545245, perimeter: 3.9864918731
            with Locations((2, 4)):
                Circle(0.6344698872)
            # Profile area: 0.4131246261, perimeter: 2.2853824086
            with BuildLine():
                Line((-4.3374165692, -2.8611388061), (-4.3374165692, -3.1388611939))
                CenterArc((-4, -3), 0.3648730908, -157.6307609538, 315.2615219077)
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)

        # Sketch15 -> Extrude15 (Join)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 1.7, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.926990817, perimeter: 7.024814731
            with Locations((-3, 3.5)):
                Circle(1.1180339887)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1, mode=Mode.ADD)

        # Sketch16 -> Extrude16 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.8, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.4247921104, perimeter: 5.7964562505
            with BuildLine():
                Line((-2.1633536059, 3.9830380209), (-3, 4.4660760417))
                Line((-3, 4.4660760417), (-3.8366463941, 3.9830380209))
                Line((-3.8366463941, 3.9830380209), (-3.8366463941, 3.0169619791))
                Line((-3.8366463941, 3.0169619791), (-3, 2.5339239583))
                Line((-3, 2.5339239583), (-2.1633536059, 3.0169619791))
                Line((-2.1633536059, 3.0169619791), (-2.1633536059, 3.9830380209))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)

        # Sketch17 -> Extrude17 (Join)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 2.3, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.5880394411, perimeter: 2.7183674425
            with Locations((-3, 3.5)):
                Circle(0.4326416156)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)
    return part.part


def model_92034_24dd7722_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 15 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 111.1415926536, perimeter: 44.2831853072
            with BuildLine():
                CenterArc((-7, -2.5), 1, 180, 90)
                Line((7, -3.5), (-7, -3.5))
                CenterArc((7, -2.5), 1, -90, 90)
                Line((8, 2.5), (8, -2.5))
                CenterArc((7, 2.5), 1, 0, 90)
                Line((-7, 3.5), (7, 3.5))
                CenterArc((-7, 2.5), 1, 90, 90)
                Line((-8, -2.5), (-8, 2.5))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 7 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 78, perimeter: 38
            with BuildLine():
                Line((-6.5, 3), (6.5, 3))
                Line((-6.5, -3), (-6.5, 3))
                Line((6.5, -3), (-6.5, -3))
                Line((6.5, 3), (6.5, -3))
            make_face()
        # OneSide extrude, distance=-0.1
        extrude(amount=-0.1, mode=Mode.ADD)

        # Sketch21 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 7 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 78, perimeter: 38
            with BuildLine():
                Line((-6.5, 3), (6.5, 3))
                Line((-6.5, -3), (-6.5, 3))
                Line((6.5, -3), (-6.5, -3))
                Line((6.5, 3), (6.5, -3))
            make_face()
        # OneSide extrude, distance=-0.1
        extrude(amount=-0.1, mode=Mode.SUBTRACT)

        # Sketch22 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 12 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 3.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1578539864, perimeter: 1.9141592952
            with BuildLine():
                CenterArc((5.8500000864, 0.5500000089), 0.05, 90, 90)
                Line((5.8000000864, 0.5500000089), (5.8000000864, 0.450000006))
                CenterArc((5.8500000864, 0.450000006), 0.05, 180, 90)
                Line((5.8500000864, 0.400000006), (6.5500000983, 0.400000006))
                CenterArc((6.5500000983, 0.450000006), 0.05, -90, 90)
                Line((6.6000000983, 0.450000006), (6.6000000983, 0.5500000089))
                CenterArc((6.5500000983, 0.5500000089), 0.05, 0, 90)
                Line((6.5500000983, 0.6000000089), (5.8500000864, 0.6000000089))
            make_face()
        # OneSide extrude, distance=0.1
        extrude(amount=0.1, mode=Mode.ADD)

        # Sketch23 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 12 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 3.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0578539834, perimeter: 0.9141592803
            with BuildLine():
                CenterArc((5.5500000834, 0.5500000089), 0.05, 0, 90)
                Line((5.5500000834, 0.6000000089), (5.350000079, 0.6000000089))
                CenterArc((5.350000079, 0.5500000089), 0.05, 90, 90)
                Line((5.300000079, 0.5500000089), (5.300000079, 0.450000006))
                CenterArc((5.350000079, 0.450000006), 0.05, 180, 90)
                Line((5.350000079, 0.400000006), (5.5500000834, 0.400000006))
                CenterArc((5.5500000834, 0.450000006), 0.05, -90, 90)
                Line((5.6000000834, 0.450000006), (5.6000000834, 0.5500000089))
            make_face()
        # OneSide extrude, distance=0.1
        extrude(amount=0.1, mode=Mode.ADD)
    return part.part


MODELS = {
    "model_28446_d757d32d_0017": {"func": model_28446_d757d32d_0017, "volume": 317.1839999986, "area": 2148.8},
    "model_28934_b02386fd_0000": {"func": model_28934_b02386fd_0000, "volume": 2.5946140084, "area": 27.6454003442},
    "model_31360_a1accb4b_0002": {"func": model_31360_a1accb4b_0002, "volume": 0.3535173331, "area": 4.883799483},
    "model_31667_a38ff7b3_0000": {"func": model_31667_a38ff7b3_0000, "volume": 313.5231475827, "area": 1615.5328330655},
    "model_34317_e9c65aa6_0015": {"func": model_34317_e9c65aa6_0015, "volume": 4859.4913925588, "area": 3352.1542898038},
    "model_36088_1ea9c8a9_0003": {"func": model_36088_1ea9c8a9_0003, "volume": 1.356561699, "area": 13.2724435633},
    "model_36920_08b32825_0000": {"func": model_36920_08b32825_0000, "volume": 8.4810704033, "area": 40.2803644241},
    "model_38757_2c865215_0008": {"func": model_38757_2c865215_0008, "volume": 3207.9211463402, "area": 1787.8974358866},
    "model_48907_25974aa4_0011": {"func": model_48907_25974aa4_0011, "volume": 7.168048132, "area": 57.1081965969},
    "model_49896_6387ac02_0000": {"func": model_49896_6387ac02_0000, "volume": 2834.2289835695, "area": 4719.2766379615},
    "model_52221_3cdb5865_0000": {"func": model_52221_3cdb5865_0000, "volume": 4789.7188259266, "area": 5649.3154566903},
    "model_54273_21c2b38f_0019": {"func": model_54273_21c2b38f_0019, "volume": 2.6437099807, "area": 21.5871167414},
    "model_55556_429d33b3_0000": {"func": model_55556_429d33b3_0000, "volume": 245.3261291059, "area": 415.4238206044},
    "model_57629_0877c022_0000": {"func": model_57629_0877c022_0000, "volume": 10.9346372102, "area": 68.4131280503},
    "model_60747_5e38b665_0000": {"func": model_60747_5e38b665_0000, "volume": 2717235449.113881588, "area": 20217103.0334011838},
    "model_63411_46a912fc_0000": {"func": model_63411_46a912fc_0000, "volume": 185.517850659, "area": 652.7096858806},
    "model_65810_620a5516_0000": {"func": model_65810_620a5516_0000, "volume": 622676.9948002216, "area": 78467.7947296332},
    "model_66233_25aede4b_0000": {"func": model_66233_25aede4b_0000, "volume": 9120807.924155863, "area": 1003594.6640377523},
    "model_69057_8b7468bb_0000": {"func": model_69057_8b7468bb_0000, "volume": 489.6005472389, "area": 826.8707882746},
    "model_92034_24dd7722_0000": {"func": model_92034_24dd7722_0000, "volume": 103.3631634506, "area": 270.6492024719},
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
