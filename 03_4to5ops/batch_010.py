"""Batch 010 - passing/03_4to5ops
98 models bundled from Fusion360 Gallery reconstructions.
"""

from build123d import *


# Description: This is a cylindrical sleeve or spacer with a hollow bore through its center, featuring a slightly tapered or stepped design at one end, commonly used as a connector, adapter, or positioning component in mechanical assemblies.
def model_40705_5ff43505_0032():
    """Model: Fast2mmc (4) (2)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0176714587, perimeter: 1.4137166941
            with BuildLine():
                CenterArc((0, 0), 0.125, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            Circle(0.1)
        # OneSide extrude, distance=0.15
        extrude(amount=0.15)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            Circle(0.1)
        # OneSide extrude, distance=-0.8
        extrude(amount=-0.8, mode=Mode.ADD)

        # Sketch2 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 12 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.15), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.001225, perimeter: 0.14
            with BuildLine():
                Line((0.0175, 0.0175), (-0.0175, 0.0175))
                Line((-0.0175, 0.0175), (-0.0175, -0.0175))
                Line((-0.0175, -0.0175), (0.0175, -0.0175))
                Line((0.0175, -0.0175), (0.0175, 0.0175))
            make_face()
            # Profile area: 0.0023185563, perimeter: 0.1949778683
            with BuildLine():
                CenterArc((0, 0.0699999984), 0.0175, 0, 180)
                Line((-0.0175, 0.0699999984), (-0.0175, 0.0175))
                Line((0.0175, 0.0175), (-0.0175, 0.0175))
                Line((0.0175, 0.0175), (0.0175, 0.0699999984))
            make_face()
            # Profile area: 0.0023185563, perimeter: 0.1949778665
            with BuildLine():
                Line((-0.0175, -0.0175), (0.0175, -0.0175))
                Line((-0.0175, -0.0175), (-0.0175, -0.0699999976))
                CenterArc((0, -0.0699999976), 0.0175, 180, 180)
                Line((0.0175, -0.0699999976), (0.0175, -0.0175))
            make_face()
            # Profile area: 0.002262442, perimeter: 0.1917713329
            with BuildLine():
                Line((-0.0175, 0.0175), (-0.0175, -0.0175))
                Line((-0.0175, 0.0175), (-0.0683967308, 0.0175))
                CenterArc((-0.0683967308, 0), 0.0175, 90, 180)
                Line((-0.0683967308, -0.0175), (-0.0175, -0.0175))
            make_face()
            # Profile area: 0.0023185563, perimeter: 0.1949778683
            with BuildLine():
                Line((0.0175, -0.0175), (0.0175, 0.0175))
                Line((0.0175, -0.0175), (0.0699999984, -0.0175))
                CenterArc((0.0699999984, 0), 0.0175, -90, 180)
                Line((0.0699999984, 0.0175), (0.0175, 0.0175))
            make_face()
        # OneSide extrude, distance=-0.06
        extrude(amount=-0.06, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical dowel pin or shaft with a smooth, uniformly rounded body and hemispherical ends, featuring no holes, slots, or flanges.
def model_40705_5ff43505_0034():
    """Model: Fast3mm (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0255254403, perimeter: 2.0420352248
            with BuildLine():
                CenterArc((0, 0), 0.175, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            Circle(0.15)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            Circle(0.15)
        # OneSide extrude, distance=-1.9
        extrude(amount=-1.9, mode=Mode.ADD)

        # Sketch2 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 12 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.2), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0034283185, perimeter: 0.242831849
            with BuildLine():
                Line((-0.02, 0.02), (-0.02, -0.02))
                Line((-0.02, 0.02), (-0.089999998, 0.02))
                CenterArc((-0.089999998, 0), 0.02, 90, 180)
                Line((-0.089999998, -0.02), (-0.02, -0.02))
            make_face()
            # Profile area: 0.0034283185, perimeter: 0.242831849
            with BuildLine():
                Line((0.02, -0.02), (0.02, 0.02))
                Line((0.02, -0.02), (0.089999998, -0.02))
                CenterArc((0.089999998, 0), 0.02, -90, 180)
                Line((0.089999998, 0.02), (0.02, 0.02))
            make_face()
            # Profile area: 0.0034283185, perimeter: 0.242831849
            with BuildLine():
                CenterArc((0, 0.089999998), 0.02, 0, 180)
                Line((-0.02, 0.089999998), (-0.02, 0.02))
                Line((0.02, 0.02), (-0.02, 0.02))
                Line((0.02, 0.02), (0.02, 0.089999998))
            make_face()
            # Profile area: 0.0016, perimeter: 0.16
            with BuildLine():
                Line((0.02, 0.02), (-0.02, 0.02))
                Line((-0.02, 0.02), (-0.02, -0.02))
                Line((-0.02, -0.02), (0.02, -0.02))
                Line((0.02, -0.02), (0.02, 0.02))
            make_face()
            # Profile area: 0.0034283185, perimeter: 0.242831849
            with BuildLine():
                Line((-0.02, -0.02), (0.02, -0.02))
                Line((-0.02, -0.02), (-0.02, -0.089999998))
                CenterArc((0, -0.089999998), 0.02, 180, 180)
                Line((0.02, -0.089999998), (0.02, -0.02))
            make_face()
        # OneSide extrude, distance=-0.06
        extrude(amount=-0.06, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a stepped cylindrical shaft or pin featuring a larger diameter cylindrical body that transitions to a smaller diameter cylindrical head, with what appears to be a hemispherical or rounded end cap on the smaller section.
def model_40705_5ff43505_0036():
    """Model: Fast5mm (2)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.2454369261, perimeter: 3.926990817
            with BuildLine():
                CenterArc((0, 0), 0.375, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            Circle(0.25)
        # OneSide extrude, distance=0.25
        extrude(amount=0.25)

        # Sketch1 -> Extrude4 (Join)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            Circle(0.25)
        # OneSide extrude, distance=-1.2
        extrude(amount=-1.2, mode=Mode.ADD)

        # Sketch2 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 11 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.25), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0182182722, perimeter: 0.6197254547
            with BuildLine():
                Line((-0.0376012841, -0.0369388359), (0.037398454, -0.036740638))
                Line((-0.0376012841, -0.0369388359), (-0.0370371921, -0.2503959556))
                CenterArc((0.000462677, -0.2502968567), 0.0375, -179.8485877791, 180)
                Line((0.0379625461, -0.2501977577), (0.037398454, -0.036740638))
            make_face()
            # Profile area: 0.0181192085, perimeter: 0.6170837558
            with BuildLine():
                Line((0.0372002561, 0.0382591001), (-0.037799482, 0.0380609022))
                Line((0.0372002561, 0.0382591001), (0.0366396546, 0.250395375))
                CenterArc((-0.0008602144, 0.2502962761), 0.0375, 0.1514122209, 180)
                Line((-0.0383600835, 0.2501971771), (-0.037799482, 0.0380609022))
            make_face()
            # Profile area: 0.0181314595, perimeter: 0.6174104485
            with BuildLine():
                Line((-0.037799482, 0.0380609022), (-0.0376012841, -0.0369388359))
                Line((-0.037799482, 0.0380609022), (-0.2500991027, 0.0374998691))
                CenterArc((-0.2500000037, 0), 0.0375, 90.1514122209, 180)
                Line((-0.2499009048, -0.0374998691), (-0.0376012841, -0.0369388359))
            make_face()
            # Profile area: 0.005625, perimeter: 0.3
            with BuildLine():
                Line((0.037398454, -0.036740638), (0.0372002561, 0.0382591001))
                Line((0.0372002561, 0.0382591001), (-0.037799482, 0.0380609022))
                Line((-0.037799482, 0.0380609022), (-0.0376012841, -0.0369388359))
                Line((-0.0376012841, -0.0369388359), (0.037398454, -0.036740638))
            make_face()
            # Profile area: 0.0181612745, perimeter: 0.6182055156
            with BuildLine():
                CenterArc((0.2499965082, 0.0013213147), 0.0375, -89.8485877791, 179.9999991462)
                Line((0.2498974098, 0.0388211838), (0.0372002561, 0.0382591001))
                Line((0.037398454, -0.036740638), (0.0372002561, 0.0382591001))
                Line((0.037398454, -0.036740638), (0.2500956072, -0.0361785543))
            make_face()
        # OneSide extrude, distance=-0.1
        extrude(amount=-0.1, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical fastener or dowel pin with a larger diameter head on one end and a smaller diameter shaft, featuring a knurled or textured surface on the cylindrical body for improved grip.
def model_40705_5ff43505_0038():
    """Model: Fast3mmcover (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0883572934, perimeter: 2.3561944902
            with BuildLine():
                CenterArc((0, 0), 0.225, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            Circle(0.15)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            Circle(0.15)
        # OneSide extrude, distance=-0.8
        extrude(amount=-0.8, mode=Mode.ADD)

        # Sketch2 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 12 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.2), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0050283184, perimeter: 0.3228318473
            with BuildLine():
                Line((0.02, -0.02), (0.02, 0.02))
                Line((0.02, -0.02), (0.1299999971, -0.02))
                CenterArc((0.1299999971, 0), 0.02, -90, 180)
                Line((0.1299999971, 0.02), (0.02, 0.02))
            make_face()
            # Profile area: 0.0016, perimeter: 0.16
            with BuildLine():
                Line((0.02, 0.02), (-0.02, 0.02))
                Line((-0.02, 0.02), (-0.02, -0.02))
                Line((-0.02, -0.02), (0.02, -0.02))
                Line((0.02, -0.02), (0.02, 0.02))
            make_face()
            # Profile area: 0.0050283184, perimeter: 0.3228318473
            with BuildLine():
                CenterArc((0, 0.1299999971), 0.02, 0, 180)
                Line((-0.02, 0.1299999971), (-0.02, 0.02))
                Line((0.02, 0.02), (-0.02, 0.02))
                Line((0.02, 0.02), (0.02, 0.1299999971))
            make_face()
            # Profile area: 0.0050283184, perimeter: 0.3228318473
            with BuildLine():
                Line((-0.02, -0.02), (0.02, -0.02))
                Line((-0.02, -0.02), (-0.02, -0.1299999971))
                CenterArc((0, -0.1299999971), 0.02, 180, 180)
                Line((0.02, -0.1299999971), (0.02, -0.02))
            make_face()
            # Profile area: 0.0050283184, perimeter: 0.3228318473
            with BuildLine():
                Line((-0.02, 0.02), (-0.02, -0.02))
                Line((-0.02, 0.02), (-0.1299999971, 0.02))
                CenterArc((-0.1299999971, 0), 0.02, 90, 180)
                Line((-0.1299999971, -0.02), (-0.02, -0.02))
            make_face()
        # OneSide extrude, distance=-0.06
        extrude(amount=-0.06, mode=Mode.SUBTRACT)
    return part.part


# Description: A toilet plunger featuring a circular rubber cup head with a textured surface and a long cylindrical handle extending horizontally to the right.
def model_40705_5ff43505_0041():
    """Model: Arm_piston"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 77.4088429845, perimeter: 35.1858377202
            with BuildLine():
                CenterArc((0, 0), 5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.6, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 1.1309733553, perimeter: 3.7699111843
            Circle(0.6)
        # OneSide extrude, distance=29
        extrude(amount=29, mode=Mode.ADD)

        # Sketch2 -> Extrude3 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 4 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.3769911184, perimeter: 3.7699111843
            with BuildLine():
                CenterArc((29.4, 0), 0.4, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((29.4, 0), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=0.2
        extrude(amount=0.2, both=True)
    return part.part


# Description: This is a square or rectangular frame assembly with corner reinforcements and internal cross-bracing, featuring a hollow center cavity with diagonal support struts and mounting points at each corner.
def model_40705_5ff43505_0043():
    """Model: Pneumatic_bottom"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 120.1415926536, perimeter: 42.2831853072
            with BuildLine():
                CenterArc((-4.5, -4.5), 1, -180, 90)
                Line((-4.5, -5.5), (4.5, -5.5))
                CenterArc((4.5, -4.5), 1, -90, 90)
                Line((5.5, -4.5), (5.5, 4.5))
                CenterArc((4.5, 4.5), 1, 0, 90)
                Line((4.5, 5.5), (-4.5, 5.5))
                CenterArc((-4.5, 4.5), 1, 90, 90)
                Line((-5.5, 4.5), (-5.5, -4.5))
            make_face()
        # OneSide extrude, distance=-2
        extrude(amount=-2)

        # Sketch3 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-2, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((4.5, 4.5)):
                Circle(0.5)
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((-4.5, 4.5)):
                Circle(0.5)
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((4.5, -4.5)):
                Circle(0.5)
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((-4.5, -4.5)):
                Circle(0.5)
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a hammer or mallet featuring a cylindrical handle shaft connected to a large spherical or rounded head, with a smooth curved transition between the two components.
def model_40782_3383cd58_0006():
    """Model: M4x12 v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.6361725124, perimeter: 2.8274333882
            Circle(0.45)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            Circle(0.2)
        # OneSide extrude, distance=1.15
        extrude(amount=1.15, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical bolt or fastener with a hexagonal head at one end and a threaded shaft, featuring a tapered or slightly enlarged base section.
def model_40782_3383cd58_0008():
    """Model: Srubadociskajaca v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            Circle(0.4)
        # OneSide extrude, distance=0.7
        extrude(amount=0.7)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.7, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            Circle(0.25)
        # OneSide extrude, distance=5.7
        extrude(amount=5.7, mode=Mode.ADD)
    return part.part


# Description: This is a paddle or impeller component with a rounded, kidney-shaped body featuring a cylindrical shaft extending from one end and mesh-textured curved blades or fins protruding from the sides.
def model_40782_3383cd58_0016():
    """Model: Belka - pokretlo v4"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            Circle(1)
        # OneSide extrude, distance=0.4
        extrude(amount=0.4)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            Circle(0.25)
        # OneSide extrude, distance=1.2
        extrude(amount=1.2, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical container or sleeve with a curved, tapered body and an open top featuring a blue-highlighted rim or flange.
def model_40782_3383cd58_0017():
    """Model: Imadlo_pokretlo v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 7.0685834706, perimeter: 9.4247779608
            Circle(1.5)
        # OneSide extrude, distance=2
        extrude(amount=2)

        # Sketch4 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            Circle(0.5)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical rod or tube with a slightly tapered or beveled end, featuring a smooth, elongated shaft with rounded edges at both extremities.
def model_40782_3383cd58_0020():
    """Model: Imadlo_gwint v6"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            Circle(0.4)
        # OneSide extrude, distance=6
        extrude(amount=6)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 6, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            Circle(0.3)
        # OneSide extrude, distance=1.3
        extrude(amount=1.3, mode=Mode.ADD)
    return part.part


# Description: This is a rectangular mounting bracket or rail with a long, flat base featuring horizontal slot details and a perpendicular flange on the right end, designed for securing or guiding components in an assembly.
def model_40782_3383cd58_0022():
    """Model: Belka - podstawa v7"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 24.86, perimeter: 27
            with BuildLine():
                Line((-11.3, 2.2), (0, 2.2))
                Line((-11.3, 0), (-11.3, 2.2))
                Line((0, 0), (-11.3, 0))
                Line((0, 2.2), (0, 0))
            make_face()
        # OneSide extrude, distance=0.9
        extrude(amount=0.9)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 15 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.9, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1039682608, perimeter: 2.2232273402
            with BuildLine():
                CenterArc((1.65, -1.1), 1.1, -140.5994312463, 50.5994312463)
                Line((0.8, -2.2), (0.8, -1.7982120022))
                Line((0.8, -2.2), (1.65, -2.2))
            make_face()
            # Profile area: 0.1039682608, perimeter: 2.2232273402
            with BuildLine():
                CenterArc((1.65, -1.1), 1.1, 39.4005687537, 50.5994312463)
                Line((2.5, -0.4017879978), (2.5, 0))
                Line((2.5, 0), (1.65, 0))
            make_face()
            # Profile area: 0.1039682608, perimeter: 2.2232273402
            with BuildLine():
                Line((0.8, -0.4017879978), (0.8, 0))
                CenterArc((1.65, -1.1), 1.1, 90, 50.5994312463)
                Line((1.65, 0), (0.8, 0))
            make_face()
            # Profile area: 3.3241269569, perimeter: 6.6786053782
            with BuildLine():
                CenterArc((1.65, -1.1), 1.1, 90, 50.5994312463)
                Line((0.8, -1.7982120022), (0.8, -0.4017879978))
                CenterArc((1.65, -1.1), 1.1, -140.5994312463, 50.5994312463)
                CenterArc((1.65, -1.1), 1.1, -90, 50.5994312463)
                Line((2.5, -1.7982120022), (2.5, -0.4017879978))
                CenterArc((1.65, -1.1), 1.1, 39.4005687537, 50.5994312463)
            make_face()
            # Profile area: 0.238600077, perimeter: 2.9092972386
            with BuildLine():
                Line((2.5, -1.7982120022), (2.5, -0.4017879978))
                CenterArc((1.65, -1.1), 1.1, -39.4005687537, 78.8011375075)
            make_face()
            # Profile area: 0.238600077, perimeter: 2.9092972386
            with BuildLine():
                Line((0.8, -1.7982120022), (0.8, -0.4017879978))
                CenterArc((1.65, -1.1), 1.1, 140.5994312463, 78.8011375075)
            make_face()
            # Profile area: 0.1039682608, perimeter: 2.2232273402
            with BuildLine():
                Line((2.5, -2.2), (2.5, -1.7982120022))
                CenterArc((1.65, -1.1), 1.1, -90, 50.5994312463)
                Line((1.65, -2.2), (2.5, -2.2))
            make_face()
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a metal suppressor or silencer with a cylindrical body featuring a wider base section and a narrower extended tube, connected by a subtle shoulder transition, designed to attach to a firearm barrel.
def model_40782_3383cd58_0024():
    """Model: Pokretlo_baza v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.6361725124, perimeter: 2.8274333882
            Circle(0.45)
        # OneSide extrude, distance=2.5
        extrude(amount=2.5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            Circle(0.25)
        # OneSide extrude, distance=2.5
        extrude(amount=2.5, mode=Mode.ADD)
    return part.part


# Description: This is a shoe or footwear sole component featuring an asymmetrical curved design with a large circular opening/hole at the heel, a tapered toe section, textured grip surfaces on the bottom, and a complex 3D molded structure with integrated channels and ribbing for structural support and comfort.
def model_40782_3383cd58_0025():
    """Model: Uchyt v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 22.2940242872, perimeter: 32.0296388693
            with BuildLine():
                Line((5.100000079, 5.7), (0.0000000373, 5.7))
                Line((0.0000000373, 5.7), (0.0000000373, 1.6))
                CenterArc((2.7841054722, 4.2096428014), 3.8159505531, -136.8526057083, 137.1628635803)
                Line((5.100000079, 5.7), (6.600000079, 4.2303061543))
            make_face()
            with BuildLine():
                CenterArc((5.300000079, 3.6000000536), 0.81, 137.8712004034, 12.262807546)
                CenterArc((5.300000079, 3.6000000536), 0.81, -26.0370934022, 163.9082938057)
                CenterArc((3.0176001936, 4.9192844728), 3.4447552458, -96.7160815497, 67.6250289401)
                CenterArc((2.5000000373, 2.3000000343), 0.81, 87.8494154995, 190.2940119661)
                CenterArc((2.7412980193, 5.4588282367), 2.3588459031, -95.1296056572, 57.0303025512)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.42
        extrude(amount=0.42)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.42, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 6.8548469953, perimeter: 14.339387812
            with BuildLine():
                Line((-5.100000079, -5.7), (-0.0000000373, -5.7))
                Line((-0.0000000373, -5.7), (0, -4.5))
                Line((0, -4.5), (-6.3247449504, -4.5))
                Line((-6.3247449504, -4.5), (-5.100000079, -5.7))
            make_face()
        # OneSide extrude, distance=0.9
        extrude(amount=0.9, mode=Mode.ADD)
    return part.part


# Description: This is a rectangular channel or U-shaped bracket with two vertical flanges on either end, a recessed central cavity, and angled top surfaces, designed for structural support or assembly mounting applications.
def model_40782_3383cd58_0028():
    """Model: Imadlo - stojace v21"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 14 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 15.6275, perimeter: 28.4
            with BuildLine():
                Line((3.25, 0.9), (5.45, 0.9))
                Line((5.45, 0.9), (5.45, 0))
                Line((8.55, 0), (5.45, 0))
                Line((8.55, 2.8), (8.55, 0))
                Line((7.25, 2.8), (8.55, 2.8))
                Line((7.25, 1.55), (7.25, 2.8))
                Line((1.4, 1.55), (7.25, 1.55))
                Line((1.4, 3.5), (1.4, 1.55))
                Line((0, 3.5), (1.4, 3.5))
                Line((0, 0), (0, 3.5))
                Line((3.25, 0), (0, 0))
                Line((3.25, 0), (3.25, 0.9))
            make_face()
        # OneSide extrude, distance=5.1
        extrude(amount=5.1)
    return part.part


# Description: This is a dark gray support bracket or clamp with a curved, elongated body featuring two rounded flanges on the ends and a central slot or channel running along its length.
def model_40815_80519d37_0001():
    """Model: Untitled"""
    with BuildPart() as part:
        # CAD_Outline -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 20 constraints, 15 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.9332299464, perimeter: 8.2432299503
            with BuildLine():
                CenterArc((-5.1414845805, -8.8060161501), 8.3, 37.1263772958, 2.9505128129)
                CenterArc((2.2, -3.6), 1, 172.088186286, 43.2531471191)
                CenterArc((2.2, -3.6), 1, -144.6586665949, 175.1828343848)
                CenterArc((2.2, -3.6), 1, 30.5241677899, 43.2531471191)
                CenterArc((9.9527350028, 0.971115835), 8.3, -154.2113889137, 2.9505128129)
                CenterArc((2.2, -3.6), 0.75, -164.8236789951, 215.5128591852)
            make_face()
            # Profile area: 0.4412168396, perimeter: 4.4620169558
            with BuildLine():
                CenterArc((2.2, -3.6), 0.75, 50.6891801901, 144.4871408148)
                CenterArc((9.9527350028, 0.971115835), 8.3, -154.2113889137, 2.9505128129)
                CenterArc((2.2, -3.6), 1, 73.7773149089, 98.3108713771)
                CenterArc((-5.1414845805, -8.8060161501), 8.3, 37.1263772958, 2.9505128129)
            make_face()
            # Profile area: 0.0786142938, perimeter: 2.3009733329
            with BuildLine():
                CenterArc((-5.1414845805, -8.8060161501), 8.3, 55.7763154358, 7.8894372519)
                CenterArc((0, 0), 2, -136.8673988267, 33.176865777)
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
            # Profile area: 1.493290072, perimeter: 12.2934528462
            with BuildLine():
                CenterArc((-7, 0), 1, 32.9727058829, 43.2531471191)
                CenterArc((-4.8571428571, 8.741176309), 8.3, -99.0385902945, 31.468270623)
                CenterArc((0, 0), 2, 119.059281068, 28.6278729553)
                CenterArc((-4.8571428571, 8.741176309), 8, -103.774146998, 42.8334280661)
            make_face()
            # Profile area: 0.7302006993, perimeter: 7.2061903612
            with BuildLine():
                CenterArc((9.9527350028, 0.971115835), 8, -174.4271333029, 24.9513010927)
                CenterArc((0, 0), 2, -23.0550062582, 28.6278729553)
                CenterArc((9.9527350028, 0.971115835), 8.3, -167.7975325634, 13.5861436497)
                CenterArc((2.2, -3.6), 1, 30.5241677899, 43.2531471191)
            make_face()
        # OneSide extrude, distance=1.2
        extrude(amount=1.2, mode=Mode.ADD)

        # CAD_Outline -> Extrude3 (Join)
        # Sketch on XZ construction plane
        # Sketch has 20 constraints, 15 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 5.253305697, perimeter: 13.2307024835
            with BuildLine():
                CenterArc((0, 0), 2, 147.6871540234, 75.4454471499)
                CenterArc((-4.8571428571, 8.741176309), 8.3, -99.0385902945, 31.468270623)
                CenterArc((-7, 0), 1, -34.8294308247, 67.8021367076)
                CenterArc((-5.1414845805, -8.8060161501), 8.3, 63.6657526877, 33.5161126649)
            make_face()
            # Profile area: 2.7765310134, perimeter: 8.7729349655
            with BuildLine():
                CenterArc((2.2, -3.6), 1, 73.7773149089, 98.3108713771)
                CenterArc((9.9527350028, 0.971115835), 8.3, -167.7975325634, 13.5861436497)
                CenterArc((0, 0), 2, -103.6905330497, 80.6355267915)
                CenterArc((-5.1414845805, -8.8060161501), 8.3, 40.0768901086, 15.6994253272)
            make_face()
        # OneSide extrude, distance=0.3
        extrude(amount=0.3, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical sleeve or bushing with a hollow center bore and a mesh or perforated pattern covering portions of its outer surface, featuring an open-ended tubular design.
def model_40939_0bedb1ea_0000():
    """Model: flashlight"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 2), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0148440253, perimeter: 1.9792033718
            with BuildLine():
                CenterArc((0, 0.5000000075), 0.165, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0.5000000075), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 0, 2), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((0, 0.5000000075)):
                Circle(0.15)
        # OneSide extrude, distance=0.14
        extrude(amount=0.14, mode=Mode.ADD)
    return part.part


# Description: This is a hexagonal or polygonal container/box with a curved dome or rounded top lid, featuring mesh or perforated panels on the upper surfaces and solid walls on the lower sections, likely designed as a ventilated enclosure or strainer with a hinged or removable top.
def model_40997_e3c88650_0000():
    """Model: Untitled v2"""
    with BuildPart() as part:
        # Sketch3 -> Extrude3 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 17.4977871438, perimeter: 19.4247779608
            with BuildLine():
                CenterArc((10, 2.5), 2, 0, 180)
                Line((8, 2.5), (8, -0.5))
                Line((8, -0.5), (12, -0.5))
                Line((12, -0.5), (12, 2.5))
            make_face()
            with BuildLine():
                CenterArc((10, 2.5), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=2.5
        extrude(amount=2.5)
    return part.part


# Description: This is a dual-chamber or twin-tube rocket or thruster assembly with a rectangular prismatic body featuring two cylindrical nozzles or exhaust ports extending from the top, characterized by a dark metallic finish with visible internal structural details.
def model_40997_e3c88650_0003():
    """Model: Component 7.1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 8 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 37.4977871438, perimeter: 29.4247779608
            with BuildLine():
                CenterArc((0, 4.5), 2, 0, 180)
                Line((-2, -3.5), (-2, 4.5))
                Line((-2, -3.5), (2, -3.5))
                Line((2, 4.5), (2, -3.5))
            make_face()
            with BuildLine():
                CenterArc((0, 4.5), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=3.5
        extrude(amount=3.5)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on YZ construction plane
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 12.5000001863, perimeter: 15.000000149
            with BuildLine():
                Line((1.5000000224, 3.0000000075), (6.5000000969, 3.0000000075))
                Line((1.5000000224, 0.5000000075), (1.5000000224, 3.0000000075))
                Line((6.5000000969, 0.5000000075), (1.5000000224, 0.5000000075))
                Line((6.5000000969, 3.0000000075), (6.5000000969, 0.5000000075))
            make_face()
        # Symmetric extrude, each_side=2
        extrude(amount=2, both=True, mode=Mode.SUBTRACT)
    return part.part


# Description: This is an angular, multi-faced bracket or connector with an irregular polyhedron shape featuring sharp edges, internal voids, and protruding flanges designed for structural support or assembly purposes.
def model_40999_cad6be09_0001():
    """Model: seat"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 9 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 3118.3231678185, perimeter: 237.1646207204
            with BuildLine():
                Line((266.6999959946, 140.9699978828), (266.4403639362, 140.9655413848))
                Line((266.4403639362, 140.9655413848), (187.4854759163, 140.9655413848))
                Line((187.4854759163, 140.9655413848), (187.4854759163, 101.5999984741))
                Line((187.4854759163, 101.5999984741), (266.6999959946, 101.5999984741))
                Line((266.6999959946, 101.5999984741), (266.6999959946, 140.9699978828))
            make_face()
            # Profile area: 4589.7697625973, perimeter: 287.6698929157
            with BuildLine():
                Line((187.4854759163, 140.9655413848), (187.4854759163, 101.5999984741))
                Line((187.4854759163, 140.9655413848), (187.4854759163, 197.6494669176))
                Line((187.4854759163, 197.6494669176), (139.6999979019, 197.6494669176))
                Line((139.6999979019, 197.6494669176), (139.6999979019, 101.5999984741))
                Line((139.6999979019, 101.5999984741), (187.4854759163, 101.5999984741))
            make_face()
        # OneSide extrude, distance=91.44
        extrude(amount=91.44)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 101.5999984741, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 1090.3203672501, perimeter: 132.0799980164
            with BuildLine():
                Line((223.5199966431, 58.4199991226), (190.499997139, 58.4199991226))
                Line((190.499997139, 58.4199991226), (190.499997139, 25.3999996185))
                Line((190.499997139, 25.3999996185), (223.5199966431, 25.3999996185))
                Line((223.5199966431, 25.3999996185), (223.5199966431, 58.4199991226))
            make_face()
        # OneSide extrude, distance=-17.78
        extrude(amount=-17.78, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a hexagonal or trapezoidal-shaped bracket or housing component with a sloped top surface featuring internal ribs and structural reinforcements, designed for strength and rigidity in a compact form factor.
def model_40999_cad6be09_0005():
    """Model: Gear change console"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 948.3851857567, perimeter: 142.2399983978
            with BuildLine():
                Line((167.6399974823, 63.4999990463), (114.2999982834, 63.4999990463))
                Line((114.2999982834, 63.4999990463), (114.2999982834, 45.7199990463))
                Line((114.2999982834, 45.7199990463), (167.6399974823, 45.7199990463))
                Line((167.6399974823, 45.7199990463), (167.6399974823, 63.4999990463))
            make_face()
        # OneSide extrude, distance=48.26
        extrude(amount=48.26)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(48.26, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 131.2265259826, perimeter: 59.6439834297
            with BuildLine():
                CenterArc((124.4616190376, 54.6099951281), 2.5399954311, 89.7135594365, 180.2864405635)
                Line((124.4616190376, 52.069999697), (146.3040046692, 52.069999697))
                CenterArc((146.3040046692, 54.6099792574), 2.5399795604, -90, 180)
                Line((124.4743172624, 57.1499588178), (146.3040046692, 57.1499588178))
            make_face()
        # OneSide extrude, distance=-5.08
        extrude(amount=-5.08, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a parallelogram-shaped box or enclosure with a slanted, trapezoidal profile featuring a large open face and angled side walls, resembling a tilted rectangular container or duct component.
def model_40999_cad6be09_0021():
    """Model: Console"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1548.3839883728, perimeter: 193.0399988556
            with BuildLine():
                Line((177.7999973297, 114.2999982834), (177.7999973297, 93.9799982834))
                Line((177.7999973297, 93.9799982834), (253.9999961853, 93.9799982834))
                Line((253.9999961853, 93.9799982834), (253.9999973297, 114.2999982834))
                Line((177.7999973297, 114.2999982834), (253.9999973297, 114.2999982834))
            make_face()
        # OneSide extrude, distance=50.8
        extrude(amount=50.8)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 50.8, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 51.8868458596, perimeter: 25.5348650884
            with Locations((-238.7599964142, -109.2199983597)):
                Circle(4.064)
            # Profile area: 52.6262742929, perimeter: 25.7161674208
            with Locations((-238.7599964142, -99.0599985123)):
                Circle(4.0928551624)
        # OneSide extrude, distance=-5.08
        extrude(amount=-5.08, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a hex bolt or hexagonal head screw featuring a cylindrical shaft with a hexagonal head at one end, designed for fastening applications.
def model_41032_ed481084_0001():
    """Model: Bolt"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 0.5133285474, perimeter: 2.667
            with BuildLine():
                Line((0.22225, 0.384948292), (0.4445, 0))
                Line((-0.22225, 0.384948292), (0.22225, 0.384948292))
                Line((-0.4445, 0), (-0.22225, 0.384948292))
                Line((-0.22225, -0.384948292), (-0.4445, 0))
                Line((0.22225, -0.384948292), (-0.22225, -0.384948292))
                Line((0.4445, 0), (0.22225, -0.384948292))
            make_face()
        # OneSide extrude, distance=0.250000008
        extrude(amount=0.250000008)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 0.3166921744, perimeter: 1.994911335
            Circle(0.3175)
        # OneSide extrude, distance=7.62
        extrude(amount=7.62, mode=Mode.ADD)
    return part.part


# Description: This is a linear rail or guide bar, characterized by an elongated rectangular profile with a grooved channel running along its length and a mounting flange at one end.
def model_41032_ed481084_0007():
    """Model: Gear Shaft"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 8 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 35.5599994659), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 16.6225560926, perimeter: 22.9695346097
            with BuildLine():
                CenterArc((23.1139998865, 61.7893697595), 0.254, 59.7987720515, 120.2012310463)
                Line((22.8599998865, 61.7893697458), (22.86, 59.69))
                Line((26.035, 59.69), (22.86, 59.69))
                Line((26.035, 59.69), (26.035, 61.7893698316))
                CenterArc((25.781, 61.7893698316), 0.254, 0, 120.2012310463)
                Line((25.6532282169, 62.0088928861), (25.4501381162, 61.8906857831))
                CenterArc((25.3223663331, 62.1102088376), 0.254, 180, 120.2012310463)
                Line((25.0683663331, 62.1102088376), (25.0683663331, 63.6197901706))
                CenterArc((25.3223663331, 63.6197901706), 0.254, 59.7987689537, 120.2012310463)
                Line((25.6532282169, 63.7211061221), (25.4501381162, 63.839313225))
                CenterArc((25.781, 63.9406291766), 0.254, -120.2012310463, 120.2012310463)
                Line((26.035, 63.9406291766), (26.035, 66.0399990082))
                Line((26.035, 66.0399990082), (22.8599996567, 66.0399990082))
                Line((22.8599996567, 66.0399990082), (22.8599997702, 63.9406290908))
                CenterArc((23.1139997702, 63.9406291045), 0.254, -179.9999969022, 120.2012310463)
                Line((23.2417715652, 63.7211060569), (23.4448616594, 63.8393131708))
                CenterArc((23.5726334544, 63.6197901233), 0.254, 0.0000030978, 120.2012310463)
                Line((23.8266334544, 63.619790137), (23.826633536, 62.110208804))
                CenterArc((23.572633536, 62.1102087903), 0.254, -120.2012279485, 120.2012310463)
                Line((23.2417716577, 62.0088928209), (23.4448617648, 61.8906857289))
            make_face()
        # OneSide extrude, distance=-71.12
        extrude(amount=-71.12)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 66.0399990082, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 15.006706852, perimeter: 14.7904841625
            with BuildLine():
                Line((-26.035, 1.982786193), (-26.035, -1.9827872611))
                CenterArc((-24.4474998283, -0.0000005341), 2.54, -128.6821924139, 77.3643848278)
                Line((-22.8599996567, -1.9827872611), (-22.8599996567, 1.982786193))
                CenterArc((-24.4474998283, -0.0000005341), 2.54, 51.3178075861, 77.3643848278)
            make_face()
            # Profile area: 2.6307961559, perimeter: 8.5155501671
            with BuildLine():
                CenterArc((-24.4474998283, -0.0000005341), 2.54, 128.6821924139, 102.6356151722)
                Line((-26.035, 1.982786193), (-26.035, -1.9827872611))
            make_face()
            # Profile area: 2.6307961559, perimeter: 8.5155501671
            with BuildLine():
                Line((-22.8599996567, -1.9827872611), (-22.8599996567, 1.982786193))
                CenterArc((-24.4474998283, -0.0000005341), 2.54, -51.3178075861, 102.6356151722)
            make_face()
        # OneSide extrude, distance=-0.508
        extrude(amount=-0.508, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a parallelogram-shaped perforated panel or mesh screen with a dark frame border and blue mesh infill, featuring multiple mounting holes and a streamlined, aerodynamic design typical of ventilation or protective covers.
def model_41117_1b3271f2_0001():
    """Model: Circuit Board v33"""
    with BuildPart() as part:
        # Sketch1 -> Extrude2 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 29 constraints, 101 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 35.4534489229, perimeter: 46.0278007562
            with BuildLine():
                Line((6.86, -5.076950107), (6.8815269488, -5.0552493314))
                Line((6.86, -1.5270472594), (6.86, -5.076950107))
                Line((6.5815269488, -1.2508048232), (6.86, -1.5270472594))
                Line((6.5815269488, -0.1341141832), (6.5815269488, -1.2508048232))
                Line((6.4463298144, 0), (6.5815269488, -0.1341141832))
                Line((0, 0), (6.4463298144, 0))
                Line((0, -5.33), (0, 0))
                Line((6.8815269488, -5.33), (0, -5.33))
                Line((6.8815269488, -5.0552493314), (6.8815269488, -5.33))
            make_face()
            with BuildLine():
                CenterArc((2.009533656, -1.3240777172), 0.032, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1.755533656, -1.1040777172), 0.032, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((2.009533656, -1.1040777172), 0.032, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1.755533656, -1.3240777172), 0.032, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((2.009533656, -0.8160777172), 0.032, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((2.009533656, -0.5960777172), 0.032, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1.755533656, -0.8160777172), 0.032, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1.755533656, -0.5960777172), 0.032, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1.501533656, -0.8160777172), 0.032, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1.501533656, -0.5960777172), 0.032, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((6.3593200759, -2.5864129536), 0.032, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((6.3593200759, -2.3324129536), 0.032, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((6.3593200759, -2.8404129536), 0.032, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((6.6133200759, -2.8404129536), 0.032, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((6.6133200759, -2.5864129536), 0.032, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0.7611803972, -5.0579262061), 0.06, 86.8422649009, 6.384295897)
                Line((0.7644854959, -4.9980173059), (0.9161443601, -4.9979262169))
                CenterArc((0.9161803972, -5.0579262061), 0.06, -90.0193135953, 180.0537264447)
                Line((0.7636636005, -5.1178747983), (0.916160172, -5.1179262027))
                CenterArc((0.7611803972, -5.0579262061), 0.06, -92.4105891158, 4.7825510411)
                CenterArc((0.7611803972, -5.0579262061), 0.06, 93.2265607978, 174.3628500863)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1.089453597, -4.6265725393), 0.06, 173.806663955, 12.138055886)
                CenterArc((1.089453597, -4.6265725393), 0.06, 6.193336045, 167.6133279099)
                CenterArc((1.089453597, -4.6265725393), 0.06, -5.944719841, 12.138055886)
                Line((1.149130934, -4.632786672), (1.1494534558, -4.7814423642))
                CenterArc((1.089453597, -4.7815725393), 0.06, 179.875691898, 180.248616204)
                Line((1.02977626, -4.632786672), (1.0294537382, -4.7814423642))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((0.5294733874, -4.6281134658), (0.5294535975, -4.7815648014))
                CenterArc((0.589453597, -4.6265725393), 0.06, -7.1012947063, 188.5729330026)
                Line((0.6489933457, -4.6339899733), (0.6494533049, -4.7813853053))
                CenterArc((0.589453597, -4.7815725393), 0.06, 179.9926108364, 180.1861847475)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0.8242400447, -1.672840132), 0.051, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0.6242400447, -1.672840132), 0.051, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0.6242400447, -1.422840132), 0.051, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0.8242400447, -1.422840132), 0.051, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0.3490100225, -2.1525596594), 0.115, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0.3490100225, -0.9475596594), 0.115, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((4.5301184195, -4.2270071317), 0.02, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((4.7801184195, -4.2270071317), 0.02, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((5.0301184195, -4.2270071317), 0.02, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((5.7801184195, -4.2270071317), 0.02, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((5.5301184195, -4.2270071317), 0.02, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((4.0301184195, -4.2270071317), 0.02, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((3.7801184195, -4.2270071317), 0.02, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((3.5301184195, -4.2270071317), 0.02, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((3.2801184195, -4.2270071317), 0.02, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((6.2801184195, -4.2270071317), 0.02, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((3.0301184195, -4.2270071317), 0.02, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((6.0301184195, -4.2270071317), 0.02, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((4.2801184195, -4.2270071317), 0.02, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((5.2801184195, -4.2270071317), 0.02, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((6.0301184195, -3.2220071317), 0.02, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((6.2801184195, -3.2220071317), 0.02, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((5.2801184195, -3.2220071317), 0.02, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((5.5301184195, -3.2220071317), 0.02, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((5.7801184195, -3.2220071317), 0.02, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((4.7801184195, -3.2220071317), 0.02, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((5.0301184195, -3.2220071317), 0.02, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((4.5301184195, -3.2220071317), 0.02, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((4.0301184195, -3.2220071317), 0.02, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((4.2801184195, -3.2220071317), 0.02, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((3.7801184195, -3.2220071317), 0.02, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((3.5301184195, -3.2220071317), 0.02, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((3.2801184195, -3.2220071317), 0.02, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((3.0301184195, -3.2220071317), 0.02, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((2.2104895318, -2.6822537096), 0.051, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1.6149756394, -2.6822537096), 0.051, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((6.6133200759, -2.3324129536), 0.032, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((3.2983121476, -5.0954439028), 0.032, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((3.8063121476, -5.0954439028), 0.032, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((3.5523121476, -5.0954439028), 0.032, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((4.0603121476, -5.0954439028), 0.032, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((4.3143121476, -5.0954439028), 0.032, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((4.5683121476, -5.0954439028), 0.032, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((5.0705975597, -5.0954439028), 0.032, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((5.3245975597, -5.0954439028), 0.032, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((5.5785975597, -5.0954439028), 0.032, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((5.8325975597, -5.0954439028), 0.032, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((6.0865975597, -5.0954439028), 0.032, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((6.3405975597, -5.0954439028), 0.032, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((6.3386750621, -0.2642786427), 0.032, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((6.0846750621, -0.2642786427), 0.032, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((5.5766750621, -0.2642786427), 0.032, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((5.8306750621, -0.2642786427), 0.032, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((5.3226750621, -0.2642786427), 0.032, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((4.8146750621, -0.2642786427), 0.032, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((4.5606750621, -0.2642786427), 0.032, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((5.0686750621, -0.2642786427), 0.032, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((3.8966750621, -0.2642786427), 0.032, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((4.1506750621, -0.2642786427), 0.032, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((3.6426750621, -0.2642786427), 0.032, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((3.3886750621, -0.2642786427), 0.032, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((2.8806750621, -0.2642786427), 0.032, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((3.1346750621, -0.2642786427), 0.032, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((2.6266750621, -0.2642786427), 0.032, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((2.3726750621, -0.2642786427), 0.032, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((6.5549424537, -4.5852493314), 0.16, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((6.5689590318, -1.7952493314), 0.16, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1.5015269488, -0.2752493314), 0.16, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1.6915269488, -5.0591685563), 0.16, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0032169909, perimeter: 0.2010619298
            with Locations((2.009533656, -1.3240777172)):
                Circle(0.032)
            # Profile area: 0.0032169909, perimeter: 0.2010619298
            with Locations((1.755533656, -1.1040777172)):
                Circle(0.032)
            # Profile area: 0.0032169909, perimeter: 0.2010619298
            with Locations((2.009533656, -1.1040777172)):
                Circle(0.032)
            # Profile area: 0.0032169909, perimeter: 0.2010619298
            with Locations((1.755533656, -1.3240777172)):
                Circle(0.032)
            # Profile area: 0.0032169909, perimeter: 0.2010619298
            with Locations((2.009533656, -0.8160777172)):
                Circle(0.032)
            # Profile area: 0.0032169909, perimeter: 0.2010619298
            with Locations((2.009533656, -0.5960777172)):
                Circle(0.032)
            # Profile area: 0.0032169909, perimeter: 0.2010619298
            with Locations((1.755533656, -0.8160777172)):
                Circle(0.032)
            # Profile area: 0.0032169909, perimeter: 0.2010619298
            with Locations((1.755533656, -0.5960777172)):
                Circle(0.032)
            # Profile area: 0.0032169909, perimeter: 0.2010619298
            with Locations((6.3593200759, -2.5864129536)):
                Circle(0.032)
            # Profile area: 0.0032169909, perimeter: 0.2010619298
            with Locations((6.3593200759, -2.3324129536)):
                Circle(0.032)
            # Profile area: 0.0032169909, perimeter: 0.2010619298
            with Locations((6.3593200759, -2.8404129536)):
                Circle(0.032)
            # Profile area: 0.0032169909, perimeter: 0.2010619298
            with Locations((6.6133200759, -2.8404129536)):
                Circle(0.032)
            # Profile area: 0.0032169909, perimeter: 0.2010619298
            with Locations((6.6133200759, -2.5864129536)):
                Circle(0.032)
        # OneSide extrude, distance=0.16
        extrude(amount=0.16)
    return part.part


# Description: This is a flat, parallelogram-shaped metal panel or cover plate with a perforated or mesh-like surface featuring an organized pattern of holes and structural ribs for reinforcement and ventilation.
def model_41117_1b3271f2_0003():
    """Model: Circuit Board v45 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude2 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 29 constraints, 105 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 35.449646025, perimeter: 46.800632549
            with BuildLine():
                Line((6.86, -5.076950107), (6.8815269488, -5.0552493314))
                Line((6.86, -1.5270472594), (6.86, -5.076950107))
                Line((6.5815269488, -1.2508048232), (6.86, -1.5270472594))
                Line((6.5815269488, -0.1341141832), (6.5815269488, -1.2508048232))
                Line((6.4463298144, 0), (6.5815269488, -0.1341141832))
                Line((0, 0), (6.4463298144, 0))
                Line((0, -5.33), (0, 0))
                Line((6.8815269488, -5.33), (0, -5.33))
                Line((6.8815269488, -5.0552493314), (6.8815269488, -5.33))
            make_face()
            with BuildLine():
                CenterArc((2.620763499, -4.498187844), 0.03, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((2.470763499, -4.498187844), 0.03, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1.920763499, -4.498187844), 0.03, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1.770763499, -4.498187844), 0.03, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((2.9326750621, -0.6242786427), 0.03, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((3.0826750621, -0.6242786427), 0.03, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1.755533656, -1.1040777172), 0.032, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((2.009533656, -1.1040777172), 0.032, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((2.009533656, -1.3580777172), 0.032, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1.755533656, -1.3580777172), 0.032, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((2.009533656, -0.8500777172), 0.032, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1.501533656, -0.8500777172), 0.032, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1.755533656, -0.8500777172), 0.032, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((2.009533656, -0.5960777172), 0.032, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1.755533656, -0.5960777172), 0.032, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1.501533656, -0.5960777172), 0.032, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((6.3593200759, -2.5864129536), 0.032, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((6.3593200759, -2.3324129536), 0.032, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((6.3593200759, -2.8404129536), 0.032, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((6.6133200759, -2.8404129536), 0.032, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((6.6133200759, -2.5864129536), 0.032, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0.7611803972, -5.0579262061), 0.06, 86.8422649009, 6.384295897)
                Line((0.7644854959, -4.9980173059), (0.9161443601, -4.9979262169))
                CenterArc((0.9161803972, -5.0579262061), 0.06, -90.0193135953, 180.0537264447)
                Line((0.7636636005, -5.1178747983), (0.916160172, -5.1179262027))
                CenterArc((0.7611803972, -5.0579262061), 0.06, -92.4105891158, 4.7825510411)
                CenterArc((0.7611803972, -5.0579262061), 0.06, 93.2265607978, 174.3628500863)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1.089453597, -4.7815725393), 0.06, 179.875691898, 180.248616204)
                Line((1.02977626, -4.632786672), (1.0294537382, -4.7814423642))
                CenterArc((1.089453597, -4.6265725393), 0.06, 173.806663955, 12.138055886)
                CenterArc((1.089453597, -4.6265725393), 0.06, 6.193336045, 167.6133279099)
                CenterArc((1.089453597, -4.6265725393), 0.06, -5.944719841, 12.138055886)
                Line((1.149130934, -4.632786672), (1.1494534558, -4.7814423642))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((0.5294733874, -4.6281134658), (0.5294535975, -4.7815648014))
                CenterArc((0.589453597, -4.6265725393), 0.06, -7.1012947063, 188.5729330026)
                Line((0.6489933457, -4.6339899733), (0.6494533049, -4.7813853053))
                CenterArc((0.589453597, -4.7815725393), 0.06, 179.9926108364, 180.1861847475)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0.8242400447, -1.672840132), 0.051, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0.6242400447, -1.672840132), 0.051, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0.6242400447, -1.422840132), 0.051, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0.8242400447, -1.422840132), 0.051, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0.3490100225, -2.1525596594), 0.115, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0.3490100225, -0.9475596594), 0.115, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((4.5301184195, -4.1372071317), 0.02, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((4.7801184195, -4.1372071317), 0.02, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((5.0301184195, -4.1372071317), 0.02, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((5.7801184195, -4.1372071317), 0.02, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((5.5301184195, -4.1372071317), 0.02, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((4.0301184195, -4.1372071317), 0.02, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((3.7801184195, -4.1372071317), 0.02, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((3.5301184195, -4.1372071317), 0.02, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((3.2801184195, -4.1372071317), 0.02, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((6.2801184195, -4.1372071317), 0.02, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((3.0301184195, -4.1372071317), 0.02, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((6.0301184195, -4.1372071317), 0.02, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((4.2801184195, -4.1372071317), 0.02, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((5.2801184195, -4.1372071317), 0.02, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((6.0301184195, -3.3118071317), 0.02, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((6.2801184195, -3.3118071317), 0.02, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((5.2801184195, -3.3118071317), 0.02, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((5.5301184195, -3.3118071317), 0.02, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((5.7801184195, -3.3118071317), 0.02, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((4.7801184195, -3.3118071317), 0.02, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((5.0301184195, -3.3118071317), 0.02, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((4.5301184195, -3.3118071317), 0.02, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((4.0301184195, -3.3118071317), 0.02, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((4.2801184195, -3.3118071317), 0.02, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((3.7801184195, -3.3118071317), 0.02, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((3.5301184195, -3.3118071317), 0.02, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((3.2801184195, -3.3118071317), 0.02, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((3.0301184195, -3.3118071317), 0.02, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((2.1028895318, -2.6822537096), 0.0225, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1.6687756394, -2.6822537096), 0.0225, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((6.6133200759, -2.3324129536), 0.032, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((3.2983121476, -5.0954439028), 0.032, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((3.8063121476, -5.0954439028), 0.032, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((3.5523121476, -5.0954439028), 0.032, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((4.0603121476, -5.0954439028), 0.032, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((4.3143121476, -5.0954439028), 0.032, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((4.5683121476, -5.0954439028), 0.032, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((5.0705975597, -5.0954439028), 0.032, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((5.3245975597, -5.0954439028), 0.032, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((5.5785975597, -5.0954439028), 0.032, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((5.8325975597, -5.0954439028), 0.032, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((6.0865975597, -5.0954439028), 0.032, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((6.3405975597, -5.0954439028), 0.032, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((6.3386750621, -0.2642786427), 0.032, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((6.0846750621, -0.2642786427), 0.032, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((5.5766750621, -0.2642786427), 0.032, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((5.8306750621, -0.2642786427), 0.032, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((5.3226750621, -0.2642786427), 0.032, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((4.8146750621, -0.2642786427), 0.032, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((4.5606750621, -0.2642786427), 0.032, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((5.0686750621, -0.2642786427), 0.032, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((3.8966750621, -0.2642786427), 0.032, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((4.1506750621, -0.2642786427), 0.032, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((3.6426750621, -0.2642786427), 0.032, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((3.3886750621, -0.2642786427), 0.032, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((2.8806750621, -0.2642786427), 0.032, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((3.1346750621, -0.2642786427), 0.032, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((2.6266750621, -0.2642786427), 0.032, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((2.3726750621, -0.2642786427), 0.032, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((6.5549424537, -4.5852493314), 0.16, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((6.5689590318, -1.7952493314), 0.16, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1.5015269488, -0.2752493314), 0.16, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1.6915269488, -5.0591685563), 0.16, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0028274334, perimeter: 0.1884955592
            with Locations((2.620763499, -4.498187844)):
                Circle(0.03)
            # Profile area: 0.0028274334, perimeter: 0.1884955592
            with Locations((2.470763499, -4.498187844)):
                Circle(0.03)
            # Profile area: 0.0028274334, perimeter: 0.1884955592
            with Locations((1.920763499, -4.498187844)):
                Circle(0.03)
            # Profile area: 0.0028274334, perimeter: 0.1884955592
            with Locations((1.770763499, -4.498187844)):
                Circle(0.03)
            # Profile area: 0.0028274334, perimeter: 0.1884955592
            with Locations((2.9326750621, -0.6242786427)):
                Circle(0.03)
            # Profile area: 0.0028274334, perimeter: 0.1884955592
            with Locations((3.0826750621, -0.6242786427)):
                Circle(0.03)
            # Profile area: 0.0032169909, perimeter: 0.2010619298
            with Locations((1.755533656, -1.1040777172)):
                Circle(0.032)
            # Profile area: 0.0032169909, perimeter: 0.2010619298
            with Locations((2.009533656, -1.1040777172)):
                Circle(0.032)
            # Profile area: 0.0032169909, perimeter: 0.2010619298
            with Locations((2.009533656, -1.3580777172)):
                Circle(0.032)
            # Profile area: 0.0032169909, perimeter: 0.2010619298
            with Locations((1.755533656, -1.3580777172)):
                Circle(0.032)
            # Profile area: 0.0032169909, perimeter: 0.2010619298
            with Locations((2.009533656, -0.8500777172)):
                Circle(0.032)
            # Profile area: 0.0032169909, perimeter: 0.2010619298
            with Locations((1.501533656, -0.8500777172)):
                Circle(0.032)
            # Profile area: 0.0032169909, perimeter: 0.2010619298
            with Locations((1.755533656, -0.8500777172)):
                Circle(0.032)
            # Profile area: 0.0032169909, perimeter: 0.2010619298
            with Locations((2.009533656, -0.5960777172)):
                Circle(0.032)
            # Profile area: 0.0032169909, perimeter: 0.2010619298
            with Locations((1.755533656, -0.5960777172)):
                Circle(0.032)
            # Profile area: 0.0032169909, perimeter: 0.2010619298
            with Locations((6.3593200759, -2.5864129536)):
                Circle(0.032)
            # Profile area: 0.0032169909, perimeter: 0.2010619298
            with Locations((6.3593200759, -2.3324129536)):
                Circle(0.032)
            # Profile area: 0.0032169909, perimeter: 0.2010619298
            with Locations((6.3593200759, -2.8404129536)):
                Circle(0.032)
            # Profile area: 0.0032169909, perimeter: 0.2010619298
            with Locations((6.6133200759, -2.8404129536)):
                Circle(0.032)
            # Profile area: 0.0032169909, perimeter: 0.2010619298
            with Locations((6.6133200759, -2.5864129536)):
                Circle(0.032)
        # OneSide extrude, distance=0.16
        extrude(amount=0.16)
    return part.part


# Description: This is a flat, parallelogram-shaped panel or frame with a perforated or mesh surface featuring multiple parallel slots and circular holes throughout, designed for ventilation, structural lightweighting, or cable management purposes.
def model_41117_1b3271f2_0008():
    """Model: Circuit Board v40"""
    with BuildPart() as part:
        # Sketch1 -> Extrude2 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 29 constraints, 101 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 35.4609557585, perimeter: 46.0466503121
            with BuildLine():
                Line((6.86, -5.076950107), (6.8815269488, -5.0552493314))
                Line((6.86, -1.5270472594), (6.86, -5.076950107))
                Line((6.5815269488, -1.2508048232), (6.86, -1.5270472594))
                Line((6.5815269488, -0.1341141832), (6.5815269488, -1.2508048232))
                Line((6.4463298144, 0), (6.5815269488, -0.1341141832))
                Line((0, 0), (6.4463298144, 0))
                Line((0, -5.33), (0, 0))
                Line((6.8815269488, -5.33), (0, -5.33))
                Line((6.8815269488, -5.0552493314), (6.8815269488, -5.33))
            make_face()
            with BuildLine():
                CenterArc((2.8806750621, -0.6242786427), 0.03, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((3.1346750621, -0.6242786427), 0.03, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1.755533656, -1.1040777172), 0.032, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((2.009533656, -1.1040777172), 0.032, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((2.009533656, -1.3580777172), 0.032, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1.755533656, -1.3580777172), 0.032, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((2.009533656, -0.8500777172), 0.032, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1.501533656, -0.8500777172), 0.032, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1.755533656, -0.8500777172), 0.032, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((2.009533656, -0.5960777172), 0.032, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1.755533656, -0.5960777172), 0.032, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1.501533656, -0.5960777172), 0.032, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((6.3593200759, -2.5864129536), 0.032, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((6.3593200759, -2.3324129536), 0.032, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((6.3593200759, -2.8404129536), 0.032, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((6.6133200759, -2.8404129536), 0.032, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((6.6133200759, -2.5864129536), 0.032, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0.7611803972, -5.0579262061), 0.06, 86.8422649009, 6.384295897)
                Line((0.7644854959, -4.9980173059), (0.9161443601, -4.9979262169))
                CenterArc((0.9161803972, -5.0579262061), 0.06, -90.0193135953, 180.0537264447)
                Line((0.7636636005, -5.1178747983), (0.916160172, -5.1179262027))
                CenterArc((0.7611803972, -5.0579262061), 0.06, -92.4105891158, 4.7825510411)
                CenterArc((0.7611803972, -5.0579262061), 0.06, 93.2265607978, 174.3628500863)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1.089453597, -4.7815725393), 0.06, 179.875691898, 180.248616204)
                Line((1.02977626, -4.632786672), (1.0294537382, -4.7814423642))
                CenterArc((1.089453597, -4.6265725393), 0.06, 173.806663955, 12.138055886)
                CenterArc((1.089453597, -4.6265725393), 0.06, 6.193336045, 167.6133279099)
                CenterArc((1.089453597, -4.6265725393), 0.06, -5.944719841, 12.138055886)
                Line((1.149130934, -4.632786672), (1.1494534558, -4.7814423642))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((0.5294733874, -4.6281134658), (0.5294535975, -4.7815648014))
                CenterArc((0.589453597, -4.6265725393), 0.06, -7.1012947063, 188.5729330026)
                Line((0.6489933457, -4.6339899733), (0.6494533049, -4.7813853053))
                CenterArc((0.589453597, -4.7815725393), 0.06, 179.9926108364, 180.1861847475)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0.8242400447, -1.672840132), 0.051, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0.6242400447, -1.672840132), 0.051, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0.6242400447, -1.422840132), 0.051, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0.8242400447, -1.422840132), 0.051, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0.3490100225, -2.1525596594), 0.115, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0.3490100225, -0.9475596594), 0.115, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((4.5301184195, -4.1372071317), 0.02, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((4.7801184195, -4.1372071317), 0.02, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((5.0301184195, -4.1372071317), 0.02, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((5.7801184195, -4.1372071317), 0.02, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((5.5301184195, -4.1372071317), 0.02, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((4.0301184195, -4.1372071317), 0.02, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((3.7801184195, -4.1372071317), 0.02, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((3.5301184195, -4.1372071317), 0.02, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((3.2801184195, -4.1372071317), 0.02, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((6.2801184195, -4.1372071317), 0.02, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((3.0301184195, -4.1372071317), 0.02, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((6.0301184195, -4.1372071317), 0.02, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((4.2801184195, -4.1372071317), 0.02, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((5.2801184195, -4.1372071317), 0.02, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((6.0301184195, -3.3118071317), 0.02, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((6.2801184195, -3.3118071317), 0.02, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((5.2801184195, -3.3118071317), 0.02, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((5.5301184195, -3.3118071317), 0.02, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((5.7801184195, -3.3118071317), 0.02, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((4.7801184195, -3.3118071317), 0.02, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((5.0301184195, -3.3118071317), 0.02, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((4.5301184195, -3.3118071317), 0.02, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((4.0301184195, -3.3118071317), 0.02, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((4.2801184195, -3.3118071317), 0.02, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((3.7801184195, -3.3118071317), 0.02, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((3.5301184195, -3.3118071317), 0.02, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((3.2801184195, -3.3118071317), 0.02, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((3.0301184195, -3.3118071317), 0.02, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((2.1028895318, -2.6822537096), 0.0225, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1.6687756394, -2.6822537096), 0.0225, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((6.6133200759, -2.3324129536), 0.032, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((3.2983121476, -5.0954439028), 0.032, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((3.8063121476, -5.0954439028), 0.032, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((3.5523121476, -5.0954439028), 0.032, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((4.0603121476, -5.0954439028), 0.032, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((4.3143121476, -5.0954439028), 0.032, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((4.5683121476, -5.0954439028), 0.032, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((5.0705975597, -5.0954439028), 0.032, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((5.3245975597, -5.0954439028), 0.032, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((5.5785975597, -5.0954439028), 0.032, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((5.8325975597, -5.0954439028), 0.032, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((6.0865975597, -5.0954439028), 0.032, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((6.3405975597, -5.0954439028), 0.032, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((6.3386750621, -0.2642786427), 0.032, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((6.0846750621, -0.2642786427), 0.032, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((5.5766750621, -0.2642786427), 0.032, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((5.8306750621, -0.2642786427), 0.032, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((5.3226750621, -0.2642786427), 0.032, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((4.8146750621, -0.2642786427), 0.032, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((4.5606750621, -0.2642786427), 0.032, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((5.0686750621, -0.2642786427), 0.032, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((3.8966750621, -0.2642786427), 0.032, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((4.1506750621, -0.2642786427), 0.032, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((3.6426750621, -0.2642786427), 0.032, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((3.3886750621, -0.2642786427), 0.032, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((2.8806750621, -0.2642786427), 0.032, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((3.1346750621, -0.2642786427), 0.032, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((2.6266750621, -0.2642786427), 0.032, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((2.3726750621, -0.2642786427), 0.032, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((6.5549424537, -4.5852493314), 0.16, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((6.5689590318, -1.7952493314), 0.16, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1.5015269488, -0.2752493314), 0.16, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1.6915269488, -5.0591685563), 0.16, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0028274334, perimeter: 0.1884955592
            with Locations((2.8806750621, -0.6242786427)):
                Circle(0.03)
            # Profile area: 0.0028274334, perimeter: 0.1884955592
            with Locations((3.1346750621, -0.6242786427)):
                Circle(0.03)
            # Profile area: 0.0032169909, perimeter: 0.2010619298
            with Locations((1.755533656, -1.1040777172)):
                Circle(0.032)
            # Profile area: 0.0032169909, perimeter: 0.2010619298
            with Locations((2.009533656, -1.1040777172)):
                Circle(0.032)
            # Profile area: 0.0032169909, perimeter: 0.2010619298
            with Locations((2.009533656, -1.3580777172)):
                Circle(0.032)
            # Profile area: 0.0032169909, perimeter: 0.2010619298
            with Locations((1.755533656, -1.3580777172)):
                Circle(0.032)
            # Profile area: 0.0032169909, perimeter: 0.2010619298
            with Locations((2.009533656, -0.8500777172)):
                Circle(0.032)
            # Profile area: 0.0032169909, perimeter: 0.2010619298
            with Locations((1.501533656, -0.8500777172)):
                Circle(0.032)
            # Profile area: 0.0032169909, perimeter: 0.2010619298
            with Locations((1.755533656, -0.8500777172)):
                Circle(0.032)
            # Profile area: 0.0032169909, perimeter: 0.2010619298
            with Locations((2.009533656, -0.5960777172)):
                Circle(0.032)
            # Profile area: 0.0032169909, perimeter: 0.2010619298
            with Locations((1.755533656, -0.5960777172)):
                Circle(0.032)
            # Profile area: 0.0032169909, perimeter: 0.2010619298
            with Locations((6.3593200759, -2.5864129536)):
                Circle(0.032)
            # Profile area: 0.0032169909, perimeter: 0.2010619298
            with Locations((6.3593200759, -2.3324129536)):
                Circle(0.032)
            # Profile area: 0.0032169909, perimeter: 0.2010619298
            with Locations((6.3593200759, -2.8404129536)):
                Circle(0.032)
            # Profile area: 0.0032169909, perimeter: 0.2010619298
            with Locations((6.6133200759, -2.8404129536)):
                Circle(0.032)
            # Profile area: 0.0032169909, perimeter: 0.2010619298
            with Locations((6.6133200759, -2.5864129536)):
                Circle(0.032)
        # OneSide extrude, distance=0.16
        extrude(amount=0.16)
    return part.part


# Description: This is a cylindrical connector or coupling with a broad, flat-topped hat-like shape featuring two concentric grooved bands or ridges running around its circumference, designed for secure gripping or alignment.
def model_41124_a5855c0d_0002():
    """Model: Stem Seat"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.4948008429, perimeter: 6.5973445725
            with BuildLine():
                CenterArc((0.02323374, -5.110233766), 0.6, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0.02323374, -5.110233766), 0.45, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.6
        extrude(amount=0.6)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.1388273369, perimeter: 9.1106186954
            with BuildLine():
                CenterArc((0.02323374, -5.110233766), 0.85, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0.02323374, -5.110233766), 0.6, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3, mode=Mode.ADD)
    return part.part


# Description: This is a dark gray cylindrical pipe or tube with a slightly tapered or textured top end, featuring a smooth cylindrical body and appearing to be a hollow tubular component commonly used in mechanical assemblies.
def model_41124_a5855c0d_0008():
    """Model: Valve Guide"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.1547562844, perimeter: 7.2256631033
            Circle(1.15)
        # OneSide extrude, distance=12
        extrude(amount=12)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.0131636308, perimeter: 13.5088484104
            with BuildLine():
                CenterArc((0, 0), 1.15, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=3.8
        extrude(amount=3.8, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a toroidal (doughnut-shaped) component featuring a smooth, rounded outer surface with a large central hole, characterized by symmetric curved geometry and appears to be a bearing ring, spacer, or similar mechanical part with a hollow core.
def model_41128_ee74f244_0015():
    """Model: 11-Collar"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 3.0877487008, perimeter: 12.9669236777
            with BuildLine():
                CenterArc((-11.6840003729, 1.0160000324), 1.27, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-11.6840003729, 1.0160000324), 0.79375, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.10998
        extrude(amount=1.10998)

        # Sketch3 -> Extrude2 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0791730436, perimeter: 0.9974556675
            with Locations((0.55626, -11.6840003729)):
                Circle(0.15875)
        # OneSide extrude, distance=3.048
        extrude(amount=3.048, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a hexagonal or wedge-shaped structural component with a tapered profile, featuring a flat base, angled top surfaces with triangulated faceting, and what appears to be a central longitudinal slot or groove running along its length.
def model_41128_ee74f244_0017():
    """Model: 2-Sliding Jaw"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 59.274075, perimeter: 31.115
            with BuildLine():
                Line((6.6675, -8.89), (0, -8.89))
                Line((6.6675, 0), (6.6675, -8.89))
                Line((0, 0), (6.6675, 0))
                Line((0, -8.89), (0, 0))
            make_face()
        # OneSide extrude, distance=2.54
        extrude(amount=2.54)

        # Sketch4 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(6.6675, 0.0000001502, 0.0000001577), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.1999996, perimeter: 2.85496
            with BuildLine():
                Line((-8.7325198423, 2.5399998498), (-8.8899998423, 2.5399998498))
                Line((-8.8899998423, 1.2699998498), (-8.8899998423, 2.5399998498))
                Line((-8.7325198423, 1.2699998498), (-8.8899998423, 1.2699998498))
                Line((-8.7325198423, 2.5399998498), (-8.7325198423, 1.2699998498))
            make_face()
        # OneSide extrude, distance=-5.715
        extrude(amount=-5.715, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical capsule-shaped component with rounded ends, featuring a central longitudinal slot or groove running along its length and circular openings or ports at each end.
def model_41128_ee74f244_0018():
    """Model: 17-Handle Post"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.7125573925, perimeter: 2.9923670025
            with Locations((-35.5599994659, 5.0799999237)):
                Circle(0.47625)
        # OneSide extrude, distance=0.762
        extrude(amount=0.762)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 2.1376721774, perimeter: 8.9771010076
            with BuildLine():
                CenterArc((35.5599994659, 5.0799999237), 0.9525, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((35.5599994659, 5.0799999237), 0.47625, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.7125573925, perimeter: 2.9923670025
            with Locations((35.5599994659, 5.0799999237)):
                Circle(0.47625)
        # OneSide extrude, distance=3.2512
        extrude(amount=3.2512, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical rod or shaft with rounded ends, featuring a uniform diameter throughout its length and a slight diagonal orientation.
def model_41142_1bf94ee2_0003():
    """Model: Pipe v5"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 2.0106192983, perimeter: 5.0265482457
            Circle(0.8)
        # OneSide extrude, distance=20
        extrude(amount=20)

        # Sketch2 -> Extrude4 (Cut)
        # Sketch on XY construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0129903811, perimeter: 0.5196152423
            with BuildLine():
                Line((0.384494388, 0.8690462635), (0.3756364502, 0.6960678344))
                Line((0.3756364502, 0.6960678344), (0.529869133, 0.7748858498))
                Line((0.529869133, 0.7748858498), (0.384494388, 0.8690462635))
            make_face()
        # OneSide extrude, distance=10
        extrude(amount=10, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a rivet or fastener consisting of a cylindrical shaft with a larger circular flange head at one end, designed for joining or securing components together.
def model_41142_1bf94ee2_0008():
    """Model: Rivet v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.5026548396, perimeter: 2.5132741603
            Circle(0.400000006)
        # OneSide extrude, distance=2.2
        extrude(amount=2.2)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 1.0367255607, perimeter: 6.9115038753
            with BuildLine():
                CenterArc((0, 0), 0.7, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.400000006, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.5026548396, perimeter: 2.5132741603
            Circle(0.400000006)
        # OneSide extrude, distance=0.15
        extrude(amount=0.15, mode=Mode.ADD)
    return part.part


# Description: This is a spherical or cylindrical manifold body with multiple rectangular flanges and ports distributed around its circumference for fluid or pneumatic connections.
def model_41142_1bf94ee2_0010():
    """Model: Gearwheel v11"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 21 constraints, 15 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.4313881528, perimeter: 6.4602875206
            with BuildLine():
                CenterArc((0, 0), 2.7, 90, 22.5)
                Line((0, 0), (-1.0332452674, 2.4944747378))
                Line((0, 0), (0, 2.7))
            make_face()
            # Profile area: 1.4313881528, perimeter: 6.4602875206
            with BuildLine():
                Line((0, 0), (1.0332452674, 2.4944747378))
                Line((0, 0), (1.9091883092, 1.9091883092))
                CenterArc((0, 0), 2.7, 45, 22.5)
            make_face()
            # Profile area: 1.4313881528, perimeter: 6.4602875206
            with BuildLine():
                Line((0, 0), (1.9091883092, 1.9091883092))
                Line((0, 0), (2.4944747378, 1.0332452674))
                CenterArc((0, 0), 2.7, 22.5, 22.5)
            make_face()
            # Profile area: 1.4313881528, perimeter: 6.4602875206
            with BuildLine():
                Line((0, 0), (0, 2.7))
                Line((0, 0), (1.0332452674, 2.4944747378))
                CenterArc((0, 0), 2.7, 67.5, 22.5)
            make_face()
            # Profile area: 1.4313881528, perimeter: 6.4602875206
            with BuildLine():
                Line((0, 0), (2.4944747378, 1.0332452674))
                Line((0, 0), (2.7, 0))
                CenterArc((0, 0), 2.7, 0, 22.5)
            make_face()
            # Profile area: 1.4313881528, perimeter: 6.4602875206
            with BuildLine():
                Line((0, 0), (1.0332452674, -2.4944747378))
                Line((0, 0), (0, -2.7))
                CenterArc((0, 0), 2.7, -90, 22.5)
            make_face()
            # Profile area: 1.4313881528, perimeter: 6.4602875206
            with BuildLine():
                Line((0, 0), (-2.7, 0))
                Line((0, 0), (-2.4944747378, 1.0332452674))
                CenterArc((0, 0), 2.7, 157.5, 22.5)
            make_face()
            # Profile area: 0.8384125394, perimeter: 3.7954643984
            with BuildLine():
                Line((1.0332452674, 2.4944747378), (1.30112367, 3.1411904105))
                CenterArc((0, 0), 2.7, 45, 22.5)
                Line((1.9091883092, 1.9091883092), (2.404163056, 2.404163056))
                CenterArc((0, 0), 3.4, 45, 22.5)
            make_face()
            # Profile area: 1.4313881528, perimeter: 6.4602875206
            with BuildLine():
                Line((0, 0), (1.9091883092, -1.9091883092))
                Line((0, 0), (1.0332452674, -2.4944747378))
                CenterArc((0, 0), 2.7, -67.5, 22.5)
            make_face()
            # Profile area: 1.4313881528, perimeter: 6.4602875206
            with BuildLine():
                Line((0, 0), (-2.4944747378, 1.0332452674))
                Line((0, 0), (-1.9091883092, 1.9091883092))
                CenterArc((0, 0), 2.7, 135, 22.5)
            make_face()
            # Profile area: 1.4313881528, perimeter: 6.4602875206
            with BuildLine():
                Line((0, 0), (2.7, 0))
                Line((0, 0), (2.4944747378, -1.0332452674))
                CenterArc((0, 0), 2.7, -22.5, 22.5)
            make_face()
            # Profile area: 1.4313881528, perimeter: 6.4602875206
            with BuildLine():
                Line((0, 0), (2.4944747378, -1.0332452674))
                Line((0, 0), (1.9091883092, -1.9091883092))
                CenterArc((0, 0), 2.7, -45, 22.5)
            make_face()
            # Profile area: 1.4313881528, perimeter: 6.4602875206
            with BuildLine():
                CenterArc((0, 0), 2.7, 112.5, 22.5)
                Line((0, 0), (-1.9091883092, 1.9091883092))
                Line((0, 0), (-1.0332452674, 2.4944747378))
            make_face()
            # Profile area: 1.4313881528, perimeter: 6.4602875206
            with BuildLine():
                Line((0, 0), (-1.9091883092, -1.9091883092))
                Line((0, 0), (-2.4944747378, -1.0332452674))
                CenterArc((0, 0), 2.7, -157.5, 22.5)
            make_face()
            # Profile area: 1.4313881528, perimeter: 6.4602875206
            with BuildLine():
                Line((0, 0), (0, -2.7))
                Line((0, 0), (-1.0332452674, -2.4944747378))
                CenterArc((0, 0), 2.7, -112.5, 22.5)
            make_face()
            # Profile area: 1.4313881528, perimeter: 6.4602875206
            with BuildLine():
                Line((0, 0), (-1.0332452674, -2.4944747378))
                Line((0, 0), (-1.9091883092, -1.9091883092))
                CenterArc((0, 0), 2.7, -135, 22.5)
            make_face()
            # Profile area: 1.4313881528, perimeter: 6.4602875206
            with BuildLine():
                Line((0, 0), (-2.4944747378, -1.0332452674))
                Line((0, 0), (-2.7, 0))
                CenterArc((0, 0), 2.7, -180, 22.5)
            make_face()
        # OneSide extrude, distance=1.2
        extrude(amount=1.2)

        # Sketch2 -> Extrude4 (NewBody)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1.2), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.76, perimeter: 3.5
            with BuildLine():
                Line((-0.7000000104, 4.900000073), (-0.7000000104, 3.950000073))
                Line((-0.7000000104, 3.950000073), (0.0999999896, 3.950000073))
                Line((0.0999999896, 4.900000073), (0.0999999896, 3.950000073))
                Line((-0.7000000104, 4.900000073), (0.0999999896, 4.900000073))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch1 -> Extrude6 (Join)
        # Sketch on XY construction plane
        # Sketch has 21 constraints, 15 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.8384125394, perimeter: 3.7954643984
            with BuildLine():
                Line((0, -2.7), (0, -3.4))
                CenterArc((0, 0), 2.7, -112.5, 22.5)
                Line((-1.0332452674, -2.4944747378), (-1.30112367, -3.1411904105))
                CenterArc((0, 0), 3.4, -112.5, 22.5)
            make_face()
            # Profile area: 0.8384125394, perimeter: 3.7954643984
            with BuildLine():
                Line((2.4944747378, -1.0332452674), (3.1411904105, -1.30112367))
                CenterArc((0, 0), 2.7, -45, 22.5)
                Line((1.9091883092, -1.9091883092), (2.404163056, -2.404163056))
                CenterArc((0, 0), 3.4, -45, 22.5)
            make_face()
            # Profile area: 0.8384125394, perimeter: 3.7954643984
            with BuildLine():
                Line((-1.9091883092, 1.9091883092), (-2.404163056, 2.404163056))
                CenterArc((0, 0), 2.7, 112.5, 22.5)
                Line((-1.0332452674, 2.4944747378), (-1.30112367, 3.1411904105))
                CenterArc((0, 0), 3.4, 112.5, 22.5)
            make_face()
            # Profile area: 0.8384125394, perimeter: 3.7954643984
            with BuildLine():
                Line((-2.4944747378, -1.0332452674), (-3.1411904105, -1.30112367))
                CenterArc((0, 0), 2.7, -180, 22.5)
                Line((-2.7, 0), (-3.4, 0))
                CenterArc((0, 0), 3.4, -180, 22.5)
            make_face()
        # OneSide extrude, distance=1.2
        extrude(amount=1.2, mode=Mode.ADD)
    return part.part


# Description: This is a dual-chamber geometric component featuring two identical pentagonal or trapezoidal boxes connected side-by-side, each with an angled pyramidal top section and internal ribbing or support structures visible through wireframe sections.
def model_41211_11f6b8a0_0007():
    """Model: cordholder"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 8 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 12.6999998093), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1.6129001029, perimeter: 5.0800001621
            with BuildLine():
                Line((-1.2700000405, 0.5080000162), (-1.2700000405, 1.7780000567))
                Line((-1.2700000405, 1.7780000567), (-2.5400000811, 1.7780000567))
                Line((-2.5400000811, 1.7780000567), (-2.5400000811, 0.5080000162))
                Line((-2.5400000811, 0.5080000162), (-1.2700000405, 0.5080000162))
            make_face()
            # Profile area: 1.6129001029, perimeter: 5.0800001621
            with BuildLine():
                Line((2.5400000811, 0.5080000162), (2.5400000811, 1.7780000567))
                Line((2.5400000811, 1.7780000567), (1.2700000405, 1.7780000567))
                Line((1.2700000405, 1.7780000567), (1.2700000405, 0.5080000162))
                Line((1.2700000405, 0.5080000162), (2.5400000811, 0.5080000162))
            make_face()
        # OneSide extrude, distance=2.286
        extrude(amount=2.286)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 8 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 14.9859998093), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 3.1612842018, perimeter: 7.112000227
            with BuildLine():
                Line((2.7940000892, 0.2540000081), (1.0160000324, 0.2540000081))
                Line((2.7940000892, 2.0320000648), (2.7940000892, 0.2540000081))
                Line((1.0160000324, 2.0320000648), (2.7940000892, 2.0320000648))
                Line((1.0160000324, 0.2540000081), (1.0160000324, 2.0320000648))
            make_face()
            # Profile area: 1.5483840988, perimeter: 12.1920003891
            with BuildLine():
                Line((-1.0160000324, 0.2540000081), (-2.7940000892, 0.2540000081))
                Line((-1.0160000324, 2.0320000648), (-1.0160000324, 0.2540000081))
                Line((-2.7940000892, 2.0320000648), (-1.0160000324, 2.0320000648))
                Line((-2.7940000892, 0.2540000081), (-2.7940000892, 2.0320000648))
            make_face()
            with BuildLine():
                Line((-1.2700000405, 1.7780000567), (-2.5400000811, 1.7780000567))
                Line((-1.2700000405, 0.5080000162), (-1.2700000405, 1.7780000567))
                Line((-2.5400000811, 0.5080000162), (-1.2700000405, 0.5080000162))
                Line((-2.5400000811, 1.7780000567), (-2.5400000811, 0.5080000162))
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 1.6129001029, perimeter: 5.0800001621
            with BuildLine():
                Line((-2.5400000811, 1.7780000567), (-2.5400000811, 0.5080000162))
                Line((-2.5400000811, 0.5080000162), (-1.2700000405, 0.5080000162))
                Line((-1.2700000405, 0.5080000162), (-1.2700000405, 1.7780000567))
                Line((-1.2700000405, 1.7780000567), (-2.5400000811, 1.7780000567))
            make_face()
        # OneSide extrude, distance=0.254
        extrude(amount=0.254, mode=Mode.ADD)
    return part.part


# Description: This is a flat parallelogram or skewed rectangular plate with a simple, uniform thickness and no holes, slots, or additional features—essentially a basic geometric panel or flat component.
def model_41229_16283ae1_0005():
    """Model: Front Panel v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 5 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1395, perimeter: 152
            with BuildLine():
                Line((-22.5, 15.5), (22.5, 15.5))
                Line((-22.5, -15.5), (-22.5, 15.5))
                Line((22.5, -15.5), (-22.5, -15.5))
                Line((22.5, 15.5), (22.5, -15.5))
            make_face()
        # OneSide extrude, distance=0.8
        extrude(amount=0.8)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.8), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1275.96, perimeter: 145.6
            with BuildLine():
                Line((21.7, 14.7), (-21.7, 14.7))
                Line((-21.7, 14.7), (-21.7, -14.7))
                Line((-21.7, -14.7), (21.7, -14.7))
                Line((21.7, -14.7), (21.7, 14.7))
            make_face()
        # OneSide extrude, distance=0.1
        extrude(amount=0.1, mode=Mode.ADD)
    return part.part


# Description: This is a long, narrow parallelogram-shaped mounting plate or bracket with a slanted rectangular form featuring multiple evenly-spaced rectangular slots or cutouts along its length for fastening or alignment purposes.
def model_41229_16283ae1_0011():
    """Model: Buttons Side v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 7.5, perimeter: 13
            with BuildLine():
                Line((1.5, 5), (1.5, 0))
                Line((0, 5), (1.5, 5))
                Line((0, 0), (0, 5))
                Line((1.5, 0), (0, 0))
            make_face()
        # OneSide extrude, distance=-0.1
        extrude(amount=-0.1)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 8 constraints, 27 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.09, perimeter: 1.2
            with BuildLine():
                Line((0.9, 0.6000000089), (0.6, 0.6000000089))
                Line((0.6, 0.6000000089), (0.6, 0.3000000089))
                Line((0.6, 0.3000000089), (0.9, 0.3000000089))
                Line((0.9, 0.3000000089), (0.9, 0.6000000089))
            make_face()
            # Profile area: 0.12, perimeter: 1.4
            with BuildLine():
                Line((0.9, 1.0500000283), (0.9, 1.4500000283))
                Line((0.9, 1.4500000283), (0.6, 1.4500000283))
                Line((0.6, 1.4500000283), (0.6, 1.0500000283))
                Line((0.6, 1.0500000283), (0.9, 1.0500000283))
            make_face()
            # Profile area: 0.12, perimeter: 1.4
            with BuildLine():
                Line((0.6, 1.5000000283), (0.6, 1.9000000283))
                Line((0.9, 1.5000000283), (0.6, 1.5000000283))
                Line((0.9, 1.9000000283), (0.9, 1.5000000283))
                Line((0.6, 1.9000000283), (0.9, 1.9000000283))
            make_face()
            # Profile area: 0.1065600224, perimeter: 1.3104001493
            with BuildLine():
                Line((0.6, 2.8552001238), (0.9, 2.8552001238))
                Line((0.6, 2.8552001238), (0.6, 2.5000000492))
                Line((0.9, 2.5000000492), (0.6, 2.5000000492))
                Line((0.9, 2.8552001238), (0.9, 2.5000000492))
            make_face()
            # Profile area: 0.1184399776, perimeter: 1.3895998507
            with BuildLine():
                Line((0.6, 3.3000000492), (0.6, 2.9052001238))
                Line((0.9, 2.9052001238), (0.6, 2.9052001238))
                Line((0.9, 2.9052001238), (0.9, 3.3000000492))
                Line((0.6, 3.3000000492), (0.9, 3.3000000492))
            make_face()
            # Profile area: 0.175, perimeter: 1.7
            with BuildLine():
                Line((1, 3.55), (0.5, 3.55))
                Line((1, 3.9), (1, 3.55))
                Line((0.5, 3.9), (1, 3.9))
                Line((0.5, 3.55), (0.5, 3.9))
            make_face()
            # Profile area: 0.175, perimeter: 1.7
            with BuildLine():
                Line((1, 4.3), (0.5, 4.3))
                Line((1, 4.3), (1, 4.65))
                Line((0.5, 4.65), (1, 4.65))
                Line((0.5, 4.3), (0.5, 4.65))
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)
    return part.part


# Description: This is a rectangular trapezoidal steel structural component or duct with angled sidewalls, an open top framework with internal ribbing or bracing, and a tapered profile that narrows toward one end.
def model_41229_16283ae1_0013():
    """Model: Audio Panels v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 24, perimeter: 22
            with BuildLine():
                Line((0, 3), (0, 0))
                Line((0, 0), (8, 0))
                Line((8, 0), (8, 3))
                Line((8, 3), (0, 3))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 52 constraints, 10 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 1, perimeter: 5
            with BuildLine():
                Line((1, -0.5), (1, -2.5))
                Line((0.5, -0.5), (1, -0.5))
                Line((0.5, -2.5), (0.5, -0.5))
                Line((1, -2.5), (0.5, -2.5))
            make_face()
            # Profile area: 1, perimeter: 5
            with BuildLine():
                Line((1.6914911568, -2.5), (1.1914911568, -2.5))
                Line((1.6914911568, -0.5), (1.6914911568, -2.5))
                Line((1.1914911568, -0.5), (1.6914911568, -0.5))
                Line((1.1914911568, -2.5), (1.1914911568, -0.5))
            make_face()
            # Profile area: 1.0000000186, perimeter: 5.0000000745
            with BuildLine():
                Line((1.8978567065, -2.5000000373), (1.8978567065, -0.5))
                Line((2.3978567065, -2.5000000373), (1.8978567065, -2.5000000373))
                Line((2.3978567065, -0.5), (2.3978567065, -2.5000000373))
                Line((1.8978567065, -0.5), (2.3978567065, -0.5))
            make_face()
            # Profile area: 1, perimeter: 5
            with BuildLine():
                Line((2.5880619504, -2.5), (2.5880619504, -0.5))
                Line((3.0880619504, -2.5), (2.5880619504, -2.5))
                Line((3.0880619504, -0.5), (3.0880619504, -2.5))
                Line((2.5880619504, -0.5), (3.0880619504, -0.5))
            make_face()
            # Profile area: 1, perimeter: 5
            with BuildLine():
                Line((3.3044358098, -2.5), (3.3044358098, -0.5))
                Line((3.8044358098, -2.5), (3.3044358098, -2.5))
                Line((3.8044358098, -0.5), (3.8044358098, -2.5))
                Line((3.3044358098, -0.5), (3.8044358098, -0.5))
            make_face()
            # Profile area: 1, perimeter: 5
            with BuildLine():
                Line((4, -2.5), (4, -0.5))
                Line((4.5, -2.5), (4, -2.5))
                Line((4.5, -0.5), (4.5, -2.5))
                Line((4, -0.5), (4.5, -0.5))
            make_face()
            # Profile area: 1, perimeter: 5
            with BuildLine():
                Line((4.7137049401, -2.5), (4.7137049401, -0.5))
                Line((5.2137049401, -2.5), (4.7137049401, -2.5))
                Line((5.2137049401, -0.5), (5.2137049401, -2.5))
                Line((4.7137049401, -0.5), (5.2137049401, -0.5))
            make_face()
            # Profile area: 1.0000000186, perimeter: 5.0000000745
            with BuildLine():
                Line((5.3937771397, -2.5000000373), (5.3937771397, -0.5))
                Line((5.8937771397, -2.5000000373), (5.3937771397, -2.5000000373))
                Line((5.8937771397, -0.5), (5.8937771397, -2.5000000373))
                Line((5.3937771397, -0.5), (5.8937771397, -0.5))
            make_face()
            # Profile area: 1, perimeter: 5
            with BuildLine():
                Line((6.1348814598, -2.5), (6.1348814598, -0.5))
                Line((6.6348814598, -2.5), (6.1348814598, -2.5))
                Line((6.6348814598, -0.5), (6.6348814598, -2.5))
                Line((6.1348814598, -0.5), (6.6348814598, -0.5))
            make_face()
            # Profile area: 1, perimeter: 5
            with BuildLine():
                Line((7, -0.5), (7, -2.5))
                Line((7, -2.5), (7.5, -2.5))
                Line((7.5, -2.5), (7.5, -0.5))
                Line((7.5, -0.5), (7, -0.5))
            make_face()
        # OneSide extrude, distance=-0.95
        extrude(amount=-0.95, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a rectangular enclosure or chassis with a sloped top surface, featuring multiple parallel vertical slots or ribs along its length and a solid end flange on the right side.
def model_41229_16283ae1_0018():
    """Model: Bottom Left Back v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 44, perimeter: 30
            with BuildLine():
                Line((0, 0), (11, 0))
                Line((11, 4), (11, 0))
                Line((0, 4), (11, 4))
                Line((0, 0), (0, 4))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 58 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1.5, perimeter: 7
            with BuildLine():
                Line((1, 0.5), (0.5, 0.5))
                Line((1, 3.5), (1, 0.5))
                Line((0.5, 3.5), (1, 3.5))
                Line((0.5, 0.5), (0.5, 3.5))
            make_face()
            # Profile area: 1.5, perimeter: 7
            with BuildLine():
                Line((1.5, 0.5), (1.5, 3.5))
                Line((2, 0.5), (1.5, 0.5))
                Line((2, 3.5), (2, 0.5))
                Line((1.5, 3.5), (2, 3.5))
            make_face()
            # Profile area: 1.5, perimeter: 7
            with BuildLine():
                Line((2.5, 0.5), (2.5, 3.5))
                Line((3, 0.5), (2.5, 0.5))
                Line((3, 3.5), (3, 0.5))
                Line((2.5, 3.5), (3, 3.5))
            make_face()
            # Profile area: 1.5, perimeter: 7
            with BuildLine():
                Line((3.5, 0.5), (3.5, 3.5))
                Line((4, 0.5), (3.5, 0.5))
                Line((4, 3.5), (4, 0.5))
                Line((3.5, 3.5), (4, 3.5))
            make_face()
            # Profile area: 1.5, perimeter: 7
            with BuildLine():
                Line((4.5, 0.5), (4.5, 3.5))
                Line((5, 0.5), (4.5, 0.5))
                Line((5, 3.5), (5, 0.5))
                Line((4.5, 3.5), (5, 3.5))
            make_face()
            # Profile area: 1.5, perimeter: 7
            with BuildLine():
                Line((5.5, 0.5), (5.5, 3.5))
                Line((6, 0.5), (5.5, 0.5))
                Line((6, 3.5), (6, 0.5))
                Line((5.5, 3.5), (6, 3.5))
            make_face()
            # Profile area: 1.5, perimeter: 7
            with BuildLine():
                Line((6.5, 0.5), (6.5, 3.5))
                Line((7, 0.5), (6.5, 0.5))
                Line((7, 3.5), (7, 0.5))
                Line((6.5, 3.5), (7, 3.5))
            make_face()
            # Profile area: 1.5, perimeter: 7
            with BuildLine():
                Line((7.5, 0.5), (7.5, 3.5))
                Line((8, 0.5), (7.5, 0.5))
                Line((8, 3.5), (8, 0.5))
                Line((7.5, 3.5), (8, 3.5))
            make_face()
            # Profile area: 1.5, perimeter: 7
            with BuildLine():
                Line((8.5, 0.5), (8.5, 3.5))
                Line((9, 0.5), (8.5, 0.5))
                Line((9, 3.5), (9, 0.5))
                Line((8.5, 3.5), (9, 3.5))
            make_face()
            # Profile area: 1.5, perimeter: 7
            with BuildLine():
                Line((9.5, 0.5), (9.5, 3.5))
                Line((10, 0.5), (9.5, 0.5))
                Line((10, 3.5), (10, 0.5))
                Line((9.5, 3.5), (10, 3.5))
            make_face()
        # OneSide extrude, distance=-0.9
        extrude(amount=-0.9, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a stepped cylindrical connector or coupling featuring a larger hollow cylindrical body with a smaller solid cylindrical shaft or post protruding from one end, commonly used as a mechanical fastener or assembly component.
def model_41234_74275eb0_0003():
    """Model: Smaller pins"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.3166921744, perimeter: 1.994911335
            with Locations((89.2907429909, 38.9206347736)):
                Circle(0.3175)
        # OneSide extrude, distance=0.3175
        extrude(amount=0.3175)

        # Sketch3 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.3175), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0791730436, perimeter: 0.9974556675
            with Locations((89.2907429909, 38.9206347736)):
                Circle(0.15875)
        # OneSide extrude, distance=0.3175
        extrude(amount=0.3175, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical pulley or sprocket wheel with a large flat face, a textured or grooved outer rim, and a central hub with a bore hole for shaft mounting.
def model_41234_74275eb0_0007():
    """Model: Big Dowel"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 11.4009182797, perimeter: 11.9694680102
            with Locations((65.156842809, 39.8205416644)):
                Circle(1.905)
        # OneSide extrude, distance=1.27
        extrude(amount=1.27)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1.27), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.3166921744, perimeter: 1.994911335
            with Locations((65.156842809, 39.8205416644)):
                Circle(0.3175)
        # OneSide extrude, distance=1.143
        extrude(amount=1.143, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical shaft or rod with a slightly tapered or stepped design, featuring a uniform circular cross-section throughout its length and a slight shoulder or diameter transition near the upper end.
def model_41234_74275eb0_0009():
    """Model: Front Support"""
    with BuildPart() as part:
        # Sketch1 -> Extrude3 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 11.4009182797, perimeter: 11.9694680102
            with Locations((121.4644841992, 0.2052236091)):
                Circle(1.905)
        # OneSide extrude, distance=27.94
        extrude(amount=27.94)

        # Sketch3 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 27.94, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 5.067074791, perimeter: 7.9796453401
            with Locations((-121.4644841992, -0.2052236091)):
                Circle(1.27)
        # OneSide extrude, distance=5.08
        extrude(amount=5.08, mode=Mode.ADD)
    return part.part


# Description: A straight cylindrical rod or shaft with a uniform circular cross-section and slightly tapered or rounded ends.
def model_41234_74275eb0_0010():
    """Model: Back Bar"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.3166921744, perimeter: 1.994911335
            with Locations((-17.7123186555, -15.6302972675)):
                Circle(0.3175)
        # OneSide extrude, distance=26.67508
        extrude(amount=26.67508)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.3166921744, perimeter: 1.994911335
            with Locations((-17.7123186555, 15.6302972675)):
                Circle(0.3175)
        # OneSide extrude, distance=0.635
        extrude(amount=0.635, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical rod or pin with a rounded end, featuring a simple, elongated shape with a hemispherical or rounded left end and a flat right end, commonly used as a dowel pin, axle, or mechanical fastener.
def model_41234_74275eb0_0013():
    """Model: Back Support"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 11.4009182797, perimeter: 11.9694680102
            with Locations((-40.4942920718, 86.484960945)):
                Circle(1.905)
        # OneSide extrude, distance=58.42
        extrude(amount=58.42)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 5.067074791, perimeter: 7.9796453401
            with Locations((40.4942920718, 86.484960945)):
                Circle(1.27)
        # OneSide extrude, distance=5.08
        extrude(amount=5.08, mode=Mode.ADD)
    return part.part


# Description: This is a rectangular pyramid or wedge-shaped 3D part with a triangulated surface structure, featuring a pointed apex at the top and a rectangular base, with internal diagonal edge divisions visible across its faces.
def model_41303_bd1def52_0006():
    """Model: Left Leg"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 70.9676, perimeter: 114.3
            with BuildLine():
                Line((-45.085, 27.94), (-45.085, -27.94))
                Line((-45.085, -27.94), (-43.815, -27.94))
                Line((-43.815, -27.94), (-43.815, 27.94))
                Line((-43.815, 27.94), (-45.085, 27.94))
            make_face()
        # OneSide extrude, distance=2.921
        extrude(amount=2.921)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 148.3868, perimeter: 121.92
            with BuildLine():
                Line((-45.7199993134, 29.2100004387), (-45.7199993134, -29.2099995613))
                Line((-45.7199993134, -29.2099995613), (-43.1799993134, -29.2099995613))
                Line((-43.1799993134, -29.2099995613), (-43.1799993134, 29.2100004387))
                Line((-43.1799993134, 29.2100004387), (-45.7199993134, 29.2100004387))
            make_face()
        # OneSide extrude, distance=-86.36
        extrude(amount=-86.36, mode=Mode.ADD)
    return part.part


# Description: This is a belt or band-like component with a curved, wrap-around shape featuring mesh or perforated sections on top, dark solid walls on the sides, and what appears to be closure or fastening mechanisms, designed to wrap around and secure an object or structure.
def model_41319_bb28c4f4_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch3 -> Extrude4 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 19 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.6437513714, perimeter: 9.3294878544
            with BuildLine():
                Line((-7, 0), (-7, 1.5))
                Line((-4, 0), (-7, 0))
                CenterArc((0, 0), 4, 157.975687163, 22.024312837)
                Line((-7, 1.5), (-3.7080992435, 1.5))
            make_face()
            # Profile area: 50.2654824574, perimeter: 25.1327412287
            with BuildLine():
                CenterArc((0, 0), 4, 157.975687163, 22.024312837)
                CenterArc((0, 0), 4, -180, 22.024312837)
                CenterArc((0, 0), 4, -157.975687163, 135.9513743259)
                CenterArc((0, 0), 4, -22.024312837, 22.024312837)
                CenterArc((0, 0), 4, 0, 22.024312837)
                CenterArc((0, 0), 4, 22.024312837, 135.9513743259)
            make_face()
            # Profile area: 4.6437513714, perimeter: 9.3294878544
            with BuildLine():
                CenterArc((0, 0), 4, 0, 22.024312837)
                Line((4, 0), (7, 0))
                Line((7, 0), (7, 1.5))
                Line((7, 1.5), (3.7080992435, 1.5))
            make_face()
            # Profile area: 3.5342917353, perimeter: 7.7123889804
            with BuildLine():
                Line((7, 0), (7, 1.5))
                Line((7, 0), (7, -1.5))
                CenterArc((7, 0), 1.5, -90, 180)
            make_face()
            # Profile area: 4.6437513714, perimeter: 9.3294878544
            with BuildLine():
                Line((7, 0), (7, -1.5))
                Line((4, 0), (7, 0))
                CenterArc((0, 0), 4, -22.024312837, 22.024312837)
                Line((7, -1.5), (3.7080992435, -1.5))
            make_face()
            # Profile area: 4.6437513714, perimeter: 9.3294878544
            with BuildLine():
                CenterArc((0, 0), 4, -180, 22.024312837)
                Line((-4, 0), (-7, 0))
                Line((-7, 0), (-7, -1.5))
                Line((-7, -1.5), (-3.7080992435, -1.5))
            make_face()
            # Profile area: 3.5342917353, perimeter: 7.7123889804
            with BuildLine():
                CenterArc((-7, 0), 1.5, 90, 180)
                Line((-7, 0), (-7, -1.5))
                Line((-7, 0), (-7, 1.5))
            make_face()
        # OneSide extrude, distance=3
        extrude(amount=3)

        # Sketch4 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 8 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 3, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.0000000596, perimeter: 6.0000000894
            with BuildLine():
                Line((-6.0000000894, 1.0000000149), (-6.0000000894, -1.0000000149))
                Line((-7.0000001043, 1.0000000149), (-6.0000000894, 1.0000000149))
                Line((-7.0000001043, -1.0000000149), (-7.0000001043, 1.0000000149))
                Line((-6.0000000894, -1.0000000149), (-7.0000001043, -1.0000000149))
            make_face()
            # Profile area: 2.0000000596, perimeter: 6.0000000894
            with BuildLine():
                Line((6.0000000894, -1.0000000149), (7.0000001043, -1.0000000149))
                Line((7.0000001043, -1.0000000149), (7.0000001043, 1.0000000149))
                Line((7.0000001043, 1.0000000149), (6.0000000894, 1.0000000149))
                Line((6.0000000894, 1.0000000149), (6.0000000894, -1.0000000149))
            make_face()
        # OneSide extrude, distance=-2
        extrude(amount=-2, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical rod or shaft with a smooth, uniform circular cross-section and tapered or rounded ends, featuring a simple elongated tubular design typical of a connector pin, dowel, or support rod.
def model_41321_43c99300_0000():
    """Model: body"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.047630503, perimeter: 3.7504333099
            with BuildLine():
                CenterArc((0, 0), 0.31115, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.28575, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.55372
        extrude(amount=0.55372)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.55372, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2244916815, perimeter: 4.5324385532
            with BuildLine():
                CenterArc((0, 0), 0.41021, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.31115, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.047630503, perimeter: 3.7504333099
            with BuildLine():
                CenterArc((0, 0), 0.31115, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.28575, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=10.3886
        extrude(amount=10.3886, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical tube or pipe with rounded ends, featuring a smooth, uniform diameter throughout its length and a slight diagonal orientation.
def model_41321_43c99300_0009():
    """Model: pusher"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0518108397, perimeter: 3.2636749441
            with BuildLine():
                CenterArc((2.4238933762, -3.0415450409), 0.27559, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((2.4238933762, -3.0415450409), 0.24384, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.17272
        extrude(amount=0.17272)

        # Sketch2 -> Extrude2 (NewBody)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.17272, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0320081728, perimeter: 2.9267528116
            with BuildLine():
                CenterArc((-2.4238933762, 3.0415450409), 0.24384, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-2.4238933762, 3.0415450409), 0.2219671772, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=2.25298
        extrude(amount=2.25298)
    return part.part


# Description: This is a cylindrical connector or coupling with a curved band clamp, featuring a solid cylindrical body on the right, a flexible mesh or perforated band wrapping around the left side, and a central slot or opening for assembly or connection purposes.
def model_41353_16ac5969_0018():
    """Model: 4mmBolt6"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.3848451001, perimeter: 2.1991148575
            with Locations((5, 5)):
                Circle(0.35)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.2), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((5, 5)):
                Circle(0.25)
        # OneSide extrude, distance=0.4
        extrude(amount=0.4, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical sleeve or spacer with a slightly larger diameter head on one end and a long hollow tubular body, featuring what appears to be text or markings embossed on its surface.
def model_41353_16ac5969_0019():
    """Model: 19mmBolt2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.3848451001, perimeter: 2.1991148575
            with Locations((-2, 5)):
                Circle(0.35)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.2), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((-2, 5)):
                Circle(0.25)
        # OneSide extrude, distance=1.9
        extrude(amount=1.9, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical shaft or pin with a larger circular flange or head on one end and a smaller diameter rod extending from it, featuring what appears to be a slot or groove detail on the cylindrical body.
def model_41353_16ac5969_0021():
    """Model: 19mmBolt"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            Circle(0.25)
        # OneSide extrude, distance=1.9
        extrude(amount=1.9)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.3848451001, perimeter: 2.1991148575
            Circle(0.35)
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2, mode=Mode.ADD)
    return part.part


# Description: This is a flat parallelogram-shaped plate or panel with a simple rectangular form tilted at an angle, featuring clean edges and a uniform thickness with no holes, slots, or additional features.
def model_41465_3c18418c_0000():
    """Model: right side"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 387.096, perimeter: 309.88
            with BuildLine():
                Line((-228.5999965668, -0.0000022888), (-228.5999965668, 152.3999977112))
                Line((-228.5999965668, 152.3999977112), (-231.1399965668, 152.3999977112))
                Line((-231.1399965668, 152.3999977112), (-231.1399965668, -0.0000022888))
                Line((-231.1399965668, -0.0000022888), (-228.5999965668, -0.0000022888))
            make_face()
        # OneSide extrude, distance=91.44
        extrude(amount=91.44)
    return part.part


# Description: This is a bolt or screw featuring a spherical head on one end and a cylindrical shaft that tapers slightly toward the opposite end, with a smooth, rounded geometry throughout.
def model_41473_c2137170_0000():
    """Model: headtube_pin"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.1309733553, perimeter: 3.7699111843
            with Locations((10, 10)):
                Circle(0.6)
        # OneSide extrude, distance=6.5
        extrude(amount=6.5)

        # Sketch3 -> Extrude2 (NewBody)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 2.0106192983, perimeter: 10.0530964915
            with BuildLine():
                CenterArc((-10, 10), 1, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-10, 10), 0.6, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


# Description: This is a torus-shaped ring or spacer with a hollow center and textured surface featuring linear grooves or ridges running across its outer and inner surfaces.
def model_41473_c2137170_0005():
    """Model: Component7"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 28.2743338823, perimeter: 18.8495559215
            with Locations((5, 10)):
                Circle(3)
        # OneSide extrude, distance=1.2
        extrude(amount=1.2)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.0000001788, -0.0000000045, 1.2), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 19.6349540849, perimeter: 15.7079632679
            with Locations((4.9999998212, 10.0000000045)):
                Circle(2.5)
        # OneSide extrude, distance=-1.2
        extrude(amount=-1.2, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a toroidal (ring-shaped) component with a circular cross-section, featuring a uniform hollow center and textured or patterned surface finish on the outer diameter.
def model_41473_c2137170_0006():
    """Model: Component8"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 28.2743338823, perimeter: 18.8495559215
            with Locations((5, 1)):
                Circle(3)
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 19.6349540849, perimeter: 15.7079632679
            with Locations((5, 1)):
                Circle(2.5)
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a toroidal (doughnut-shaped) ring featuring a smooth, curved body with a textured or knurled surface pattern on portions of the outer circumference.
def model_41473_c2137170_0007():
    """Model: Component9"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 34.2119439976, perimeter: 20.7345115137
            with Locations((4, -7)):
                Circle(3.3)
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.000001812, 0.0000001503, 1), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 19.6349540849, perimeter: 15.7079632679
            with Locations((3.999998188, -7.0000001503)):
                Circle(2.5)
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a pentahedron or wedge-shaped container/bracket featuring a trapezoidal profile with a large rectangular face, angled side panels, and internal structural ribbing or bracing elements visible through the translucent geometry.
def model_41501_b627682a_0005():
    """Model: Base v20"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 10 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 35.0000000317, perimeter: 69.9999999925
            with BuildLine():
                Line((-8, 8.5), (-8, -0.5))
                Line((-8, -0.5), (2.5, -0.5))
                Line((2.5, -0.5), (2.5, 8.5))
                Line((2.5, 8.5), (-8, 8.5))
            make_face()
            with BuildLine():
                Line((1.5, 7.5), (1.5, 0.5))
                Line((1.5, 0.5), (-7, 0.5000000075))
                Line((-7, 0.5000000075), (-7, 7.5))
                Line((-7, 7.5), (1.5, 7.5))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=10
        extrude(amount=10)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -0.5000000013), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 1.5200000453, perimeter: 5.4000000805
            with BuildLine():
                Line((3.4000000507, 1.2000000179), (1.5000000224, 1.2000000179))
                Line((3.4000000507, 2.0000000298), (3.4000000507, 1.2000000179))
                Line((1.5000000224, 2.0000000298), (3.4000000507, 2.0000000298))
                Line((1.5000000224, 1.2000000179), (1.5000000224, 2.0000000298))
            make_face()
        # OneSide extrude, distance=-0.8
        extrude(amount=-0.8, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical duct or pipe component with an elongated hexagonal cross-section, featuring multiple rectangular slots or vanes along its upper surface and angled end faces, designed likely for airflow direction, ventilation, or structural reinforcement.
def model_41501_b627682a_0006():
    """Model: Wall Bracket v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.0053097089, perimeter: 5.913274211
            with BuildLine():
                Line((-2.5000000373, 1.0000000149), (-2.5000000373, -1.0000000149))
                Line((-2.5000000373, -1.0000000149), (-2.0000000298, -1.0000000149))
                Line((-2.0000000298, -1.0000000149), (-2.0000000298, -0.8000000119))
                CenterArc((-2.0000000298, 0), 0.8000000119, -90, 180)
                Line((-2.0000000298, 1.0000000149), (-2.0000000298, 0.8000000119))
                Line((-2.5000000373, 1.0000000149), (-2.0000000298, 1.0000000149))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 0.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0314159275, perimeter: 0.6283185401
            with Locations((1.7000000253, 0)):
                Circle(0.1000000015)
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a rounded rectangular bar or shaft with a cylindrical shape, featuring smoothly rounded ends and a uniform diameter throughout its length.
def model_41501_b627682a_0007():
    """Model: Beam No.1 v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.5924972893, perimeter: 10.9549156435
            with BuildLine():
                CenterArc((-1.9999567073, 0), 0.1519933467, 90, 180)
                Line((-1.9999567073, -0.1519933467), (2.9999999329, -0.1519933467))
                CenterArc((2.9999999329, 0), 0.1519933467, -90, 180)
                Line((-1.9999567073, 0.1519933467), (2.9999999329, 0.1519933467))
            make_face()
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0314159275, perimeter: 0.6283185401
            with Locations((1.9999567073, 0)):
                Circle(0.1000000015)
            # Profile area: 0.0314159275, perimeter: 0.6283185401
            with Locations((-2.9999999329, 0)):
                Circle(0.1000000015)
        # OneSide extrude, distance=-0.1
        extrude(amount=-0.1, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical socket head cap screw featuring a long shaft with a hexagonal socket in the head and a notch or slot on one side of the head.
def model_41501_b627682a_0014():
    """Model: Pivot v7"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0314159251, perimeter: 0.6283185167
            Circle(0.0999999978)
        # OneSide extrude, distance=0.7
        extrude(amount=0.7)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.7, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0392699117, perimeter: 1.5707963268
            with BuildLine():
                CenterArc((0, 0), 0.1500000022, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.0999999978, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0314159251, perimeter: 0.6283185167
            Circle(0.0999999978)
        # OneSide extrude, distance=0.15
        extrude(amount=0.15, mode=Mode.ADD)
    return part.part


# Description: This is a rectangular duct or channel component with a long, elongated box-like shape featuring an open top edge and internal ribbing or reinforcement structure running along its length.
def model_41508_b9593bb5_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 75, perimeter: 40
            with BuildLine():
                Line((10.7198661589, -1.1416157892), (-4.2801338411, -1.1416157892))
                Line((10.7198661589, 3.8583842108), (10.7198661589, -1.1416157892))
                Line((-4.2801338411, 3.8583842108), (10.7198661589, 3.8583842108))
                Line((-4.2801338411, -1.1416157892), (-4.2801338411, 3.8583842108))
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 7 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(2, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 5.9828384084, perimeter: 58.4100403119
            with BuildLine():
                Line((9.5, 2.5), (-3, 2.5))
                Line((-3, 2.5), (-3, 0))
                Line((-3, 0), (9.5, 0))
                Line((9.5, 0), (9.5, 2.5))
            make_face()
            with BuildLine():
                Line((9.3211318597, 0.1972893123), (9.3211318597, 2.2916802189))
                Line((-2.7991858869, 0.1972893123), (9.3211318597, 0.1972893123))
                Line((-2.7991858869, 2.2722877106), (-2.7991858869, 0.1972893123))
                Line((9.3211318597, 2.2916802189), (-2.7991858869, 2.2722877106))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)
    return part.part


# Description: This is an elongated rectangular duct or channel with a tapered hexagonal head at one end, featuring a longitudinal slot or opening along its length and a protruding attachment point or flange at the opposite end.
def model_41508_c18d22f2_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 4 constraints, 29 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 31.5030619379, perimeter: 74.8901044967
            with BuildLine():
                Line((9.2114557224, 0.0964816429), (-5.2885442776, 0.0964816429))
                Line((9.2114557224, 2.6211816429), (9.2114557224, 0.0964816429))
                Line((-5.2885442776, 2.6211816429), (9.2114557224, 2.6211816429))
                Line((-5.2885442776, 0.0964816429), (-5.2885442776, 2.6211816429))
            make_face()
            with BuildLine():
                CenterArc((7.5, 1), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((6.5, 1), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((5.5, 1), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((4.5, 1), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((3.5, 1), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((2.5, 1), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1.5, 1), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0.5, 1), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-0.5, 1), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-1.5, 1), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-2.5, 1), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-3.5, 1), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-4.5, 1), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((7.5, 2), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((6.5, 2), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((5.5, 2), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((4.5, 2), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((3.5, 2), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((2.5, 2), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1.5, 2), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0.5, 2), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-0.5, 2), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-1.5, 2), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-2.5, 2), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-3.5, 2), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-4.5, 2), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=2
        extrude(amount=2)

        # Sketch2 -> Extrude2 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.9312222479, perimeter: 6.0404904196
            with BuildLine():
                CenterArc((2.7331076317, 1.23765), 1.2902554238, -78.0620445277, 156.1240890554)
                Line((3, 2.5), (3, -0.0247))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


# Description: This is a dark blue rectangular extrusion or channel with a hollow interior cross-section, featuring vertical grooves or flutes along its sides and open ends at the top and bottom.
def model_41595_e15895be_0005():
    """Model: Leg"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.27, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 135.4836, perimeter: 52.07
            with BuildLine():
                Line((-118.1458616393, 80.9863975357), (-118.1458616393, 61.9363975357))
                Line((-118.1458616393, 61.9363975357), (-113.7008616393, 61.9363975357))
                Line((-109.2558616393, 77.1763975357), (-113.7008616393, 61.9363975357))
                Line((-109.2558616393, 80.9863975357), (-109.2558616393, 77.1763975357))
                Line((-118.1458616393, 80.9863975357), (-109.2558616393, 80.9863975357))
            make_face()
        # OneSide extrude, distance=0.635
        extrude(amount=0.635)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.905, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 24.2523036458, perimeter: 77.6816666667
            with BuildLine():
                Line((-109.4410699726, 76.5413975357), (-109.2558616393, 77.1763975357))
                Line((-108.6208616393, 76.5413975357), (-109.4410699726, 76.5413975357))
                Line((-108.6208616393, 76.5413975357), (-108.6208616393, 81.6213975357))
                Line((-108.6208616393, 81.6213975357), (-118.7808616393, 81.6213975357))
                Line((-118.7808616393, 81.6213975357), (-118.7808616393, 61.3013975357))
                Line((-114.3358616393, 61.3013975357), (-118.7808616393, 61.3013975357))
                Line((-114.3358616393, 61.9363975357), (-114.3358616393, 61.3013975357))
                Line((-118.1458616393, 61.9363975357), (-114.3358616393, 61.9363975357))
                Line((-118.1458616393, 80.9863975357), (-118.1458616393, 61.9363975357))
                Line((-109.2558616393, 80.9863975357), (-118.1458616393, 80.9863975357))
                Line((-109.2558616393, 77.1763975357), (-109.2558616393, 80.9863975357))
            make_face()
            # Profile area: 61.2313963542, perimeter: 60.80125
            with BuildLine():
                Line((-109.2558616393, 77.1763975357), (-109.2558616393, 80.9863975357))
                Line((-109.2558616393, 80.9863975357), (-118.1458616393, 80.9863975357))
                Line((-118.1458616393, 80.9863975357), (-118.1458616393, 61.9363975357))
                Line((-118.1458616393, 61.9363975357), (-114.3358616393, 61.9363975357))
                Line((-114.3358616393, 63.2063975357), (-114.3358616393, 61.9363975357))
                Line((-116.8758616393, 63.2063975357), (-114.3358616393, 63.2063975357))
                Line((-116.8758616393, 76.5413975357), (-116.8758616393, 63.2063975357))
                Line((-109.4410699726, 76.5413975357), (-116.8758616393, 76.5413975357))
                Line((-109.4410699726, 76.5413975357), (-109.2558616393, 77.1763975357))
            make_face()
        # OneSide extrude, distance=71.12
        extrude(amount=71.12, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical bushing or sleeve with a central bore, featuring a curved, bulbous outer profile with mesh-textured surfaces and what appears to be radial slots or vents around its circumference.
def model_41599_f66b4e5b_0002():
    """Model: hanger part3 v2"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 2.5446901252, perimeter: 5.6548668607
            Circle(0.9000000134)
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch3 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.7853981868, perimeter: 3.1415927004
            Circle(0.5000000075)
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a circular disc or wheel with a shallow dome/convex top surface, featuring a central hub, radial ribbing or spoke-like internal reinforcement patterns, and a flat peripheral flange or rim around the base.
def model_41599_f66b4e5b_0005():
    """Model: new 1 v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 12.5663706144, perimeter: 12.5663706144
            Circle(2)
        # OneSide extrude, distance=0.4
        extrude(amount=0.4)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.4, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            Circle(0.5)
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical mesh or perforated filter basket with an open top, featuring a slotted or latticed pattern on its curved walls and a recessed internal surface, designed for filtering or straining applications.
def model_41599_f66b4e5b_0008():
    """Model: light holder v5"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.9503317777, perimeter: 3.4557519189
            Circle(0.55)
        # OneSide extrude, distance=0.6
        extrude(amount=0.6)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.6, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            Circle(0.5)
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical shell or sleeve with an open top, featuring a curved, tapered form that widens slightly toward the upper rim, and constructed from a mesh or wireframe material indicating a thin-walled design.
def model_41599_f66b4e5b_0009():
    """Model: light string insert v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0078539816, perimeter: 0.3141592654
            Circle(0.05)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)

        # Sketch2 -> Extrude2 (Cut)
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
            # Profile area: 0.0078539816, perimeter: 0.3141592654
            Circle(0.05)
        # OneSide extrude, distance=-0.05
        extrude(amount=-0.05, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical shaft or rod with a stepped diameter, featuring a larger main body that transitions to a smaller diameter section, commonly used as a mechanical connector or drive shaft component.
def model_41648_577daf16_0009():
    """Model: Handle"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 3 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            Circle(0.2)
        # OneSide extrude, distance=2.8
        extrude(amount=2.8)

        # Sketch2 -> Extrude2 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 3 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.2031136543, perimeter: 3.2892556093
            with BuildLine():
                CenterArc((0, 0), 0.3235012893, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-13
        extrude(amount=-13)
    return part.part


# Description: This is a three-way connector or junction piece with a cross-shaped body featuring three cylindrical ports extending outward at 120-degree angles, each with threaded or ribbed openings for fluid/gas flow or mechanical attachment.
def model_41648_577daf16_0010():
    """Model: Screw"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 3 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.6104991106, perimeter: 10.2245917149
            with BuildLine():
                CenterArc((-1, 0), 0.2, 94.5129914499, 191.3414857828)
                CenterArc((-0.909902562, -0.9073478127), 0.7158348234, -4.2476802197, 97.0869532285)
                CenterArc((0, -1.0000000149), 0.2, 168.5707158559, 200.5113980184)
                CenterArc((0.9249817778, -0.9249179518), 0.7287892483, 86.6342406523, 96.78861884)
                CenterArc((1.0000000149, 0), 0.200000003, -99.2739903805, 205.528157064)
                CenterArc((0.8750274607, 0.8751372515), 0.6866064693, 174.2947175631, 101.4723095962)
                CenterArc((0, 1), 0.2, -16.4411809236, 199.0034780433)
                CenterArc((-0.9848352896, 0.9838399329), 0.7850684397, -92.2558500634, 92.7827096639)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.6
        extrude(amount=0.6)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        # Sketch has 3 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.2513274048, perimeter: 4.2904273246
            with BuildLine():
                CenterArc((0, 0), 0.4, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.2828427167, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0549778789, perimeter: 3.3479495285
            with BuildLine():
                CenterArc((0, 0), 0.2828427167, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            Circle(0.25)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)

        # Sketch1 -> Extrude3 (Join)
        # Sketch on XY construction plane
        # Sketch has 3 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            Circle(0.25)
        # OneSide extrude, distance=-1.5
        extrude(amount=-1.5, mode=Mode.ADD)

        # Sketch1 -> Extrude4 (Join)
        # Sketch on XY construction plane
        # Sketch has 3 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0549778789, perimeter: 3.3479495285
            with BuildLine():
                CenterArc((0, 0), 0.2828427167, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.4
        extrude(amount=-0.4, mode=Mode.ADD)
    return part.part


# Description: This is a rectangular steel rod or bar with an elongated prismatic shape, featuring a tapered or beveled end on one side and a flat rectangular cross-section throughout its length.
def model_41650_9417da80_0006():
    """Model: Base v12"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.0400000608, perimeter: 8.0000001192
            with BuildLine():
                Line((0.3000000045, -1.7000000253), (0.3000000045, 1.7000000253))
                Line((0.3000000045, 1.7000000253), (-0.3000000045, 1.7000000253))
                Line((-0.3000000045, 1.7000000253), (-0.3000000045, -1.7000000253))
                Line((-0.3000000045, -1.7000000253), (0.3000000045, -1.7000000253))
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0078539816, perimeter: 0.3141592654
            with Locations((0, -1.1299999747)):
                Circle(0.05)
        # OneSide extrude, distance=-0.27
        extrude(amount=-0.27, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a lightweight, elongated oval disc with a central black web structure featuring multiple white oval cutouts for weight reduction, flanged edges with radial ribbing, and blue-highlighted structural reinforcement areas.
def model_41654_b616fab1_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 106.0287520587, perimeter: 47.1238898038
            with BuildLine():
                CenterArc((0, 0), 6, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 8 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            with Locations((0, -4)):
                Circle(1)
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            with Locations((4, 0)):
                Circle(1)
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            with Locations((0, 4)):
                Circle(1)
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            with Locations((-4, 0)):
                Circle(1)
        # Symmetric extrude, each_side=6
        extrude(amount=6, both=True, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a torus (donut-shaped ring) with a smooth, uniformly curved cross-section and a central circular hole, featuring a textured or mesh-like surface finish rendered in dark blue and gray tones.
def model_41672_cf87e0b6_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.0106192646, perimeter: 10.0530965477
            with BuildLine():
                CenterArc((0, 0), 1, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.6000000089, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)

        # Sketch3 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0054340402, perimeter: 0.3190100115
            with BuildLine():
                CenterArc((0, 0), 1, -90, 3.2016077581)
                Line((0, -1), (0, -1.1084803268))
                Line((0.0439706581, -1.1084803268), (0, -1.1084803268))
                Line((0.0558495219, -0.9984391974), (0.0439706581, -1.1084803268))
            make_face()
            # Profile area: 0.0054340402, perimeter: 0.3190100115
            with BuildLine():
                Line((0, -1), (0, -1.1084803268))
                CenterArc((0, 0), 1, -93.2016077581, 3.2016077581)
                Line((-0.0439706581, -1.1084803268), (-0.0558495219, -0.9984391974))
                Line((0, -1.1084803268), (-0.0439706581, -1.1084803268))
            make_face()
        # OneSide extrude, distance=-0.1
        extrude(amount=-0.1, mode=Mode.ADD)
    return part.part


# Description: This is a disc or washer-like component with an oblate, flattened spheroid shape featuring a central hole and radial ribbing or corrugated surface pattern that extends from the center outward.
def model_41672_d9512d5c_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude3 (NewBody)
        # Sketch on XZ construction plane
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 78.5398163397, perimeter: 31.4159265359
            with Locations((5, -2.5)):
                Circle(5)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch3 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            with Locations((-5, 2.5)):
                Circle(1)
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a knob or handle assembly with a cylindrical main body featuring a larger rounded head on one end and a smaller diameter shaft or post on the other end, commonly used as a control knob or grip component.
def model_41672_f0d8843f_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0314159275, perimeter: 0.6283185401
            Circle(0.1000000015)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on YZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0078539816, perimeter: 0.3141592654
            with Locations((-0.1000000015, 0)):
                Circle(0.05)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3, mode=Mode.ADD)
    return part.part


# Description: This is an oval or elliptical-shaped enclosure or housing with a curved, streamlined body featuring a raised head or connector element at one end and a smooth, tapered profile.
def model_41672_ffe3d8cc_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with BuildLine():
                CenterArc((0, 0), 0.5, 95.7391705631, 348.5216588739)
                CenterArc((0, 0), 0.5, 84.2608294369, 11.4783411261)
            make_face()
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0113779097, perimeter: 0.4350070731
            with BuildLine():
                Line((0.0627725166, -0.4960439609), (0.0499999989, -0.5999999866))
                CenterArc((0, 0), 0.5, -97.180400456, 14.3926322992)
                Line((-0.0499999989, -0.5999999866), (-0.0624969235, -0.4960787584))
                Line((0.0499999989, -0.5999999866), (-0.0499999989, -0.5999999866))
            make_face()
        # OneSide extrude, distance=-0.1
        extrude(amount=-0.1, mode=Mode.ADD)
    return part.part


# Description: A solar panel with a blue photovoltaic surface and dark frame, accompanied by a separate cylindrical mounting rod for installation.
def model_41680_49185107_0001():
    """Model: Ramp Brace"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 451.612, perimeter: 187.96
            with BuildLine():
                Line((-211.3588514632, -64.1883343325), (-216.4388514632, -64.1883343325))
                Line((-211.3588514632, 24.7116656675), (-211.3588514632, -64.1883343325))
                Line((-216.4388514632, 24.7116656675), (-211.3588514632, 24.7116656675))
                Line((-216.4388514632, -64.1883343325), (-216.4388514632, 24.7116656675))
            make_face()
        # OneSide extrude, distance=12.7
        extrude(amount=12.7)

        # Sketch2 -> Extrude2 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 15695.77506, perimeter: 530.9108
            with BuildLine():
                Line((216.4631156598, -50.5812384906), (39.9077156598, -50.5812384906))
                Line((216.4631156598, 38.3187615094), (216.4631156598, -50.5812384906))
                Line((39.9077156598, 38.3187615094), (216.4631156598, 38.3187615094))
                Line((39.9077156598, -50.5812384906), (39.9077156598, 38.3187615094))
            make_face()
        # OneSide extrude, distance=2.54
        extrude(amount=2.54)
    return part.part


# Description: This is a cylindrical battery or power cell with a tapered pointed top and vertical ribbed detailing along its body, featuring a dark gray finish with blue accents.
def model_41681_2586b16d_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.7321908424, perimeter: 5.7035697113
            with BuildLine():
                CenterArc((-0.381, 1.1447625727), 0.0635, 0, 108.40847953)
                CenterArc((0, 0), 1.2700000405, 108.40847953, 143.18304094)
                CenterArc((-0.381, -1.1447625727), 0.0635, -108.40847953, 108.40847953)
                Line((-0.3175, 1.1447625727), (-0.3175, -1.1447625727))
            make_face()
        # OneSide extrude, distance=7.14375
        extrude(amount=7.14375)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-0.3175, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0791730436, perimeter: 0.9974556675
            with Locations((0, 6.6675)):
                Circle(0.15875)
            # Profile area: 0.0791730436, perimeter: 0.9974556675
            with Locations((0, 0.47625)):
                Circle(0.15875)
        # TwoSides extrude (symmetric), distance=2.54
        extrude(amount=2.54, both=True, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a curved bracket or support component with an irregular, organic shape featuring multiple notched cutouts along its upper edges, internal ribbed reinforcement patterns, and a complex bent geometry designed for structural support or mechanical assembly.
def model_41685_df8ac866_0001():
    """Model: Connector"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 8 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 26.7766494372, perimeter: 21.7571378947
            with BuildLine():
                Line((0, 0), (5, 0))
                CenterArc((0, 0), 5, 0, 40.4151144481)
                CenterArc((3.5355339059, 3.5355339059), 0.4, 137.292442776, 175.4151144481)
                CenterArc((0, 0), 5, 49.5848855519, 35.8302288962)
                CenterArc((0, 5), 0.4, -177.707557224, 175.4151144481)
                CenterArc((0, 0), 5, 94.5848855519, 30.4151144481)
                Line((0, 0), (-2.8678821818, 4.0957602214))
            make_face()
        # Symmetric extrude, each_side=2
        extrude(amount=2, both=True)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 19, perimeter: 17.6
            with BuildLine():
                Line((1.9, 0.1), (-1.9, 0.1))
                Line((1.9, 5.1), (1.9, 0.1))
                Line((-1.9, 5.1), (1.9, 5.1))
                Line((-1.9, 0.1), (-1.9, 5.1))
            make_face()
        # OneSide extrude, distance=5
        extrude(amount=5, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a curved wing or hydrofoil component with an aerodynamic/hydrodynamic profile, featuring a tapered rectangular base that transitions into a curved, textured upper surface with diagonal ribbing or reinforcement patterns.
def model_41685_df8ac866_0005():
    """Model: Back Wheel Brake"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 8 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.575, perimeter: 9.7
            with BuildLine():
                Line((-3.4648232278, 3.4648232278), (-6.6468037432, 0.2828427125))
                Line((-3.7123106012, 3.7123106012), (-3.4648232278, 3.4648232278))
                Line((-6.8942911166, 0.5303300859), (-3.7123106012, 3.7123106012))
                Line((-6.6468037432, 0.2828427125), (-6.8942911166, 0.5303300859))
            make_face()
            # Profile area: 3.255148138, perimeter: 19.3008465031
            with BuildLine():
                CenterArc((0, 0), 4.9, 30, 105)
                Line((4.2435244785, 2.45), (4.5466333699, 2.625))
                CenterArc((0, 0), 5.25, 30, 105)
                Line((-3.7123106012, 3.7123106012), (-3.4648232278, 3.4648232278))
            make_face()
        # Symmetric extrude, each_side=1
        extrude(amount=1, both=True)
    return part.part


# Description: This is an elongated, tapered dark blue solid with a pointed top end and a faceted/geometric surface treatment, featuring a narrower upper section and wider lower body with subtle angular surfaces and edges.
def model_41685_df8ac866_0006():
    """Model: Inner Deck/ Staff Connector"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 4 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 40.2650658318, perimeter: 37.4
            with BuildLine():
                Line((0, 0), (0, 5.2))
                Line((-7.7432818907, 16.2585525979), (0, 5.2))
                Line((-7.7432818907, 11.0585525979), (-7.7432818907, 16.2585525979))
                Line((0, 0), (-7.7432818907, 11.0585525979))
            make_face()
        # Symmetric extrude, each_side=1.9
        extrude(amount=1.9, both=True)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1.9), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((-2.0075175272, 5.467032155)):
                Circle(0.25)
        # Symmetric extrude, each_side=10
        extrude(amount=10, both=True, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a clamping or gripping tool with an elongated cylindrical handle and a forked end featuring two curved prongs or jaws for grasping or holding objects.
def model_41685_df8ac866_0014():
    """Model: Configuration handle"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 8 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.9066700709, perimeter: 9.1493724673
            with BuildLine():
                Line((-1.499485704, 0), (-1.5, 0))
                CenterArc((-1.499742852, 2.0008061093), 2.0008061258, -126.796080664, 36.7887168841)
                CenterArc((-1.499742852, 2.0008061093), 2.0008061258, -126.93097854, 0.134897876)
                Line((-2.7620174837, 0.321505918), (-2.7019322328, 0.4014419088))
                CenterArc((-1.499742852, 2.0008061093), 2.1008061258, -126.93097854, 49.0100432341)
                CenterArc((-1.0313287654, -1.3523898337), 1.2992213335, 64.1738304059, 27.0962113431)
                CenterArc((0, 0), 0.5, -158.5388818433, 287.213508062)
                CenterArc((-1.499742852, 2.0008061093), 2.0008061258, -89.9926362202, 36.3918613447)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=0.5
        extrude(amount=0.5, both=True)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY) as sk:
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            Circle(0.25)
        # TwoSides extrude, along=1, against=-4.2
        extrude(amount=1, mode=Mode.ADD)
        extrude(sk.sketch, amount=-4.2, mode=Mode.ADD)
    return part.part


# Description: This is a pulley or wheel assembly with a toroidal (donut-shaped) main body featuring two concentric circular grooves or channels around its circumference, a central hub on one side, and multiple relief holes or slots distributed across its surface for weight reduction and mounting purposes.
def model_41693_a737c734_0003():
    """Model: Stopper"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 5.0799999237), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0506707479, perimeter: 0.797964534
            with Locations((1.7780000567, -1.0160000324)):
                Circle(0.127)
        # OneSide extrude, distance=0.254
        extrude(amount=0.254)

        # Sketch2 -> Extrude2 (NewBody)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 5.3339999237), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.2660214265, perimeter: 2.792875869
            with BuildLine():
                CenterArc((1.7780000567, -1.0160000324), 0.3175, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((1.7780000567, -1.0160000324), 0.127, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.127
        extrude(amount=0.127)
    return part.part


# Description: This is a space satellite or spacecraft component featuring a flat rectangular solar panel or antenna array (light blue) mounted on top of a cylindrical body (dark gray) with angular structural supports, designed for orbital deployment with prominent geometric faceting for thermal and structural efficiency.
def model_41698_900d863d_0008():
    """Model: Tail Fin 2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.9000000268, perimeter: 4.4439089577
            with BuildLine():
                Line((0, 12.2000001818), (0.9000000134, 12.4000001848))
                Line((0.9000000134, 12.8000001907), (0.9000000134, 12.4000001848))
                Line((-0.9000000134, 12.8000001907), (0.9000000134, 12.8000001907))
                Line((-0.9000000134, 12.4000001848), (-0.9000000134, 12.8000001907))
                Line((0, 12.2000001818), (-0.9000000134, 12.4000001848))
            make_face()
        # OneSide extrude, distance=3.6
        extrude(amount=3.6)

        # Sketch1 -> Extrude2 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.9000000268, perimeter: 4.4439089577
            with BuildLine():
                Line((0, 12.2000001818), (0.9000000134, 12.4000001848))
                Line((0.9000000134, 12.8000001907), (0.9000000134, 12.4000001848))
                Line((-0.9000000134, 12.8000001907), (0.9000000134, 12.8000001907))
                Line((-0.9000000134, 12.4000001848), (-0.9000000134, 12.8000001907))
                Line((0, 12.2000001818), (-0.9000000134, 12.4000001848))
            make_face()
        # OneSide extrude, distance=3.4
        extrude(amount=3.4, mode=Mode.SUBTRACT)

        # Sketch2 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -12.8000001907), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.1861307072, perimeter: 1.5490457406
            with BuildLine():
                CenterArc((0, 3.2000000477), 0.25, 126.8699158597, 286.2601682806)
                Line((0.1500000636, 3.4), (-0.1500000636, 3.4))
            make_face()
        # OneSide extrude, distance=0.6
        extrude(amount=0.6, mode=Mode.ADD)
    return part.part


# Description: This is a tapered metal punch or drift pin with a flat striking head at the top and a sharp conical point at the bottom, used for aligning, driving, or removing pins and fasteners.
def model_41708_3a74f048_0009():
    """Model: toothpick v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.7853700081, perimeter: 6.4658394343
            with BuildLine():
                Line((-0.2540000081, -0.5080000162), (-0.1385971413, -1.9851567582))
                CenterArc((-0.0879514645, -1.9812000648), 0.0508, -175.5328410806, 77.2724490583)
                CenterArc((-0.1025485517, -1.9812000648), 0.0508, -81.7396079777, 77.2724490583)
                Line((-0.0519028749, -1.9851567582), (0.0634999919, -0.5080000162))
                Line((0.0634999919, 1.0160000324), (0.0634999919, -0.5080000162))
                Line((-0.2540000081, 1.0160000324), (0.0634999919, 1.0160000324))
                Line((-0.2540000081, -0.5080000162), (-0.2540000081, 1.0160000324))
            make_face()
        # OneSide extrude, distance=0.0635
        extrude(amount=0.0635)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.0635, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.10080625, perimeter: 1.27
            with BuildLine():
                Line((-0.0634999919, -0.6985000324), (0.2540000081, -0.6985000324))
                Line((-0.0634999919, -1.0160000324), (-0.0634999919, -0.6985000324))
                Line((0.2540000081, -1.0160000324), (-0.0634999919, -1.0160000324))
                Line((0.2540000081, -0.6985000324), (0.2540000081, -1.0160000324))
            make_face()
        # OneSide extrude, distance=0.0762
        extrude(amount=0.0762, mode=Mode.ADD)
    return part.part


# Description: This is a rectangular sheet metal box or tray with a parallelogram profile, featuring an open top, slanted sides, and a recessed internal lip or flange along the upper edges.
def model_41714_1d49f4d1_0005():
    """Model: birdhouse_sign"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 5 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 6.5806322285, perimeter: 34.5440011997
            with BuildLine():
                Line((-8.8900002837, 3.0480000973), (-8.8900002837, 6.0960001945))
                Line((-2.5400000811, 3.0480000973), (-8.8900002837, 3.0480000973))
                Line((-2.5400000811, 6.0960001945), (-2.5400000811, 3.0480000973))
                Line((-8.8900002837, 6.0960001945), (-2.5400000811, 6.0960001945))
            make_face()
            with BuildLine():
                Line((-2.9210000811, 3.4290000973), (-8.5090002837, 3.4290000973))
                Line((-8.5090002837, 3.4290000973), (-8.5090002837, 5.7150001945))
                Line((-8.5090002837, 5.7150001945), (-2.9210000811, 5.7150001945))
                Line((-2.9210000811, 5.7150001945), (-2.9210000811, 3.4290000973))
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 12.7741690068, perimeter: 15.7480005999
            with BuildLine():
                Line((-2.9210000811, 5.7150001945), (-2.9210000811, 3.4290000973))
                Line((-8.5090002837, 5.7150001945), (-2.9210000811, 5.7150001945))
                Line((-8.5090002837, 3.4290000973), (-8.5090002837, 5.7150001945))
                Line((-2.9210000811, 3.4290000973), (-8.5090002837, 3.4290000973))
            make_face()
        # OneSide extrude, distance=0.762
        extrude(amount=0.762)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 12.7569243155, perimeter: 15.6804617432
            with BuildLine():
                Line((8.4828915333, 5.7242242308), (2.9471088315, 5.7242242308))
                Line((2.9471088315, 5.7242242308), (2.9471088315, 3.419776061))
                Line((2.9471088315, 3.419776061), (8.4828915333, 3.419776061))
                Line((8.4828915333, 3.419776061), (8.4828915333, 5.7242242308))
            make_face()
        # OneSide extrude, distance=-0.635
        extrude(amount=-0.635, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a hollow rectangular frame or box structure with an open center, featuring thick walls with beveled or angled edges and dark edges that suggest depth and a three-dimensional construction.
def model_41716_d55164d4_0006():
    """Model: Roof 1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 15.8833641236, 15.8643416122), x_dir=(1, 0, 0), z_dir=(0, 0.7075303367, 0.7066829719))):
            # Profile area: 198.3867, perimeter: 100.33
            with BuildLine():
                Line((0.5, 11.1273039923), (0.5, -4.1126960077))
                Line((18.28, -4.1126960077), (0.5, -4.1126960077))
                Line((18.28, 11.1273039923), (18.28, -4.1126960077))
                Line((0.5, 11.1273039923), (18.28, 11.1273039923))
            make_face()
            with BuildLine():
                Line((13.2, 8.2698039923), (5.58, 8.2698039923))
                Line((13.2, -1.2551960077), (13.2, 8.2698039923))
                Line((5.58, -1.2551960077), (13.2, -1.2551960077))
                Line((5.58, 8.2698039923), (5.58, -1.2551960077))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.27
        extrude(amount=1.27)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(18.28, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.8074169928, perimeter: 4.3386511688
            with BuildLine():
                Line((-19.6716861774, 13.8755554141), (-18.7741988032, 12.9769918865))
                Line((-18.7741988032, 12.9769918865), (-17.8745578319, 13.8755554141))
                Line((-19.6716861774, 13.8755554141), (-17.8745578319, 13.8755554141))
            make_face()
        # OneSide extrude, distance=-22.86
        extrude(amount=-22.86, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a flat, parallelogram-shaped sheet metal bracket or panel with two vertical slots cut through its center and flanged edges on all sides for structural rigidity.
def model_41716_d55164d4_0009():
    """Model: Front Wall"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 17.78), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 193.5479985466, perimeter: 55.8799998093
            with BuildLine():
                Line((1.77, 1.27), (1.77, 13.97))
                Line((1.77, 1.27), (17.01, 1.27))
                Line((17.01, 13.9699998093), (17.01, 1.27))
                Line((1.77, 13.97), (17.01, 13.9699998093))
            make_face()
        # OneSide extrude, distance=-1.27
        extrude(amount=-1.27)

        # Sketch3 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 17.78), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 45.1612, perimeter: 27.94
            with BuildLine():
                Line((11.93, 1.27), (11.93, 10.16))
                Line((11.93, 10.16), (6.85, 10.16))
                Line((6.85, 10.16), (6.85, 1.27))
                Line((6.85, 1.27), (11.93, 1.27))
            make_face()
        # OneSide extrude, distance=-0.635
        extrude(amount=-0.635, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a hexagonal prism or cube-like polyhedron with alternating dark and light blue facets, featuring a complex geometric structure with multiple triangulated faces and internal geometry that suggests it may be a structural component or abstract geometric solid.
def model_41722_92ab0003_0000():
    """Model: Top Shell"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1275.094224, perimeter: 144.272
            with BuildLine():
                Line((0, 30.988), (0, 0))
                Line((0, 0), (41.148, 0))
                Line((41.148, 0), (41.148, 30.988))
                Line((41.148, 30.988), (0, 30.988))
            make_face()
        # OneSide extrude, distance=25.4
        extrude(amount=25.4)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 25.4), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1238.7072, perimeter: 142.24
            with BuildLine():
                Line((40.894, 0.254), (0.254, 0.254))
                Line((40.894, 30.734), (40.894, 0.254))
                Line((0.254, 30.734), (40.894, 30.734))
                Line((0.254, 0.254), (0.254, 30.734))
            make_face()
        # OneSide extrude, distance=-25.146
        extrude(amount=-25.146, mode=Mode.SUBTRACT)
    return part.part


# Description: This is an octahedron, a geometric polyhedron composed of eight equilateral triangular faces arranged symmetrically around a central point, with no holes, slots, or flanges.
def model_41722_92ab0003_0001():
    """Model: inner baffle"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 735.4824, perimeter: 109.22
            with BuildLine():
                Line((-30.48, 24.13), (0, 24.13))
                Line((-30.48, 0), (-30.48, 24.13))
                Line((0, 0), (-30.48, 0))
                Line((0, 24.13), (0, 0))
            make_face()
        # OneSide extrude, distance=1.27
        extrude(amount=1.27)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 24.13, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 28.4273625, perimeter: 61.595
            with BuildLine():
                Line((-0.9525, 30.1625), (0, 30.1625))
                Line((-0.9525, 0.3175), (-0.9525, 30.1625))
                Line((0, 0.3175), (-0.9525, 0.3175))
                Line((0, 30.1625), (0, 0.3175))
            make_face()
        # OneSide extrude, distance=-38.1
        extrude(amount=-38.1, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a parallelogram-shaped flat plate or frame with a hollow rectangular center and uniform border walls, featuring a slanted profile characteristic of a 3D extruded shape.
def model_41722_92ab0003_0007():
    """Model: front plate"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 22 constraints, 10 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 236.5791726476, perimeter: 273.0477517381
            with BuildLine():
                CenterArc((37.973, 22.987), 0.889, 0, 90)
                Line((37.973, 23.876), (0.889, 23.876))
                CenterArc((0.889, 22.987), 0.889, 90, 90)
                Line((0, 22.987), (0, 0.889))
                CenterArc((0.889, 0.889), 0.889, -180, 90)
                Line((0.889, 0), (37.973, 0))
                CenterArc((37.973, 0.889), 0.889, -90, 90)
                Line((38.862, 0.889), (38.862, 22.987))
            make_face()
            with BuildLine():
                Line((1.905, 1.905), (1.905, 21.971))
                Line((1.905, 21.971), (31.242, 21.971))
                Line((31.242, 21.971), (31.242, 1.905))
                Line((31.242, 1.905), (1.905, 1.905))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((32.512, 1.905), (32.512, 21.971))
                Line((32.512, 21.971), (37.592, 21.971))
                Line((37.592, 21.971), (37.592, 1.905))
                Line((37.592, 1.905), (32.512, 1.905))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.254
        extrude(amount=0.254)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 12 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.254), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.3166921744, perimeter: 1.994911335
            with Locations((0.635, 23.241)):
                Circle(0.3175)
            # Profile area: 0.3166921744, perimeter: 1.994911335
            with Locations((0.635, 0.635)):
                Circle(0.3175)
            # Profile area: 0.3166921744, perimeter: 1.994911335
            with Locations((38.227, 23.241)):
                Circle(0.3175)
            # Profile area: 0.3166921744, perimeter: 1.994911335
            with Locations((38.227, 0.635)):
                Circle(0.3175)
        # OneSide extrude, distance=-2.54
        extrude(amount=-2.54, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a rectangular bracket or support frame with a central rectangular cutout, featuring four vertical cylindrical posts at the corners and reinforcing ribs on the side panels, designed to provide structural support while minimizing weight.
def model_41729_b5092135_0004():
    """Model: Base v1 (1)"""
    with BuildPart() as part:
        # Sketch6 -> Extrude2 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 15 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 8.45, perimeter: 21
            with BuildLine():
                Line((-1.5, 1), (-0.5, 1))
                Line((-1.5, 0), (-1.5, 1))
                Line((-3, 0), (-1.5, 0))
                Line((-3, -1), (-3, 0))
                Line((-1.5, -1), (-3, -1))
                Line((-1.5, -0.5), (-1.5, -1))
                Line((3, -0.5), (-1.5, -0.5))
                Line((3, -1), (3, -0.5))
                Line((4.5, -1), (3, -1))
                Line((4.5, 0), (4.5, -1))
                Line((3, 0), (4.5, 0))
                Line((3, 1), (3, 0))
                Line((2.1, 1), (3, 1))
                Line((2.1, 0.5), (2.1, 1))
                Line((-0.5, 0.5), (2.1, 0.5))
                Line((-0.5, 1), (-0.5, 0.5))
            make_face()
        # OneSide extrude, distance=2.6
        extrude(amount=2.6)
    return part.part


# Description: This is a rectangular tray or shallow box with angled/tapered side walls, featuring a flat bottom and open top with a slightly recessed inner surface, resembling a drainage pan or collection basin.
def model_41729_b5092135_0007():
    """Model: Cap v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 14 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 6.76, perimeter: 10.4
            with BuildLine():
                Line((1.3, -1.3), (1.3, 1.3))
                Line((1.3, 1.3), (-1.3, 1.3))
                Line((-1.3, 1.3), (-1.3, -1.3))
                Line((-1.3, -1.3), (1.3, -1.3))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch2 -> Extrude2 (NewBody)
        # Sketch on BRepFace
        # Sketch has 7 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.24, perimeter: 22.4
            with BuildLine():
                Line((-1.5, 1.5), (-1.5, -1.5))
                Line((-1.5, -1.5), (1.5, -1.5))
                Line((1.5, -1.5), (1.5, 1.5))
                Line((1.5, 1.5), (-1.5, 1.5))
            make_face()
            with BuildLine():
                Line((1.3, -1.3), (1.3, 1.3))
                Line((-1.3, -1.3), (1.3, -1.3))
                Line((-1.3, 1.3), (-1.3, -1.3))
                Line((1.3, 1.3), (-1.3, 1.3))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.4
        extrude(amount=0.4)
    return part.part


# Description: This is a roof rack or carrier assembly with a streamlined, aerodynamic design featuring a central rectangular base channel, triangular upper frame elements, and side mounting flanges for vehicle attachment.
def model_41733_1ec9b00c_0021():
    """Model: height"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 88.9769450323, perimeter: 37.7953890065
            with BuildLine():
                Line((-66.1023054968, 0), (-75, 0))
                Line((-66.1023054968, 0), (-66.1023054968, 10))
                Line((-75, 10), (-66.1023054968, 10))
                Line((-75, 0), (-75, 10))
            make_face()
        # OneSide extrude, distance=15
        extrude(amount=15)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 14 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 75), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 21.7755740658, perimeter: 27.084005415
            with BuildLine():
                Line((22, 5.1115519627), (22, 1.9966036757))
                Line((22, 1.9966036757), (23.9761219398, 1.9966036757))
                Line((23.9761219398, 1.9966036757), (23.9106506186, 4.7291941225))
                CenterArc((22, 5.1115519627), 1.9485336293, -11.3164983481, 81.074170598)
                Line((15, 6.939739624), (22.6741759261, 6.939739624))
                Line((15, 5.1115519627), (15, 6.939739624))
                Line((15, 5.1115519627), (22, 5.1115519627))
            make_face()
            # Profile area: 24.4838789438, perimeter: 29.3048386321
            with BuildLine():
                Line((0, 5.1115519627), (0, 6.939739624))
                Line((-6.9765164477, 6.939739624), (0, 6.939739624))
                CenterArc((-7.9600893274, 5.1115519627), 2.0759782597, 61.7195560618, 122.3039932212)
                Line((-10.0309509136, 4.9658878774), (-10.0309509136, 2))
                Line((-10.0309509136, 2), (-8, 2))
                Line((-8, 2), (-7.9600893274, 5.1115519627))
                Line((-7.9600893274, 5.1115519627), (0, 5.1115519627))
            make_face()
            # Profile area: 27.42281492, perimeter: 33.6563753227
            with BuildLine():
                Line((15, 5.1115519627), (15, 6.939739624))
                Line((0, 6.939739624), (15, 6.939739624))
                Line((0, 5.1115519627), (0, 6.939739624))
                Line((0, 5.1115519627), (15, 5.1115519627))
            make_face()
        # OneSide extrude, distance=4
        extrude(amount=4, mode=Mode.ADD)
    return part.part


# Description: This is an elliptical or oval-shaped bowl or dish with a flat rim base and a shallow, curved interior surface featuring radial ribbing or fluting that extends from the center outward.
def model_41737_a8ec36c3_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.7671459203, perimeter: 4.7123890506
            Circle(0.7500000112)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.1623893165, perimeter: 3.8219124727
            Circle(0.6082762621)
        # OneSide extrude, distance=0.07
        extrude(amount=0.07, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a blue and gray automotive trim piece or molding with an elongated, slightly curved rectangular profile and a central slot or depression running along its length.
def model_41737_ab26cd49_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 198.8517687778, perimeter: 87.3691841672
            with BuildLine():
                CenterArc((-17.5, -1.5), 2.9154759474, 149.0362434679, 90)
                Line((-19, -4), (0, -6))
                Line((0, -6), (19, -4))
                CenterArc((17.5, -1.5), 2.9154759474, -59.0362434679, 90)
                Line((-20, 0), (20, 0))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 5.6578947368, perimeter: 12.5539403091
            with BuildLine():
                Line((2.5, 7), (2.5, 5.7368421053))
                Line((-2.5, 7), (2.5, 7))
                Line((-2.5, 5.7368421053), (-2.5, 7))
                Line((0, 6), (-2.5, 5.7368421053))
                Line((2.5, 5.7368421053), (0, 6))
            make_face()
            # Profile area: 6.8421052632, perimeter: 12.5013087301
            with BuildLine():
                Line((2.5, 5.7368421053), (2.5, 4.5))
                Line((2.5, 5.7368421053), (0, 6))
                Line((0, 6), (-2.5, 5.7368421053))
                Line((-2.5, 4.5), (-2.5, 5.7368421053))
                Line((2.5, 4.5), (-2.5, 4.5))
            make_face()
        # OneSide extrude, distance=-4.4
        extrude(amount=-4.4, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical tube or sleeve with a hollow interior, featuring a closed bottom end and an open top end with a blue-tinted mesh or perforated surface, commonly used as a filter, screen, or protective cover component.
def model_41737_d1472a19_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.8063904905, perimeter: 7.7716719065
            Circle(1.2369)
        # OneSide extrude, distance=6.5
        extrude(amount=6.5)
    return part.part


# Description: This is a hexagonal or polygonal geometric solid featuring triangulated faceted surfaces with internal geometric subdivisions and wireframe details visible on its faces.
def model_41739_1bc15d9f_0007():
    """Model: Seat Clamp Part 3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 6.4515998062, perimeter: 10.1599998474
            with BuildLine():
                Line((66.0399990082, 2.5399999619), (66.0399990082, 0))
                Line((63.4999990463, 2.5399999619), (66.0399990082, 2.5399999619))
                Line((63.4999990463, 0), (63.4999990463, 2.5399999619))
                Line((66.0399990082, 0), (63.4999990463, 0))
            make_face()
        # OneSide extrude, distance=2.54
        extrude(amount=2.54)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 2.54), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.3166921744, perimeter: 1.994911335
            with Locations((64.7699990273, 1.2699999809)):
                Circle(0.3175)
        # OneSide extrude, distance=-0.635
        extrude(amount=-0.635, mode=Mode.SUBTRACT)
    return part.part


MODELS = {
    "model_40705_5ff43505_0032": {"func": model_40705_5ff43505_0032, "volume": 0.0318692624, "area": 0.7568416157},
    "model_40705_5ff43505_0034": {"func": model_40705_5ff43505_0034, "volume": 0.1526265445, "area": 2.2517214921},
    "model_40705_5ff43505_0036": {"func": model_40705_5ff43505_0036, "volume": 0.3382405443, "area": 3.574819666},
    "model_40705_5ff43505_0038": {"func": model_40705_5ff43505_0038, "volume": 0.087054497, "area": 1.4226914752},
    "model_40705_5ff43505_0041": {"func": model_40705_5ff43505_0041, "volume": 110.3578667353, "area": 296.3150190866},
    "model_40705_5ff43505_0043": {"func": model_40705_5ff43505_0043, "volume": 237.1415926536, "area": 337.4159265359},
    "model_40782_3383cd58_0006": {"func": model_40782_3383cd58_0006, "volume": 0.3353650158, "area": 3.5657076618},
    "model_40782_3383cd58_0008": {"func": model_40782_3383cd58_0008, "volume": 1.47105076, "area": 11.7181405979},
    "model_40782_3383cd58_0016": {"func": model_40782_3383cd58_0016, "volume": 1.4922565105, "area": 10.6814150222},
    "model_40782_3383cd58_0017": {"func": model_40782_3383cd58_0017, "volume": 14.2157067575, "area": 33.3008821281},
    "model_40782_3383cd58_0020": {"func": model_40782_3383cd58_0020, "volume": 3.3834952879, "area": 18.5353966562},
    "model_40782_3383cd58_0022": {"func": model_40782_3383cd58_0022, "volume": 20.265399923, "area": 74.6364492298},
    "model_40782_3383cd58_0024": {"func": model_40782_3383cd58_0024, "volume": 2.081305133, "area": 12.2679193123},
    "model_40782_3383cd58_0025": {"func": model_40782_3383cd58_0025, "volume": 15.5328525057, "area": 70.9459460068},
    "model_40782_3383cd58_0028": {"func": model_40782_3383cd58_0028, "volume": 79.70025, "area": 176.095},
    "model_40815_80519d37_0001": {"func": model_40815_80519d37_0001, "volume": 24.5473089614, "area": 154.8130346733},
    "model_40939_0bedb1ea_0000": {"func": model_40939_0bedb1ea_0000, "volume": 0.0128648219, "area": 0.4349535029},
    "model_40997_e3c88650_0000": {"func": model_40997_e3c88650_0000, "volume": 43.7444678595, "area": 83.5575191895},
    "model_40997_e3c88650_0003": {"func": model_40997_e3c88650_0003, "volume": 87.4977873673, "area": 184.4159264688},
    "model_40999_cad6be09_0001": {"func": model_40999_cad6be09_0001, "volume": 685442.1214275192, "area": 58556.2656649399},
    "model_40999_cad6be09_0005": {"func": model_40999_cad6be09_0005, "volume": 45102.4383126258, "area": 9064.2641300154},
    "model_40999_cad6be09_0021": {"func": model_40999_cad6be09_0021, "volume": 78126.9799589639, "area": 13163.5551637565},
    "model_41032_ed481084_0001": {"func": model_41032_ed481084_0001, "volume": 2.462353464, "area": 16.3959036393},
    "model_41032_ed481084_0007": {"func": model_41032_ed481084_0007, "volume": 1174.5727822541, "area": 1666.2939341863},
    "model_41117_1b3271f2_0001": {"func": model_41117_1b3271f2_0001, "volume": 5.6792431687, "area": 77.9367789155},
    "model_41117_1b3271f2_0003": {"func": model_41117_1b3271f2_0003, "volume": 5.6818637596, "area": 77.8800637434},
    "model_41117_1b3271f2_0008": {"func": model_41117_1b3271f2_0008, "volume": 5.6818637596, "area": 77.8800637434},
    "model_41124_a5855c0d_0002": {"func": model_41124_a5855c0d_0002, "volume": 0.6385287068, "area": 7.6969020013},
    "model_41124_a5855c0d_0008": {"func": model_41124_a5855c0d_0008, "volume": 46.0070536155, "area": 91.4360541827},
    "model_41128_ee74f244_0015": {"func": model_41128_ee74f244_0015, "volume": 3.3716021115, "area": 21.117120129},
    "model_41128_ee74f244_0017": {"func": model_41128_ee74f244_0017, "volume": 149.413152786, "area": 197.58025},
    "model_41128_ee74f244_0018": {"func": model_41128_ee74f244_0018, "volume": 9.8096351108, "area": 27.4382099931},
    "model_41142_1bf94ee2_0003": {"func": model_41142_1bf94ee2_0003, "volume": 40.2119104693, "area": 104.6566437066},
    "model_41142_1bf94ee2_0008": {"func": model_41142_1bf94ee2_0008, "volume": 1.3367477071, "area": 9.2676984105},
    "model_41142_1bf94ee2_0010": {"func": model_41142_1bf94ee2_0010, "volume": 33.2731277702, "area": 89.615402822},
    "model_41211_11f6b8a0_0007": {"func": model_41211_11f6b8a0_0007, "volume": 8.9801116452, "area": 39.4837936637},
    "model_41229_16283ae1_0005": {"func": model_41229_16283ae1_0005, "volume": 1243.596, "area": 2926.16},
    "model_41229_16283ae1_0011": {"func": model_41229_16283ae1_0011, "volume": 0.931, "area": 18.32},
    "model_41229_16283ae1_0013": {"func": model_41229_16283ae1_0013, "volume": 14.4999999646, "area": 117.5000001416},
    "model_41229_16283ae1_0018": {"func": model_41229_16283ae1_0018, "volume": 30.5, "area": 181},
    "model_41234_74275eb0_0003": {"func": model_41234_74275eb0_0003, "volume": 0.1256872067, "area": 1.5834608722},
    "model_41234_74275eb0_0007": {"func": model_41234_74275eb0_0007, "volume": 14.8411453706, "area": 40.2832445883},
    "model_41234_74275eb0_0009": {"func": model_41234_74275eb0_0009, "volume": 344.2823966728, "area": 397.7653710915},
    "model_41234_74275eb0_0010": {"func": model_41234_74275eb0_0010, "volume": 8.6488886192, "area": 55.1145725014},
    "model_41234_74275eb0_0013": {"func": model_41234_74275eb0_0013, "volume": 691.7823858379, "area": 762.5947560417},
    "model_41303_bd1def52_0006": {"func": model_41303_bd1def52_0006, "volume": 13021.9804076, "area": 11159.6551},
    "model_41319_bb28c4f4_0000": {"func": model_41319_bb28c4f4_0000, "volume": 219.7272140021, "area": 300.5424646547},
    "model_41321_43c99300_0000": {"func": model_41321_43c99300_0000, "volume": 2.8533424888, "area": 48.0486785835},
    "model_41321_43c99300_0009": {"func": model_41321_43c99300_0009, "volume": 0.0810625415, "area": 7.3252555111},
    "model_41353_16ac5969_0018": {"func": model_41353_16ac5969_0018, "volume": 0.1555088364, "area": 1.8378317024},
    "model_41353_16ac5969_0019": {"func": model_41353_16ac5969_0019, "volume": 0.4500331476, "area": 4.1940261925},
    "model_41353_16ac5969_0021": {"func": model_41353_16ac5969_0021, "volume": 0.4500331476, "area": 4.1940261925},
    "model_41465_3c18418c_0000": {"func": model_41465_3c18418c_0000, "volume": 35396.0582399999, "area": 29109.6192},
    "model_41473_c2137170_0000": {"func": model_41473_c2137170_0000, "volume": 8.3566364585, "area": 35.8141562509},
    "model_41473_c2137170_0005": {"func": model_41473_c2137170_0005, "volume": 10.3672557568, "area": 58.7477826221},
    "model_41473_c2137170_0006": {"func": model_41473_c2137170_0006, "volume": 8.6393797974, "area": 51.8362787842},
    "model_41473_c2137170_0007": {"func": model_41473_c2137170_0007, "volume": 14.5769899127, "area": 65.596454607},
    "model_41501_b627682a_0005": {"func": model_41501_b627682a_0005, "volume": 348.7840002771, "area": 774.3200000648},
    "model_41501_b627682a_0006": {"func": model_41501_b627682a_0006, "volume": 0.9869468907, "area": 7.2185839384},
    "model_41501_b627682a_0007": {"func": model_41501_b627682a_0007, "volume": 0.1529665434, "area": 4.2804861411},
    "model_41501_b627682a_0014": {"func": model_41501_b627682a_0014, "volume": 0.0325940231, "area": 0.7225663068},
    "model_41508_b9593bb5_0000": {"func": model_41508_b9593bb5_0000, "volume": 151.1965676817, "area": 241.6820080624},
    "model_41508_c18d22f2_0000": {"func": model_41508_c18d22f2_0000, "volume": 63.9717349998, "area": 219.6690225747},
    "model_41595_e15895be_0005": {"func": model_41595_e15895be_0005, "volume": 6165.63283, "area": 5049.3010572917},
    "model_41599_f66b4e5b_0002": {"func": model_41599_f66b4e5b_0002, "volume": 1.7592919384, "area": 12.315043438},
    "model_41599_f66b4e5b_0005": {"func": model_41599_f66b4e5b_0005, "volume": 4.8694686131, "area": 30.7876080052},
    "model_41599_f66b4e5b_0008": {"func": model_41599_f66b4e5b_0008, "volume": 0.4131194339, "area": 4.6024332375},
    "model_41599_f66b4e5b_0009": {"func": model_41599_f66b4e5b_0009, "volume": 0.0003926991, "area": 0.0314159265},
    "model_41648_577daf16_0009": {"func": model_41648_577daf16_0009, "volume": 2.9923358832, "area": 46.9364614135},
    "model_41648_577daf16_0010": {"func": model_41648_577daf16_0010, "volume": 1.5341423415, "area": 11.5431630781},
    "model_41650_9417da80_0006": {"func": model_41650_9417da80_0006, "volume": 0.4064292158, "area": 5.7271240352},
    "model_41654_b616fab1_0000": {"func": model_41654_b616fab1_0000, "volume": 18.6924762889, "area": 201.3760890951},
    "model_41672_cf87e0b6_0000": {"func": model_41672_cf87e0b6_0000, "volume": 0.2021487345, "area": 5.068038843},
    "model_41672_d9512d5c_0000": {"func": model_41672_d9512d5c_0000, "volume": 37.6991118431, "area": 169.6460032938},
    "model_41672_f0d8843f_0000": {"func": model_41672_f0d8843f_0000, "volume": 0.0078791695, "area": 0.2531279852},
    "model_41672_ffe3d8cc_0000": {"func": model_41672_ffe3d8cc_0000, "volume": 0.0796776073, "area": 1.9260922368},
    "model_41680_49185107_0001": {"func": model_41680_49185107_0001, "volume": 45602.7410524, "area": 36030.379552},
    "model_41681_2586b16d_0000": {"func": model_41681_2586b16d_0000, "volume": 12.2239044596, "area": 45.7819686339},
    "model_41685_df8ac866_0001": {"func": model_41685_df8ac866_0001, "volume": 35.8018879086, "area": 182.3225741559},
    "model_41685_df8ac866_0005": {"func": model_41685_df8ac866_0005, "volume": 9.6602962761, "area": 66.2619892824},
    "model_41685_df8ac866_0006": {"func": model_41685_df8ac866_0006, "volume": 152.2611219058, "area": 228.2264586238},
    "model_41685_df8ac866_0014": {"func": model_41685_df8ac866_0014, "volume": 1.9276876833, "area": 16.3819599365},
    "model_41693_a737c734_0003": {"func": model_41693_a737c734_0003, "volume": 0.0466550911, "area": 1.1907625759},
    "model_41698_900d863d_0008": {"func": model_41698_900d863d_0008, "volume": 0.2916784297, "area": 3.6404705546},
    "model_41708_3a74f048_0009": {"func": model_41708_3a74f048_0009, "volume": 0.0575524318, "area": 2.0780948203},
    "model_41714_1d49f4d1_0005": {"func": model_41714_1d49f4d1_0005, "volume": 6.647711601, "area": 62.9892481348},
    "model_41716_d55164d4_0006": {"func": model_41716_d55164d4_0006, "volume": 237.5952348678, "area": 509.3423321988},
    "model_41716_d55164d4_0009": {"func": model_41716_d55164d4_0009, "volume": 217.1285961542, "area": 469.353896851},
    "model_41722_92ab0003_0000": {"func": model_41722_92ab0003_0000, "volume": 1238.8620384, "area": 9791.464288},
    "model_41722_92ab0003_0001": {"func": model_41722_92ab0003_0001, "volume": 248.110390875, "area": 1598.787125},
    "model_41722_92ab0003_0007": {"func": model_41722_92ab0003_0007, "volume": 59.7693506033, "area": 542.0057667575},
    "model_41729_b5092135_0004": {"func": model_41729_b5092135_0004, "volume": 21.97, "area": 71.5},
    "model_41729_b5092135_0007": {"func": model_41729_b5092135_0007, "volume": 4.276, "area": 32.16},
    "model_41733_1ec9b00c_0021": {"func": model_41733_1ec9b00c_0021, "volume": 1629.3832472034, "area": 1168.3335060787},
    "model_41737_a8ec36c3_0000": {"func": model_41737_a8ec36c3_0000, "volume": 0.2720619319, "area": 4.7443035238},
    "model_41737_ab26cd49_0000": {"func": model_41737_ab26cd49_0000, "volume": 96.0048317573, "area": 428.9269489583},
    "model_41737_d1472a19_0000": {"func": model_41737_d1472a19_0000, "volume": 31.2415381885, "area": 60.128648373},
    "model_41739_1bc15d9f_0007": {"func": model_41739_1bc15d9f_0007, "volume": 16.185963977, "area": 39.9763679226},
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
