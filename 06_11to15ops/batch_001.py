"""Batch 001 - passing/06_11to15ops
49 models bundled from Fusion360 Gallery reconstructions.
"""

from build123d import *


# Description: This is a rectangular box-shaped container or enclosure with an angled, multi-faceted trapezoidal top featuring triangulated surface geometry and what appears to be ventilation slots or openings along the upper surface.
def model_101605_59c455b1_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 14, perimeter: 18
            with BuildLine():
                Line((7, -2), (0, -2))
                Line((7, 0), (7, -2))
                Line((0, 0), (7, 0))
                Line((0, -2), (0, 0))
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2)

        # Sketch3 -> Extrude2 (Cut)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((1, 1)):
                Circle(0.5)
        # OneSide extrude, distance=-6
        extrude(amount=-6, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 2), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.6, perimeter: 4.6880613018
            with BuildLine():
                Line((2, 2), (2, 1.4))
                Line((2, 1.4), (4, 2))
                Line((2, 2), (4, 2))
            make_face()
        # OneSide extrude, distance=-2
        extrude(amount=-2, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(2, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.7445228862, perimeter: 3.0980915448
            with BuildLine():
                CenterArc((-1, 1), 0.5, 126.8698976458, 286.2602047083)
                Line((-1.3, 1.4), (-0.7, 1.4))
            make_face()
        # OneSide extrude, distance=-2
        extrude(amount=-2, mode=Mode.ADD)

        # Sketch10 -> Extrude6 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 14, perimeter: 18
            with BuildLine():
                Line((7, -2), (7, 0))
                Line((7, 0), (0, 0))
                Line((0, 0), (0, -2))
                Line((0, -2), (7, -2))
            make_face()
        # OneSide extrude, distance=0.1
        extrude(amount=0.1, mode=Mode.SUBTRACT)
    return part.part


# Description: This is an oval or elliptical ring-shaped component with a solid base section and an open mesh or latticed top section featuring a central cross-shaped cutout, designed as a containment or filtering structure.
def model_106815_f6580357_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 78.5398163397, perimeter: 31.4159265359
            Circle(5)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 0.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 78.5398163397, perimeter: 31.4159265359
            Circle(5)
        # OneSide extrude, distance=1.5
        extrude(amount=1.5, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            Circle(0.5)
        # OneSide extrude, distance=-1.5
        extrude(amount=-1.5, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.1471257208, perimeter: 10.2732740885
            with BuildLine():
                CenterArc((-2.75, -4.75), 5.2559490104, 64.6538240581, 50.6923518839)
                CenterArc((0, 0), 0.5, 141.7158138209, 38.2841861791)
                CenterArc((-2.8539783577, -3.7188548932), 4.7211136373, 58.5749869133, 58.1219791667)
                CenterArc((0, 0), 5, 174.2727462456, 5.7272537544)
            make_face()
        # OneSide extrude, distance=-1.5
        extrude(amount=-1.5, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical connector or adapter housing with an angled top opening, featuring a central cylindrical bore, lateral flanges or mounting tabs on the sides, and a slotted base for assembly or mounting purposes.
def model_107260_5d11b1b9_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 11.4009182797, perimeter: 11.9694680102
            Circle(1.905)
        # OneSide extrude, distance=3.81
        extrude(amount=3.81)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 3.81, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 8.8673808842, perimeter: 27.9287586904
            with BuildLine():
                CenterArc((0, 0), 2.54, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.905, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 11.4009182797, perimeter: 11.9694680102
            Circle(1.905)
        # OneSide extrude, distance=1.905
        extrude(amount=1.905, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 5.715, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 11.4009182797, perimeter: 11.9694680102
            Circle(1.905)
        # OneSide extrude, distance=3.81
        extrude(amount=3.81, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 9.525, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.2489822118, perimeter: 6.0442779663
            with BuildLine():
                Line((1.4199031657, -1.27), (-1.4199031657, -1.27))
                CenterArc((0, 0), 1.905, -138.1896851042, 96.3793702084)
            make_face()
        # OneSide extrude, distance=-2.8448
        extrude(amount=-2.8448, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -1.27), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.7316855998, perimeter: 3.0322652292
            with Locations((0, 7.62)):
                Circle(0.4826)
        # OneSide extrude, distance=-2.2352
        extrude(amount=-2.2352, mode=Mode.SUBTRACT)

        # Sketch6 -> Extrude6 (Cut)
        # Sketch on BRepFace
        # Sketch has 9 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 4.7475383354, perimeter: 9.7737621469
            with BuildLine():
                Line((-0.635, 1.7960512242), (-0.635, -1.7960512242))
                CenterArc((0, 0), 1.905, -109.4712206345, 38.942441269)
                Line((0.635, 1.7960512242), (0.635, -1.7960512242))
                CenterArc((0, 0), 1.905, 70.5287793655, 38.942441269)
            make_face()
        # OneSide extrude, distance=-1.27
        extrude(amount=-1.27, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a circular pulley or sprocket with a large central bore, featuring a flat disc body with curved flanges on opposite sides and mesh-textured cutout sections for weight reduction.
def model_109121_f33a42fa_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 15.8337055139, perimeter: 14.1057510146
            Circle(2.245)
        # OneSide extrude, distance=0.6
        extrude(amount=0.6)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 4.9087385212, perimeter: 7.853981634
            Circle(1.25)
        # OneSide extrude, distance=1.4
        extrude(amount=1.4, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 10 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -1.4), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.2554704825, perimeter: 3.108752772
            with BuildLine():
                Line((-1, 0.75), (-1, -0.75))
                CenterArc((0, 0), 1.25, 143.1301023542, 73.7397952917)
            make_face()
            # Profile area: 0.2554704825, perimeter: 3.108752772
            with BuildLine():
                Line((1, 0.75), (1, -0.75))
                CenterArc((0, 0), 1.25, -36.8698976459, 73.7397952917)
            make_face()
        # OneSide extrude, distance=-1.4
        extrude(amount=-1.4, mode=Mode.SUBTRACT)

        # Sketch8 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.6), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1.7671458676, perimeter: 4.7123889804
            Circle(0.75)
        # OneSide extrude, distance=-2
        extrude(amount=-2, mode=Mode.SUBTRACT)

        # Sketch9 -> Extrude6 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.6), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1.3744467859, perimeter: 10.9955742876
            with BuildLine():
                CenterArc((0, 0), 1, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.75, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.03
        extrude(amount=-0.03, mode=Mode.SUBTRACT)

        # Sketch10 -> Extrude7 (Cut)
        # Sketch on BRepFace
        # Sketch has 10 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.57), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0217545656, perimeter: 0.5961715178
            with BuildLine():
                Line((-0.15, 0.89), (0, 0.89))
                Line((-0.15, 0.7348469228), (-0.15, 0.89))
                CenterArc((0, 0), 0.75, 90, 11.5369590328)
                Line((0, 0.75), (0, 0.89))
            make_face()
            # Profile area: 0.0217545656, perimeter: 0.5961715178
            with BuildLine():
                Line((0, 0.75), (0, 0.89))
                CenterArc((0, 0), 0.75, 78.4630409672, 11.5369590328)
                Line((0.15, 0.89), (0.15, 0.7348469228))
                Line((0, 0.89), (0.15, 0.89))
            make_face()
        # OneSide extrude, distance=-1.97
        extrude(amount=-1.97, mode=Mode.SUBTRACT)

        # Sketch11 -> Extrude8 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -1.4), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.4099775458, perimeter: 9.5491137723
            with BuildLine():
                Line((-0.15, 0.7348469228), (-0.15, 0.8239576749))
                CenterArc((0, 0), 0.8375, 100.3176025129, 339.3647949743)
                Line((0.15, 0.8239576749), (0.15, 0.7348469228))
                CenterArc((0, 0), 0.75, 101.5369590328, 336.9260819344)
            make_face()
        # OneSide extrude, distance=-0.4
        extrude(amount=-0.4, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a dark blue plastic or metal bracket with an angular, asymmetrical C-shaped design featuring a vertical flange on the right side, an open cavity in the center, and internal ribbing for structural reinforcement.
def model_111043_c6235173_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch5 -> Extrude2 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 12 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0478247413, perimeter: 1.1752629887
            with BuildLine():
                CenterArc((0.5587422383, -0.1770814663), 0.05, 0, 90)
                Line((0.3579503087, -0.1270814663), (0.5587422383, -0.1270814663))
                Line((0.3579503087, -0.1270814663), (0.3579503087, -0.2087144767))
                Line((0.4598801876, -0.2087144767), (0.3579503087, -0.2087144767))
                CenterArc((0.4598801876, -0.2587144767), 0.05, 0, 90)
                Line((0.5098801876, -0.4853812147), (0.5098801876, -0.2587144767))
                Line((0.6087422383, -0.4853812147), (0.5098801876, -0.4853812147))
                Line((0.6087422383, -0.1770814663), (0.6087422383, -0.4853812147))
            make_face()
        # OneSide extrude, distance=0.35
        extrude(amount=0.35)

        # Sketch6 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0.5098801876, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.0255999997, perimeter: 0.6399999969
            with BuildLine():
                Line((0.2899999935, 0), (0.4499999899, 0))
                Line((0.2899999935, -0.160000002), (0.2899999935, 0))
                Line((0.4499999899, -0.160000002), (0.2899999935, -0.160000002))
                Line((0.4499999899, 0), (0.4499999899, -0.160000002))
            make_face()
            # Profile area: 0.044799998, perimeter: 0.8799999803
            with BuildLine():
                Line((0.4499999899, 0.2799999937), (0.4499999899, 0))
                Line((0.2899999935, 0.2799999937), (0.4499999899, 0.2799999937))
                Line((0.2899999935, 0), (0.2899999935, 0.2799999937))
                Line((0.2899999935, 0), (0.4499999899, 0))
            make_face()
        # OneSide extrude, distance=-0.4
        extrude(amount=-0.4, mode=Mode.SUBTRACT)

        # Sketch7 -> Extrude4 (Cut)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 0, 0.1270814663), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.0096637924, perimeter: 0.3484806981
            with Locations((-0.4843061423, 0.1444445224)):
                Circle(0.0554624257)
        # OneSide extrude, distance=-0.3
        extrude(amount=-0.3, mode=Mode.SUBTRACT)

        # Sketch8 -> Extrude5 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0246465901, perimeter: 1.0051829061
            with BuildLine():
                Line((0.531140198, -0.2587144767), (0.531140198, -0.4641212044))
                Line((0.531140198, -0.4641212044), (0.5874822279, -0.4641212044))
                Line((0.5874822279, -0.4641212044), (0.5874822279, -0.1770814663))
                CenterArc((0.5587422383, -0.1770814663), 0.0287399897, 0, 90)
                Line((0.5587422383, -0.1483414766), (0.379210319, -0.1483414766))
                Line((0.379210319, -0.1483414766), (0.379210319, -0.1874544664))
                Line((0.379210319, -0.1874544664), (0.4598801876, -0.1874544664))
                CenterArc((0.4598801876, -0.2587144767), 0.0712600103, 0, 90)
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a bracket or support assembly featuring an angular, multi-planar structure with a tall vertical flange, horizontal mounting base, and internal ribbing or reinforcement elements for structural rigidity.
def model_111506_a7273ee0_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 13 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 9, perimeter: 20
            with BuildLine():
                Line((-4.5, 0), (-4.5, 1))
                Line((4.5, 0), (-4.5, 0))
                Line((4.5, 1), (4.5, 0))
                Line((-4.5, 1), (4.5, 1))
            make_face()
        # Symmetric extrude, each_side=6.75
        extrude(amount=6.75, both=True)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        # Sketch has 13 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 9, perimeter: 20
            with BuildLine():
                Line((-4.5, 1), (-4.5, 2))
                Line((-4.5, 1), (4.5, 1))
                Line((4.5, 2), (4.5, 1))
                Line((1.0736724378, 2), (4.5, 2))
                Line((-4.5, 2), (1.0736724378, 2))
            make_face()
            # Profile area: 13.460731299, perimeter: 22.0915756186
            with BuildLine():
                Line((4.5, 2), (4.5, 5.5))
                CenterArc((2.7868362189, 5.5), 1.7131637811, 0, 180)
                Line((1.0736724378, 2), (1.0736724378, 5.5))
                Line((1.0736724378, 2), (4.5, 2))
            make_face()
            with BuildLine():
                CenterArc((2.7868362189, 5.5), 1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=3.75
        extrude(amount=3.75, both=True, mode=Mode.ADD)

        # Sketch4 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(4.5, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 5.5, perimeter: 13
            with BuildLine():
                Line((2.75, 0), (2.75, 1))
                Line((2.75, 1), (-2.75, 1))
                Line((-2.75, 1), (-2.75, 0))
                Line((-2.75, 0), (2.75, 0))
            make_face()
        # OneSide extrude, distance=-10.5343
        extrude(amount=-10.5343, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 9 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.1309733553, perimeter: 3.7699111843
            with Locations((-2.5, 5.25)):
                Circle(0.6)
            # Profile area: 1.1309733553, perimeter: 3.7699111843
            with Locations((2.5, 5.25)):
                Circle(0.6)
            # Profile area: 1.1309733553, perimeter: 3.7699111843
            with Locations((-2.5, -5.25)):
                Circle(0.6)
            # Profile area: 1.1309733553, perimeter: 3.7699111843
            with Locations((2.5, -5.25)):
                Circle(0.6)
        # OneSide extrude, distance=-2.3791
        extrude(amount=-2.3791, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical pipe or tube connector featuring two rounded end caps with a central cylindrical body, characterized by a smooth curved surface and symmetrical geometry typical of a sleeve or coupling component.
def model_113343_e692c488_0006():
    """Model: PART 3 v1 (2)"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((-1.0582196205, 1.2247912275)):
                Circle(0.15)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)
    return part.part


# Description: This is a hollow rectangular box or container with an angled/tilted top lid, featuring a trapezoidal or wedge-like overall shape with flat side panels and an open front face.
def model_113698_dcf18f66_0022():
    """Model: RING_TOOTH2 v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 52.4645973149, perimeter: 209.8583892598
            with BuildLine():
                CenterArc((0, 0), 16.95, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 16.45, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=3
        extrude(amount=3)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 898.3502768428, perimeter: 139.9000326658
            with BuildLine():
                CenterArc((0, 0), 16.95, -88.31, 358.31)
                Line((0, 0), (0, -16.95))
                Line((0, 0), (0.4998857986, -16.9426271336))
            make_face()
        # OneSide extrude, distance=3
        extrude(amount=3, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on XY construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 4, perimeter: 8
            with BuildLine():
                Line((-0.5, 2), (-0.5, 0))
                Line((-0.5, 0), (1.5, 0))
                Line((1.5, 0), (1.5, 2))
                Line((1.5, 2), (-0.5, 2))
            make_face()
        # OneSide extrude, distance=28
        extrude(amount=28, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude4 (Cut)
        # Sketch on XY construction plane
        # Sketch has 6 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0606424881, perimeter: 1.2983038652
            with BuildLine():
                Line((0.2425699524, 3), (0, 3))
                Line((0, 2.5), (0, 3))
                Line((0, 2.5), (0.2425699524, 3))
            make_face()
            # Profile area: 0.0643289615, perimeter: 1.3196426592
            with BuildLine():
                Line((0.2425699524, 3), (0.4851399048, 3))
                Line((0.2425699524, 3), (0.4998857986, 2.5))
                Line((0.4998857986, 3), (0.4998857986, 2.5))
                Line((0.4851399048, 3), (0.4998857986, 3))
            make_face()
        # OneSide extrude, distance=19.3
        extrude(amount=19.3, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical sleeve or tube with a slightly tapered upper end and a flanged or stepped shoulder near the top, featuring a hollow interior bore running through its length.
def model_113841_5c85a0f0_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 12.5663706144, perimeter: 12.5663706144
            with Locations((1, -3)):
                Circle(2)
        # OneSide extrude, distance=8
        extrude(amount=8)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 8, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 8.0424771932, perimeter: 10.0530964915
            with Locations((-1, 3)):
                Circle(1.6)
        # OneSide extrude, distance=2
        extrude(amount=2, mode=Mode.ADD)

        # Sketch5 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 10, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 6.157521601, perimeter: 8.7964594301
            with Locations((-1, 3)):
                Circle(1.4)
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)

        # Sketch6 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 11, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.5238934212, perimeter: 7.5398223686
            with Locations((-1, 3)):
                Circle(1.2)
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)
    return part.part


# Description: This is a gripper or clamping jaw with an elongated cylindrical body, two opposing curved finger-like prongs at one end for gripping, and a tapered handle section with blue striping or detailing along its length.
def model_114495_ab1d8a08_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch3 -> Extrude2 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 12 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 43.5203988903, perimeter: 46.4996761811
            with BuildLine():
                CenterArc((1, 7), 1, 0, 180)
                Line((0, 4), (0, 7))
                CenterArc((-4, 5.1666666667), 4.1666666667, -90, 73.7397952917)
                CenterArc((-4, 0), 1, 90, 180)
                Line((0, -1), (-4, -1))
                Line((0, -7), (0, -1))
                CenterArc((1, -7), 1, 180, 180)
                Line((2, 0), (2, -7))
                Line((2, 7), (2, 0))
            make_face()
            with BuildLine():
                CenterArc((1, -7), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1, 7), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1, 0), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-4, 0), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-1.5, 0), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch4 -> Extrude3 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2002961666, perimeter: 1.5865042901
            with Locations((1, 6.9895367098)):
                Circle(0.2525)
        # OneSide extrude, distance=0.25
        extrude(amount=0.25, mode=Mode.SUBTRACT)

        # Sketch6 -> Extrude5 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2002961666, perimeter: 1.5865042901
            with Locations((1.0000000149, 0)):
                Circle(0.2525)
        # OneSide extrude, distance=0.25
        extrude(amount=0.25, mode=Mode.SUBTRACT)

        # Sketch7 -> Extrude6 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2002961666, perimeter: 1.5865042901
            with Locations((1.0000000149, -7.0000001043)):
                Circle(0.2525)
        # OneSide extrude, distance=0.25
        extrude(amount=0.25, mode=Mode.SUBTRACT)

        # Sketch8 -> Extrude7 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2002961666, perimeter: 1.5865042901
            with Locations((-1.5, 0)):
                Circle(0.2525)
        # OneSide extrude, distance=0.25
        extrude(amount=0.25, mode=Mode.SUBTRACT)

        # Sketch9 -> Extrude8 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2002961666, perimeter: 1.5865042901
            with Locations((-4.0000000596, 0)):
                Circle(0.2525)
        # OneSide extrude, distance=0.25
        extrude(amount=0.25, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a sheet metal bracket or duct component with an angular, asymmetrical shape featuring a main body with an open interior cavity, flanged edges, and internal ribbing or support structures for reinforcement.
def model_114867_991a50e4_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrusion1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 36, perimeter: 24
            with BuildLine():
                Line((0, 6), (0, 0))
                Line((0, 0), (6, 0))
                Line((6, 0), (6, 6))
                Line((6, 6), (0, 6))
            make_face()
        # OneSide extrude, distance=3.5
        extrude(amount=3.5)

        # Sketch2 -> Extrusion2 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, -1, 0), z_dir=(-1, 0, 0))):
            # Profile area: 9, perimeter: 12
            with BuildLine():
                Line((-3, 3.5), (-3, 0.5))
                Line((-3, 0.5), (0, 0.5))
                Line((0, 0.5), (0, 3.5))
                Line((0, 3.5), (-3, 3.5))
            make_face()
        # OneSide extrude, distance=-6.5
        extrude(amount=-6.5, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrusion3 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, -1, 0), z_dir=(-1, 0, 0))):
            # Profile area: 4.2190551832, perimeter: 8.6917328367
            with BuildLine():
                CenterArc((-2, -0.5), 3.6400549446, 105.9453959009, 58.1092081982)
                Line((-3, 0.5), (-5.5, 0.5))
                Line((-3, 0.5), (-3, 3))
            make_face()
        # OneSide extrude, distance=-6.5
        extrude(amount=-6.5, mode=Mode.SUBTRACT)

        # Sketch6 -> Extrusion4 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.5), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.5, perimeter: 3.2360679775
            with BuildLine():
                Line((-2.5, -2), (-3, -1))
                Line((-3, -1), (-3.5, -2))
                Line((-2.5, -2), (-3.5, -2))
            make_face()
        # OneSide extrude, distance=1.5
        extrude(amount=1.5, mode=Mode.ADD)
    return part.part


# Description: This is a complex geometric bracket or connector with an irregular, organic shape featuring a large central oval aperture, multiple angular flanges and protruding sections, and a wireframe lattice structure with internal ribbing for structural reinforcement.
def model_115629_40d61053_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 320, perimeter: 72
            with BuildLine():
                Line((13.5, -17.5), (-2.5, -17.5))
                Line((13.5, 2.5), (13.5, -17.5))
                Line((-2.5, 2.5), (13.5, 2.5))
                Line((-2.5, -17.5), (-2.5, 2.5))
            make_face()
        # OneSide extrude, distance=12
        extrude(amount=12)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 17.5), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 130, perimeter: 46
            with BuildLine():
                Line((-1, 11), (-1, 1))
                Line((-1, 1), (12, 1))
                Line((12, 1), (12, 11))
                Line((12, 11), (-1, 11))
            make_face()
        # OneSide extrude, distance=-21
        extrude(amount=-21, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(13.5, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 25.1327412287, perimeter: 20.5663706144
            with BuildLine():
                CenterArc((-9, 0), 4, 0, 180)
                Line((-13, 0), (-5, 0))
            make_face()
        # OneSide extrude, distance=-4
        extrude(amount=-4, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(-2.5, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 25.1327412287, perimeter: 20.5663706144
            with BuildLine():
                CenterArc((9, 0), 4, 0, 180)
                Line((5, 0), (13, 0))
            make_face()
        # OneSide extrude, distance=-4
        extrude(amount=-4, mode=Mode.SUBTRACT)

        # Sketch8 -> Extrude5 (Join)
        # Sketch on XY construction plane
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 130, perimeter: 46
            with BuildLine():
                Line((12, 1), (12, 11))
                Line((12, 11), (-1, 11))
                Line((-1, 11), (-1, 1))
                Line((-1, 1), (12, 1))
            make_face()
        # OneSide extrude, distance=-5
        extrude(amount=-5, mode=Mode.ADD)

        # Sketch9 -> Extrude6 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -5), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 49, perimeter: 28
            with BuildLine():
                Line((-2, 9), (-2, 2))
                Line((-9, 9), (-2, 9))
                Line((-9, 2), (-9, 9))
                Line((-2, 2), (-9, 2))
            make_face()
        # OneSide extrude, distance=-7
        extrude(amount=-7, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a circular disk or wheel hub with an overall flat, disk-like shape featuring two parallel longitudinal slots running across its face and a textured or ribbed edge pattern around its perimeter.
def model_120132_b78e04ad_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch5 -> Extrude4 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 182.4146924751, perimeter: 47.8778720407
            Circle(7.62)
        # OneSide extrude, distance=1.27
        extrude(amount=1.27)

        # Sketch6 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 16 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1.27), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 9.039778347, perimeter: 30.6428432075
            with BuildLine():
                CenterArc((0, 0), 7.62, -69.4437442749, 4.536351068)
                Line((3.2315091713, -6.9008512863), (3.2271042776, -3.1116193882))
                CenterArc((0.285567592, 0.0663823209), 4.3303963947, -47.2128647346, 94.5589394264)
                Line((3.2197076316, 3.2512143673), (3.2154563016, 6.9083457334))
                CenterArc((0, 0), 7.62, 65.0406031642, 4.0515164098)
                Line((2.7059377655, 2.7562646311), (2.7193226222, 7.1182641477))
                CenterArc((0.1035279912, 0.0221603677), 3.7746341222, -46.765282973, 93.1789412451)
                Line((2.6755868384, -7.134818503), (2.6891096421, -2.7278633201))
            make_face()
            # Profile area: 8.3325915153, perimeter: 30.3131384543
            with BuildLine():
                Line((-2.6994921851, 2.7301511046), (-2.6928804576, 7.1283093957))
                CenterArc((0, 0), 7.62, 110.6951945213, 3.6331186136)
                Line((-3.144713008, 3.2567011845), (-3.1391709, 6.9433425712))
                CenterArc((0.241062678, 0.0629080999), 4.6544378031, 136.6713363852, 84.9602931953)
                Line((-3.2947078656, -6.8709024211), (-3.2378105765, -3.0292161121))
                CenterArc((0, 0), 7.62, -115.6184647359, 4.7510054753)
                Line((-2.7143001356, -7.1201808105), (-2.7076798297, -2.7163160745))
                CenterArc((0.3253662699, 0.0023641075), 4.0731548674, 137.9561763725, 83.9153825157)
            make_face()
        # OneSide extrude, distance=-0.79375
        extrude(amount=-0.79375, mode=Mode.SUBTRACT)

        # Sketch11 -> Extrude6 (Cut)
        # Sketch on BRepFace
        # Sketch has 29 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1.27), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.3158369183, perimeter: 1.9922157938
            with Locations((2.4171645859, -2.2765715496)):
                Circle(0.3170709913)
            # Profile area: 0.318015104, perimeter: 1.9990736998
            with Locations((-2.3402266944, -2.3354501546)):
                Circle(0.3181624609)
            # Profile area: 0.3175794668, perimeter: 1.997704002
            with Locations((-2.3402266944, 2.4101654047)):
                Circle(0.3179444668)
            # Profile area: 0.3245496609, perimeter: 2.0195076928
            with Locations((2.3629030117, 2.3694692241)):
                Circle(0.3214146319)
        # OneSide extrude, distance=-0.635
        extrude(amount=-0.635, mode=Mode.SUBTRACT)

        # Sketch12 -> Extrude7 (NewBody)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1.27), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.1335597562, perimeter: 1.2955158802
            with Locations((2.4171645859, -2.2765715496)):
                Circle(0.2061877562)
            # Profile area: 0.1335597562, perimeter: 1.2955158802
            with Locations((-2.3402266944, -2.3354501546)):
                Circle(0.2061877562)
            # Profile area: 0.1187397598, perimeter: 1.2215268431
            with Locations((-2.3402266944, 2.4101654047)):
                Circle(0.1944120352)
            # Profile area: 0.1335597562, perimeter: 1.2955158802
            with Locations((2.3629030117, 2.3694692241)):
                Circle(0.2061877562)
        # OneSide extrude, distance=-0.79375
        extrude(amount=-0.79375)

        # Sketch11 -> Extrude8 (Cut)
        # Sketch on BRepFace
        # Sketch has 29 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1.27), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 19.9033494879, perimeter: 35.3936225058
            with BuildLine():
                CenterArc((0, 0), 2.667, 0, 360)
            make_face()
            with BuildLine():
                Line((2.0135054338, -0.1632616873), (2.0150948696, -0.4586469875))
                Line((2.0150948696, -0.4586469875), (1.6651009911, -0.4586469875))
                Line((1.6651009911, -0.4586469875), (1.6651009911, -0.3269661224))
                Line((1.6651009911, -0.3269661224), (1.4987672667, -0.4586469875))
                Line((1.4987672667, -0.4586469875), (0.3067089084, -0.4586469875))
                Line((0.3067089084, -0.4586469875), (0.0774365214, -0.2118214962))
                Line((0.0774365214, -0.2118214962), (1.2106827124, -0.2118214962))
                Line((1.2106827124, -0.2118214962), (1.3304694073, -0.1232258839))
                Line((1.3304694073, -0.1232258839), (1.3304694073, 0.4787976548))
                Line((1.3304694073, 0.4787976548), (1.6545265684, 0.4787976548))
                Line((1.6545265684, 0.4787976548), (1.6545265684, -0.2349354555))
                Line((1.6545265684, -0.2349354555), (1.7037579556, -0.1632616873))
                Line((1.7037579556, -0.1632616873), (2.0135054338, -0.1632616873))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((1.0347007362, 0.4637063884), (1.0347007362, -0.0498612894))
                Line((1.0347007362, -0.0498612894), (0.9530618173, -0.1102423693))
                Line((0.9530618173, -0.1102423693), (0.7944351559, -0.1102423693))
                Line((0.7944351559, -0.1102423693), (0.7944351559, 0.4637063884))
                Line((0.7944351559, 0.4637063884), (1.0347007362, 0.4637063884))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((0.6748710833, 0.1366027841), (0.6743023658, -0.1189376437))
                Line((0.6743023658, -0.1189376437), (0.0796450546, -0.1189376437))
                Line((0.0796450546, -0.1189376437), (0.0796450546, -0.0108181326))
                Line((0.0796450546, -0.0108181326), (0.1907678855, 0.0968395184))
                Line((0.1907678855, 0.0968395184), (0.404003588, 0.0968395184))
                Line((0.404003588, 0.0968395184), (0.0315919386, 0.481726307))
                Line((0.0315919386, 0.481726307), (0.3409338732, 0.481726307))
                Line((0.3409338732, 0.481726307), (0.6748710833, 0.1366027841))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-0.4564651301, 0.0063871102), 0.4956591567, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((-1.4716022719, -0.0171295804), (-1.1012143958, -0.4972620123))
                Line((-1.4716022719, 0.1278900113), (-1.4716022719, -0.0171295804))
                Line((-1.2207575728, 0.1278900113), (-1.4716022719, 0.1278900113))
                Line((-1.2207575728, 0.4826000937), (-1.2207575728, 0.1278900113))
                Line((-0.9816712189, 0.4826000937), (-1.2207575728, 0.4826000937))
                Line((-0.9816712189, -0.4953022881), (-0.9816712189, 0.4826000937))
                Line((-1.1012143958, -0.4972620123), (-0.9816712189, -0.4953022881))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((-1.7420442132, -0.5051009092), (-1.7420442132, -0.0210616985))
                Line((-1.9850500154, -0.5051009092), (-1.7420442132, -0.5051009092))
                Line((-1.9850500154, 0.4874161131), (-1.9850500154, -0.5051009092))
                Line((-1.7887137787, 0.4874161131), (-1.9850500154, 0.4874161131))
                Line((-1.5112111309, 0.1276904585), (-1.7887137787, 0.4874161131))
                Line((-1.508772571, -0.0210616985), (-1.5112111309, 0.1276904585))
                Line((-1.7420442132, -0.0210616985), (-1.508772571, -0.0210616985))
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.6836333042, perimeter: 5.8369021335
            with BuildLine():
                Line((1.7037579556, -0.1632616873), (2.0135054338, -0.1632616873))
                Line((1.6545265684, -0.2349354555), (1.7037579556, -0.1632616873))
                Line((1.6545265684, 0.4787976548), (1.6545265684, -0.2349354555))
                Line((1.3304694073, 0.4787976548), (1.6545265684, 0.4787976548))
                Line((1.3304694073, -0.1232258839), (1.3304694073, 0.4787976548))
                Line((1.2106827124, -0.2118214962), (1.3304694073, -0.1232258839))
                Line((0.0774365214, -0.2118214962), (1.2106827124, -0.2118214962))
                Line((0.3067089084, -0.4586469875), (0.0774365214, -0.2118214962))
                Line((1.4987672667, -0.4586469875), (0.3067089084, -0.4586469875))
                Line((1.6651009911, -0.3269661224), (1.4987672667, -0.4586469875))
                Line((1.6651009911, -0.4586469875), (1.6651009911, -0.3269661224))
                Line((2.0150948696, -0.4586469875), (1.6651009911, -0.4586469875))
                Line((2.0135054338, -0.1632616873), (2.0150948696, -0.4586469875))
            make_face()
            # Profile area: 0.1354354083, perimeter: 1.5879507271
            with BuildLine():
                Line((0.7944351559, 0.4637063884), (1.0347007362, 0.4637063884))
                Line((0.7944351559, -0.1102423693), (0.7944351559, 0.4637063884))
                Line((0.9530618173, -0.1102423693), (0.7944351559, -0.1102423693))
                Line((1.0347007362, -0.0498612894), (0.9530618173, -0.1102423693))
                Line((1.0347007362, 0.4637063884), (1.0347007362, -0.0498612894))
            make_face()
            # Profile area: 0.2406785957, perimeter: 2.6514131941
            with BuildLine():
                Line((0.3409338732, 0.481726307), (0.6748710833, 0.1366027841))
                Line((0.0315919386, 0.481726307), (0.3409338732, 0.481726307))
                Line((0.404003588, 0.0968395184), (0.0315919386, 0.481726307))
                Line((0.1907678855, 0.0968395184), (0.404003588, 0.0968395184))
                Line((0.0796450546, -0.0108181326), (0.1907678855, 0.0968395184))
                Line((0.0796450546, -0.1189376437), (0.0796450546, -0.0108181326))
                Line((0.6743023658, -0.1189376437), (0.0796450546, -0.1189376437))
                Line((0.6748710833, 0.1366027841), (0.6743023658, -0.1189376437))
            make_face()
            # Profile area: 0.5117275299, perimeter: 4.9221957796
            with BuildLine():
                CenterArc((-0.4564651301, 0.0063871102), 0.4956591567, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-0.4564651301, 0.0063871102), 0.2877326325, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.2600926688, perimeter: 1.8078774489
            with Locations((-0.4564651301, 0.0063871102)):
                Circle(0.2877326325)
            # Profile area: 0.3020529778, perimeter: 2.6935168821
            with BuildLine():
                Line((-1.1012143958, -0.4972620123), (-0.9816712189, -0.4953022881))
                Line((-0.9816712189, -0.4953022881), (-0.9816712189, 0.4826000937))
                Line((-0.9816712189, 0.4826000937), (-1.2207575728, 0.4826000937))
                Line((-1.2207575728, 0.4826000937), (-1.2207575728, 0.1278900113))
                Line((-1.2207575728, 0.1278900113), (-1.4716022719, 0.1278900113))
                Line((-1.4716022719, 0.1278900113), (-1.4716022719, -0.0171295804))
                Line((-1.4716022719, -0.0171295804), (-1.1012143958, -0.4972620123))
            make_face()
            # Profile area: 0.3088298555, perimeter: 2.752266024
            with BuildLine():
                Line((-1.7420442132, -0.0210616985), (-1.508772571, -0.0210616985))
                Line((-1.508772571, -0.0210616985), (-1.5112111309, 0.1276904585))
                Line((-1.5112111309, 0.1276904585), (-1.7887137787, 0.4874161131))
                Line((-1.7887137787, 0.4874161131), (-1.9850500154, 0.4874161131))
                Line((-1.9850500154, 0.4874161131), (-1.9850500154, -0.5051009092))
                Line((-1.9850500154, -0.5051009092), (-1.7420442132, -0.5051009092))
                Line((-1.7420442132, -0.5051009092), (-1.7420442132, -0.0210616985))
            make_face()
        # OneSide extrude, distance=-0.3175
        extrude(amount=-0.3175, mode=Mode.SUBTRACT)

        # Sketch11 -> Extrude9 (Cut)
        # Sketch on BRepFace
        # Sketch has 29 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1.27), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.6836333042, perimeter: 5.8369021335
            with BuildLine():
                Line((1.7037579556, -0.1632616873), (2.0135054338, -0.1632616873))
                Line((1.6545265684, -0.2349354555), (1.7037579556, -0.1632616873))
                Line((1.6545265684, 0.4787976548), (1.6545265684, -0.2349354555))
                Line((1.3304694073, 0.4787976548), (1.6545265684, 0.4787976548))
                Line((1.3304694073, -0.1232258839), (1.3304694073, 0.4787976548))
                Line((1.2106827124, -0.2118214962), (1.3304694073, -0.1232258839))
                Line((0.0774365214, -0.2118214962), (1.2106827124, -0.2118214962))
                Line((0.3067089084, -0.4586469875), (0.0774365214, -0.2118214962))
                Line((1.4987672667, -0.4586469875), (0.3067089084, -0.4586469875))
                Line((1.6651009911, -0.3269661224), (1.4987672667, -0.4586469875))
                Line((1.6651009911, -0.4586469875), (1.6651009911, -0.3269661224))
                Line((2.0150948696, -0.4586469875), (1.6651009911, -0.4586469875))
                Line((2.0135054338, -0.1632616873), (2.0150948696, -0.4586469875))
            make_face()
            # Profile area: 0.1354354083, perimeter: 1.5879507271
            with BuildLine():
                Line((0.7944351559, 0.4637063884), (1.0347007362, 0.4637063884))
                Line((0.7944351559, -0.1102423693), (0.7944351559, 0.4637063884))
                Line((0.9530618173, -0.1102423693), (0.7944351559, -0.1102423693))
                Line((1.0347007362, -0.0498612894), (0.9530618173, -0.1102423693))
                Line((1.0347007362, 0.4637063884), (1.0347007362, -0.0498612894))
            make_face()
            # Profile area: 0.2406785957, perimeter: 2.6514131941
            with BuildLine():
                Line((0.3409338732, 0.481726307), (0.6748710833, 0.1366027841))
                Line((0.0315919386, 0.481726307), (0.3409338732, 0.481726307))
                Line((0.404003588, 0.0968395184), (0.0315919386, 0.481726307))
                Line((0.1907678855, 0.0968395184), (0.404003588, 0.0968395184))
                Line((0.0796450546, -0.0108181326), (0.1907678855, 0.0968395184))
                Line((0.0796450546, -0.1189376437), (0.0796450546, -0.0108181326))
                Line((0.6743023658, -0.1189376437), (0.0796450546, -0.1189376437))
                Line((0.6748710833, 0.1366027841), (0.6743023658, -0.1189376437))
            make_face()
            # Profile area: 0.5117275299, perimeter: 4.9221957796
            with BuildLine():
                CenterArc((-0.4564651301, 0.0063871102), 0.4956591567, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-0.4564651301, 0.0063871102), 0.2877326325, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.3020529778, perimeter: 2.6935168821
            with BuildLine():
                Line((-1.1012143958, -0.4972620123), (-0.9816712189, -0.4953022881))
                Line((-0.9816712189, -0.4953022881), (-0.9816712189, 0.4826000937))
                Line((-0.9816712189, 0.4826000937), (-1.2207575728, 0.4826000937))
                Line((-1.2207575728, 0.4826000937), (-1.2207575728, 0.1278900113))
                Line((-1.2207575728, 0.1278900113), (-1.4716022719, 0.1278900113))
                Line((-1.4716022719, 0.1278900113), (-1.4716022719, -0.0171295804))
                Line((-1.4716022719, -0.0171295804), (-1.1012143958, -0.4972620123))
            make_face()
            # Profile area: 0.3088298555, perimeter: 2.752266024
            with BuildLine():
                Line((-1.7420442132, -0.0210616985), (-1.508772571, -0.0210616985))
                Line((-1.508772571, -0.0210616985), (-1.5112111309, 0.1276904585))
                Line((-1.5112111309, 0.1276904585), (-1.7887137787, 0.4874161131))
                Line((-1.7887137787, 0.4874161131), (-1.9850500154, 0.4874161131))
                Line((-1.9850500154, 0.4874161131), (-1.9850500154, -0.5051009092))
                Line((-1.9850500154, -0.5051009092), (-1.7420442132, -0.5051009092))
                Line((-1.7420442132, -0.5051009092), (-1.7420442132, -0.0210616985))
            make_face()
        # OneSide extrude, distance=-0.79375
        extrude(amount=-0.79375, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a complex polyhedron-shaped mechanical housing or enclosure with an irregular geometric form, featuring multiple angular faces, circular apertures or ports on one side, and internal cavity structures visible through the mesh rendering.
def model_120465_0d427fa4_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 18 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.27, perimeter: 2.4
            with BuildLine():
                Line((0, -1.1), (0, -1.4))
                Line((0, -1.4), (0.9, -1.4))
                Line((0.9, -1.4), (0.9, -1.1))
                Line((0.9, -1.1), (0, -1.1))
            make_face()
        # OneSide extrude, distance=1.1
        extrude(amount=1.1)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 18 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.9857531944, perimeter: 5.164680558
            with BuildLine():
                Line((0.9, -1.1), (0, -1.1))
                Line((0.9, 0), (0.9, -1.1))
                Line((0.5000000075, 0), (0.9, 0))
                Line((0.5000000075, 0), (0.5000000075, -0.7))
                Line((0.6000000075, -0.7), (0.5000000075, -0.7))
                Line((0.6000000075, -0.72), (0.6000000075, -0.7))
                Line((0.5000000075, -0.72), (0.6000000075, -0.72))
                Line((0.3876597284, -0.72), (0.5000000075, -0.72))
                Line((0.3876597284, -0.7), (0.3876597284, -0.72))
                Line((0.5000000075, -0.7), (0.3876597284, -0.7))
                Line((0, 0), (0.5000000075, 0))
                Line((0, -1.1), (0, 0))
            make_face()
            # Profile area: 0.002, perimeter: 0.24
            with BuildLine():
                Line((0.5000000075, -0.7), (0.5000000075, -0.72))
                Line((0.5000000075, -0.72), (0.6000000075, -0.72))
                Line((0.6000000075, -0.72), (0.6000000075, -0.7))
                Line((0.6000000075, -0.7), (0.5000000075, -0.7))
            make_face()
            # Profile area: 0.0022468056, perimeter: 0.264680558
            with BuildLine():
                Line((0.5000000075, -0.7), (0.3876597284, -0.7))
                Line((0.3876597284, -0.7), (0.3876597284, -0.72))
                Line((0.3876597284, -0.72), (0.5000000075, -0.72))
                Line((0.5000000075, -0.7), (0.5000000075, -0.72))
            make_face()
        # OneSide extrude, distance=0.6
        extrude(amount=0.6, mode=Mode.ADD)

        # Sketch2 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 12 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.6, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.9199799115, perimeter: 3.8726907481
            with BuildLine():
                Line((-0.031827313, 0.031827313), (-0.031827313, 0))
                Line((-0.031827313, 1.068172687), (-0.031827313, 0.031827313))
                Line((-0.031827313, 1.1), (-0.031827313, 1.068172687))
                Line((-0.868172687, 1.1), (-0.031827313, 1.1))
                Line((-0.868172687, 1.068172687), (-0.868172687, 1.1))
                Line((-0.868172687, 0.031827313), (-0.868172687, 1.068172687))
                Line((-0.868172687, 0), (-0.868172687, 0.031827313))
                Line((-0.031827313, 0), (-0.868172687, 0))
            make_face()
        # OneSide extrude, distance=0.4
        extrude(amount=0.4, mode=Mode.ADD)

        # Sketch3 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1.4), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            with Locations((0.45, 0.64)):
                Circle(0.3)
        # OneSide extrude, distance=-0.9
        extrude(amount=-0.9, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 10 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.9, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.21, perimeter: 1.9
            with BuildLine():
                Line((-0.4500000015, 0.6), (-0.4500000015, 0))
                Line((-0.4500000015, 0), (-0.1000000015, 0))
                Line((-0.1000000015, 0), (-0.1000000015, 0.6))
                Line((-0.1000000015, 0.6), (-0.4500000015, 0.6))
            make_face()
        # OneSide extrude, distance=-0.02
        extrude(amount=-0.02, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude6 (Cut)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.21, perimeter: 1.9
            with BuildLine():
                Line((0.1000000015, 0), (0.1000000015, 0.6))
                Line((0.4500000015, 0), (0.1000000015, 0))
                Line((0.4500000015, 0.6), (0.4500000015, 0))
                Line((0.1000000015, 0.6), (0.4500000015, 0.6))
            make_face()
        # OneSide extrude, distance=-0.02
        extrude(amount=-0.02, mode=Mode.SUBTRACT)

        # Sketch6 -> Extrude7 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.2510785543, perimeter: 2.2609381399
            with BuildLine():
                CenterArc((-0.468172687, 0.71), 0.1739181182, -36.3920130497, 252.7840260993)
                Line((-0.608172687, 0.6068132188), (-0.608172687, 0))
                Line((-0.608172687, 0), (-0.468172687, 0))
                Line((-0.328172687, 0), (-0.468172687, 0))
                Line((-0.328172687, 0.6068132188), (-0.328172687, 0))
            make_face()
        # OneSide extrude, distance=-0.02
        extrude(amount=-0.02, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a mesh headband or sweatband featuring a curved cylindrical shape with ventilated mesh paneling on the upper section and a solid fabric band on the lower portion, designed for comfort and breathability during athletic activities.
def model_121262_f4a03dbc_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 75.4296396127, perimeter: 30.7876080052
            Circle(4.9)
        # OneSide extrude, distance=3
        extrude(amount=3)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 50.2654824574, perimeter: 25.1327412287
            Circle(4)
        # OneSide extrude, distance=-1.5
        extrude(amount=-1.5, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 3, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((-1, 0)):
                Circle(0.5)
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((1, 0)):
                Circle(0.5)
        # OneSide extrude, distance=-2.5
        extrude(amount=-2.5, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 3, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 6.2257672548, perimeter: 16.9590696961
            with BuildLine():
                CenterArc((1, 0), 1.0625, -90, 180)
                Line((1, 1.0625), (-1.0000000149, 1.0625))
                CenterArc((-1, 0), 1.0625, 90.0000008036, 179.9999987926)
                Line((1, -1.0625), (-1.0000000075, -1.0625))
            make_face()
            with BuildLine():
                CenterArc((-1, 0), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1, 0), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.825
        extrude(amount=-0.825, mode=Mode.SUBTRACT)

        # Sketch6 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.5, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 5.3092915846, perimeter: 8.1681408993
            with Locations((-1.8, 1.95)):
                Circle(1.3)
            # Profile area: 5.3092915846, perimeter: 8.1681408993
            with Locations((1.8, 1.95)):
                Circle(1.3)
        # OneSide extrude, distance=-0.4
        extrude(amount=-0.4, mode=Mode.SUBTRACT)

        # Sketch7 -> Extrude6 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.9, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 2.0106192983, perimeter: 5.0265482457
            with Locations((-1.8, 1.95)):
                Circle(0.8)
            # Profile area: 1.0053096491, perimeter: 4.1132741229
            with BuildLine():
                CenterArc((1.8, 1.95), 0.8, 180, 180)
                Line((1, 1.95), (2.6, 1.95))
            make_face()
            # Profile area: 1.0053096491, perimeter: 4.1132741229
            with BuildLine():
                Line((1, 1.95), (2.6, 1.95))
                CenterArc((1.8, 1.95), 0.8, 0, 180)
            make_face()
        # OneSide extrude, distance=-0.475
        extrude(amount=-0.475, mode=Mode.SUBTRACT)

        # Sketch8 -> Extrude7 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.5, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 10.1995913617, perimeter: 19.8959478832
            with BuildLine():
                CenterArc((0, 0), 2.1, 76.1404244045, 27.7191511911)
                CenterArc((-1.8, 1.95), 1.3, -98.5006646119, 102.4201091386)
                CenterArc((0, 0), 2.1, 161.5592043192, 216.8815913616)
                CenterArc((1.8, 1.95), 1.3, 176.0805554733, 102.4201091386)
            make_face()
            with BuildLine():
                CenterArc((1, 0), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-1, 0), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.1
        extrude(amount=-0.1, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical housing or motor casing with a curved, rounded top featuring ventilation slots or cooling fins, two prominent vertical posts or mounting tabs on the upper surface, and a mesh or perforated pattern visible throughout the structure for thermal management.
def model_121264_68fcc38a_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 41.8538681275, perimeter: 22.9336263712
            Circle(3.65)
        # OneSide extrude, distance=2.2
        extrude(amount=2.2)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2.2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 31.1724531052, perimeter: 19.7920337176
            Circle(3.15)
        # OneSide extrude, distance=0.45
        extrude(amount=0.45, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2.65, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 26.4207942167, perimeter: 18.2212373908
            Circle(2.9)
        # OneSide extrude, distance=0.55
        extrude(amount=0.55, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 3.2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.6033953503, perimeter: 37.9661472186
            with BuildLine():
                CenterArc((0, 0), 3.1425, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 2.9, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 26.4207942167, perimeter: 18.2212373908
            Circle(2.9)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)

        # Sketch5 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 3.4, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 16.5108169055, perimeter: 14.4042023167
            Circle(2.2925)
        # OneSide extrude, distance=-0.15
        extrude(amount=-0.15, mode=Mode.SUBTRACT)

        # Sketch6 -> Extrude6 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.9245903529, perimeter: 3.4086280291
            with Locations((-2, 0)):
                Circle(0.5425)
            # Profile area: 0.9245903529, perimeter: 3.4086280291
            with Locations((2, 0)):
                Circle(0.5425)
        # OneSide extrude, distance=-2.6
        extrude(amount=-2.6, mode=Mode.SUBTRACT)

        # Sketch7 -> Extrude7 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.9245903529, perimeter: 3.4086280291
            with Locations((0, 1.25)):
                Circle(0.5425)
            # Profile area: 0.9245903529, perimeter: 3.4086280291
            with Locations((0, -1.25)):
                Circle(0.5425)
        # OneSide extrude, distance=-2.6
        extrude(amount=-2.6, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a curved sheet metal or plastic duct component with a tapered, tubular shape featuring a rectangular opening at the top and a flared or angled exit, likely designed for air or fluid flow redirection in HVAC or ventilation systems.
def model_122579_2663ded3_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Tip -> Extrude4 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 7.8735079203, perimeter: 15.4031769261
            with BuildLine():
                CenterArc((-6.7827760994, 1.6224070921), 1.8666181843, 53.6717085759, 38.4589647869)
                Line((-6.8521745277, 3.4877347588), (-8.4132680438, 3.0084340118))
                CenterArc((-8.4843146675, -0.4562892062), 3.4654515723, 51.165250667, 37.6600230932)
                CenterArc((-12.6150153295, -4.6810978356), 9.3639288508, 34.7904525255, 12.894968251)
                CenterArc((0.3257725776, 3.699678637), 6.0662231965, -149.9473636814, 20.1958099372)
                Line((-2.7413407448, 1.5678007202), (-3.5533336048, -0.9641823275))
                CenterArc((1.2694297965, 12.6671375296), 11.8017607984, -126.0570275928, 16.1895907769)
            make_face()
        # Symmetric extrude, each_side=0.6
        extrude(amount=0.6, both=True)
    return part.part


# Description: This is a folding or articulated sail-like structure featuring a composite design with triangular panels in blue and dark gray, connected by internal bracing and struts, designed to fold or collapse along a central hinge for compact storage or deployment.
def model_125011_9b62f62f_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 34 constraints, 10 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 3.452802603, perimeter: 46.2801408837
            with BuildLine():
                Line((-6.9439774773, 0.8888470665), (-1.2676018909, 0.8888470665))
                Line((-6.9439774773, 0.8888470665), (-6.9439774773, 0.7388470665))
                Line((-6.9439774773, 0.7388470665), (-1.2676018909, 0.7388470665))
                CenterArc((-1.2676018909, 1.0888470665), 0.35, -90, 106.4526763527)
                Line((-0.9319329939, 1.1879752241), (-3.3700724124, 9.4440307077))
                CenterArc((-3.8016467084, 9.3165802194), 0.45, 16.4526763527, 150.1081586255)
                Line((-5.5701533305, 3.8518208206), (-4.2393244654, 9.4211659787))
                Line((-5.5701533305, 3.8518208206), (-6.4455088444, 4.0609923393))
                Line((-6.4455088444, 4.0609923393), (-6.3757850048, 4.3527775106))
                CenterArc((-6.4244158667, 4.3643981505), 0.05, -13.4391650218, 90)
                Line((-6.4614260886, 4.4246496524), (-6.4127952268, 4.4130290124))
                CenterArc((-6.4730467286, 4.3760187905), 0.05, 76.5608349782, 90)
                Line((-6.60302207, 4.0472233972), (-6.5216775905, 4.3876394304))
                CenterArc((-6.5057603462, 4.0239821174), 0.1, 166.5608349782, 90)
                Line((-5.5563843884, 3.694307595), (-6.5290016261, 3.9267203936))
                CenterArc((-5.5331431085, 3.7915693188), 0.1, -103.4391650218, 90)
                Line((-5.4358813847, 3.7683280389), (-4.0934318797, 9.3863040589))
                CenterArc((-3.8016467084, 9.3165802194), 0.3, 16.4526763527, 150.1081586255)
                Line((-1.0757910926, 1.145491728), (-3.5139305111, 9.4015472116))
                CenterArc((-1.2676018909, 1.0888470665), 0.2, -90, 106.4526763527)
            make_face()
        # OneSide extrude, distance=8
        extrude(amount=8)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.7388470665, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.2827433388, perimeter: 5.6548667765
            with BuildLine():
                CenterArc((0.6978236449, 6.0078310874), 0.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0.6978236449, 6.0078310874), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1, mode=Mode.ADD)

        # Sketch7 -> Extrude4 (Cut)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            with Locations((4, 3.645491728)):
                Circle(1)
        # OneSide extrude, distance=3
        extrude(amount=3, mode=Mode.SUBTRACT)

        # Sketch8 -> Extrude5 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.84, perimeter: 3.8
            with BuildLine():
                Line((4.6, -6.3201533305), (3.4, -6.3201533305))
                Line((4.6, -5.6201533305), (4.6, -6.3201533305))
                Line((3.4, -5.6201533305), (4.6, -5.6201533305))
                Line((3.4, -6.3201533305), (3.4, -5.6201533305))
            make_face()
        # OneSide extrude, distance=2.5
        extrude(amount=2.5, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a curved, dark-colored bracket or housing component with a C-shaped profile, featuring internal ribbing/reinforcement structures and blue-highlighted cutouts or apertures on its upper surfaces.
def model_128366_d8d9d0fd_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.5, perimeter: 7.8
            with BuildLine():
                Line((5.5, -2.4), (3, -2.4))
                Line((5.5, -1), (5.5, -2.4))
                Line((3, -1), (5.5, -1))
                Line((3, -2.4), (3, -1))
            make_face()
            # Profile area: 0.7696902001, perimeter: 3.5991148575
            with BuildLine():
                CenterArc((5.5, -1.7), 0.7, -90, 180)
                Line((5.5, -1), (5.5, -2.4))
            make_face()
        # OneSide extrude, distance=-1.451
        extrude(amount=-1.451)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 10 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 2.4), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.3584000473, perimeter: 2.4240001848
            with BuildLine():
                Line((5.5, -0.912000006), (5.5, -0.400000006))
                Line((5.5, -0.912000006), (6.2000000924, -0.912000006))
                Line((6.2000000924, -0.912000006), (6.2000000924, -0.400000006))
                Line((6.2000000924, -0.400000006), (5.5, -0.400000006))
            make_face()
            # Profile area: 0.9215999527, perimeter: 4.6239998152
            with BuildLine():
                Line((4.900000073, -0.400000006), (3.7000000924, -0.400000006))
                Line((3.7000000924, -0.400000006), (3.7000000924, -0.912000006))
                Line((3.7000000924, -0.912000006), (5.5, -0.912000006))
                Line((5.5, -0.912000006), (5.5, -0.400000006))
                Line((5.5, -0.400000006), (4.900000073, -0.400000006))
            make_face()
        # OneSide extrude, distance=-1.8
        extrude(amount=-1.8, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2827432995, perimeter: 1.8849554611
            with Locations((-5.5, 1.7)):
                Circle(0.2999999791)
        # OneSide extrude, distance=-1.8
        extrude(amount=-1.8, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 2.4), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.8267890393, perimeter: 3.7302254702
            with BuildLine():
                Line((3, 0), (3, -1.451))
                CenterArc((3, -0.7255), 0.7255, 90, 180)
            make_face()
        # OneSide extrude, distance=-1.4
        extrude(amount=-1.4, mode=Mode.ADD)

        # Sketch5 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 2.4), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.4938968497, perimeter: 2.4912829743
            with Locations((3, -0.7255)):
                Circle(0.3965)
        # OneSide extrude, distance=-1.5
        extrude(amount=-1.5, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a hexagonal or coffin-shaped enclosure or housing with a sloped top surface featuring a transparent or translucent panel, designed to contain or protect internal components while allowing visibility into the upper section.
def model_128996_9ff71fb1_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 34.4, perimeter: 25.2
            with BuildLine():
                Line((0, 0), (-4, 0))
                Line((-4, 0), (-4, -8.6))
                Line((-4, -8.6), (0, -8.6))
                Line((0, 0), (0, -8.6))
            make_face()
        # OneSide extrude, distance=3
        extrude(amount=3)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 2.0106192983, perimeter: 5.0265482457
            with Locations((2, 1.5)):
                Circle(0.8)
        # OneSide extrude, distance=1.2
        extrude(amount=1.2, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -1.2), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 1.1309733553, perimeter: 3.7699111843
            with Locations((2, 1.5)):
                Circle(0.6)
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -0.2), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((2, 1.5)):
                Circle(0.5)
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            with Locations((2, 1.5)):
                Circle(0.4)
        # OneSide extrude, distance=-0.8
        extrude(amount=-0.8, mode=Mode.SUBTRACT)

        # Sketch7 -> Extrude6 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 3, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((1.3000000268, 0.5)):
                Circle(0.2)
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((2.6999999732, 0.5)):
                Circle(0.2)
        # OneSide extrude, distance=-0.9
        extrude(amount=-0.9, mode=Mode.SUBTRACT)

        # Sketch8 -> Extrude7 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((-0.5, 0.8)):
                Circle(0.2)
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((-0.5, 2.2)):
                Circle(0.2)
        # OneSide extrude, distance=-0.9
        extrude(amount=-0.9, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical intake or exhaust manifold component mounted on a rectangular base plate, featuring a curved duct/pipe section extending from one side and a perforated or mesh-covered cylindrical chamber on top.
def model_129579_144d8158_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 9 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 55.25, perimeter: 38
            with BuildLine():
                Line((15.3402268012, -1.1455887998), (15.3402268012, 1.3544112002))
                Line((14.3402268012, 1.3544112002), (15.3402268012, 1.3544112002))
                Line((14.3402268012, 4.3544112002), (14.3402268012, 1.3544112002))
                Line((14.3402268012, 4.3544112002), (12.3402268012, 4.3544112002))
                Line((12.3402268012, 4.3544112002), (12.3402268012, 3.3544112002))
                Line((12.3402268012, 3.3544112002), (9.8402268012, 3.3544112002))
                Line((9.8402268012, 3.3544112002), (9.8402268012, 4.3544112002))
                Line((9.8402268012, 4.3544112002), (7.8402268012, 4.3544112002))
                Line((7.8402268012, 4.3544112002), (7.8402268012, 1.3544112002))
                Line((7.8402268012, 1.3544112002), (6.8402268012, 1.3544112002))
                Line((6.8402268012, 1.3544112002), (6.8402268012, -1.1455887998))
                Line((7.8402268012, -1.1455887998), (6.8402268012, -1.1455887998))
                Line((7.8402268012, -4.1455887998), (7.8402268012, -1.1455887998))
                Line((9.8402268012, -4.1455887998), (7.8402268012, -4.1455887998))
                Line((9.8402268012, -3.1455887998), (9.8402268012, -4.1455887998))
                Line((12.3402268012, -3.1455887998), (9.8402268012, -3.1455887998))
                Line((12.3402268012, -4.1455887998), (12.3402268012, -3.1455887998))
                Line((14.3402268012, -4.1455887998), (12.3402268012, -4.1455887998))
                Line((14.3402268012, -4.1455887998), (14.3402268012, -1.1455887998))
                Line((14.3402268012, -1.1455887998), (15.3402268012, -1.1455887998))
            make_face()
        # OneSide extrude, distance=0.4
        extrude(amount=0.4)

        # Sketch5 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.4, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 11.8791472214, perimeter: 14.1393797974
            with BuildLine():
                Line((-11, -2.75), (-11, 2.75))
                CenterArc((-11, 0), 2.75, -90, 180)
            make_face()
            # Profile area: 11.8791472214, perimeter: 14.1393797974
            with BuildLine():
                CenterArc((-11, 0), 2.75, 90, 180)
                Line((-11, -2.75), (-11, 2.75))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)

        # Sketch6 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.4, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 11.9805036242, perimeter: 14.1761137261
            with BuildLine():
                Line((-11.0253580431, -2.7498830829), (-11.0114989895, 2.7499759587))
                CenterArc((-11, 0), 2.75, -90.5283379777, 180.7679181542)
            make_face()
            # Profile area: 11.7777908186, perimeter: 14.1023988751
            with BuildLine():
                CenterArc((-11, 0), 2.75, 90.2395801765, 179.2320818458)
                Line((-11.0253580431, -2.7498830829), (-11.0114989895, 2.7499759587))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)
    return part.part


# Description: This is a canopy or shelter frame structure with a rectangular top panel supported by four cylindrical legs, featuring a skeletal frame design with a small cylindrical component shown separately.
def model_129611_59e33fba_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 9 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 12.5, perimeter: 15
            with BuildLine():
                Line((-5, 2.5), (0, 2.5))
                Line((-5, 0), (-5, 2.5))
                Line((0, 0), (-5, 0))
                Line((0, 2.5), (0, 0))
            make_face()
            # Profile area: 12.5, perimeter: 15
            with BuildLine():
                Line((-5, 15), (0, 15))
                Line((-5, 12.5), (-5, 15))
                Line((0, 12.5), (-5, 12.5))
                Line((0, 15), (0, 12.5))
            make_face()
        # OneSide extrude, distance=20
        extrude(amount=20)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 20, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 12.5, perimeter: 15
            with BuildLine():
                Line((0, 0), (5, 0))
                Line((0, -2.5), (0, 0))
                Line((0, -2.5), (5, -2.5))
                Line((5, -2.5), (5, 0))
            make_face()
            # Profile area: 317.5, perimeter: 74
            with BuildLine():
                Line((22, -15), (0, -15))
                Line((22, 0), (22, -15))
                Line((5, 0), (22, 0))
                Line((5, -2.5), (5, 0))
                Line((0, -2.5), (5, -2.5))
                Line((0, -15), (0, -2.5))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 20, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 11.25, perimeter: 14
            with BuildLine():
                Line((-17.5, 0), (-17.5, -2.5))
                Line((-22, 0), (-17.5, 0))
                Line((-22, -2.5), (-22, 0))
                Line((-17.5, -2.5), (-22, -2.5))
            make_face()
        # OneSide extrude, distance=20
        extrude(amount=20, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 20, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 11.25, perimeter: 14
            with BuildLine():
                Line((-17.5, -12.5), (-22, -12.5))
                Line((-22, -12.5), (-22, -15))
                Line((-22, -15), (-17.5, -15))
                Line((-17.5, -15), (-17.5, -12.5))
            make_face()
        # OneSide extrude, distance=20
        extrude(amount=20, mode=Mode.ADD)

        # Sketch5 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 20.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 37.5, perimeter: 25
            with BuildLine():
                Line((15, -10), (15, -5))
                Line((15, -5), (7.5, -5))
                Line((7.5, -5), (7.5, -10))
                Line((7.5, -10), (15, -10))
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2, mode=Mode.ADD)

        # Sketch7 -> Extrude6 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 9.6211275016, perimeter: 10.9955742876
            with Locations((10, 0)):
                Circle(1.75)
        # OneSide extrude, distance=4.5
        extrude(amount=4.5)

        # Sketch8 -> Extrude7 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 4.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 6.2831853072, perimeter: 8.8857658763
            with Locations((-10, 0)):
                Circle(1.4142135624)
        # OneSide extrude, distance=-4
        extrude(amount=-4, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a hexagonal or polygonal prism-like container or housing with an asymmetrical design, featuring a hollow or open interior structure visible on the left side with internal triangular bracing elements, and solid exterior faces on the right side.
def model_130490_15f074ea_0003():
    """Model: Main Body"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1075, perimeter: 130.9901951359
            with BuildLine():
                Line((15, 20), (-15, 20))
                Line((-15, 20), (-15, 5))
                Line((-15, 5), (-10, -20))
                Line((10, -20), (-10, -20))
                Line((10, -20), (15, 5))
                Line((15, 14), (15, 5))
                Line((15, 20), (15, 14))
            make_face()
        # OneSide extrude, distance=20
        extrude(amount=20)

        # Sketch6 -> Extrude6 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((-13.7000002041, 18.8000002801)):
                Circle(0.2)
        # OneSide extrude, distance=-0.8
        extrude(amount=-0.8, mode=Mode.SUBTRACT)

        # Sketch7 -> Extrude7 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((-14.5000002161, 5.0000000745)):
                Circle(0.2)
        # OneSide extrude, distance=-0.8
        extrude(amount=-0.8, mode=Mode.SUBTRACT)

        # Sketch8 -> Extrude8 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((-11.9497472927, -7.5340114114)):
                Circle(0.2)
        # OneSide extrude, distance=-0.8
        extrude(amount=-0.8, mode=Mode.SUBTRACT)

        # Sketch9 -> Extrude9 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.0628318531, perimeter: 1.0283185307
            with BuildLine():
                CenterArc((-8.9947876839, -19), 0.2, 180, 180)
                Line((-8.7947876839, -19), (-9.1947876839, -19))
            make_face()
            # Profile area: 0.0628318531, perimeter: 1.0283185307
            with BuildLine():
                Line((-8.7947876839, -19), (-9.1947876839, -19))
                CenterArc((-8.9947876839, -19), 0.2, 0, 180)
            make_face()
        # OneSide extrude, distance=-0.8
        extrude(amount=-0.8, mode=Mode.SUBTRACT)

        # Sketch10 -> Extrude10 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((0, 19.5000002906)):
                Circle(0.2)
        # OneSide extrude, distance=-0.8
        extrude(amount=-0.8, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a perforated hexagonal or cubic structural component featuring multiple triangular and rectangular cutouts across its faces, designed for lightweight strength with open lattice-like geometry.
def model_130759_c37b385b_0002():
    """Model: D6"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 2.25, perimeter: 6
            with BuildLine():
                Line((-0.75, 0.75), (0.75, 0.75))
                Line((-0.75, -0.75), (-0.75, 0.75))
                Line((0.75, -0.75), (-0.75, -0.75))
                Line((0.75, 0.75), (0.75, -0.75))
            make_face()
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -0.75, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((0, 0.75)):
                Circle(0.25)
        # OneSide extrude, distance=-0.25
        extrude(amount=-0.25, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.75, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((-0.2121320344, 0.5378679656)):
                Circle(0.15)
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((0.2121320344, 0.9621320344)):
                Circle(0.15)
        # OneSide extrude, distance=-0.15
        extrude(amount=-0.15, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 13 constraints, 12 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.75, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((-0.3, 1.2)):
                Circle(0.15)
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((0.3, 1.2)):
                Circle(0.15)
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((0.3, 0.75)):
                Circle(0.15)
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((-0.3, 0.75)):
                Circle(0.15)
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((-0.3, 0.3)):
                Circle(0.15)
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((0.3, 0.3)):
                Circle(0.15)
        # OneSide extrude, distance=-0.15
        extrude(amount=-0.15, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 8 constraints, 9 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-0.75, 0, 0), x_dir=(0, -1, 0), z_dir=(-1, 0, 0))):
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((0, 0.7500000112)):
                Circle(0.15)
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((-0.3535533961, 1.1035533963)):
                Circle(0.15)
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((0.3535533954, 1.103553397)):
                Circle(0.15)
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((0.3535533855, 0.3964466155)):
                Circle(0.15)
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((-0.3535533855, 0.3964466155)):
                Circle(0.15)
        # OneSide extrude, distance=-0.15
        extrude(amount=-0.15, mode=Mode.SUBTRACT)

        # Sketch7 -> Extrude6 (Cut)
        # Sketch on BRepFace
        # Sketch has 10 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1.5), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0706858368, perimeter: 0.9424778101
            with Locations((0, 0.3000000045)):
                Circle(0.1500000022)
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((-0.2598076224, -0.1499999978)):
                Circle(0.15)
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((0.2598076224, -0.1499999978)):
                Circle(0.15)
        # OneSide extrude, distance=-0.15
        extrude(amount=-0.15, mode=Mode.SUBTRACT)

        # Sketch6 -> Extrude7 (Cut)
        # Sketch on BRepFace
        # Sketch has 8 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((-0.3535533906, -0.3535533906)):
                Circle(0.15)
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((-0.3535533906, 0.3535533906)):
                Circle(0.15)
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((0.3535533906, 0.3535533906)):
                Circle(0.15)
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((0.3535533906, -0.3535533906)):
                Circle(0.15)
        # OneSide extrude, distance=-0.15
        extrude(amount=-0.15, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical sleeve or tube with a curved, tapered shape featuring a open top end and vertical ribbed or fluted surface texture on its sides, designed for containment or structural support.
def model_130917_2e98fb39_0002():
    """Model: Cylinder"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 314.159265359, perimeter: 62.8318530718
            Circle(10)
        # OneSide extrude, distance=18
        extrude(amount=18)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 18, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 254.4690049408, perimeter: 56.5486677646
            Circle(9)
        # OneSide extrude, distance=-16
        extrude(amount=-16, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 78.5398163397, perimeter: 31.4159265359
            Circle(5)
        # OneSide extrude, distance=4
        extrude(amount=4, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 8 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 6, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 24.1935, perimeter: 20.32
            with BuildLine():
                Line((3.175, -1.905), (-3.175, -1.905))
                Line((3.175, 1.905), (3.175, -1.905))
                Line((-3.175, 1.905), (3.175, 1.905))
                Line((-3.175, -1.905), (-3.175, 1.905))
            make_face()
        # OneSide extrude, distance=-3.5
        extrude(amount=-3.5, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a pyramid-shaped housing or enclosure with a pointed apex and a rectangular base, featuring internal structural framing/ribbing visible through transparent sections and what appears to be a recessed opening or cavity on one of the lower faces.
def model_131580_c88dee64_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 12.5, perimeter: 15
            with BuildLine():
                Line((2.5, 0), (5, 0))
                Line((2.5, -5), (2.5, 0))
                Line((5, -5), (2.5, -5))
                Line((5, 0), (5, -5))
            make_face()
            # Profile area: 12.5, perimeter: 15
            with BuildLine():
                Line((0, 0), (2.5, 0))
                Line((0, -5), (0, 0))
                Line((2.5, -5), (0, -5))
                Line((2.5, -5), (2.5, 0))
            make_face()
        # OneSide extrude, distance=5
        extrude(amount=5)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 5), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 7.0873412263, perimeter: 13.1698729811
            with BuildLine():
                Line((0, 5), (0, 0))
                Line((0, 0), (2.5, 4.3301270189))
                Line((2.5, 4.3301270189), (2.5, 5))
                Line((0, 5), (2.5, 5))
            make_face()
        # OneSide extrude, distance=-5
        extrude(amount=-5, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 5), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 7.0873412263, perimeter: 13.1698729811
            with BuildLine():
                Line((5, 5), (2.5, 5))
                Line((2.5, 5), (2.5, 4.3301270189))
                Line((2.5, 4.3301270189), (5, 0))
                Line((5, 0), (5, 5))
            make_face()
        # OneSide extrude, distance=-5
        extrude(amount=-5, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 9 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(3.75, 2.1650635095, 0), x_dir=(0, 0, -1), z_dir=(0.8660254038, 0.5, 0))):
            # Profile area: 12.25, perimeter: 14
            with BuildLine():
                Line((-4.25, -1.75), (-0.75, -1.75))
                Line((-0.75, -1.75), (-0.75, 1.75))
                Line((-0.75, 1.75), (-4.25, 1.75))
                Line((-4.25, 1.75), (-4.25, -1.75))
            make_face()
        # OneSide extrude, distance=-0.3
        extrude(amount=-0.3, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(3.4901923789, 2.0150635095, 0), x_dir=(0, 0, -1), z_dir=(0.8660254038, 0.5, 0))):
            # Profile area: 8.1562415863, perimeter: 11.4253327144
            with BuildLine():
                Line((-3.9234132322, 1.4520347871), (-3.9234132322, -1.4532641032))
                Line((-3.9234132322, -1.4532641032), (-1.1160457652, -1.4532641032))
                Line((-1.1160457652, -1.4532641032), (-1.1160457652, 1.4520347871))
                Line((-1.1160457652, 1.4520347871), (-3.9234132322, 1.4520347871))
            make_face()
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.SUBTRACT)

        # Sketch6 -> Extrude6 (Cut)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 0, 5), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.6077080841, perimeter: 2.7634552665
            with Locations((2.6244743041, 1.5145312)):
                Circle(0.4398175657)
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a dark blue mounting bracket with a vertical rectangular body featuring a central oval hole, a base flange at the bottom, and vertical ribbing/reinforcement grooves along its sides for structural rigidity.
def model_132291_265066d2_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 13 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 17.7373451754, perimeter: 45.2566370614
            with BuildLine():
                Line((0.8, 16.8), (0, 16.8))
                Line((0, 16.8), (0, 0.8))
                Line((0, 0.8), (0, 0))
                Line((0, 0), (6, 0))
                Line((6, 0), (6, 0.8))
                Line((6, 0.8), (1.6, 0.8))
                CenterArc((1.6, 1.6), 0.8, -180, 90)
                Line((0.8, 1.6), (0.8, 16.8))
            make_face()
        # OneSide extrude, distance=6
        extrude(amount=6)

        # Sketch2 -> Extrude3 (Join)
        # Sketch on YZ construction plane
        # Sketch has 15 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 2, perimeter: 6
            with BuildLine():
                Line((-6, 0), (-6, -2))
                Line((-6, -2), (-5, -2))
                Line((-5, -2), (-5, 0))
                Line((-5, 0), (-6, 0))
            make_face()
            # Profile area: 2, perimeter: 6
            with BuildLine():
                Line((-1, 0), (-1, -2))
                Line((-1, -2), (0, -2))
                Line((0, -2), (0, 0))
                Line((0, 0), (-1, 0))
            make_face()
        # OneSide extrude, distance=6
        extrude(amount=6, mode=Mode.ADD)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on YZ construction plane
        # Sketch has 15 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 8.0424771932, perimeter: 10.0530964915
            with Locations((-3, 14)):
                Circle(1.6)
        # OneSide extrude, distance=2.6461
        extrude(amount=2.6461, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 6), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.2827434596, perimeter: 1.8849559947
            with Locations((4, -1)):
                Circle(0.3000000641)
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            with Locations((1.5, -1)):
                Circle(0.3)
        # OneSide extrude, distance=-7.237
        extrude(amount=-7.237, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 9 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.8, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            with Locations((-2.660724805, 2.0000000298)):
                Circle(0.3)
            # Profile area: 0.2827432911, perimeter: 1.884955433
            with Locations((-5.0000000745, 4.0000000298)):
                Circle(0.2999999747)
        # OneSide extrude, distance=-2.08
        extrude(amount=-2.08, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude6 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0.8, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 7.146204182, perimeter: 17.7529182092
            with BuildLine():
                Line((-2.5428342515, 1.6), (-2.5428342515, 9.5810642051))
                Line((-2.5428342515, 9.5810642051), (-3.4382291511, 9.5810642051))
                Line((-3.4382291511, 9.5810642051), (-3.4382291511, 1.6))
                Line((-3.4382291511, 1.6), (-2.5428342515, 1.6))
            make_face()
        # OneSide extrude, distance=4.067
        extrude(amount=4.067, mode=Mode.ADD)

        # Sketch6 -> Extrude7 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 3.4382291511), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 14.8970511315, perimeter: 20.4617958684
            with BuildLine():
                Line((1.2099413499, 9.5810642051), (4.7909597178, 1.6))
                Line((4.7909597178, 1.6), (4.867, 1.6))
                Line((4.867, 1.6), (4.867, 9.5810642051))
                Line((4.867, 9.5810642051), (1.2099413499, 9.5810642051))
            make_face()
        # OneSide extrude, distance=-12.9459
        extrude(amount=-12.9459, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a rectangular tray or shallow pan with raised flanged edges, featuring a flat bottom surface and angled side walls that slope outward, with what appears to be a small notch or cutout on the upper right corner.
def model_132668_067b89d4_0001():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 102, perimeter: 41
            with BuildLine():
                Line((-6, 4.25), (6, 4.25))
                Line((-6, -4.25), (-6, 4.25))
                Line((6, -4.25), (-6, -4.25))
                Line((6, 4.25), (6, -4.25))
            make_face()
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)

        # Sketch3 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 82.5, perimeter: 37
            with BuildLine():
                Line((5.5, -3.75), (5.5, 3.75))
                Line((5.5, 3.75), (-5.5, 3.75))
                Line((-5.5, 3.75), (-5.5, -3.75))
                Line((-5.5, -3.75), (5.5, -3.75))
            make_face()
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((5.2, -3.45)):
                Circle(0.15)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3, mode=Mode.ADD)

        # Sketch5 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.8, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            with Locations((5.2, -3.45)):
                Circle(0.1)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)

        # Sketch6 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 10 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.7, perimeter: 3.8
            with BuildLine():
                Line((-2.8, -3.75), (-2.8, -4.25))
                Line((-4.2, -3.75), (-2.8, -3.75))
                Line((-4.2, -4.25), (-4.2, -3.75))
                Line((-2.8, -4.25), (-4.2, -4.25))
            make_face()
            # Profile area: 0.7000001252, perimeter: 3.8000001788
            with BuildLine():
                Line((-5.5, 1.05), (-6.0000000894, 1.05))
                Line((-5.5, 2.45), (-5.5, 1.05))
                Line((-6.0000000894, 2.45), (-5.5, 2.45))
                Line((-6.0000000894, 1.05), (-6.0000000894, 2.45))
            make_face()
        # OneSide extrude, distance=-0.8
        extrude(amount=-0.8, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a motor housing or gearbox component featuring a rectangular main body with an angled top cover, a circular mounting flange on the left side, and ribbed reinforcement ribs on the bottom surface for structural support.
def model_132757_27127ea1_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 9 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.3070509723, perimeter: 2.906757159
            with BuildLine():
                Line((1.9835617142, 0.5582744952), (3.1, 0))
                Line((2, 0), (1.9835617142, 0.5582744952))
                Line((3.1, 0), (2, 0))
            make_face()
            # Profile area: 1.3707733353, perimeter: 5.3544324643
            with BuildLine():
                Line((2.490553415, 2.1139003903), (1.9451178092, 1.8639003903))
                Line((1.9835617142, 0.5582744952), (1.9451178092, 1.8639003903))
                Line((1.9835617142, 0.5582744952), (3.1, 0))
                Line((3.1, 0), (2.490553415, 2.1139003903))
            make_face()
        # OneSide extrude, distance=1.45
        extrude(amount=1.45)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 9 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.4506439776, perimeter: 5.0955788247
            with BuildLine():
                Line((0.4167716422, 1.3417472116), (1.9835617142, 0.5582744952))
                Line((1.9835617142, 0.5582744952), (1.9451178092, 1.8639003903))
                Line((1.9451178092, 1.8639003903), (1.9451178092, 2.1139003903))
                Line((1.9451178092, 2.1139003903), (1.590553415, 2.1139003903))
                CenterArc((2.0817557005, 0.0889700741), 2.0836560346, 103.6352815365, 6.0138035111)
                CenterArc((2.0817557005, 0.0889700741), 2.0836560346, 109.6490850476, 33.3921645927)
            make_face()
            # Profile area: 0.0681794507, perimeter: 1.3954356057
            with BuildLine():
                Line((2.490553415, 2.1139003903), (1.9451178092, 2.1139003903))
                Line((1.9451178092, 1.8639003903), (1.9451178092, 2.1139003903))
                Line((2.490553415, 2.1139003903), (1.9451178092, 1.8639003903))
            make_face()
            # Profile area: 1.8876079305, perimeter: 5.743339125
            with BuildLine():
                CenterArc((2.0817557005, 0.0889700741), 2.0836560346, 143.0412496403, 39.4059681038)
                Line((0, 0), (2, 0))
                Line((2, 0), (1.9835617142, 0.5582744952))
                Line((0.4167716422, 1.3417472116), (1.9835617142, 0.5582744952))
            make_face()
        # OneSide extrude, distance=0.25
        extrude(amount=0.25, mode=Mode.ADD)

        # Sketch5 -> Extrude6 (Join)
        # Sketch on BRepFace
        # Sketch has 6 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.25, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0023559444, perimeter: 0.8120132671
            with BuildLine():
                Line((-1.9882211774, 0), (-2, 0))
                Line((-2, 0), (-1.9882211774, -0.4000305347))
                Line((-1.9882211774, -0.2101986246), (-1.9882211774, -0.4000305347))
                Line((-1.9882211774, 0), (-1.9882211774, -0.2101986246))
            make_face()
        # OneSide extrude, distance=1.2
        extrude(amount=1.2, mode=Mode.ADD)

        # Sketch7 -> Extrude7 (Join)
        # Sketch on BRepFace
        # Sketch has 8 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(1.9882211774, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.0500072361, perimeter: 0.9000578888
            with BuildLine():
                Line((-0.4000305347, 1.2), (-0.2000031807, 1.2))
                Line((-0.2, 1.45), (-0.2000031807, 1.2))
                Line((-0.2, 1.45), (-0.4000305347, 1.45))
                Line((-0.4000305347, 1.45), (-0.4000305347, 1.2))
            make_face()
        # OneSide extrude, distance=0.25
        extrude(amount=0.25, mode=Mode.ADD)

        # Sketch7 -> Extrude8 (Join)
        # Sketch on BRepFace
        # Sketch has 8 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(1.9882211774, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.1900202452, perimeter: 2.3000426215
            with BuildLine():
                Line((-0.4000305347, 1.2), (-0.4000305347, 0.25))
                Line((-0.4000305347, 0.25), (-0.2000152674, 0.25))
                Line((-0.2000031807, 1.2), (-0.2000152674, 0.25))
                Line((-0.4000305347, 1.2), (-0.2000031807, 1.2))
            make_face()
        # OneSide extrude, distance=1.4
        extrude(amount=1.4, mode=Mode.ADD)

        # Sketch8 -> Extrude9 (Join)
        # Sketch on BRepFace
        # Sketch has 13 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.0000025448, -0.200018448), x_dir=(1, 0, 0), z_dir=(0, -0.0000127228, 1))):
            # Profile area: 0.3025, perimeter: 2.2
            with BuildLine():
                Line((0.8882211774, 1.1399974553), (1.4382211774, 1.1399974553))
                Line((0.8882211774, 0.5899974553), (0.8882211774, 1.1399974553))
                Line((1.4382211774, 0.5899974553), (0.8882211774, 0.5899974553))
                Line((1.4382211774, 1.1399974553), (1.4382211774, 0.5899974553))
            make_face()
        # OneSide extrude, distance=0.15
        extrude(amount=0.15, mode=Mode.ADD)

        # Sketch9 -> Extrude10 (Join)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.25, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.22, perimeter: 2.6
            with BuildLine():
                Line((-1.2666694933, -1.6819654625), (-1.0666694933, -1.6819654625))
                Line((-1.0666694933, -1.6819654625), (-1.0666694933, -0.5819654625))
                Line((-1.0666694933, -0.5819654625), (-1.2666694933, -0.5819654625))
                Line((-1.2666694933, -0.5819654625), (-1.2666694933, -1.1319654625))
                Line((-1.2666694933, -1.1319654625), (-1.2666694933, -1.6819654625))
            make_face()
        # OneSide extrude, distance=0.4
        extrude(amount=0.4, mode=Mode.ADD)

        # Sketch1 -> Extrude11 (Join)
        # Sketch on XZ construction plane
        # Sketch has 9 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0484727142, perimeter: 2.2553527837
            with BuildLine():
                CenterArc((2.0817557005, 0.0889700741), 2.0836560346, 103.6352815365, 6.0138035111)
                Line((1.9451178092, 2.1139003903), (1.590553415, 2.1139003903))
                Line((2.490553415, 2.1139003903), (1.9451178092, 2.1139003903))
                CenterArc((2.0170905336, 0.6425958694), 1.5456080011, 72.1619275058, 42.1357137337)
            make_face()
        # OneSide extrude, distance=0.25
        extrude(amount=0.25, mode=Mode.ADD)
    return part.part


# Description: This is a complex multi-faceted housing or bracket component with an irregular polyhedral shape, featuring a central cylindrical opening, internal structural ribs and supports, and multiple flat and angled surfaces designed for mechanical assembly and mounting.
def model_133510_c26c1e00_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 30 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 17.0223664874, perimeter: 19.6110946637
            with BuildLine():
                Line((-2.1, 1.6907994539), (-1.6907994539, 2.1))
                Line((-2.1, 1.6907994539), (-2.1, -1.6907994539))
                Line((-1.6907994539, -2.1), (-2.1, -1.6907994539))
                Line((-1.6907994539, -2.1), (1.6907994539, -2.1))
                Line((2.1, -1.6907994539), (1.6907994539, -2.1))
                Line((2.1, -1.6907994539), (2.1, 1.6907994539))
                Line((1.6907994539, 2.1), (2.1, 1.6907994539))
                Line((1.6907994539, 2.1), (-1.6907994539, 2.1))
            make_face()
            with BuildLine():
                CenterArc((-1.55, -1.55), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1.55, -1.55), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-1.55, 1.55), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((1.55, 1.55), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=3.26
        extrude(amount=3.26)

        # Sketch2 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 9 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 3.26), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 2.5780694714, perimeter: 15.8650429006
            with BuildLine():
                CenterArc((0, 0), 1.425, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.03
        extrude(amount=-0.03, mode=Mode.SUBTRACT)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 9 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 3.26), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.1861307215, perimeter: 1.5490457724
            with BuildLine():
                CenterArc((0, 0), 0.25, 126.8698976458, 286.2602047083)
                Line((-0.15, 0.2), (0.15, 0.2))
            make_face()
        # OneSide extrude, distance=2.38
        extrude(amount=2.38, mode=Mode.ADD)

        # Sketch2 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 9 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 3.26), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 3.0925052684, perimeter: 9.8960168588
            with BuildLine():
                CenterArc((0, 0), 1.1, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.475, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1, mode=Mode.ADD)

        # Sketch4 -> Extrude8 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((-1.55, 1.55)):
                Circle(0.15)
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((1.55, 1.55)):
                Circle(0.15)
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((1.55, -1.55)):
                Circle(0.15)
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((-1.55, -1.55)):
                Circle(0.15)
        # OneSide extrude, distance=-1.5
        extrude(amount=-1.5, mode=Mode.ADD)

        # Sketch4 -> Extrude7 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.6792908715, perimeter: 2.9216811678
            Circle(0.465)
        # OneSide extrude, distance=-0.275
        extrude(amount=-0.275, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude9 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2.1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))) as sk:
            # Profile area: 1.76, perimeter: 5.4
            with BuildLine():
                Line((0.8, 1.1), (0.8, 0))
                Line((-0.8, 1.1), (0.8, 1.1))
                Line((-0.8, 0), (-0.8, 1.1))
                Line((0.8, 0), (-0.8, 0))
            make_face()
        # TwoSides extrude, along=0.83, against=-0.02
        extrude(amount=0.83, mode=Mode.ADD)
        extrude(sk.sketch, amount=-0.02, mode=Mode.ADD)
    return part.part


# Description: This is a triangular or trapezoidal structural bracket or frame component with a central elongated slot, featuring internal cross-bracing or ribbing patterns for reinforcement and weight reduction.
def model_134667_e293572a_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 67 constraints, 31 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.2792985571, perimeter: 7.4023692837
            with BuildLine():
                Line((10.425, -7.5), (10.6, -7.5))
                CenterArc((7.5, -7.5), 2.925, -45, 45)
                Line((9.568287335, -9.568287335), (9.7450640303, -9.7450640303))
                CenterArc((9.9748737342, -9.9748737342), 0.325, -45, 180)
                Line((10.204683438, -10.204683438), (10.6, -10.6))
                Line((10.6, -7.5), (10.6, -10.6))
            make_face()
            # Profile area: 2.5585971142, perimeter: 14.4547385674
            with BuildLine():
                Line((10.204683438, -10.204683438), (10.6, -10.6))
                CenterArc((9.9748737342, -9.9748737342), 0.325, 135, 180)
                Line((9.568287335, -9.568287335), (9.7450640303, -9.7450640303))
                CenterArc((7.5, -7.5), 2.925, -135, 90)
                Line((5.431712665, -9.568287335), (5.2549359697, -9.7450640303))
                CenterArc((5.0251262658, -9.9748737342), 0.325, -135, 180)
                Line((4.4, -10.6), (4.795316562, -10.204683438))
                Line((10.6, -10.6), (4.4, -10.6))
            make_face()
            # Profile area: 45.8009513775, perimeter: 34.1578566035
            with BuildLine():
                Line((14.5, -14.5), (14.8535533906, -14.8535533906))
                CenterArc((14.5, -14.5), 0.5, -45, 45)
                Line((15, -0.5), (15, -14.5))
                CenterArc((14.5, -0.5), 0.5, 0, 45)
                Line((14.5, -0.5), (14.8535533906, -0.1464466094))
                Line((14.5, -0.5), (14.1464466094, -0.8535533906))
                CenterArc((13.7928932188, -1.2071067812), 0.5, -135, 180)
                Line((10.6, -4.4), (13.4393398282, -1.5606601718))
                Line((10.6, -4.4), (10.6, -7.5))
                Line((10.6, -7.5), (10.6, -10.6))
                Line((10.6, -10.6), (13.4393398282, -13.4393398282))
                CenterArc((13.7928932188, -13.7928932188), 0.5, -45, 180)
                Line((14.5, -14.5), (14.1464466094, -14.1464466094))
            make_face()
            # Profile area: 45.8009513775, perimeter: 34.1578566035
            with BuildLine():
                Line((14.5, -14.5), (14.1464466094, -14.1464466094))
                CenterArc((13.7928932188, -13.7928932188), 0.5, 135, 180)
                Line((10.6, -10.6), (13.4393398282, -13.4393398282))
                Line((10.6, -10.6), (4.4, -10.6))
                Line((1.5606601718, -13.4393398282), (4.4, -10.6))
                CenterArc((1.2071067812, -13.7928932188), 0.5, -135, 180)
                Line((0.5, -14.5), (0.8535533906, -14.1464466094))
                Line((0.1464466094, -14.8535533906), (0.5, -14.5))
                CenterArc((0.5, -14.5), 0.5, -135, 45)
                Line((14.5, -15), (0.5, -15))
                CenterArc((14.5, -14.5), 0.5, -90, 45)
                Line((14.5, -14.5), (14.8535533906, -14.8535533906))
            make_face()
            # Profile area: 1.2792985571, perimeter: 7.4023692837
            with BuildLine():
                Line((10.204683438, -4.795316562), (10.6, -4.4))
                CenterArc((9.9748737342, -5.0251262658), 0.325, -135, 180)
                Line((9.568287335, -5.431712665), (9.7450640303, -5.2549359697))
                CenterArc((7.5, -7.5), 2.925, 0, 45)
                Line((10.425, -7.5), (10.6, -7.5))
                Line((10.6, -4.4), (10.6, -7.5))
            make_face()
            # Profile area: 2.5585971142, perimeter: 14.4547385674
            with BuildLine():
                Line((4.4, -10.6), (4.795316562, -10.204683438))
                CenterArc((5.0251262658, -9.9748737342), 0.325, 45, 180)
                Line((5.431712665, -9.568287335), (5.2549359697, -9.7450640303))
                CenterArc((7.5, -7.5), 2.925, 135, 90)
                Line((5.431712665, -5.431712665), (5.2549359697, -5.2549359697))
                CenterArc((5.0251262658, -5.0251262658), 0.325, 135, 180)
                Line((4.4, -4.4), (4.795316562, -4.795316562))
                Line((4.4, -10.6), (4.4, -4.4))
            make_face()
            # Profile area: 45.8009513775, perimeter: 34.1578566035
            with BuildLine():
                CenterArc((14.5, -0.5), 0.5, 45, 45)
                Line((0.5, 0), (14.5, 0))
                CenterArc((0.5, -0.5), 0.5, 90, 45)
                Line((0.1464466094, -0.1464466094), (0.5, -0.5))
                Line((0.5, -0.5), (0.8535533906, -0.8535533906))
                CenterArc((1.2071067812, -1.2071067812), 0.5, -45, 180)
                Line((1.5606601718, -1.5606601718), (4.4, -4.4))
                Line((4.4, -4.4), (10.6, -4.4))
                Line((10.6, -4.4), (13.4393398282, -1.5606601718))
                CenterArc((13.7928932188, -1.2071067812), 0.5, 45, 180)
                Line((14.5, -0.5), (14.1464466094, -0.8535533906))
                Line((14.5, -0.5), (14.8535533906, -0.1464466094))
            make_face()
            # Profile area: 45.8009513775, perimeter: 34.1578566035
            with BuildLine():
                Line((4.4, -10.6), (4.4, -4.4))
                Line((1.5606601718, -1.5606601718), (4.4, -4.4))
                CenterArc((1.2071067812, -1.2071067812), 0.5, 135, 180)
                Line((0.5, -0.5), (0.8535533906, -0.8535533906))
                Line((0.1464466094, -0.1464466094), (0.5, -0.5))
                CenterArc((0.5, -0.5), 0.5, 135, 45)
                Line((0, -14.5), (0, -0.5))
                CenterArc((0.5, -14.5), 0.5, -180, 45)
                Line((0.1464466094, -14.8535533906), (0.5, -14.5))
                Line((0.5, -14.5), (0.8535533906, -14.1464466094))
                CenterArc((1.2071067812, -13.7928932188), 0.5, 45, 180)
                Line((1.5606601718, -13.4393398282), (4.4, -10.6))
            make_face()
            # Profile area: 2.5585971142, perimeter: 14.4547385674
            with BuildLine():
                Line((4.4, -4.4), (10.6, -4.4))
                Line((4.4, -4.4), (4.795316562, -4.795316562))
                CenterArc((5.0251262658, -5.0251262658), 0.325, -45, 180)
                Line((5.431712665, -5.431712665), (5.2549359697, -5.2549359697))
                CenterArc((7.5, -7.5), 2.925, 45, 90)
                Line((9.568287335, -5.431712665), (9.7450640303, -5.2549359697))
                CenterArc((9.9748737342, -5.0251262658), 0.325, 45, 180)
                Line((10.204683438, -4.795316562), (10.6, -4.4))
            make_face()
            # Profile area: 0.2513274123, perimeter: 2.9132741229
            with BuildLine():
                Line((14.1464466094, -0.8535533906), (14.0050252532, -0.9949747468))
                CenterArc((13.7928932188, -1.2071067812), 0.3, -135, 180)
                Line((13.4393398282, -1.5606601718), (13.5807611845, -1.4192388155))
                CenterArc((13.7928932188, -1.2071067812), 0.5, -135, 180)
            make_face()
            # Profile area: 0.2513274123, perimeter: 2.9132741229
            with BuildLine():
                CenterArc((13.7928932188, -1.2071067812), 0.5, 45, 180)
                Line((13.4393398282, -1.5606601718), (13.5807611845, -1.4192388155))
                CenterArc((13.7928932188, -1.2071067812), 0.3, 45, 180)
                Line((14.1464466094, -0.8535533906), (14.0050252532, -0.9949747468))
            make_face()
            # Profile area: 0.1413716694, perimeter: 1.5424777961
            with BuildLine():
                CenterArc((13.7928932188, -1.2071067812), 0.3, 45, 180)
                Line((13.5807611845, -1.4192388155), (13.7928932188, -1.2071067812))
                Line((14.0050252532, -0.9949747468), (13.7928932188, -1.2071067812))
            make_face()
            # Profile area: 0.1413716694, perimeter: 1.5424777961
            with BuildLine():
                Line((14.0050252532, -0.9949747468), (13.7928932188, -1.2071067812))
                Line((13.5807611845, -1.4192388155), (13.7928932188, -1.2071067812))
                CenterArc((13.7928932188, -1.2071067812), 0.3, -135, 180)
            make_face()
            # Profile area: 0.2513274123, perimeter: 2.9132741229
            with BuildLine():
                Line((13.4393398282, -13.4393398282), (13.5807611845, -13.5807611845))
                CenterArc((13.7928932188, -13.7928932188), 0.3, -45, 180)
                Line((14.1464466094, -14.1464466094), (14.0050252532, -14.0050252532))
                CenterArc((13.7928932188, -13.7928932188), 0.5, -45, 180)
            make_face()
            # Profile area: 0.2513274123, perimeter: 2.9132741229
            with BuildLine():
                CenterArc((13.7928932188, -13.7928932188), 0.5, 135, 180)
                Line((14.1464466094, -14.1464466094), (14.0050252532, -14.0050252532))
                CenterArc((13.7928932188, -13.7928932188), 0.3, 135, 180)
                Line((13.4393398282, -13.4393398282), (13.5807611845, -13.5807611845))
            make_face()
            # Profile area: 0.1413716694, perimeter: 1.5424777961
            with BuildLine():
                CenterArc((13.7928932188, -13.7928932188), 0.3, 135, 180)
                Line((14.0050252532, -14.0050252532), (13.7928932188, -13.7928932188))
                Line((13.5807611845, -13.5807611845), (13.7928932188, -13.7928932188))
            make_face()
            # Profile area: 0.1413716694, perimeter: 1.5424777961
            with BuildLine():
                Line((13.5807611845, -13.5807611845), (13.7928932188, -13.7928932188))
                Line((14.0050252532, -14.0050252532), (13.7928932188, -13.7928932188))
                CenterArc((13.7928932188, -13.7928932188), 0.3, -45, 180)
            make_face()
            # Profile area: 0.2513274123, perimeter: 2.9132741229
            with BuildLine():
                Line((1.4192388155, -13.5807611845), (1.5606601718, -13.4393398282))
                CenterArc((1.2071067812, -13.7928932188), 0.3, -135, 180)
                Line((0.8535533906, -14.1464466094), (0.9949747468, -14.0050252532))
                CenterArc((1.2071067812, -13.7928932188), 0.5, -135, 180)
            make_face()
            # Profile area: 0.2513274123, perimeter: 2.9132741229
            with BuildLine():
                CenterArc((1.2071067812, -13.7928932188), 0.5, 45, 180)
                Line((0.8535533906, -14.1464466094), (0.9949747468, -14.0050252532))
                CenterArc((1.2071067812, -13.7928932188), 0.3, 45, 180)
                Line((1.4192388155, -13.5807611845), (1.5606601718, -13.4393398282))
            make_face()
            # Profile area: 0.1413716694, perimeter: 1.5424777961
            with BuildLine():
                CenterArc((1.2071067812, -13.7928932188), 0.3, 45, 180)
                Line((0.9949747468, -14.0050252532), (1.2071067812, -13.7928932188))
                Line((1.2071067812, -13.7928932188), (1.4192388155, -13.5807611845))
            make_face()
            # Profile area: 0.1413716694, perimeter: 1.5424777961
            with BuildLine():
                Line((1.2071067812, -13.7928932188), (1.4192388155, -13.5807611845))
                Line((0.9949747468, -14.0050252532), (1.2071067812, -13.7928932188))
                CenterArc((1.2071067812, -13.7928932188), 0.3, -135, 180)
            make_face()
            # Profile area: 0.2513274123, perimeter: 2.9132741229
            with BuildLine():
                Line((0.8535533906, -0.8535533906), (0.9949747468, -0.9949747468))
                CenterArc((1.2071067812, -1.2071067812), 0.3, -45, 180)
                Line((1.4192388155, -1.4192388155), (1.5606601718, -1.5606601718))
                CenterArc((1.2071067812, -1.2071067812), 0.5, -45, 180)
            make_face()
            # Profile area: 0.2513274123, perimeter: 2.9132741229
            with BuildLine():
                CenterArc((1.2071067812, -1.2071067812), 0.5, 135, 180)
                Line((1.4192388155, -1.4192388155), (1.5606601718, -1.5606601718))
                CenterArc((1.2071067812, -1.2071067812), 0.3, 135, 180)
                Line((0.8535533906, -0.8535533906), (0.9949747468, -0.9949747468))
            make_face()
            # Profile area: 0.1413716694, perimeter: 1.5424777961
            with BuildLine():
                CenterArc((1.2071067812, -1.2071067812), 0.3, 135, 180)
                Line((1.2071067812, -1.2071067812), (1.4192388155, -1.4192388155))
                Line((0.9949747468, -0.9949747468), (1.2071067812, -1.2071067812))
            make_face()
            # Profile area: 0.1413716694, perimeter: 1.5424777961
            with BuildLine():
                Line((0.9949747468, -0.9949747468), (1.2071067812, -1.2071067812))
                Line((1.2071067812, -1.2071067812), (1.4192388155, -1.4192388155))
                CenterArc((1.2071067812, -1.2071067812), 0.3, -45, 180)
            make_face()
        # OneSide extrude, distance=-0.8
        extrude(amount=-0.8)

        # Sketch1 -> Extrude2 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 67 constraints, 31 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1413716694, perimeter: 1.5424777961
            with BuildLine():
                CenterArc((13.7928932188, -13.7928932188), 0.3, 135, 180)
                Line((14.0050252532, -14.0050252532), (13.7928932188, -13.7928932188))
                Line((13.5807611845, -13.5807611845), (13.7928932188, -13.7928932188))
            make_face()
            # Profile area: 0.1413716694, perimeter: 1.5424777961
            with BuildLine():
                Line((13.5807611845, -13.5807611845), (13.7928932188, -13.7928932188))
                Line((14.0050252532, -14.0050252532), (13.7928932188, -13.7928932188))
                CenterArc((13.7928932188, -13.7928932188), 0.3, -45, 180)
            make_face()
        # OneSide extrude, distance=-13
        extrude(amount=-13, mode=Mode.SUBTRACT)

        # Sketch1 -> Extrude3 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 67 constraints, 31 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1413716694, perimeter: 1.5424777961
            with BuildLine():
                CenterArc((13.7928932188, -1.2071067812), 0.3, 45, 180)
                Line((13.5807611845, -1.4192388155), (13.7928932188, -1.2071067812))
                Line((14.0050252532, -0.9949747468), (13.7928932188, -1.2071067812))
            make_face()
            # Profile area: 0.1413716694, perimeter: 1.5424777961
            with BuildLine():
                Line((14.0050252532, -0.9949747468), (13.7928932188, -1.2071067812))
                Line((13.5807611845, -1.4192388155), (13.7928932188, -1.2071067812))
                CenterArc((13.7928932188, -1.2071067812), 0.3, -135, 180)
            make_face()
        # OneSide extrude, distance=-8.5
        extrude(amount=-8.5, mode=Mode.SUBTRACT)

        # Sketch1 -> Extrude4 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 67 constraints, 31 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1413716694, perimeter: 1.5424777961
            with BuildLine():
                CenterArc((1.2071067812, -1.2071067812), 0.3, 135, 180)
                Line((1.2071067812, -1.2071067812), (1.4192388155, -1.4192388155))
                Line((0.9949747468, -0.9949747468), (1.2071067812, -1.2071067812))
            make_face()
            # Profile area: 0.1413716694, perimeter: 1.5424777961
            with BuildLine():
                Line((0.9949747468, -0.9949747468), (1.2071067812, -1.2071067812))
                Line((1.2071067812, -1.2071067812), (1.4192388155, -1.4192388155))
                CenterArc((1.2071067812, -1.2071067812), 0.3, -45, 180)
            make_face()
        # OneSide extrude, distance=-5.5
        extrude(amount=-5.5, mode=Mode.SUBTRACT)

        # Sketch1 -> Extrude5 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 67 constraints, 31 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1413716694, perimeter: 1.5424777961
            with BuildLine():
                CenterArc((1.2071067812, -13.7928932188), 0.3, 45, 180)
                Line((0.9949747468, -14.0050252532), (1.2071067812, -13.7928932188))
                Line((1.2071067812, -13.7928932188), (1.4192388155, -13.5807611845))
            make_face()
            # Profile area: 0.1413716694, perimeter: 1.5424777961
            with BuildLine():
                Line((1.2071067812, -13.7928932188), (1.4192388155, -13.5807611845))
                Line((0.9949747468, -14.0050252532), (1.2071067812, -13.7928932188))
                CenterArc((1.2071067812, -13.7928932188), 0.3, -135, 180)
            make_face()
        # OneSide extrude, distance=-5.5
        extrude(amount=-5.5, mode=Mode.SUBTRACT)

        # Sketch1 -> Extrude6 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 67 constraints, 31 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2513274123, perimeter: 2.9132741229
            with BuildLine():
                CenterArc((1.2071067812, -1.2071067812), 0.5, 135, 180)
                Line((1.4192388155, -1.4192388155), (1.5606601718, -1.5606601718))
                CenterArc((1.2071067812, -1.2071067812), 0.3, 135, 180)
                Line((0.8535533906, -0.8535533906), (0.9949747468, -0.9949747468))
            make_face()
            # Profile area: 0.2513274123, perimeter: 2.9132741229
            with BuildLine():
                Line((0.8535533906, -0.8535533906), (0.9949747468, -0.9949747468))
                CenterArc((1.2071067812, -1.2071067812), 0.3, -45, 180)
                Line((1.4192388155, -1.4192388155), (1.5606601718, -1.5606601718))
                CenterArc((1.2071067812, -1.2071067812), 0.5, -45, 180)
            make_face()
        # OneSide extrude, distance=-0.3
        extrude(amount=-0.3, mode=Mode.SUBTRACT)

        # Sketch1 -> Extrude7 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 67 constraints, 31 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2513274123, perimeter: 2.9132741229
            with BuildLine():
                Line((14.1464466094, -0.8535533906), (14.0050252532, -0.9949747468))
                CenterArc((13.7928932188, -1.2071067812), 0.3, -135, 180)
                Line((13.4393398282, -1.5606601718), (13.5807611845, -1.4192388155))
                CenterArc((13.7928932188, -1.2071067812), 0.5, -135, 180)
            make_face()
            # Profile area: 0.2513274123, perimeter: 2.9132741229
            with BuildLine():
                CenterArc((13.7928932188, -1.2071067812), 0.5, 45, 180)
                Line((13.4393398282, -1.5606601718), (13.5807611845, -1.4192388155))
                CenterArc((13.7928932188, -1.2071067812), 0.3, 45, 180)
                Line((14.1464466094, -0.8535533906), (14.0050252532, -0.9949747468))
            make_face()
        # OneSide extrude, distance=-0.3
        extrude(amount=-0.3, mode=Mode.SUBTRACT)

        # Sketch1 -> Extrude8 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 67 constraints, 31 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2513274123, perimeter: 2.9132741229
            with BuildLine():
                Line((13.4393398282, -13.4393398282), (13.5807611845, -13.5807611845))
                CenterArc((13.7928932188, -13.7928932188), 0.3, -45, 180)
                Line((14.1464466094, -14.1464466094), (14.0050252532, -14.0050252532))
                CenterArc((13.7928932188, -13.7928932188), 0.5, -45, 180)
            make_face()
            # Profile area: 0.2513274123, perimeter: 2.9132741229
            with BuildLine():
                CenterArc((13.7928932188, -13.7928932188), 0.5, 135, 180)
                Line((14.1464466094, -14.1464466094), (14.0050252532, -14.0050252532))
                CenterArc((13.7928932188, -13.7928932188), 0.3, 135, 180)
                Line((13.4393398282, -13.4393398282), (13.5807611845, -13.5807611845))
            make_face()
        # OneSide extrude, distance=-0.3
        extrude(amount=-0.3, mode=Mode.SUBTRACT)

        # Sketch1 -> Extrude9 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 67 constraints, 31 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2513274123, perimeter: 2.9132741229
            with BuildLine():
                CenterArc((1.2071067812, -13.7928932188), 0.5, 45, 180)
                Line((0.8535533906, -14.1464466094), (0.9949747468, -14.0050252532))
                CenterArc((1.2071067812, -13.7928932188), 0.3, 45, 180)
                Line((1.4192388155, -13.5807611845), (1.5606601718, -13.4393398282))
            make_face()
            # Profile area: 0.2513274123, perimeter: 2.9132741229
            with BuildLine():
                Line((1.4192388155, -13.5807611845), (1.5606601718, -13.4393398282))
                CenterArc((1.2071067812, -13.7928932188), 0.3, -135, 180)
                Line((0.8535533906, -14.1464466094), (0.9949747468, -14.0050252532))
                CenterArc((1.2071067812, -13.7928932188), 0.5, -135, 180)
            make_face()
        # OneSide extrude, distance=-0.3
        extrude(amount=-0.3, mode=Mode.SUBTRACT)

        # Sketch2 -> Extrude10 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.4000000119, perimeter: 5.9538040066
            with BuildLine():
                Line((-13.0000001937, 13.0000001937), (-11.0000001639, 11.0000001639))
                Line((-12.8000001907, 13.2000001967), (-11.0000001639, 11.0000001639))
                Line((-12.8000001907, 13.2000001967), (-13.0000001937, 13.0000001937))
            make_face()
            # Profile area: 0.4000000119, perimeter: 5.9538040066
            with BuildLine():
                Line((-13.2000001967, 12.8000001907), (-11.0000001639, 11.0000001639))
                Line((-13.0000001937, 13.0000001937), (-11.0000001639, 11.0000001639))
                Line((-13.0000001937, 13.0000001937), (-13.2000001967, 12.8000001907))
            make_face()
            # Profile area: 0.4000003196, perimeter: 5.9538042117
            with BuildLine():
                Line((-1.999999918, 13.000000082), (-2.2000000328, 13.2000001967))
                Line((-2.2000000328, 13.2000001967), (-4, 11))
                Line((-1.999999918, 13.000000082), (-4, 11))
            make_face()
            # Profile area: 0.3999997169, perimeter: 5.9538038641
            with BuildLine():
                Line((-1.999999918, 13.000000082), (-4, 11))
                Line((-1.8000000268, 12.8000001907), (-4, 11))
                Line((-1.8000000268, 12.8000001907), (-1.999999918, 13.000000082))
            make_face()
            # Profile area: 0.3999998726, perimeter: 5.9538038641
            with BuildLine():
                Line((-12.8000001907, 1.8000000268), (-13.000000082, 1.999999918))
                Line((-12.8000001907, 1.8000000268), (-11, 4))
                Line((-13.000000082, 1.999999918), (-11, 4))
            make_face()
            # Profile area: 0.4000001639, perimeter: 5.9538042117
            with BuildLine():
                Line((-13.000000082, 1.999999918), (-11, 4))
                Line((-13.2000001967, 2.2000000328), (-11, 4))
                Line((-13.000000082, 1.999999918), (-13.2000001967, 2.2000000328))
            make_face()
            # Profile area: 0.4, perimeter: 5.9538038385
            with BuildLine():
                Line((-2.0000000298, 2.0000000298), (-4, 4))
                Line((-2.2000000328, 1.8000000268), (-4, 4))
                Line((-2.0000000298, 2.0000000298), (-2.2000000328, 1.8000000268))
            make_face()
            # Profile area: 0.4, perimeter: 5.9538038385
            with BuildLine():
                Line((-1.8000000268, 2.2000000328), (-2.0000000298, 2.0000000298))
                Line((-1.8000000268, 2.2000000328), (-4, 4))
                Line((-2.0000000298, 2.0000000298), (-4, 4))
            make_face()
        # OneSide extrude, distance=-0.3
        extrude(amount=-0.3, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a bracket or support arm with an angular, L-shaped design featuring a vertical flange on the left, a horizontal extending beam, and reinforcing ribs or flanges along its length for structural rigidity.
def model_135067_f79b4c96_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch16 -> Extrude9 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 30 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 3.0672683512, perimeter: 12.8975467474
            with BuildLine():
                CenterArc((-1.5013936965, 2.9500000462), 0.15, 1.6484724946, 88.3515275054)
                Line((-1.5013936965, 3.1000000462), (-1.6000000313, 3.1000000462))
                CenterArc((-1.6000000313, 2.6000000462), 0.5, 90, 90)
                Line((-2.1000000313, 2.6000000462), (-2.1000000313, 1.8000000224))
                CenterArc((-1.8000000313, 1.8000000224), 0.3, 180, 90)
                Line((-1.8000000313, 1.5000000224), (2.5928462966, 1.5000000224))
                CenterArc((2.5928462966, 1.5750000224), 0.075, -90, 140.1944289077)
                Line((2.6408601266, 1.6326166183), (2.213906756, 1.9884110938))
                CenterArc((2.181897536, 1.9500000298), 0.05, 50.1944289077, 39.8055710923)
                Line((2.181897536, 2.0000000298), (1.87840799, 2.0000000298))
                CenterArc((1.87840799, 1.9500000298), 0.05, 90, 90)
                Line((1.82840799, 1.9500000298), (1.82840799, 1.8342874212))
                CenterArc((1.77840799, 1.8342874212), 0.05, -99.2755845152, 99.2755845152)
                Line((1.7703488261, 1.7849411967), (-1.148355004, 2.2616202661))
                CenterArc((-1.1000000209, 2.5576976134), 0.3, 180, 80.7244154848)
                Line((-1.4000000209, 2.5576976134), (-1.4000000209, 2.7860000417))
                CenterArc((-1.3860000209, 2.7860000417), 0.014, 90, 90)
                Line((-1.3860000209, 2.8000000417), (-1.3614234144, 2.8000000417))
                CenterArc((-1.3614234144, 2.8140000417), 0.014, -90, 91.6484724946)
                Line((-1.3514557762, 2.9543151417), (-1.3474292085, 2.814402784))
            make_face()
            with BuildLine():
                CenterArc((-1.6979966553, 1.839391883), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=0.2
        extrude(amount=0.2, both=True)
    return part.part


# Description: This is a structural assembly featuring two pyramidal towers connected by a trussed rectangular base frame with internal bracing and mesh panels, designed for a space frame or lattice structure application.
def model_135873_2ceb32d1_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 13 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 5.7704790035, perimeter: 13.9216811678
            with BuildLine():
                Line((-3.2481718107, -2.9529760271), (-3.2481718107, -0.9529760271))
                Line((-0.1481718107, -2.9529760271), (-3.2481718107, -2.9529760271))
                Line((-0.1481718107, -0.9529760271), (-0.1481718107, -2.9529760271))
                Line((-2.7481718107, -0.9529760271), (-0.1481718107, -0.9529760271))
                Line((-3.2481718107, -0.9529760271), (-2.7481718107, -0.9529760271))
            make_face()
            with BuildLine():
                CenterArc((-2.9981718107, -1.2029760271), 0.12, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-1.4481718107, -1.2029760271), 0.12, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((-0.4076641072, -2.1382844322), (-0.4076641072, -1.7382844322))
                CenterArc((-0.6326641072, -2.1382844322), 0.225, 180, 180)
                Line((-0.8576641072, -1.7382844322), (-0.8576641072, -2.1382844322))
                CenterArc((-0.6326641072, -1.7382844322), 0.225, 0, 180)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.0452389342, perimeter: 0.7539822369
            with Locations((-2.9981718107, -1.2029760271)):
                Circle(0.12)
            # Profile area: 0.0452389342, perimeter: 0.7539822369
            with Locations((-1.4481718107, -1.2029760271)):
                Circle(0.12)
        # OneSide extrude, distance=0.4
        extrude(amount=0.4)

        # Sketch3 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.4, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.24, perimeter: 4.24
            with BuildLine():
                Line((3.1281718107, 0.9529760271), (3.1281718107, 2.9529760271))
                Line((3.2481718107, 0.9529760271), (3.1281718107, 0.9529760271))
                Line((3.2481718107, 2.9529760271), (3.2481718107, 0.9529760271))
                Line((3.1281718107, 2.9529760271), (3.2481718107, 2.9529760271))
            make_face()
        # OneSide extrude, distance=0.9
        extrude(amount=0.9, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.4, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.24, perimeter: 4.24
            with BuildLine():
                Line((1.1721753553, 0.9529760271), (1.1721753553, 2.9529760271))
                Line((1.2921753553, 0.9529760271), (1.1721753553, 0.9529760271))
                Line((1.2921753553, 2.9529760271), (1.2921753553, 0.9529760271))
                Line((1.1721753553, 2.9529760271), (1.2921753553, 2.9529760271))
            make_face()
        # OneSide extrude, distance=0.9
        extrude(amount=0.9, mode=Mode.ADD)

        # Sketch4 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.4, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.24, perimeter: 4.24
            with BuildLine():
                Line((1.1721753553, 0.9529760271), (1.1721753553, 2.9529760271))
                Line((1.2921753553, 0.9529760271), (1.1721753553, 0.9529760271))
                Line((1.2921753553, 2.9529760271), (1.2921753553, 0.9529760271))
                Line((1.1721753553, 2.9529760271), (1.2921753553, 2.9529760271))
            make_face()
        # OneSide extrude, distance=0.9
        extrude(amount=0.9, mode=Mode.ADD)

        # Sketch5 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 2.9529760271), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.108, perimeter: 2.04
            with BuildLine():
                Line((-1.2921753553, 0.4), (-1.1721753553, 0.4))
                Line((-1.1721753553, 0.4), (-1.1721753553, 1.3))
                Line((-1.1721753553, 1.3), (-1.2921753553, 1.3))
                Line((-1.2921753553, 1.3), (-1.2921753553, 0.4))
            make_face()
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.SUBTRACT)

        # Sketch1 -> Extrude6 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 13 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0452389342, perimeter: 0.7539822369
            with Locations((-1.4481718107, -1.2029760271)):
                Circle(0.12)
        # OneSide extrude, distance=3.3
        extrude(amount=3.3, mode=Mode.SUBTRACT)

        # Sketch1 -> Extrude7 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 13 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0452389342, perimeter: 0.7539822369
            with Locations((-2.9981718107, -1.2029760271)):
                Circle(0.12)
        # OneSide extrude, distance=1.6
        extrude(amount=1.6, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a fan shroud or protective guard with a large circular mesh screen top, a cylindrical body, and a mounting flange at the base for attachment to equipment.
def model_135897_34593cf4_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 28.2743338823, perimeter: 18.8495559215
            Circle(3)
        # OneSide extrude, distance=0.8
        extrude(amount=0.8)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 22.9022104447, perimeter: 16.9646003294
            Circle(2.7)
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.2000000015, perimeter: 2.4000000149
            with BuildLine():
                Line((0.5000000075, 2.7), (0, 2.7))
                Line((0.5000000075, 2.9), (0.5000000075, 2.7))
                Line((-0.5, 2.9), (0.5000000075, 2.9))
                Line((-0.5, 2.7), (-0.5, 2.9))
                Line((0, 2.7), (-0.5, 2.7))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0.5000000075, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.075, perimeter: 2.0444293616
            with BuildLine():
                Line((-2.7, 0), (-2.55, -0.45))
                Line((-2.7, -1), (-2.7, 0))
                Line((-2.55, -0.45), (-2.7, -1))
            make_face()
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.ADD)

        # Sketch5 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 10 constraints, 14 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.8, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.0916858462, perimeter: 20.9168584624
            with BuildLine():
                Line((1.5, -1.0000000149), (1.9999999925, 0.9999999851))
                Line((1.9999999925, 0.9999999851), (1.5229438454, 1.143116839))
                CenterArc((-0.0000000435, -3.933362444), 5.3, 73.300754689, 33.3984897212)
                Line((-1.5229438526, 1.143116863), (-2.0000000075, 1.0000000149))
                Line((-1.5, -0.9999999851), (-2.0000000075, 1.0000000149))
                Line((-1.5, -0.9999999851), (-1.0394154907, -0.9078830906))
                CenterArc((-0.0000000539, -6.1049606876), 5.3, 78.6900674165, 22.6198641818)
                Line((1.0394154722, -0.9078831084), (1.5, -1.0000000149))
            make_face()
            with BuildLine():
                CenterArc((-0.0000000539, -6.1049606876), 5.5, 78.6900674165, 22.6198641818)
                Line((-1.3522237274, -0.766483953), (-1.0786387148, -0.7117669548))
                Line((-1.3522237274, -0.766483953), (-1.7596680871, 0.8632934614))
                Line((-1.4654742749, 0.9515516061), (-1.7596680871, 0.8632934614))
                CenterArc((-0.0000000435, -3.933362444), 5.1, 73.300754689, 33.3984897212)
                Line((1.7596680742, 0.8632934342), (1.4654742647, 0.951551583))
                Line((1.3522237269, -0.7664839794), (1.7596680742, 0.8632934342))
                Line((1.0786386996, -0.7117669734), (1.3522237269, -0.7664839794))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1, mode=Mode.ADD)

        # Sketch6 -> Extrude6 (Join)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.8, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0314159275, perimeter: 0.6283185401
            with Locations((0, -1.6000000238)):
                Circle(0.1000000015)
            # Profile area: 0.0317306001, perimeter: 0.6314574258
            with Locations((-0.0000000018, -1.0899918677)):
                Circle(0.1004995707)
            # Profile area: 0.0315668339, perimeter: 0.6298257964
            with Locations((-0.0000000084, -0.293069396)):
                Circle(0.1002398888)
            # Profile area: 0.0314159275, perimeter: 0.6283185401
            with Locations((0, 0.3000000045)):
                Circle(0.1000000015)
            # Profile area: 0.0314159275, perimeter: 0.6283185401
            with Locations((0, 0.8000000119)):
                Circle(0.1000000015)
            # Profile area: 0.0314159275, perimeter: 0.6283185401
            with Locations((0, 1.7000000253)):
                Circle(0.1000000015)
            # Profile area: 0.0314159275, perimeter: 0.6283185401
            with Locations((0.3000000045, 2.0000000298)):
                Circle(0.1000000015)
            # Profile area: 0.0314159275, perimeter: 0.6283185401
            with Locations((0.7000000104, 2.0000000298)):
                Circle(0.1000000015)
            # Profile area: 0.0314159275, perimeter: 0.6283185401
            with Locations((1.1000000164, 1.7000000253)):
                Circle(0.1000000015)
            # Profile area: 0.0314159275, perimeter: 0.6283185401
            with Locations((-0.3000000045, 2.0000000298)):
                Circle(0.1000000015)
            # Profile area: 0.0314159275, perimeter: 0.6283185401
            with Locations((-0.7000000104, 2.0000000298)):
                Circle(0.1000000015)
            # Profile area: 0.0314159275, perimeter: 0.6283185401
            with Locations((-1.1000000164, 1.7000000253)):
                Circle(0.1000000015)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1, mode=Mode.ADD)
    return part.part


# Description: A rectangular box-shaped component with an open top, featuring internal dividers/partitions, corner flanges, and what appears to be mounting tabs or brackets extending from the sides.
def model_136355_b5fd1a59_0001():
    """Model: Jumper"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 9 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0649999982, perimeter: 2.6000000164
            with BuildLine():
                Line((0.5, -0.25), (0, -0.25))
                Line((0.5, 0), (0.5, -0.25))
                Line((0, 0), (0.5, 0))
                Line((0, -0.25), (0, 0))
            make_face()
            with BuildLine():
                Line((0.0500000007, -0.200000003), (0.0500000007, -0.0500000007))
                Line((0.0500000007, -0.0500000007), (0.4500000067, -0.0500000007))
                Line((0.4500000067, -0.0500000007), (0.4500000067, -0.200000003))
                Line((0.4500000067, -0.200000003), (0.0500000007, -0.200000003))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.6
        extrude(amount=0.6)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.25), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.025, perimeter: 1.1
            with BuildLine():
                Line((0.5, 0.5), (0, 0.5))
                Line((0, 0.5), (0, 0.45))
                Line((0, 0.45), (0.5, 0.45))
                Line((0.5, 0.45), (0.5, 0.5))
            make_face()
        # OneSide extrude, distance=-0.025
        extrude(amount=-0.025, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0.5, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0112500023, perimeter: 0.5500000101
            with BuildLine():
                Line((-0.225, 0.5), (0, 0.5))
                Line((-0.225, 0.5), (-0.225, 0.4499999899))
                Line((0, 0.4499999899), (-0.225, 0.4499999899))
                Line((0, 0.5), (0, 0.4499999899))
            make_face()
        # OneSide extrude, distance=-0.025
        extrude(amount=-0.025, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.02375, perimeter: 1.05
            with BuildLine():
                Line((-0.475, 0.5), (0, 0.5))
                Line((-0.475, 0.5), (-0.475, 0.45))
                Line((0, 0.45), (-0.475, 0.45))
                Line((0, 0.5), (0, 0.45))
            make_face()
        # OneSide extrude, distance=-0.025
        extrude(amount=-0.025, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.01, perimeter: 0.5
            with BuildLine():
                Line((0.025, 0.5), (0.025, 0.45))
                Line((0.225, 0.45), (0.025, 0.45))
                Line((0.225, 0.45), (0.225, 0.5))
                Line((0.025, 0.5), (0.225, 0.5))
            make_face()
        # OneSide extrude, distance=-0.025
        extrude(amount=-0.025, mode=Mode.SUBTRACT)

        # Sketch6 -> Extrude6 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.25), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.01, perimeter: 0.4
            with BuildLine():
                Line((0.3, 0.6), (0.3, 0.5))
                Line((0.2, 0.6), (0.3, 0.6))
                Line((0.2, 0.5), (0.2, 0.6))
                Line((0.2, 0.5), (0.3, 0.5))
            make_face()
            # Profile area: 0.005, perimeter: 0.3
            with BuildLine():
                Line((0.2, 0.5), (0.3, 0.5))
                Line((0.2, 0.45), (0.2, 0.5))
                Line((0.2, 0.45), (0.3, 0.45))
                Line((0.3, 0.5), (0.3, 0.45))
            make_face()
        # OneSide extrude, distance=-0.25
        extrude(amount=-0.25, mode=Mode.SUBTRACT)

        # Sketch7 -> Extrude7 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.25), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0039269908, perimeter: 0.2570796327
            with BuildLine():
                CenterArc((0.25, 0.45), 0.05, 0, 180)
                Line((0.3, 0.45), (0.2, 0.45))
            make_face()
            # Profile area: 0.0039269908, perimeter: 0.2570796327
            with BuildLine():
                Line((0.3, 0.45), (0.2, 0.45))
                CenterArc((0.25, 0.45), 0.05, 180, 180)
            make_face()
        # OneSide extrude, distance=-0.25
        extrude(amount=-0.25, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a complex 3D molded component featuring two prominent circular holes, curved organic surfaces, and angular faceted sections that suggest it may be a fluid connector, valve body, or industrial manifold part.
def model_136473_1a062e83_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 15, perimeter: 23
            with BuildLine():
                Line((-7, 0), (3, 0))
                Line((3, 0), (3, 1.5))
                Line((-7, 1.5), (3, 1.5))
                Line((-7, 0), (-7, 1.5))
            make_face()
        # OneSide extrude, distance=8
        extrude(amount=8)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 21.9911485751, perimeter: 44.9822971503
            with BuildLine():
                CenterArc((2, -4), 3, 0, 360)
                Line((5.1234752378, -6.4987801902), (4.3426064283, -5.8740851427))
                CenterArc((2, -4), 4, -38.6598082541, 128.6598082541)
                CenterArc((2, -4), 4, 90, 180)
                CenterArc((2, -4), 4, -90, 51.3401917459)
            make_face()
            # Profile area: 28.2743338823, perimeter: 18.8495559215
            with Locations((2, -4)):
                Circle(3)
        # OneSide extrude, distance=2
        extrude(amount=2, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 10 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(-7, 0, 0), x_dir=(0, -1, 0), z_dir=(-1, 0, 0))):
            # Profile area: 52.4711007057, perimeter: 43.1089591359
            with BuildLine():
                Line((-8, -6.5), (-7.9999645453, -6.5))
                CenterArc((-3.9999822727, -6.4880912438), 4, -179.829419381, 179.6588387619)
                Line((0, -6.4761824876), (0, -6.5))
                Line((0, -1.5), (0, -6.4761824876))
                Line((-8, -1.5), (0, -1.5))
                Line((-8, -1.5), (-8, -6.5))
            make_face()
            with BuildLine():
                CenterArc((-3.9999822727, -6.4880912438), 2, 178.3350235665, 1.9191148961)
                CenterArc((-3.9999822727, -6.4880912438), 2, -179.7458615374, 358.0808851039)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-2
        extrude(amount=-2, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 8 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(3, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 52.4710120689, perimeter: 43.1089236813
            with BuildLine():
                Line((0, -1.5), (0, -6.4761824876))
                Line((0, -6.4761824876), (0, -6.5))
                CenterArc((3.9999822727, -6.4880912438), 4, -179.829419381, 179.6588387619)
                Line((7.9999647138, -6.4762392149), (7.9999645453, -6.5))
                Line((8, -1.5), (7.9999647138, -6.4762392149))
                Line((0, -1.5), (8, -1.5))
            make_face()
            with BuildLine():
                CenterArc((3.9999822727, -6.4880912438), 2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-2
        extrude(amount=-2, mode=Mode.ADD)

        # Sketch5 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 2), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 28.2743338823, perimeter: 18.8495559215
            with Locations((2, -4)):
                Circle(3)
        # OneSide extrude, distance=-1.5
        extrude(amount=-1.5, mode=Mode.SUBTRACT)

        # Sketch6 -> Extrude6 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.5), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            with Locations((2, -4)):
                Circle(1)
        # OneSide extrude, distance=-5
        extrude(amount=-5, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a rectangular channel or duct with an elongated parallelogram profile, featuring an open rectangular cross-section and a slight taper or twist along its length, commonly used as a structural member or air passage component.
def model_136635_d193c419_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 60, perimeter: 34
            with BuildLine():
                Line((0, 12), (0, 0))
                Line((0, 0), (5, 0))
                Line((5, 0), (5, 12))
                Line((5, 12), (0, 12))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch2 -> Extrude9 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 1.7671458676, perimeter: 4.7123889804
            with Locations((-2.4999999275, 7.2817472591)):
                Circle(0.75)
        # OneSide extrude, distance=-0.1
        extrude(amount=-0.1, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 constraints, 18 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.0176714587, perimeter: 0.471238898
            with Locations((0.7, 0.65)):
                Circle(0.075)
            # Profile area: 0.0176714587, perimeter: 0.471238898
            with Locations((1, 0.65)):
                Circle(0.075)
            # Profile area: 0.0176714587, perimeter: 0.471238898
            with Locations((1.3, 0.65)):
                Circle(0.075)
            # Profile area: 0.0176714587, perimeter: 0.471238898
            with Locations((1.6, 0.65)):
                Circle(0.075)
            # Profile area: 0.0176714587, perimeter: 0.471238898
            with Locations((1.9, 0.65)):
                Circle(0.075)
            # Profile area: 0.0524416116, perimeter: 1.1511147609
            with BuildLine():
                Line((2.2689685828, 0.706747273), (2.7310314172, 0.706747273))
                Line((2.2689685828, 0.593252727), (2.2689685828, 0.706747273))
                Line((2.7310314172, 0.593252727), (2.2689685828, 0.593252727))
                Line((2.7310314172, 0.706747273), (2.7310314172, 0.593252727))
            make_face()
            # Profile area: 0.0176714587, perimeter: 0.471238898
            with Locations((3.1, 0.6626659013)):
                Circle(0.075)
            # Profile area: 0.0176714587, perimeter: 0.471238898
            with Locations((3.4, 0.6626659013)):
                Circle(0.075)
            # Profile area: 0.0176714587, perimeter: 0.471238898
            with Locations((3.7, 0.6626659013)):
                Circle(0.075)
            # Profile area: 0.0176714587, perimeter: 0.471238898
            with Locations((4, 0.6626659013)):
                Circle(0.075)
            # Profile area: 0.0176714587, perimeter: 0.471238898
            with Locations((4.3, 0.6626659013)):
                Circle(0.075)
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.SUBTRACT)

        # Sketch6 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 12 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(5, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.3121892301, perimeter: 4.7631093526
            with BuildLine():
                Line((-0.729874774, 10.0124682152), (-0.5906493551, 10.0124682152))
                Line((-0.729874774, 7.7701389578), (-0.729874774, 10.0124682152))
                Line((-0.5906493551, 7.7701389578), (-0.729874774, 7.7701389578))
                Line((-0.5906493551, 10.0124682152), (-0.5906493551, 7.7701389578))
            make_face()
            # Profile area: 0.1445545776, perimeter: 2.3611379416
            with BuildLine():
                Line((-0.5929513596, 6.4314587023), (-0.5929513596, 7.473275242))
                Line((-0.5929513596, 7.473275242), (-0.7317037906, 7.473275242))
                Line((-0.7317037906, 7.473275242), (-0.7317037906, 6.4314587023))
                Line((-0.7317037906, 6.4314587023), (-0.5929513596, 6.4314587023))
            make_face()
        # OneSide extrude, distance=0.1
        extrude(amount=0.1, mode=Mode.ADD)

        # Sketch7 -> Extrude6 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 12, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0176714587, perimeter: 0.471238898
            with Locations((-1.1119039227, 0.6515835085)):
                Circle(0.075)
            # Profile area: 0.0019634954, perimeter: 0.1570796327
            with Locations((-1.5836529492, 0.6617651422)):
                Circle(0.025)
            # Profile area: 0.0078539816, perimeter: 0.3141592654
            with Locations((-3.8677327683, 0.6626659013)):
                Circle(0.05)
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2, mode=Mode.SUBTRACT)

        # Sketch8 -> Extrude7 (Cut)
        # Sketch on Profile plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 2.1050720601, perimeter: 13.2005919636
            with BuildLine():
                CenterArc((-3.4944190531, 10.159039214), 0.7, 0, 180)
                Line((-4.1944190531, 10.159039214), (-4.1944190531, 8.7423711106))
                CenterArc((-3.4944190531, 8.7423711106), 0.7, 180, 180)
                Line((-2.7944190531, 8.7423711106), (-2.7944190531, 10.159039214))
            make_face()
            with BuildLine():
                CenterArc((-3.4944190531, 10.159039214), 0.475, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((-3.4944190531, 8.7423711106), 0.475, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.05
        extrude(amount=-0.05, mode=Mode.SUBTRACT)

        # Sketch9 -> Extrude8 (Cut)
        # Sketch on Profile plane
        # Sketch has 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((-3.5118674102, 10.159039214)):
                Circle(0.15)
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((-3.5118674102, 8.7423711106)):
                Circle(0.15)
        # OneSide extrude, distance=-0.1
        extrude(amount=-0.1, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a rectangular enclosure or chassis with a trapezoidal profile, featuring a central blue panel or window, black structural frame members with diagonal bracing, and mounting flanges or attachment points on the sides.
def model_136816_c21745e0_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 8 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 25.200000751, perimeter: 20.400000304
            with BuildLine():
                Line((3.0000000447, -2.1000000313), (3.0000000447, 2.1000000313))
                Line((3.0000000447, 2.1000000313), (-3.0000000447, 2.1000000313))
                Line((-3.0000000447, 2.1000000313), (-3.0000000447, -2.1000000313))
                Line((-3.0000000447, -2.1000000313), (3.0000000447, -2.1000000313))
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        # Sketch has 8 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 4.2400000608, perimeter: 42.400000608
            with BuildLine():
                Line((3.2000000447, -2.3000000313), (3.2000000447, 2.3000000313))
                Line((3.2000000447, 2.3000000313), (-3.2000000447, 2.3000000313))
                Line((-3.2000000447, 2.3000000313), (-3.2000000447, -2.3000000313))
                Line((-3.2000000447, -2.3000000313), (3.2000000447, -2.3000000313))
            make_face()
            with BuildLine():
                Line((-3.0000000447, -2.1000000313), (3.0000000447, -2.1000000313))
                Line((-3.0000000447, 2.1000000313), (-3.0000000447, -2.1000000313))
                Line((3.0000000447, 2.1000000313), (-3.0000000447, 2.1000000313))
                Line((3.0000000447, -2.1000000313), (3.0000000447, 2.1000000313))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=2.5
        extrude(amount=2.5, mode=Mode.ADD)

        # Sketch2 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(3.2000000447, 0, 0), x_dir=(0, 1, 0), z_dir=(1, 0, 0))):
            # Profile area: 1.7600000525, perimeter: 9.6000001431
            with BuildLine():
                Line((2.2000000328, 0), (-2.2000000328, 0))
                Line((2.2000000328, 0.400000006), (2.2000000328, 0))
                Line((-2.2000000328, 0.400000006), (2.2000000328, 0.400000006))
                Line((-2.2000000328, 0), (-2.2000000328, 0.400000006))
            make_face()
        # OneSide extrude, distance=2.1
        extrude(amount=2.1, mode=Mode.ADD)

        # Sketch3 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.400000006), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((-3.6000000536, -1.8000000268)):
                Circle(0.2)
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((-4.8000000715, -1.8000000268)):
                Circle(0.2)
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((-3.6000000536, 1.6000000238)):
                Circle(0.2)
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((-4.900000073, 1.6000000238)):
                Circle(0.2)
        # OneSide extrude, distance=-0.6
        extrude(amount=-0.6, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(-3.2000000447, 0, 0), x_dir=(0, -1, 0), z_dir=(-1, 0, 0))):
            # Profile area: 0.1256637099, perimeter: 1.2566370802
            with Locations((-1.9922724297, 2.1768172324)):
                Circle(0.200000003)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)

        # Sketch5 -> Extrude6 (Join)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 2.5), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0122836962, perimeter: 0.4826445788
            with BuildLine():
                Line((-3.1000000492, 0), (-3.2000000447, 0))
                Line((-3.2000000447, 0), (-3.2000000447, -0.1732050782))
                CenterArc((-3.3000000492, 0), 0.2, -59.9999985212, 59.9999985212)
            make_face()
            # Profile area: 0.1010963137, perimeter: 1.1841682076
            with BuildLine():
                Line((-3.2000000447, 0), (-3.2000000447, -0.1732050782))
                Line((-3.2000000447, 0.1732050782), (-3.2000000447, 0))
                CenterArc((-3.3000000492, 0), 0.2, 59.9999985212, 240.0000029576)
            make_face()
            # Profile area: 0.0122836962, perimeter: 0.4826445788
            with BuildLine():
                CenterArc((-3.3000000492, 0), 0.2, 0, 59.9999985212)
                Line((-3.2000000447, 0.1732050782), (-3.2000000447, 0))
                Line((-3.1000000492, 0), (-3.2000000447, 0))
            make_face()
        # OneSide extrude, distance=-2.1
        extrude(amount=-2.1, mode=Mode.ADD)
    return part.part


# Description: This is a dual-panel solar array module featuring two rectangular blue photovoltaic panels connected by a central hinge mechanism, allowing the panels to fold together for transport or adjust their angle for optimal sun exposure.
def model_136886_e7626c2e_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 88, perimeter: 38
            with BuildLine():
                Line((5.5, 2.5), (-2.5, 2.5))
                Line((-2.5, 2.5), (-2.5, -8.5))
                Line((-2.5, -8.5), (5.5, -8.5))
                Line((5.5, -8.5), (5.5, 2.5))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 34 constraints, 14 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.09, perimeter: 1.2
            with BuildLine():
                Line((-0.6500000052, -6.025), (-0.6500000052, -5.725))
                Line((-0.3500000052, -6.025), (-0.6500000052, -6.025))
                Line((-0.3500000052, -5.725), (-0.3500000052, -6.025))
                Line((-0.6500000052, -5.725), (-0.3500000052, -5.725))
            make_face()
            # Profile area: 0.0900000013, perimeter: 1.2000000089
            with BuildLine():
                Line((-0.6500000097, -0.275), (-0.6500000097, 0.025))
                Line((-0.3500000052, -0.275), (-0.6500000097, -0.275))
                Line((-0.3500000052, 0.025), (-0.3500000052, -0.275))
                Line((-0.6500000097, 0.025), (-0.3500000052, 0.025))
            make_face()
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 8 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.1999996662, perimeter: 16.7999999166
            with BuildLine():
                Line((-5.500000082, 2.8000000417), (2.499999918, 2.8000000417))
                Line((2.499999918, 2.8000000417), (2.5, 3.2))
                Line((-5.2488457606, 3.2), (2.5, 3.2))
                Line((-5.2488457606, 3.2), (-5.5, 3.2))
                Line((-5.5, 3.2), (-5.5, 3))
                Line((-5.500000082, 2.8000000417), (-5.5, 3))
            make_face()
        # OneSide extrude, distance=0.05
        extrude(amount=0.05, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.55, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.8, perimeter: 16.2
            with BuildLine():
                Line((-5.5000000307, 3.0500016319), (2.4999999693, 3.0499999927))
                Line((-5.5000000512, 2.9500016319), (-5.5000000307, 3.0500016319))
                Line((2.4999999488, 2.9499999927), (-5.5000000512, 2.9500016319))
                Line((2.4999999488, 2.9499999927), (2.4999999693, 3.0499999927))
            make_face()
        # OneSide extrude, distance=-0.05
        extrude(amount=-0.05, mode=Mode.SUBTRACT)

        # Sketch6 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 8 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0900000003, perimeter: 1.2000000035
            with BuildLine():
                Line((0.1999999772, -1.0250000251), (0.4999999807, -1.0250000205))
                Line((0.1999999818, -1.3250000251), (0.1999999772, -1.0250000251))
                Line((0.3499999818, -1.3250000228), (0.1999999818, -1.3250000251))
                Line((0.4999999818, -1.3250000205), (0.3499999818, -1.3250000228))
                Line((0.4999999795, -1.1750000205), (0.4999999818, -1.3250000205))
                Line((0.4999999807, -1.0250000205), (0.4999999795, -1.1750000205))
            make_face()
        # OneSide extrude, distance=-0.35
        extrude(amount=-0.35, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a curved bracket or mounting block featuring a rounded, boat-shaped profile with two circular holes on opposing sides and a flat mounting base with ventilation slots or cutouts along its surface.
def model_136922_a27905c9_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 153.279012427, perimeter: 43.8880493706
            Circle(6.985)
        # OneSide extrude, distance=1.905
        extrude(amount=1.905)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.905, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 38.3197531067, perimeter: 21.9440246853
            Circle(3.4925)
        # OneSide extrude, distance=3.81
        extrude(amount=3.81, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 5.715, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 19.6349540849, perimeter: 15.7079632679
            Circle(2.5)
        # OneSide extrude, distance=-20
        extrude(amount=-20, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude4 (Cut)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 1.905, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            with Locations((0, -5.5)):
                Circle(1)
        # OneSide extrude, distance=-7.5
        extrude(amount=-7.5, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude5 (Cut)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 1.905, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            with Locations((5.5, 0)):
                Circle(1)
        # OneSide extrude, distance=-3.5
        extrude(amount=-3.5, mode=Mode.SUBTRACT)

        # Sketch6 -> Extrude6 (Cut)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 1.905, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            with Locations((-5.5, 0)):
                Circle(1)
        # OneSide extrude, distance=-6
        extrude(amount=-6, mode=Mode.SUBTRACT)

        # Sketch7 -> Extrude7 (Cut)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 1.905, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            with Locations((0, 5.5)):
                Circle(1)
        # OneSide extrude, distance=-4
        extrude(amount=-4, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a twisted or helical rectangular duct/channel component with slotted openings along its sides and a pyramidal or tapered top section, featuring a complex curved geometry that appears designed for fluid flow or ventilation purposes.
def model_138128_8f07de22_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 8 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 6.0713425245, perimeter: 10.5342508123
            with BuildLine():
                Line((9, -7.3961200313), (9, -9.1))
                Line((9, -9.1), (12.5632454374, -9.1))
                Line((12.5632454374, -9.1), (12.5632454374, -7.3961200313))
                Line((12.5632454374, -7.3961200313), (9, -7.3961200313))
            make_face()
        # OneSide extrude, distance=5.5
        extrude(amount=5.5)

        # Sketch3 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 14 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 9.1), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.690516028, perimeter: 4.3836130673
            with BuildLine():
                CenterArc((-13.3969956413, -2.8106519718), 1.3191374984, -50.799066758, 101.5981335159)
                Line((-12.5632454374, -1.7884072176), (-12.5632454374, -3.8328967259))
            make_face()
        # OneSide extrude, distance=-1.6
        extrude(amount=-1.6, mode=Mode.SUBTRACT)

        # Sketch4 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 9.1), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.6409098987, perimeter: 4.3400124495
            with BuildLine():
                CenterArc((-8.0797940731, -2.8202060893), 1.3738994158, 132.0498464549, 95.900314622)
                Line((-9, -3.8404122728), (-9.0000001341, -1.8000000268))
            make_face()
        # OneSide extrude, distance=-1.8
        extrude(amount=-1.8, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 9.1), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 5.25, perimeter: 10
            with BuildLine():
                Line((-11.5, -1), (-10, -1))
                Line((-11.5, -4.5), (-11.5, -1))
                Line((-10, -4.5), (-11.5, -4.5))
                Line((-10, -1), (-10, -4.5))
            make_face()
        # OneSide extrude, distance=-0.2
        extrude(amount=-0.2, mode=Mode.SUBTRACT)

        # Sketch6 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 8.9), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 2.9155656501, perimeter: 8.3670094587
            with BuildLine():
                Line((-11.3000001684, -1.2000000179), (-10.4164954211, -1.2000000179))
                Line((-11.3000001684, -4.5), (-11.3000001684, -1.2000000179))
                Line((-10.4164954211, -4.5), (-11.3000001684, -4.5))
                Line((-10.4164954211, -1.2000000179), (-10.4164954211, -4.5))
            make_face()
        # OneSide extrude, distance=0.1
        extrude(amount=0.1, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical tube or sleeve with a hollow core, featuring a closed top end and an open bottom end, with a smooth external surface and what appears to be a seam or ridge running along its length.
def model_138157_8777dfee_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.5796418331, perimeter: 2.8340347282
            with BuildLine():
                Line((2.3509502373, -1.0386037729), (2.0169560416, -0.7046095772))
                Line((2.0169560416, -0.7046095772), (1.5607114855, -0.8268599375))
                Line((1.5607114855, -0.8268599375), (1.4384611252, -1.2831044936))
                Line((1.4384611252, -1.2831044936), (1.7724553209, -1.6170986893))
                Line((1.7724553209, -1.6170986893), (2.228699877, -1.494848329))
                Line((2.228699877, -1.494848329), (2.3509502373, -1.0386037729))
            make_face()
        # OneSide extrude, distance=9
        extrude(amount=9)
    return part.part


# Description: This is a complex automotive or mechanical engine component (possibly a cylinder head, intake manifold, or transmission housing) featuring an irregular, multi-faceted body with integrated cooling passages (shown in light blue), mounting bosses with cylindrical holes, and strategically placed flanges for assembly and fluid routing.
def model_138479_6ab3ef15_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 15 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.2306858347, perimeter: 5.7424777961
            with BuildLine():
                CenterArc((0.1, -0.15), 0.15, 90, 90)
                Line((-0.05, -1.35), (-0.05, -0.15))
                CenterArc((0.1, -1.35), 0.15, 180, 90)
                Line((1.3, -1.5), (0.1, -1.5))
                CenterArc((1.3, -1.35), 0.15, -90, 90)
                Line((1.45, -0.15), (1.45, -1.35))
                CenterArc((1.3, -0.15), 0.15, 0, 90)
                Line((0.1, 0), (1.3, 0))
            make_face()
        # OneSide extrude, distance=0.08
        extrude(amount=0.08)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 12 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.08, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.8771724537, perimeter: 5.3397787144
            with BuildLine():
                CenterArc((-0.105, 1.3475), 0.09, 0, 90)
                Line((-0.105, 1.4375), (-1.295, 1.4375))
                CenterArc((-1.295, 1.3475), 0.09, 90, 90)
                Line((-1.385, 1.3475), (-1.385, 0.1475))
                CenterArc((-1.3, 0.1475), 0.085, -180, 90)
                Line((-1.3, 0.0625), (-0.1, 0.0625))
                CenterArc((-0.1, 0.1475), 0.085, -90, 90)
                Line((-0.015, 0.1475), (-0.015, 1.3475))
            make_face()
        # OneSide extrude, distance=0.21
        extrude(amount=0.21, mode=Mode.ADD)

        # Sketch4 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 12 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 1.8775426419, perimeter: 5.3440707511
            with BuildLine():
                CenterArc((0.1025, 0.15), 0.0875, 180, 90)
                Line((0.1025, 0.0625), (1.3025, 0.0625))
                CenterArc((1.3025, 0.145), 0.0825, -90, 90)
                Line((1.385, 0.145), (1.385, 1.355))
                CenterArc((1.3025, 1.355), 0.0825, 0, 90)
                Line((1.3025, 1.4375), (0.1025, 1.4375))
                CenterArc((0.1025, 1.35), 0.0875, 90, 90)
                Line((0.015, 1.35), (0.015, 0.15))
            make_face()
        # OneSide extrude, distance=0.21
        extrude(amount=0.21, mode=Mode.ADD)

        # Sketch5 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 15 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.29, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.7478539816, perimeter: 3.5641592654
            with BuildLine():
                CenterArc((-0.15, 0.5153048903), 0.05, -90, 90)
                Line((-0.1, 1.0403048903), (-0.1, 0.5153048903))
                CenterArc((-0.15, 1.0403048903), 0.05, 0, 90)
                Line((-1.25, 1.0903048903), (-0.15, 1.0903048903))
                CenterArc((-1.25, 1.0403048903), 0.05, 90, 90)
                Line((-1.3, 0.5153048903), (-1.3, 1.0403048903))
                CenterArc((-1.25, 0.5153048903), 0.05, -180, 90)
                Line((-0.15, 0.4653048903), (-1.25, 0.4653048903))
            make_face()
        # OneSide extrude, distance=0.05
        extrude(amount=0.05, mode=Mode.ADD)

        # Sketch6 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 16 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.34, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0205389774, perimeter: 1.0997905577
            with BuildLine():
                Line((-0.7, 1.0500000156), (-0.9546207198, 1.0500000156))
                Line((-0.4450303157, 1.0500000156), (-0.7, 1.0500000156))
                Line((-0.4450303157, 1.0500000156), (-0.4450303157, 1.0903048903))
                Line((-0.4450303157, 1.0903048903), (-0.9546207198, 1.0903048903))
                Line((-0.9546207198, 1.0500000156), (-0.9546207198, 1.0903048903))
            make_face()
            # Profile area: 0.0261173501, perimeter: 1.1216841124
            with BuildLine():
                Line((-0.7, 0.9987483636), (-0.4450303157, 0.9987483636))
                Line((-0.4450303157, 0.9987483636), (-0.4450303157, 1.0500000156))
                Line((-0.4450303157, 1.0500000156), (-0.7, 1.0500000156))
                Line((-0.7, 1.0500000156), (-0.9546207198, 1.0500000156))
                Line((-0.9546207198, 0.9987483636), (-0.9546207198, 1.0500000156))
                Line((-0.9546207198, 0.9987483636), (-0.7, 0.9987483636))
            make_face()
            # Profile area: 0.229175, perimeter: 1.92
            with BuildLine():
                Line((-0.7, 0.5537483636), (-1.215, 0.5537483636))
                Line((-0.7, 0.5537483636), (-0.7, 0.9987483636))
                Line((-0.9546207198, 0.9987483636), (-0.7, 0.9987483636))
                Line((-1.215, 0.9987483636), (-0.9546207198, 0.9987483636))
                Line((-1.215, 0.5537483636), (-1.215, 0.9987483636))
            make_face()
            # Profile area: 0.229175, perimeter: 1.92
            with BuildLine():
                Line((-0.185, 0.5537483636), (-0.7, 0.5537483636))
                Line((-0.185, 0.9987483636), (-0.185, 0.5537483636))
                Line((-0.4450303157, 0.9987483636), (-0.185, 0.9987483636))
                Line((-0.7, 0.9987483636), (-0.4450303157, 0.9987483636))
                Line((-0.7, 0.5537483636), (-0.7, 0.9987483636))
            make_face()
        # OneSide extrude, distance=-0.05
        extrude(amount=-0.05, mode=Mode.SUBTRACT)

        # Sketch7 -> Extrude6 (Join)
        # Sketch on BRepFace
        # Sketch has 16 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.29, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.229175, perimeter: 1.92
            with BuildLine():
                Line((-0.4450303157, 0.9987483636), (-0.185, 0.9987483636))
                Line((-0.55, 0.9987483636), (-0.4450303157, 0.9987483636))
                Line((-0.55, 0.9987483636), (-0.7, 0.9987483636))
                Line((-0.7, 0.5537483636), (-0.7, 0.9987483636))
                Line((-0.185, 0.5537483636), (-0.7, 0.5537483636))
                Line((-0.185, 0.9987483636), (-0.185, 0.5537483636))
            make_face()
            # Profile area: 0.229175, perimeter: 1.92
            with BuildLine():
                Line((-0.7, 0.9987483636), (-0.85, 0.9987483636))
                Line((-0.9546207198, 0.9987483636), (-0.85, 0.9987483636))
                Line((-1.215, 0.9987483636), (-0.9546207198, 0.9987483636))
                Line((-1.215, 0.5537483636), (-1.215, 0.9987483636))
                Line((-0.7, 0.5537483636), (-1.215, 0.5537483636))
                Line((-0.7, 0.5537483636), (-0.7, 0.9987483636))
            make_face()
            # Profile area: 0.0345, perimeter: 0.83
            with BuildLine():
                Line((-0.55, 1.1137483636), (-0.55, 0.9987483636))
                Line((-0.7, 1.1137483636), (-0.55, 1.1137483636))
                Line((-0.85, 1.1137483636), (-0.7, 1.1137483636))
                Line((-0.85, 0.9987483636), (-0.85, 1.1137483636))
                Line((-0.7, 0.9987483636), (-0.85, 0.9987483636))
                Line((-0.55, 0.9987483636), (-0.7, 0.9987483636))
            make_face()
        # OneSide extrude, distance=0.314
        extrude(amount=0.314, mode=Mode.ADD)

        # Sketch10 -> Extrude9 (Join)
        # Sketch on BRepFace
        # Sketch has 29 constraints, 11 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -0.21, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.0018, perimeter: 0.22
            with BuildLine():
                Line((0.6575, 1.358), (0.7025, 1.358))
                Line((0.6575, 1.338), (0.6575, 1.358))
                Line((0.7475, 1.338), (0.6575, 1.338))
                Line((0.7475, 1.358), (0.7475, 1.338))
                Line((0.7025, 1.358), (0.7475, 1.358))
            make_face()
            # Profile area: 0.0032, perimeter: 0.24
            with BuildLine():
                Line((0.225, 1.098), (0.145, 1.098))
                Line((0.225, 1.138), (0.225, 1.098))
                Line((0.145, 1.138), (0.225, 1.138))
                Line((0.145, 1.098), (0.145, 1.138))
            make_face()
        # OneSide extrude, distance=0.285
        extrude(amount=0.285, mode=Mode.ADD)

        # Sketch10 -> Extrude10 (Join)
        # Sketch on BRepFace
        # Sketch has 29 constraints, 11 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -0.21, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.0186265028, perimeter: 0.4838052687
            with Locations((0.1685, 0.7500000153)):
                Circle(0.077)
            # Profile area: 0.0387185587, perimeter: 0.8072300466
            with BuildLine():
                Line((0.7025, 0.75), (0.5455, 0.75))
                Line((0.7025, 0.75), (0.8595, 0.75))
                CenterArc((0.7025, 0.75), 0.157, 0, 180)
            make_face()
            # Profile area: 0.0193592793, perimeter: 0.5606150233
            with BuildLine():
                Line((0.7025, 0.75), (0.7025, 0.593))
                Line((0.7025, 0.75), (0.5455, 0.75))
                CenterArc((0.7025, 0.75), 0.157, -180, 90)
            make_face()
            # Profile area: 0.0193592793, perimeter: 0.5606150233
            with BuildLine():
                CenterArc((0.7025, 0.75), 0.157, -90, 90)
                Line((0.7025, 0.75), (0.8595, 0.75))
                Line((0.7025, 0.75), (0.7025, 0.593))
            make_face()
            # Profile area: 0.0186265028, perimeter: 0.4838052687
            with Locations((1.2365, 0.75)):
                Circle(0.077)
        # OneSide extrude, distance=0.265
        extrude(amount=0.265, mode=Mode.ADD)
    return part.part


# Description: This is a disc or pulley wheel with an overall elliptical/oval disc shape and a central hub or axle hole, featuring a curved, slightly domed surface with a smooth finish.
def model_138844_0291c208_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 176.7145867644, perimeter: 47.1238898038
            Circle(7.5)
        # OneSide extrude, distance=0.6
        extrude(amount=0.6)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.6), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 15.9043128088, perimeter: 14.1371669412
            Circle(2.25)
        # OneSide extrude, distance=2.2
        extrude(amount=2.2, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (NewBody)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 2.8), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 47.7129384264, perimeter: 42.4115008235
            with BuildLine():
                CenterArc((0, 0), 4.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 2.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.6
        extrude(amount=0.6)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 2.8), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 15.9043128088, perimeter: 14.1371669412
            Circle(2.25)
        # OneSide extrude, distance=0.6
        extrude(amount=0.6, mode=Mode.ADD)

        # Sketch5 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 3.4), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.6730742002, perimeter: 2.9082812538
            with Locations((3.2827102416, -0.0125719765)):
                Circle(0.4628673374)
        # OneSide extrude, distance=-0.6
        extrude(amount=-0.6, mode=Mode.SUBTRACT)

        # Sketch6 -> Extrude6 (Join)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 3.4), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.6361725124, perimeter: 2.8274333882
            with Locations((-0.0286877492, 5.8852931351)):
                Circle(0.45)
        # OneSide extrude, distance=-3
        extrude(amount=-3, mode=Mode.ADD)
    return part.part


# Description: This is a fan shroud or air intake duct assembly featuring a cylindrical mesh-covered housing with curved aerodynamic surfaces, a rectangular mounting flange on one side, and a cylindrical outlet port at the bottom for directing airflow.
def model_138943_bd47b743_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.8364678936, perimeter: 3.2421236185
            Circle(0.516)
        # OneSide extrude, distance=0.8
        extrude(amount=0.8)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.8), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.252571951, perimeter: 3.94098798
            with BuildLine():
                CenterArc((0, 0), 0.516, -180, 179.3275452028)
                Line((-0.516, 0), (-0.516, -0.647))
                Line((-0.516, -0.647), (0.5159644618, -0.6530559209))
                Line((0.5159644618, -0.0060559209), (0.5159644618, -0.6530559209))
            make_face()
        # OneSide extrude, distance=-0.8
        extrude(amount=-0.8, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on XY construction plane
        # Sketch has 6 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.2063928924, perimeter: 2.4639289236
            with BuildLine():
                Line((-0.516, -0.6530559209), (-0.516, -0.647))
                Line((0.5159644618, -0.6530559209), (-0.516, -0.6530559209))
                Line((0.5159644618, -0.4530559209), (0.5159644618, -0.6530559209))
                Line((-0.516, -0.4530559209), (0.5159644618, -0.4530559209))
                Line((-0.516, -0.647), (-0.516, -0.4530559209))
            make_face()
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.ADD)

        # Sketch4 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-0.003814456, -0.6500056802, 0), x_dir=(0, 0, 1), z_dir=(-0.0058682415, -0.9999827817, 0))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((0.4500000067, 0)):
                Circle(0.2)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)

        # Sketch5 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.8), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.3992720789, perimeter: 2.239955562
            Circle(0.3565)
        # OneSide extrude, distance=0.63
        extrude(amount=0.63, mode=Mode.ADD)

        # Sketch6 -> Extrude6 (Cut)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1.43), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.1638, perimeter: 1.67
            with BuildLine():
                Line((0.26, -0.1575), (0.26, 0.1575))
                Line((0.26, 0.1575), (-0.26, 0.1575))
                Line((-0.26, 0.1575), (-0.26, -0.1575))
                Line((-0.26, -0.1575), (0.26, -0.1575))
            make_face()
        # OneSide extrude, distance=-1.1
        extrude(amount=-1.1, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a rectangular ladder or rack frame structure composed of parallel vertical posts connected by horizontal cross-members, featuring an open grid-like lattice design with regular rectangular openings.
def model_140700_644ef199_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 27 constraints, 9 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 56.25, perimeter: 30
            with BuildLine():
                Line((-76.5, 16), (-84, 16))
                Line((-76.5, 23.5), (-76.5, 16))
                Line((-84, 23.5), (-76.5, 23.5))
                Line((-84, 16), (-84, 23.5))
            make_face()
            # Profile area: 56.25, perimeter: 30
            with BuildLine():
                Line((-30.5, 23.5), (-23, 23.5))
                Line((-30.5, 16), (-30.5, 23.5))
                Line((-23, 16), (-30.5, 16))
                Line((-23, 23.5), (-23, 16))
            make_face()
            # Profile area: 56.25, perimeter: 30
            with BuildLine():
                Line((30.5, 23.5), (23, 23.5))
                Line((23, 23.5), (23, 16))
                Line((23, 16), (30.5, 16))
                Line((30.5, 16), (30.5, 23.5))
            make_face()
            # Profile area: 56.25, perimeter: 30
            with BuildLine():
                Line((23, -16), (30.5, -16))
                Line((23, -23.5), (23, -16))
                Line((30.5, -23.5), (23, -23.5))
                Line((30.5, -16), (30.5, -23.5))
            make_face()
            # Profile area: 56.25, perimeter: 30
            with BuildLine():
                Line((-23, -23.5), (-23, -16))
                Line((-23, -16), (-30.5, -16))
                Line((-30.5, -16), (-30.5, -23.5))
                Line((-30.5, -23.5), (-23, -23.5))
            make_face()
            # Profile area: 56.25, perimeter: 30
            with BuildLine():
                Line((-76.5, -23.5), (-76.5, -16))
                Line((-76.5, -16), (-84, -16))
                Line((-84, -16), (-84, -23.5))
                Line((-84, -23.5), (-76.5, -23.5))
            make_face()
        # OneSide extrude, distance=46
        extrude(amount=46)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -16), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 56.25, perimeter: 30
            with BuildLine():
                Line((30.5, 38.5), (23, 38.5))
                Line((30.5, 46), (30.5, 38.5))
                Line((23, 46), (30.5, 46))
                Line((23, 38.5), (23, 46))
            make_face()
        # OneSide extrude, distance=35
        extrude(amount=35, mode=Mode.ADD)

        # Sketch4 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 12 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(23, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 56.25, perimeter: 30
            with BuildLine():
                Line((-16, 46), (-16, 38.5))
                Line((-23.5, 46), (-16, 46))
                Line((-23.5, 38.5), (-23.5, 46))
                Line((-16, 38.5), (-23.5, 38.5))
            make_face()
            # Profile area: 56.25, perimeter: 30
            with BuildLine():
                Line((23.5, 38.5), (23.5, 46))
                Line((23.5, 46), (16, 46))
                Line((16, 46), (16, 38.5))
                Line((16, 38.5), (23.5, 38.5))
            make_face()
        # OneSide extrude, distance=105
        extrude(amount=105, mode=Mode.ADD)

        # Sketch5 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 16), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 56.25, perimeter: 30
            with BuildLine():
                Line((84, 38.5), (84, 46))
                Line((84, 46), (76.5, 46))
                Line((76.5, 46), (76.5, 38.5))
                Line((76.5, 38.5), (84, 38.5))
            make_face()
        # OneSide extrude, distance=35
        extrude(amount=35, mode=Mode.ADD)

        # Sketch6 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 17 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 46, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 56.25, perimeter: 30
            with BuildLine():
                Line((76.5, 16), (84, 16))
                Line((84, 16), (84, 23.5))
                Line((84, 23.5), (76.5, 23.5))
                Line((76.5, 23.5), (76.5, 16))
            make_face()
            # Profile area: 56.25, perimeter: 30
            with BuildLine():
                Line((30.5, 16), (30.5, 23.5))
                Line((30.5, 23.5), (23, 23.5))
                Line((23, 23.5), (23, 16))
                Line((23, 16), (30.5, 16))
            make_face()
            # Profile area: 56.25, perimeter: 30
            with BuildLine():
                Line((-23, 23.5), (-23, 16))
                Line((-30.5, 23.5), (-23, 23.5))
                Line((-30.5, 16), (-30.5, 23.5))
                Line((-23, 16), (-30.5, 16))
            make_face()
        # OneSide extrude, distance=38
        extrude(amount=38, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical connector or coupling assembly featuring a dark cylindrical body on the left connected to a blue rectangular flange or mounting plate on the right, with what appears to be internal geometry and mounting features visible through the transparent rendering.
def model_141096_54f486ec_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 25 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.0278596144, perimeter: 5.7814646047
            with BuildLine():
                CenterArc((0, 0), 2.1, -28.4368906112, 56.8737812224)
                Line((1.8466185232, 1.0000000149), (1.0000000149, 1.0000000149))
                Line((1.0000000149, 1.0000000149), (1.0000000149, 0.2249999338))
                CenterArc((0, 0), 1.025, -12.6803796973, 25.3607593945)
                Line((1.0000000149, -0.2249999338), (1.0000000149, -1.0000000149))
                Line((1.0000000149, -1.0000000149), (1.8466185232, -1.0000000149))
            make_face()
            # Profile area: 1.1039414032, perimeter: 4.2071658851
            with BuildLine():
                Line((3.9964154066, -1.0000000149), (3.9964154066, -2.0999982896))
                Line((3.9964154066, -2.0999982896), (5.0000000745, -2.0999982896))
                Line((5.0000000745, -2.0999982896), (5.0000000745, -1.0000000149))
                Line((3.9964154066, -1.0000000149), (5.0000000745, -1.0000000149))
            make_face()
            # Profile area: 1.6273984175, perimeter: 6.3416057038
            with BuildLine():
                Line((1.0000000149, -1.0000000149), (1.8466185232, -1.0000000149))
                Line((1.0000000149, -0.2249999338), (1.0000000149, -1.0000000149))
                CenterArc((0, 0), 1.025, -90.1498219223, 77.469442225)
                Line((-0.0026802549, -1.0249964957), (-0.0026802549, -2.0999982896))
                Line((-0.0026802549, -2.0999982896), (0.0026802549, -2.0999982896))
                CenterArc((0, 0), 2.1, -89.9268726967, 61.4899820855)
            make_face()
            # Profile area: 1.6273984252, perimeter: 6.3416074462
            with BuildLine():
                CenterArc((0, 0), 2.1, 28.4368906112, 61.5631093888)
                Line((0, 2.1000000209), (-0.0026802549, 2.1000000313))
                Line((-0.0026802549, 2.1000000313), (-0.0026802549, 2.0999982896))
                Line((-0.0026802549, 2.0999982896), (-0.0026802549, 1.0249964957))
                CenterArc((0, 0), 1.025, 12.6803796973, 77.469442225)
                Line((1.0000000149, 1.0000000149), (1.0000000149, 0.2249999338))
                Line((1.8466185232, 1.0000000149), (1.0000000149, 1.0000000149))
            make_face()
            # Profile area: 1.1000000328, perimeter: 4.2000000626
            with BuildLine():
                Line((5.0000000745, 1.0000000149), (5.0000000745, 2.1000000313))
                Line((5.0000000745, 2.1000000313), (4.0000000596, 2.1000000313))
                Line((4.0000000596, 1.0000000149), (4.0000000596, 2.1000000313))
                Line((5.0000000745, 1.0000000149), (4.0000000596, 1.0000000149))
            make_face()
            # Profile area: 5.9646221448, perimeter: 10.3912960872
            with BuildLine():
                Line((3.9964154066, -1.0000000149), (5.0000000745, -1.0000000149))
                Line((5.0000000745, -1.0000000149), (5.0000000745, 1.0000000149))
                Line((5.0000000745, 1.0000000149), (4.0000000596, 1.0000000149))
                Line((1.8466185232, 1.0000000149), (4.0000000596, 1.0000000149))
                CenterArc((0, 0), 2.1, -28.4368906112, 56.8737812224)
                Line((1.8466185232, -1.0000000149), (3.9964154066, -1.0000000149))
            make_face()
            # Profile area: 5.271131359, perimeter: 11.9567596029
            with BuildLine():
                Line((-0.0026802549, -1.0249964957), (-0.0026802549, -2.0999982896))
                CenterArc((0, 0), 1.025, 90.1498219223, 179.7003561555)
                Line((-0.0026802549, 2.0999982896), (-0.0026802549, 1.0249964957))
                CenterArc((0, 0), 2.1, 90.0731273033, 179.8537453933)
            make_face()
        # OneSide extrude, distance=2.8
        extrude(amount=2.8)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 4.2075261486, perimeter: 10.403584537
            with BuildLine():
                Line((4.0000000596, -2.1000000313), (5.0000000745, -2.1000000313))
                Line((5.0000000745, -2.1000000313), (5.0000000745, 2.0999982896))
                Line((5.0000000745, 2.0999982896), (3.9964154066, 2.0999982896))
                Line((3.9964154066, 2.0999982896), (3.9964154066, 1.0000000149))
                Line((3.9964154066, 1.0000000149), (4.0000000596, -1.0000000149))
                Line((4.0000000596, -1.0000000149), (4.0000000596, -2.1000000313))
            make_face()
        # OneSide extrude, distance=1.2
        extrude(amount=1.2, mode=Mode.ADD)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 8 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2.8, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.2075261486, perimeter: 10.403584537
            with BuildLine():
                Line((-3.9964154066, 1.0000000149), (-4.0000000596, -1.0000000149))
                Line((-3.9964154066, 1.0000000149), (-3.9964154066, 2.0999982896))
                Line((-3.9964154066, 2.0999982896), (-5.0000000745, 2.0999982896))
                Line((-5.0000000745, 2.0999982896), (-5.0000000745, -2.1000000313))
                Line((-5.0000000745, -2.1000000313), (-4.0000000596, -2.1000000313))
                Line((-4.0000000596, -2.1000000313), (-4.0000000596, -1.0000000149))
            make_face()
        # OneSide extrude, distance=1.2
        extrude(amount=1.2, mode=Mode.ADD)

        # Sketch9 -> Extrude4 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.9760782022, perimeter: 7.0685834706
            Circle(1.125)
        # OneSide extrude, distance=2.8
        extrude(amount=2.8, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical container or vessel with an angled top opening, featuring vertical ribbing or fluting on its curved sidewalls and a flat or slightly tapered rectangular lid/cover element on top.
def model_141168_03e1161c_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2021.6559139847, perimeter: 174.1473400509
            with BuildLine():
                Line((0, -38.1), (0, 0))
                CenterArc((19.05, -38.1), 19.05, 180, 180)
                Line((38.1, 0), (38.1, -38.1))
                Line((0, 0), (38.1, 0))
            make_face()
        # OneSide extrude, distance=38.1
        extrude(amount=38.1)

        # Sketch3 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 38.1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 174.1931947678, perimeter: 60.9599990845
            with BuildLine():
                Line((-7.6199998856, 38.0999994278), (-30.4799995422, 38.0999994278))
                Line((-7.6199998856, 45.7199993134), (-7.6199998856, 38.0999994278))
                Line((-30.4799995422, 45.7199993134), (-7.6199998856, 45.7199993134))
                Line((-30.4799995422, 38.0999994278), (-30.4799995422, 45.7199993134))
            make_face()
        # OneSide extrude, distance=1.905
        extrude(amount=1.905, mode=Mode.ADD)

        # Sketch9 -> Extrude4 (Join)
        # Sketch on BRepFace
        # Sketch has 15 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 38.1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 645.16, perimeter: 101.6
            with BuildLine():
                Line((-6.35, 5.08), (-6.35, 30.48))
                Line((-6.35, 30.48), (-31.75, 30.48))
                Line((-31.75, 30.48), (-31.75, 5.08))
                Line((-31.75, 5.08), (-19.05, 5.08))
                Line((-19.05, 5.08), (-6.35, 5.08))
            make_face()
        # OneSide extrude, distance=0.254
        extrude(amount=0.254, mode=Mode.ADD)

        # Sketch11 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 10 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, -1, 0), z_dir=(-1, 0, 0))):
            # Profile area: 645.16, perimeter: 101.6
            with BuildLine():
                Line((-31.75, 5.08), (-19.05, 5.08))
                Line((-19.05, 5.08), (-6.35, 5.08))
                Line((-6.35, 5.08), (-6.35, 30.48))
                Line((-6.35, 30.48), (-31.75, 30.48))
                Line((-31.75, 30.48), (-31.75, 5.08))
            make_face()
        # OneSide extrude, distance=0.254
        extrude(amount=0.254, mode=Mode.ADD)
    return part.part


# Description: This is a blue anodized aluminum channel or extrusion with a parallelogram cross-section, featuring a central longitudinal slot running along its length and a recessed rectangular pocket on the upper surface.
def model_141742_0e1d8c2e_0001():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 63, perimeter: 33
            with BuildLine():
                Line((0, 10.5), (0, 0))
                Line((0, 0), (6, 0))
                Line((6, 0), (6, 10.5))
                Line((6, 10.5), (0, 10.5))
            make_face()
        # OneSide extrude, distance=0.65
        extrude(amount=0.65)

        # Sketch3 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 10.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))) as sk:
            # Profile area: 2.1031725877, perimeter: 10.0646370614
            with BuildLine():
                Line((-0.875, 0.65), (-0.875, 0.096))
                Line((-2.6, 0.65), (-0.875, 0.65))
                CenterArc((-3, 0.65), 0.4, 180, 180)
                Line((-3.4, 0.65), (-5.125, 0.65))
                Line((-5.125, 0.096), (-5.125, 0.65))
                Line((-0.875, 0.096), (-5.125, 0.096))
            make_face()
            # Profile area: 0.2513274123, perimeter: 2.0566370614
            with BuildLine():
                Line((-3.4, 0.65), (-2.6, 0.65))
                CenterArc((-3, 0.65), 0.4, 180, 180)
            make_face()
        # TwoSides offset extrude, full=-10, trim=-4.1
        extrude(amount=-10, mode=Mode.SUBTRACT)
        extrude(sk.sketch, amount=-4.1, mode=Mode.ADD)

        # Sketch4 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.45, perimeter: 7.45
            with BuildLine():
                Line((-4.8, 0.65), (-4.8, 0.525))
                Line((-4.8, 0.525), (-1.2, 0.525))
                Line((-1.2, 0.525), (-1.2, 0.65))
                Line((-1.2, 0.65), (-3, 0.65))
                Line((-3, 0.65), (-4.8, 0.65))
            make_face()
        # OneSide extrude, distance=-1.7
        extrude(amount=-1.7, mode=Mode.SUBTRACT)

        # Sketch3 -> Extrude4 (Cut)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 10.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2513274123, perimeter: 2.0566370614
            with BuildLine():
                Line((-3.4, 0.65), (-2.6, 0.65))
                CenterArc((-3, 0.65), 0.4, 180, 180)
            make_face()
        # OneSide extrude, distance=-6
        extrude(amount=-6, mode=Mode.SUBTRACT)

        # Sketch5 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.65), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((-5.6, -0.4)):
                Circle(0.25)
        # OneSide extrude, distance=-0.47
        extrude(amount=-0.47, mode=Mode.SUBTRACT)

        # Sketch6 -> Extrude6 (Join)
        # Sketch on BRepFace
        # Sketch has 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.65), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.1565887588, perimeter: 2.2776546739
            with BuildLine():
                CenterArc((-0.4, -10.1), 0.25, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-0.4, -10.1), 0.1125, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.47
        extrude(amount=0.47, mode=Mode.ADD)
    return part.part


MODELS = {
    "model_101605_59c455b1_0000": {"func": model_101605_59c455b1_0000, "volume": 22.1821564224, "area": 78.5934172682},
    "model_106815_f6580357_0000": {"func": model_106815_f6580357_0000, "volume": 152.6808468532, "area": 237.5321166874},
    "model_107260_5d11b1b9_0000": {"func": model_107260_5d11b1b9_0000, "volume": 114.2681652638, "area": 173.7219152078},
    "model_109121_f33a42fa_0000": {"func": model_109121_f33a42fa_0000, "volume": 11.8319107416, "area": 57.42859711},
    "model_111043_c6235173_0000": {"func": model_111043_c6235173_0000, "volume": 0.0056998801, "area": 0.6216799582},
    "model_111506_a7273ee0_0000": {"func": model_111506_a7273ee0_0000, "volume": 235.9315913211, "area": 475.2452241985},
    "model_113343_e692c488_0006": {"func": model_113343_e692c488_0006, "volume": 0.0212057504, "area": 0.4241150082},
    "model_113698_dcf18f66_0022": {"func": model_113698_dcf18f66_0022, "volume": 0.1856046005, "area": 2.0468560242},
    "model_113841_5c85a0f0_0000": {"func": model_113841_5c85a0f0_0000, "volume": 127.2973343235, "area": 162.1061809252},
    "model_114495_ab1d8a08_0000": {"func": model_114495_ab1d8a08_0000, "volume": 21.5981865303, "area": 111.0956689886},
    "model_114867_991a50e4_0000": {"func": model_114867_991a50e4_0000, "volume": 47.4356689008, "area": 156.5663886198},
    "model_115629_40d61053_0000": {"func": model_115629_40d61053_0000, "volume": 1530.0224391714, "area": 2342.2089933857},
    "model_120132_b78e04ad_0000": {"func": model_120132_b78e04ad_0000, "volume": 209.3452424024, "area": 495.6705987982},
    "model_120465_0d427fa4_0000": {"func": model_120465_0d427fa4_0000, "volume": 0.9911013886, "area": 9.1104787957},
    "model_121262_f4a03dbc_0000": {"func": model_121262_f4a03dbc_0000, "volume": 136.2207619393, "area": 301.9415329885},
    "model_121264_68fcc38a_0000": {"func": model_121264_68fcc38a_0000, "volume": 114.7500263043, "area": 203.8559445261},
    "model_122579_2663ded3_0000": {"func": model_122579_2663ded3_0000, "volume": 9.4482095044, "area": 34.230828152},
    "model_125011_9b62f62f_0000": {"func": model_125011_9b62f62f_0000, "volume": 27.0297897442, "area": 371.0022438039},
    "model_128366_d8d9d0fd_0000": {"func": model_128366_d8d9d0fd_0000, "volume": 4.7115522714, "area": 31.2958256692},
    "model_128996_9ff71fb1_0000": {"func": model_128996_9ff71fb1_0000, "volume": 103.4701769682, "area": 161.3646003294},
    "model_129579_144d8158_0000": {"func": model_129579_144d8158_0000, "volume": 69.6165888855, "area": 160.2575191895},
    "model_129611_59e33fba_0000": {"func": model_129611_59e33fba_0000, "volume": 1208.1623325286, "area": 2011.2654028025},
    "model_130490_15f074ea_0003": {"func": model_130490_15f074ea_0003, "volume": 21499.4973451754, "area": 4774.8304509643},
    "model_130759_c37b385b_0002": {"func": model_130759_c37b385b_0002, "volume": 3.1138551104, "area": 16.720132472},
    "model_130917_2e98fb39_0002": {"func": model_130917_2e98fb39_0002, "volume": 1812.8447127682, "area": 2860.8542763877},
    "model_131580_c88dee64_0000": {"func": model_131580_c88dee64_0000, "volume": 41.6876380662, "area": 115.0394230755},
    "model_132291_265066d2_0000": {"func": model_132291_265066d2_0000, "volume": 138.1315952042, "area": 401.8856669651},
    "model_132668_067b89d4_0001": {"func": model_132668_067b89d4_0001, "volume": 69.4074888356, "area": 300.028407188},
    "model_132757_27127ea1_0000": {"func": model_132757_27127ea1_0000, "volume": 3.7113035499, "area": 23.6230697862},
    "model_133510_c26c1e00_0000": {"func": model_133510_c26c1e00_0000, "volume": 57.8659243274, "area": 103.325265712},
    "model_134667_e293572a_0000": {"func": model_134667_e293572a_0000, "volume": 154.7958647886, "area": 474.4887938131},
    "model_135067_f79b4c96_0000": {"func": model_135067_f79b4c96_0000, "volume": 1.2269073405, "area": 11.2935554014},
    "model_135873_2ceb32d1_0000": {"func": model_135873_2ceb32d1_0000, "volume": 2.6321916014, "area": 22.9416304741},
    "model_135897_34593cf4_0000": {"func": model_135897_34593cf4_0000, "volume": 18.5609392739, "area": 80.4617946453},
    "model_136355_b5fd1a59_0001": {"func": model_136355_b5fd1a59_0001, "volume": 0.0356073004, "area": 1.6950000034},
    "model_136473_1a062e83_0000": {"func": model_136473_1a062e83_0000, "volume": 381.7205043335, "area": 617.1429928305},
    "model_136635_d193c419_0000": {"func": model_136635_d193c419_0000, "volume": 59.6294931377, "area": 159.1524362147},
    "model_136816_c21745e0_0000": {"func": model_136816_c21745e0_0000, "volume": 19.4100725927, "area": 183.6254621788},
    "model_136886_e7626c2e_0000": {"func": model_136886_e7626c2e_0000, "volume": 44.2684999846, "area": 199.4499999937},
    "model_136922_a27905c9_0000": {"func": model_136922_a27905c9_0000, "volume": 301.8420793944, "area": 547.0177256746},
    "model_138128_8f07de22_0000": {"func": model_138128_8f07de22_0000, "volume": 30.4370810338, "area": 72.3722841413},
    "model_138157_8777dfee_0000": {"func": model_138157_8777dfee_0000, "volume": 5.2167764977, "area": 26.6655962199},
    "model_138479_6ab3ef15_0000": {"func": model_138479_6ab3ef15_0000, "volume": 1.1656602022, "area": 8.8516906139},
    "model_138844_0291c208_0000": {"func": model_138844_0291c208_0000, "volume": 180.5660294936, "area": 533.5113857027},
    "model_138943_bd47b743_0000": {"func": model_138943_bd47b743_0000, "volume": 1.1086215847, "area": 10.4552642609},
    "model_140700_644ef199_0000": {"func": model_140700_644ef199_0000, "volume": 35887.5, "area": 19140},
    "model_141096_54f486ec_0000": {"func": model_141096_54f486ec_0000, "volume": 60.6294078903, "area": 147.5418239631},
    "model_141168_03e1161c_0000": {"func": model_141168_03e1161c_0000, "volume": 77684.6696388491, "area": 10846.067082164},
    "model_141742_0e1d8c2e_0001": {"func": model_141742_0e1d8c2e_0001, "volume": 25.7843200421, "area": 161.0995290976},
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
