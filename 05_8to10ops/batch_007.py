"""Batch 007 - passing/05_8to10ops
60 models bundled from Fusion360 Gallery reconstructions.
"""

from build123d import *


def model_40603_f38d1b3d_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 10.8222157059, perimeter: 36.6865055733
            with BuildLine():
                Line((-11.5960838366, 1.8146305768), (0.1609634074, 1.8146305768))
                Line((-11.5960838366, 1.225227153), (-11.5960838366, 1.8146305768))
                Line((0.5952606671, 1.225227153), (-11.5960838366, 1.225227153))
                Line((5.6207003862, 3.5518196155), (0.5952606671, 1.225227153))
                Line((5.6207003862, 4.203265505), (5.6207003862, 3.5518196155))
                Line((0.1609634074, 1.8146305768), (5.6207003862, 4.203265505))
            make_face()
        # OneSide extrude, distance=17
        extrude(amount=17)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.8146305768, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.2953235943, perimeter: 6.3748967262
            with BuildLine():
                Line((-6.1811083413, 4.3653275585), (-4.0927801035, 4.3653275585))
                Line((-6.1811083413, 3.2662074333), (-6.1811083413, 4.3653275585))
                Line((-4.0927801035, 3.2662074333), (-6.1811083413, 3.2662074333))
                Line((-4.0927801035, 4.3653275585), (-4.0927801035, 3.2662074333))
            make_face()
        # OneSide extrude, distance=0.3
        extrude(amount=0.3, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.8146305768, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.3742239552, perimeter: 6.1323284997
            with BuildLine():
                Line((-3.1741109391, 4.1420499124), (-0.6530425559, 4.1420499124))
                Line((-3.1741109391, 3.5969540457), (-3.1741109391, 4.1420499124))
                Line((-0.6530425559, 3.5969540457), (-3.1741109391, 3.5969540457))
                Line((-0.6530425559, 4.1420499124), (-0.6530425559, 3.5969540457))
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.8146305768, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.5451652137, perimeter: 9.5045122857
            with BuildLine():
                Line((-4.7117710735, 2.1340666643), (-1.2864435939, 2.1340666643))
                Line((-4.7117710735, 0.8071380011), (-4.7117710735, 2.1340666643))
                Line((-1.2864435939, 0.8071380011), (-4.7117710735, 0.8071380011))
                Line((-1.2864435939, 2.1340666643), (-1.2864435939, 0.8071380011))
            make_face()
        # OneSide extrude, distance=-0.05
        extrude(amount=-0.05, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.4639918886, 0.6404964513), x_dir=(1, 0, 0), z_dir=(0, 0.9161573349, 0.400818834))):
            # Profile area: 68.3117476993, perimeter: 39.1906837752
            with BuildLine():
                Line((16.0848696254, 1.6337550161), (1.0257722378, 1.6337550161))
                Line((16.0848696254, 6.1699995161), (16.0848696254, 1.6337550161))
                Line((1.0257722378, 6.1699995161), (16.0848696254, 6.1699995161))
                Line((1.0257722378, 1.6337550161), (1.0257722378, 6.1699995161))
            make_face()
        # OneSide extrude, distance=-0.05
        extrude(amount=-0.05, mode=Mode.SUBTRACT)
    return part.part


def model_40997_e3c88650_0001():
    """Model: Component 8 / basculante"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 37 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 45.6104226539, perimeter: 93.9509709311
            with BuildLine():
                Line((10.0571128277, 2), (12.5, 2))
                CenterArc((12.5, 2.25), 0.25, -90, 180)
                Line((10, 2.5), (12.5, 2.5))
                CenterArc((10.5753349642, -6.187158018), 8.7061888764, 93.7890638033, 31.7517308631)
                Line((4.4854199208, 0.8970839842), (5.5145800792, 0.8970839842))
                CenterArc((-0.5753349642, -6.187158018), 8.7061888764, 54.4592053336, 31.7517308631)
                Line((-12.5, 2.5), (0, 2.5))
                CenterArc((-12.5, 2.25), 0.25, 90, 180)
                Line((-12.5, 2), (-1.5, 2))
                CenterArc((-1.5, 0), 2, -90, 180)
                Line((-1.5, -2), (-12.5, -2))
                CenterArc((-12.5, -2.25), 0.25, 90, 180)
                Line((0, -2.5), (-12.5, -2.5))
                CenterArc((-0.5753349642, 6.187158018), 8.7061888764, -86.2109361967, 31.7517308631)
                Line((4.4854199208, -0.8970839842), (5.5145800792, -0.8970839842))
                CenterArc((10.5753349642, 6.187158018), 8.7061888764, -125.5407946664, 31.7517308631)
                Line((12.5, -2.5), (10, -2.5))
                CenterArc((12.5, -2.25), 0.25, -90, 180)
                Line((10.0571128277, -2), (12.5, -2))
                CenterArc((10.0571128277, 0), 2, 90, 180)
            make_face()
        # Symmetric extrude, each_side=2.5
        extrude(amount=2.5, both=True)

        # Sketch3 -> Extrude2 (Cut)
        # Sketch on XY construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((-10, 0)):
                Circle(0.5)
        # Symmetric extrude, each_side=2.5
        extrude(amount=2.5, both=True, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude3 (Cut)
        # Sketch on XY construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((11.2759446831, 0)):
                Circle(0.5)
        # Symmetric extrude, each_side=3
        extrude(amount=3, both=True, mode=Mode.SUBTRACT)
    return part.part


def model_40999_cad6be09_0018():
    """Model: Spoiler"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 426.2599512463, perimeter: 95.2199112069
            with BuildLine():
                Line((183.3253304747, 53.7811305406), (200.737469634, 53.7811305406))
                Line((189.2299971581, 74.9299988747), (200.737469634, 53.7811305406))
                Line((168.1921289259, 81.5935009547), (189.2299971581, 74.9299988747))
                Line((183.3253304747, 53.7811305406), (168.1921289259, 81.5935009547))
            make_face()
        # OneSide extrude, distance=2.54
        extrude(amount=2.54)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2.54, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 11.032415892, perimeter: 20.5273672599
            with BuildLine():
                Line((-189.0574137894, -66.1019154089), (-180.0483746308, -67.388921003))
                Line((-189.2299971581, -67.3099989891), (-189.0574137894, -66.1019154089))
                Line((-180.3399972916, -68.57999897), (-189.2299971581, -67.3099989891))
                Line((-180.0483746308, -67.388921003), (-180.3399972916, -68.57999897))
            make_face()
        # OneSide extrude, distance=182.88
        extrude(amount=182.88, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 9 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 185.42, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 415.2275353543, perimeter: 115.7472784668
            with BuildLine():
                Line((-200.737469634, -53.7811305406), (-189.2299971581, -74.9299988747))
                Line((-189.2299971581, -74.9299988747), (-168.1921289259, -81.5935009547))
                Line((-168.1921289259, -81.5935009547), (-183.3253304747, -53.7811305406))
                Line((-200.737469634, -53.7811305406), (-183.3253304747, -53.7811305406))
            make_face()
            with BuildLine():
                Line((-189.2299971581, -67.3099989891), (-180.3399972916, -68.57999897))
                Line((-189.0574137894, -66.1019154089), (-189.2299971581, -67.3099989891))
                Line((-180.0483746308, -67.388921003), (-189.0574137894, -66.1019154089))
                Line((-180.3399972916, -68.57999897), (-180.0483746308, -67.388921003))
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 11.032415892, perimeter: 20.5273672599
            with BuildLine():
                Line((-180.3399972916, -68.57999897), (-180.0483746308, -67.388921003))
                Line((-180.0483746308, -67.388921003), (-189.0574137894, -66.1019154089))
                Line((-189.0574137894, -66.1019154089), (-189.2299971581, -67.3099989891))
                Line((-189.2299971581, -67.3099989891), (-180.3399972916, -68.57999897))
            make_face()
        # OneSide extrude, distance=2.54
        extrude(amount=2.54, mode=Mode.ADD)
    return part.part


def model_40999_cad6be09_0019():
    """Model: Gas pedal"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 232.2575930237, perimeter: 66.0399990082
            with BuildLine():
                Line((99.0599985123, 101.5999984741), (88.8999986649, 101.5999984741))
                Line((88.8999986649, 101.5999984741), (88.8999986649, 78.7399988174))
                Line((88.8999986649, 78.7399988174), (99.0599985123, 78.7399988174))
                Line((99.0599985123, 78.7399988174), (99.0599985123, 101.5999984741))
            make_face()
        # OneSide extrude, distance=5.08
        extrude(amount=5.08)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 20 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(5.08, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 3.2257999031, perimeter: 7.6199998856
            with BuildLine():
                Line((92.7099986076, 97.7899985313), (92.7099986076, 96.5199985504))
                Line((92.7099986076, 96.5199985504), (95.2499985695, 96.5199985504))
                Line((95.2499985695, 97.7899985313), (95.2499985695, 96.5199985504))
                Line((92.7099986076, 97.7899985313), (95.2499985695, 97.7899985313))
            make_face()
            # Profile area: 3.2257999031, perimeter: 7.6199998856
            with BuildLine():
                Line((95.2499985695, 93.9799985886), (92.7099986076, 93.9799985886))
                Line((92.7099986076, 93.9799985886), (92.7099986076, 92.7099986076))
                Line((92.7099986076, 92.7099986076), (95.2499985695, 92.7099986076))
                Line((95.2499985695, 92.7099986076), (95.2499985695, 93.9799985886))
            make_face()
            # Profile area: 3.2257999031, perimeter: 7.6199998856
            with BuildLine():
                Line((95.2499985695, 90.1699986458), (92.7099986076, 90.1699986458))
                Line((92.7099986076, 90.1699986458), (92.7099986076, 88.8999986649))
                Line((92.7099986076, 88.8999986649), (95.2499985695, 88.8999986649))
                Line((95.2499985695, 88.8999986649), (95.2499985695, 90.1699986458))
            make_face()
            # Profile area: 3.2257999031, perimeter: 7.6199998856
            with BuildLine():
                Line((95.2499985695, 86.359998703), (92.7099986076, 86.359998703))
                Line((92.7099986076, 86.359998703), (92.7099986076, 85.0899987221))
                Line((92.7099986076, 85.0899987221), (95.2499985695, 85.0899987221))
                Line((95.2499985695, 85.0899987221), (95.2499985695, 86.359998703))
            make_face()
            # Profile area: 3.2257999031, perimeter: 7.6199998856
            with BuildLine():
                Line((95.2499985695, 82.5499987602), (92.7099986076, 82.5499987602))
                Line((92.7099986076, 82.5499987602), (92.7099986076, 81.2799987793))
                Line((92.7099986076, 81.2799987793), (95.2499985695, 81.2799987793))
                Line((95.2499985695, 81.2799987793), (95.2499985695, 82.5499987602))
            make_face()
        # OneSide extrude, distance=-1.27
        extrude(amount=-1.27, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 25.8063992249, perimeter: 20.3199996948
            with BuildLine():
                Line((-91.4399986267, 99.0599985123), (-96.5199985504, 99.0599985123))
                Line((-96.5199985504, 99.0599985123), (-96.5199985504, 93.9799985886))
                Line((-96.5199985504, 93.9799985886), (-91.4399986267, 93.9799985886))
                Line((-91.4399986267, 93.9799985886), (-91.4399986267, 99.0599985123))
            make_face()
        # OneSide extrude, distance=7.62
        extrude(amount=7.62, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 99.0599985123, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 6.4515998062, perimeter: 10.1599998474
            with BuildLine():
                Line((2.5399999619, -92.7099986076), (2.5399999619, -95.2499985695))
                Line((2.5399999619, -95.2499985695), (5.0799999237, -95.2499985695))
                Line((5.0799999237, -95.2499985695), (5.0799999237, -92.7099986076))
                Line((5.0799999237, -92.7099986076), (2.5399999619, -92.7099986076))
            make_face()
        # OneSide extrude, distance=-2.54
        extrude(amount=-2.54, mode=Mode.SUBTRACT)
    return part.part


def model_41117_1b3271f2_0000():
    """Model: ATmega328p Seat v9"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 141 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.5028325843, perimeter: 9.4635148575
            with BuildLine():
                Line((6.3950184195, -4.2134071317), (6.3950184195, -4.0610071317))
                Line((6.3950184195, -4.0610071317), (2.9152184195, -4.0610071317))
                Line((2.9152184195, -4.2134071317), (2.9152184195, -4.0610071317))
                Line((6.3950184195, -4.2134071317), (2.9152184195, -4.2134071317))
            make_face()
            with BuildLine():
                CenterArc((3.2801184195, -4.1372071317), 0.025, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((3.0301184195, -4.1372071317), 0.025, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((4.2801184195, -4.1372071317), 0.025, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((3.7801184195, -4.1372071317), 0.025, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((4.5301184195, -4.1372071317), 0.025, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((3.5301184195, -4.1372071317), 0.025, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((5.7801184195, -4.1372071317), 0.025, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((5.2801184195, -4.1372071317), 0.025, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((6.2801184195, -4.1372071317), 0.025, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((5.5301184195, -4.1372071317), 0.025, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((5.0301184195, -4.1372071317), 0.025, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((6.0301184195, -4.1372071317), 0.025, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((4.0301184195, -4.1372071317), 0.025, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((4.7801184195, -4.1372071317), 0.025, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.5028325843, perimeter: 9.4635148575
            with BuildLine():
                Line((6.3950184195, -3.3880071317), (2.9152184195, -3.3880071317))
                Line((6.3950184195, -3.3880071317), (6.3950184195, -3.2356071317))
                Line((6.3950184195, -3.2356071317), (2.9152184195, -3.2356071317))
                Line((2.9152184195, -3.3880071317), (2.9152184195, -3.2356071317))
            make_face()
            with BuildLine():
                CenterArc((3.0301184195, -3.3118071317), 0.025, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((3.2801184195, -3.3118071317), 0.025, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((3.5301184195, -3.3118071317), 0.025, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((3.7801184195, -3.3118071317), 0.025, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((4.2801184195, -3.3118071317), 0.025, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((4.5301184195, -3.3118071317), 0.025, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((4.0301184195, -3.3118071317), 0.025, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((4.7801184195, -3.3118071317), 0.025, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((5.7801184195, -3.3118071317), 0.025, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((5.0301184195, -3.3118071317), 0.025, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((5.5301184195, -3.3118071317), 0.025, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((5.2801184195, -3.3118071317), 0.025, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((6.0301184195, -3.3118071317), 0.025, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((6.2801184195, -3.3118071317), 0.025, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.4
        extrude(amount=0.4)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 141 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.3419054, perimeter: 8.3056
            with BuildLine():
                Line((6.3950184195, -4.0610071317), (6.3950184195, -3.3880071317))
                Line((6.3950184195, -3.3880071317), (2.9152184195, -3.3880071317))
                Line((2.9152184195, -4.0610071317), (2.9152184195, -3.3880071317))
                Line((6.3950184195, -4.0610071317), (2.9152184195, -4.0610071317))
            make_face()
        # OneSide extrude, distance=0.3
        extrude(amount=0.3, mode=Mode.ADD)

        # Sketch1 -> Extrude3 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 141 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0007068583, perimeter: 0.2827433388
            with BuildLine():
                CenterArc((6.2801184195, -4.1372071317), 0.025, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((6.2801184195, -4.1372071317), 0.02, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0012566371, perimeter: 0.1256637061
            with Locations((6.2801184195, -4.1372071317)):
                Circle(0.02)
        # OneSide extrude, distance=-0.17
        extrude(amount=-0.17)

        # Sketch1 -> Extrude4 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 141 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0007068583, perimeter: 0.2827433388
            with BuildLine():
                CenterArc((5.7801184195, -4.1372071317), 0.025, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((5.7801184195, -4.1372071317), 0.02, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0012566371, perimeter: 0.1256637061
            with Locations((5.7801184195, -4.1372071317)):
                Circle(0.02)
        # OneSide extrude, distance=-0.17
        extrude(amount=-0.17)

        # Sketch1 -> Extrude5 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 141 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0007068583, perimeter: 0.2827433388
            with BuildLine():
                CenterArc((6.0301184195, -4.1372071317), 0.025, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((6.0301184195, -4.1372071317), 0.02, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0012566371, perimeter: 0.1256637061
            with Locations((6.0301184195, -4.1372071317)):
                Circle(0.02)
        # OneSide extrude, distance=-0.17
        extrude(amount=-0.17)

        # Sketch1 -> Extrude6 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 141 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0007068583, perimeter: 0.2827433388
            with BuildLine():
                CenterArc((3.0301184195, -4.1372071317), 0.025, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((3.0301184195, -4.1372071317), 0.02, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0007068583, perimeter: 0.2827433388
            with BuildLine():
                CenterArc((3.2801184195, -4.1372071317), 0.025, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((3.2801184195, -4.1372071317), 0.02, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0007068583, perimeter: 0.2827433388
            with BuildLine():
                CenterArc((3.7801184195, -4.1372071317), 0.025, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((3.7801184195, -4.1372071317), 0.02, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0007068583, perimeter: 0.2827433388
            with BuildLine():
                CenterArc((4.0301184195, -4.1372071317), 0.025, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((4.0301184195, -4.1372071317), 0.02, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0007068583, perimeter: 0.2827433388
            with BuildLine():
                CenterArc((4.7801184195, -4.1372071317), 0.025, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((4.7801184195, -4.1372071317), 0.02, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0007068583, perimeter: 0.2827433388
            with BuildLine():
                CenterArc((3.5301184195, -4.1372071317), 0.025, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((3.5301184195, -4.1372071317), 0.02, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0007068583, perimeter: 0.2827433388
            with BuildLine():
                CenterArc((4.2801184195, -4.1372071317), 0.025, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((4.2801184195, -4.1372071317), 0.02, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0007068583, perimeter: 0.2827433388
            with BuildLine():
                CenterArc((4.5301184195, -4.1372071317), 0.025, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((4.5301184195, -4.1372071317), 0.02, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0007068583, perimeter: 0.2827433388
            with BuildLine():
                CenterArc((5.0301184195, -4.1372071317), 0.025, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((5.0301184195, -4.1372071317), 0.02, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0007068583, perimeter: 0.2827433388
            with BuildLine():
                CenterArc((5.2801184195, -4.1372071317), 0.025, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((5.2801184195, -4.1372071317), 0.02, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0007068583, perimeter: 0.2827433388
            with BuildLine():
                CenterArc((5.5301184195, -4.1372071317), 0.025, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((5.5301184195, -4.1372071317), 0.02, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0012566371, perimeter: 0.1256637061
            with Locations((3.0301184195, -4.1372071317)):
                Circle(0.02)
            # Profile area: 0.0012566371, perimeter: 0.1256637061
            with Locations((3.2801184195, -4.1372071317)):
                Circle(0.02)
            # Profile area: 0.0012566371, perimeter: 0.1256637061
            with Locations((3.7801184195, -4.1372071317)):
                Circle(0.02)
            # Profile area: 0.0012566371, perimeter: 0.1256637061
            with Locations((4.0301184195, -4.1372071317)):
                Circle(0.02)
            # Profile area: 0.0012566371, perimeter: 0.1256637061
            with Locations((4.7801184195, -4.1372071317)):
                Circle(0.02)
            # Profile area: 0.0012566371, perimeter: 0.1256637061
            with Locations((3.5301184195, -4.1372071317)):
                Circle(0.02)
            # Profile area: 0.0012566371, perimeter: 0.1256637061
            with Locations((4.2801184195, -4.1372071317)):
                Circle(0.02)
            # Profile area: 0.0012566371, perimeter: 0.1256637061
            with Locations((4.5301184195, -4.1372071317)):
                Circle(0.02)
            # Profile area: 0.0012566371, perimeter: 0.1256637061
            with Locations((5.0301184195, -4.1372071317)):
                Circle(0.02)
            # Profile area: 0.0012566371, perimeter: 0.1256637061
            with Locations((5.2801184195, -4.1372071317)):
                Circle(0.02)
            # Profile area: 0.0012566371, perimeter: 0.1256637061
            with Locations((5.5301184195, -4.1372071317)):
                Circle(0.02)
        # OneSide extrude, distance=-0.17
        extrude(amount=-0.17)

        # Sketch1 -> Extrude7 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 141 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0007068583, perimeter: 0.2827433388
            with BuildLine():
                CenterArc((3.0301184195, -3.3118071317), 0.025, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((3.0301184195, -3.3118071317), 0.02, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0007068583, perimeter: 0.2827433388
            with BuildLine():
                CenterArc((3.2801184195, -3.3118071317), 0.025, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((3.2801184195, -3.3118071317), 0.02, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0007068583, perimeter: 0.2827433388
            with BuildLine():
                CenterArc((3.5301184195, -3.3118071317), 0.025, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((3.5301184195, -3.3118071317), 0.02, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0007068583, perimeter: 0.2827433388
            with BuildLine():
                CenterArc((3.7801184195, -3.3118071317), 0.025, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((3.7801184195, -3.3118071317), 0.02, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0007068583, perimeter: 0.2827433388
            with BuildLine():
                CenterArc((4.5301184195, -3.3118071317), 0.025, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((4.5301184195, -3.3118071317), 0.02, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0007068583, perimeter: 0.2827433388
            with BuildLine():
                CenterArc((4.7801184195, -3.3118071317), 0.025, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((4.7801184195, -3.3118071317), 0.02, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0007068583, perimeter: 0.2827433388
            with BuildLine():
                CenterArc((4.2801184195, -3.3118071317), 0.025, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((4.2801184195, -3.3118071317), 0.02, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0007068583, perimeter: 0.2827433388
            with BuildLine():
                CenterArc((4.0301184195, -3.3118071317), 0.025, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((4.0301184195, -3.3118071317), 0.02, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0007068583, perimeter: 0.2827433388
            with BuildLine():
                CenterArc((5.7801184195, -3.3118071317), 0.025, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((5.7801184195, -3.3118071317), 0.02, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0007068583, perimeter: 0.2827433388
            with BuildLine():
                CenterArc((5.5301184195, -3.3118071317), 0.025, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((5.5301184195, -3.3118071317), 0.02, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0007068583, perimeter: 0.2827433388
            with BuildLine():
                CenterArc((5.0301184195, -3.3118071317), 0.025, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((5.0301184195, -3.3118071317), 0.02, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0007068583, perimeter: 0.2827433388
            with BuildLine():
                CenterArc((5.2801184195, -3.3118071317), 0.025, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((5.2801184195, -3.3118071317), 0.02, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0007068583, perimeter: 0.2827433388
            with BuildLine():
                CenterArc((6.2801184195, -3.3118071317), 0.025, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((6.2801184195, -3.3118071317), 0.02, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0007068583, perimeter: 0.2827433388
            with BuildLine():
                CenterArc((6.0301184195, -3.3118071317), 0.025, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((6.0301184195, -3.3118071317), 0.02, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0012566371, perimeter: 0.1256637061
            with Locations((3.0301184195, -3.3118071317)):
                Circle(0.02)
            # Profile area: 0.0012566371, perimeter: 0.1256637061
            with Locations((3.2801184195, -3.3118071317)):
                Circle(0.02)
            # Profile area: 0.0012566371, perimeter: 0.1256637061
            with Locations((3.5301184195, -3.3118071317)):
                Circle(0.02)
            # Profile area: 0.0012566371, perimeter: 0.1256637061
            with Locations((3.7801184195, -3.3118071317)):
                Circle(0.02)
            # Profile area: 0.0012566371, perimeter: 0.1256637061
            with Locations((4.5301184195, -3.3118071317)):
                Circle(0.02)
            # Profile area: 0.0012566371, perimeter: 0.1256637061
            with Locations((4.7801184195, -3.3118071317)):
                Circle(0.02)
            # Profile area: 0.0012566371, perimeter: 0.1256637061
            with Locations((4.2801184195, -3.3118071317)):
                Circle(0.02)
            # Profile area: 0.0012566371, perimeter: 0.1256637061
            with Locations((4.0301184195, -3.3118071317)):
                Circle(0.02)
            # Profile area: 0.0012566371, perimeter: 0.1256637061
            with Locations((5.7801184195, -3.3118071317)):
                Circle(0.02)
            # Profile area: 0.0012566371, perimeter: 0.1256637061
            with Locations((5.5301184195, -3.3118071317)):
                Circle(0.02)
            # Profile area: 0.0012566371, perimeter: 0.1256637061
            with Locations((5.0301184195, -3.3118071317)):
                Circle(0.02)
            # Profile area: 0.0012566371, perimeter: 0.1256637061
            with Locations((5.2801184195, -3.3118071317)):
                Circle(0.02)
            # Profile area: 0.0012566371, perimeter: 0.1256637061
            with Locations((6.2801184195, -3.3118071317)):
                Circle(0.02)
            # Profile area: 0.0012566371, perimeter: 0.1256637061
            with Locations((6.0301184195, -3.3118071317)):
                Circle(0.02)
        # OneSide extrude, distance=-0.17
        extrude(amount=-0.17)
    return part.part


def model_41117_1b3271f2_0007():
    """Model: Power Jack v17"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 26 constraints, 9 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.5822707993, perimeter: 5.3409733553
            with BuildLine():
                Line((1.2, -0.8), (0.36, -0.8))
                Line((1.2, 0), (1.2, -0.8))
                Line((0.36, 0), (1.2, 0))
                Line((0.36, 0), (0.36, -0.8))
            make_face()
            with BuildLine():
                CenterArc((0.7612, -0.6779000119), 0.06, 90, 180)
                Line((0.7612, -0.6179000119), (0.9162, -0.6179000119))
                CenterArc((0.9162, -0.6779000119), 0.06, -90, 180)
                Line((0.7612, -0.7379000119), (0.9162, -0.7379000119))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((0.5295, -0.2466), (0.5295, -0.4016))
                CenterArc((0.5895, -0.2466), 0.06, 0, 180)
                Line((0.6495, -0.2466), (0.6495, -0.4016))
                CenterArc((0.5895, -0.4016), 0.06, 180, 180)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((1.0295, -0.2466), (1.0295, -0.4016))
                CenterArc((1.0895, -0.2466), 0.06, 0, 180)
                Line((1.1495, -0.2466), (1.1495, -0.4016))
                CenterArc((1.0895, -0.4016), 0.06, 180, 180)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0113097336, perimeter: 0.3769911184
            with BuildLine():
                CenterArc((0.7612, -0.6779000119), 0.06, 90, 180)
                CenterArc((0.7612, -0.6779000119), 0.06, -90, 180)
            make_face()
            # Profile area: 0.0072902664, perimeter: 0.6869911184
            with BuildLine():
                CenterArc((0.7612, -0.6779000119), 0.06, -90, 180)
                Line((0.7612, -0.7379000119), (0.9162, -0.7379000119))
                CenterArc((0.9162, -0.6779000119), 0.06, 90, 180)
                Line((0.7612, -0.6179000119), (0.9162, -0.6179000119))
            make_face()
            # Profile area: 0.0113097336, perimeter: 0.3769911184
            with BuildLine():
                CenterArc((0.9162, -0.6779000119), 0.06, 90, 180)
                CenterArc((0.9162, -0.6779000119), 0.06, -90, 180)
            make_face()
            # Profile area: 0.0072902664, perimeter: 0.6869911184
            with BuildLine():
                CenterArc((0.5895, -0.4016), 0.06, 0, 180)
                Line((0.6495, -0.2466), (0.6495, -0.4016))
                CenterArc((0.5895, -0.2466), 0.06, 180, 180)
                Line((0.5295, -0.2466), (0.5295, -0.4016))
            make_face()
            # Profile area: 0.0113097336, perimeter: 0.3769911184
            with BuildLine():
                CenterArc((0.5895, -0.4016), 0.06, 180, 180)
                CenterArc((0.5895, -0.4016), 0.06, 0, 180)
            make_face()
            # Profile area: 0.0113097336, perimeter: 0.3769911184
            with BuildLine():
                CenterArc((0.5895, -0.2466), 0.06, 180, 180)
                CenterArc((0.5895, -0.2466), 0.06, 0, 180)
            make_face()
            # Profile area: 0.0072902664, perimeter: 0.6869911184
            with BuildLine():
                CenterArc((1.0895, -0.4016), 0.06, 0, 180)
                Line((1.1495, -0.2466), (1.1495, -0.4016))
                CenterArc((1.0895, -0.2466), 0.06, 180, 180)
                Line((1.0295, -0.2466), (1.0295, -0.4016))
            make_face()
            # Profile area: 0.0113097336, perimeter: 0.3769911184
            with BuildLine():
                CenterArc((1.0895, -0.4016), 0.06, 180, 180)
                CenterArc((1.0895, -0.4016), 0.06, 0, 180)
            make_face()
            # Profile area: 0.0113097336, perimeter: 0.3769911184
            with BuildLine():
                CenterArc((1.0895, -0.2466), 0.06, 180, 180)
                CenterArc((1.0895, -0.2466), 0.06, 0, 180)
            make_face()
        # OneSide extrude, distance=1.1
        extrude(amount=1.1)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 26 constraints, 9 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.288, perimeter: 2.32
            with BuildLine():
                Line((0.36, -0.8), (0, -0.8))
                Line((0.36, 0), (0.36, -0.8))
                Line((0, 0), (0.36, 0))
                Line((0, -0.8), (0, 0))
            make_face()
        # OneSide extrude, distance=1.1
        extrude(amount=1.1, mode=Mode.ADD)

        # Sketch1 -> Extrude3 (Join)
        # Sketch on XZ construction plane
        # Sketch has 26 constraints, 9 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0072902664, perimeter: 0.6869911184
            with BuildLine():
                CenterArc((1.0895, -0.4016), 0.06, 0, 180)
                Line((1.1495, -0.2466), (1.1495, -0.4016))
                CenterArc((1.0895, -0.2466), 0.06, 180, 180)
                Line((1.0295, -0.2466), (1.0295, -0.4016))
            make_face()
            # Profile area: 0.0113097336, perimeter: 0.3769911184
            with BuildLine():
                CenterArc((1.0895, -0.2466), 0.06, 180, 180)
                CenterArc((1.0895, -0.2466), 0.06, 0, 180)
            make_face()
            # Profile area: 0.0113097336, perimeter: 0.3769911184
            with BuildLine():
                CenterArc((1.0895, -0.4016), 0.06, 180, 180)
                CenterArc((1.0895, -0.4016), 0.06, 0, 180)
            make_face()
            # Profile area: 0.0072902664, perimeter: 0.6869911184
            with BuildLine():
                CenterArc((0.5895, -0.4016), 0.06, 0, 180)
                Line((0.6495, -0.2466), (0.6495, -0.4016))
                CenterArc((0.5895, -0.2466), 0.06, 180, 180)
                Line((0.5295, -0.2466), (0.5295, -0.4016))
            make_face()
            # Profile area: 0.0113097336, perimeter: 0.3769911184
            with BuildLine():
                CenterArc((0.5895, -0.2466), 0.06, 180, 180)
                CenterArc((0.5895, -0.2466), 0.06, 0, 180)
            make_face()
            # Profile area: 0.0113097336, perimeter: 0.3769911184
            with BuildLine():
                CenterArc((0.5895, -0.4016), 0.06, 180, 180)
                CenterArc((0.5895, -0.4016), 0.06, 0, 180)
            make_face()
            # Profile area: 0.0113097336, perimeter: 0.3769911184
            with BuildLine():
                CenterArc((0.9162, -0.6779000119), 0.06, 90, 180)
                CenterArc((0.9162, -0.6779000119), 0.06, -90, 180)
            make_face()
            # Profile area: 0.0072902664, perimeter: 0.6869911184
            with BuildLine():
                CenterArc((0.7612, -0.6779000119), 0.06, -90, 180)
                Line((0.7612, -0.7379000119), (0.9162, -0.7379000119))
                CenterArc((0.9162, -0.6779000119), 0.06, 90, 180)
                Line((0.7612, -0.6179000119), (0.9162, -0.6179000119))
            make_face()
            # Profile area: 0.0113097336, perimeter: 0.3769911184
            with BuildLine():
                CenterArc((0.7612, -0.6779000119), 0.06, 90, 180)
                CenterArc((0.7612, -0.6779000119), 0.06, -90, 180)
            make_face()
        # OneSide extrude, distance=-0.4
        extrude(amount=-0.4, mode=Mode.ADD)

        # Sketch2 -> Extrude4 (Cut)
        # Sketch on YZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.3117245311, perimeter: 1.9792033718
            with Locations((-0.400000006, 0.7000000104)):
                Circle(0.315)
        # OneSide extrude, distance=0.7
        extrude(amount=0.7, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude5 (Join)
        # Sketch on YZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0078539816, perimeter: 0.3141592654
            with Locations((-0.400000006, 0.7000000104)):
                Circle(0.05)
        # OneSide extrude, distance=0.7
        extrude(amount=0.7, mode=Mode.ADD)

        # Sketch1 -> Extrude6 (Join)
        # Sketch on XZ construction plane
        # Sketch has 26 constraints, 9 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0072902664, perimeter: 0.6869911184
            with BuildLine():
                CenterArc((1.0895, -0.4016), 0.06, 0, 180)
                Line((1.1495, -0.2466), (1.1495, -0.4016))
                CenterArc((1.0895, -0.2466), 0.06, 180, 180)
                Line((1.0295, -0.2466), (1.0295, -0.4016))
            make_face()
            # Profile area: 0.0113097336, perimeter: 0.3769911184
            with BuildLine():
                CenterArc((1.0895, -0.2466), 0.06, 180, 180)
                CenterArc((1.0895, -0.2466), 0.06, 0, 180)
            make_face()
            # Profile area: 0.0113097336, perimeter: 0.3769911184
            with BuildLine():
                CenterArc((1.0895, -0.4016), 0.06, 180, 180)
                CenterArc((1.0895, -0.4016), 0.06, 0, 180)
            make_face()
            # Profile area: 0.0072902664, perimeter: 0.6869911184
            with BuildLine():
                CenterArc((0.5895, -0.4016), 0.06, 0, 180)
                Line((0.6495, -0.2466), (0.6495, -0.4016))
                CenterArc((0.5895, -0.2466), 0.06, 180, 180)
                Line((0.5295, -0.2466), (0.5295, -0.4016))
            make_face()
            # Profile area: 0.0113097336, perimeter: 0.3769911184
            with BuildLine():
                CenterArc((0.5895, -0.2466), 0.06, 180, 180)
                CenterArc((0.5895, -0.2466), 0.06, 0, 180)
            make_face()
            # Profile area: 0.0113097336, perimeter: 0.3769911184
            with BuildLine():
                CenterArc((0.5895, -0.4016), 0.06, 180, 180)
                CenterArc((0.5895, -0.4016), 0.06, 0, 180)
            make_face()
            # Profile area: 0.0113097336, perimeter: 0.3769911184
            with BuildLine():
                CenterArc((0.9162, -0.6779000119), 0.06, 90, 180)
                CenterArc((0.9162, -0.6779000119), 0.06, -90, 180)
            make_face()
            # Profile area: 0.0072902664, perimeter: 0.6869911184
            with BuildLine():
                CenterArc((0.7612, -0.6779000119), 0.06, -90, 180)
                Line((0.7612, -0.7379000119), (0.9162, -0.7379000119))
                CenterArc((0.9162, -0.6779000119), 0.06, 90, 180)
                Line((0.7612, -0.6179000119), (0.9162, -0.6179000119))
            make_face()
            # Profile area: 0.0113097336, perimeter: 0.3769911184
            with BuildLine():
                CenterArc((0.7612, -0.6779000119), 0.06, 90, 180)
                CenterArc((0.7612, -0.6779000119), 0.06, -90, 180)
            make_face()
        # OneSide extrude, distance=-0.32
        extrude(amount=-0.32, mode=Mode.ADD)
    return part.part


def model_41227_90e1c07c_0006():
    """Model: Seat connector"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 5 constraints, 9 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 219.2923424258, perimeter: 61.4582271537
            with BuildLine():
                Line((-57.8149597897, 55.5940369644), (-70.5149597897, 55.5940369644))
                Line((-70.5149597897, 55.5940369644), (-77.1140733666, 51.7840369644))
                Line((-77.1140733666, 51.7840369644), (-73.3040733666, 45.1849233876))
                Line((-55.0258462129, 45.1849233876), (-73.3040733666, 45.1849233876))
                Line((-51.2158462129, 51.7840369644), (-55.0258462129, 45.1849233876))
                Line((-57.8149597897, 55.5940369644), (-51.2158462129, 51.7840369644))
            make_face()
        # OneSide extrude, distance=7.62
        extrude(amount=7.62)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 45.6036731188, perimeter: 23.9389360204
            with Locations((64.7043368021, 50.2775181999)):
                Circle(3.81)
        # OneSide extrude, distance=20.32
        extrude(amount=20.32, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 72.2294009857, 41.7016641025), x_dir=(1, 0, 0), z_dir=(0, 0.8660254038, 0.5))):
            # Profile area: 31.9230778906, perimeter: 20.0289098037
            with Locations((3.81, -37.0807280425)):
                Circle(3.1877)
        # OneSide extrude, distance=-2.54
        extrude(amount=-2.54, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 16.660915775, -9.6191842076), x_dir=(-1, 0, 0), z_dir=(0, 0.8660254038, -0.5))):
            # Profile area: 31.9230778906, perimeter: 20.0289098037
            with Locations((-3.81, 74.0562423789)):
                Circle(3.1877)
        # OneSide extrude, distance=-2.54
        extrude(amount=-2.54, mode=Mode.SUBTRACT)
    return part.part


def model_41229_16283ae1_0002():
    """Model: VGA v5"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.25, perimeter: 6.8
            with BuildLine():
                Line((0, 2.5), (0, 0))
                Line((0, 0), (0.9, 0))
                Line((0.9, 0), (0.9, 2.5))
                Line((0.9, 2.5), (0, 2.5))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1385640646, perimeter: 1.3856406461
            with BuildLine():
                Line((-0.5654700538, -0.55), (-0.3345299462, -0.55))
                Line((-0.3345299462, -0.55), (-0.2190598923, -0.35))
                Line((-0.2190598923, -0.35), (-0.3345299462, -0.15))
                Line((-0.3345299462, -0.15), (-0.5654700538, -0.15))
                Line((-0.5654700538, -0.15), (-0.6809401077, -0.35))
                Line((-0.6809401077, -0.35), (-0.5654700538, -0.55))
            make_face()
            # Profile area: 0.1385640646, perimeter: 1.3856406461
            with BuildLine():
                Line((-0.3345299462, -1.95), (-0.5654700538, -1.95))
                Line((-0.5654700538, -1.95), (-0.6809401077, -2.15))
                Line((-0.6809401077, -2.15), (-0.5654700538, -2.35))
                Line((-0.5654700538, -2.35), (-0.3345299462, -2.35))
                Line((-0.3345299462, -2.35), (-0.2190598923, -2.15))
                Line((-0.2190598923, -2.15), (-0.3345299462, -1.95))
            make_face()
            # Profile area: 0.5000000149, perimeter: 3.0198039477
            with BuildLine():
                Line((-0.200000003, -1.8000000268), (-0.200000003, -0.7000000104))
                Line((-0.200000003, -0.7000000104), (-0.7000000104, -0.8000000119))
                Line((-0.7000000104, -0.8000000119), (-0.7000000104, -1.7000000253))
                Line((-0.200000003, -1.8000000268), (-0.7000000104, -1.7000000253))
            make_face()
        # OneSide extrude, distance=0.4
        extrude(amount=0.4, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.9, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0593957361, perimeter: 0.8639379797
            with Locations((-0.4500000067, -0.3500000052)):
                Circle(0.1375)
        # OneSide extrude, distance=-0.4
        extrude(amount=-0.4, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.9, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0593957361, perimeter: 0.8639379797
            with Locations((-0.4500000067, -2.150000032)):
                Circle(0.1375)
        # OneSide extrude, distance=-0.4
        extrude(amount=-0.4, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 15 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.9, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0028274334, perimeter: 0.1884955592
            with Locations((-0.6000000089, -0.9000000134)):
                Circle(0.03)
            # Profile area: 0.0028274334, perimeter: 0.1884955592
            with Locations((-0.6000000089, -1.0500000156)):
                Circle(0.03)
            # Profile area: 0.0028274334, perimeter: 0.1884955592
            with Locations((-0.3500000052, -0.9000000134)):
                Circle(0.03)
            # Profile area: 0.0028274334, perimeter: 0.1884955592
            with Locations((-0.4500000067, -1.0000000149)):
                Circle(0.03)
            # Profile area: 0.0028274334, perimeter: 0.1884955592
            with Locations((-0.3500000052, -1.0500000156)):
                Circle(0.03)
            # Profile area: 0.0028274334, perimeter: 0.1884955592
            with Locations((-0.4500000067, -1.1500000171)):
                Circle(0.03)
            # Profile area: 0.0028274334, perimeter: 0.1884955592
            with Locations((-0.3500000052, -1.2000000179)):
                Circle(0.03)
            # Profile area: 0.0028274334, perimeter: 0.1884955592
            with Locations((-0.6000000089, -1.2500000186)):
                Circle(0.03)
            # Profile area: 0.0028274334, perimeter: 0.1884955592
            with Locations((-0.4500000067, -1.3000000194)):
                Circle(0.03)
            # Profile area: 0.0028274334, perimeter: 0.1884955592
            with Locations((-0.3500000052, -1.4000000209)):
                Circle(0.03)
            # Profile area: 0.0028274334, perimeter: 0.1884955592
            with Locations((-0.6000000089, -1.4000000209)):
                Circle(0.03)
            # Profile area: 0.0028274334, perimeter: 0.1884955592
            with Locations((-0.6000000089, -1.6000000238)):
                Circle(0.03)
            # Profile area: 0.0028274334, perimeter: 0.1884955592
            with Locations((-0.4500000067, -1.6500000246)):
                Circle(0.03)
            # Profile area: 0.0028274334, perimeter: 0.1884955592
            with Locations((-0.4500000067, -1.5000000224)):
                Circle(0.03)
            # Profile area: 0.0028274334, perimeter: 0.1884955592
            with Locations((-0.3500000052, -1.5500000231)):
                Circle(0.03)
        # OneSide extrude, distance=-0.25
        extrude(amount=-0.25, mode=Mode.SUBTRACT)
    return part.part


def model_41229_16283ae1_0003():
    """Model: USB v4"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.04, perimeter: 4.2
            with BuildLine():
                Line((0.8, 0), (0, 0))
                Line((0, 0), (0, -1.3))
                Line((0, -1.3), (0.8, -1.3))
                Line((0.8, -1.3), (0.8, 0))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.840000025, perimeter: 3.8000000566
            with BuildLine():
                Line((-0.0500000007, 0.0500000007), (-0.7500000112, 0.0500000007))
                Line((-0.0500000007, 1.2500000186), (-0.0500000007, 0.0500000007))
                Line((-0.7500000112, 1.2500000186), (-0.0500000007, 1.2500000186))
                Line((-0.7500000112, 0.0500000007), (-0.7500000112, 1.2500000186))
            make_face()
        # OneSide extrude, distance=-0.9
        extrude(amount=-0.9, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2200000066, perimeter: 2.6000000387
            with BuildLine():
                Line((-0.3500000052, 1.2000000179), (-0.1500000022, 1.2000000179))
                Line((-0.3500000052, 0.1000000015), (-0.3500000052, 1.2000000179))
                Line((-0.1500000022, 0.1000000015), (-0.3500000052, 0.1000000015))
                Line((-0.1500000022, 1.2000000179), (-0.1500000022, 0.1000000015))
            make_face()
        # OneSide extrude, distance=0.9
        extrude(amount=0.9, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 16 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0.3500000052, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0400000012, perimeter: 1.0000000149
            with BuildLine():
                Line((-0.200000003, 0.6000000089), (-0.3000000045, 0.6000000089))
                Line((-0.3000000045, 0.6000000089), (-0.3000000045, 0.200000003))
                Line((-0.3000000045, 0.200000003), (-0.200000003, 0.200000003))
                Line((-0.200000003, 0.200000003), (-0.200000003, 0.6000000089))
            make_face()
            # Profile area: 0.0400000012, perimeter: 1.0000000149
            with BuildLine():
                Line((-0.400000006, 0.6000000089), (-0.5000000075, 0.6000000089))
                Line((-0.5000000075, 0.6000000089), (-0.5000000075, 0.200000003))
                Line((-0.5000000075, 0.200000003), (-0.400000006, 0.200000003))
                Line((-0.400000006, 0.200000003), (-0.400000006, 0.6000000089))
            make_face()
            # Profile area: 0.0400000012, perimeter: 1.0000000149
            with BuildLine():
                Line((-0.7500000112, 0.6000000089), (-0.8500000127, 0.6000000089))
                Line((-0.8500000127, 0.6000000089), (-0.8500000127, 0.200000003))
                Line((-0.8500000127, 0.200000003), (-0.7500000112, 0.200000003))
                Line((-0.7500000112, 0.200000003), (-0.7500000112, 0.6000000089))
            make_face()
            # Profile area: 0.0400000012, perimeter: 1.0000000149
            with BuildLine():
                Line((-1.0500000156, 0.6000000089), (-1.0500000156, 0.200000003))
                Line((-1.0500000156, 0.200000003), (-0.9500000142, 0.200000003))
                Line((-0.9500000142, 0.6000000089), (-0.9500000142, 0.200000003))
                Line((-1.0500000156, 0.6000000089), (-0.9500000142, 0.6000000089))
            make_face()
        # OneSide extrude, distance=0.025
        extrude(amount=0.025, mode=Mode.ADD)

        # Sketch5 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 9 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0.7500000112, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.0600000018, perimeter: 1.0000000149
            with BuildLine():
                Line((0.200000003, 0.9000000134), (0.200000003, 0.6000000089))
                Line((0.200000003, 0.6000000089), (0.400000006, 0.6000000089))
                Line((0.400000006, 0.6000000089), (0.400000006, 0.9000000134))
                Line((0.400000006, 0.9000000134), (0.200000003, 0.9000000134))
            make_face()
            # Profile area: 0.0600000018, perimeter: 1.0000000149
            with BuildLine():
                Line((0.9000000134, 0.9000000134), (1.1000000164, 0.9000000134))
                Line((0.9000000134, 0.6000000089), (0.9000000134, 0.9000000134))
                Line((1.1000000164, 0.6000000089), (0.9000000134, 0.6000000089))
                Line((1.1000000164, 0.9000000134), (1.1000000164, 0.6000000089))
            make_face()
        # OneSide extrude, distance=0.05
        extrude(amount=0.05, mode=Mode.ADD)
    return part.part


def model_41229_16283ae1_0012():
    """Model: Power Input v1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 4.5, perimeter: 8.6
            with BuildLine():
                Line((-1.25, 0), (1.25, 0))
                Line((1.25, 0), (1.25, 1.8))
                Line((1.25, 1.8), (-1.25, 1.8))
                Line((-1.25, 1.8), (-1.25, 0))
            make_face()
        # OneSide extrude, distance=-1.4
        extrude(amount=-1.4)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 13 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.0400440999, perimeter: 4.6065127201
            with BuildLine():
                Line((0, 0.8000000179), (0.0434120444, 0.5537980796))
                Line((0.0434120444, 0.5537980796), (0.2434120444, 0.5537980796))
                CenterArc((0.2434120444, 1.0009341085), 0.4471360289, -90, 180.0011180739)
                Line((0.0434120444, 1.4462019561), (0.243403319, 1.4480701373))
                Line((0, 1.2000000179), (0.0434120444, 1.4462019561))
                Line((0, 1.2000000179), (-0.0434120444, 1.4462019561))
                Line((-0.0434120444, 1.4462019561), (-0.2434120444, 1.4462019561))
                CenterArc((-0.2434120444, 1.0000000179), 0.4462019383, 90, 180)
                Line((-0.0434120444, 0.5537980796), (-0.2434120444, 0.5537980796))
                Line((0, 0.8000000179), (-0.0434120444, 0.5537980796))
            make_face()
        # OneSide extrude, distance=-1.2
        extrude(amount=-1.2, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -1.2), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            with Locations((-0.3500000052, 1.0000000149)):
                Circle(0.1)
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -1.2), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            with Locations((0.3500000052, 1.0000000149)):
                Circle(0.1)
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)
    return part.part


def model_41229_16283ae1_0015():
    """Model: HDMI v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.7, perimeter: 3.8
            with BuildLine():
                Line((0, 1.4), (0, 0))
                Line((0, 0), (0.5, 0))
                Line((0.5, 0), (0.5, 1.4))
                Line((0.5, 1.4), (0, 1.4))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.3320440588, perimeter: 2.8636476517
            with BuildLine():
                Line((-0.1000000015, -0.1000000015), (-0.200000003, -0.1000000015))
                CenterArc((-0.400000006, 0.0500000007), 0.2500000037, -90, 53.1301023542)
                Line((-0.400000006, -0.200000003), (-0.400000006, -1.2000000179))
                CenterArc((-0.400000006, -1.4500000216), 0.2500000037, 36.8698976458, 53.1301023542)
                Line((-0.1000000015, -1.3000000194), (-0.200000003, -1.3000000194))
                Line((-0.1000000015, -0.1000000015), (-0.1000000015, -1.3000000194))
            make_face()
        # OneSide extrude, distance=-0.45
        extrude(amount=-0.45, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.05, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0400000012, perimeter: 1.7000000253
            with BuildLine():
                Line((-0.2500000037, -0.3000000045), (-0.200000003, -0.3000000045))
                Line((-0.2500000037, -1.1000000164), (-0.2500000037, -0.3000000045))
                Line((-0.200000003, -1.1000000164), (-0.2500000037, -1.1000000164))
                Line((-0.200000003, -0.3000000045), (-0.200000003, -1.1000000164))
            make_face()
        # OneSide extrude, distance=0.4
        extrude(amount=0.4, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.400000006, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.014967822, perimeter: 0.4993553948
            with BuildLine():
                Line((-0.4999978944, 0.3006498603), (-0.4990273133, 0.45))
                Line((-0.400000006, 0.3000000045), (-0.4999978944, 0.3006498603))
                Line((-0.400000006, 0.3000000045), (-0.3990252222, 0.4499968371))
                Line((-0.3990252222, 0.4499968371), (-0.399511921, 0.45))
                Line((-0.4990273133, 0.45), (-0.399511921, 0.45))
            make_face()
            # Profile area: 0.0150729506, perimeter: 0.5009747868
            with BuildLine():
                Line((-1.0000000149, 0.3000000045), (-0.9000000134, 0.3000000045))
                Line((-0.9000000134, 0.3000000045), (-0.8990252296, 0.4499968371))
                Line((-1.0000000149, 0.4500000045), (-0.8990252296, 0.4499968371))
                Line((-1.0000000149, 0.3000000045), (-1.0000000149, 0.4500000045))
            make_face()
        # OneSide extrude, distance=0.025
        extrude(amount=0.025, mode=Mode.ADD)
    return part.part


def model_41353_16ac5969_0000():
    """Model: bottomHelm"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 6.2517693806, perimeter: 125.0353876129
            with BuildLine():
                CenterArc((0, 0), 10, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 9.9, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-8
        extrude(amount=-8)

        # Sketch3 -> Extrude2 (Cut)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 63.7363796855, perimeter: 39.1331191851
            with BuildLine():
                Line((-10, -8), (5, -8))
                Line((5, -8), (4, -4))
                CenterArc((2, -4.1446681012), 2.0052253887, 4.1372302301, 171.7255395398)
                Line((-10, -4), (0, -4))
                Line((-10, -8), (-10, -4))
            make_face()
        # Symmetric extrude, each_side=10
        extrude(amount=10, both=True, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude3 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.1884955592, perimeter: 3.7699111843
            with BuildLine():
                CenterArc((-10.544567528, -4.2653884674), 0.35, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-10.544567528, -4.2653884674), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=0.9
        extrude(amount=0.9, both=True)

        # Sketch6 -> Extrude4 (Cut)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((-1.0000000149, -2.5000000373)):
                Circle(0.25)
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((2, -1.5)):
                Circle(0.25)
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((5.238104693, -6)):
                Circle(0.25)
        # Symmetric extrude, each_side=20
        extrude(amount=20, both=True, mode=Mode.SUBTRACT)
    return part.part


def model_41495_a639572a_0000():
    """Model: piston cyclinder"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 8.6393797974, perimeter: 34.5575191895
            with BuildLine():
                CenterArc((-3.3160328037, 1.3402976623), 3, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-3.3160328037, 1.3402976623), 2.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=5
        extrude(amount=5)

        # Sketch4 -> Extrude3 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 8 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 29.9932862731, perimeter: 37.5295349012
            with BuildLine():
                Line((-2.4172912797, -7.7139760078), (-2.2523409721, -7.7037341973))
                Line((-2.2523409721, -7.7037341973), (9.6845370854, -6.9625701131))
                CenterArc((9.6380588817, -6.2140116474), 0.75, -86.4470501839, 172.9145452569)
                Line((-2.195588764, -4.7320682518), (9.6842699739, -5.4654366445))
                Line((-2.4756398511, -4.7147801156), (-2.195588764, -4.7320682518))
                CenterArc((-2.4276313725, -6.2140116474), 1.5, 91.8341020259, 178.5608635522)
            make_face()
            with BuildLine():
                CenterArc((-2.4276313725, -6.2140116474), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((9.6380588817, -6.2140116474), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch5 -> Extrude4 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 4 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 35.5582171655, perimeter: 28.1256572648
            with BuildLine():
                Line((14.7206165204, 1.445377755), (14.7206165204, -4.9587575288))
                CenterArc((12.4747218549, 1.445377755), 2.2458946655, 0, 180)
                Line((10.2288271894, -4.9587575288), (10.2288271894, 1.445377755))
                Line((14.7206165204, -4.9587575288), (10.2288271894, -4.9587575288))
            make_face()
            with BuildLine():
                CenterArc((12.4747218549, 1.445377755), 0.6, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=3
        extrude(amount=3, both=True)

        # Sketch9 -> Extrude7 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((-6.852525537, 6.2491076551)):
                Circle(0.5)
        # OneSide extrude, distance=5
        extrude(amount=5)
    return part.part


def model_41624_a15f83c1_0017():
    """Model: Scroll knob v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 7.0685834706, perimeter: 9.4247779608
            Circle(1.5)
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 1.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 7.0685834706, perimeter: 9.4247779608
            Circle(1.5)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.0797776261, perimeter: 1.1934743219
            with BuildLine():
                Line((-0.1000000015, 1.4966629546), (-0.1000000015, 1.1000000164))
                Line((-0.1000000015, 1.1000000164), (0.0999999985, 1.1000000164))
                Line((0.0999999985, 1.1000000164), (0.0999999985, 1.4966629548))
                CenterArc((0, 0), 1.5, 86.1774463278, 3.8225536722)
                CenterArc((0, 0), 1.5, 90, 3.8225537863)
            make_face()
        # OneSide extrude, distance=-1.8
        extrude(amount=-1.8, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.08, perimeter: 1.2
            with BuildLine():
                Line((0.0999999985, -1.5000000164), (-0.1000000015, -1.5000000164))
                Line((0.0999999985, -1.1000000164), (0.0999999985, -1.5000000164))
                Line((-0.1000000015, -1.1000000164), (0.0999999985, -1.1000000164))
                Line((-0.1000000015, -1.5000000164), (-0.1000000015, -1.1000000164))
            make_face()
        # OneSide extrude, distance=1.8
        extrude(amount=1.8, mode=Mode.ADD)
    return part.part


def model_41624_a15f83c1_0019():
    """Model: Pitch bender v3 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 15, perimeter: 16
            with BuildLine():
                Line((0, 5), (0, 0))
                Line((0, 0), (3, 0))
                Line((3, 0), (3, 5))
                Line((3, 5), (0, 5))
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 2.7600000823, perimeter: 10.400000155
            with BuildLine():
                Line((1.2000000179, -0.200000003), (1.8000000268, -0.200000003))
                Line((1.2000000179, -4.8000000715), (1.2000000179, -0.200000003))
                Line((1.8000000268, -4.8000000715), (1.2000000179, -4.8000000715))
                Line((1.8000000268, -0.200000003), (1.8000000268, -4.8000000715))
            make_face()
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 44 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.1400000042, perimeter: 1.8000000268
            with BuildLine():
                Line((1.8000000268, -1.1000000164), (1.8000000268, -1.3000000194))
                Line((1.8000000268, -1.3000000194), (2.5000000373, -1.3000000194))
                Line((2.5000000373, -1.3000000194), (2.5000000373, -1.1000000164))
                Line((2.5000000373, -1.1000000164), (1.8000000268, -1.1000000164))
            make_face()
            # Profile area: 0.1400000042, perimeter: 1.8000000268
            with BuildLine():
                Line((1.8000000268, -4.0000000596), (1.8000000268, -4.2000000626))
                Line((2.5000000373, -4.2000000626), (1.8000000268, -4.2000000626))
                Line((2.5000000373, -4.0000000596), (2.5000000373, -4.2000000626))
                Line((1.8000000268, -4.0000000596), (2.5000000373, -4.0000000596))
            make_face()
            # Profile area: 0.1800000054, perimeter: 2.2000000328
            with BuildLine():
                Line((1.2000000179, -4.70000007), (1.2000000179, -4.5000000671))
                Line((1.2000000179, -4.5000000671), (0.3000000045, -4.5000000671))
                Line((0.3000000045, -4.5000000671), (0.3000000045, -4.70000007))
                Line((0.3000000045, -4.70000007), (1.2000000179, -4.70000007))
            make_face()
            # Profile area: 0.1400000042, perimeter: 1.8000000268
            with BuildLine():
                Line((1.8000000268, -0.7000000104), (1.8000000268, -0.9000000134))
                Line((2.5000000373, -0.9000000134), (1.8000000268, -0.9000000134))
                Line((2.5000000373, -0.7000000104), (2.5000000373, -0.9000000134))
                Line((1.8000000268, -0.7000000104), (2.5000000373, -0.7000000104))
            make_face()
            # Profile area: 0.1400000042, perimeter: 1.8000000268
            with BuildLine():
                Line((1.8000000268, -3.5000000522), (1.8000000268, -3.7000000551))
                Line((1.8000000268, -3.7000000551), (2.5000000373, -3.7000000551))
                Line((2.5000000373, -3.7000000551), (2.5000000373, -3.5000000522))
                Line((2.5000000373, -3.5000000522), (1.8000000268, -3.5000000522))
            make_face()
            # Profile area: 0.1800000054, perimeter: 2.2000000328
            with BuildLine():
                Line((1.8000000268, -4.5000000671), (1.8000000268, -4.70000007))
                Line((1.8000000268, -4.70000007), (2.7000000402, -4.70000007))
                Line((2.7000000402, -4.70000007), (2.7000000402, -4.5000000671))
                Line((2.7000000402, -4.5000000671), (1.8000000268, -4.5000000671))
            make_face()
            # Profile area: 0.1400000042, perimeter: 1.8000000268
            with BuildLine():
                Line((1.8000000268, -1.5000000224), (1.8000000268, -1.7000000253))
                Line((2.5000000373, -1.7000000253), (1.8000000268, -1.7000000253))
                Line((2.5000000373, -1.5000000224), (2.5000000373, -1.7000000253))
                Line((1.8000000268, -1.5000000224), (2.5000000373, -1.5000000224))
            make_face()
            # Profile area: 0.1800000054, perimeter: 2.2000000328
            with BuildLine():
                Line((1.8000000268, -0.3000000045), (1.8000000268, -0.5000000075))
                Line((1.8000000268, -0.5000000075), (2.7000000402, -0.5000000075))
                Line((2.7000000402, -0.5000000075), (2.7000000402, -0.3000000045))
                Line((2.7000000402, -0.3000000045), (1.8000000268, -0.3000000045))
            make_face()
            # Profile area: 0.1400000042, perimeter: 1.8000000268
            with BuildLine():
                Line((1.8000000268, -1.9000000283), (1.8000000268, -2.1000000313))
                Line((1.8000000268, -2.1000000313), (2.5000000373, -2.1000000313))
                Line((2.5000000373, -2.1000000313), (2.5000000373, -1.9000000283))
                Line((2.5000000373, -1.9000000283), (1.8000000268, -1.9000000283))
            make_face()
            # Profile area: 0.1400000042, perimeter: 1.8000000268
            with BuildLine():
                Line((1.8000000268, -2.3000000343), (1.8000000268, -2.5000000373))
                Line((2.5000000373, -2.5000000373), (1.8000000268, -2.5000000373))
                Line((2.5000000373, -2.3000000343), (2.5000000373, -2.5000000373))
                Line((1.8000000268, -2.3000000343), (2.5000000373, -2.3000000343))
            make_face()
            # Profile area: 0.1400000042, perimeter: 1.8000000268
            with BuildLine():
                Line((1.8000000268, -2.7000000402), (1.8000000268, -2.9000000432))
                Line((1.8000000268, -2.9000000432), (2.5000000373, -2.9000000432))
                Line((2.5000000373, -2.9000000432), (2.5000000373, -2.7000000402))
                Line((2.5000000373, -2.7000000402), (1.8000000268, -2.7000000402))
            make_face()
            # Profile area: 0.1400000042, perimeter: 1.8000000268
            with BuildLine():
                Line((1.8000000268, -3.1000000462), (1.8000000268, -3.3000000492))
                Line((2.5000000373, -3.3000000492), (1.8000000268, -3.3000000492))
                Line((2.5000000373, -3.1000000462), (2.5000000373, -3.3000000492))
                Line((1.8000000268, -3.1000000462), (2.5000000373, -3.1000000462))
            make_face()
            # Profile area: 0.1400000042, perimeter: 1.8000000268
            with BuildLine():
                Line((1.2000000179, -4.2000000626), (1.2000000179, -4.0000000596))
                Line((0.5000000075, -4.0000000596), (1.2000000179, -4.0000000596))
                Line((0.5000000075, -4.2000000626), (0.5000000075, -4.0000000596))
                Line((1.2000000179, -4.2000000626), (0.5000000075, -4.2000000626))
            make_face()
            # Profile area: 0.1400000042, perimeter: 1.8000000268
            with BuildLine():
                Line((1.2000000179, -3.7000000551), (1.2000000179, -3.5000000522))
                Line((1.2000000179, -3.5000000522), (0.5000000075, -3.5000000522))
                Line((0.5000000075, -3.5000000522), (0.5000000075, -3.7000000551))
                Line((0.5000000075, -3.7000000551), (1.2000000179, -3.7000000551))
            make_face()
            # Profile area: 0.1400000042, perimeter: 1.8000000268
            with BuildLine():
                Line((1.2000000179, -3.3000000492), (1.2000000179, -3.1000000462))
                Line((0.5000000075, -3.1000000462), (1.2000000179, -3.1000000462))
                Line((0.5000000075, -3.3000000492), (0.5000000075, -3.1000000462))
                Line((1.2000000179, -3.3000000492), (0.5000000075, -3.3000000492))
            make_face()
            # Profile area: 0.1400000042, perimeter: 1.8000000268
            with BuildLine():
                Line((1.2000000179, -2.9000000432), (1.2000000179, -2.7000000402))
                Line((1.2000000179, -2.7000000402), (0.5000000075, -2.7000000402))
                Line((0.5000000075, -2.7000000402), (0.5000000075, -2.9000000432))
                Line((0.5000000075, -2.9000000432), (1.2000000179, -2.9000000432))
            make_face()
            # Profile area: 0.1400000042, perimeter: 1.8000000268
            with BuildLine():
                Line((1.2000000179, -2.5000000373), (1.2000000179, -2.3000000343))
                Line((0.5000000075, -2.3000000343), (1.2000000179, -2.3000000343))
                Line((0.5000000075, -2.5000000373), (0.5000000075, -2.3000000343))
                Line((1.2000000179, -2.5000000373), (0.5000000075, -2.5000000373))
            make_face()
            # Profile area: 0.1400000042, perimeter: 1.8000000268
            with BuildLine():
                Line((1.2000000179, -2.1000000313), (1.2000000179, -1.9000000283))
                Line((1.2000000179, -1.9000000283), (0.5000000075, -1.9000000283))
                Line((0.5000000075, -1.9000000283), (0.5000000075, -2.1000000313))
                Line((0.5000000075, -2.1000000313), (1.2000000179, -2.1000000313))
            make_face()
            # Profile area: 0.1400000042, perimeter: 1.8000000268
            with BuildLine():
                Line((1.2000000179, -1.7000000253), (1.2000000179, -1.5000000224))
                Line((0.5000000075, -1.5000000224), (1.2000000179, -1.5000000224))
                Line((0.5000000075, -1.7000000253), (0.5000000075, -1.5000000224))
                Line((1.2000000179, -1.7000000253), (0.5000000075, -1.7000000253))
            make_face()
            # Profile area: 0.1400000042, perimeter: 1.8000000268
            with BuildLine():
                Line((1.2000000179, -1.3000000194), (1.2000000179, -1.1000000164))
                Line((1.2000000179, -1.1000000164), (0.5000000075, -1.1000000164))
                Line((0.5000000075, -1.1000000164), (0.5000000075, -1.3000000194))
                Line((0.5000000075, -1.3000000194), (1.2000000179, -1.3000000194))
            make_face()
            # Profile area: 0.1400000042, perimeter: 1.8000000268
            with BuildLine():
                Line((1.2000000179, -0.9000000134), (1.2000000179, -0.7000000104))
                Line((0.5000000075, -0.7000000104), (1.2000000179, -0.7000000104))
                Line((0.5000000075, -0.9000000134), (0.5000000075, -0.7000000104))
                Line((1.2000000179, -0.9000000134), (0.5000000075, -0.9000000134))
            make_face()
            # Profile area: 0.1800000054, perimeter: 2.2000000328
            with BuildLine():
                Line((1.2000000179, -0.5000000075), (1.2000000179, -0.3000000045))
                Line((1.2000000179, -0.3000000045), (0.3000000045, -0.3000000045))
                Line((0.3000000045, -0.3000000045), (0.3000000045, -0.5000000075))
                Line((0.3000000045, -0.5000000075), (1.2000000179, -0.5000000075))
            make_face()
        # OneSide extrude, distance=-0.05
        extrude(amount=-0.05, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude4 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1600000048, perimeter: 1.6000000238
            with BuildLine():
                Line((1.3000000194, 2.7000000402), (1.3000000194, 2.3000000343))
                Line((1.3000000194, 2.3000000343), (1.7000000253, 2.3000000343))
                Line((1.7000000253, 2.3000000343), (1.7000000253, 2.7000000402))
                Line((1.7000000253, 2.7000000402), (1.3000000194, 2.7000000402))
            make_face()
        # OneSide extrude, distance=-0.35
        extrude(amount=-0.35)
    return part.part


def model_41624_a15f83c1_0020():
    """Model: Knobs v1 (12)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.2644910431, perimeter: 7.2256631033
            with BuildLine():
                CenterArc((0, 0), 0.75, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.05
        extrude(amount=0.05)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            Circle(0.4)
        # OneSide extrude, distance=1.3
        extrude(amount=1.3, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.045, perimeter: 1.1
            with BuildLine():
                Line((0.0500000011, 0.2999999832), (-0.0499999989, 0.2999999832))
                Line((0.0500000011, 0.7499999832), (0.0500000011, 0.2999999832))
                Line((-0.0499999989, 0.7499999832), (0.0500000011, 0.7499999832))
                Line((-0.0499999989, 0.2999999832), (-0.0499999989, 0.7499999832))
            make_face()
        # OneSide extrude, distance=1.3
        extrude(amount=1.3, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude4 (Join)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0450000026, perimeter: 1.1000000551
            with BuildLine():
                Line((-0.0499999989, 0.7500000112), (-0.0499999989, 0.2999999832))
                Line((-0.0499999989, 0.2999999832), (0.0500000007, 0.2999999832))
                Line((0.0500000007, 0.2999999832), (0.0500000007, 0.7500000112))
                Line((0.0500000007, 0.7500000112), (-0.0499999989, 0.7500000112))
            make_face()
        # OneSide extrude, distance=1.3
        extrude(amount=1.3, mode=Mode.ADD)
    return part.part


def model_41647_00943ed3_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 26.9516808664, perimeter: 29.1362817987
            with BuildLine():
                CenterArc((-3.2, 0), 1.6, 90, 180)
                Line((3.2, -1.6), (-3.2, -1.6))
                CenterArc((3.2, 0), 1.6, -90, 180)
                Line((-3.2, 1.6), (3.2, 1.6))
            make_face()
            with BuildLine():
                CenterArc((3.2, 0), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-3.2, 0), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=2
        extrude(amount=2)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 6 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1.6), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 12.8, perimeter: 14.4
            with BuildLine():
                Line((-2, 5.2), (-2, 2))
                Line((-2, 2), (2, 2))
                Line((2, 2), (2, 5.2))
                Line((2, 5.2), (-2, 5.2))
            make_face()
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 3.52, perimeter: 9.2832975678
            with BuildLine():
                Line((1.6, 2), (-0.6, 5.2))
                Line((-0.6, 5.2), (-0.6, 2))
                Line((1.6, 2), (-0.6, 2))
            make_face()
        # Symmetric extrude, each_side=0.5
        extrude(amount=0.5, both=True, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 5.2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 11.6496147475, perimeter: 21.471461842
            with BuildLine():
                CenterArc((0, 4.8), 1.5, 8.5834486976, 162.8331026049)
                Line((-2, 1.6), (-1.4831993052, 5.0238745657))
                Line((2, 1.6), (-2, 1.6))
                Line((2, 1.6), (1.4831993052, 5.0238745657))
            make_face()
            with BuildLine():
                CenterArc((0, 4.8), 1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.ADD)

        # Sketch5 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 5.2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.926990817, perimeter: 15.7079632679
            with BuildLine():
                CenterArc((0, 4.8), 1.5, 171.4165513024, 197.1668973951)
                CenterArc((0, 4.8), 1.5, 8.5834486976, 162.8331026049)
            make_face()
            with BuildLine():
                CenterArc((0, 4.8), 1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)
    return part.part


def model_41648_577daf16_0000():
    """Model: Center Pole"""
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
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.0681415341, perimeter: 3.6636951818
            Circle(0.5830951982)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (NewBody)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.0734511195, perimeter: 9.946880489
            with BuildLine():
                CenterArc((0, 0), 1, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.5830951982, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.4
        extrude(amount=0.4)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.4, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.6990043336, perimeter: 8.3760841622
            with BuildLine():
                CenterArc((0, 0), 0.75, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.5830951982, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=27
        extrude(amount=27, mode=Mode.ADD)
    return part.part


def model_41648_577daf16_0008():
    """Model: Camera Mount Pin"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 3 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.3547816553, perimeter: 2.1382436447
            with BuildLine():
                CenterArc((-0.7320199811, -0.0008062343), 0.35, -131.7526959873, 263.6316011026)
                CenterArc((0, 0), 1, 164.9424665514, 30.2412760252)
            make_face()
            # Profile area: 0.3918427075, perimeter: 4.2501835219
            with BuildLine():
                CenterArc((-0.7320199811, -0.0008062343), 0.5681792427, -99.7181478157, 199.5625047593)
                CenterArc((0, 0), 1, 146.0128441775, 18.9296223738)
                CenterArc((-0.7320199811, -0.0008062343), 0.35, -131.7526959873, 263.6316011026)
                CenterArc((0, 0), 1, -164.8162574234, 18.9296223738)
            make_face()
            # Profile area: 2.3949682908, perimeter: 7.073588238
            with BuildLine():
                CenterArc((0, 0), 1, -145.8866350496, 291.8994792272)
                CenterArc((-0.7320199811, -0.0008062343), 0.5681792427, -99.7181478157, 199.5625047593)
            make_face()
        # OneSide extrude, distance=-1.5
        extrude(amount=-1.5)

        # Sketch1 -> Extrude2 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 3 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.2374998279, perimeter: 2.8404369931
            with BuildLine():
                CenterArc((0, 0), 1.3, 179.1784633077, 1.7692825126)
                CenterArc((-0.7320199811, -0.0008062343), 0.5681792427, -177.9124863023, 78.1943384866)
                CenterArc((0, 0), 1, -164.8162574234, 18.9296223738)
                CenterArc((-0.7320199811, -0.0008062343), 0.35, 131.8789051152, 96.3683988974)
                CenterArc((0, 0), 1, 146.0128441775, 18.9296223738)
                CenterArc((-0.7320199811, -0.0008062343), 0.5681792427, 99.8443569436, 78.1943384866)
            make_face()
            # Profile area: 0.0300634448, perimeter: 1.1164908861
            with BuildLine():
                CenterArc((0, 0), 1, 164.9424665514, 30.2412760252)
                CenterArc((-0.7320199811, -0.0008062343), 0.35, 131.8789051152, 96.3683988974)
            make_face()
            # Profile area: 1.9001356583, perimeter: 14.7734478735
            with BuildLine():
                CenterArc((-0.7320199811, -0.0008062343), 0.5681792427, 99.8443569436, 78.1943384866)
                CenterArc((0, 0), 1, -145.8866350496, 291.8994792272)
                CenterArc((-0.7320199811, -0.0008062343), 0.5681792427, -177.9124863023, 78.1943384866)
                CenterArc((0, 0), 1.3, -179.0522541797, 358.2307174874)
            make_face()
        # OneSide extrude, distance=-0.3
        extrude(amount=-0.3)

        # Sketch2 -> Extrude3 (Join)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.1513771301, perimeter: 15.7660267552
            with BuildLine():
                CenterArc((1.4003912034, -0.0003912034), 1.2996087966, -90, 180)
                Line((1.4003912034, 1.2992175932), (0, 1.2992175932))
                Line((0, 1.2992175932), (0, -1.3))
                Line((0, -1.3), (1.4003912034, -1.3))
            make_face()
            with BuildLine():
                CenterArc((1.4003912034, -0.0003912034), 1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=0.75
        extrude(amount=0.75, both=True, mode=Mode.ADD)

        # Sketch1 -> Extrude4 (Join)
        # Sketch on YZ construction plane
        # Sketch has 3 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.2374998279, perimeter: 2.8404369931
            with BuildLine():
                CenterArc((0, 0), 1.3, 179.1784633077, 1.7692825126)
                CenterArc((-0.7320199811, -0.0008062343), 0.5681792427, -177.9124863023, 78.1943384866)
                CenterArc((0, 0), 1, -164.8162574234, 18.9296223738)
                CenterArc((-0.7320199811, -0.0008062343), 0.35, 131.8789051152, 96.3683988974)
                CenterArc((0, 0), 1, 146.0128441775, 18.9296223738)
                CenterArc((-0.7320199811, -0.0008062343), 0.5681792427, 99.8443569436, 78.1943384866)
            make_face()
        # OneSide extrude, distance=3
        extrude(amount=3, mode=Mode.ADD)

        # Sketch1 -> Extrude5 (Join)
        # Sketch on YZ construction plane
        # Sketch has 3 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.3918427075, perimeter: 4.2501835219
            with BuildLine():
                CenterArc((-0.7320199811, -0.0008062343), 0.5681792427, -99.7181478157, 199.5625047593)
                CenterArc((0, 0), 1, 146.0128441775, 18.9296223738)
                CenterArc((-0.7320199811, -0.0008062343), 0.35, -131.7526959873, 263.6316011026)
                CenterArc((0, 0), 1, -164.8162574234, 18.9296223738)
            make_face()
        # OneSide extrude, distance=3
        extrude(amount=3, mode=Mode.ADD)

        # Sketch1 -> Extrude6 (Cut)
        # Sketch on YZ construction plane
        # Sketch has 3 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.3547816553, perimeter: 2.1382436447
            with BuildLine():
                CenterArc((-0.7320199811, -0.0008062343), 0.35, -131.7526959873, 263.6316011026)
                CenterArc((0, 0), 1, 164.9424665514, 30.2412760252)
            make_face()
        # OneSide extrude, distance=3
        extrude(amount=3, mode=Mode.SUBTRACT)

        # Sketch1 -> Extrude7 (Cut)
        # Sketch on YZ construction plane
        # Sketch has 3 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0300634448, perimeter: 1.1164908861
            with BuildLine():
                CenterArc((0, 0), 1, 164.9424665514, 30.2412760252)
                CenterArc((-0.7320199811, -0.0008062343), 0.35, 131.8789051152, 96.3683988974)
            make_face()
        # OneSide extrude, distance=3
        extrude(amount=3, mode=Mode.SUBTRACT)

        # Sketch2 -> Extrude8 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            with Locations((1.4003912034, -0.0003912034)):
                Circle(1)
        # Symmetric extrude, each_side=0.75
        extrude(amount=0.75, both=True, mode=Mode.SUBTRACT)
    return part.part


def model_41650_9417da80_0004():
    """Model: small connector v4"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.8225248646, perimeter: 3.8160397834
            with BuildLine():
                Line((0.3290099458, -0.625), (0.3290099458, 0.625))
                Line((0.3290099458, 0.625), (-0.3290099458, 0.625))
                Line((-0.3290099458, 0.625), (-0.3290099458, -0.625))
                Line((-0.3290099458, -0.625), (0.3290099458, -0.625))
            make_face()
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 0.1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0078539819, perimeter: 0.31415927
            with Locations((0, -0.5000000075)):
                Circle(0.0500000007)
        # OneSide extrude, distance=-0.25
        extrude(amount=-0.25, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0078539819, perimeter: 0.31415927
            Circle(0.0500000007)
        # OneSide extrude, distance=-0.3
        extrude(amount=-0.3, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 0.1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0078539819, perimeter: 0.31415927
            with Locations((0, 0.5000000075)):
                Circle(0.0500000007)
        # OneSide extrude, distance=-0.3
        extrude(amount=-0.3, mode=Mode.SUBTRACT)
    return part.part


def model_41650_9417da80_0005():
    """Model: Longest connector v4"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 6, perimeter: 14
            with BuildLine():
                Line((0.5, -3), (0.5, 3))
                Line((0.5, 3), (-0.5, 3))
                Line((-0.5, 3), (-0.5, -3))
                Line((-0.5, -3), (0.5, -3))
            make_face()
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0078539816, perimeter: 0.3141592654
            with Locations((0, -2.5000000373)):
                Circle(0.05)
        # OneSide extrude, distance=-0.3
        extrude(amount=-0.3, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0078539816, perimeter: 0.3141592654
            Circle(0.05)
        # OneSide extrude, distance=-0.4
        extrude(amount=-0.4, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0078539816, perimeter: 0.3141592654
            with Locations((0, 2.5000000373)):
                Circle(0.05)
        # OneSide extrude, distance=-0.4
        extrude(amount=-0.4, mode=Mode.SUBTRACT)
    return part.part


def model_41672_f0bd39e4_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch4 -> Extrude5 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 8 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.1676671895, perimeter: 3.8823296782
            with BuildLine():
                Line((-0.1000000015, 0.0658359243), (-0.1000000015, 0.8000000119))
                Line((-0.2329179651, 0.0658359243), (-0.1000000015, 0.0658359243))
                Line((-0.6000000089, 0.8000000119), (-0.2329179651, 0.0658359243))
                Line((-0.7000000104, 0.8000000119), (-0.6000000089, 0.8000000119))
                Line((-0.3000000045, 0), (-0.7000000104, 0.8000000119))
                Line((0, 0), (-0.3000000045, 0))
                Line((0, 0.8000000119), (0, 0))
                Line((-0.1000000015, 0.8000000119), (0, 0.8000000119))
            make_face()
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)

        # Sketch5 -> Extrude6 (Join)
        # Sketch on YZ construction plane
        # Sketch has 13 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.4000000119, perimeter: 2.6944272312
            with BuildLine():
                Line((-0.7000000104, 0.8000000119), (-0.3000000045, 0))
                Line((0, 0), (-0.3000000045, 0))
                Line((0, 0.8000000119), (0, 0))
                Line((-0.7000000104, 0.8000000119), (0, 0.8000000119))
            make_face()
        # OneSide extrude, distance=-0.05
        extrude(amount=-0.05, mode=Mode.ADD)

        # Sketch8 -> Extrude8 (Join)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(1.5, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.2323328224, perimeter: 2.1879024619
            with BuildLine():
                Line((-0.6000000089, 0.8000000119), (-0.1000000015, 0.8000000119))
                Line((-0.2329179651, 0.0658359243), (-0.6000000089, 0.8000000119))
                Line((-0.1000000015, 0.0658359243), (-0.2329179651, 0.0658359243))
                Line((-0.1000000015, 0.8000000119), (-0.1000000015, 0.0658359243))
            make_face()
            # Profile area: 0.1676671895, perimeter: 3.8823296782
            with BuildLine():
                Line((-0.1000000015, 0.8000000119), (-0.1000000015, 0.0658359243))
                Line((-0.1000000015, 0.0658359243), (-0.2329179651, 0.0658359243))
                Line((-0.2329179651, 0.0658359243), (-0.6000000089, 0.8000000119))
                Line((-0.7000000104, 0.8000000119), (-0.6000000089, 0.8000000119))
                Line((-0.3000000045, 0), (-0.7000000104, 0.8000000119))
                Line((0, 0), (-0.3000000045, 0))
                Line((0, 0.8000000119), (0, 0))
                Line((-0.1000000015, 0.8000000119), (0, 0.8000000119))
            make_face()
        # OneSide extrude, distance=0.05
        extrude(amount=0.05, mode=Mode.ADD)
    return part.part


def model_41717_5bfe31cb_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 522.7924334839, perimeter: 81.0530904626
            Circle(12.9)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 0.2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 12.5663706144, perimeter: 12.5663706144
            with Locations((-10, 0)):
                Circle(2)
        # OneSide extrude, distance=-2.5
        extrude(amount=-2.5, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.9087385212, perimeter: 7.853981634
            Circle(1.25)
        # OneSide extrude, distance=-1.5
        extrude(amount=-1.5, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude5 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 6.3995003333, perimeter: 9.9792461676
            with BuildLine():
                CenterArc((-0.0093515349, -12.7342227565), 1.75, 4.432982653, 171.0498829723)
                Line((-1.7539157301, -12.5963976187), (-1.7963429747, -13.1334335544))
                Line((1.7844186949, -13.2310858764), (-1.7963429747, -13.1334335544))
                Line((1.7354132058, -12.5989600508), (1.7844186949, -13.2310858764))
            make_face()
        # Symmetric extrude, each_side=1
        extrude(amount=1, both=True, mode=Mode.SUBTRACT)
    return part.part


def model_41757_c1173a7e_0005():
    """Model: Floor v8"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 506.7074790975, perimeter: 79.7964534012
            Circle(12.7)
        # OneSide extrude, distance=0.762
        extrude(amount=0.762)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 0.762, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 45.603671749, perimeter: 23.9389356608
            with Locations((0, -7.6199998856)):
                Circle(3.8099999428)
        # OneSide extrude, distance=0.00000254
        extrude(amount=0.00000254, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 0.762, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 89.0285964777, perimeter: 38.1367329081
            with BuildLine():
                CenterArc((0, 0), 12.7, 48.5903779991, 82.8192440017)
                CenterArc((0, 15.2399997711), 10.1599998474, -145.7711347563, 111.5422695126)
            make_face()
        # OneSide extrude, distance=-1.27
        extrude(amount=-1.27, mode=Mode.SUBTRACT)

        # Sketch6 -> Extrude6 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.762, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 31.6692174436, perimeter: 19.9491133503
            with Locations((-8.6786771872, -0.7217440861)):
                Circle(3.175)
        # OneSide extrude, distance=-0.762
        extrude(amount=-0.762, mode=Mode.SUBTRACT)
    return part.part


def model_41757_c1173a7e_0025():
    """Model: Spokes v5 (2)"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 2.1408390992, perimeter: 5.1867694711
            Circle(0.8255)
        # OneSide extrude, distance=-17.78
        extrude(amount=-17.78)

        # Sketch3 -> Extrude2 (NewBody)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.3420275484, perimeter: 10.7725212092
            with BuildLine():
                CenterArc((0, 0), 0.889, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.8255, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.27
        extrude(amount=1.27)

        # Sketch4 -> Extrude3 (Cut)
        # Sketch on YZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 10.8386886918, perimeter: 29.9720009565
            with BuildLine():
                Line((1.2700000405, 1.0160000324), (1.2700000405, 0.2540000081))
                Line((1.2700000405, 0.2540000081), (15.4940004945, 0.2540000081))
                Line((15.4940004945, 0.2540000081), (15.4940004945, 1.0160000324))
                Line((15.4940004945, 1.0160000324), (1.2700000405, 1.0160000324))
            make_face()
        # Symmetric extrude, each_side=0.127
        extrude(amount=0.127, both=True, mode=Mode.SUBTRACT)

        # Sketch6 -> Extrude4 (Cut)
        # Sketch on YZ construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.96774, perimeter: 4.064
            with BuildLine():
                Line((16.7639998128, 0.1015999896), (15.4939998128, 0.1015999896))
                Line((16.7639998128, 0.8635999896), (16.7639998128, 0.1015999896))
                Line((15.4939998128, 0.8635999896), (16.7639998128, 0.8635999896))
                Line((15.4939998128, 0.1015999896), (15.4939998128, 0.8635999896))
            make_face()
        # Symmetric extrude, each_side=0.381
        extrude(amount=0.381, both=True, mode=Mode.SUBTRACT)
    return part.part


def model_41759_f26a9c8c_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2499999888, perimeter: 1.9999999553
            with BuildLine():
                Line((0.2499999944, -0.2499999944), (-0.2499999944, -0.2499999944))
                Line((0.2499999944, 0.2499999944), (0.2499999944, -0.2499999944))
                Line((-0.2499999944, 0.2499999944), (0.2499999944, 0.2499999944))
                Line((-0.2499999944, -0.2499999944), (-0.2499999944, 0.2499999944))
            make_face()
        # OneSide extrude, distance=0.35
        extrude(amount=0.35)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 10 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.2499999944), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0323999986, perimeter: 0.7199999839
            with BuildLine():
                Line((-0.0499999989, 0.3049999932), (-0.2299999949, 0.3049999932))
                Line((-0.2299999949, 0.3049999932), (-0.2299999949, 0.1249999972))
                Line((-0.2299999949, 0.1249999972), (-0.0499999989, 0.1249999972))
                Line((-0.0499999989, 0.3049999932), (-0.0499999989, 0.1249999972))
            make_face()
            # Profile area: 0.0323999986, perimeter: 0.7199999839
            with BuildLine():
                Line((0.0499999989, 0.1249999972), (0.2299999949, 0.1249999972))
                Line((0.2299999949, 0.1249999972), (0.2299999949, 0.3049999932))
                Line((0.2299999949, 0.3049999932), (0.0499999989, 0.3049999932))
                Line((0.0499999989, 0.3049999932), (0.0499999989, 0.1249999972))
            make_face()
        # OneSide extrude, distance=-0.01
        extrude(amount=-0.01, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.35, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.096211275, perimeter: 1.0995574288
            Circle(0.175)
        # OneSide extrude, distance=-0.02
        extrude(amount=-0.02, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.2399999944), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0209999991, perimeter: 0.579999987
            with BuildLine():
                Line((-0.0749999983, 0.1399999969), (-0.0749999983, 0.2899999935))
                Line((-0.0749999983, 0.2899999935), (-0.2149999952, 0.2899999935))
                Line((-0.2149999952, 0.2899999935), (-0.2149999952, 0.1399999969))
                Line((-0.2149999952, 0.1399999969), (-0.0749999983, 0.1399999969))
            make_face()
            # Profile area: 0.0201061921, perimeter: 0.5026548133
            with Locations((0.1449999968, 0.2149999952)):
                Circle(0.0799999982)
        # OneSide extrude, distance=0.06
        extrude(amount=0.06, mode=Mode.ADD)

        # Sketch5 -> Extrude5 (Cut)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 0, 0.2999999944), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0028274333, perimeter: 0.188495555
            with Locations((-0.1449999968, 0.2149999952)):
                Circle(0.0299999993)
        # OneSide extrude, distance=-0.01
        extrude(amount=-0.01, mode=Mode.SUBTRACT)
    return part.part


def model_41762_1092e172_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 27.56, perimeter: 26.4
            with BuildLine():
                Line((0, 2.6), (0, 0))
                Line((0, 0), (10.6, 0))
                Line((10.6, 0), (10.6, 2.6))
                Line((10.6, 2.6), (0, 2.6))
            make_face()
        # OneSide extrude, distance=15
        extrude(amount=15)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 15, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 24.4800007296, perimeter: 25.2000003755
            with BuildLine():
                Line((-10.400000155, -0.200000003), (-0.200000003, -0.200000003))
                Line((-10.400000155, -2.6000000387), (-10.400000155, -0.200000003))
                Line((-0.200000003, -2.6000000387), (-10.400000155, -2.6000000387))
                Line((-0.200000003, -0.200000003), (-0.200000003, -2.6000000387))
            make_face()
        # OneSide extrude, distance=-15
        extrude(amount=-15, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(10.6, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            with Locations((0.8467362889, 14.2033262244)):
                Circle(0.1)
        # OneSide extrude, distance=-20
        extrude(amount=-20, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            with Locations((-0.8467362889, 10.3762478603)):
                Circle(0.1)
        # OneSide extrude, distance=-20
        extrude(amount=-20, mode=Mode.SUBTRACT)
    return part.part


def model_41780_da6cd1db_0015():
    """Model: Rod/Seal"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.7671458676, perimeter: 4.7123889804
            Circle(0.75)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)

        # Sketch4 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1963495467, perimeter: 1.5707963502
            Circle(0.2500000037)
        # OneSide extrude, distance=-3.5
        extrude(amount=-3.5, mode=Mode.ADD)
    return part.part


def model_41845_a5180a74_0000():
    """Model: Back Wheel/Leg"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.09, perimeter: 1.2
            with BuildLine():
                Line((0.3, -1.8000000224), (0, -1.8000000224))
                Line((0.3, -1.5000000224), (0.3, -1.8000000224))
                Line((0, -1.5000000224), (0.3, -1.5000000224))
                Line((0, -1.8000000224), (0, -1.5000000224))
            make_face()
        # OneSide extrude, distance=0.05
        extrude(amount=0.05)

        # Sketch5 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.0019634954, perimeter: 0.1570796327
            with Locations((0.15, 1.6500000224)):
                Circle(0.025)
        # OneSide extrude, distance=-0.3
        extrude(amount=-0.3, mode=Mode.SUBTRACT)

        # Sketch6 -> Extrude6 (Join)
        # Sketch on BRepFace
        # Sketch has 6 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1.5000000224), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.0400000002, perimeter: 0.8000000022
            with BuildLine():
                Line((-0.25, 0), (-0.0499999989, 0))
                Line((-0.25, -0.2), (-0.25, 0))
                Line((-0.0499999989, -0.2), (-0.25, -0.2))
                Line((-0.0499999989, 0), (-0.0499999989, -0.2))
            make_face()
        # OneSide extrude, distance=-0.025
        extrude(amount=-0.025, mode=Mode.ADD)

        # Sketch8 -> Extrude7 (Join)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1.8000000224), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0400000002, perimeter: 0.8000000022
            with BuildLine():
                Line((0.0499999989, 0), (0.25, 0))
                Line((0.0499999989, -0.2), (0.0499999989, 0))
                Line((0.25, -0.2), (0.0499999989, -0.2))
                Line((0.25, 0), (0.25, -0.2))
            make_face()
        # OneSide extrude, distance=-0.025
        extrude(amount=-0.025, mode=Mode.ADD)

        # Sketch9 -> Extrude8 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1.5000000224), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.0044178647, perimeter: 0.235619449
            with Locations((-0.1483448217, -0.1)):
                Circle(0.0375)
        # OneSide extrude, distance=-0.36
        extrude(amount=-0.36, mode=Mode.SUBTRACT)
    return part.part


def model_41859_173a686e_0000():
    """Model: Fish v5"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.9991374345, perimeter: 5.0587087729
            with BuildLine():
                Line((0.1334333638, 0.3202400731), (0.4500000067, 0.5500000082))
                CenterArc((1.2742320336, 1.8398838224), 1.5307379555, -122.5784601202, 28.4646928006)
                CenterArc((1.1727272743, 0.849980168), 0.5369547133, -90.8863233758, 74.6462156563)
                CenterArc((1.1252421715, 0.6197601697), 0.5686771488, 8.0924880355, 66.8721961103)
                CenterArc((0.9954226495, 0.9218824229), 0.371444219, 41.698119316, 82.2508411485)
                Line((0.9000000134, 1.1500000171), (0.787988077, 1.2300085431))
                Line((0.4500000067, 0.9500000142), (0.9000000134, 1.1500000171))
                Line((0.1000000015, 1.2000000179), (0.4500000067, 0.9500000142))
                CenterArc((-0.4360523518, 0.7391132612), 0.7069432282, -36.3355554303, 77.0238190976)
            make_face()
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.0111343096, perimeter: 0.3740559603
            with Locations((-1.4384321791, 0.9123108519)):
                Circle(0.0595328551)
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.0096176365, perimeter: 0.6219878125
            with BuildLine():
                CenterArc((-1.1727272743, 0.849980168), 0.5369547133, -155.7508823185, 5.284287241)
                CenterArc((-1.5947992596, 0.9449538315), 0.3624738475, -97.1498714049, 44.1536430435)
                CenterArc((-1.4035232092, 0.3481432822), 0.3085141012, 85.0006643471, 30.2480146166)
                CenterArc((-1.5958447208, 0.7892187436), 0.1730404836, -112.5864535534, 43.1307954764)
            make_face()
        # OneSide extrude, distance=-0.45
        extrude(amount=-0.45, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 0, 0.3), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0295763699, perimeter: 0.6209458946
            with BuildLine():
                CenterArc((0.9999999776, 1.3699999694), 0.0999999978, -54.9662767746, 288.7620907207)
                CenterArc((0.9954226495, 0.9218824229), 0.371444219, 80.3940727491, 18.0413916731)
            make_face()
        # OneSide extrude, distance=-0.3
        extrude(amount=-0.3, mode=Mode.ADD)

        # Sketch5 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.3), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0201061921, perimeter: 0.5026548133
            with Locations((0.9999999776, 1.3699999694)):
                Circle(0.0799999982)
        # OneSide extrude, distance=-0.41
        extrude(amount=-0.41, mode=Mode.SUBTRACT)
    return part.part


def model_41859_173a686e_0001():
    """Model: FlipFlopBase v5"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 0.5918229215, perimeter: 3.3068175594
            with BuildLine():
                CenterArc((0.938289733, 0.3043589009), 0.1980408839, -177.9859111952, 179.2637773856)
                CenterArc((-1.7386180467, 0.3394926033), 2.8750635064, -0.6121595499, 6.6769410875)
                CenterArc((2.8953578894, 0.503267309), 1.7805152392, 163.7081387999, 11.7826183506)
                CenterArc((0.7390584963, 1.171131491), 0.4779227577, -20.6284937663, 41.2569875326)
                CenterArc((1.0039395234, 1.3020065842), 0.1862145155, 11.6178628975, 97.1661329311)
                CenterArc((1.0726574042, 1.0647519234), 0.4331084968, 107.2838732016, 88.6471610611)
                CenterArc((-1.6528212637, 0.3164051421), 2.3932679317, -0.4550263669, 15.7041068728)
            make_face()
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.0078539816, perimeter: 0.3141592654
            with Locations((-0.9935724257, 1.2861154593)):
                Circle(0.05)
        # OneSide extrude, distance=-0.1
        extrude(amount=-0.1, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 0, 0.1), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0279298819, perimeter: 0.6183120984
            with BuildLine():
                CenterArc((0.9999999776, 1.5499999654), 0.0999999978, -47.049760995, 275.6296578407)
                CenterArc((1.0726574042, 1.0647519234), 0.4331084968, 107.2838732016, 1.4098024393)
                CenterArc((1.0039395234, 1.3020065842), 0.1862145155, 69.8336967335, 38.9502990951)
            make_face()
        # OneSide extrude, distance=-0.1
        extrude(amount=-0.1, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.1), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0201061921, perimeter: 0.5026548133
            with Locations((0.9999999776, 1.5499999654)):
                Circle(0.0799999982)
        # OneSide extrude, distance=-0.14
        extrude(amount=-0.14, mode=Mode.SUBTRACT)
    return part.part


def model_41859_173a686e_0006():
    """Model: Smile v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 0.8153078759, perimeter: 3.540469717
            with BuildLine():
                CenterArc((0.7999999821, 1.5799999647), 0.0999999978, -56.2050991348, 292.4102041578)
                CenterArc((0.8000000119, 1.0000000149), 0.5000000075, 96.3870530134, 347.2258998613)
            make_face()
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)

        # Sketch3 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.0235438712, perimeter: 0.6387362852
            with Locations((-0.9299999792, 1.1999999732)):
                Ellipse(0.1399999969, 0.0535303367, rotation=90)
        # OneSide extrude, distance=-0.35
        extrude(amount=-0.35, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.022047463, perimeter: 0.6311644349
            with Locations((-0.669999985, 1.1999999732)):
                Ellipse(0.1399999969, 0.0501280401, rotation=90)
        # OneSide extrude, distance=-0.3
        extrude(amount=-0.3, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude4 (Cut)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.0268800883, perimeter: 2.3415899449
            with BuildLine():
                CenterArc((-1.1241946358, 0.9324635267), 0.0709578179, 82.4543585704, 50.1614610752)
                CenterArc((-1.1654254125, 0.9721080475), 0.0143013219, 118.4511576572, 175.1887308224)
                CenterArc((-1.1500861471, 0.9524485948), 0.0116301048, 94.5803001237, 51.0935956821)
                CenterArc((-0.7992895892, 1.0108335768), 0.3548241472, -172.4221127917, 164.8442255833)
                CenterArc((-0.4381991661, 0.956010846), 0.0123368544, 40.613488124, 98.7730237521)
                CenterArc((-0.424085649, 0.9758006629), 0.0126816302, -111.9891119896, 172.8011976965)
                CenterArc((-0.4610531968, 0.9036692209), 0.0937273202, 62.5870711987, 41.4710532466)
                CenterArc((-0.4823870517, 0.9812587301), 0.0134074686, 96.135890746, 192.8183879856)
                CenterArc((-0.4725247916, 0.9656774493), 0.0062245725, 27.7764177448, 124.4471645105)
                CenterArc((-0.7967135332, 1.0113182407), 0.3324548226, -173.8741443174, 166.4878242061)
                CenterArc((-1.121329428, 0.9690955969), 0.0089884236, 63.1291036242, 68.2405047088)
                CenterArc((-1.1154742094, 0.9899046145), 0.0129161018, -97.9777908897, 185.3264904394)
            make_face()
        # OneSide extrude, distance=-0.3
        extrude(amount=-0.3, mode=Mode.SUBTRACT)

        # Sketch2 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.3), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.020106164, perimeter: 0.5026544622
            with Locations((0.7999999821, 1.5799999647)):
                Circle(0.0799999423)
        # OneSide extrude, distance=-0.3
        extrude(amount=-0.3, mode=Mode.SUBTRACT)
    return part.part


def model_41859_173a686e_0008():
    """Model: Dragon v3"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 0.0314159275, perimeter: 0.6283185401
            with Locations((0.7500000112, 1.5500000231)):
                Circle(0.1000000015)
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.2063784512, perimeter: 8.6415919438
            with BuildLine():
                CenterArc((1.288807566, 0.6528070714), 0.1715774592, -162.5135360726, 42.5303288151)
                CenterArc((1.414140022, 0.6633818429), 0.2643772555, -142.9771633153, 59.5571456033)
                CenterArc((1.4592511653, 0.2027647654), 0.1985349277, -16.0485294241, 110.3283392717)
                CenterArc((1.5697762579, 0.4259956271), 0.2894689223, -73.9003016985, 78.5082617261)
                CenterArc((1.7672636784, 1.0446547669), 0.6023248471, -94.0067855401, 12.7007912022)
                CenterArc((1.6771287935, 0.4117029224), 0.0577835421, 33.7457005125, 39.920134943)
                CenterArc((1.7540989885, 0.5109878707), 0.0748880096, 144.1741838252, 71.6516323496)
                CenterArc((1.6581677192, 0.4671541916), 0.094474625, 68.116877435, 24.9011993742)
                CenterArc((1.1242679023, 1.380476041), 0.974929597, -59.6450751318, 2.5009041996)
                CenterArc((1.6753215315, 0.5548215499), 0.0604228366, 133.5124829501, 61.4726867729)
                CenterArc((1.5923123618, 0.4662907697), 0.1386770442, 72.6271919158, 25.0576154183)
                CenterArc((1.3346808643, 0.5145183563), 0.2551862099, 20.4606603284, 23.328676224)
                CenterArc((1.3261952492, 2.0781265198), 1.4003393387, -82.0903860883, 3.9891386025)
                CenterArc((1.2856952223, 0.3644237665), 0.4757614353, 38.5833629632, 7.6281496686)
                CenterArc((1.2420016448, 1.0813032758), 0.5909851354, -45.3134692222, 4.3221589765)
                CenterArc((1.4928544792, 0.477850641), 0.2910039305, 38.0146361759, 9.8505056007)
                CenterArc((1.3886460334, 1.1472059576), 0.5928245601, -55.7696042473, 5.8558020645)
                CenterArc((1.7621581383, 0.6521307017), 0.042327101, -40.6576881106, 119.4444710838)
                CenterArc((1.8031034355, 0.6725257529), 0.0487796079, -100.4353994342, 82.9994651815)
                CenterArc((1.7749918917, 0.6191259964), 0.084123473, -64.0648400449, 91.5184536953)
                CenterArc((1.8101158838, 0.6814876913), 0.1380231319, -89.3076829353, 71.7456373415)
                CenterArc((1.3909045633, -0.1842325598), 0.9912007832, 51.1751798791, 5.0665016461)
                CenterArc((2.458301629, 0.7506141726), 0.4747015757, 147.8983409606, 52.1373648724)
                CenterArc((2.0730188559, 0.7298208159), 0.2735795249, 93.5290403581, 45.5121054991)
                CenterArc((1.7068485864, 0.5786705264), 0.3669921535, 64.227405238, 44.1734686158)
                CenterArc((2.1450058916, 0.6327253721), 0.6272620731, 143.8121582451, 8.2197278877)
                CenterArc((1.4950592746, 1.5757275099), 0.5903980282, -95.5273244593, 19.6135759792)
                CenterArc((1.9775586474, 1.6070617662), 0.8210125561, -168.3334077716, 37.2654940916)
                CenterArc((0.5906431847, 1.4441831868), 0.5828727767, -31.5132887974, 31.2042804404)
                CenterArc((2.1829048807, 2.4475346648), 1.706078373, -146.2150187204, 16.2717430775)
                CenterArc((0.0362087409, 1.2492092111), 0.7702880184, -7.3064146628, 26.214550905)
                Line((0.5923855049, 1.2982316911), (0.8002421828, 1.151247326))
                Line((0.5472374148, 1.1239155226), (0.5923855049, 1.2982316911))
                Line((0.2725113078, 1.2075980812), (0.5472374148, 1.1239155226))
                Line((0.2725113078, 1.043712569), (0.2725113078, 1.2075980812))
                Line((0.0015444304, 1.0843576006), (0.2725113078, 1.043712569))
                Line((0.0015444304, 0.8714550541), (0.0015444304, 1.0843576006))
                CenterArc((-0.0756687493, 0.4436636547), 0.4347037572, 18.1970738626, 61.5716169112)
                CenterArc((0.9396764202, 0.9015491468), 0.6831059891, -151.8636356865, 35.2321628601)
                CenterArc((1.1941075556, -0.0314121137), 0.646687561, 122.2207854676, 27.8831562118)
                CenterArc((0.4911012815, 0.4971117495), 0.3586845401, -17.0728741515, 20.0411362872)
                CenterArc((1.491852667, 0.1434714296), 0.7031838518, 143.7665542097, 15.5528583898)
                CenterArc((1.1148784754, 0.1521301741), 0.4492388686, 88.6887043504, 26.3631203624)
            make_face()
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)

        # Sketch3 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.3), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0122718463, perimeter: 0.3926990817
            with Locations((0.7500000112, 1.5500000231)):
                Circle(0.0625)
        # OneSide extrude, distance=-0.8
        extrude(amount=-0.8, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude3 (Cut)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.0041269307, perimeter: 0.5780057234
            with BuildLine():
                CenterArc((-1.3513251498, 1.1361658159), 0.2475610705, -121.4433130707, 16.9887515796)
                CenterArc((-1.3439037238, 0.7322907649), 0.1781463766, 112.8632236613, 19.0349080905)
                CenterArc((-1.5722266218, 1.411053179), 0.5570023765, -78.677676457, 22.6683666792)
                CenterArc((-1.4060261683, 1.2572625088), 0.3405407981, -102.6265014031, 37.8638947608)
            make_face()
        # OneSide extrude, distance=-0.3
        extrude(amount=-0.3, mode=Mode.SUBTRACT)
    return part.part


def model_41896_7d8659e6_0004():
    """Model: Brake Hinge Pin v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.096211275, perimeter: 1.0995574288
            Circle(0.175)
        # OneSide extrude, distance=3.5
        extrude(amount=3.5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))) as sk:
            # Profile area: 0.0294524311, perimeter: 2.3561944902
            with BuildLine():
                CenterArc((0, 0), 0.2, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.175, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # TwoSides extrude, along=-0.05, against=0.15
        extrude(amount=-0.05, mode=Mode.ADD)
        extrude(sk.sketch, amount=0.15, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 3.5), x_dir=(1, 0, 0), z_dir=(0, 0, 1))) as sk:
            # Profile area: 0.0294524311, perimeter: 2.3561944902
            with BuildLine():
                CenterArc((0, 0), 0.2, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.175, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # TwoSides extrude, along=-0.05, against=0.15
        extrude(amount=-0.05, mode=Mode.ADD)
        extrude(sk.sketch, amount=0.15, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -0.15), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))) as sk:
            # Profile area: 0.0333794219, perimeter: 2.6703537556
            with BuildLine():
                CenterArc((0, 0), 0.225, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # TwoSides offset extrude, full=-0.15, trim=-0.05
        extrude(amount=-0.15, mode=Mode.ADD)
        extrude(sk.sketch, amount=-0.05, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 3.65), x_dir=(1, 0, 0), z_dir=(0, 0, 1))) as sk:
            # Profile area: 0.0333794219, perimeter: 2.6703537556
            with BuildLine():
                CenterArc((0, 0), 0.225, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # TwoSides offset extrude, full=-0.15, trim=-0.05
        extrude(amount=-0.15, mode=Mode.ADD)
        extrude(sk.sketch, amount=-0.05, mode=Mode.SUBTRACT)
    return part.part


def model_41896_7d8659e6_0011():
    """Model: Neck Clamp Pin v3"""
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
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1), x_dir=(1, 0, 0), z_dir=(0, 0, 1))) as sk:
            # Profile area: 0.2827433707, perimeter: 6.8052878354
            with BuildLine():
                CenterArc((0, 0), 0.5830951982, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # TwoSides offset extrude, full=-0.8, trim=-0.6
        extrude(amount=-0.8, mode=Mode.ADD)
        extrude(sk.sketch, amount=-0.6, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1), x_dir=(1, 0, 0), z_dir=(0, 0, 1))) as sk:
            # Profile area: 0.2827433707, perimeter: 6.8052878354
            with BuildLine():
                CenterArc((0, 0), 0.5830951982, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # TwoSides offset extrude, full=-0.4, trim=-0.2
        extrude(amount=-0.4, mode=Mode.ADD)
        extrude(sk.sketch, amount=-0.2, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            Circle(0.2)
        # OneSide extrude, distance=3.4
        extrude(amount=3.4, mode=Mode.ADD)
    return part.part


def model_41896_7d8659e6_0014():
    """Model: Neck Clamp Part 2 v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 4.1667673851, perimeter: 11.0705720386
            with BuildLine():
                CenterArc((1.7770828997, 8.7964473744), 9.7164354422, -100.7626448231, 21.369235764)
                CenterArc((3.585880603, -0.3939942976), 0.3605551329, -93.2351616253, 201.4501234361)
                CenterArc((2.3119802756, 2.7748086187), 3.0555580495, -68.5338552598, 0.8692584508)
                CenterArc((2.3119802756, 2.7748086187), 3.0555580495, -119.5283842213, 50.9945289615)
                CenterArc((0.904605149, 0.2901543113), 0.2, -162.216229706, 42.6878454848)
                CenterArc((0, 0), 0.75, 17.783770294, 249.3599954977)
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1), x_dir=(1, 0, 0), z_dir=(0, 0, 1))) as sk:
            # Profile area: 1.3418670706, perimeter: 4.2471127368
            with BuildLine():
                CenterArc((0, 0), 0.75, 17.3252570534, 0.4585132405)
                CenterArc((0, 0), 0.75, 17.783770294, 208.1171639971)
                CenterArc((-0.5947261658, 0.9662186806), 1.5065818551, -87.2303012896, 57.6867939236)
            make_face()
        # TwoSides offset extrude, full=-0.9, trim=-0.1
        extrude(amount=-0.9, mode=Mode.SUBTRACT)
        extrude(sk.sketch, amount=-0.1, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            Circle(0.25)
        # OneSide extrude, distance=-2.2
        extrude(amount=-2.2, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1), x_dir=(1, 0, 0), z_dir=(0, 0, 1))) as sk:
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            Circle(0.25)
        # TwoSides extrude, along=0.1, against=-1.1
        extrude(amount=0.1, mode=Mode.ADD)
        extrude(sk.sketch, amount=-1.1, mode=Mode.ADD)

        # Sketch5 -> Extrude5 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((0, -0.5000000075)):
                Circle(0.2)
        # OneSide extrude, distance=0.25
        extrude(amount=0.25, mode=Mode.SUBTRACT)
    return part.part


def model_41896_7d8659e6_0015():
    """Model: Clamp Part 1 v5"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 9 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 3.3970152883, perimeter: 18.8345843646
            with BuildLine():
                Line((0.6000000089, -1.2093386578), (0.6000000089, -2.3000000343))
                CenterArc((0, 0), 1.35, -63.6121996152, 307.2243992303)
                Line((-0.6000000089, -1.2093386578), (-0.6000000089, -2.3000000343))
                Line((-0.6000000089, -2.3000000343), (-0.200000003, -2.3000000343))
                Line((-0.200000003, -2.3000000343), (-0.200000003, -1.3351029918))
                CenterArc((0, 0), 1.35, -98.519624382, 17.0392487641)
                Line((0.200000003, -2.3000000343), (0.200000003, -1.3351029918))
                Line((0.6000000089, -2.3000000343), (0.200000003, -2.3000000343))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.7
        extrude(amount=0.7)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.3200000095, perimeter: 2.4000000358
            with BuildLine():
                Line((-0.200000003, 0), (-0.200000003, -0.8000000119))
                Line((-0.200000003, -0.8000000119), (0.200000003, -0.8000000119))
                Line((0.200000003, -0.8000000119), (0.200000003, 0))
                Line((0.200000003, 0), (-0.200000003, 0))
            make_face()
        # OneSide extrude, distance=-1.7
        extrude(amount=-1.7, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-0.6000000089, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((0.3499999922, -1.7599999607)):
                Circle(0.2)
        # OneSide extrude, distance=-1.5
        extrude(amount=-1.5, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            with Locations((0, -0.3499999922)):
                Circle(0.1)
        # OneSide extrude, distance=1.5
        extrude(amount=1.5, mode=Mode.SUBTRACT)
    return part.part


def model_41907_7bcecdb1_0004():
    """Model: Pliers Nose Left"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 8 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0558577674, perimeter: 1.5107665407
            with BuildLine():
                Line((0, 0.4), (0, 0.075))
                CenterArc((0, 0), 0.075, 90, 55.1820672498)
                Line((-0.0615727908, 0.0428227911), (-0.1410485287, -0.0714514741))
                CenterArc((-0.0999999978, -0.0999999978), 0.0500000009, 145.1820731918, 159.6358536163)
                Line((0.0428227911, -0.0615727908), (-0.0714514741, -0.1410485287))
                CenterArc((0, 0), 0.075, -55.1820672498, 72.5872253292)
                Line((0.0999999978, 0.0499999989), (0.0715660053, 0.0224345023))
                Line((0.0999999978, 0.0999999978), (0.0999999978, 0.0499999989))
                Line((0.0999999978, 0.0999999978), (0.05, 0.4))
                Line((0, 0.4), (0.05, 0.4))
            make_face()
            with BuildLine():
                CenterArc((-0.1000000015, -0.1000000015), 0.025, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=0.05
        extrude(amount=0.05, both=True)

        # Sketch3 -> Extrude2 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0051918887, perimeter: 0.6622017878
            with BuildLine():
                Line((-0.0714514741, -0.1410485287), (0.0428227911, -0.0615727908))
                CenterArc((0, 0), 0.075, 145.1820672498, 159.6358655004)
                Line((-0.0615727908, 0.0428227911), (-0.1410485287, -0.0714514741))
                CenterArc((-0.0999999978, -0.0999999978), 0.0500000009, -55.1820731918, 200.3641463837)
            make_face()
        # OneSide extrude, distance=-0.05
        extrude(amount=-0.05, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude3 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0019634953, perimeter: 0.1570796292
            Circle(0.0249999994)
        # OneSide extrude, distance=0.025
        extrude(amount=0.025, mode=Mode.SUBTRACT)

        # Sketch7 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.05, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0078539816, perimeter: 0.3141592654
            Circle(0.05)
        # OneSide extrude, distance=-0.025
        extrude(amount=-0.025, mode=Mode.SUBTRACT)
    return part.part


def model_41920_98cdf3b2_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1256.6370614359, perimeter: 125.6637061436
            Circle(20)
        # OneSide extrude, distance=10
        extrude(amount=10)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 10, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 78.5398163397, perimeter: 31.4159265359
            Circle(5)
        # OneSide extrude, distance=-18
        extrude(amount=-18, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 10, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 255.2544031042, perimeter: 204.2035224833
            with BuildLine():
                CenterArc((0, 0), 17.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-5
        extrude(amount=-5, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 10, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.590549649, perimeter: 7.8256189346
            with BuildLine():
                CenterArc((0, 0), 20, -94.3526394116, 8.5963825075)
                CenterArc((-0.0190059897, -19.9999909693), 1.5, 177.7964562153, 184.2981912537)
            make_face()
            # Profile area: 3.4780338216, perimeter: 7.6005661668
            with BuildLine():
                CenterArc((-0.0190059897, -19.9999909693), 1.5, 2.094647469, 175.7018087463)
                CenterArc((0, 0), 20, -94.3526394116, 8.5963825075)
            make_face()
        # OneSide extrude, distance=-12
        extrude(amount=-12, mode=Mode.SUBTRACT)
    return part.part


def model_42230_4b89c7e8_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 3 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 45.1612, perimeter: 40.64
            with BuildLine():
                Line((17.7844327714, 25.3372959003), (0.0044327714, 25.3372959003))
                Line((0.0044327714, 25.3372959003), (0.0044327714, 22.7972959003))
                Line((0.0044327714, 22.7972959003), (17.7844327714, 22.7972959003))
                Line((17.7844327714, 25.3372959003), (17.7844327714, 22.7972959003))
            make_face()
        # OneSide extrude, distance=-12.7
        extrude(amount=-12.7)

        # Sketch3 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 25.3372959003, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 154.8384, perimeter: 50.8
            with BuildLine():
                Line((-1.2744327714, -1.27), (-16.5144327714, -1.27))
                Line((-16.5144327714, -1.27), (-16.5144327714, -11.43))
                Line((-16.5144327714, -11.43), (-1.2744327714, -11.43))
                Line((-1.2744327714, -11.43), (-1.2744327714, -1.27))
            make_face()
        # OneSide extrude, distance=-1.905
        extrude(amount=-1.905, mode=Mode.SUBTRACT)

        # Sketch8 -> Extrude6 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 24.5246419883, perimeter: 17.5552197483
            with Locations((-4.3770590429, 19.5394173507)):
                Circle(2.794)
        # OneSide extrude, distance=-3.175
        extrude(amount=-3.175)
    return part.part


def model_42230_f5bce306_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch6 -> Extrude4 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 28 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 13681.4455601116, perimeter: 897.9889316071
            with BuildLine():
                Line((-659.114571692, -512.7973579392), (-659.114571692, -524.1327805188))
                Line((-659.114571692, -524.1327805188), (-595.6107833558, -524.1327805188))
                Line((-595.6107833558, -524.1327805188), (-595.6107833558, -511.536987791))
                Line((-595.6107833558, -511.536987791), (-581.4405165369, -496.3170715782))
                Line((-581.4405165369, -496.3170715782), (-568.0574867636, -511.536987791))
                Line((-568.0574867636, -511.536987791), (-568.0574867636, -524.1327805188))
                Line((-568.0574867636, -524.1327805188), (-506.0756900486, -524.1327805188))
                Line((-506.0756900486, -524.1327805188), (-506.0756900486, -517.8348841549))
                Line((-506.0756900486, -517.8348841549), (-524.9693791404, -513.636286579))
                Line((-524.9693791404, -513.636286579), (-540.0843304138, -503.9270296846))
                Line((-540.0843304138, -503.9270296846), (-556.6163083691, -484.1148973731))
                Line((-556.6163083691, -484.1148973731), (-556.6163083691, -451.2871125761))
                Line((-556.6163083691, -451.2871125761), (-544.2712726343, -459.2170834474))
                Line((-544.2712726343, -459.2170834474), (-537.1923947999, -459.2170834474))
                Line((-537.1923947999, -459.2170834474), (-537.1923947999, -466.6462461244))
                Line((-537.1923947999, -466.6462461244), (-541.973699323, -468.9999460996))
                Line((-541.973699323, -468.9999460996), (-541.973699323, -477.5021061909))
                Line((-541.973699323, -477.5021061909), (-521.4268124357, -477.5021061909))
                Line((-521.4268124357, -477.5021061909), (-518.1204168446, -473.2510261453))
                Line((-518.1204168446, -473.2510261453), (-519.7736146402, -452.9403103716))
                Line((-519.7736146402, -452.9403103716), (-527.2784059515, -447.1032504628))
                Line((-527.2784059515, -447.1032504628), (-527.9923205919, -438.3322991675))
                Line((-527.9923205919, -438.3322991675), (-545.8687059973, -432.644128205))
                Line((-545.8687059973, -432.644128205), (-539.6119881865, -424.599776734))
                Line((-539.6119881865, -424.599776734), (-539.6119881865, -385.8677140958))
                Line((-539.6119881865, -385.8677140958), (-564.3329633364, -356.9235270917))
                Line((-564.3329633364, -356.9235270917), (-586.2512958807, -356.9235270917))
                Line((-586.2512958807, -356.9235270917), (-609.3553062149, -376.6564587941))
                Line((-609.3553062149, -376.6564587941), (-615.5995716603, -390.3582716507))
                Line((-615.5995716603, -390.3582716507), (-615.5995716603, -413.0195985185))
                Line((-615.5995716603, -413.0195985185), (-600.7396851896, -432.3374509304))
                Line((-600.7396851896, -432.3374509304), (-604.5637582042, -435.279045557))
                Line((-604.5637582042, -435.279045557), (-614.256466537, -422.6785247245))
                Line((-614.256466537, -422.6785247245), (-633.7583529275, -427.5198757366))
                Line((-633.7583529275, -427.5198757366), (-646.4903036555, -448.3029129545))
                Line((-646.4903036555, -448.3029129545), (-646.4903036555, -477.5115058013))
                Line((-646.4903036555, -477.5115058013), (-641.2212609947, -480.7393877917))
                Line((-641.2212609947, -480.7393877917), (-625.1455627291, -480.7393877917))
                Line((-625.1455627291, -480.7393877917), (-619.9029947822, -476.3880983841))
                Line((-619.9029947822, -476.3880983841), (-619.9029947822, -467.4008390466))
                Line((-619.9029947822, -467.4008390466), (-629.0774886892, -461.4093328216))
                Line((-629.0774886892, -461.4093328216), (-629.0774886892, -458.2263451396))
                Line((-629.0774886892, -458.2263451396), (-618.0025639015, -459.0033686032))
                Line((-618.0025639015, -459.0033686032), (-611.2621193984, -450.2407907491))
                Line((-611.2621193984, -450.2407907491), (-608.7468342286, -450.4172646875))
                Line((-608.7468342286, -450.4172646875), (-610.0044768135, -484.0183976871))
                Line((-610.0044768135, -484.0183976871), (-625.1462841759, -503.7027472582))
                Line((-625.1462841759, -503.7027472582), (-659.114571692, -512.7973579392))
            make_face()
        # OneSide extrude, distance=-38.1
        extrude(amount=-38.1)

        # Sketch7 -> Extrude5 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 39 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 25093.7970968091, perimeter: 1451.3407525416
            with BuildLine():
                Line((413.5452016826, -428.3243430926), (436.5074206575, -428.3243430926))
                Line((436.5074206575, -428.3243430926), (448.3817248718, -414.4607941424))
                Line((449.6508138772, -400.3258806674), (448.3817248718, -414.4607941424))
                Line((454.2572365903, -400.7394637028), (449.6508138772, -400.3258806674))
                Line((467.98570291, -411.6925676374), (454.2572365903, -400.7394637028))
                Line((466.6270735023, -426.8247680121), (467.98570291, -411.6925676374))
                Line((467.98570291, -439.7809864621), (466.6270735023, -426.8247680121))
                Line((485.1167314379, -453.448786754), (467.98570291, -439.7809864621))
                Line((466.6270735023, -476.6234637904), (485.1167314379, -453.448786754))
                Line((466.6270735023, -496.1577588195), (466.6270735023, -476.6234637904))
                Line((478.3312970673, -505.4958432199), (466.6270735023, -496.1577588195))
                Line((479.8333574656, -509.6391736987), (478.3312970673, -505.4958432199))
                Line((466.9022044182, -509.6391736987), (479.8333574656, -509.6391736987))
                Line((445.9922548096, -517.2195507403), (466.9022044182, -509.6391736987))
                Line((445.9922548096, -523.6501382518), (445.9922548096, -517.2195507403))
                Line((516.4257692807, -523.6501382518), (445.9922548096, -523.6501382518))
                Line((516.4257692807, -516.2423156804), (516.4257692807, -523.6501382518))
                Line((508.1718418036, -516.2423156804), (516.4257692807, -516.2423156804))
                Line((508.1718418036, -502.2106389694), (508.1718418036, -516.2423156804))
                Line((502.3584695585, -497.4492824578), (508.1718418036, -502.2106389694))
                Line((502.3584695585, -482.8211097941), (502.3584695585, -497.4492824578))
                Line((519.6394196482, -482.8211097941), (502.3584695585, -482.8211097941))
                Line((519.6394196482, -478.0461104272), (519.6394196482, -482.8211097941))
                Line((570.1179843841, -478.0461104272), (519.6394196482, -478.0461104272))
                Line((582.0933796217, -487.596109161), (570.1179843841, -478.0461104272))
                Line((582.0933796217, -506.3929320656), (582.0933796217, -487.596109161))
                Line((573.3630750767, -510.7889632288), (582.0933796217, -506.3929320656))
                Line((573.3630750767, -523.6501382518), (573.3630750767, -510.7889632288))
                Line((637.9713458964, -523.6501382518), (573.3630750767, -523.6501382518))
                Line((639.9331510745, -517.7015571445), (637.9713458964, -523.6501382518))
                Line((633.9872441377, -512.5712323752), (639.9331510745, -517.7015571445))
                Line((617.5525402189, -507.1511688899), (633.9872441377, -512.5712323752))
                Line((618.9672799964, -502.8613982206), (617.5525402189, -507.1511688899))
                Line((627.2781574436, -486.4317549874), (618.9672799964, -502.8613982206))
                Line((610.6564025493, -460.7706487599), (627.2781574436, -486.4317549874))
                Line((584.6966810783, -452.2092935248), (610.6564025493, -460.7706487599))
                Line((581.56080587, -441.9033844061), (584.6966810783, -452.2092935248))
                Line((596.4923204298, -396.6280806171), (581.56080587, -441.9033844061))
                Line((616.8966739093, -373.9876336056), (596.4923204298, -396.6280806171))
                Line((633.1083520162, -365.3227711691), (616.8966739093, -373.9876336056))
                Line((633.1083520162, -373.9876336056), (633.1083520162, -365.3227711691))
                Line((647.3634482827, -391.127319293), (633.1083520162, -373.9876336056))
                Line((663.8165335651, -391.127319293), (647.3634482827, -391.127319293))
                Line((675.561169364, -374.5466569886), (663.8165335651, -391.127319293))
                Line((675.561169364, -356.1454167758), (675.561169364, -374.5466569886))
                Line((647.0839365912, -335.9740435617), (675.561169364, -356.1454167758))
                Line((624.1639778883, -332.6199032637), (647.0839365912, -335.9740435617))
                Line((619.4122791328, -339.3281838597), (624.1639778883, -332.6199032637))
                Line((614.3810686858, -339.3281838597), (619.4122791328, -339.3281838597))
                Line((605.1571828663, -325.9116226678), (614.3810686858, -339.3281838597))
                Line((580.2806423229, -325.9116226678), (605.1571828663, -325.9116226678))
                Line((573.8518734184, -335.0932415757), (580.2806423229, -325.9116226678))
                Line((549.1972189391, -335.0932415757), (573.8518734184, -335.0932415757))
                Line((545.4521052574, -329.7712379228), (549.1972189391, -335.0932415757))
                Line((508.8647889374, -329.7712379228), (545.4521052574, -329.7712379228))
                Line((482.8685378679, -348.0648960829), (508.8647889374, -329.7712379228))
                Line((450.1325180026, -348.0648960829), (482.8685378679, -348.0648960829))
                Line((450.1325180026, -354.8046648787), (450.1325180026, -348.0648960829))
                Line((429.9132116152, -354.8046648787), (450.1325180026, -354.8046648787))
                Line((413.5452016826, -373.0983230387), (429.9132116152, -354.8046648787))
                Line((413.5452016826, -428.3243430926), (413.5452016826, -373.0983230387))
            make_face()
            with BuildLine():
                CenterArc((525.0828959331, -425.4782969026), 36.4304662547, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-50.8
        extrude(amount=-50.8)

        # Sketch8 -> Extrude6 (NewBody)
        # Sketch on BRepFace
        # Sketch has 25 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 283.663266759, perimeter: 77.7599112175
            with BuildLine():
                CenterArc((525.0828959331, -425.4782969026), 9.8358742447, 131.7377394725, 61.0932907008)
                CenterArc((525.0828959331, -425.4782969026), 9.8358742447, -167.1689698267, 85.0681461268)
                CenterArc((525.0828959331, -425.4782969026), 9.8358742447, -82.1008236999, 41.6416431339)
                CenterArc((525.0828959331, -425.4782969026), 9.8358742447, -40.459180566, 57.4351506892)
                CenterArc((525.0828959331, -425.4782969026), 9.8358742447, 16.9759701232, 25.7689185837)
                CenterArc((525.0828959331, -425.4782969026), 9.8358742447, 42.7448887068, 88.9928507656)
            make_face()
            with BuildLine():
                CenterArc((525.0828959331, -425.4782969026), 2.54, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 20.2682991639, perimeter: 15.9592906802
            with Locations((525.0828959331, -425.4782969026)):
                Circle(2.54)
        # OneSide extrude, distance=-38.1
        extrude(amount=-38.1)

        # Sketch8 -> Extrude7 (Join)
        # Sketch on BRepFace
        # Sketch has 25 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 259.5024664732, perimeter: 88.6974977104
            with BuildLine():
                CenterArc((525.0828959331, -425.4782969026), 9.8358742447, 131.7377394725, 61.0932907008)
                Line((518.534938015, -418.1387690391), (513.4761461338, -417.4806826615))
                Line((513.4761461338, -417.4806826615), (513.4761461338, -403.5279185891))
                Line((513.4761461338, -403.5279185891), (507.2915467247, -403.5279185891))
                Line((507.2915467247, -403.5279185891), (507.2915467247, -413.5076100247))
                Line((507.2915467247, -413.5076100247), (496.9739714506, -413.5076100247))
                Line((496.9739714506, -413.5076100247), (496.9739714506, -422.6970049432))
                Line((496.9739714506, -422.6970049432), (509.4457344046, -422.6970049432))
                Line((509.4457344046, -422.6970049432), (509.4457344046, -427.6626142675))
                Line((509.4457344046, -427.6626142675), (515.4926310876, -427.6626142675))
            make_face()
            # Profile area: 259.630538143, perimeter: 63.6024496109
            with BuildLine():
                Line((547.6441806925, -422.606510755), (534.4901945081, -422.606510755))
                Line((547.6441806925, -405.3610419552), (547.6441806925, -422.606510755))
                Line((532.3061953741, -405.3610419552), (547.6441806925, -405.3610419552))
                Line((532.3061953741, -418.8023424884), (532.3061953741, -405.3610419552))
                CenterArc((525.0828959331, -425.4782969026), 9.8358742447, 16.9759701232, 25.7689185837)
            make_face()
            # Profile area: 233.3841684543, perimeter: 68.6012389826
            with BuildLine():
                Line((526.4346431421, -435.2208428553), (526.4346431421, -440.5352391476))
                Line((526.4346431421, -440.5352391476), (517.3810121987, -440.5352391476))
                Line((517.3810121987, -440.5352391476), (517.3810121987, -449.6562491887))
                Line((517.3810121987, -449.6562491887), (535.8912972822, -449.6562491887))
                Line((535.8912972822, -449.6562491887), (535.8912972822, -434.3651441198))
                Line((535.8912972822, -434.3651441198), (532.5667024336, -431.86085614))
                CenterArc((525.0828959331, -425.4782969026), 9.8358742447, -82.1008236999, 41.6416431339)
            make_face()
        # OneSide extrude, distance=-25.4
        extrude(amount=-25.4, mode=Mode.ADD)

        # Sketch8 -> Extrude8 (Cut)
        # Sketch on BRepFace
        # Sketch has 25 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 259.5024664732, perimeter: 88.6974977104
            with BuildLine():
                CenterArc((525.0828959331, -425.4782969026), 9.8358742447, 131.7377394725, 61.0932907008)
                Line((518.534938015, -418.1387690391), (513.4761461338, -417.4806826615))
                Line((513.4761461338, -417.4806826615), (513.4761461338, -403.5279185891))
                Line((513.4761461338, -403.5279185891), (507.2915467247, -403.5279185891))
                Line((507.2915467247, -403.5279185891), (507.2915467247, -413.5076100247))
                Line((507.2915467247, -413.5076100247), (496.9739714506, -413.5076100247))
                Line((496.9739714506, -413.5076100247), (496.9739714506, -422.6970049432))
                Line((496.9739714506, -422.6970049432), (509.4457344046, -422.6970049432))
                Line((509.4457344046, -422.6970049432), (509.4457344046, -427.6626142675))
                Line((509.4457344046, -427.6626142675), (515.4926310876, -427.6626142675))
            make_face()
            # Profile area: 259.630538143, perimeter: 63.6024496109
            with BuildLine():
                Line((547.6441806925, -422.606510755), (534.4901945081, -422.606510755))
                Line((547.6441806925, -405.3610419552), (547.6441806925, -422.606510755))
                Line((532.3061953741, -405.3610419552), (547.6441806925, -405.3610419552))
                Line((532.3061953741, -418.8023424884), (532.3061953741, -405.3610419552))
                CenterArc((525.0828959331, -425.4782969026), 9.8358742447, 16.9759701232, 25.7689185837)
            make_face()
            # Profile area: 233.3841684543, perimeter: 68.6012389826
            with BuildLine():
                Line((526.4346431421, -435.2208428553), (526.4346431421, -440.5352391476))
                Line((526.4346431421, -440.5352391476), (517.3810121987, -440.5352391476))
                Line((517.3810121987, -440.5352391476), (517.3810121987, -449.6562491887))
                Line((517.3810121987, -449.6562491887), (535.8912972822, -449.6562491887))
                Line((535.8912972822, -449.6562491887), (535.8912972822, -434.3651441198))
                Line((535.8912972822, -434.3651441198), (532.5667024336, -431.86085614))
                CenterArc((525.0828959331, -425.4782969026), 9.8358742447, -82.1008236999, 41.6416431339)
            make_face()
        # OneSide extrude, distance=-12.7
        extrude(amount=-12.7, mode=Mode.SUBTRACT)

        # Sketch8 -> Extrude10 (Cut)
        # Sketch on BRepFace
        # Sketch has 25 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 20.2682991639, perimeter: 15.9592906802
            with Locations((525.0828959331, -425.4782969026)):
                Circle(2.54)
        # OneSide extrude, distance=-38.1
        extrude(amount=-38.1, mode=Mode.SUBTRACT)
    return part.part


def model_42329_df7f540f_0056():
    """Model: Arm Pin 30mm"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.020106193, perimeter: 0.5026548246
            Circle(0.08)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.3, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.015393804, perimeter: 0.4398229715
            Circle(0.07)
        # OneSide extrude, distance=0.02
        extrude(amount=0.02, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.015393804, perimeter: 0.4398229715
            Circle(0.07)
        # OneSide extrude, distance=0.02
        extrude(amount=0.02, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -0.02, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.004712389, perimeter: 0.9424777961
            with BuildLine():
                CenterArc((0, 0), 0.08, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.07, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.015393804, perimeter: 0.4398229715
            Circle(0.07)
        # OneSide extrude, distance=0.04
        extrude(amount=0.04, mode=Mode.ADD)

        # Sketch5 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.32, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.004712389, perimeter: 0.9424777961
            with BuildLine():
                CenterArc((0, 0), 0.08, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.07, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.015393804, perimeter: 0.4398229715
            Circle(0.07)
        # OneSide extrude, distance=0.04
        extrude(amount=0.04, mode=Mode.ADD)
    return part.part


def model_42329_df7f540f_0061():
    """Model: hydraulic Rod"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            Circle(0.1)
        # OneSide extrude, distance=2.1
        extrude(amount=2.1)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2.1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.020106193, perimeter: 0.5026548246
            Circle(0.08)
        # OneSide extrude, distance=0.4987
        extrude(amount=0.4987, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.0054338852, perimeter: 0.3315146744
            with BuildLine():
                CenterArc((0, 0), 0.1, -120, 60)
                Line((-0.05, -0.0866025404), (-0.05, -0.15))
                Line((-0.05, -0.15), (0.05, -0.15))
                Line((0.05, -0.15), (0.05, -0.0866025404))
            make_face()
            # Profile area: 0.0054338852, perimeter: 0.3315146744
            with BuildLine():
                CenterArc((0, 0), 0.1, 60, 60)
                Line((0.05, 0.0866025404), (0.05, 0.15))
                Line((0.05, 0.15), (-0.05, 0.15))
                Line((-0.05, 0.15), (-0.05, 0.0866025404))
            make_face()
            # Profile area: 0.0191322295, perimeter: 0.5558496718
            with BuildLine():
                Line((-0.05, 0.0866025404), (-0.05, -0.0866025404))
                CenterArc((0, 0), 0.1, -120, 60)
                Line((0.05, -0.0866025404), (0.05, 0.0866025404))
                CenterArc((0, 0), 0.1, 60, 60)
            make_face()
        # OneSide extrude, distance=0.1
        extrude(amount=0.1, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -0.1, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.03, perimeter: 0.8
            with BuildLine():
                Line((0.05, 0.15), (-0.05, 0.15))
                Line((-0.05, -0.15), (-0.05, 0.15))
                Line((-0.05, -0.15), (0.05, -0.15))
                Line((0.05, 0.15), (0.05, -0.15))
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)
    return part.part


def model_42329_df7f540f_0067():
    """Model: Arm Pin 50mm (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.020106193, perimeter: 0.5026548246
            Circle(0.08)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.015393804, perimeter: 0.4398229715
            Circle(0.07)
        # OneSide extrude, distance=0.02
        extrude(amount=0.02, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.015393804, perimeter: 0.4398229715
            Circle(0.07)
        # OneSide extrude, distance=0.02
        extrude(amount=0.02, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -0.02, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.004712389, perimeter: 0.9424777961
            with BuildLine():
                CenterArc((0, 0), 0.08, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.07, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.015393804, perimeter: 0.4398229715
            Circle(0.07)
        # OneSide extrude, distance=0.04
        extrude(amount=0.04, mode=Mode.ADD)

        # Sketch5 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.52, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.004712389, perimeter: 0.9424777961
            with BuildLine():
                CenterArc((0, 0), 0.08, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.07, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.015393804, perimeter: 0.4398229715
            Circle(0.07)
        # OneSide extrude, distance=0.04
        extrude(amount=0.04, mode=Mode.ADD)
    return part.part


def model_42329_df7f540f_0068():
    """Model: Arm Pin 70mm (3)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.020106193, perimeter: 0.5026548246
            Circle(0.08)
        # OneSide extrude, distance=0.7
        extrude(amount=0.7)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.7, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.015393804, perimeter: 0.4398229715
            Circle(0.07)
        # OneSide extrude, distance=0.02
        extrude(amount=0.02, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.015393804, perimeter: 0.4398229715
            Circle(0.07)
        # OneSide extrude, distance=0.02
        extrude(amount=0.02, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -0.02, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.004712389, perimeter: 0.9424777961
            with BuildLine():
                CenterArc((0, 0), 0.08, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.07, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.015393804, perimeter: 0.4398229715
            Circle(0.07)
        # OneSide extrude, distance=0.04
        extrude(amount=0.04, mode=Mode.ADD)

        # Sketch5 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.72, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.004712389, perimeter: 0.9424777961
            with BuildLine():
                CenterArc((0, 0), 0.08, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.07, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.015393804, perimeter: 0.4398229715
            Circle(0.07)
        # OneSide extrude, distance=0.04
        extrude(amount=0.04, mode=Mode.ADD)
    return part.part


def model_42429_b48647fb_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 11 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 8.6194005031, perimeter: 14.2272160483
            with BuildLine():
                Line((1.5875, 3.01752), (1.5875, 4.96189))
                Line((0.99187, 5.55752), (1.5875, 4.96189))
                Line((0.91313, 5.55752), (0.99187, 5.55752))
                Line((0.3175, 4.96189), (0.91313, 5.55752))
                Line((0.3175, 3.01752), (0.3175, 4.96189))
                Line((0, 3.01752), (0.3175, 3.01752))
                Line((0, 0), (0, 3.01752))
                Line((1.905, 0), (0, 0))
                Line((1.905, 3.01752), (1.905, 0))
                Line((1.5875, 3.01752), (1.905, 3.01752))
            make_face()
        # OneSide extrude, distance=0.635
        extrude(amount=0.635)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on XY construction plane
        # Sketch has 5 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0447726729, perimeter: 0.750086662
            with Locations((1.31064, 0.3175)):
                Circle(0.11938)
            # Profile area: 0.0447726729, perimeter: 0.750086662
            with Locations((0.59436, 0.3175)):
                Circle(0.11938)
        # OneSide extrude, distance=-2.58064
        extrude(amount=-2.58064, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 17 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.635, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0447726729, perimeter: 0.750086662
            with Locations((-0.59436, -3.8608)):
                Circle(0.11938)
        # OneSide extrude, distance=-5.08
        extrude(amount=-5.08, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 17 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.635, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0447726729, perimeter: 0.750086662
            with Locations((-0.71374, -2.58064)):
                Circle(0.11938)
            # Profile area: 0.0447726729, perimeter: 0.750086662
            with Locations((-1.19126, -2.58064)):
                Circle(0.11938)
            # Profile area: 0.0447726729, perimeter: 0.750086662
            with Locations((-0.71374, -0.43688)):
                Circle(0.11938)
            # Profile area: 0.0447726729, perimeter: 0.750086662
            with Locations((-1.19126, -0.43688)):
                Circle(0.11938)
        # OneSide extrude, distance=-0.3175
        extrude(amount=-0.3175, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 17 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.635, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0791730436, perimeter: 0.9974556675
            with Locations((-0.9525, -1.50876)):
                Circle(0.15875)
        # OneSide extrude, distance=-2.54
        extrude(amount=-2.54, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude6 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 17 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.635, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0522580841, perimeter: 0.8103668628
            with Locations((-0.9525, -4.52628)):
                Circle(0.1289738919)
        # OneSide extrude, distance=-2.54
        extrude(amount=-2.54, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude7 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 17 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.635, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1999787598, perimeter: 2.5907324609
            with BuildLine():
                CenterArc((-0.9525, -4.52628), 0.2833539855, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-0.9525, -4.52628), 0.1289738919, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.3175
        extrude(amount=-0.3175, mode=Mode.SUBTRACT)
    return part.part


def model_42568_09cf35f8_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1000, perimeter: 130
            with BuildLine():
                Line((20, -12.5), (20, 12.5))
                Line((20, 12.5), (-20, 12.5))
                Line((-20, 12.5), (-20, -12.5))
                Line((-20, -12.5), (20, -12.5))
            make_face()
        # OneSide extrude, distance=35
        extrude(amount=35)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 7 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 35, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 700, perimeter: 110
            with BuildLine():
                Line((17.5, -10), (-17.5, -10))
                Line((17.5, 10), (17.5, -10))
                Line((-17.5, 10), (17.5, 10))
                Line((-17.5, -10), (-17.5, 10))
            make_face()
        # OneSide extrude, distance=30
        extrude(amount=30, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 7 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 65, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 344.6183562236, perimeter: 79.1031612214
            with BuildLine():
                Line((13.296103112, -6.4796871933), (-13.296103112, -6.4796871933))
                Line((13.296103112, 6.4796871933), (13.296103112, -6.4796871933))
                Line((-13.296103112, 6.4796871933), (13.296103112, 6.4796871933))
                Line((-13.296103112, -6.4796871933), (-13.296103112, 6.4796871933))
            make_face()
        # OneSide extrude, distance=20
        extrude(amount=20, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 7 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 85, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 75, perimeter: 40
            with BuildLine():
                Line((7.5, -2.5), (7.5, 2.5))
                Line((7.5, 2.5), (-7.5, 2.5))
                Line((-7.5, 2.5), (-7.5, -2.5))
                Line((-7.5, -2.5), (7.5, -2.5))
            make_face()
        # OneSide extrude, distance=15
        extrude(amount=15, mode=Mode.ADD)

        # Sketch5 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 100, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.6545259597, perimeter: 7.6479080959
            Circle(1.2172023778)
        # OneSide extrude, distance=15
        extrude(amount=15, mode=Mode.ADD)
    return part.part


def model_42586_517832f9_0015():
    """Model: Hinge1 (1)"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 15.7236339908, perimeter: 20.9718582379
            with BuildLine():
                Line((-3.175, 1.27), (-3.175, -1.27))
                Line((-3.175, -1.27), (3.175, -1.27))
                Line((3.175, -1.27), (3.175, 1.27))
                Line((3.175, 1.27), (-3.175, 1.27))
            make_face()
            with BuildLine():
                CenterArc((-1.9050000608, 0.6350000203), 0.2540000081, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1.9050000608, 0.6350000203), 0.2540000081, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.254
        extrude(amount=0.254)

        # Sketch3 -> Extrude2 (Join)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0688737489, perimeter: 1.7666496909
            with BuildLine():
                CenterArc((-0.8889999893, 0.1269999985), 0.179571031, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-0.8889999893, 0.1269999985), 0.1016, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=2.54
        extrude(amount=2.54, both=True, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0688737489, perimeter: 1.7666496909
            with BuildLine():
                CenterArc((-0.8889999893, 0.1269999985), 0.179571031, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-0.8889999893, 0.1269999985), 0.1016, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=5.08
        extrude(amount=5.08, both=True, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude4 (Join)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0688737489, perimeter: 1.7666496909
            with BuildLine():
                CenterArc((-0.8889999893, 0.1269999985), 0.179571031, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-0.8889999893, 0.1269999985), 0.1016, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=2.286
        extrude(amount=2.286, both=True, mode=Mode.ADD)

        # Sketch3 -> Extrude5 (Cut)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0688737489, perimeter: 1.7666496909
            with BuildLine():
                CenterArc((-0.8889999893, 0.1269999985), 0.179571031, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-0.8889999893, 0.1269999985), 0.1016, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=0.508
        extrude(amount=0.508, both=True, mode=Mode.SUBTRACT)
    return part.part


def model_42601_bfe96b47_0005():
    """Model: Tail Stalk v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 3.7133625165, perimeter: 24.7557501103
            with BuildLine():
                CenterArc((0, 0), 2.12, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.82, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=100
        extrude(amount=100)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on XY construction plane
        # Sketch has 4 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 49.02, perimeter: 38.68
            with BuildLine():
                Line((0, 3), (0, 0))
                Line((0, 0), (16.34, 0))
                Line((16.34, 0), (16.34, 3))
                Line((16.34, 3), (0, 3))
            make_face()
        # OneSide extrude, distance=-7
        extrude(amount=-7, mode=Mode.SUBTRACT)

        # Sketch2 -> Extrude3 (Cut)
        # Sketch on XY construction plane
        # Sketch has 4 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 49.02, perimeter: 38.68
            with BuildLine():
                Line((0, 3), (0, 0))
                Line((0, 0), (16.34, 0))
                Line((16.34, 0), (16.34, 3))
                Line((16.34, 3), (0, 3))
            make_face()
        # OneSide extrude, distance=4.5
        extrude(amount=4.5, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude4 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.515299735, perimeter: 2.5446900494
            with Locations((12.84, 0)):
                Circle(0.405)
            # Profile area: 0.515299735, perimeter: 2.5446900494
            with Locations((3.5, 0)):
                Circle(0.405)
        # OneSide extrude, distance=-4.5
        extrude(amount=-4.5, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude6 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.515299735, perimeter: 2.5446900494
            with Locations((96.5, 0)):
                Circle(0.405)
        # Symmetric extrude, each_side=11
        extrude(amount=11, both=True, mode=Mode.SUBTRACT)
    return part.part


def model_42601_bfe96b47_0006():
    """Model: Top Stalk v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 18.020175461, perimeter: 60.0672515366
            with BuildLine():
                CenterArc((0, 0), 5.08, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 4.48, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=350
        extrude(amount=350)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on XY construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY) as sk:
            # Profile area: 3.1730871199, perimeter: 6.3146012337
            with Locations((343, 0)):
                Circle(1.005)
        # TwoSides extrude, along=31, against=-34
        extrude(amount=31, mode=Mode.SUBTRACT)
        extrude(sk.sketch, amount=-34, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on XY construction plane
        # Sketch has 4 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY) as sk:
            # Profile area: 3.1730871199, perimeter: 6.3146012337
            with Locations((140, 0)):
                Circle(1.005)
            # Profile area: 3.1730871199, perimeter: 6.3146012337
            with Locations((132.5, 0)):
                Circle(1.005)
        # TwoSides extrude, along=21, against=-26
        extrude(amount=21, mode=Mode.SUBTRACT)
        extrude(sk.sketch, amount=-26, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.1730871199, perimeter: 6.3146012337
            with Locations((123.5, 0)):
                Circle(1.005)
            # Profile area: 3.1730871199, perimeter: 6.3146012337
            with Locations((116, 0)):
                Circle(1.005)
        # Symmetric extrude, each_side=13
        extrude(amount=13, both=True, mode=Mode.SUBTRACT)
    return part.part


def model_43529_4804941b_0002():
    """Model: Solid46_tornillito"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.3848451001, perimeter: 2.1991148575
            Circle(0.35)
        # OneSide extrude, distance=0.131
        extrude(amount=0.131)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.131, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            Circle(0.25)
        # OneSide extrude, distance=0.68
        extrude(amount=0.68, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.811, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            Circle(0.2)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.111, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            Circle(0.15)
        # OneSide extrude, distance=-0.15
        extrude(amount=-0.15, mode=Mode.SUBTRACT)
    return part.part


def model_43529_4804941b_0042():
    """Model: Solid70_tornillo mas chico (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.022710006, perimeter: 1.4312393053
            with BuildLine():
                CenterArc((0, 0), 0.65, -120.0002438954, 60.0002444809)
                Line((-0.3250023962, -0.562915129), (0, -0.7505553499))
                Line((0, -0.7505553499), (0.3250000058, -0.5629165091))
            make_face()
            # Profile area: 0.022710006, perimeter: 1.431241773
            with BuildLine():
                Line((-0.3249965295, 0.5629185161), (-0.65, 0.375277675))
                Line((-0.65, 0.375277675), (-0.65, 0))
                CenterArc((0, 0), 0.65, 119.9996467615, 60.0003532385)
            make_face()
            # Profile area: 0.022710006, perimeter: 1.4312257363
            with BuildLine():
                Line((0.3249999969, 0.5629165143), (0, 0.7505553499))
                Line((0, 0.7505553499), (-0.3249965295, 0.5629185161))
                CenterArc((0, 0), 0.65, 60.0000003172, 59.9996464442)
            make_face()
            # Profile area: 0.022710006, perimeter: 1.4312337824
            with BuildLine():
                Line((0.65, -0.0000000085), (0.65, 0.375277675))
                Line((0.65, 0.375277675), (0.3249999969, 0.5629165143))
                CenterArc((0, 0), 0.65, -0.0000007488, 60.000001066)
            make_face()
            # Profile area: 0.022710006, perimeter: 1.4312282244
            with BuildLine():
                CenterArc((0, 0), 0.65, -180, 59.9997561046)
                Line((-0.65, 0), (-0.65, -0.375277675))
                Line((-0.65, -0.375277675), (-0.3250023962, -0.562915129))
            make_face()
            # Profile area: 0.022710006, perimeter: 1.431233728
            with BuildLine():
                Line((0.3250000058, -0.5629165091), (0.65, -0.375277675))
                Line((0.65, -0.375277675), (0.65, -0.0000000085))
                CenterArc((0, 0), 0.65, -59.9999994145, 59.9999986657)
            make_face()
            # Profile area: 1.3273228961, perimeter: 4.0840704497
            with BuildLine():
                CenterArc((0, 0), 0.65, -59.9999994145, 59.9999986657)
                CenterArc((0, 0), 0.65, -0.0000007488, 60.000001066)
                CenterArc((0, 0), 0.65, 60.0000003172, 59.9996464442)
                CenterArc((0, 0), 0.65, 119.9996467615, 60.0003532385)
                CenterArc((0, 0), 0.65, -180, 59.9997561046)
                CenterArc((0, 0), 0.65, -120.0002438954, 60.0002444809)
            make_face()
        # OneSide extrude, distance=0.53
        extrude(amount=0.53)

        # Sketch3 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.53, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            Circle(0.4)
        # OneSide extrude, distance=2.5
        extrude(amount=2.5, mode=Mode.ADD)

        # Sketch4 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-0.325, 0, -0.5629165125), x_dir=(-0.8660254038, 0, 0.5), z_dir=(-0.5, 0, -0.8660254038))):
            # Profile area: 0.0157079633, perimeter: 0.5141592654
            with BuildLine():
                CenterArc((0, 0.265), 0.1, 90, 180)
                Line((0, 0.365), (0, 0.165))
            make_face()
            # Profile area: 0.0157079633, perimeter: 0.5141592654
            with BuildLine():
                Line((0, 0.365), (0, 0.165))
                CenterArc((0, 0.265), 0.1, -90, 180)
            make_face()
        # OneSide extrude, distance=-2
        extrude(amount=-2, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.325, 0, -0.5629165125), x_dir=(-0.8660254038, 0, -0.5), z_dir=(0.5, 0, -0.8660254038))):
            # Profile area: 0.0157079633, perimeter: 0.5141592654
            with BuildLine():
                Line((0, 0.365), (0, 0.165))
                CenterArc((0, 0.265), 0.1, -90, 180)
            make_face()
            # Profile area: 0.0157079633, perimeter: 0.5141592654
            with BuildLine():
                CenterArc((0, 0.265), 0.1, 90, 180)
                Line((0, 0.365), (0, 0.165))
            make_face()
        # OneSide extrude, distance=-2
        extrude(amount=-2, mode=Mode.SUBTRACT)
    return part.part


def model_43529_4804941b_0051():
    """Model: Solid34_tornillo (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.048510723, perimeter: 2.0917899709
            with BuildLine():
                CenterArc((0, 0), 0.95, -119.9996020418, 59.999601517)
                Line((-0.4749942856, -0.8227274328), (0, -1.0969655115))
                Line((0, -1.0969655115), (0.4749999925, -0.8227241379))
            make_face()
            # Profile area: 0.048510723, perimeter: 2.0917960632
            with BuildLine():
                Line((-0.4750030839, 0.8227223531), (-0.95, 0.5484827557))
                Line((-0.95, 0.5484827557), (-0.95, 0))
                CenterArc((0, 0), 0.95, 120.0002147642, 59.9997852358)
            make_face()
            # Profile area: 0.048510723, perimeter: 2.0918103273
            with BuildLine():
                Line((0.4750000088, 0.8227241285), (0, 1.0969655115))
                Line((0, 1.0969655115), (-0.4750030839, 0.8227223531))
                CenterArc((0, 0), 0.95, 59.9999993854, 60.0002153787)
            make_face()
            # Profile area: 0.048510723, perimeter: 2.0918031853
            with BuildLine():
                Line((0.95, -0.0000000103), (0.95, 0.5484827557))
                Line((0.95, 0.5484827557), (0.4750000088, 0.8227241285))
                CenterArc((0, 0), 0.95, -0.0000006193, 60.0000000047)
            make_face()
            # Profile area: 0.048510723, perimeter: 2.0918163819
            with BuildLine():
                CenterArc((0, 0), 0.95, -180, 60.0003979582)
                Line((-0.95, 0), (-0.95, -0.5484827557))
                Line((-0.95, -0.5484827557), (-0.4749942856, -0.8227274328))
            make_face()
            # Profile area: 0.048510723, perimeter: 2.091803182
            with BuildLine():
                Line((0.4749999925, -0.8227241379), (0.95, -0.5484827557))
                Line((0.95, -0.5484827557), (0.95, -0.0000000103))
                CenterArc((0, 0), 0.95, -60.0000005247, 59.9999999055)
            make_face()
            # Profile area: 2.8352873699, perimeter: 5.9690260418
            with BuildLine():
                CenterArc((0, 0), 0.95, -60.0000005247, 59.9999999055)
                CenterArc((0, 0), 0.95, -0.0000006193, 60.0000000047)
                CenterArc((0, 0), 0.95, 59.9999993854, 60.0002153787)
                CenterArc((0, 0), 0.95, 120.0002147642, 59.9997852358)
                CenterArc((0, 0), 0.95, -180, 60.0003979582)
                CenterArc((0, 0), 0.95, -119.9996020418, 59.999601517)
            make_face()
        # OneSide extrude, distance=0.75
        extrude(amount=0.75)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.75, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.1309733553, perimeter: 3.7699111843
            Circle(0.6)
        # OneSide extrude, distance=5
        extrude(amount=5, mode=Mode.ADD)

        # Sketch4 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-0.475, 0, 0.8227241336), x_dir=(0.8660254038, 0, 0.5), z_dir=(-0.5, 0, 0.8660254038))):
            # Profile area: 0.0157079633, perimeter: 0.5141592654
            with BuildLine():
                Line((0, 0.475), (0, 0.275))
                CenterArc((0, 0.375), 0.1, -90, 180)
            make_face()
            # Profile area: 0.0157079633, perimeter: 0.5141592654
            with BuildLine():
                CenterArc((0, 0.375), 0.1, 90, 180)
                Line((0, 0.475), (0, 0.275))
            make_face()
        # OneSide extrude, distance=-2
        extrude(amount=-2, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-0.95, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.0157079633, perimeter: 0.5141592654
            with BuildLine():
                Line((0, 0.475), (0, 0.275))
                CenterArc((0, 0.375), 0.1, -90, 180)
            make_face()
            # Profile area: 0.0157079633, perimeter: 0.5141592654
            with BuildLine():
                CenterArc((0, 0.375), 0.1, 90, 180)
                Line((0, 0.475), (0, 0.275))
            make_face()
        # OneSide extrude, distance=-2
        extrude(amount=-2, mode=Mode.SUBTRACT)
    return part.part


def model_43562_004c6cea_0010():
    """Model: tube frame v1 v2 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 8 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 33.2122214294, perimeter: 37.7520048512
            with BuildLine():
                CenterArc((10, 0), 1.5, -170.4059317731, 160.8118635463)
                Line((8.5209800542, -0.25), (0, -0.25))
                Line((0, -2.5), (0, -0.25))
                Line((16, -2.5), (0, -2.5))
                Line((16, -0.25), (16, -2.5))
                Line((11.4790199458, -0.25), (16, -0.25))
            make_face()
        # OneSide extrude, distance=4
        extrude(amount=4)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -0.25, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((-7.5, 2)):
                Circle(0.5)
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((-12.5, 2)):
                Circle(0.5)
        # OneSide extrude, distance=-1.5
        extrude(amount=-1.5, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -0.25, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 5, perimeter: 9
            with BuildLine():
                Line((-16, 1), (-13.5, 1))
                Line((-13.5, 1), (-13.5, 3))
                Line((-13.5, 3), (-16, 3))
                Line((-16, 1), (-16, 3))
            make_face()
        # OneSide extrude, distance=-2.25
        extrude(amount=-2.25, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 4), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.8659014751, perimeter: 3.2986722863
            with Locations((14.875, -1.375)):
                Circle(0.525)
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((-14.875, -1.375)):
                Circle(0.5)
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.SUBTRACT)
    return part.part


def model_43628_a95b7e66_0028():
    """Model: Brush case v10"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.0106192983, perimeter: 5.0265482457
            Circle(0.8)
        # OneSide extrude, distance=0.4
        extrude(amount=0.4)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.4, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.5393804003, perimeter: 4.398229715
            Circle(0.7)
        # OneSide extrude, distance=1.6
        extrude(amount=1.6, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 1.5393804003, perimeter: 4.398229715
            Circle(0.7)
        # OneSide extrude, distance=-0.1
        extrude(amount=-0.1, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.1, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            Circle(0.5)
        # OneSide extrude, distance=-3.3
        extrude(amount=-3.3, mode=Mode.SUBTRACT)
    return part.part


def model_43628_a95b7e66_0032():
    """Model: brush case cover v5 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.5393804003, perimeter: 4.398229715
            Circle(0.7)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            Circle(0.5)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.7, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            Circle(0.3)
        # OneSide extrude, distance=-0.1
        extrude(amount=-0.1, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.6, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            Circle(0.2)
        # OneSide extrude, distance=0.05
        extrude(amount=0.05, mode=Mode.ADD)

        # Sketch6 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 7 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.1398551899, perimeter: 1.9402715546
            with BuildLine():
                Line((0.0880706261, -0.3969972625), (0.0880706261, 0.3969972625))
                Line((0.0880706261, 0.3969972625), (-0.0880706261, 0.3969972625))
                Line((-0.0880706261, 0.3969972625), (-0.0880706261, -0.3969972625))
                Line((-0.0880706261, -0.3969972625), (0.0880706261, -0.3969972625))
            make_face()
        # OneSide extrude, distance=-0.1
        extrude(amount=-0.1, mode=Mode.SUBTRACT)
    return part.part


def model_43757_d0d2a59a_0000():
    """Model: CLIP v4"""
    with BuildPart() as part:
        # Sketch2 -> 擠出1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 6 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 2.3771085359, perimeter: 16.3867223308
            with BuildLine():
                Line((1.5, -0.25), (1.5, -0.55))
                CenterArc((1.35, -0.25), 0.15, 0, 180)
                Line((1.2, -0.25), (-1.1877501001, -0.25))
                CenterArc((-1.5, 0), 0.4, 38.6821874535, 282.635625093)
                Line((-1.1877501001, 0.25), (1.5, 0.25))
                Line((1.5, 0.55), (1.5, 0.25))
                Line((-1.0669872981, 0.55), (1.5, 0.55))
                CenterArc((-1.5, 0), 0.7, 51.7867892983, 256.4264214035)
                Line((1.5, -0.55), (-1.0669872981, -0.55))
            make_face()
        # Symmetric extrude, each_side=0.5
        extrude(amount=0.5, both=True)

        # Sketch3 -> 擠出2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.25, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 2.1849811761, perimeter: 7.9680385636
            with BuildLine():
                Line((1.5, 0.5), (0.6339745962, 0.5))
                Line((1.5, -0.5), (1.5, 0.5))
                Line((0.6339745962, -0.5), (1.5, -0.5))
                CenterArc((1.5, 0), 1, -150, 300)
            make_face()
        # OneSide extrude, distance=-0.3
        extrude(amount=-0.3, mode=Mode.ADD)

        # Sketch4 -> 擠出3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.55, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.5446900494, perimeter: 5.6548667765
            with Locations((-1.5, 0)):
                Circle(0.9)
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2, mode=Mode.SUBTRACT)

        # Sketch5 -> 擠出4 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.35, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.1309733553, perimeter: 3.7699111843
            with Locations((-1.5, 0)):
                Circle(0.6)
        # OneSide extrude, distance=-0.1
        extrude(amount=-0.1, mode=Mode.SUBTRACT)
    return part.part


def model_43759_ba3249d8_0000():
    """Model: CLIP v2"""
    with BuildPart() as part:
        # Sketch1 -> 擠出1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 6 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 2.3574735818, perimeter: 16.3296426981
            with BuildLine():
                Line((1.5, -0.25), (1.5, -0.55))
                CenterArc((1.4, -0.25), 0.1, 0, 180)
                Line((1.3, -0.25), (-1.1877501001, -0.25))
                CenterArc((-1.5, 0), 0.4, 38.6821874535, 282.635625093)
                Line((-1.1877501001, 0.25), (1.5, 0.25))
                Line((1.5, 0.55), (1.5, 0.25))
                Line((-1.0669872981, 0.55), (1.5, 0.55))
                CenterArc((-1.5, 0), 0.7, 51.7867892983, 256.4264214035)
                Line((1.5, -0.55), (-1.0669872981, -0.55))
            make_face()
        # Symmetric extrude, each_side=0.5
        extrude(amount=0.5, both=True)

        # Sketch5 -> 擠出2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.25, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 2.1849811761, perimeter: 7.9680385636
            with BuildLine():
                Line((1.5, 0.5), (0.6339745962, 0.5))
                Line((1.5, -0.5), (1.5, 0.5))
                Line((0.6339745962, -0.5), (1.5, -0.5))
                CenterArc((1.5, 0), 1, -150, 300)
            make_face()
        # OneSide extrude, distance=-0.3
        extrude(amount=-0.3, mode=Mode.ADD)

        # Sketch6 -> 擠出3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.55, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.5446900494, perimeter: 5.6548667765
            with Locations((-1.5, 0)):
                Circle(0.9)
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2, mode=Mode.SUBTRACT)

        # Sketch7 -> 擠出4 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.35, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.1309733553, perimeter: 3.7699111843
            with Locations((-1.5, 0)):
                Circle(0.6)
        # OneSide extrude, distance=-0.1
        extrude(amount=-0.1, mode=Mode.SUBTRACT)
    return part.part


def model_43866_908e0b9a_0017():
    """Model: ramie obceg"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 29 constraints, 18 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 4.4255070553, perimeter: 17.4090026718
            with BuildLine():
                Line((3.0010654009, -1.2999167599), (5.1224544108, -0.8706578245))
                CenterArc((5.1026215578, -0.7726442645), 0.1, -78.5607669807, 55.1810588337)
                Line((5.3294355391, -0.5), (5.19441108, -0.8123265479))
                Line((5.1294355391, -0.5), (5.3294355391, -0.5))
                Line((4.0613078648, -0.6311495875), (5.1294355391, -0.5))
                CenterArc((3.584205444, 0.2441651451), 0.9968964846, -108.7188942869, 47.3120989676)
                Line((2.6522779818, -0.7), (3.2642761084, -0.7))
                CenterArc((2.6522779818, -0.625), 0.075, 172.634114171, 97.365885829)
                CenterArc((1.6853240015, -0.5), 0.9, -7.365885829, 97.365885829)
                Line((0, 0.4), (1.6853240015, 0.4))
                CenterArc((0, 0), 0.4, 90, 176.625819759)
                CenterArc((-0.0250140214, -0.4242632423), 0.025, 0, 86.625819759)
                Line((-0.0000140214, -0.4242632423), (-0.0000140214, -0.5265855842))
                CenterArc((0.0199859786, -0.5265855842), 0.02, -180, 99.489458269)
                Line((0.0232833014, -0.5463119033), (0.7638409108, -0.4225251257))
                CenterArc((0.7671382336, -0.4422514447), 0.02, -3.5988316853, 103.0882899543)
                CenterArc((1.6853240015, -0.5), 0.9, 176.4011683147, 98.0675153181)
                Line((1.7554467772, -1.3972640616), (3.0010654009, -1.2999167599))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1.6853240015, -0.5), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=0.3
        extrude(amount=0.3, both=True)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 8 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.3), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.3200678127, perimeter: 4.3853828413
            with BuildLine():
                Line((1.6853240015, 0.4), (1.3370033387, 0.4))
                CenterArc((1.6853240015, -0.5), 0.9, -7.365885829, 97.365885829)
                CenterArc((2.6522779818, -0.625), 0.075, 172.634114171, 97.365885829)
                Line((2.6522779818, -0.7), (2.6522779818, -0.5))
                CenterArc((1.4097535364, -0.5), 1.2425244454, 0, 81.1111754136)
                Line((1.3370033387, 0.4), (1.601745536, 0.7276017552))
            make_face()
            # Profile area: 0.9207914311, perimeter: 4.9460824052
            with BuildLine():
                CenterArc((1.3299128762, -0.9831980585), 0.8638796198, 141.057558731, 190.0951451436)
                Line((2.1112763621, -1.3694553493), (2.0865925568, -1.4))
                Line((1.7554467772, -1.3972640616), (2.1112763621, -1.3694553493))
                CenterArc((1.6853240015, -0.5), 0.9, 176.4011683147, 98.0675153181)
                CenterArc((0.7671382336, -0.4422514447), 0.02, -3.5988316853, 103.0882899543)
                Line((0.7638409108, -0.4225251257), (0.6580065053, -0.4402157143))
            make_face()
            # Profile area: 2.0536175392, perimeter: 8.5001146958
            with BuildLine():
                Line((0.7638409108, -0.4225251257), (0.6580065053, -0.4402157143))
                CenterArc((0.7671382336, -0.4422514447), 0.02, -3.5988316853, 103.0882899543)
                CenterArc((1.6853240015, -0.5), 0.9, 176.4011683147, 98.0675153181)
                Line((1.7554467772, -1.3972640616), (2.1112763621, -1.3694553493))
                Line((2.6522779818, -0.7), (2.1112763621, -1.3694553493))
                CenterArc((2.6522779818, -0.625), 0.075, 172.634114171, 97.365885829)
                CenterArc((1.6853240015, -0.5), 0.9, -7.365885829, 97.365885829)
                Line((1.6853240015, 0.4), (1.3370033387, 0.4))
                Line((0.6580065053, -0.4402157143), (1.3370033387, 0.4))
            make_face()
            with BuildLine():
                CenterArc((1.6853240015, -0.5), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.3
        extrude(amount=-0.3, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 9 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -0.7, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.18, perimeter: 1.8
            with BuildLine():
                Line((-3.2582770451, 0.15), (-3.2582770451, -0.15))
                Line((-3.2582770451, -0.15), (-2.6582770451, -0.15))
                Line((-2.6582770451, -0.15), (-2.6582770451, 0.15))
                Line((-2.6582770451, 0.15), (-3.2582770451, 0.15))
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)

        # Sketch8 -> Extrude9 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.0894686942, -0.5352487849, 0), x_dir=(0, 0, -1), z_dir=(0.1648661384, -0.9863159516, 0))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((0, 0.2500000037)):
                Circle(0.2)
        # OneSide extrude, distance=-0.25
        extrude(amount=-0.25, mode=Mode.SUBTRACT)
    return part.part


def model_43928_6ca53538_0000():
    """Model: line guide drive shaft v4"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0637939658, perimeter: 0.8953539063
            Circle(0.1425)
        # OneSide extrude, distance=0.54
        extrude(amount=0.54)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.54), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.1325555809, perimeter: 2.4661502565
            with BuildLine():
                CenterArc((0, 0), 0.2500000037, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.1425, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0637939658, perimeter: 0.8953539063
            Circle(0.1425)
        # OneSide extrude, distance=3
        extrude(amount=3, mode=Mode.ADD)

        # Sketch20 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 3.54), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            Circle(0.15)
        # OneSide extrude, distance=0.66
        extrude(amount=0.66, mode=Mode.ADD)

        # Sketch22 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 4.2), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0490873852, perimeter: 0.7853981634
            Circle(0.125)
        # OneSide extrude, distance=0.05
        extrude(amount=0.05, mode=Mode.ADD)

        # Sketch23 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 9 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 4.25), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.082123144, perimeter: 1.0707795693
            with BuildLine():
                CenterArc((0, 0), 0.18, -133.9829631304, 87.9659262607)
                Line((0.125, -0.1295183385), (0.125, 0.1295183385))
                CenterArc((0, 0), 0.18, 46.0170368696, 87.9659262607)
                Line((-0.125, 0.1295183385), (-0.125, -0.1295183385))
            make_face()
        # OneSide extrude, distance=0.17
        extrude(amount=0.17, mode=Mode.ADD)
    return part.part


MODELS = {
    "model_40603_f38d1b3d_0000": {"func": model_40603_f38d1b3d_0000, "volume": 181.2982632239, "area": 650.888720678},
    "model_40997_e3c88650_0001": {"func": model_40997_e3c88650_0001, "volume": 226.4813169425, "area": 560.9756999632},
    "model_40999_cad6be09_0018": {"func": model_40999_cad6be09_0018, "volume": 4183.0087706587, "area": 5920.737046619},
    "model_40999_cad6be09_0019": {"func": model_40999_cad6be09_0019, "volume": 1339.6424417612, "area": 1029.0301775692},
    "model_41117_1b3271f2_0000": {"func": model_41117_1b3271f2_0000, "volume": 1.1141839256, "area": 13.4395278176},
    "model_41117_1b3271f2_0007": {"func": model_41117_1b3271f2_0007, "volume": 0.8791822957, "area": 8.7497431881},
    "model_41227_90e1c07c_0006": {"func": model_41227_90e1c07c_0006, "volume": 2435.505051374, "area": 1495.082417499},
    "model_41229_16283ae1_0002": {"func": model_41229_16283ae1_0002, "volume": 1.3777317936, "area": 11.6144428268},
    "model_41229_16283ae1_0003": {"func": model_41229_16283ae1_0003, "volume": 0.4919999837, "area": 12.2400000888},
    "model_41229_16283ae1_0012": {"func": model_41229_16283ae1_0012, "volume": 5.1147789331, "area": 27.8244523255},
    "model_41229_16283ae1_0015": {"func": model_41229_16283ae1_0015, "volume": 0.2173311933, "area": 5.2936497079},
    "model_41353_16ac5969_0000": {"func": model_41353_16ac5969_0000, "volume": 32.8082774821, "area": 671.1726636389},
    "model_41495_a639572a_0000": {"func": model_41495_a639572a_0000, "volume": 290.46647907, "area": 544.7316005043},
    "model_41624_a15f83c1_0017": {"func": model_41624_a15f83c1_0017, "volume": 12.72385052, "area": 31.1139582389},
    "model_41624_a15f83c1_0019": {"func": model_41624_a15f83c1_0019, "volume": 2.3419999804, "area": 32.2599999085},
    "model_41624_a15f83c1_0020": {"func": model_41624_a15f83c1_0020, "volume": 0.7605591202, "area": 7.7942936218},
    "model_41647_00943ed3_0000": {"func": model_41647_00943ed3_0000, "volume": 85.7999672973, "area": 202.1778775029},
    "model_41648_577daf16_0000": {"func": model_41648_577daf16_0000, "volume": 21.8073645486, "area": 245.5365523667},
    "model_41648_577daf16_0008": {"func": model_41648_577daf16_0008, "volume": 10.007278992, "area": 48.056890501},
    "model_41650_9417da80_0004": {"func": model_41650_9417da80_0004, "volume": 0.0798962919, "area": 2.0737775973},
    "model_41650_9417da80_0005": {"func": model_41650_9417da80_0005, "volume": 0.5976438055, "area": 13.4471238898},
    "model_41672_f0bd39e4_0000": {"func": model_41672_f0bd39e4_0000, "volume": 0.2915007855, "area": 7.357602909},
    "model_41717_5bfe31cb_0000": {"func": model_41717_5bfe31cb_0000, "volume": 100.0128556684, "area": 1020.8353323066},
    "model_41757_c1173a7e_0005": {"func": model_41757_c1173a7e_0005, "volume": 294.1394806976, "area": 849.1089499319},
    "model_41757_c1173a7e_0025": {"func": model_41757_c1173a7e_0025, "volume": 35.7743301257, "area": 129.4525361087},
    "model_41759_f26a9c8c_0000": {"func": model_41759_f26a9c8c_0000, "volume": 0.0873658678, "area": 1.3032353538},
    "model_41762_1092e172_0000": {"func": model_41762_1092e172_0000, "volume": 46.1748622526, "area": 474.4113272302},
    "model_41780_da6cd1db_0015": {"func": model_41780_da6cd1db_0015, "volume": 0.8639380002, "area": 9.503317859},
    "model_41845_a5180a74_0000": {"func": model_41845_a5180a74_0000, "volume": 0.006180932, "area": 0.4180365055},
    "model_41859_173a686e_0000": {"func": model_41859_173a686e_0000, "volume": 0.2963566999, "area": 4.0293272957},
    "model_41859_173a686e_0001": {"func": model_41859_173a686e_0001, "volume": 0.059179263, "area": 1.630330112},
    "model_41859_173a686e_0006": {"func": model_41859_173a686e_0006, "volume": 0.2168190868, "area": 3.7418450319},
    "model_41859_173a686e_0008": {"func": model_41859_173a686e_0008, "volume": 0.3663222646, "area": 5.4816083594},
    "model_41896_7d8659e6_0004": {"func": model_41896_7d8659e6_0004, "volume": 0.3551963194, "area": 5.0461831998},
    "model_41896_7d8659e6_0011": {"func": model_41896_7d8659e6_0011, "volume": 1.3257521125, "area": 10.3247694832},
    "model_41896_7d8659e6_0014": {"func": model_41896_7d8659e6_0014, "volume": 3.2609794048, "area": 22.5460453762},
    "model_41896_7d8659e6_0015": {"func": model_41896_7d8659e6_0015, "volume": 2.1678832305, "area": 20.2912388217},
    "model_41907_7bcecdb1_0004": {"func": model_41907_7bcecdb1_0004, "volume": 0.0050807454, "area": 0.2798444284},
    "model_41920_98cdf3b2_0000": {"func": model_41920_98cdf3b2_0000, "volume": 10469.9200972253, "area": 4957.0439520226},
    "model_42230_4b89c7e8_0000": {"func": model_42230_4b89c7e8_0000, "volume": 356.4458263129, "area": 808.0115066774},
    "model_42230_f5bce306_0000": {"func": model_42230_f5bce306_0000, "volume": 1816392.5069196699, "area": 192772.1071429274},
    "model_42329_df7f540f_0056": {"func": model_42329_df7f540f_0056, "volume": 0.0082561055, "area": 0.2676636941},
    "model_42329_df7f540f_0061": {"func": model_42329_df7f540f_0061, "volume": 0.0850004042, "area": 1.8947102695},
    "model_42329_df7f540f_0067": {"func": model_42329_df7f540f_0067, "volume": 0.0122773441, "area": 0.368194659},
    "model_42329_df7f540f_0068": {"func": model_42329_df7f540f_0068, "volume": 0.0162985827, "area": 0.4687256239},
    "model_42429_b48647fb_0000": {"func": model_42429_b48647fb_0000, "volume": 5.0159130917, "area": 32.3573979907},
    "model_42568_09cf35f8_0000": {"func": model_42568_09cf35f8_0000, "volume": 64087.1850138662, "area": 12146.7818458658},
    "model_42586_517832f9_0015": {"func": model_42586_517832f9_0015, "volume": 3.9181686065, "area": 39.0898684767},
    "model_42601_bfe96b47_0005": {"func": model_42601_bfe96b47_0005, "volume": 340.3779180345, "area": 2289.476854119},
    "model_42601_bfe96b47_0006": {"func": model_42601_bfe96b47_0006, "volume": 6287.9154463783, "area": 21034.0342929088},
    "model_43529_4804941b_0002": {"func": model_43529_4804941b_0002, "volume": 0.2110286325, "area": 2.6442785365},
    "model_43529_4804941b_0042": {"func": model_43529_4804941b_0042, "volume": 1.9568130095, "area": 12.9203295724},
    "model_43529_4804941b_0051": {"func": model_43529_4804941b_0051, "volume": 7.8864084392, "area": 32.1157987629},
    "model_43562_004c6cea_0010": {"func": model_43562_004c6cea_0010, "volume": 117.5913915889, "area": 231.244905887},
    "model_43628_a95b7e66_0028": {"func": model_43628_a95b7e66_0028, "volume": 1.6210618093, "area": 17.9070781255},
    "model_43628_a95b7e66_0032": {"func": model_43628_a95b7e66_0032, "volume": 0.6645984942, "area": 5.9745576381},
    "model_43757_d0d2a59a_0000": {"func": model_43757_d0d2a59a_0000, "volume": 2.4105675433, "area": 25.5081006025},
    "model_43759_ba3249d8_0000": {"func": model_43759_ba3249d8_0000, "volume": 2.3909325893, "area": 25.4117510616},
    "model_43866_908e0b9a_0017": {"func": model_43866_908e0b9a_0017, "volume": 2.0438030449, "area": 18.5851439622},
    "model_43928_6ca53538_0000": {"func": model_43928_6ca53538_0000, "volume": 0.6865653363, "area": 6.4979885513},
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
