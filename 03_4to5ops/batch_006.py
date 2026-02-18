"""Batch 006 - passing/03_4to5ops
128 models bundled from Fusion360 Gallery reconstructions.
"""

from build123d import *
from build123d import Edge, BuildLine
from collections import Counter
from OCP.BRepBuilderAPI import BRepBuilderAPI_MakeEdge
from OCP.Geom import Geom_BSplineCurve
from OCP.TColStd import TColStd_Array1OfReal, TColStd_Array1OfInteger
from OCP.TColgp import TColgp_Array1OfPnt
from OCP.gp import gp_Pnt


# Description: This is a cylindrical sleeve or tube with a closed bottom end, an open top with a beveled edge, and vertical ribbing or fluting running along its exterior surface for structural reinforcement.
def model_22430_c6f08b03_0030():
    """Model: Cylinder v7"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.4560367312, perimeter: 7.1816808061
            with BuildLine():
                CenterArc((0, 0), 0.635, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.508, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=2.37998
        extrude(amount=2.37998)
    return part.part


# Description: This is a circular disc or plate with a flat, elliptical appearance featuring a textured or mesh-patterned rim edge around its perimeter and a smooth, dark central surface.
def model_22430_c6f08b03_0036():
    """Model: TimingWheel v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 9.3970168767, perimeter: 12.4881449573
            with BuildLine():
                CenterArc((0, 0), 1.74625, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.2413, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.15875
        extrude(amount=-0.15875)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -0.15875), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.5296359925, perimeter: 4.5084996172
            with BuildLine():
                CenterArc((0, 0), 0.47625, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.2413, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.635
        extrude(amount=0.635, mode=Mode.ADD)
    return part.part


# Description: This is a dumbbell weight featuring two rounded cylindrical heads connected by a narrow grip handle in the middle, with a symmetrical design for balanced weight distribution during exercise.
def model_22433_9f17ac4c_0003():
    """Model: Master Rod"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 12 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.816173205, perimeter: 7.6277869629
            with BuildLine():
                CenterArc((0, 0), 0.714, 42.8785276146, 274.2429447709)
                CenterArc((0, 0), 0.714, -42.8785276146, 85.7570552291)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.468705989, perimeter: 5.1365039886
            with BuildLine():
                CenterArc((0, 0), 0.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.3175, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=0.159
        extrude(amount=0.159, both=True)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 12 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.5566708353, perimeter: 6.1427769867
            with BuildLine():
                CenterArc((3.017, 0), 0.437, 134.8480472816, 90.3039054368)
                Line((0.5232177412, 0.4858386515), (2.7088149286, 0.309824082))
                CenterArc((0, 0), 0.714, -42.8785276146, 85.7570552291)
                Line((0.5232177412, -0.4858386515), (2.7088149286, -0.309824082))
            make_face()
        # Symmetric extrude, each_side=0.12
        extrude(amount=0.12, both=True, mode=Mode.ADD)

        # Sketch1 -> Extrude3 (Join)
        # Sketch on XZ construction plane
        # Sketch has 12 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.3657410322, perimeter: 4.4613033692
            with BuildLine():
                CenterArc((3.017, 0), 0.437, 134.8480472816, 90.3039054368)
                CenterArc((3.017, 0), 0.437, -134.8480472816, 269.6960945632)
            make_face()
            with BuildLine():
                CenterArc((3.017, 0), 0.2730384838, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.1085420691, perimeter: 2.9721884514
            with BuildLine():
                CenterArc((3.017, 0), 0.2730384838, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((3.017, 0), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=0.4365
        extrude(amount=0.4365, both=True, mode=Mode.ADD)
    return part.part


# Description: This is a suppressor or muzzle device featuring an elongated cylindrical body with a tapered end, equipped with mounting tabs or fins at the base for attachment to a firearm barrel.
def model_22447_4062c6cb_0007():
    """Model: Flap Final v1(1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.08, perimeter: 1.8
            with BuildLine():
                Line((1.7, -0.8), (1.8, -0.8))
                Line((1.8, -0.8), (1.8, 0))
                Line((1.7, 0), (1.8, 0))
                Line((1.7, 0), (1.7, -0.8))
            make_face()
            # Profile area: 0.3611374861, perimeter: 4.5240738419
            with BuildLine():
                Line((1.7, 0), (1.8, 0))
                Line((1.8, 0), (1.8, 0.1))
                CenterArc((0.85, -0.6197266304), 1.19185, 37.1478232543, 105.7043534915)
                Line((-0.1, 0), (-0.1, 0.1))
                Line((0, 0), (-0.1, 0))
                CenterArc((0.85, -0.741845833), 1.1282, 41.1131484514, 97.7737030971)
            make_face()
            # Profile area: 0.08, perimeter: 1.8
            with BuildLine():
                Line((0, 0), (-0.1, 0))
                Line((-0.1, 0), (-0.1, -0.8))
                Line((-0.1, -0.8), (0, -0.8))
                Line((0, -0.8), (0, 0))
            make_face()
        # OneSide extrude, distance=8.5
        extrude(amount=8.5)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 16 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(-0.1, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.0085840735, perimeter: 0.7141592654
            with BuildLine():
                CenterArc((0.6, 0.2), 0.2, -90, 90)
                Line((0.6, 0), (0.8, 0))
                Line((0.8, 0), (0.8, 0.2))
            make_face()
            # Profile area: 2.7728988012, perimeter: 15.7205151698
            with BuildLine():
                CenterArc((-0.0307754372, 0.6243406413), 0.8762, 18.5300130635, 40.4853137153)
                Line((0.8, 0.9027982019), (0.8, 8.5))
                Line((0.8, 8.5), (0.4203, 8.5))
                Line((0.4203, 8.5), (0.4203, 1.375511321))
            make_face()
            # Profile area: 2.9600948951, perimeter: 14.9878423467
            with BuildLine():
                CenterArc((-0.0307754372, 0.6243406413), 0.8762, 59.0153267788, 28.971816087)
                Line((0.4203, 8.5), (0.4203, 1.375511321))
                Line((0.4203, 8.5), (0, 8.5))
                Line((0, 8.5), (0, 2.3762))
                Line((0, 2.3762), (0, 1.5))
            make_face()
            # Profile area: 0.0241063779, perimeter: 0.6255014613
            with BuildLine():
                CenterArc((0.4203, 0.7014688819), 0.175, -90, 90.2004056281)
                Line((0.4203, 0.7014688819), (0.5952989295, 0.7020809848))
                Line((0.4203, 0.7014688819), (0.4203, 0.5264688819))
            make_face()
            # Profile area: 0.0239992596, perimeter: 0.624277253
            with BuildLine():
                Line((0.4203, 0.8764688819), (0.4203, 0.7014688819))
                Line((0.4203, 0.7014688819), (0.5952989295, 0.7020809848))
                CenterArc((0.4203, 0.7014688819), 0.175, 0.2004056281, 89.7995943719)
            make_face()
            # Profile area: 0.0241063779, perimeter: 0.6255014613
            with BuildLine():
                Line((0.2453010705, 0.700856779), (0.4203, 0.7014688819))
                Line((0.4203, 0.8764688819), (0.4203, 0.7014688819))
                CenterArc((0.4203, 0.7014688819), 0.175, 90, 90.2004056281)
            make_face()
            # Profile area: 0.0239992596, perimeter: 0.624277253
            with BuildLine():
                CenterArc((0.4203, 0.7014688819), 0.175, -179.7995943719, 89.7995943719)
                Line((0.4203, 0.7014688819), (0.4203, 0.5264688819))
                Line((0.2453010705, 0.700856779), (0.4203, 0.7014688819))
            make_face()
        # OneSide extrude, distance=-2.1
        extrude(amount=-2.1, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical pin or bolt with a rounded head at the top and a smooth shaft, designed for fastening or alignment purposes.
def model_22447_4062c6cb_0009():
    """Model: Rivet Final v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.096211275, perimeter: 1.0995574288
            Circle(0.175)
        # OneSide extrude, distance=1.9
        extrude(amount=1.9)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.9, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1621079481, perimeter: 2.9012608156
            with BuildLine():
                CenterArc((0, 0), 0.28675, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.175, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.096211275, perimeter: 1.0995574288
            Circle(0.175)
        # OneSide extrude, distance=0.05
        extrude(amount=0.05, mode=Mode.ADD)
    return part.part


# Description: This is a composite structural bracket or connector featuring an irregular hexagonal/polygonal base shape with multiple internal slots, cutouts, and triangulated reinforcement ribs throughout its body for weight reduction and structural support.
def model_22454_f707c2e5_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch16 -> Extrude22 (NewBody)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY) as sk:
            # Profile area: 0.5286164886, perimeter: 5.5046919206
            with BuildLine():
                Line((-0.2554499193, 7.1493728181), (-0.7582499779, 7.1493728181))
                Line((-0.2554499193, 6.9807727953), (-0.2554499193, 7.1493728181))
                Line((-0.2734499856, 7.1001727601), (-0.2554499193, 6.9807727953))
                Line((-0.7582499779, 7.1001727601), (-0.2734499856, 7.1001727601))
                Line((-0.7582499779, 6.8613727709), (-0.7582499779, 7.1001727601))
                Line((-0.0022499248, 6.8613727709), (-0.7582499779, 6.8613727709))
                Line((-0.0022499248, 7.34137279), (-0.0022499248, 6.8613727709))
                Line((-0.5062499627, 7.34137279), (-0.0022499248, 7.34137279))
                Line((-0.5062499627, 7.5093727728), (-0.5062499627, 7.34137279))
                Line((-0.488249956, 7.3893727681), (-0.5062499627, 7.5093727728))
                Line((-0.0022499248, 7.3893727681), (-0.488249956, 7.3893727681))
                Line((-0.0022499248, 7.6281728169), (-0.0022499248, 7.3893727681))
                Line((-0.7582499779, 7.6281728169), (-0.0022499248, 7.6281728169))
                Line((-0.7582499779, 7.1493728181), (-0.7582499779, 7.6281728169))
            make_face()
            # Profile area: 0.4306715951, perimeter: 4.1542305441
            with BuildLine():
                Line((0.3349501208, 7.6281728169), (0.4261501149, 7.1193727871))
                Line((0.0517500952, 7.6281728169), (0.3349501208, 7.6281728169))
                Line((0.1885500864, 6.8613727709), (0.0517500952, 7.6281728169))
                Line((0.6997500972, 6.8613727709), (0.1885500864, 6.8613727709))
                Line((0.8281500653, 7.6281728169), (0.6997500972, 6.8613727709))
                Line((0.5449501589, 7.6281728169), (0.8281500653, 7.6281728169))
                Line((0.4537501649, 7.1193727871), (0.5449501589, 7.6281728169))
                Line((0.5725500897, 7.1013727805), (0.4537501649, 7.1193727871))
                Line((0.3169501141, 7.1013727805), (0.5725500897, 7.1013727805))
                Line((0.4261501149, 7.1193727871), (0.3169501141, 7.1013727805))
            make_face()
        # TwoSides offset extrude, full=1.3, trim=0.8
        extrude(amount=1.3)
        extrude(sk.sketch, amount=0.8, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a fastener consisting of a long cylindrical shaft with a hexagonal head at the base, designed for threaded assembly with a corresponding nut or threaded hole.
def model_22457_a6c2776f_0006():
    """Model: 9:1 Gear Bolt v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.4635829324, perimeter: 4.5033320997
            with BuildLine():
                Line((0.6915280867, -0.291757157), (0.5984331531, 0.453002312))
                Line((0.5984331531, 0.453002312), (-0.0930949336, 0.744759469))
                Line((-0.0930949336, 0.744759469), (-0.6915280867, 0.291757157))
                Line((-0.6915280867, 0.291757157), (-0.5984331531, -0.453002312))
                Line((-0.5984331531, -0.453002312), (0.0930949336, -0.744759469))
                Line((0.0930949336, -0.744759469), (0.6915280867, -0.291757157))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            Circle(0.4)
        # OneSide extrude, distance=4
        extrude(amount=4, mode=Mode.ADD)
    return part.part


# Description: This is a hexagonal or octagonal box-like enclosure with a faceted geometric design featuring triangular and rectangular faces, internal ribbing or reinforcement structures, and multiple openings or cutouts on its sides.
def model_22457_a6c2776f_0008():
    """Model: Nut v1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.2470765814, perimeter: 4.1569219382
            with BuildLine():
                Line((0.6, -0.3464101615), (0.6, 0.3464101615))
                Line((0.6, 0.3464101615), (0, 0.692820323))
                Line((0, 0.692820323), (-0.6, 0.3464101615))
                Line((-0.6, 0.3464101615), (-0.6, -0.3464101615))
                Line((-0.6, -0.3464101615), (0, -0.692820323))
                Line((0, -0.692820323), (0.6, -0.3464101615))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            Circle(0.4)
        # OneSide extrude, distance=-1.2
        extrude(amount=-1.2, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical rod or pin with tapered ends, featuring a slightly rounded or beveled tip at one end and a uniform cylindrical shaft along its length.
def model_22524_0be3da8a_0012():
    """Model: Rotary Valve v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0812091841, perimeter: 1.1372989397
            with BuildLine():
                Line((0, -0.23876), (0, 0.16764))
                Line((0, 0.16764), (-0.1700093174, 0.16764))
                CenterArc((0, 0), 0.23876, 135.4020433385, 134.5979566615)
            make_face()
            # Profile area: 0.0166723232, perimeter: 0.7184127141
            with BuildLine():
                Line((0, 0.16764), (-0.1700093174, 0.16764))
                Line((0, 0.16764), (0.1700093174, 0.16764))
                CenterArc((0, 0), 0.23876, 44.5979566615, 90.804086677)
            make_face()
            # Profile area: 0.0812091841, perimeter: 1.1372989397
            with BuildLine():
                CenterArc((0, 0), 0.23876, -90, 134.5979566615)
                Line((0, 0.16764), (0.1700093174, 0.16764))
                Line((0, -0.23876), (0, 0.16764))
            make_face()
        # OneSide extrude, distance=9.8425
        extrude(amount=9.8425)

        # Sketch1 -> Extrude2 (Cut)
        # Sketch on XY construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.0166723232, perimeter: 0.7184127141
            with BuildLine():
                Line((0, 0.16764), (-0.1700093174, 0.16764))
                Line((0, 0.16764), (0.1700093174, 0.16764))
                CenterArc((0, 0), 0.23876, 44.5979566615, 90.804086677)
            make_face()
        # OneSide extrude, distance=0.4572
        extrude(amount=0.4572, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a fastener or rivet consisting of a cylindrical shaft with an enlarged, flat circular head at the top, commonly used for joining materials together.
def model_22534_e899f645_0009():
    """Model: 1010 - Binder Screw v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.9698697842, perimeter: 3.4910948363
            Circle(0.555625)
        # OneSide extrude, distance=-0.555625
        extrude(amount=-0.555625)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -0.555625, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.1829214, perimeter: 1.5161326146
            Circle(0.2413)
        # OneSide extrude, distance=1.190625
        extrude(amount=1.190625, mode=Mode.ADD)
    return part.part


# Description: This is a dumbbell consisting of two spherical weights connected by a cylindrical bar, designed for weightlifting and strength training exercises.
def model_22543_684108ff_0009():
    """Model: 5.2_Conrod v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.3328737328, perimeter: 3.6379642929
            with BuildLine():
                CenterArc((-1.4985, 0), 0.381, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((-1.4985, 0), 0.198, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.3328737328, perimeter: 3.6379642929
            with BuildLine():
                CenterArc((1.4985, 0), 0.381, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((1.4985, 0), 0.198, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.406
        extrude(amount=0.406)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on YZ construction plane
        # Sketch has 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.1231629984, perimeter: 1.2440706908
            with Locations((-0.203, 0)):
                Circle(0.198)
        # Symmetric extrude, each_side=-1.2
        extrude(amount=-1.2, both=True, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical battery or power cell with a protruding connector terminal at the top, featuring a smooth rounded body and a tapered antenna-like post extending upward.
def model_22606_f1813fe7_0000():
    """Model: Solar Motor v4"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1570700822, perimeter: 1.4049202347
            Circle(0.2236)
        # OneSide extrude, distance=1.2
        extrude(amount=1.2)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0078539816, perimeter: 0.3141592654
            Circle(0.05)
        # OneSide extrude, distance=0.6
        extrude(amount=0.6, mode=Mode.ADD)
    return part.part


# Description: This is a cricket bat with an elongated rectangular blade and a cylindrical handle, featuring a tapered grip section at the top.
def model_22608_c4bce8da_0000():
    """Model: Solar Motor v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0628128779, perimeter: 0.8884424024
            Circle(0.1414)
        # OneSide extrude, distance=1.2
        extrude(amount=1.2)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0078539816, perimeter: 0.3141592654
            Circle(0.05)
        # OneSide extrude, distance=0.6
        extrude(amount=0.6, mode=Mode.ADD)
    return part.part


# Description: A cylindrical housing or drum with a rounded top, featuring multiple rectangular mesh or perforated openings on its sides and a domed cap with ventilation slots.
def model_22624_7af10d7d_0001():
    """Model: cam v8"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 12 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.2135566587, perimeter: 2.3288973549
            with BuildLine():
                CenterArc((0, 0), 0.55, 65, 25)
                Line((0, 0.4), (0, 0.55))
                CenterArc((0, 0), 0.4, 0, 90)
                Line((0.4, 0), (0.85, 0))
                CenterArc((0, 0), 0.85, 0, 7.5789703928)
                CenterArc((0.6443216106, 0.0857301703), 0.2, 7.5789703928, 57.4210296072)
                Line((0.232440044, 0.4984692829), (0.728845263, 0.2669917277))
            make_face()
            # Profile area: 1.0971295925, perimeter: 6.2558881718
            with BuildLine():
                CenterArc((0, 0), 0.55, 90, 25)
                Line((-0.232440044, 0.4984692829), (-0.728845263, 0.2669917277))
                CenterArc((-0.6443216106, 0.0857301703), 0.2, 115, 57.4210296072)
                CenterArc((0, 0), 0.85, 172.4210296072, 187.5789703928)
                Line((0.4, 0), (0.85, 0))
                CenterArc((0, 0), 0.4, 90, 270)
                Line((0, 0.4), (0, 0.55))
            make_face()
        # OneSide extrude, distance=0.6
        extrude(amount=0.6)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.6), x_dir=(1, 0, 0), z_dir=(0, 0, 1))) as sk:
            # Profile area: 0.3632466506, perimeter: 5.8119464091
            with BuildLine():
                CenterArc((0, 0), 0.525, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # TwoSides extrude, along=0.35, against=-0.95
        extrude(amount=0.35, mode=Mode.ADD)
        extrude(sk.sketch, amount=-0.95, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical rod or shaft with a simple, elongated tubular shape and rounded ends, featuring no additional holes, slots, or flanges.
def model_22624_7af10d7d_0004():
    """Model: shaft v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            Circle(0.4)
        # OneSide extrude, distance=9
        extrude(amount=9)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 9, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2827433388, perimeter: 1.8849555922
            Circle(0.3)
        # OneSide extrude, distance=0.6
        extrude(amount=0.6, mode=Mode.ADD)
    return part.part


# Description: This is a curved structural bracket or support frame with a boomerang-like shape, featuring multiple mounting flanges, internal ribbing for reinforcement, and strategically placed holes for fastening and assembly.
def model_22645_1ba0af00_0006():
    """Model: Brake Calliper v4"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 5 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 73.5245088196, perimeter: 38.4472071976
            with BuildLine():
                Line((-5.1, 5), (-7.383775871, 1.3956059079))
                Line((-7.383775871, 1.3956059079), (-5.742, -1.9))
                CenterArc((0.0115609608, -9.6614026509), 9.6614095679, 53.4503016897, 73.0993966206)
                Line((7.4068977926, 1.3956059079), (5.7651219215, -1.9))
                Line((5.1231219215, 5), (7.4068977926, 1.3956059079))
                Line((-5.1, 5), (5.1231219215, 5))
            make_face()
        # Symmetric extrude, each_side=3.45
        extrude(amount=3.45, both=True)

        # Sketch3 -> Extrude2 (Cut)
        # Sketch on YZ construction plane
        # Sketch has 7 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 21.03772, perimeter: 18.3626
            with BuildLine():
                Line((1.95, -1.9), (1.95, 2.8813))
                Line((1.95, 2.8813), (-2.45, 2.8813))
                Line((-2.45, -1.9), (-2.45, 2.8813))
                Line((-2.45, -1.9), (1.95, -1.9))
            make_face()
        # Symmetric extrude, each_side=8.5
        extrude(amount=8.5, both=True, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical spacer or sleeve with a hollow center bore and a rectangular slot cut through the side of the tube.
def model_22666_bdaa1303_0009():
    """Model: FrontBearing v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.395865218, perimeter: 4.9872783376
            with BuildLine():
                CenterArc((0, 0), 0.47625, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.3175, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-1.52146
        extrude(amount=-1.52146)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -1.52146), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.0255861287, perimeter: 0.6470017406
            with BuildLine():
                Line((0.3072533969, 0.08001), (0.4694810565, 0.08001))
                CenterArc((0, 0), 0.3175, -14.5958935002, 29.1917870004)
                Line((0.4694810565, -0.08001), (0.3072533969, -0.08001))
                CenterArc((0, 0), 0.47625, -9.6715551421, 19.3431102842)
            make_face()
            # Profile area: 0.0255861287, perimeter: 0.6470017406
            with BuildLine():
                CenterArc((0, 0), 0.47625, 170.3284448579, 19.3431102842)
                Line((-0.3072533969, -0.08001), (-0.4694810565, -0.08001))
                CenterArc((0, 0), 0.3175, 165.4041064998, 29.1917870004)
                Line((-0.4694810565, 0.08001), (-0.3072533969, 0.08001))
            make_face()
        # OneSide extrude, distance=-0.0127
        extrude(amount=-0.0127, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical component with a rounded/domed top end and a flat circular base, featuring a hollow or recessed cavity on the upper surface, commonly used as a bearing housing, connector body, or sealed container.
def model_22666_bdaa1303_0018():
    """Model: ContraPiston v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.7125573925, perimeter: 2.9923670025
            Circle(0.47625)
        # OneSide extrude, distance=-0.635
        extrude(amount=-0.635)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, -0.635), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 0.5996173625, perimeter: 2.744997997
            Circle(0.43688)
        # OneSide extrude, distance=-0.51562
        extrude(amount=-0.51562, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a rivet or fastener featuring a cylindrical shaft with a enlarged domed or mushroom-shaped head, commonly used for permanent mechanical assembly by deformation.
def model_22670_9353c710_0000():
    """Model: P16-Crankrod Bolt 1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((8.0000001192, 0)):
                Circle(0.25)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.1), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((-8.0000001192, 0)):
                Circle(0.15)
        # OneSide extrude, distance=0.65
        extrude(amount=0.65, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical fastener or rivet with a larger hemispherical or dome-shaped head on one end and a tapered or slightly reduced shaft on the opposite end, featuring a smooth cylindrical body.
def model_22670_9353c710_0001():
    """Model: P17-Crankrod Bolt 2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((9.0000001341, 0)):
                Circle(0.2)
        # OneSide extrude, distance=0.15
        extrude(amount=0.15)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.15), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((-9.0000001341, 0)):
                Circle(0.15)
        # OneSide extrude, distance=0.6
        extrude(amount=0.6, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical housing or manifold block with a curved body, featuring multiple drilled holes on its sides and a rectangular slot or opening at the top, designed for fluid or component integration.
def model_22711_33843a5d_0006():
    """Model: Drag Plate v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 4 constraints, 7 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 49.1321014759, perimeter: 40.4940678676
            with BuildLine():
                Line((-3.3, 1.4), (-3.3, -7.0163514831))
                CenterArc((0, 4), 11.5, -106.6758348513, 33.3516697027)
                Line((3.3, 1.4), (3.3, -7.0163514831))
                Line((-3.3, 1.4), (3.3, 1.4))
            make_face()
            with BuildLine():
                CenterArc((0, -4), 1.65, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=3
        extrude(amount=3)

        # Sketch2 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(-1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 7.3513268094, perimeter: 24.504422698
            with BuildLine():
                CenterArc((0, -4), 2.25, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, -4), 1.65, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 8.5529859994, perimeter: 10.3672557568
            with Locations((0, -4)):
                Circle(1.65)
        # OneSide extrude, distance=-1.3
        extrude(amount=-1.3, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a hexagonal prism or block with a triangular wedge or angled cut removed from one corner, creating an asymmetrical geometry with both flat faces and angled surfaces.
def model_22719_67a50d6f_0005():
    """Model: Eccentric Rod"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.36, perimeter: 2.4
            with BuildLine():
                Line((0.3, -0.3), (0.3, 0.3))
                Line((0.3, 0.3), (-0.3, 0.3))
                Line((-0.3, 0.3), (-0.3, -0.3))
                Line((-0.3, -0.3), (0.3, -0.3))
            make_face()
        # OneSide extrude, distance=0.9
        extrude(amount=0.9)
    return part.part


# Description: This is a bracket or mounting arm with an angular L-shaped design, featuring a curved vertical flange on the left, a horizontal body extending to the right, and multiple slot openings or cutouts along its length for fastening or alignment purposes.
def model_22719_67a50d6f_0008():
    """Model: P35-Reverse Gear Link Lever"""
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
        # OneSide extrude, distance=0.8
        extrude(amount=0.8)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.8213472863, perimeter: 5.0680456106
            with BuildLine():
                CenterArc((0, 0), 0.3, -85.0679527961, 170.1359055922)
                Line((0.0257922584, -0.2988892092), (1.8086002418, -0.1996911195))
                CenterArc((1.7974891307, 0), 0.2, -86.8152614633, 173.6305229266)
                Line((1.8086002418, 0.1996911195), (0.0257922584, 0.2988892092))
            make_face()
        # OneSide extrude, distance=-0.4
        extrude(amount=-0.4, mode=Mode.ADD)
    return part.part


# Description: This is a mounting bracket or support plate with a rectangular base plate and a cylindrical pivot pin or post protruding from its left side, designed for articulated or rotational assembly.
def model_22742_3c107495_0015():
    """Model: Exterior Shovel v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0530205405, perimeter: 1.3352793916
            with BuildLine():
                Line((1.2649110641, 0.3), (1.2, 0.3))
                Line((1.2, 0.3), (1.2, -0.3))
                Line((1.2, -0.3), (1.2649110641, -0.3))
                CenterArc((0, 0), 1.3, -13.3423637971, 26.6847275942)
            make_face()
            # Profile area: 2.1146783905, perimeter: 14.5756910712
            with BuildLine():
                CenterArc((0, 0), 1.3, 13.3423637971, 333.3152724058)
                Line((1.2, -0.3), (1.2649110641, -0.3))
                Line((1.2, 0.3), (1.2, -0.3))
                Line((1.2649110641, 0.3), (1.2, 0.3))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 6.0013157496, perimeter: 22.9322722155
            with BuildLine():
                CenterArc((0, 0), 1.3, -13.3423637971, 26.6847275942)
                Line((1.2649110641, -0.3), (11.5, -0.3))
                Line((11.5, -0.3), (11.5, 0.3))
                Line((11.5, 0.3), (1.2649110641, 0.3))
            make_face()
            with BuildLine():
                CenterArc((6.5, 0), 0.200000003, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=4
        extrude(amount=4, mode=Mode.ADD)

        # Sketch2 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.3), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.8, perimeter: 4.8
            with BuildLine():
                Line((7.8, 1.8), (7.8, 2.2))
                Line((7.8, 2.2), (5.8, 2.2))
                Line((5.8, 2.2), (5.8, 1.8))
                Line((5.8, 1.8), (7.8, 1.8))
            make_face()
        # OneSide extrude, distance=-2.3808
        extrude(amount=-2.3808, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a simple L-shaped angle bracket or corner brace featuring two perpendicular flanges that meet at a right angle, with one flange extending horizontally and the other angled downward.
def model_22751_90a6225a_0001():
    """Model: Barra L v6"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 7 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 74, perimeter: 150
            with BuildLine():
                Line((0, 0), (0, 25))
                Line((0, 0), (1, 0))
                Line((1, 0), (1, 24))
                Line((1, 24), (50, 24))
                Line((50, 25), (50, 24))
                Line((0, 25), (50, 25))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch3 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.5), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1.3799606076, perimeter: 4.4252509462
            with BuildLine():
                Line((-1, -23.9409830056), (-1, -24))
                Line((-1, -24), (-1.0590169944, -24))
                CenterArc((-0.5, -24.5), 0.75, 138.1896851042, 83.6206297916)
                Line((-1.0590169944, -25), (0, -25))
                Line((0, -25), (0, -23.9409830056))
                CenterArc((-0.5, -24.5), 0.75, 48.1896851042, 83.6206297916)
            make_face()
            # Profile area: 0.3853790969, perimeter: 4.5577342397
            with BuildLine():
                Line((0, -25), (0, -23.9409830056))
                Line((-1.0590169944, -25), (0, -25))
                CenterArc((-0.5, -24.5), 0.75, -138.1896851042, 186.3793702084)
            make_face()
            # Profile area: 0.0018061631, perimeter: 0.2015397495
            with BuildLine():
                CenterArc((-0.5, -24.5), 0.75, 131.8103148958, 6.3793702084)
                Line((-1, -24), (-1.0590169944, -24))
                Line((-1, -23.9409830056), (-1, -24))
            make_face()
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.ADD)
    return part.part


# Description: This is a knife sheath or blade cover with an elongated tapered body, a small attachment loop or hole at the top, and a curved, pointed tip designed to accommodate and protect a blade.
def model_22756_fc3fdda5_0020():
    """Model: Insert 9"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 6 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 8.4532755554, perimeter: 19.2839199302
            with BuildLine():
                Line((2.0462366891, -0.078968698), (3.9699999113, -0.1299999971))
                Line((3.9699999113, -0.1299999971), (3.9699999113, 0.9855000029))
                Line((3.9699999113, 0.9855000029), (2.7000000402, 0.9855000029))
                Line((2.7000000402, 0.9855000029), (2.7000000402, 1.2839461225))
                CenterArc((1.3589552128, -28.9998259121), 30.313449983, 87.4644491555, 10.5167284169)
                Line((-2.8499999363, 1.0199999772), (-3.6609043126, 0.8952082187))
                CenterArc((-3.5765118811, 0.4800879725), 0.4236117342, 101.4914197341, 69.0362947)
                Line((-3.9943478053, 0.5498019725), (-3.9943478053, 0.204633705))
                Line((-3.9943478053, 0.204633705), (2.0495506985, 0.0539982135))
                Line((2.0495506985, 0.0539982135), (2.0462366891, -0.078968698))
            make_face()
            with BuildLine():
                CenterArc((3.3317163073, 0.4317163722), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.1585355817, perimeter: 2.331276148
            with BuildLine():
                Line((3.9699999113, -0.1299999971), (3.9699999113, 0.9855000029))
                CenterArc((3.3243213803, 0.4277500029), 0.8532208552, -40.8211084407, 81.6422168815)
            make_face()
        # OneSide extrude, distance=0.15
        extrude(amount=0.15)
    return part.part


# Description: This is a blue and black personal watercraft (jet ski) featuring a streamlined hull design with an elevated seat area, integrated handlebars, and a tapered nose, designed for recreational water sports.
def model_22756_fc3fdda5_0030():
    """Model: Insert 3-flathead1"""
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
        # Sketch on XZ construction plane
        # Sketch has 6 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.155317947, perimeter: 11.9553197231
            with BuildLine():
                Line((-0.4699999895, -1.1954999982), (-2.4814496722, -1.1431574974))
                Line((-0.4699999895, -0.0799999982), (-0.4699999895, -1.1954999982))
                Line((-1.7002330329, -0.0799999982), (-0.4699999895, -0.0799999982))
                Line((-1.7002330329, 0.2144840921), (-1.7002330329, -0.0799999982))
                _nurbs_edge([(-2.7199999392, -0.5084382859), (-2.7181766017, -0.5086947602), (-2.7144277774, -0.50908655), (-2.7084981334, -0.5093107544), (-2.6999786685, -0.508882639), (-2.6883530143, -0.5071340658), (-2.6758830708, -0.5041690612), (-2.6628458407, -0.4999813098), (-2.6496633874, -0.4945655417), (-2.6367842368, -0.4879348949), (-2.6245905616, -0.4801352688), (-2.6132935511, -0.4712614944), (-2.6028375644, -0.4614712765), (-2.5930202826, -0.4509349198), (-2.5836178305, -0.4397814863), (-2.5744934578, -0.4280549692), (-2.5657486462, -0.415644923), (-2.5576947726, -0.4023246003), (-2.5507086368, -0.3878580124), (-2.5451200284, -0.3720890056), (-2.5410921891, -0.3550319184), (-2.5384889741, -0.3369772291), (-2.5369625095, -0.318387058), (-2.536064044, -0.2997702973), (-2.535351288, -0.2815580941), (-2.5344860237, -0.2639950548), (-2.5333640091, -0.2469837224), (-2.5320978218, -0.2301379083), (-2.5309140607, -0.2129559663), (-2.5300731116, -0.194964731), (-2.529787735, -0.1758593115), (-2.5301222595, -0.1556846226), (-2.5309773677, -0.1348440588), (-2.5321698232, -0.1139178893), (-2.5334853453, -0.0935359479), (-2.5347453186, -0.0742211968), (-2.5358608321, -0.0562620555), (-2.5369096586, -0.0395300541), (-2.5380889977, -0.0235972734), (-2.5396313552, -0.0079425713), (-2.5417307267, 0.0078662906), (-2.5444689515, 0.0239929145), (-2.5477299934, 0.0401180853), (-2.5512588019, 0.0556330082), (-2.554742797, 0.0698991139), (-2.5578810071, 0.0824666133), (-2.5604683068, 0.0933514449), (-2.5624420621, 0.1031574555), (-2.5638164017, 0.1127064665), (-2.5646373411, 0.1227812548), (-2.5649264107, 0.1337604331), (-2.5646460985, 0.1456396016), (-2.563670265, 0.1582172312), (-2.5617564588, 0.1712231662), (-2.5585085088, 0.1844847395), (-2.5534817638, 0.1978743453), (-2.5463128313, 0.2112331164), (-2.5368231762, 0.2243134703), (-2.5251757467, 0.2366880956), (-2.5118342502, 0.2477800034), (-2.4973679255, 0.2569870698), (-2.4822915918, 0.2637845575), (-2.4669105739, 0.2678259975), (-2.4511147369, 0.2690718513), (-2.4344467423, 0.2677661657), (-2.4163025006, 0.2643387688), (-2.3960963657, 0.2593291973), (-2.3734261018, 0.2533061031), (-2.3482740804, 0.2467779655), (-2.3210659312, 0.2401452196), (-2.2925017581, 0.2337200689), (-2.2634418693, 0.2277301335), (-2.2347697985, 0.2223285405), (-2.2072670478, 0.2176012463), (-2.1814781902, 0.2135753839), (-2.1575906764, 0.2102273833), (-2.1352797304, 0.2074904458), (-2.1138451152, 0.2052692679), (-2.0923994879, 0.2034562417), (-2.0700351803, 0.2019467786), (-2.046007594, 0.2006557711), (-2.0198938971, 0.199531785), (-1.9918056166, 0.1985766207), (-1.9624264527, 0.1978471737), (-1.9327805831, 0.1974299222), (-1.9040640943, 0.1974218111), (-1.8774523627, 0.1979087261), (-1.8539149084, 0.1989446308), (-1.834033516, 0.2005312425), (-1.8178029681, 0.2025954282), (-1.8044843222, 0.2049733424), (-1.7929050252, 0.2074515026), (-1.7817243085, 0.2098035387), (-1.7697005118, 0.2118269711), (-1.7559866776, 0.213384174), (-1.7400821319, 0.2143937561), (-1.7254046422, 0.2147307021), (-1.7132605619, 0.2147126717), (-1.704659679, 0.2145803374), (-1.7002330329, 0.2144840921)], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0.0105263158, 0.0210526316, 0.0315789474, 0.0421052632, 0.0526315789, 0.0631578947, 0.0736842105, 0.0842105263, 0.0947368421, 0.1052631579, 0.1157894737, 0.1263157895, 0.1368421053, 0.1473684211, 0.1578947368, 0.1684210526, 0.1789473684, 0.1894736842, 0.2, 0.2105263158, 0.2210526316, 0.2315789474, 0.2421052632, 0.2526315789, 0.2631578947, 0.2736842105, 0.2842105263, 0.2947368421, 0.3052631579, 0.3157894737, 0.3263157895, 0.3368421053, 0.3473684211, 0.3578947368, 0.3684210526, 0.3789473684, 0.3894736842, 0.4, 0.4105263158, 0.4210526316, 0.4315789474, 0.4421052632, 0.4526315789, 0.4631578947, 0.4736842105, 0.4842105263, 0.4947368421, 0.5052631579, 0.5157894737, 0.5263157895, 0.5368421053, 0.5473684211, 0.5578947368, 0.5684210526, 0.5789473684, 0.5894736842, 0.6, 0.6105263158, 0.6210526316, 0.6315789474, 0.6421052632, 0.6526315789, 0.6631578947, 0.6736842105, 0.6842105263, 0.6947368421, 0.7052631579, 0.7157894737, 0.7263157895, 0.7368421053, 0.7473684211, 0.7578947368, 0.7684210526, 0.7789473684, 0.7894736842, 0.8, 0.8105263158, 0.8210526316, 0.8315789474, 0.8421052632, 0.8526315789, 0.8631578947, 0.8736842105, 0.8842105263, 0.8947368421, 0.9052631579, 0.9157894737, 0.9263157895, 0.9368421053, 0.9473684211, 0.9578947368, 0.9684210526, 0.9789473684, 0.9894736842, 1, 1, 1, 1, 1, 1], 5)
                Line((-3.8000000566, -0.5084382859), (-2.7199999392, -0.5084382859))
                Line((-4.5631803506, -0.5699999873), (-3.8000000566, -0.5084382859))
                Line((-4.5631803506, -0.8469435815), (-4.5631803506, -0.5699999873))
                Line((-3.8000000566, -0.9099999797), (-4.5631803506, -0.8469435815))
                Line((-2.6099999417, -0.9099999797), (-3.8000000566, -0.9099999797))
                Line((-2.4814496722, -1.1431574974), (-2.6099999417, -0.9099999797))
            make_face()
            with BuildLine():
                CenterArc((-1.1044052769, -0.6351155255), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.1653779953, perimeter: 2.33941854
            with BuildLine():
                CenterArc((-1.0819803818, -0.6377499982), 0.8280127192, -42.3455855129, 84.6911710258)
                Line((-0.4699999895, -0.0799999982), (-0.4699999895, -1.1954999982))
            make_face()
        # OneSide extrude, distance=0.15
        extrude(amount=0.15)

        # Sketch3 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.9099999797), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.1882598909, perimeter: 3.7063786186
            with BuildLine():
                Line((-3.8000000566, 0.2500000037), (-4.6500000693, 0.2500000037))
                Line((-4.6500000693, 0.2500000037), (-4.6500000693, -0.0500000007))
                Line((-4.6500000693, -0.0500000007), (-3.8000000566, -0.0500000007))
                Line((-3.8000000566, -0.0500000007), (-3.8000000566, 0))
                Line((-4.5631803506, 0.06255), (-3.8000000566, 0))
                Line((-4.5631803506, 0.06255), (-4.5631803506, 0.08745))
                Line((-4.5631803506, 0.08745), (-3.8000000566, 0.15))
                Line((-3.8000000566, 0.15), (-3.8000000566, 0.2500000037))
            make_face()
        # OneSide extrude, distance=-0.65
        extrude(amount=-0.65, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a skateboard or longboard deck featuring an elongated tapered shape with two mounting holes at each end, a concave curved profile along its length, and decorative geometric line patterns on its dark surface.
def model_22756_fc3fdda5_0031():
    """Model: Black Insert"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 11 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 2.1965818891, perimeter: 6.6568167191
            with BuildLine():
                CenterArc((-7.3138124054, 0.989287826), 0.8597146067, 8.4942557125, 170.535151129)
                CenterArc((-7.3138124054, 0.989287826), 0.8597146067, 179.0294068415, 184.4223721987)
                CenterArc((43.3797034897, 6.2932551306), 50.1113645958, -174.0702232377, 0.0864812282)
            make_face()
            with BuildLine():
                CenterArc((-7.3138124054, 0.989287826), 0.1997545641, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 9.9820948166, perimeter: 21.1242581726
            with BuildLine():
                CenterArc((43.3797034897, 6.2932551306), 50.1113645958, 176.824512901, 9.1052638613)
                CenterArc((-7.312820753, 9.1124175168), 0.6595242851, 177.6375226381, 178.6001443713)
                CenterArc((101.2839830961, 1.5531221693), 109.5188451934, 176.0278820563, 0.7860708627)
                Line((-8.1499998178, 7.6399998292), (-8.0655819366, 7.6399998292))
                Line((-8.2476485978, 4.9354907633), (-8.1499998178, 7.6399998292))
                CenterArc((-9.2872010691, 3.9262605274), 1.4488668019, -45.6613494355, 89.8134267783)
                Line((-8.2745910775, 1.7791452496), (-8.2745910775, 2.8899999354))
                Line((-8.1799998172, 1.7799999602), (-8.2745910775, 1.7791452496))
                Line((-8.173403661, 1.0500000156), (-8.1799998172, 1.7799999602))
                Line((-8.173403661, 1.0038507348), (-8.173403661, 1.0500000156))
                CenterArc((-7.3138124054, 0.989287826), 0.8597146067, 8.4942557125, 170.535151129)
            make_face()
            # Profile area: 1.2429537254, perimeter: 5.3899471047
            with BuildLine():
                CenterArc((-7.312820753, 9.1124175168), 0.6595242851, 177.6375226381, 178.6001443713)
                CenterArc((-7.312820753, 9.1124175168), 0.6595242851, -3.7623329907, 181.3998556287)
            make_face()
            with BuildLine():
                CenterArc((-7.312820753, 9.1124175168), 0.1983124397, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0.1, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 3.1674870644, perimeter: 12.3214416723
            with BuildLine():
                Line((-8.1499998178, 7.6399998292), (-8.2476485978, 4.9354907633))
                CenterArc((-9.2872010691, 3.9262605274), 1.4488668019, -45.6613494355, 89.8134267783)
                Line((-8.2745910775, 2.8899999354), (-8.2745910775, 1.7791452496))
                CenterArc((-12.467859758, 4.8000382063), 5.1681037608, -35.7695376179, 69.1034310117)
            make_face()
        # OneSide extrude, distance=0.2698
        extrude(amount=0.2698, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical bushing or spacer with a central axial hole, featuring a smooth outer diameter and a geometric mesh pattern on the top surface that suggests a complex internal or decorative feature.
def model_22768_620b0a0b_0006():
    """Model: Handle Cap v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 2.0106192983, perimeter: 5.0265482457
            Circle(0.8)
        # Symmetric extrude, each_side=0.6
        extrude(amount=0.6, both=True)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.6), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            Circle(0.25)
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a curved, bent structural component with two rectangular box-like end sections connected by a curved middle section, featuring internal ribbing and what appears to be mounting flanges or reinforcement areas at each end.
def model_22772_2b5f6629_0003():
    """Model: Component8"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 13 constraints, 11 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 3.64, perimeter: 8
            with BuildLine():
                Line((14.4358464911, 2.6), (14.4358464911, 4))
                Line((17.0358464911, 2.6), (14.4358464911, 2.6))
                Line((17.0358464911, 4), (17.0358464911, 2.6))
                Line((17.0358464911, 4), (14.4358464911, 4))
            make_face()
            # Profile area: 22.7119050875, perimeter: 35.2455539669
            with BuildLine():
                Line((14.4358464911, 4), (6.0358464911, 4))
                Line((5.0378, 1.4), (6.0358464911, 4))
                Line((0, 1.4), (5.0378, 1.4))
                Line((0, 0), (0, 1.4))
                Line((0, 0), (6, 0))
                Line((6, 0), (6.9980464911, 2.6))
                Line((14.4358464911, 2.6), (6.9980464911, 2.6))
                Line((14.4358464911, 2.6), (14.4358464911, 4))
            make_face()
            # Profile area: 0.78, perimeter: 5.8
            with BuildLine():
                Line((17.0358464911, 2.6), (14.4358464911, 2.6))
                Line((14.4358464911, 2.3), (14.4358464911, 2.6))
                Line((17.0358464911, 2.3), (14.4358464911, 2.3))
                Line((17.0358464911, 2.6), (17.0358464911, 2.3))
            make_face()
            # Profile area: 0.78, perimeter: 5.8
            with BuildLine():
                Line((17.0358464911, 4), (14.4358464911, 4))
                Line((17.0358464911, 4.3), (17.0358464911, 4))
                Line((14.4358464911, 4.3), (17.0358464911, 4.3))
                Line((14.4358464911, 4), (14.4358464911, 4.3))
            make_face()
        # OneSide extrude, distance=4
        extrude(amount=4)

        # Sketch2 -> Extrude2 (Intersect)
        # Sketch on BRepFace
        # Sketch has 14 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 5.3092915846, perimeter: 8.1681408993
            with BuildLine():
                CenterArc((15.7358464911, 2), 1.3, 87.0896273259, 185.8207453482)
                CenterArc((15.7358464911, 2), 1.3, -87.0896273259, 174.1792546518)
            make_face()
            # Profile area: 27.5102121445, perimeter: 27.4384470195
            with BuildLine():
                Line((6, 0.2033572728), (6, 3.7966427272))
                Line((6, 0.2033572728), (15.8018523592, 0.7016767639))
                CenterArc((15.7358464911, 2), 1.3, 87.0896273259, 185.8207453482)
                Line((6, 3.7966427272), (15.8018523592, 3.2983232361))
            make_face()
            # Profile area: 8.9040842401, perimeter: 17.0742479922
            with BuildLine():
                Line((2.2028330232, 3.9896881074), (6, 3.7966427272))
                CenterArc((2, 2), 2, -84.1792546518, 168.3585093037)
                Line((2.2028330232, 0.0103118926), (6, 0.2033572728))
                Line((6, 0.2033572728), (6, 3.7966427272))
            make_face()
            # Profile area: 12.5656719758, perimeter: 12.5661958871
            with BuildLine():
                Line((2, 0), (2.2028330232, 0.0103118926))
                CenterArc((2, 2), 2, -84.1792546518, 168.3585093037)
                Line((2, 4), (2.2028330232, 3.9896881074))
                CenterArc((2, 2), 2, 90, 90)
                CenterArc((2, 2), 2, -180, 90)
            make_face()
        # OneSide extrude, distance=-6.5
        extrude(amount=-6.5, mode=Mode.INTERSECT)
    return part.part


# Description: This is a boat hull or marine vessel component with a trapezoidal box-like shape, featuring a sloped top surface with internal ribbing/bracing, dark side walls, and a flat bottom base designed for structural support and buoyancy.
def model_22787_49022c32_0007():
    """Model: Head v8 (16)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 21 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 52.7787624477, perimeter: 29.3898226701
            with BuildLine():
                CenterArc((4.28625, 2.06375), 0.635, 0, 90)
                Line((-4.28625, 2.69875), (4.28625, 2.69875))
                CenterArc((-4.28625, 2.06375), 0.635, 90, 90)
                Line((-4.92125, -2.06375), (-4.92125, 2.06375))
                CenterArc((-4.28625, -2.06375), 0.635, 180, 90)
                Line((4.28625, -2.69875), (-4.28625, -2.69875))
                CenterArc((4.28625, -2.06375), 0.635, -90, 90)
                Line((4.92125, 2.06375), (4.92125, -2.06375))
            make_face()
        # OneSide extrude, distance=2.2225
        extrude(amount=2.2225)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 15 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 57.7182705508, perimeter: 30.6598233186
            with BuildLine():
                CenterArc((4.4450001621, -2.2225), 0.635, -90, 90)
                Line((5.0800001621, 2.2225), (5.0800001621, -2.2225))
                CenterArc((4.4450001621, 2.2225), 0.635, 0, 90)
                Line((-4.4450001621, 2.8575), (4.4450001621, 2.8575))
                CenterArc((-4.4450001621, 2.2225), 0.635, 90, 90)
                Line((-5.0800001621, -2.2225), (-5.0800001621, 2.2225))
                CenterArc((-4.4450001621, -2.2225), 0.635, 180, 90)
                Line((4.4450001621, -2.8575), (-4.4450001621, -2.8575))
            make_face()
        # OneSide extrude, distance=0.3175
        extrude(amount=0.3175, mode=Mode.ADD)
    return part.part


# Description: This is a flat parallelogram-shaped plate or panel with a blue surface and dark edges, featuring a slight 3D perspective that suggests it has minimal thickness.
def model_22788_b6a9e30a_0001():
    """Model: DeskBack v4"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4785, perimeter: 284
            with BuildLine():
                Line((-43.5, 27.5), (43.5, 27.5))
                Line((-43.5, -27.5), (-43.5, 27.5))
                Line((43.5, -27.5), (-43.5, -27.5))
                Line((43.5, 27.5), (43.5, -27.5))
            make_face()
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 19.6349540849, perimeter: 15.7079632679
            with Locations((38.6637906628, -22.7728783271)):
                Circle(2.5)
        # OneSide extrude, distance=-30
        extrude(amount=-30, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a flat parallelogram or skewed rectangular plate with a uniform blue surface, featuring a dark beveled or chamfered edge along one side, and subtle diagonal line details across its face.
def model_22788_b6a9e30a_0008():
    """Model: Back 1 v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3217.5, perimeter: 227
            with BuildLine():
                Line((-29.25, 27.5), (29.25, 27.5))
                Line((-29.25, -27.5), (-29.25, 27.5))
                Line((29.25, -27.5), (-29.25, -27.5))
                Line((29.25, 27.5), (29.25, -27.5))
            make_face()
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)
    return part.part


# Description: This is a tapered cylindrical pin or stylus with a pointed tip, featuring a gradually narrowing conical shape from a thicker rounded end to a sharp point.
def model_22848_cc91b848_0005():
    """Model: Back of wine bottle bracket v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 220.816090625, perimeter: 218.1225
            with BuildLine():
                Line((-1.031875, 53.49875), (1.031875, 53.49875))
                Line((-1.031875, -53.49875), (-1.031875, 53.49875))
                Line((1.031875, -53.49875), (-1.031875, -53.49875))
                Line((1.031875, 53.49875), (1.031875, -53.49875))
            make_face()
        # OneSide extrude, distance=5.08
        extrude(amount=5.08)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 53.49875), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.4560367312, perimeter: 2.393893602
            with Locations((0, 3.8100000405)):
                Circle(0.381)
            # Profile area: 0.4560367312, perimeter: 2.393893602
            with Locations((0, 1.2700000405)):
                Circle(0.381)
        # OneSide extrude, distance=1.27
        extrude(amount=1.27, mode=Mode.ADD)
    return part.part


# Description: This is a stylus or pen with a tapered, cylindrical body that gradually narrows to a fine point at one end, featuring a smooth, streamlined design typical of touchscreen or writing instruments.
def model_22848_cc91b848_0008():
    """Model: Wine Base v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 475.6038875, perimeter: 222.885
            with BuildLine():
                Line((-2.2225, 53.49875), (2.2225, 53.49875))
                Line((-2.2225, -53.49875), (-2.2225, 53.49875))
                Line((2.2225, -53.49875), (-2.2225, -53.49875))
                Line((2.2225, 53.49875), (2.2225, -53.49875))
            make_face()
        # OneSide extrude, distance=2.9845
        extrude(amount=2.9845)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 53.49875), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.4560367312, perimeter: 2.393893602
            with Locations((0, 1.27)):
                Circle(0.381)
        # OneSide extrude, distance=1.27
        extrude(amount=1.27, mode=Mode.ADD)
    return part.part


# Description: This is a rectangular bar or rod with a long, slender cylindrical or prismatic shape, featuring a uniform cross-section and smooth surface with minimal features.
def model_22848_cc91b848_0030():
    """Model: Drawer Assembly v7"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 102.015925, perimeter: 163.195
            with BuildLine():
                Line((-0.635, 40.16375), (0.635, 40.16375))
                Line((-0.635, -40.16375), (-0.635, 40.16375))
                Line((0.635, -40.16375), (-0.635, -40.16375))
                Line((0.635, 40.16375), (0.635, -40.16375))
            make_face()
        # OneSide extrude, distance=7.62
        extrude(amount=7.62)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 40.16375), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0197932609, perimeter: 0.4987278338
            with Locations((0, 5.715)):
                Circle(0.079375)
            # Profile area: 0.0197932609, perimeter: 0.4987278338
            with Locations((0, 2.54)):
                Circle(0.079375)
        # OneSide extrude, distance=-0.635
        extrude(amount=-0.635, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical sleeve or bushing with an elongated tubular body featuring a mesh or perforated pattern on its outer surface and a hollow central passage, designed for use as a connector, filter, or structural component.
def model_22998_00817368_0005():
    """Model: aggancio v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 245.4369260617, perimeter: 64.2699081699
            with BuildLine():
                CenterArc((0, 0), 12.5, -90, 180)
                Line((0, 12.5), (0, -12.5))
            make_face()
        # OneSide extrude, distance=3.5
        extrude(amount=3.5)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 3.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 12.5663706144, perimeter: 12.5663706144
            with Locations((-6.94311, 0)):
                Circle(2)
        # OneSide extrude, distance=-16
        extrude(amount=-16, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a curved duct or channel component with an elongated, semi-circular cross-section featuring a mesh or perforated top surface and solid side walls, designed for airflow or material passage.
def model_22998_00817368_0006():
    """Model: sostegno_base v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 353.4291735289, perimeter: 77.1238898038
            with BuildLine():
                CenterArc((0, 0), 15, -90, 180)
                Line((0, 15), (0, -15))
            make_face()
        # OneSide extrude, distance=3.5
        extrude(amount=3.5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 3.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 265.4645792283, perimeter: 66.8407044967
            with BuildLine():
                CenterArc((0, 0), 13, 90, 180)
                Line((0, -13), (0, 13))
            make_face()
        # OneSide extrude, distance=3.5
        extrude(amount=3.5, mode=Mode.ADD)
    return part.part


# Description: This is a mesh or perforated cylindrical container/basket with an oval or elliptical shape, featuring a split or open side design with internal curved surfaces and multiple drainage or ventilation holes throughout its surface.
def model_23025_02ad81fe_0000():
    """Model: Piezas 4 v0 v0"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 10 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.3711221126, perimeter: 3.9117876291
            with BuildLine():
                Line((0.3354101966, 0.3), (-0.3354101966, 0.3))
                CenterArc((0, 0), 0.45, 138.1896851042, 83.6206297916)
                Line((-0.3354101966, -0.3), (0.3354101966, -0.3))
                CenterArc((0, 0), 0.45, -41.8103148958, 83.6206297916)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=0.1
        extrude(amount=0.1, both=True)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 10 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0696933468, perimeter: 1.4277821968
            with BuildLine():
                CenterArc((0, 0), 0.45, 41.8103148958, 96.3793702084)
                Line((0.3354101966, 0.3), (-0.3354101966, 0.3))
            make_face()
            # Profile area: 0.0696933468, perimeter: 1.4277821968
            with BuildLine():
                CenterArc((0, 0), 0.45, -138.1896851042, 96.3793702084)
                Line((-0.3354101966, -0.3), (0.3354101966, -0.3))
            make_face()
        # OneSide extrude, distance=-0.1
        extrude(amount=-0.1, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical sleeve or bushing with an elliptical or slot-shaped opening at the top and a curved, tapered wall structure featuring vertical ribbing or fluting along its exterior surface.
def model_23044_9a964a68_0006():
    """Model: PVC Cap 1.5in v9 (3)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 6.8912217157, perimeter: 27.1307941564
            with BuildLine():
                CenterArc((0, 0), 2.413, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.905, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=3.556
        extrude(amount=3.556)

        # Sketch3 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 11.4009182797, perimeter: 11.9694680102
            Circle(1.905)
        # OneSide extrude, distance=0.4318
        extrude(amount=0.4318, mode=Mode.ADD)
    return part.part


# Description: This is a flat, parallelogram-shaped plate or panel with a slightly beveled or chamfered edge along the top surface, featuring internal diagonal reinforcement lines or creases that divide the surface into triangular sections.
def model_23044_9a964a68_0009():
    """Model: Arduino Board v6"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 33.274, perimeter: 23.26
            with BuildLine():
                Line((0, 5.08), (0, 0))
                Line((0, 0), (6.55, 0))
                Line((6.55, 0), (6.55, 5.08))
                Line((6.55, 5.08), (0, 5.08))
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.875, perimeter: 7.7071067812
            with BuildLine():
                Line((6.55, 0.25), (6.8, 0.5))
                Line((6.8, 0.5), (6.8, 3.75))
                Line((6.8, 3.75), (6.55, 4))
                Line((6.55, 0.25), (6.55, 4))
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical roller or spacer with a solid, uniform circular cross-section and rounded end caps, featuring a fine mesh or textured surface pattern across its body.
def model_23049_207a41f0_0005():
    """Model: P3-Piston 2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 7.0685834706, perimeter: 9.4247779608
            Circle(1.5)
        # OneSide extrude, distance=8
        extrude(amount=8)
    return part.part


# Description: This is a cylindrical connector or coupling with a hexagonal base, featuring a hollow cylindrical body with a mesh-textured surface and a solid hexagonal mounting flange at one end.
def model_23049_207a41f0_0006():
    """Model: Bolt M10x18"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            Circle(0.5)
        # OneSide extrude, distance=1.8
        extrude(amount=1.8)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1.8), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.912011628, perimeter: 7.9913349148
            with BuildLine():
                Line((-0.7, 0.4041451884), (-0.7, -0.4041451884))
                Line((-0.7, -0.4041451884), (0, -0.8082903769))
                Line((0, -0.8082903769), (0.7, -0.4041451884))
                Line((0.7, -0.4041451884), (0.7, 0.4041451884))
                Line((0.7, 0.4041451884), (0, 0.8082903769))
                Line((0, 0.8082903769), (-0.7, 0.4041451884))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            Circle(0.5)
        # OneSide extrude, distance=0.3
        extrude(amount=0.3, mode=Mode.ADD)
    return part.part


# Description: This is a hex dumbbell with two cylindrical weights connected by a shorter hexagonal-shaped grip section in the middle, featuring knurled surfaces for improved grip.
def model_23104_3b70eba4_0003():
    """Model: P18-Hinge"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 17 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2420953398, perimeter: 3.6644363588
            with BuildLine():
                CenterArc((0, -1.4), 0.7, 44.4153085972, 45.5846914028)
                CenterArc((0, -1.4), 0.7, 90, 45.5846914028)
                Line((-0.5, -0.9101020514), (-0.5, -1.4))
                CenterArc((0, -1.4), 0.5, 0, 180)
                Line((0.5, -1.4), (0.5, -0.9101020514))
            make_face()
            # Profile area: 0.2420953398, perimeter: 3.6644363588
            with BuildLine():
                CenterArc((0, 0), 0.7, -90, 45.5846914028)
                Line((0.5, -0.4898979486), (0.5, 0))
                CenterArc((0, 0), 0.5, -180, 180)
                Line((-0.5, 0), (-0.5, -0.4898979486))
                CenterArc((0, 0), 0.7, -135.5846914028, 45.5846914028)
            make_face()
            # Profile area: 0.0652055785, perimeter: 1.5340482378
            with BuildLine():
                CenterArc((0, 0), 0.7, -135.5846914028, 45.5846914028)
                Line((-0.5, -0.4898979486), (-0.5, -0.9101020514))
                CenterArc((0, -1.4), 0.7, 90, 45.5846914028)
            make_face()
            # Profile area: 0.0652055785, perimeter: 1.5340482378
            with BuildLine():
                Line((0.5, -0.9101020514), (0.5, -0.4898979486))
                CenterArc((0, 0), 0.7, -90, 45.5846914028)
                CenterArc((0, -1.4), 0.7, 44.4153085972, 45.5846914028)
            make_face()
        # Symmetric extrude, each_side=0.1
        extrude(amount=0.1, both=True)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 17 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))) as sk:
            # Profile area: 0.5890486225, perimeter: 4.7123889804
            with BuildLine():
                CenterArc((0, -1.4), 0.5, 180, 180)
                CenterArc((0, -1.4), 0.5, 0, 180)
            make_face()
            with BuildLine():
                CenterArc((0, -1.4), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # TwoSides extrude, along=0.1, against=-0.3
        extrude(amount=0.1, mode=Mode.ADD)
        extrude(sk.sketch, amount=-0.3, mode=Mode.ADD)

        # Sketch1 -> Extrude3 (Join)
        # Sketch on XZ construction plane
        # Sketch has 17 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))) as sk:
            # Profile area: 0.5890486225, perimeter: 4.7123889804
            with BuildLine():
                CenterArc((0, 0), 0.5, 0, 180)
                CenterArc((0, 0), 0.5, -180, 180)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # TwoSides extrude, along=0.3, against=-0.1
        extrude(amount=0.3, mode=Mode.ADD)
        extrude(sk.sketch, amount=-0.1, mode=Mode.ADD)
    return part.part


# Description: This is a roller or pulley assembly featuring two large circular wheels with central holes connected by a central hub or bracket, creating an hourglass-shaped profile with geometric faceted surfaces.
def model_23132_1847c4ef_0002():
    """Model: link v5"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 7 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 53.2974654364, perimeter: 44.9745302452
            with BuildLine():
                CenterArc((0, 0), 2.7, 137.7945535963, 264.4108928075)
                Line((2, 1.8138357147), (2, 6.1861642853))
                CenterArc((0, 8), 2.7, -42.2054464037, 264.4108928075)
                Line((-2, 1.8138357147), (-2, 6.1861642853))
            make_face()
            with BuildLine():
                CenterArc((0, 8), 0.9, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((0, 0), 0.9, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 9 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 9.6, perimeter: 12.8
            with BuildLine():
                Line((0, 5.2), (-2, 5.2))
                Line((-2, 5.2), (-2, 2.8))
                Line((-2, 2.8), (2, 2.8))
                Line((2, 2.8), (2, 5.2))
                Line((2, 5.2), (0, 5.2))
            make_face()
        # OneSide extrude, distance=1.35
        extrude(amount=1.35, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical mesh filter or strainer basket with a curved, oval-shaped body featuring a fine perforated mesh surface on top and solid sidewalls, designed to retain particles while allowing fluid flow through the mesh.
def model_23132_1847c4ef_0006():
    """Model: Star grip v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 63.6172512352, perimeter: 28.2743338823
            Circle(4.5)
        # OneSide extrude, distance=2.5
        extrude(amount=2.5)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.3398735947, perimeter: 2.9959321297
            with BuildLine():
                CenterArc((5.1499435897, -0.0241044255), 1, 134.6477155028, 90.1682245712)
                CenterArc((0, 0), 4.5, -9.3221768969, 18.1080093707)
            make_face()
        # OneSide extrude, distance=-2.5
        extrude(amount=-2.5, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a toothed friction ring or drive ring with a toroidal (doughnut-like) shape featuring fine radial teeth or ridges on its inner and outer surfaces for high-friction engagement with mating components.
def model_23132_1847c4ef_0009():
    """Model: Handle v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 24.1274315796, perimeter: 60.3185789489
            with BuildLine():
                CenterArc((0, 0), 5.2, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 4.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # TwoSides extrude (symmetric), distance=1
        extrude(amount=1, both=True)
    return part.part


# Description: This is a polygonal bracket or connector piece with an irregular geometric form featuring multiple planar faces and internal triangulated surfaces, designed for structural support or assembly purposes.
def model_23137_e55b73cb_0013():
    """Model: Belt_Bracket v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 9.6774, perimeter: 12.7
            with BuildLine():
                Line((0, 3.81), (0, 0))
                Line((0, 0), (2.54, 0))
                Line((2.54, 0), (2.54, 3.81))
                Line((2.54, 3.81), (0, 3.81))
            make_face()
        # OneSide extrude, distance=0.3175
        extrude(amount=0.3175)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.3175), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1.209675, perimeter: 8.255
            with BuildLine():
                Line((0, -3.81), (0, 0))
                Line((0, 0), (-0.3175, 0))
                Line((-0.3175, 0), (-0.3175, -3.81))
                Line((-0.3175, -3.81), (0, -3.81))
            make_face()
        # OneSide extrude, distance=3.81
        extrude(amount=3.81, mode=Mode.ADD)
    return part.part


# Description: This is a hexagonal or polygonal prism with faceted surfaces, featuring a combination of flat planes and angular faces that create a geometric, low-poly appearance with darker and lighter shaded regions indicating multiple oriented surfaces.
def model_23138_630f02f9_0001():
    """Model: Part 7 v15"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 400, perimeter: 80
            with BuildLine():
                Line((10, -10), (-10, -10))
                Line((10, 10), (10, -10))
                Line((-10, 10), (10, 10))
                Line((-10, -10), (-10, 10))
            make_face()
        # TwoSides extrude (symmetric), distance=9
        extrude(amount=9, both=True)
    return part.part


# Description: This is a flat, dark blue parallelogram-shaped plate or panel with a slight 3D depth, featuring a recessed slot or channel running vertically along its left side.
def model_23144_88ca00a5_0007():
    """Model: top door v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 2845.1556, perimeter: 213.36
            with BuildLine():
                Line((26.67, -26.67), (26.67, 26.67))
                Line((26.67, 26.67), (-26.67, 26.67))
                Line((-26.67, 26.67), (-26.67, -26.67))
                Line((-26.67, -26.67), (26.67, -26.67))
            make_face()
        # OneSide extrude, distance=2.54
        extrude(amount=2.54)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 2.54), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 2258.06, perimeter: 190.5
            with BuildLine():
                Line((22.225, -25.4), (-22.225, -25.4))
                Line((22.225, 25.4), (22.225, -25.4))
                Line((-22.225, 25.4), (22.225, 25.4))
                Line((-22.225, -25.4), (-22.225, 25.4))
            make_face()
        # OneSide extrude, distance=-2.286
        extrude(amount=-2.286, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a flat rectangular parallelogram plate or panel with a slightly skewed trapezoidal profile, featuring beveled edges around its perimeter and a uniform dark blue-gray finish.
def model_23144_88ca00a5_0008():
    """Model: bottom door v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1219.3524, perimeter: 152.4
            with BuildLine():
                Line((26.67, -11.43), (-26.67, -11.43))
                Line((26.67, 11.43), (26.67, -11.43))
                Line((-26.67, 11.43), (26.67, 11.43))
                Line((-26.67, -11.43), (-26.67, 11.43))
            make_face()
        # OneSide extrude, distance=2.54
        extrude(amount=2.54)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 2.54), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1124.126784, perimeter: 145.288
            with BuildLine():
                Line((25.146, -11.176), (-25.146, -11.176))
                Line((25.146, 11.176), (25.146, -11.176))
                Line((-25.146, 11.176), (25.146, 11.176))
                Line((-25.146, -11.176), (-25.146, 11.176))
            make_face()
        # OneSide extrude, distance=-2.286
        extrude(amount=-2.286, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a hexagonal or wedge-shaped box/enclosure with a sloped top face, featuring a rectangular cutout or slot on one side and an angled upper surface, designed as a compact geometric container or structural component.
def model_23144_88ca00a5_0010():
    """Model: broiler v4"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2709.672, perimeter: 208.28
            with BuildLine():
                Line((25.4, -26.67), (-25.4, -26.67))
                Line((25.4, 26.67), (25.4, -26.67))
                Line((-25.4, 26.67), (25.4, 26.67))
                Line((-25.4, -26.67), (-25.4, 26.67))
            make_face()
        # OneSide extrude, distance=22.86
        extrude(amount=22.86)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(25.4, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 986.121470842, perimeter: 137.3870306951
            with BuildLine():
                Line((-24.1299996376, 21.7035160533), (-24.1299996376, 1.2699999809))
                Line((-24.1299996376, 1.2699999809), (24.1299996376, 1.2699999809))
                Line((24.1299996376, 1.2699999809), (24.1299996376, 21.7035160533))
                Line((24.1299996376, 21.7035160533), (-24.1299996376, 21.7035160533))
            make_face()
        # OneSide extrude, distance=-48.26
        extrude(amount=-48.26, mode=Mode.SUBTRACT)
    return part.part


# Description: This is an extruded angle or corner trim piece with an elongated triangular/wedge cross-section, featuring a dark navy base with a light blue top surface and a central ridge or reinforcing rib running along its length.
def model_23206_b99a5251_0045():
    """Model: 1_018-a v3 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 12 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.2100000212, perimeter: 4.3141593309
            with BuildLine():
                Line((0.1, 1), (1.0000000149, 1))
                Line((1.0000000149, 1), (1.0000000149, 1.1000000164))
                Line((1.0000000149, 1.1000000164), (-0.0000000015, 1.1000000164))
                CenterArc((-0.0000000015, 1.0000000164), 0.1, 90, 90)
                Line((-0.1000000015, 1.0000000164), (-0.1000000015, 0))
                Line((-0.1000000015, 0), (0, 0))
                Line((0, 0), (0, 0.9))
                CenterArc((0.1, 0.9), 0.1, 90, 90)
            make_face()
        # OneSide extrude, distance=5
        extrude(amount=5)
    return part.part


# Description: This is a boat hull or marine vessel component featuring a tapered, wedge-shaped body with an angled stern section, multiple internal structural ribs and frames, and an asymmetrical design typical of a ship's lower hull structure.
def model_23231_efe613bb_0008():
    """Model: X carriage v11"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 28 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.6569407963, perimeter: 5.8498964474
            with BuildLine():
                Line((0.25, -2.58), (0.25, -2.68))
                Line((0.25, -2.58), (0.2398765863, 0))
                Line((0, 0), (0.2398765863, 0))
                Line((0, 0), (0, -2.68))
                Line((0, -2.68), (0.25, -2.68))
            make_face()
            # Profile area: 2.016, perimeter: 7.04
            with BuildLine():
                Line((2.8, -3.4), (2.8, -2.68))
                Line((0.25, -2.68), (2.8, -2.68))
                Line((0, -2.68), (0.25, -2.68))
                Line((0, -3.4), (0, -2.68))
                Line((0, -3.4), (2.8, -3.4))
            make_face()
            # Profile area: 5.1135415778, perimeter: 21.3654549264
            with BuildLine():
                Line((0.2398765863, 0), (2.8, 0))
                Line((0.25, -2.58), (0.2398765863, 0))
                Line((0.25, -2.58), (0.25, -2.68))
                Line((0.25, -2.68), (2.8, -2.68))
                Line((2.8, -2.68), (2.8, 0))
            make_face()
            with BuildLine():
                CenterArc((1.25, -2.275), 0.2061552571, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((0.4500000305, -2.15), (0.4500000305, -2))
                Line((0.4500000305, -0.3), (0.4500000305, -2))
                Line((0.4500000305, -0.15), (0.4500000305, -0.3))
                Line((0.8500000305, -0.15), (0.4500000305, -0.15))
                Line((0.8500000305, -0.3), (0.8500000305, -0.15))
                Line((0.8500000305, -2), (0.8500000305, -0.3))
                Line((0.8500000305, -2.15), (0.8500000305, -2))
                Line((0.4500000305, -2.15), (0.8500000305, -2.15))
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                Line((2.4500000023, -0.2999999939), (2.45, -0.15))
                Line((2.4500000283, -1.9999999939), (2.4500000023, -0.2999999939))
                Line((2.4500000305, -2.15), (2.4500000283, -1.9999999939))
                Line((2.0500000305, -2.15), (2.4500000305, -2.15))
                Line((2.0500000305, -2), (2.0500000305, -2.15))
                Line((2.0500000305, -0.3), (2.0500000305, -2))
                Line((2.0500000305, -0.15), (2.0500000305, -0.3))
                Line((2.45, -0.15), (2.0500000305, -0.15))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.2
        extrude(amount=1.2)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 28 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.68, perimeter: 4.2
            with BuildLine():
                Line((0.8500000305, -2), (0.4500000305, -2))
                Line((0.8500000305, -2), (0.8500000305, -0.3))
                Line((0.4500000305, -0.3), (0.8500000305, -0.3))
                Line((0.4500000305, -0.3), (0.4500000305, -2))
            make_face()
            # Profile area: 0.679999974, perimeter: 4.1999999695
            with BuildLine():
                Line((2.0500000305, -0.3), (2.4500000023, -0.2999999939))
                Line((2.0500000305, -0.3), (2.0500000305, -2))
                Line((2.0500000305, -2), (2.4500000283, -1.9999999939))
                Line((2.4500000283, -1.9999999939), (2.4500000023, -0.2999999939))
            make_face()
        # OneSide extrude, distance=1.1
        extrude(amount=1.1, mode=Mode.ADD)

        # Sketch1 -> Extrude3 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 28 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.016, perimeter: 7.04
            with BuildLine():
                Line((2.8, -3.4), (2.8, -2.68))
                Line((0.25, -2.68), (2.8, -2.68))
                Line((0, -2.68), (0.25, -2.68))
                Line((0, -3.4), (0, -2.68))
                Line((0, -3.4), (2.8, -3.4))
            make_face()
        # OneSide extrude, distance=0.6
        extrude(amount=0.6, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a hexagonal or polygonal housing/enclosure with a sloped, faceted top surface and a solid base, featuring multiple triangulated panels and what appears to be mounting or structural flanges on its sides.
def model_23231_efe613bb_0010():
    """Model: NEMA back v4"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 12 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.2356932223, perimeter: 7.5378254531
            with BuildLine():
                Line((1.005, -2.105), (0, -2.105))
                CenterArc((2.105, -2.105), 1.1, 90, 90)
                Line((2.105, 0), (2.105, -1.005))
                Line((0.7, 0), (2.105, 0))
                Line((0, -0.7), (0.7, 0))
                Line((0, -2.105), (0, -0.7))
            make_face()
        # OneSide extrude, distance=0.8
        extrude(amount=0.8)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 12 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.8992612621, perimeter: 3.8184290228
            with BuildLine():
                Line((1.85, -2.105), (1.005, -2.105))
                CenterArc((2.105, -2.105), 0.255, 90, 90)
                Line((2.105, -1.005), (2.105, -1.85))
                CenterArc((2.105, -2.105), 1.1, 90, 90)
            make_face()
        # OneSide extrude, distance=0.8
        extrude(amount=0.8, mode=Mode.ADD)

        # Sketch1 -> Extrude3 (Join)
        # Sketch on XZ construction plane
        # Sketch has 12 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1568, perimeter: 2.1439191899
            with BuildLine():
                Line((0.42, 0), (0.7, 0))
                Line((0, -0.42), (0.42, 0))
                Line((0, -0.42), (0, -0.7))
                Line((0, -0.7), (0.7, 0))
            make_face()
        # OneSide extrude, distance=1.05
        extrude(amount=1.05, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical rod or pin with a slightly tapered or rounded end, featuring a smooth, uniform shaft suitable for mechanical assembly or fastening applications.
def model_23231_efe613bb_0017():
    """Model: nema shaft v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            Circle(0.25)
        # OneSide extrude, distance=7.2
        extrude(amount=7.2)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 7.2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            Circle(0.1)
        # OneSide extrude, distance=-0.05
        extrude(amount=-0.05, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical flanged bushing or adapter with a large circular flange at the top and a smaller diameter cylindrical body below, featuring a central hollow passage and what appears to be internal threading or grooves.
def model_23231_efe613bb_0021():
    """Model: PTFE tube mount 2 v10"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2007477706, perimeter: 4.4610615681
            with BuildLine():
                CenterArc((0, 0), 0.4, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.31, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.4
        extrude(amount=0.4)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))) as sk:
            # Profile area: 0.5360342465, perimeter: 6.1261056745
            with BuildLine():
                CenterArc((0, 0), 0.575, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.4, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # TwoSides offset extrude, full=0.4, trim=0.3
        extrude(amount=0.4, mode=Mode.ADD)
        extrude(sk.sketch, amount=0.3, mode=Mode.SUBTRACT)

        # Sketch1 -> Extrude3 (Join)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2007477706, perimeter: 4.4610615681
            with BuildLine():
                CenterArc((0, 0), 0.4, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.31, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.1
        extrude(amount=-0.1, mode=Mode.ADD)
    return part.part


# Description: This is a long, rectangular prismatic beam or bar with a uniform cross-section, angled diagonally, featuring slightly beveled or rounded edges at the top end.
def model_23255_972fbfe6_0011():
    """Model: part7.1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 19 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0353429174, perimeter: 0.771238898
            with BuildLine():
                Line((-1.825, 0), (-2.125, 0))
                CenterArc((-1.975, 0), 0.15, -180, 69.1939682435)
                CenterArc((-1.975, 0), 0.15, -110.8060317565, 110.8060317565)
            make_face()
            # Profile area: 0.0353429174, perimeter: 0.771238898
            with BuildLine():
                CenterArc((-1.975, 0), 0.15, 0, 87.6655870148)
                CenterArc((-1.975, 0), 0.15, 87.6655870148, 92.3344129852)
                Line((-1.825, 0), (-2.125, 0))
            make_face()
            # Profile area: 1.8156030485, perimeter: 8.6390459581
            with BuildLine():
                CenterArc((-1.975, 0), 0.15, -110.8060317565, 110.8060317565)
                CenterArc((0.6357594937, 6.8706939145), 7.5, -110.8060317565, 31.8358638927)
                CenterArc((1.975, 0), 0.5, -180, 101.0298321362)
                Line((1.475, 0), (-1.825, 0))
            make_face()
            # Profile area: 0.3926990817, perimeter: 2.5707963268
            with BuildLine():
                CenterArc((1.975, 0), 0.5, -180, 101.0298321362)
                CenterArc((1.975, 0), 0.5, -78.9701678638, 78.9701678638)
                Line((2.475, 0), (1.475, 0))
            make_face()
            # Profile area: 0.3926990817, perimeter: 2.5707963268
            with BuildLine():
                Line((2.475, 0), (1.475, 0))
                CenterArc((1.975, 0), 0.5, 0, 102.4170844373)
                CenterArc((1.975, 0), 0.5, 102.4170844373, 77.5829155627)
            make_face()
            # Profile area: 0.7454484616, perimeter: 8.0684796244
            with BuildLine():
                Line((1.475, 0), (-1.825, 0))
                CenterArc((1.975, 0), 0.5, 102.4170844373, 77.5829155627)
                CenterArc((-1.3579113924, 15.1374271807), 15, -92.3344129852, 14.7514974225)
                CenterArc((-1.975, 0), 0.15, 0, 87.6655870148)
            make_face()
        # OneSide extrude, distance=16
        extrude(amount=16)
    return part.part


# Description: This is a bracket or mounting bracket with a rectangular body featuring internal ribbing/bracing, angular side flanges, and cutout openings designed for fastening and structural support.
def model_23258_87a2ba81_0005():
    """Model: P4-Seats"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 11 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 43.0630699639, perimeter: 39.3762624804
            with BuildLine():
                Line((-6.1664344851, -11.5747005426), (-3, 0))
                CenterArc((-5.173174128, -9.8387760445), 2, -119.7773037156, 104.4775121859)
                Line((-0.955908672, -2.0023326005), (-3.2440573709, -10.3665151254))
                Line((2.2657163123, -2.8836568655), (-0.955908672, -2.0023326005))
                CenterArc((2.7934553932, -0.9545401084), 2, -105.2997915296, 90)
                Line((4.8545069205, -1), (4.7225721503, -1.4822791893))
                Line((2.71, 0), (4.8545069205, -1))
                Line((-3, 0), (2.71, 0))
            make_face()
        # Symmetric extrude, each_side=5
        extrude(amount=5, both=True)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 0, -1))):
            # Profile area: 1.7671458676, perimeter: 4.7123889804
            Circle(0.75)
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)
    return part.part


# Description: This is a curved knife or blade tool featuring a dark gray textured handle with blue accents and a long, thin, slightly curved blade that tapers to a sharp point.
def model_23264_20be13a0_0006():
    """Model: Crank v8"""
    with BuildPart() as part:
        # Sketch3 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 4 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 9.1194302517, perimeter: 18.3295370025
            with BuildLine():
                Line((2.5031984209, 1.4054744822), (4.3458764109, 1.4054744822))
                CenterArc((-0.5058477268, -1.7726968303), 5.8, 33.2272118221, 25.4209282138)
                CenterArc((4.2034739033, 5.957007011), 3.2513, -157.0585077793, 35.7066478153)
                CenterArc((5.0615599048, 6.4447571272), 4.2331889849, 172.5776938842, 31.9163946649)
                CenterArc((0.060628077, 7.0962446491), 0.81, -7.4223061158, 267.8123134313)
                CenterArc((5.1831104128, 6.1422235168), 5.26, 178.3071545462, 51.8143527213)
                CenterArc((-1.5234400653, -1.8848419922), 5.2, 39.2535396458, 10.8679676217)
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)
    return part.part


# Description: This is a polyhedron or truncated geometric solid with an irregular hexagonal or octagonal shape, featuring multiple flat triangular and polygonal faces in varying shades, with a sharp angular design and no prominent holes, slots, or curves.
def model_23264_20be13a0_0008():
    """Model: Nut v2 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.8660245962, perimeter: 3.4641
            with BuildLine():
                Line((0.288675, -0.4999997669), (0.57735, 0))
                Line((0.57735, 0), (0.288675, 0.4999997669))
                Line((0.288675, 0.4999997669), (-0.288675, 0.4999997669))
                Line((-0.288675, 0.4999997669), (-0.57735, 0))
                Line((-0.57735, 0), (-0.288675, -0.4999997669))
                Line((-0.288675, -0.4999997669), (0.288675, -0.4999997669))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)
    return part.part


# Description: This is a structural bracket or support component with an elongated, curved body featuring two opposing curved flanges and a central oval aperture, designed for lightweight load distribution and assembly mounting.
def model_23264_20be13a0_0010():
    """Model: Washer v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.3296314285, perimeter: 6.3076196324
            with BuildLine():
                Line((-0.36, -0.7000036008), (0.36, -0.7000036008))
                CenterArc((0.7523, -1.01), 0.4999970575, 65.7384640873, 75.9456608911)
                Line((0.95775, -0.554163017), (0.95775, 0.5541587348))
                CenterArc((0.7522996423, 1.0100002086), 0.5000012987, -141.6834267618, 75.944788593)
                Line((0.3600000924, 0.6999963992), (-0.36, 0.6999963992))
                CenterArc((-0.7523, 1.01), 0.5000015225, -114.2613053086, 75.9447828025)
                Line((-0.95775, 0.5541581195), (-0.95775, -0.5541530841))
                CenterArc((-0.7523067279, -1.0099965287), 0.5000001841, 38.3150849327, 75.9454438571)
            make_face()
        # OneSide extrude, distance=0.12
        extrude(amount=0.12)

        # Sketch3 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.12, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.3888262203, perimeter: 2.2656496823
            with BuildLine():
                CenterArc((0, 0), 0.37, 125.8247743687, 108.3504512627)
                Line((-0.2165640783, -0.3), (0.2165640783, -0.3))
                CenterArc((0, 0), 0.37, -54.1752256313, 108.3504512627)
                Line((0.2165640783, 0.3), (-0.2165640783, 0.3))
            make_face()
        # OneSide extrude, distance=-0.12
        extrude(amount=-0.12, mode=Mode.SUBTRACT)
    return part.part


# Description: This is an aerodynamic fairings or cowling component with a streamlined, elongated teardrop shape featuring a curved mesh or perforated section on one side and flat triangulated panel sections that form a pointed, swept-back profile.
def model_23264_20be13a0_0011():
    """Model: Clamp v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 6.0371141266, perimeter: 9.2876176784
            with BuildLine():
                CenterArc((-0.5, 0), 1.3250023585, 89.8918948839, 180.2162102322)
                Line((-0.4975, -1.325), (0.7375, -1.325))
                Line((0.7375, -1.325), (0.7375, 1.325))
                Line((0.7375, 1.325), (-0.4975, 1.325))
            make_face()
        # OneSide extrude, distance=0.12
        extrude(amount=0.12)

        # Sketch3 -> Extrude3 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.12, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            with Locations((1.0725, 0)):
                Circle(0.2)
        # OneSide extrude, distance=-0.12
        extrude(amount=-0.12, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a bent metal duct or pipe fitting with a curved central section connecting two rectangular flanged ends, featuring horizontal ribbing or corrugation along the bend for structural reinforcement.
def model_23269_7c2afd7f_0002():
    """Model: Crankshaft Connect v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 10 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 4.9224476619, perimeter: 16.43707757
            with BuildLine():
                CenterArc((0, 0), 2, -150, 120)
                Line((3, -1), (1.7320508076, -1))
                Line((3, 0), (3, -1))
                Line((1.5, 0), (3, 0))
                CenterArc((0, 0), 1.5, 180, 180)
                Line((-3, 0), (-1.5, 0))
                Line((-3, -1), (-3, 0))
                Line((-1.7320508076, -1), (-3, -1))
            make_face()
        # OneSide extrude, distance=2.5
        extrude(amount=2.5)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            with Locations((1.25, 2.3)):
                Circle(0.4)
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            with Locations((1.25, -2.3)):
                Circle(0.4)
        # OneSide extrude, distance=-3
        extrude(amount=-3, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a dark blue/navy composite or molded part with an angular, asymmetrical wedge-like shape, featuring a faceted upper surface with light blue geometric panels and a curved, tapered profile that narrows toward one end.
def model_23331_192866b6_0001():
    """Model: Pedals v1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 59.8174770425, perimeter: 32.853981634
            with BuildLine():
                CenterArc((5, 0), 2.5, -90, 180)
                Line((-5, 2.5), (5, 2.5))
                Line((-5, -2.5), (-5, 2.5))
                Line((5, -2.5), (-5, -2.5))
            make_face()
        # OneSide extrude, distance=3
        extrude(amount=3)

        # Sketch3 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 3, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 7.3779940458, perimeter: 12.8774995705
            with BuildLine():
                Line((-6.2255667323, 0.5580802172), (-1, 0.5))
                Line((-1, 0.5), (-1, 2))
                Line((-1, 2), (-5, 2))
                CenterArc((-5, 0.7582019062), 1.2417980938, 90, 99.2739296779)
            make_face()
        # OneSide extrude, distance=-3
        extrude(amount=-3, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a rectangular box-shaped component with a large central cavity and two curved inlet or outlet ports on the top surface, featuring angled side walls and perforated or mesh-covered openings.
def model_23410_0163b27d_0005():
    """Model: Component28"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.5871681663, perimeter: 3.8283185844
            with BuildLine():
                Line((10.000000149, -9.800000146), (10.4500001587, -9.800000146))
                Line((10.000000149, -10.3000001535), (10.000000149, -9.800000146))
                Line((11.3000001684, -10.3000001535), (10.000000149, -10.3000001535))
                Line((11.3000001684, -9.800000146), (11.3000001684, -10.3000001535))
                Line((10.8500001587, -9.800000146), (11.3000001684, -9.800000146))
                CenterArc((10.6500001587, -9.800000146), 0.2, 180, 180)
            make_face()
        # TwoSides extrude (symmetric), distance=0.225
        extrude(amount=0.225, both=True)

        # Sketch3 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1884955592, perimeter: 2.2849555922
            with BuildLine():
                CenterArc((10.6500001587, -9.800000146), 0.4, 180, 180)
                Line((10.8500001587, -9.800000146), (11.0500001587, -9.800000146))
                CenterArc((10.6500001587, -9.800000146), 0.2, 180, 180)
                Line((10.2500001587, -9.800000146), (10.4500001587, -9.800000146))
            make_face()
        # TwoSides extrude (symmetric), distance=0.25
        extrude(amount=0.25, both=True, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical tube or sleeve with rounded ends, featuring a smooth, hollow tubular body with no visible holes, slots, or flanges.
def model_23410_0163b27d_0009():
    """Model: pipeline - t piece adapter"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0549778714, perimeter: 2.1991148575
            with BuildLine():
                CenterArc((4, -9.5), 0.2, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((4, -9.5), 0.15, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)
    return part.part


# Description: This is a cylindrical suppressor or muzzle device with a tapered geometric head section featuring angular faceted surfaces and a threaded cylindrical barrel body for firearm attachment.
def model_23422_f214bd4d_0000():
    """Model: Component46"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 0.3771393409, perimeter: 2.286
            with BuildLine():
                Line((0.1905, 0.3299556788), (0.381, 0))
                Line((-0.1905, 0.3299556788), (0.1905, 0.3299556788))
                Line((-0.381, 0), (-0.1905, 0.3299556788))
                Line((-0.1905, -0.3299556788), (-0.381, 0))
                Line((0.1905, -0.3299556788), (-0.1905, -0.3299556788))
                Line((0.381, 0), (0.1905, -0.3299556788))
            make_face()
        # OneSide extrude, distance=0.508
        extrude(amount=0.508)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XY construction plane
        with BuildSketch(Plane.XY):
            # Profile area: 0.3166921744, perimeter: 1.994911335
            Circle(0.3175)
        # OneSide extrude, distance=2.54
        extrude(amount=2.54, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical sleeve or adapter with a rounded end cap on one side and a tapered or angled opening on the opposite end, designed to connect or guide components along its axis.
def model_23449_3f3d53b6_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 18 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 10.0906307148, perimeter: 41.2551861052
            with BuildLine():
                CenterArc((-5.4679393019, 3.5052925514), 2.2874544297, 28.9550243719, 207.2807045469)
                CenterArc((-7.4870762645, 0.4850693093), 1.345541924, -74.1746635953, 130.410392514)
                CenterArc((-7.0519625243, -1.049998767), 0.250001233, 105.8253364047, 180)
                CenterArc((-7.4870762645, 0.4850693093), 1.84554439, -74.1746635953, 130.476090831)
                CenterArc((-5.4679393019, 3.5052925514), 1.7874544297, 28.9550243719, 207.2128711184)
                Line((-3.9039166759, 4.3706402062), (-1.1375, -0.6293597938))
                CenterArc((0, 0), 1.3, -151.0449756281, 151.0449756281)
                Line((1.3, 0), (1.3, 0.5))
                Line((0.8, 0.5), (1.3, 0.5))
                Line((0.8, 0), (0.8, 0.5))
                CenterArc((0, 0), 0.8, -151.0449756281, 151.0449756281)
                Line((-3.4664166759, 4.6127016654), (-0.7, -0.3872983346))
            make_face()
        # OneSide extrude, distance=12
        extrude(amount=12)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(-0.7, -0.3872983346, 0), x_dir=(0, 0, -1), z_dir=(0.875, 0.4841229183, 0))):
            # Profile area: 6.0012903087, perimeter: 12.3207123549
            with BuildLine():
                Line((-3.4193450417, 2.7387335556), (-5.3345908104, 2.7387335556))
                Line((-2.0000000298, 3.0500000454), (-3.4193450417, 2.7387335556))
                Line((-3.57999992, 3.8899999131), (-2.0000000298, 3.0500000454))
                Line((-2.059999954, 4.8799998909), (-3.57999992, 3.8899999131))
                Line((-3.57999992, 5.5399998762), (-2.059999954, 4.8799998909))
                Line((-5.0799998865, 4.6899998952), (-3.57999992, 5.5399998762))
                Line((-5.3345908104, 2.7387335556), (-5.0799998865, 4.6899998952))
            make_face()
            # Profile area: 0.853044331, perimeter: 4.9057646866
            with BuildLine():
                Line((-3.57999992, 2.7035014735), (-3.57999992, 2.2518019558))
                Line((-3.4193450417, 2.7387335556), (-3.57999992, 2.7035014735))
                Line((-3.4193450417, 2.7387335556), (-5.3345908104, 2.7387335556))
                Line((-5.3935665505, 2.2867246046), (-5.3345908104, 2.7387335556))
                Line((-5.100000076, 2.350000035), (-5.3935665505, 2.2867246046))
                Line((-5.100000076, 2.2518019558), (-5.100000076, 2.350000035))
                Line((-3.57999992, 2.2518019558), (-5.100000076, 2.2518019558))
            make_face()
            # Profile area: 2.1307392204, perimeter: 5.8436042617
            with BuildLine():
                Line((-3.57999992, 2.2518019558), (-5.100000076, 2.2518019558))
                Line((-5.100000076, 0.849999981), (-5.100000076, 2.2518019558))
                Line((-3.57999992, 0.849999981), (-5.100000076, 0.849999981))
                Line((-3.57999992, 2.2518019558), (-3.57999992, 0.849999981))
            make_face()
            # Profile area: 0.6104693113, perimeter: 3.5637488687
            with BuildLine():
                Line((-9.8746216743, 2.2518019558), (-11.126214421, 2.2518019558))
                Line((-9.6679225184, 2.7387335556), (-9.8746216743, 2.2518019558))
                Line((-9.6679225184, 2.7387335556), (-10.9237427702, 2.7387335556))
                Line((-11.126214421, 2.2518019558), (-10.9237427702, 2.7387335556))
            make_face()
            # Profile area: 5.9974975008, perimeter: 12.7705764683
            with BuildLine():
                Line((-9.6679225184, 2.7387335556), (-10.9237427702, 2.7387335556))
                Line((-9.0680004307, 4.1520001972), (-9.6679225184, 2.7387335556))
                Line((-8.472130445, 2.7387335556), (-9.0680004307, 4.1520001972))
                Line((-7.2013169443, 2.7387335556), (-8.472130445, 2.7387335556))
                Line((-8.2876180628, 5.3300717286), (-7.2013169443, 2.7387335556))
                Line((-9.8462351327, 5.3300717286), (-8.2876180628, 5.3300717286))
                Line((-10.9237427702, 2.7387335556), (-9.8462351327, 5.3300717286))
            make_face()
            # Profile area: 0.6185121998, perimeter: 3.5968765001
            with BuildLine():
                Line((-7.2013169443, 2.7387335556), (-6.9971929333, 2.2518019558))
                Line((-7.2013169443, 2.7387335556), (-8.472130445, 2.7387335556))
                Line((-8.2668274138, 2.2518019558), (-8.472130445, 2.7387335556))
                Line((-6.9971929333, 2.2518019558), (-8.2668274138, 2.2518019558))
            make_face()
            # Profile area: 1.8046017228, perimeter: 5.623732707
            with BuildLine():
                Line((-6.9971929333, 2.2518019558), (-8.2668274138, 2.2518019558))
                Line((-7.666732595, 0.8285149812), (-8.2668274138, 2.2518019558))
                Line((-6.4005443567, 0.8285149812), (-7.666732595, 0.8285149812))
                Line((-6.9971929333, 2.2518019558), (-6.4005443567, 0.8285149812))
            make_face()
            # Profile area: 1.8849333906, perimeter: 6.8068394196
            with BuildLine():
                Line((-11.1491462192, 2.1966524218), (-11.126214421, 2.2518019558))
                Line((-10.3149681703, 0.6600857442), (-11.1491462192, 2.1966524218))
                Line((-8.6566558835, 1.9784363193), (-10.3149681703, 0.6600857442))
                Line((-9.9899997767, 1.9799999557), (-8.6566558835, 1.9784363193))
                Line((-9.8746216743, 2.2518019558), (-9.9899997767, 1.9799999557))
                Line((-9.8746216743, 2.2518019558), (-11.126214421, 2.2518019558))
            make_face()
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a flat, diamond-shaped or parallelogram-based plate with a faceted, multi-surfaced top featuring triangulated panels and internal ribbing or support structure, creating a lightweight yet rigid geometric form.
def model_23472_ed1faab6_0002():
    """Model: Handle v4"""
    with BuildPart() as part:
        # Sketch3 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 14 constraints, 10 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 24.6219265625, perimeter: 33.2561600315
            with BuildLine():
                Line((0.9525, 1.905), (7.3025, 1.905))
                Line((0, 1.905), (0.9525, 1.905))
                Line((0, 0), (0, 1.905))
                Line((15.24, 0), (0, 0))
                Line((15.24, 0), (15.24, 0.79375))
                Line((15.24, 0.79375), (7.3025, 1.905))
            make_face()
        # OneSide extrude, distance=10.16
        extrude(amount=10.16)
    return part.part


# Description: This is a sheet metal bracket or mounting frame with an open rectangular profile featuring a twisted or angled top flange and vertical side walls forming a C or U-shaped channel with a hollow center opening.
def model_23493_57512264_0001():
    """Model: szczyt"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 14 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 2.2, perimeter: 10.6
            with BuildLine():
                Line((0.7, 0), (-0.7, 0))
                Line((0.7, 0), (0.7, 2))
                Line((0.7, 2), (-0.7, 2))
                Line((-0.7, 0), (-0.7, 2))
            make_face()
            with BuildLine():
                Line((-0.2, 1.8), (0.2, 1.8))
                Line((0.2, 1.8), (0.2, 0.3))
                Line((0.2, 0.3), (-0.2, 0.3))
                Line((-0.2, 1.8), (-0.2, 0.3))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.05
        extrude(amount=0.05)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.7), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.075, perimeter: 3.1
            with BuildLine():
                Line((-1.5, 2), (-1.5, 1.95))
                Line((-1.5, 1.95), (0, 1.95))
                Line((0, 1.95), (0, 2))
                Line((0, 2), (-1.5, 2))
            make_face()
        # OneSide extrude, distance=-1.4
        extrude(amount=-1.4, mode=Mode.ADD)
    return part.part


# Description: A flat, rectangular solar panel with a blue photovoltaic surface and dark frame/border, designed for mounting and energy collection.
def model_23493_57512264_0004():
    """Model: podstawa1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 48.6834757469, perimeter: 34.2685258803
            with BuildLine():
                CenterArc((4, 0), 2.8504385627, -37.8749836511, 75.7499673022)
                Line((6.25, 1.75), (-7.25, 1.75))
                Line((-7.25, 1.75), (-7.25, -1.75))
                Line((-7.25, -1.75), (6.25, -1.75))
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch6 -> Extrude5 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1.75), x_dir=(1, 0, 0), z_dir=(0, 0, 1))) as sk:
            # Profile area: 0.2989152677, perimeter: 3.6299094643
            with BuildLine():
                CenterArc((4.0076230831, -3.9496185949), 5, 63.3540918674, 18.505370013)
                Line((6.25, 0.5193573239), (6.25, 1))
                Line((6.25, 1), (4.7156313919, 1))
            make_face()
            # Profile area: 5.0415167462, perimeter: 10.4424255034
            with BuildLine():
                Line((6.25, 1), (4.7156313919, 1))
                Line((6.25, 0.5193573239), (6.25, 1))
                CenterArc((4.0076230831, -3.9496185949), 5, 50.3071156051, 13.0469762623)
                Line((7.2009843845, -0.1022242041), (8.212160439, 0.0101996184))
                Line((8.212160439, 0.0101996184), (7.9770340903, 2.1250016987))
                Line((7.9770340903, 2.1250016987), (5.7145110786, 2.1177543665))
                Line((4.4817228955, 1.0278535917), (5.7145110786, 2.1177543665))
                CenterArc((4.0076230831, -3.9496185949), 5, 81.8594618805, 2.699580473)
            make_face()
        # TwoSides extrude, along=-4, against=1
        extrude(amount=-4, mode=Mode.SUBTRACT)
        extrude(sk.sketch, amount=1, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a simple L-shaped bracket or angle iron featuring a horizontal bar with a small perpendicular flange or foot on the left end, used for structural support or mounting applications.
def model_23493_57512264_0009():
    """Model: rurka"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0314159265, perimeter: 0.6283185307
            with Locations((0.0030982133, 0.2943026411)):
                Circle(0.1)
        # Symmetric extrude, each_side=4.7
        extrude(amount=4.7, both=True)

        # Sketch3 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(-4.7, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 0.0985336099, perimeter: 1.3424157315
            with BuildLine():
                Line((-0.1030982133, 0.2943026411), (-0.1030982133, 0.7084308742))
                CenterArc((-0.0030982133, 0.2943026411), 0.1, 180, 180)
                Line((0.0969017867, 0.7084308742), (0.0969017867, 0.2943026411))
                Line((-0.1030982133, 0.7084308742), (0.0969017867, 0.7084308742))
            make_face()
        # OneSide extrude, distance=0.1
        extrude(amount=0.1, mode=Mode.ADD)
    return part.part


# Description: This is a hexagonal or elongated geometric container or duct with a hollow interior channel running through its length, featuring tapered end sections and a open central passage.
def model_23554_a0845d54_0001():
    """Model: Bullone molla v5"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 66.3045638514, perimeter: 60.0962663416
            with BuildLine():
                Line((-3.1754264805, -5.5), (3.1754264805, -5.5))
                Line((3.1754264805, -5.5), (6.3508529611, 0))
                Line((6.3508529611, 0), (3.1754264805, 5.5))
                Line((3.1754264805, 5.5), (-3.1754264805, 5.5))
                Line((-3.1754264805, 5.5), (-6.3508529611, 0))
                Line((-6.3508529611, 0), (-3.1754264805, -5.5))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 3.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=0.5
        extrude(amount=0.5, both=True)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, -0.5, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 26.2492575182, perimeter: 69.5210443024
            with BuildLine():
                Line((6.3508529611, 0), (3.1754264805, 5.5))
                Line((3.1754264805, 5.5), (-3.1754264805, 5.5))
                Line((-3.1754264805, 5.5), (-6.3508529611, 0))
                Line((-6.3508529611, 0), (-3.1754264805, -5.5))
                Line((-3.1754264805, -5.5), (3.1754264805, -5.5))
                Line((3.1754264805, -5.5), (6.3508529611, 0))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.5
        extrude(amount=1.5, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical mesh or perforated basket with an oval/elliptical shape, featuring a solid dark rim around the top edge and an open mesh body with radial wire or rib patterns extending downward from the rim to a solid base.
def model_23554_a0845d54_0009():
    """Model: piatto molla v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 73.6310778185, perimeter: 39.2699081699
            with BuildLine():
                CenterArc((0, 0), 5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.8
        extrude(amount=0.8)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 16.4933614313, perimeter: 65.9734457254
            with BuildLine():
                CenterArc((0, 0), 5.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-2
        extrude(amount=-2, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical fastener or spacer with a hexagonal head on top, featuring a hollow cylindrical body with vertical ribbing or fluting along its sides and an open top with a curved flange rim.
def model_23554_a0845d54_0010():
    """Model: gancio  v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.926990817, perimeter: 15.7079632679
            with BuildLine():
                CenterArc((0, 0), 1.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=2.5
        extrude(amount=2.5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 5.497787114, perimeter: 21.9911485602
            with BuildLine():
                CenterArc((0, 0), 1.9999999976, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 3.926990817, perimeter: 15.7079632679
            with BuildLine():
                CenterArc((0, 0), 1.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical container lid or cap with an oval/elliptical shape, featuring a ribbed or textured mesh pattern on the transparent top surface and a solid dark base ring, designed for sealing or covering a wide, shallow cylindrical vessel.
def model_23554_a0845d54_0016():
    """Model: tappo serbatoio v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 28.2743338823, perimeter: 18.8495559215
            Circle(3)
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 5.4212108229, perimeter: 39.4269878026
            with BuildLine():
                CenterArc((0, 0), 3.275, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 28.2743338823, perimeter: 18.8495559215
            Circle(3)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)
    return part.part


# Description: This is a truncated polyhedron or irregular dodecahedron-like geometric solid featuring multiple flat faceted surfaces with rectangular cutouts or slots along its edges, creating an open-frame lattice structure with a complex angular shape.
def model_23602_5daaccf5_0004():
    """Model: Nut v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.9159079447, perimeter: 8.2532913801
            with BuildLine():
                Line((0.1331797547, 1.3690861927), (-1.1190735455, 0.7998801472))
                Line((-1.1190735455, 0.7998801472), (-1.2522533002, -0.5692060455))
                Line((-1.2522533002, -0.5692060455), (-0.1331797547, -1.3690861927))
                Line((-0.1331797547, -1.3690861927), (1.1190735455, -0.7998801472))
                Line((1.1190735455, -0.7998801472), (1.2522533002, 0.5692060455))
                Line((1.2522533002, 0.5692060455), (0.1331797547, 1.3690861927))
            make_face()
        # OneSide extrude, distance=1.397
        extrude(amount=1.397)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.397, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.9793260902, perimeter: 4.9872783376
            Circle(0.79375)
        # OneSide extrude, distance=-2.032
        extrude(amount=-2.032, mode=Mode.SUBTRACT)
    return part.part


# Description: These are two blue polygonal geometric shapes or stone-like objects with faceted surfaces, featuring irregular polyhedron forms with angular faces and minimal surface details.
def model_23683_72d2534f_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch22 -> Extrude13 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.0594940802, perimeter: 7.5
            with BuildLine():
                Line((-3.6022304916, -44.6890580094), (-2.9772304916, -43.6065262547))
                Line((-2.9772304916, -43.6065262547), (-3.6022304916, -42.5239944999))
                Line((-3.6022304916, -42.5239944999), (-4.8522304916, -42.5239944999))
                Line((-4.8522304916, -42.5239944999), (-5.4772304916, -43.6065262547))
                Line((-5.4772304916, -43.6065262547), (-4.8522304916, -44.6890580094))
                Line((-4.8522304916, -44.6890580094), (-3.6022304916, -44.6890580094))
            make_face()
        # OneSide extrude, distance=0.95
        extrude(amount=0.95)

        # Sketch21 -> Extrude14 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 10.3923048454, perimeter: 12
            with BuildLine():
                Line((-8.5968849342, -42.6013719889), (-10.331906437, -41.6065351254))
                Line((-10.331906437, -41.6065351254), (-12.0609711847, -42.6116893912))
                Line((-12.0609711847, -42.6116893912), (-12.0550144297, -44.6116805205))
                Line((-12.0550144297, -44.6116805205), (-10.3199929269, -45.6065173839))
                Line((-10.3199929269, -45.6065173839), (-8.5909281792, -44.6013631181))
                Line((-8.5909281792, -44.6013631181), (-8.5968849342, -42.6013719889))
            make_face()
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)
    return part.part


# Description: This is a ring or cylindrical band with a toroidal (doughnut-like) overall shape, featuring a central hollow core and uniform radial thickness with a visible slot or gap on one side.
def model_23739_47fb03ab_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 3.914315276, perimeter: 41.0951735016
            with BuildLine():
                CenterArc((0, 0), 3.3655, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 3.175, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=1.27
        extrude(amount=1.27, both=True)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on YZ construction plane
        # Sketch has 6 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 2.5179884008, perimeter: 16.4963442568
            with BuildLine():
                CenterArc((0, 0), 3.683, 25.5332289441, 128.9335421118)
                Line((-3.3233014835, 1.5875), (-3.0368099763, 1.4506465517))
                CenterArc((0, 0), 3.3655, 25.5332254548, 128.9335456011)
                Line((3.3233014835, 1.5875), (3.0368100646, 1.4506463668))
            make_face()
        # Symmetric extrude, each_side=1.143
        extrude(amount=1.143, both=True, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical tube or sleeve with an open top end and a mesh or perforated section visible on the upper portion, appearing to be a filter housing or ventilation component with a slightly tapered or curved upper edge.
def model_23753_b32a4e2e_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 19.8762876701, perimeter: 15.8042018875
            Circle(2.515316852)
        # OneSide extrude, distance=5.5
        extrude(amount=5.5)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 5.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 8.8744992937, perimeter: 10.5603147274
            Circle(1.6807262895)
        # OneSide extrude, distance=-6
        extrude(amount=-6, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a curved ribbon or strap-like bracket featuring two rectangular flanges connected by a flexible, wave-like central section with a mesh/lattice pattern, designed to flex and bend while maintaining structural rigidity at the mounting points.
def model_23770_f35c1c3b_0008():
    """Model: handle 2 v8"""
    with BuildPart() as part:
        # Sketch5 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 12 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.6789368494, perimeter: 8.51958582
            with BuildLine():
                Line((3, 0), (1.5, 0))
                Line((3, 0.3021826566), (3, 0))
                Line((1.9770396157, 0.3021826566), (3, 0.3021826566))
                CenterArc((0, 0), 2, 8.6901759172, 81.3098240828)
                Line((0, 1.5), (0, 2))
                CenterArc((0, 0), 1.5, 0, 90)
            make_face()
            # Profile area: 1.6789368494, perimeter: 8.51958582
            with BuildLine():
                Line((0, 1.5), (0, 2))
                CenterArc((0, 0), 2, 90, 81.3098240828)
                Line((-1.9770396157, 0.3021826566), (-3, 0.3021826566))
                Line((-3, 0.3021826566), (-3, 0))
                Line((-3, 0), (-1.5, 0))
                CenterArc((0, 0), 1.5, 90, 90)
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


# Description: This is a cylindrical belt or band component with an oval/elongated shape, featuring mesh or perforated sides and a smooth central body with visible slot or groove details along its surface.
def model_23774_716b8bc4_0007():
    """Model: Cuscinetto v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.5132741229, perimeter: 25.1327412287
            with BuildLine():
                CenterArc((0, 0), 2.1, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.9, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch1 -> Extrude2 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.7592922053, perimeter: 17.5929193001
            with BuildLine():
                CenterArc((0, 0), 1.5000000507, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.3000000194, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1
        extrude(amount=1)

        # Sketch1 -> Extrude3 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 6 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1256636743, perimeter: 1.2566369023
            with BuildLine():
                CenterArc((0, 1.7000000253), 0.1999999747, 90, 180)
                CenterArc((0, 1.7000000253), 0.1999999747, -90, 180)
            make_face()
        # OneSide extrude, distance=1
        extrude(amount=1)
    return part.part


# Description: This is a cylindrical shaft or post with a polygonal (faceted) dome-shaped cap or head at the top, featuring a textured or ribbed surface along the cylindrical body.
def model_23775_6d8ee909_0005():
    """Model: Vite pale v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            Circle(1)
        # OneSide extrude, distance=7
        extrude(amount=7)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 7, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.704078822, perimeter: 15.2831853072
            with BuildLine():
                Line((-1.2990381057, -0.75), (0, -1.5))
                Line((0, -1.5), (1.2990381057, -0.75))
                Line((1.2990381057, -0.75), (1.2990381057, 0.75))
                Line((1.2990381057, 0.75), (0, 1.5))
                Line((0, 1.5), (-1.2990381057, 0.75))
                Line((-1.2990381057, 0.75), (-1.2990381057, -0.75))
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 3.1415926536, perimeter: 6.2831853072
            Circle(1)
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)
    return part.part


# Description: This is a spring clip or retaining ring featuring an open-loop, oval shape with a split design and textured surface, commonly used for securing or fastening components together.
def model_23775_6d8ee909_0009():
    """Model: OR cuscinetti v3 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 83.368130089, perimeter: 121.7052994001
            with BuildLine():
                CenterArc((0, 0), 10.37, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 9, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.4998991949, perimeter: 6.4296872015
            with BuildLine():
                Line((7.7314974383, 1), (8.94427191, 1))
                Line((7.7314974383, -1), (7.7314974383, 1))
                Line((8.94427191, -1), (7.7314974383, -1))
                CenterArc((0, 0), 9, -6.3793702084, 12.7587404169)
            make_face()
            # Profile area: 2.7449169369, perimeter: 6.7620499452
            with BuildLine():
                CenterArc((0, 0), 9, -6.3793702084, 12.7587404169)
                Line((10.3216713763, -1), (8.94427191, -1))
                CenterArc((0, 0), 10.37, -5.533746708, 11.067493416)
                Line((8.94427191, 1), (10.3216713763, 1))
            make_face()
            # Profile area: 1.2921889914, perimeter: 5.359770002
            with BuildLine():
                Line((11, -1), (10.3216713763, -1))
                Line((11, 1), (11, -1))
                Line((10.3216713763, 1), (11, 1))
                CenterArc((0, 0), 10.37, -5.533746708, 11.067493416)
            make_face()
        # OneSide extrude, distance=-1.5
        extrude(amount=-1.5, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a polyhedral geometric solid featuring multiple angular facets and triangular faces with a roughly cubic or dodecahedron-like shape, characterized by sharp edges, varied plane orientations, and internal mesh or lattice detailing visible through semi-transparent surfaces.
def model_23876_74957d38_0009():
    """Model: ISO 4032 M8 v1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 3 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 1.4635829324, perimeter: 4.5033320997
            with BuildLine():
                Line((0.65, -0.375277675), (0.65, 0.375277675))
                Line((0.65, 0.375277675), (0, 0.7505553499))
                Line((0, 0.7505553499), (-0.65, 0.375277675))
                Line((-0.65, 0.375277675), (-0.65, -0.375277675))
                Line((-0.65, -0.375277675), (0, -0.7505553499))
                Line((0, -0.7505553499), (0.65, -0.375277675))
            make_face()
        # OneSide extrude, distance=0.68
        extrude(amount=0.68)

        # Sketch3 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.68, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            Circle(0.4)
        # OneSide extrude, distance=-1.1
        extrude(amount=-1.1, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a hexagonal or octagonal ring-shaped spacer or washer with a large central circular hole and thick walls, featuring a flat face design typical of a flange or adapter ring.
def model_23881_bec7f38c_0001():
    """Model: lockring v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 3.2986722863, perimeter: 21.9911485751
            with BuildLine():
                CenterArc((0, 0), 1.9, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.6, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.4
        extrude(amount=0.4)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.4), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.1940428918, perimeter: 4.183582805
            with BuildLine():
                Line((1.645454155, -0.9499898021), (2.1939310229, 0))
                Line((2.1939310229, 0), (1.6454482707, 0.9499999939))
                CenterArc((0, 0), 1.9, -29.9996448996, 59.999644688)
            make_face()
            # Profile area: 0.1940428919, perimeter: 4.1836063842
            with BuildLine():
                Line((1.6454482707, 0.9499999939), (1.0969655115, 1.9))
                Line((1.0969655115, 1.9), (0, 1.9))
                CenterArc((0, 0), 1.9, 29.9999997884, 60.0000002116)
            make_face()
            # Profile area: 0.1940428918, perimeter: 4.1836299624
            with BuildLine():
                Line((-0.0000000205, -1.9), (1.0969655115, -1.9))
                Line((1.0969655115, -1.9), (1.645454155, -0.9499898021))
                CenterArc((0, 0), 1.9, -90.0000006194, 60.0003557198)
            make_face()
            # Profile area: 0.1940428919, perimeter: 4.1836063458
            with BuildLine():
                Line((-1.6454482714, -0.9499999928), (-1.0969655115, -1.9))
                Line((-1.0969655115, -1.9), (-0.0000000205, -1.9))
                CenterArc((0, 0), 1.9, -150.0000002515, 59.9999996321)
            make_face()
            # Profile area: 0.1940428919, perimeter: 4.1836063376
            with BuildLine():
                CenterArc((0, 0), 1.9, 90, 59.9999995081)
                Line((0, 1.9), (-1.0969655115, 1.9))
                Line((-1.0969655115, 1.9), (-1.645448259, 0.9500000141))
            make_face()
            # Profile area: 0.1940428919, perimeter: 4.1836063861
            with BuildLine():
                CenterArc((0, 0), 1.9, 149.9999995081, 60.0000002404)
                Line((-1.645448259, 0.9500000141), (-2.1939310229, 0))
                Line((-2.1939310229, 0), (-1.6454482714, -0.9499999928))
            make_face()
        # OneSide extrude, distance=-0.4
        extrude(amount=-0.4, mode=Mode.ADD)

        # Sketch2 -> Extrude3 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.4), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.1940428918, perimeter: 4.183582805
            with BuildLine():
                Line((1.645454155, -0.9499898021), (2.1939310229, 0))
                Line((2.1939310229, 0), (1.6454482707, 0.9499999939))
                CenterArc((0, 0), 1.9, -29.9996448996, 59.999644688)
            make_face()
            # Profile area: 0.1940428919, perimeter: 4.1836063842
            with BuildLine():
                Line((1.6454482707, 0.9499999939), (1.0969655115, 1.9))
                Line((1.0969655115, 1.9), (0, 1.9))
                CenterArc((0, 0), 1.9, 29.9999997884, 60.0000002116)
            make_face()
            # Profile area: 0.1940428918, perimeter: 4.1836299624
            with BuildLine():
                Line((-0.0000000205, -1.9), (1.0969655115, -1.9))
                Line((1.0969655115, -1.9), (1.645454155, -0.9499898021))
                CenterArc((0, 0), 1.9, -90.0000006194, 60.0003557198)
            make_face()
            # Profile area: 0.1940428919, perimeter: 4.1836063458
            with BuildLine():
                Line((-1.6454482714, -0.9499999928), (-1.0969655115, -1.9))
                Line((-1.0969655115, -1.9), (-0.0000000205, -1.9))
                CenterArc((0, 0), 1.9, -150.0000002515, 59.9999996321)
            make_face()
            # Profile area: 0.1940428919, perimeter: 4.1836063376
            with BuildLine():
                CenterArc((0, 0), 1.9, 90, 59.9999995081)
                Line((0, 1.9), (-1.0969655115, 1.9))
                Line((-1.0969655115, 1.9), (-1.645448259, 0.9500000141))
            make_face()
            # Profile area: 0.1940428919, perimeter: 4.1836063861
            with BuildLine():
                CenterArc((0, 0), 1.9, 149.9999995081, 60.0000002404)
                Line((-1.645448259, 0.9500000141), (-2.1939310229, 0))
                Line((-2.1939310229, 0), (-1.6454482714, -0.9499999928))
            make_face()
            # Profile area: 1.3509996299, perimeter: 27.0199925981
            with BuildLine():
                Line((-1.1547005384, -2), (1.1547005384, -2))
                Line((1.1547005384, -2), (2.3094010768, 0))
                Line((2.3094010768, 0), (1.1547005384, 2))
                Line((1.1547005384, 2), (-1.1547005384, 2))
                Line((-1.1547005384, 2), (-2.3094010768, 0))
                Line((-2.3094010768, 0), (-1.1547005384, -2))
            make_face()
            with BuildLine():
                Line((-1.0969655115, 1.9), (-1.645448259, 0.9500000141))
                Line((0, 1.9), (-1.0969655115, 1.9))
                Line((1.0969655115, 1.9), (0, 1.9))
                Line((1.6454482707, 0.9499999939), (1.0969655115, 1.9))
                Line((2.1939310229, 0), (1.6454482707, 0.9499999939))
                Line((1.645454155, -0.9499898021), (2.1939310229, 0))
                Line((1.0969655115, -1.9), (1.645454155, -0.9499898021))
                Line((-0.0000000205, -1.9), (1.0969655115, -1.9))
                Line((-1.0969655115, -1.9), (-0.0000000205, -1.9))
                Line((-1.6454482714, -0.9499999928), (-1.0969655115, -1.9))
                Line((-2.1939310229, 0), (-1.6454482714, -0.9499999928))
                Line((-1.645448259, 0.9500000141), (-2.1939310229, 0))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.4
        extrude(amount=-0.4, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical coupling or connector with a hollow tubular body, featuring two opposing rectangular slots or windows cut through its walls and a central bore, designed to allow flexibility and alignment between connected components.
def model_23881_bec7f38c_0011():
    """Model: crank bolt v4 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.9011204639, perimeter: 8.1764905955
            with BuildLine():
                CenterArc((0, 0), 0.75, 0, 360)
            make_face()
            with BuildLine():
                Line((0.5773502692, 0), (0.2886751346, 0.5))
                Line((0.2886751346, -0.5), (0.5773502692, 0))
                Line((-0.2886751346, -0.5), (0.2886751346, -0.5))
                Line((-0.5773502692, 0), (-0.2886751346, -0.5))
                Line((-0.2886751346, 0.5), (-0.5773502692, 0))
                Line((0.2886751346, 0.5), (-0.2886751346, 0.5))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1.5
        extrude(amount=1.5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1.5), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 3.1415926536, perimeter: 12.5663706144
            with BuildLine():
                CenterArc((0, 0), 1.25, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.75, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 0.9011204639, perimeter: 8.1764905955
            with BuildLine():
                CenterArc((0, 0), 0.75, 0, 360)
            make_face()
            with BuildLine():
                Line((0.5773502692, 0), (0.2886751346, -0.5))
                Line((0.2886751346, -0.5), (-0.2886751346, -0.5))
                Line((-0.2886751346, -0.5), (-0.5773502692, 0))
                Line((-0.5773502692, 0), (-0.2886751346, 0.5))
                Line((-0.2886751346, 0.5), (0.2886751346, 0.5))
                Line((0.2886751346, 0.5), (0.5773502692, 0))
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)
    return part.part


# Description: This is a toroidal ring or doughnut-shaped part with a uniform circular cross-section, featuring a smooth curved geometry with a hollow center and no additional features or holes.
def model_23881_bec7f38c_0014():
    """Model: bearing shield v3"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 6.7858401318, perimeter: 22.6194671058
            with BuildLine():
                CenterArc((0, 0), 2.1, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.05
        extrude(amount=0.05)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.05), x_dir=(-1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 1.4844025288, perimeter: 19.7920337176
            with BuildLine():
                CenterArc((0, 0), 1.65, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.5, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.1
        extrude(amount=0.1, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical pin or dowel with rounded ends, featuring a smooth cylindrical shaft and hemispherical caps at both extremities, commonly used as a fastener or alignment component.
def model_23883_040b5fef_0000():
    """Model: center axle"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            Circle(0.25)
        # OneSide extrude, distance=2.9
        extrude(amount=2.9)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 2.9), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.1884955592, perimeter: 3.7699111843
            with BuildLine():
                CenterArc((0, 0), 0.35, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.1
        extrude(amount=-0.1, mode=Mode.ADD)
    return part.part


# Description: This is a toroidal (doughnut-shaped) component with a hollow center and curved, ribbed or textured external surfaces, featuring a continuous ring geometry with uniform cross-sectional thickness throughout.
def model_23951_3afdbe1c_0000():
    """Model: Part_Thirteen"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 3 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 2.6703537218, perimeter: 10.6814150784
            with BuildLine():
                CenterArc((0, 0), 1.1, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.6000000089, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 1.130973389, perimeter: 3.7699112405
            Circle(0.6000000089)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2)

        # Sketch1 -> Extrude2 (Join)
        # Sketch on XY construction plane
        # Sketch has 3 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.1074114104, perimeter: 14.7654854719
            with BuildLine():
                CenterArc((0, 0), 1.25, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 1.1, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)

        # Sketch1 -> Extrude3 (Cut)
        # Sketch on XY construction plane
        # Sketch has 3 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.130973389, perimeter: 3.7699112405
            Circle(0.6000000089)
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.SUBTRACT)

        # Sketch1 -> Extrude4 (Cut)
        # Sketch on XY construction plane
        # Sketch has 3 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 2.6703537218, perimeter: 10.6814150784
            with BuildLine():
                CenterArc((0, 0), 1.1, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.6000000089, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.05
        extrude(amount=0.05, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a rectangular channel or tray with two parallel internal dividers, featuring an open top, sloped sides, and a base that forms three separate compartments for organizing or containing items.
def model_23951_3afdbe1c_0001():
    """Model: Part_Two"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 27 constraints, 13 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.34, perimeter: 23.8
            with BuildLine():
                Line((-4.1, 5.85), (-4.1, -5.85))
                Line((-4.1, 5.85), (-4.3, 5.85))
                Line((-4.3, -5.85), (-4.3, 5.85))
                Line((-4.1, -5.85), (-4.3, -5.85))
            make_face()
            # Profile area: 2.34, perimeter: 23.8
            with BuildLine():
                Line((4.1, -5.85), (4.3, -5.85))
                Line((4.3, 5.85), (4.3, -5.85))
                Line((4.1, 5.85), (4.3, 5.85))
                Line((4.1, 5.85), (4.1, -5.85))
            make_face()
            # Profile area: 6.36, perimeter: 63.6
            with BuildLine():
                Line((2.3, -5.85), (2.3, 5.85))
                Line((2.3, 5.85), (-2.3, 5.85))
                Line((-2.3, 5.85), (-2.3, -5.85))
                Line((-2.3, -5.85), (2.3, -5.85))
            make_face()
            with BuildLine():
                Line((-2.1, -5.65), (2.1, -5.65))
                Line((-2.1, 5.65), (-2.1, -5.65))
                Line((2.1, 5.65), (-2.1, 5.65))
                Line((2.1, -5.65), (2.1, 5.65))
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 47.46, perimeter: 31
            with BuildLine():
                Line((2.1, -5.65), (2.1, 5.65))
                Line((2.1, 5.65), (-2.1, 5.65))
                Line((-2.1, 5.65), (-2.1, -5.65))
                Line((-2.1, -5.65), (2.1, -5.65))
            make_face()
        # OneSide extrude, distance=-1.2
        extrude(amount=-1.2)

        # Sketch1 -> Extrude2 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 27 constraints, 13 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 47.46, perimeter: 31
            with BuildLine():
                Line((2.1, -5.65), (2.1, 5.65))
                Line((2.1, 5.65), (-2.1, 5.65))
                Line((-2.1, 5.65), (-2.1, -5.65))
                Line((-2.1, -5.65), (2.1, -5.65))
            make_face()
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.SUBTRACT)

        # Sketch1 -> Extrude3 (Join)
        # Sketch on XZ construction plane
        # Sketch has 27 constraints, 13 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 2.34, perimeter: 23.8
            with BuildLine():
                Line((-4.1, 5.85), (-4.1, -5.85))
                Line((-4.1, 5.85), (-4.3, 5.85))
                Line((-4.3, -5.85), (-4.3, 5.85))
                Line((-4.1, -5.85), (-4.3, -5.85))
            make_face()
            # Profile area: 2.34, perimeter: 23.8
            with BuildLine():
                Line((4.1, -5.85), (4.3, -5.85))
                Line((4.3, 5.85), (4.3, -5.85))
                Line((4.1, 5.85), (4.3, 5.85))
                Line((4.1, 5.85), (4.1, -5.85))
            make_face()
            # Profile area: 21.06, perimeter: 27
            with BuildLine():
                Line((-2.3, 5.85), (-4.1, 5.85))
                Line((-4.1, 5.85), (-4.1, -5.85))
                Line((-2.3, -5.85), (-4.1, -5.85))
                Line((-2.3, 5.85), (-2.3, -5.85))
            make_face()
            # Profile area: 6.36, perimeter: 63.6
            with BuildLine():
                Line((2.3, -5.85), (2.3, 5.85))
                Line((2.3, 5.85), (-2.3, 5.85))
                Line((-2.3, 5.85), (-2.3, -5.85))
                Line((-2.3, -5.85), (2.3, -5.85))
            make_face()
            with BuildLine():
                Line((-2.1, -5.65), (2.1, -5.65))
                Line((-2.1, 5.65), (-2.1, -5.65))
                Line((2.1, 5.65), (-2.1, 5.65))
                Line((2.1, -5.65), (2.1, 5.65))
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 21.06, perimeter: 27
            with BuildLine():
                Line((2.3, -5.85), (4.1, -5.85))
                Line((4.1, 5.85), (4.1, -5.85))
                Line((2.3, 5.85), (4.1, 5.85))
                Line((2.3, -5.85), (2.3, 5.85))
            make_face()
        # OneSide extrude, distance=0.2
        extrude(amount=0.2, mode=Mode.ADD)
    return part.part


# Description: This is a knight chess piece with a stylized horse head featuring an angular, geometric design, a curved neck, and a flared base for stability.
def model_23956_ee17fe48_0002():
    """Model: Tip Actual v3 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 38 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 59.2444397974, perimeter: 44.8413296093
            with BuildLine():
                Line((3.5168161404, 9.0864029925), (3.0264935416, 9.086203024))
                Line((3.0264935416, 9.086203024), (3.0264935513, 9.9108902786))
                Line((3.0264265341, 9.9110029694), (3.0264935513, 9.9108902786))
                Line((3.0264265341, 9.9110029694), (2.5360935416, 9.910603024))
                Line((2.5360935416, 9.910603024), (2.5360935416, 10.735403024))
                Line((2.5360935416, 10.735403024), (2.0456935416, 10.735403024))
                Line((2.0456935416, 10.735403024), (2.0275309427, 11.560003024))
                Line((2.0275309427, 11.560003024), (1.5552935416, 11.560003024))
                Line((1.5552935416, 11.560003024), (1.5552935416, 12.3847426575))
                Line((0, 15), (1.5552935416, 12.3847426575))
                Line((0, 0), (0, 15))
                Line((0, 0), (8.912856073, 0))
                CenterArc((10.3761, 4.7811), 5, 168.384635096, 84.5987632328)
                Line((5.4784935416, 5.787803024), (4.9880935416, 5.787803024))
                Line((4.9880935416, 5.787803024), (4.9880935416, 6.6124204782))
                Line((4.9879850079, 6.6126029798), (4.9880935416, 6.6124204782))
                Line((4.9879850079, 6.6126029798), (4.4976935416, 6.612403024))
                Line((4.4976935416, 6.612403024), (4.4976935416, 7.4370379324))
                Line((4.4975953854, 7.437202984), (4.4976935416, 7.4370379324))
                Line((4.4975953854, 7.437202984), (4.0072935416, 7.437003024))
                Line((4.0072935416, 7.437003024), (4.0072935416, 8.2616553866))
                Line((4.0072057629, 8.2618029882), (4.0072935416, 8.2616553866))
                Line((4.0072057629, 8.2618029882), (3.5168935416, 8.261603024))
                Line((3.5168935416, 8.261603024), (3.5168935416, 9.0862728407))
                Line((3.5168161404, 9.0864029925), (3.5168935416, 9.0862728407))
            make_face()
        # Symmetric extrude, each_side=3
        extrude(amount=3, both=True)

        # Sketch3 -> Extrude2 (Cut)
        # Sketch on XY construction plane
        # Sketch has 9 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 44.6360859494, perimeter: 35.9884788496
            with BuildLine():
                Line((-0.4694, -0.8287), (8.249988017, -0.8287))
                CenterArc((10.3755, 4.7822), 6, -149.2597778232, 38.5121698376)
                Line((-0.4694, 11.2796), (5.2185380771, 1.7153215013))
                Line((-0.4694, -0.8287), (-0.4694, 11.2796))
            make_face()
        # Symmetric extrude, each_side=2.5
        extrude(amount=2.5, both=True, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a toroidal (donut-shaped) washer or spacer with a large central hole and a smooth, rounded outer profile, featuring a mesh-textured surface on portions of its geometry.
def model_23956_ee17fe48_0015():
    """Model: Ring(2) - Speader part v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 51.0508806208, perimeter: 40.8407044967
            with BuildLine():
                CenterArc((0, 0), 4.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 2, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=1
        extrude(amount=1, both=True)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 12.9983417633, perimeter: 57.5042331402
            with BuildLine():
                CenterArc((0, 0), 4.802082953, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 4.35, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # Symmetric extrude, each_side=0.25
        extrude(amount=0.25, both=True, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a rectangular base or chassis component with an elongated box shape, featuring multiple angled internal ribs or structural reinforcements visible through the top surface and a sloped side wall for structural support.
def model_23961_8b0c848b_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 18 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 13.0845059746, perimeter: 23.5680886845
            with BuildLine():
                Line((-2.2551821619, -0.400000006), (2.25, -0.400000006))
                Line((2.25, -0.400000006), (2.25, -0.5))
                Line((5, -0.5), (2.25, -0.5))
                Line((5, 1), (5, -0.5))
                Line((2.6006474163, 1), (5, 1))
                CenterArc((2.6006474163, 0.99), 0.01, 90, 148.7042279771)
                CenterArc((2.3465715202, 0.957831294), 0.25, -90, 95.4222510907)
                Line((-2.2595358188, 0.707831294), (2.3465715202, 0.707831294))
                CenterArc((-2.2595358188, 0.957831294), 0.25, -178.7999415997, 88.7999415997)
                Line((-2.5102689237, 0.9902094344), (-2.5094809844, 0.9525954343))
                CenterArc((-2.5202667303, 0.99), 0.01, 1.2000584003, 88.7999415997)
                Line((-2.5202667303, 1), (-5, 1))
                Line((-5, 1), (-5, -0.5))
                Line((-2.2551821619, -0.5), (-5, -0.5))
                Line((-2.2551821619, -0.5), (-2.2551821619, -0.400000006))
            make_face()
        # Symmetric extrude, each_side=2.5
        extrude(amount=2.5, both=True)

        # Sketch5 -> Extrude5 (Cut)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.354235396, perimeter: 2.109846741
            with Locations((-4.2161766761, 1.7608214615)):
                Circle(0.335792538)
        # OneSide extrude, distance=-2.5
        extrude(amount=-2.5, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a mounting bracket or support arm with an angular, bent design featuring a dark upper section connected to a blue-highlighted lower arm, incorporating structural ribs and mounting points for mechanical assembly.
def model_24032_d6172503_0013():
    """Model: snab grab catch v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 34 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 3.5831963688, perimeter: 21.6361523402
            with BuildLine():
                Line((0.1088851031, 2.3674816407), (0.1088851031, 1))
                Line((-0.1011148969, 1), (0.1088851031, 1))
                Line((-0.1011148969, 1), (-0.1011148969, 2.3674816407))
                CenterArc((0.0038851031, 2.659157831), 0.31, 109.8151335667, 140.3865862963)
                Line((-0.1012006883, 2.9508031232), (-0.1012006883, 3.1978005139))
                CenterArc((0.0038851031, 2.659157831), 0.5487977436, 101.0393805965, 124.6484143453)
                CenterArc((-0.5611148969, 2.0804275052), 0.26, 0, 45.6877949418)
                Line((-0.3011148969, 1.34), (-0.3011148969, 2.0804275052))
                CenterArc((-0.6411148969, 1.34), 0.34, -90, 90)
                Line((-2.9, 1), (-0.6411148969, 1))
                CenterArc((-2.9, 0.9), 0.1, 90, 90)
                Line((-3, 0.67), (-3, 0.9))
                CenterArc((-2.9, 0.67), 0.1, -180, 90)
                Line((2.9, 0.57), (-2.9, 0.57))
                CenterArc((2.9, 0.67), 0.1, -90, 90)
                Line((3, 1), (3, 0.67))
                Line((0.6488851031, 1), (3, 1))
                CenterArc((0.6488851031, 1.34), 0.34, 180, 90)
                Line((0.3088851031, 2.1360182703), (0.3088851031, 1.34))
                CenterArc((0.5688851031, 2.1360182703), 0.26, 137.203067028, 42.796932972)
                CenterArc((0.0038851031, 2.659157831), 0.51, -42.796932972, 120.915776951)
                Line((0.1088851031, 2.9508340214), (0.1088851031, 3.1582319738))
                CenterArc((0.0038851031, 2.659157831), 0.31, -70.201719863, 140.4034397259)
            make_face()
        # OneSide extrude, distance=2.54
        extrude(amount=2.54)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.2042820623, perimeter: 1.6022122533
            with Locations((-1.27, 2.1)):
                Circle(0.255)
        # OneSide extrude, distance=-2
        extrude(amount=-2, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a threaded fastener or mounting stud with a cylindrical shaft and a geometric base feature, consisting of an elongated dark gray rod extending from a multi-faceted blue base that provides mounting or alignment surfaces.
def model_24032_d6172503_0023():
    """Model: m5 screw v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.8660254038, perimeter: 3.4641016151
            with BuildLine():
                Line((-0.2314654569, 0.5289206704), (-0.5737914656, 0.0640053695))
                Line((-0.5737914656, 0.0640053695), (-0.3423260088, -0.464915301))
                Line((-0.3423260088, -0.464915301), (0.2314654569, -0.5289206704))
                Line((0.2314654569, -0.5289206704), (0.5737914656, -0.0640053695))
                Line((0.5737914656, -0.0640053695), (0.3423260088, 0.464915301))
                Line((0.3423260088, 0.464915301), (-0.2314654569, 0.5289206704))
            make_face()
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.3, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            Circle(0.25)
        # OneSide extrude, distance=2
        extrude(amount=2, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical socket or wrench bit with a hexagonal drive end, featuring a long shaft and a deeper recessed cup at the top for fastener engagement.
def model_24032_d6172503_0024():
    """Model: Damper 2 v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.9760782022, perimeter: 7.0685834706
            Circle(1.125)
        # OneSide extrude, distance=3
        extrude(amount=3)

        # Sketch5 -> Extrude5 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            Circle(0.5)
        # OneSide extrude, distance=8.58
        extrude(amount=8.58, mode=Mode.ADD)
    return part.part


# Description: This is a solar-powered mounting bracket or spacecraft component featuring a central angular body with two large rectangular solar panel or heat dissipation fins extending outward at opposing angles, connected by a ribbed cylindrical central section with ventilation slots.
def model_24032_d6172503_0027():
    """Model: snab grab catch v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 39 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 5.5779197412, perimeter: 20.6338761848
            with BuildLine():
                Line((0.0569789362, 2), (0.0239623248, 2))
                CenterArc((0.0239623248, 2.5), 0.5, -90, 1.8920563469)
                CenterArc((0.0569789362, 2.5), 0.5, 180, 88.1079436531)
                Line((-0.4430210638, 3.8), (-0.4430210638, 2.5))
                Line((-0.56595, 3.8), (-0.4430210638, 3.8))
                CenterArc((-0.56595, 3.3), 0.5, 90, 90)
                Line((-1.06595, 2.3589), (-1.06595, 3.3))
                CenterArc((-1.42485, 2.3589), 0.3589, -90, 90)
                Line((-3.34135, 2), (-1.42485, 2))
                CenterArc((-3.34135, 1.9282), 0.0718, 90, 90)
                Line((-3.41315, 1.5693), (-3.41315, 1.9282))
                CenterArc((-3.34135, 1.5693), 0.0718, 180, 90)
                Line((3.34135, 1.4975), (-3.34135, 1.4975))
                CenterArc((3.34135, 1.5693), 0.0718, -90, 90)
                Line((3.41315, 1.9282), (3.41315, 1.5693))
                CenterArc((3.34135, 1.9282), 0.0718, 0, 90)
                Line((1.42485, 2), (3.34135, 2))
                CenterArc((1.42485, 2.3589), 0.3589, 180, 90)
                Line((1.06595, 3.3), (1.06595, 2.3589))
                CenterArc((0.56595, 3.3), 0.5, 0, 90)
                Line((0.5239623248, 3.8), (0.56595, 3.8))
                Line((0.5239623248, 2.5), (0.5239623248, 3.8))
                CenterArc((0.0239623248, 2.5), 0.5, -88.1079436531, 88.1079436531)
                CenterArc((0.0569789362, 2.5), 0.5, -91.8920563469, 1.8920563469)
            make_face()
        # OneSide extrude, distance=2.54
        extrude(amount=2.54)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 14 constraints, 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.672, perimeter: 3.52
            with BuildLine():
                Line((-0.99, -3.21315), (-1.27, -3.21315))
                Line((-0.99, -2.01315), (-0.99, -3.21315))
                Line((-1.55, -2.01315), (-0.99, -2.01315))
                Line((-1.55, -3.21315), (-1.55, -2.01315))
                Line((-1.27, -3.21315), (-1.55, -3.21315))
            make_face()
            # Profile area: 0.672, perimeter: 3.52
            with BuildLine():
                Line((-1.55, 3.21315), (-0.99, 3.21315))
                Line((-1.55, 2.01315), (-1.55, 3.21315))
                Line((-0.99, 2.01315), (-1.55, 2.01315))
                Line((-0.99, 3.21315), (-0.99, 2.01315))
            make_face()
        # OneSide extrude, distance=-1
        extrude(amount=-1, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a hex bolt (or machine bolt) consisting of a long cylindrical shaft with a hexagonal head at the base, used for fastening applications.
def model_24032_d6172503_0032():
    """Model: m8 x 115 v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.2162959324, perimeter: 6.5292778058
            with BuildLine():
                Line((0.2170218839, -1.0440468543), (0.8917102563, -0.5847949648))
                Line((0.8917102563, -0.5847949648), (1.0440468543, 0.2170218839))
                Line((1.0440468543, 0.2170218839), (0.5847949648, 0.8917102563))
                Line((0.5847949648, 0.8917102563), (-0.2170218839, 1.0440468543))
                Line((-0.2170218839, 1.0440468543), (-0.8917102563, 0.5847949648))
                Line((-0.8917102563, 0.5847949648), (-1.0440468543, -0.2170218839))
                Line((-1.0440468543, -0.2170218839), (-0.5847949648, -0.8917102563))
                Line((-0.5847949648, -0.8917102563), (0.2170218839, -1.0440468543))
            make_face()
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.5, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.5026548246, perimeter: 2.5132741229
            Circle(0.4)
        # OneSide extrude, distance=12.5
        extrude(amount=12.5, mode=Mode.ADD)
    return part.part


# Description: This is a flanged connector or mounting bracket featuring a rectangular base with angled flanges and a cylindrical socket extending upward at an angle, designed to join or mount two components at an offset angle.
def model_24032_d6172503_0033():
    """Model: m10x15 v1 (2)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 3.4641016151, perimeter: 6.9282032303
            with BuildLine():
                Line((0.2988584907, -1.1153550717), (1.1153550717, -0.2988584907))
                Line((1.1153550717, -0.2988584907), (0.8164965809, 0.8164965809))
                Line((0.8164965809, 0.8164965809), (-0.2988584907, 1.1153550717))
                Line((-0.2988584907, 1.1153550717), (-1.1153550717, 0.2988584907))
                Line((-1.1153550717, 0.2988584907), (-0.8164965809, -0.8164965809))
                Line((-0.8164965809, -0.8164965809), (0.2988584907, -1.1153550717))
            make_face()
        # OneSide extrude, distance=0.6
        extrude(amount=0.6)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.6, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            Circle(0.5)
        # OneSide extrude, distance=1.5
        extrude(amount=1.5, mode=Mode.ADD)
    return part.part


# Description: This is a rectangular box-like tray or container with a tapered, open top design featuring an angled front flange and internal ribbing or support structures for reinforcement.
def model_24047_9eb475f0_0007():
    """Model: Valve cover"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        with BuildSketch(Plane(origin=(0, 28, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 356.110160052, perimeter: 78.8728800074
            with BuildLine():
                Line((11.7900821449, 4.9734328945), (11.7900821449, -9.0265671055))
                Line((-13.6463578588, 4.9734328945), (11.7900821449, 4.9734328945))
                Line((-13.6463578588, -9.0265671055), (-13.6463578588, 4.9734328945))
                Line((11.7900821449, -9.0265671055), (-13.6463578588, -9.0265671055))
            make_face()
        # OneSide extrude, distance=4
        extrude(amount=4)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 28, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 251.6062640394, perimeter: 68.6728800074
            with BuildLine():
                Line((-11.7900821449, 3.2734328945), (11.9463578588, 3.2734328945))
                Line((-11.7900821449, 3.2734328945), (-11.7900821449, -7.3265671055))
                Line((11.9463578588, -7.3265671055), (-11.7900821449, -7.3265671055))
                Line((11.9463578588, 3.2734328945), (11.9463578588, -7.3265671055))
            make_face()
            # Profile area: 25.0537359606, perimeter: 25.9271199926
            with BuildLine():
                Line((-14.1536421412, 3.2734328945), (-11.7900821449, 3.2734328945))
                Line((-14.1536421412, -7.3265671055), (-14.1536421412, 3.2734328945))
                Line((-11.7900821449, -7.3265671055), (-14.1536421412, -7.3265671055))
                Line((-11.7900821449, 3.2734328945), (-11.7900821449, -7.3265671055))
            make_face()
        # OneSide extrude, distance=-3.3
        extrude(amount=-3.3, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a rifle stock or foregrip component featuring an elongated horizontal body with a curved left end, a central slot or cutout along the top surface, and a tapered right end.
def model_24056_959fa476_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 49 constraints, 27 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.865741316, perimeter: 12.7340089056
            with BuildLine():
                Line((1.752592345, 0.5588000003), (-1.71788836, 0.5588))
                Line((-1.71788836, 0.5588), (-2.0828, 0.4318))
                CenterArc((-1.1563434206, 0.9683609657), 1.0706163942, -149.9225540681, 57.917595072)
                CenterArc((-1.0287, 4.6145422119), 4.71903119, -92.0049589961, 4.0099179922)
                Line((-0.8636, -0.1016), (0.45837094, -0.0553212))
                CenterArc((0.5990342404, -0.0641000523), 0.14093698, 95.2158872158, 81.2128923893)
                CenterArc((0.9823945044, -4.2636186261), 4.3579171014, 77.1836182992, 18.0322689166)
                Line((2.05744064, 0.05073142), (1.94909948, -0.0142748))
                Line((1.752592345, 0.5588000003), (2.05744064, 0.05073142))
            make_face()
            with BuildLine():
                Line((0.4412615, 0.2032), (1.34547356, 0.2032))
                CenterArc((0.380492, 0.1758728444), 0.0666311156, 24.2127526805, 65.7872473195)
                Line((0.380492, 0.24250396), (-0.0508018522, 0.24250396))
                CenterArc((-0.1016, 0.20076668), 0.06574536, 39.4075497208, 50.5924502792)
                Line((-0.2970276, 0.26651204), (-0.1016, 0.26651204))
                CenterArc((-0.2970276, 0.31773114), 0.0512191, 90, 180)
                Line((-0.2970276, 0.36895024), (-0.1016, 0.36895024))
                CenterArc((-0.1016, 0.4346956), 0.06574536, -90, 50.5924502792)
                Line((0.380492, 0.39295832), (-0.0508018522, 0.39295832))
                CenterArc((0.380492, 0.4595894356), 0.0666311156, -90, 65.7872473195)
                Line((1.34547356, 0.43226228), (0.4412615, 0.43226228))
                CenterArc((1.34547356, 0.31773114), 0.11453114, -90, 180)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.04
        extrude(amount=0.04)
    return part.part


# Description: This is a curved, elongated tray or pan with an oval footprint, featuring a textured or ribbed surface pattern on the interior and sloped side walls that form a shallow basin shape.
def model_24090_a2bf0d93_0005():
    """Model: Placa de la mano v4 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 2.7493394431, perimeter: 27.6687653994
            with BuildLine():
                Line((-6.1194411065, -5.1544584143), (-6.1194411065, -5.4645528805))
                CenterArc((0, 0), 8.2042, -138.2357089554, 94.1150299702)
                Line((5.8895907697, -5.4155998344), (5.8895907697, -5.7115337875))
                CenterArc((0, 0), 8.001, -139.8922736731, 97.2930986303)
            make_face()
        # OneSide extrude, distance=-13.716
        extrude(amount=-13.716)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on XZ construction plane
        # Sketch has 8 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 212.6226541734, perimeter: 70.5572169083
            with BuildLine():
                Line((6.8311978704, -1.0714805892), (-7.3867056277, -1.0714805892))
                Line((6.8311978704, 14.4152121974), (6.8311978704, -1.0714805892))
                Line((-7.3867056277, 14.4152121974), (6.8311978704, 14.4152121974))
                Line((-7.3867056277, -1.0714805892), (-7.3867056277, 14.4152121974))
            make_face()
            with BuildLine():
                EllipticalCenterArc((0, 7.8740002513), 2.4003, 1.0033, 0, 360, 180)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-11.43
        extrude(amount=-11.43, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a multi-chambered aerospace or industrial bracket featuring three interconnected hexagonal/octagonal box sections with internal ribbing and truss-like structural supports, designed for lightweight strength with minimal material.
def model_24094_a5dcc4fc_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 18 constraints, 12 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 5.25, perimeter: 10
            with BuildLine():
                Line((4, -4.5), (7.5, -4.5))
                Line((7.5, -4.5), (7.5, -3))
                Line((4, -3), (7.5, -3))
                Line((4, -3), (4, -4.5))
            make_face()
            # Profile area: 34.5, perimeter: 34
            with BuildLine():
                Line((4, -3), (7.5, -3))
                Line((7.5, -3), (7.5, -1.5))
                Line((7.5, -1.5), (4, -1.5))
                Line((4, -1.5), (4, 1.5))
                Line((4, 1.5), (7.5, 1.5))
                Line((7.5, 1.5), (7.5, 3))
                Line((4, 3), (7.5, 3))
                Line((0, 3), (4, 3))
                Line((0, 3), (0, -3))
                Line((0, -3), (4, -3))
            make_face()
            # Profile area: 5.25, perimeter: 10
            with BuildLine():
                Line((4, 3), (7.5, 3))
                Line((7.5, 3), (7.5, 4.5))
                Line((7.5, 4.5), (4, 4.5))
                Line((4, 3), (4, 4.5))
            make_face()
        # TwoSides extrude (symmetric), distance=0.7475
        extrude(amount=0.7475, both=True)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.7475, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((-2, -1.5)):
                Circle(0.5)
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            with Locations((-2, 1.5)):
                Circle(0.5)
        # OneSide extrude, distance=-1.5
        extrude(amount=-1.5, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical belt or band with an oval/elliptical cross-section, featuring a textured or ribbed inner surface and smooth outer surface, designed for power transmission or fastening applications.
def model_24131_3ea7d5a8_0000():
    """Model: Shoulder Fitting v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 9.5007652331, perimeter: 59.8473400509
            with BuildLine():
                CenterArc((0, 0), 4.92125, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 4.60375, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.15875
        extrude(amount=0.15875)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))) as sk:
            # Profile area: 4.3649649843, perimeter: 58.7855118177
            with BuildLine():
                CenterArc((0, 0), 4.752254788, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 4.60375, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # TwoSides extrude, along=-0.3175, against=1.27
        extrude(amount=-0.3175, mode=Mode.ADD)
        extrude(sk.sketch, amount=1.27, mode=Mode.ADD)
    return part.part


# Description: This is a U-shaped metal bracket or clamp with two vertical flanges on each end and a curved base, designed to secure or hold cylindrical objects or components in place.
def model_24131_3ea7d5a8_0001():
    """Model: Centering Ring v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 15 constraints, 10 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1341543239, perimeter: 2.0076332144
            with BuildLine():
                Line((1.6288709326, -4.4752861065), (1.6831666303, -4.62446231))
                CenterArc((0, 0), 4.7625, -80, 10)
                Line((0.8269994461, -4.6901469237), (0.8545660943, -4.8464851545))
                CenterArc((0, 0), 4.92125, -80, 10)
            make_face()
            # Profile area: 0.1341543239, perimeter: 2.0076332144
            with BuildLine():
                CenterArc((0, 0), 4.7625, 100, 10)
                Line((-0.8269994461, 4.6901469237), (-0.8545660943, 4.8464851545))
                CenterArc((0, 0), 4.92125, 100, 10)
                Line((-1.6288709326, 4.4752861065), (-1.6831666303, 4.62446231))
            make_face()
            # Profile area: 0.1341543239, perimeter: 2.0076332144
            with BuildLine():
                CenterArc((0, 0), 4.92125, -110, 10)
                Line((-0.8269994461, -4.6901469237), (-0.8545660943, -4.8464851545))
                CenterArc((0, 0), 4.7625, -110, 10)
                Line((-1.6288709326, -4.4752861065), (-1.6831666303, -4.62446231))
            make_face()
            # Profile area: 0.1341543239, perimeter: 2.0076332144
            with BuildLine():
                Line((0.8269994461, 4.6901469237), (0.8545660943, 4.8464851545))
                CenterArc((0, 0), 4.7625, 70, 10)
                Line((1.6288709326, 4.4752861065), (1.6831666303, 4.62446231))
                CenterArc((0, 0), 4.92125, 70, 10)
            make_face()
        # OneSide extrude, distance=5.08
        extrude(amount=5.08)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.8295556601, perimeter: 60.8447957184
            with BuildLine():
                CenterArc((0, 0), 4.92125, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 4.7625, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.635
        extrude(amount=0.635, mode=Mode.ADD)
    return part.part


# Description: This is a connector or coupling component with a hexagonal/tapered threaded head on one end and a rectangular socket or cavity on the other, featuring a slotted opening and ribbed texture on the upper surface.
def model_24131_3ea7d5a8_0009():
    """Model: Bearing Rack v2 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 4 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.6341760793, perimeter: 8.8773554409
            with BuildLine():
                CenterArc((0, 0), 0.777875, -35.2812592429, 250.5625184858)
                CenterArc((0, 0), 0.777875, -144.7187407571, 109.4374815142)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.635, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            # Profile area: 1.9593999074, perimeter: 6.3021891651
            with BuildLine():
                CenterArc((0, 0), 0.777875, -144.7187407571, 109.4374815142)
                Line((-0.6350000203, -2.2225), (-0.6350000203, -0.4492933228))
                Line((0.6350000203, -2.2225), (-0.6350000203, -2.2225))
                Line((0.6350000203, -0.4492933228), (0.6350000203, -2.2225))
            make_face()
        # OneSide extrude, distance=0.635
        extrude(amount=0.635)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 6 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 2.2225), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0197932609, perimeter: 0.4987278338
            with Locations((-0.3175, 0.3175)):
                Circle(0.079375)
            # Profile area: 0.0197932609, perimeter: 0.4987278338
            with Locations((0.3175, 0.3175)):
                Circle(0.079375)
        # OneSide extrude, distance=-0.508
        extrude(amount=-0.508, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical pen or stylus with a long, slender shaft and a tapered tip at the top end.
def model_24131_3ea7d5a8_0013():
    """Model: Motion Piston v3 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0197932609, perimeter: 0.4987278338
            Circle(0.079375)
        # OneSide extrude, distance=1.80975
        extrude(amount=1.80975)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 1.80975, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0049483152, perimeter: 0.2493639169
            Circle(0.0396875)
        # OneSide extrude, distance=0.15875
        extrude(amount=0.15875, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical mesh or perforated filter/strainer component with an open top and bottom, featuring a uniform pattern of vertical slots or perforations across its curved walls.
def model_24131_3ea7d5a8_0016():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude2 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 81.0732018304, perimeter: 31.9185823791
            Circle(5.0800001621)
        # OneSide extrude, distance=10.16
        extrude(amount=10.16)

        # Sketch2 -> Extrude3 (Cut)
        # Sketch on XY construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.7125573925, perimeter: 2.9923670025
            with Locations((0, 6.3500002027)):
                Circle(0.47625)
        # Symmetric extrude, each_side=10.16
        extrude(amount=10.16, both=True, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical sleeve or barrel component with a notched opening at the top, featuring vertical ribbing or fluting along its outer surface for structural reinforcement and a slightly tapered design.
def model_24131_3ea7d5a8_0017():
    """Model: Rocket Tube Shoulder v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 4.8295556601, perimeter: 60.8447957184
            with BuildLine():
                CenterArc((0, 0), 4.92125, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 4.7625, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=7.62
        extrude(amount=7.62)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.6333843489, perimeter: 3.264911335
            with BuildLine():
                Line((-0.635, 7.62), (0.635, 7.62))
                CenterArc((0, 7.62), 0.635, 180, 180)
            make_face()
        # Symmetric extrude, each_side=7.62
        extrude(amount=7.62, both=True, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical mesh or perforated filter element with a closed bottom, open top with a central oval hole, and vertical slot patterns on the sides, designed for fluid filtration or ventilation applications.
def model_24131_3ea7d5a8_0021():
    """Model: Motion Piston Cap v1 (1)"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0387947914, perimeter: 0.6982189673
            Circle(0.111125)
        # OneSide extrude, distance=0.22225
        extrude(amount=0.22225)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.22225, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.0049483152, perimeter: 0.2493639169
            Circle(0.0396875)
        # OneSide extrude, distance=-0.15875
        extrude(amount=-0.15875, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cutting tool holder or boring bar featuring a cylindrical dark gray shaft with a blue polygonal indexable insert head at one end, designed for precision machining operations.
def model_24146_08d7c016_0003():
    """Model: SCREW M8 v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.2470765814, perimeter: 4.1569219382
            with BuildLine():
                Line((0.3464101615, 0.6), (-0.3464101615, 0.6))
                Line((-0.3464101615, 0.6), (-0.692820323, 0))
                Line((-0.692820323, 0), (-0.3464101615, -0.6))
                Line((-0.3464101615, -0.6), (0.3464101615, -0.6))
                Line((0.3464101615, -0.6), (0.692820323, 0))
                Line((0.692820323, 0), (0.3464101615, 0.6))
            make_face()
        # OneSide extrude, distance=0.6
        extrude(amount=0.6)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.6), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.4869458874, perimeter: 2.4736900554
            Circle(0.3937)
        # OneSide extrude, distance=4.191
        extrude(amount=4.191, mode=Mode.ADD)
    return part.part


# Description: This is a gear or pulley wheel with a large central hub hole, featuring a broad flat face with a mesh or textured pattern on its outer rim edge.
def model_24157_49bf3a04_0001():
    """Model: wheel 1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 2 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 1.5707963268, perimeter: 6.2831853072
            with BuildLine():
                CenterArc((0, 0), 0.75, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.25, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 2 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.5), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.5026548246, perimeter: 10.0530964915
            with BuildLine():
                CenterArc((0, 0), 0.85, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 0.75, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=-0.5
        extrude(amount=-0.5, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical standoff or spacer with a hexagonal base, featuring a hollow cylindrical shaft mounted on a geometric hexagonal or polygonal mounting foot.
def model_24157_49bf3a04_0006():
    """Model: vertical shaft"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 5 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.36, perimeter: 2.4
            with BuildLine():
                Line((0, 0.6), (0, 0))
                Line((0, 0), (0.6, 0))
                Line((0.6, 0), (0.6, 0.6))
                Line((0.6, 0.6), (0, 0.6))
            make_face()
        # OneSide extrude, distance=0.3
        extrude(amount=0.3)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 5 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0.3, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1963495408, perimeter: 1.5707963268
            with Locations((-0.3, -0.3)):
                Circle(0.25)
        # OneSide extrude, distance=1
        extrude(amount=1, mode=Mode.ADD)
    return part.part


# Description: This is a cylindrical sleeve or spacer with a flat circular end face on the left and a textured/ribbed surface on the right, featuring a rounded end cap and horizontal linear surface details.
def model_24164_bb49fff8_0000():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch2 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 153.9380400259, perimeter: 43.9822971503
            Circle(7)
        # OneSide extrude, distance=15
        extrude(amount=15)

        # Sketch3 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, 1), z_dir=(-1, 0, 0))):
            # Profile area: 1.7671458676, perimeter: 4.7123889804
            with Locations((-3.7228131294, 2.9173989296)):
                Circle(0.75)
        # OneSide extrude, distance=-1.5
        extrude(amount=-1.5, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical rod or pin with a smooth, uniform circular cross-section and slightly tapered or rounded ends, featuring a simple elongated shaft design.
def model_24195_9791f5d3_0002():
    """Model: Featuring Shaft"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.1256637061, perimeter: 1.2566370614
            Circle(0.2)
        # Symmetric extrude, each_side=2.53
        extrude(amount=2.53, both=True)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 2.53), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 0.0490873852, perimeter: 0.7853981634
            Circle(0.125)
        # OneSide extrude, distance=-0.6
        extrude(amount=-0.6, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a sheet metal enclosure or channel cover with a rectangular, tapered box shape featuring three circular holes along its front face and a hinged or removable top flange.
def model_24206_28ebcfe4_0002():
    """Model: Plate rail"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.8), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 11.1517699835, perimeter: 21.6548667765
            with BuildLine():
                Line((5, 0), (3, 0))
                Line((5, 6), (5, 0))
                Line((3, 6), (5, 6))
                Line((3, 0), (3, 6))
            make_face()
            with BuildLine():
                CenterArc((4, 5), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((4, 2.5), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((4, 1), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 4 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 1.3), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 6, perimeter: 14
            with BuildLine():
                Line((6, 0), (5, 0))
                Line((6, 6), (6, 0))
                Line((5, 6), (6, 6))
                Line((5, 0), (5, 6))
            make_face()
            # Profile area: 6, perimeter: 14
            with BuildLine():
                Line((3, 6), (3, 0))
                Line((2, 6), (3, 6))
                Line((2, 0), (2, 6))
                Line((3, 0), (2, 0))
            make_face()
            # Profile area: 11.1517699835, perimeter: 21.6548667765
            with BuildLine():
                Line((5, 0), (5, 6))
                Line((3, 6), (5, 6))
                Line((3, 6), (3, 0))
                Line((5, 0), (3, 0))
            make_face()
            with BuildLine():
                CenterArc((4, 1), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((4, 2.5), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
            with BuildLine():
                CenterArc((4, 5), 0.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)
    return part.part


# Description: This is a computer tower or server chassis with a tall, rectangular profile featuring a dark front panel, light blue side panels, and a sloped top section with ventilation slots and a small display window.
def model_24221_0b711dbf_0006():
    """Model: statecznik"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 22.9632336369, perimeter: 19.8703173837
            with BuildLine():
                Line((-0.0644992057, 7.2614566636), (-0.7440103675, 2.5))
                CenterArc((-0.5594840905, 7.3320963392), 0.5, -8.1218835471, 98.1218835471)
                Line((-2.5245076367, 7.8320963392), (-0.5594840905, 7.8320963392))
                CenterArc((-2.5245076367, 6.8320963392), 1, 90, 58.9734708886)
                Line((-6.2971826945, 2.5), (-3.3814363724, 7.3475312448))
                Line((-0.7440103675, 2.5), (-6.2971826945, 2.5))
            make_face()
        # Symmetric extrude, each_side=0.8
        extrude(amount=0.8, both=True)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 2.5, 0), x_dir=(1, 0, 0), z_dir=(0, -1, 0))):
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((0, 5.4000000805)):
                Circle(0.15)
        # OneSide extrude, distance=0.5
        extrude(amount=0.5, mode=Mode.ADD)
    return part.part


# Description: This is a rounded rectangular enclosure or housing with a predominantly solid body, featuring curved edges, mesh or ventilation panels on the sides and top, and an overall compact, box-like form factor typical of an electronic device casing or equipment cover.
def model_24221_0b711dbf_0007():
    """Model: dziob"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on BRepFace
        # Sketch has 18 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 22), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 24.1415930261, perimeter: 18.2831854562
            with BuildLine():
                CenterArc((-1.5, 1.5), 1, 90, 90)
                Line((-2.5, 1.5), (-2.5000000373, -1.5000000373))
                CenterArc((-1.5000000373, -1.5000000373), 1, 180, 90)
                Line((-1.5000000373, -2.5000000373), (1.5000000373, -2.5000000373))
                CenterArc((1.5000000373, -1.5000000373), 1, -90, 90)
                Line((2.5000000373, -1.5000000373), (2.5, 1.5))
                CenterArc((1.5, 1.5), 1, 0, 90)
                Line((1.5, 2.5), (-1.5, 2.5))
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2)
    return part.part


# Description: This is a elongated hexagonal or coffin-shaped housing or enclosure with a tapered design, featuring an open central cavity or channel running along its length, angled side walls, and a raised section at one end.
def model_24230_636208ab_0002():
    """Model: Untitled"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on YZ construction plane
        # Sketch has 25 constraints, 5 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 31.7265014307, perimeter: 30.0496187093
            with BuildLine():
                Line((1.6445412588, 2.5166978747), (-1.2723356033, 2.5166978747))
                CenterArc((-1.2723356033, 1.5166978747), 1, 90, 8.3102771675)
                Line((-1.4168692936, 2.5061977546), (-6.8968325814, 1.7057536788))
                CenterArc((-6.8679258433, 1.5078537028), 0.2, 98.3102771675, 90)
                Line((-7.0658258193, 1.4789469648), (-6.9171086856, 0.460806588))
                CenterArc((-6.6796287145, 0.4954946736), 0.24, -171.6897228325, 61.871051243)
                Line((-6.7609993986, 0.2697097942), (-6.0520606118, 0.0142151206))
                CenterArc((-5.9706899277, 0.24), 0.24, -109.8186715895, 19.8186715895)
                Line((-5.9706899277, 0), (5.2337717768, 0))
                CenterArc((5.2337717768, 0.24), 0.24, -90, 66.1157849778)
                Line((5.4532195057, 0.1428264733), (6.2455669651, 1.9321908852))
                CenterArc((5.7883841966, 2.1346357325), 0.5, -23.8842150222, 103.9372270856)
                Line((5.8747526591, 2.6271197309), (2.4070528622, 3.2352611132))
                CenterArc((2.3552317848, 2.9397707141), 0.3, 80.0530120634, 76.0627729144)
                Line((2.0809221237, 3.0612376225), (1.9188509199, 2.6952309663))
                CenterArc((1.6445412588, 2.8166978747), 0.3, -90, 66.1157849778)
            make_face()
        # Symmetric extrude, each_side=2
        extrude(amount=2, both=True)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on YZ construction plane
        # Sketch has 4 constraints (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 8.8279643192, perimeter: 13.086768413
            with BuildLine():
                Line((-1.2049473227, 2.9596105451), (-1.4339173129, 1.9384678812))
                Line((-1.4339173129, 1.9384678812), (-2.8432387655, 1.7129841007))
                Line((-2.8432387655, 1.7129841007), (-2.6677092852, 0.615887619))
                Line((-2.6677092852, 0.615887619), (1.4194193994, 0.615887619))
                Line((1.4194193994, 0.615887619), (1.811503523, 1.9944803946))
                Line((1.811503523, 2.9596105451), (1.811503523, 1.9944803946))
                Line((-1.2049473227, 2.9596105451), (1.811503523, 2.9596105451))
            make_face()
        # Symmetric extrude, each_side=1.6
        extrude(amount=1.6, both=True, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical dowel pin or shaft with a slightly rounded end on one side and a flat or tapered end on the other, featuring a smooth, uniform cylindrical body with no holes or additional features.
def model_24248_1cfc202d_0006():
    """Model: Eixo Inferior"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 0.7853981634, perimeter: 3.1415926536
            Circle(0.5)
        # OneSide extrude, distance=5
        extrude(amount=5)

        # Sketch6 -> Extrude5 (Cut)
        # Sketch on YZ construction plane
        # Sketch has 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.0706858347, perimeter: 0.9424777961
            with Locations((-2.3000000343, 0)):
                Circle(0.15)
        # TwoSides extrude (symmetric), distance=0.5
        extrude(amount=0.5, both=True, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical rod or shaft with a slight taper, featuring a smooth, elongated body with rounded ends.
def model_24284_3710e946_0006():
    """Model: manette_D‚faut v1"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.291863508, perimeter: 1.9151148816
            Circle(0.3048)
        # TwoSides extrude (symmetric), distance=4.4958
        extrude(amount=4.4958, both=True)

        # Sketch2 -> Extrude2 (Join)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 4.4958, 0), x_dir=(-1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.1297171146, perimeter: 1.2767432544
            Circle(0.2032)
        # OneSide extrude, distance=0.508
        extrude(amount=0.508, mode=Mode.ADD)
    return part.part


# Description: This is a angular, box-like structural component with an irregular polygonal shape, featuring multiple planar surfaces, triangulated sections, and rectangular cutouts or slots on its faces, designed as a lightweight frame or bracket assembly.
def model_24284_3710e946_0007():
    """Model: Bati_D‚faut v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 10 constraints, 21 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 14.1116071412, perimeter: 23.8073156891
            with BuildLine():
                Line((3.0226, 0), (4.4196, 0))
                Line((4.4196, 0), (4.4196, 3.2004))
                Line((4.199156714, 3.3906482744), (4.4196, 3.2004))
                Line((3.487956714, 3.3906482744), (4.199156714, 3.3906482744))
                Line((3.487956714, 4.0002482744), (3.487956714, 3.3906482744))
                Line((-0.499843286, 4.0002482744), (3.487956714, 4.0002482744))
                Line((-0.499843286, 3.3906482744), (-0.499843286, 4.0002482744))
                Line((-1.388843286, 3.3906482744), (-0.499843286, 3.3906482744))
                Line((-1.0922, 0), (-1.388843286, 3.3906482744))
                Line((0, 0), (-1.0922, 0))
                Line((0, 0), (0, 2.0066))
                CenterArc((0.508, 2.0066), 0.508, 90, 90)
                Line((0.508, 2.5146), (2.5146, 2.5146))
                CenterArc((2.5146, 2.0066), 0.508, 0, 90)
                Line((3.0226, 2.0066), (3.0226, 0))
            make_face()
        # OneSide extrude, distance=2.794
        extrude(amount=2.794)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(4.4196, 0, 0), x_dir=(0, 0, -1), z_dir=(1, 0, 0))):
            # Profile area: 0.3693897523, perimeter: 2.1545042418
            with Locations((-1.397, 0.9906)):
                Circle(0.3429)
        # OneSide extrude, distance=-2.032
        extrude(amount=-2.032, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a square or rectangular mounting plate with a parallelogram-like 3D shape featuring a central elliptical hole and reinforcing ribs or flanges on the underside for structural support.
def model_24284_3710e946_0008():
    """Model: PLAQUE 2_D‚faut v4"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XY construction plane
        # Sketch has 7 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 22.064472, perimeter: 19.2024
            with BuildLine():
                Line((-2.8956, 1.905), (2.8956, 1.905))
                Line((-2.8956, -1.905), (-2.8956, 1.905))
                Line((2.8956, -1.905), (-2.8956, -1.905))
                Line((2.8956, 1.905), (2.8956, -1.905))
            make_face()
        # OneSide extrude, distance=0.508
        extrude(amount=0.508)

        # Sketch2 -> Extrude2 (Cut)
        # Sketch on BRepFace
        # Sketch has 1 constraints, 3 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0.508), x_dir=(1, 0, 0), z_dir=(0, 0, 1))):
            # Profile area: 2.0111219845, perimeter: 5.0271765643
            Circle(0.8001)
        # OneSide extrude, distance=-1.778
        extrude(amount=-1.778, mode=Mode.SUBTRACT)
    return part.part


# Description: This is a cylindrical rod or shaft with a long, slender tubular body and rounded ends, featuring a uniform diameter throughout its length.
def model_24284_3710e946_0012():
    """Model: ax4_D‚faut v2"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 1 constraints, 1 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 0.7707020757, perimeter: 3.1120616826
            Circle(0.4953)
        # OneSide extrude, distance=9.8044
        extrude(amount=9.8044)
    return part.part


# Description: This is a cylindrical pipe or sleeve with a smooth tubular body and threaded ends on both sides, featuring a longer central section with a slightly larger diameter than the threaded portions.
def model_24355_99bf3f8f_0000():
    """Model: Base"""
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
        # Sketch has 2 constraints, 2 dimensions (parametric, not converted)
        with BuildSketch(Plane.XY):
            # Profile area: 3.0159289474, perimeter: 30.1592894745
            with BuildLine():
                CenterArc((0, 0), 2.5, 0, 360)
            make_face()
            with BuildLine():
                CenterArc((0, 0), 2.3, 0, 360)
            make_face(mode=Mode.SUBTRACT)
        # OneSide extrude, distance=15
        extrude(amount=15)
    return part.part


# Description: This is a hexagonal or polygonal connector block featuring a complex geometric structure with multiple triangulated faces, internal geometric divisions, and a stepped or offset design that creates an asymmetrical, angular profile suitable for mechanical assembly or structural applications.
def model_24412_a8e106be_0002():
    """Model: Motorblock"""
    with BuildPart() as part:
        # Sketch1 -> Extrude1 (NewBody)
        # Sketch on XZ construction plane
        # Sketch has 7 constraints, 8 dimensions (parametric, not converted)
        with BuildSketch(Plane(origin=(0, 0, 0), x_dir=(1, 0, 0), z_dir=(0, 1, 0))):
            # Profile area: 16.82, perimeter: 19.384971769
            with BuildLine():
                Line((4, 3), (2.1, 3))
                Line((4, 6.2), (4, 3))
                Line((1.2, 6.2), (4, 6.2))
                Line((0, 2.4), (1.2, 6.2))
                Line((0, 0), (0, 2.4))
                Line((2.1, 0), (0, 0))
                Line((2.1, 3), (2.1, 0))
            make_face()
        # OneSide extrude, distance=2
        extrude(amount=2)
    return part.part


MODELS = {
    "model_22430_c6f08b03_0030": {"func": model_22430_c6f08b03_0030, "volume": 1.0853582995, "area": 18.0043301473},
    "model_22430_c6f08b03_0036": {"func": model_22430_c6f08b03_0036, "volume": 1.8280952844, "area": 23.6394240223},
    "model_22433_9f17ac4c_0003": {"func": model_22433_9f17ac4c_0003, "volume": 1.1962417316, "area": 12.8174433785},
    "model_22447_4062c6cb_0007": {"func": model_22447_4062c6cb_0007, "volume": 3.2621108227, "area": 43.4814851006},
    "model_22447_4062c6cb_0009": {"func": model_22447_4062c6cb_0009, "volume": 0.1957173837, "area": 2.6958827302},
    "model_22454_f707c2e5_0000": {"func": model_22454_f707c2e5_0000, "volume": 0.4796440419, "area": 6.7480373998},
    "model_22457_a6c2776f_0006": {"func": model_22457_a6c2776f_0006, "volume": 2.7424107645, "area": 15.2319284061},
    "model_22457_a6c2776f_0008": {"func": model_22457_a6c2776f_0008, "volume": 0.3722108784, "area": 4.8239415443},
    "model_22524_0be3da8a_0012": {"func": model_22524_0be3da8a_0012, "volume": 1.7550775441, "area": 15.1060920705},
    "model_22534_e899f645_0009": {"func": model_22534_e899f645_0009, "volume": 0.7566746907, "area": 5.6846245311},
    "model_22543_684108ff_0009": {"func": model_22543_684108ff_0009, "volume": 0.5488480125, "area": 6.8780679122},
    "model_22606_f1813fe7_0000": {"func": model_22606_f1813fe7_0000, "volume": 0.1931964877, "area": 2.1885400053},
    "model_22608_c4bce8da_0000": {"func": model_22608_c4bce8da_0000, "volume": 0.0800878424, "area": 1.3802521978},
    "model_22624_7af10d7d_0001": {"func": model_22624_7af10d7d_0001, "volume": 1.0406844061, "area": 11.1206063048},
    "model_22624_7af10d7d_0004": {"func": model_22624_7af10d7d_0004, "volume": 4.6935394245, "area": 24.7557501103},
    "model_22645_1ba0af00_0006": {"func": model_22645_1ba0af00_0006, "volume": 291.6285574237, "area": 465.0570686959},
    "model_22666_bdaa1303_0009": {"func": model_22666_bdaa1303_0009, "volume": 0.601643207, "area": 8.3797234216},
    "model_22666_bdaa1303_0018": {"func": model_22666_bdaa1303_0018, "volume": 0.1432992398, "area": 4.7406436988},
    "model_22670_9353c710_0000": {"func": model_22670_9353c710_0000, "volume": 0.0655807466, "area": 1.1623892818},
    "model_22670_9353c710_0001": {"func": model_22670_9353c710_0001, "volume": 0.0612610567, "area": 1.0053096491},
    "model_22711_33843a5d_0006": {"func": model_22711_33843a5d_0006, "volume": 137.8395795756, "area": 224.6472910944},
    "model_22719_67a50d6f_0005": {"func": model_22719_67a50d6f_0005, "volume": 0.324, "area": 2.88},
    "model_22719_67a50d6f_0008": {"func": model_22719_67a50d6f_0008, "volume": 0.4981849178, "area": 5.6433109209},
    "model_22742_3c107495_0015": {"func": model_22742_3c107495_0015, "volume": 25.7432274135, "area": 121.8335476509},
    "model_22751_90a6225a_0001": {"func": model_22751_90a6225a_0001, "volume": 37.19359263, "area": 223.9179395371},
    "model_22756_fc3fdda5_0020": {"func": model_22756_fc3fdda5_0020, "volume": 1.2917716706, "area": 20.131251686},
    "model_22756_fc3fdda5_0030": {"func": model_22756_fc3fdda5_0030, "volume": 0.4828720275, "area": 8.3218294793},
    "model_22756_fc3fdda5_0031": {"func": model_22756_fc3fdda5_0031, "volume": 2.1967510531, "area": 32.5617485167},
    "model_22768_620b0a0b_0006": {"func": model_22768_620b0a0b_0006, "volume": 2.3145683875, "area": 10.8384946549},
    "model_22772_2b5f6629_0003": {"func": model_22772_2b5f6629_0003, "volume": 88.6648008661, "area": 185.1020190419},
    "model_22787_49022c32_0007": {"func": model_22787_49022c32_0007, "volume": 118.8690933628, "area": 181.1586471918},
    "model_22788_b6a9e30a_0001": {"func": model_22788_b6a9e30a_0001, "volume": 7148.0475688726, "area": 9980.2920367321},
    "model_22788_b6a9e30a_0008": {"func": model_22788_b6a9e30a_0008, "volume": 4826.25, "area": 6775.5},
    "model_22848_cc91b848_0005": {"func": model_22848_cc91b848_0005, "volume": 1122.9040736722, "area": 1555.7749709992},
    "model_22848_cc91b848_0008": {"func": model_22848_cc91b848_0008, "volume": 1420.0189688924, "area": 1619.4483023746},
    "model_22848_cc91b848_0030": {"func": model_22848_cc91b848_0030, "volume": 777.3362110587, "area": 1448.2111343489},
    "model_22998_00817368_0005": {"func": model_22998_00817368_0005, "volume": 815.0469440657, "area": 734.6680866395},
    "model_22998_00817368_0006": {"func": model_22998_00817368_0006, "volume": 2166.1281346502, "area": 1210.7344271095},
    "model_23025_02ad81fe_0000": {"func": model_23025_02ad81fe_0000, "volume": 0.0881630919, "area": 1.8206034203},
    "model_23044_9a964a68_0006": {"func": model_23044_9a964a68_0006, "volume": 29.4281009343, "area": 127.8929677242},
    "model_23044_9a964a68_0009": {"func": model_23044_9a964a68_0009, "volume": 6.8298, "area": 72.9914213562},
    "model_23049_207a41f0_0005": {"func": model_23049_207a41f0_0005, "volume": 56.5486677646, "area": 89.5353906273},
    "model_23049_207a41f0_0006": {"func": model_23049_207a41f0_0006, "volume": 1.9229396315, "area": 10.5046090377},
    "model_23104_3b70eba4_0003": {"func": model_23104_3b70eba4_0003, "volume": 0.5941592654, "area": 7.286990817},
    "model_23132_1847c4ef_0002": {"func": model_23132_1847c4ef_0002, "volume": 66.2574654364, "area": 168.849461118},
    "model_23132_1847c4ef_0006": {"func": model_23132_1847c4ef_0006, "volume": 158.1934441012, "area": 197.6194216597},
    "model_23132_1847c4ef_0009": {"func": model_23132_1847c4ef_0009, "volume": 48.2548631591, "area": 168.892021057},
    "model_23137_e55b73cb_0013": {"func": model_23137_e55b73cb_0013, "volume": 7.68143625, "area": 54.8386},
    "model_23138_630f02f9_0001": {"func": model_23138_630f02f9_0001, "volume": 7200, "area": 2240},
    "model_23144_88ca00a5_0007": {"func": model_23144_88ca00a5_0007, "volume": 2064.770064, "area": 6667.7286},
    "model_23144_88ca00a5_0008": {"func": model_23144_88ca00a5_0008, "volume": 527.401267776, "area": 3157.929168},
    "model_23144_88ca00a5_0010": {"func": model_23144_88ca00a5_0010, "volume": 14352.8797371633, "area": 16810.9229013472},
    "model_23206_b99a5251_0045": {"func": model_23206_b99a5251_0045, "volume": 1.0500001058, "area": 21.9907966969},
    "model_23231_efe613bb_0008": {"func": model_23231_efe613bb_0008, "volume": 9.6301788204, "area": 39.6633386447},
    "model_23231_efe613bb_0010": {"func": model_23231_efe613bb_0010, "volume": 3.4726035875, "area": 15.5711069739},
    "model_23231_efe613bb_0017": {"func": model_23231_efe613bb_0017, "volume": 1.4121458978, "area": 11.7338485612},
    "model_23231_efe613bb_0021": {"func": model_23231_efe613bb_0021, "volume": 0.1539773099, "area": 3.8140505611},
    "model_23255_972fbfe6_0011": {"func": model_23255_972fbfe6_0011, "volume": 54.6741681301, "area": 167.3945995442},
    "model_23258_87a2ba81_0005": {"func": model_23258_87a2ba81_0005, "volume": 432.3978455071, "area": 484.6011537118},
    "model_23264_20be13a0_0006": {"func": model_23264_20be13a0_0006, "volume": 1.8238860503, "area": 21.9047679038},
    "model_23264_20be13a0_0008": {"func": model_23264_20be13a0_0008, "volume": 0.4330122981, "area": 3.4640991924},
    "model_23264_20be13a0_0010": {"func": model_23264_20be13a0_0010, "volume": 0.232896625, "area": 4.9104027342},
    "model_23264_20be13a0_0011": {"func": model_23264_20be13a0_0011, "volume": 0.7093740505, "area": 13.0882114096},
    "model_23269_7c2afd7f_0002": {"func": model_23269_7c2afd7f_0002, "volume": 11.3008095057, "area": 53.9535181964},
    "model_23331_192866b6_0001": {"func": model_23331_192866b6_0001, "volume": 157.3184489901, "area": 242.073409607},
    "model_23410_0163b27d_0005": {"func": model_23410_0163b27d_0005, "volume": 0.2736504528, "area": 3.0113274752},
    "model_23410_0163b27d_0009": {"func": model_23410_0163b27d_0009, "volume": 0.0824668072, "area": 3.4086280291},
    "model_23422_f214bd4d_0000": {"func": model_23422_f214bd4d_0000, "volume": 0.8351052836, "area": 5.9692265146},
    "model_23449_3f3d53b6_0000": {"func": model_23449_3f3d53b6_0000, "volume": 111.1370245848, "area": 494.6741394504},
    "model_23472_ed1faab6_0002": {"func": model_23472_ed1faab6_0002, "volume": 250.158773875, "area": 387.1264390447},
    "model_23493_57512264_0001": {"func": model_23493_57512264_0001, "volume": 0.215, "area": 9.28},
    "model_23493_57512264_0004": {"func": model_23493_57512264_0004, "volume": 46.7562260554, "area": 128.8703933419},
    "model_23493_57512264_0009": {"func": model_23493_57512264_0009, "volume": 0.3051630704, "area": 6.2375029817},
    "model_23554_a0845d54_0001": {"func": model_23554_a0845d54_0001, "volume": 105.6784501287, "area": 296.9869604981},
    "model_23554_a0845d54_0009": {"func": model_23554_a0845d54_0009, "volume": 91.8915851175, "area": 293.3462140289},
    "model_23554_a0845d54_0010": {"func": model_23554_a0845d54_0010, "volume": 19.2422549734, "area": 76.9690199384},
    "model_23554_a0845d54_0016": {"func": model_23554_a0845d54_0016, "volume": 59.259273176, "area": 105.9541392331},
    "model_23602_5daaccf5_0004": {"func": model_23602_5daaccf5_0004, "volume": 4.1024048507, "area": 24.3702396046},
    "model_23683_72d2534f_0000": {"func": model_23683_72d2534f_0000, "volume": 19.4449766443, "area": 54.0285978513},
    "model_23739_47fb03ab_0000": {"func": model_23739_47fb03ab_0000, "volume": 15.6984822853, "area": 120.3312473315},
    "model_23753_b32a4e2e_0000": {"func": model_23753_b32a4e2e_0000, "volume": 60.5098360703, "area": 167.0084181347},
    "model_23770_f35c1c3b_0008": {"func": model_23770_f35c1c3b_0008, "volume": 3.3578736989, "area": 22.7549190378},
    "model_23774_716b8bc4_0007": {"func": model_23774_716b8bc4_0007, "volume": 4.3982300025, "area": 52.7787574361},
    "model_23775_6d8ee909_0005": {"func": model_23775_6d8ee909_0005, "volume": 27.8368200507, "area": 64.6736401013},
    "model_23775_6d8ee909_0009": {"func": model_23775_6d8ee909_0009, "volume": 40.3116065761, "area": 221.4728499642},
    "model_23876_74957d38_0009": {"func": model_23876_74957d38_0009, "volume": 0.6534311133, "area": 6.693148447},
    "model_23881_bec7f38c_0001": {"func": model_23881_bec7f38c_0001, "volume": 2.3255717069, "area": 21.1916597155},
    "model_23881_bec7f38c_0011": {"func": model_23881_bec7f38c_0011, "volume": 3.3730372545, "area": 26.0092037527},
    "model_23881_bec7f38c_0014": {"func": model_23881_bec7f38c_0014, "volume": 0.4877322595, "area": 16.6818569906},
    "model_23883_040b5fef_0000": {"func": model_23883_040b5fef_0000, "volume": 0.5882632244, "area": 5.3878314009},
    "model_23951_3afdbe1c_0000": {"func": model_23951_3afdbe1c_0000, "volume": 1.5079644687, "area": 21.8497768467},
    "model_23951_3afdbe1c_0001": {"func": model_23951_3afdbe1c_0001, "volume": 33.372, "area": 342.8},
    "model_23956_ee17fe48_0002": {"func": model_23956_ee17fe48_0002, "volume": 190.507659519, "area": 429.9323488213},
    "model_23956_ee17fe48_0015": {"func": model_23956_ee17fe48_0015, "volume": 100.0165291178, "area": 191.6528598322},
    "model_23961_8b0c848b_0000": {"func": model_23961_8b0c848b_0000, "volume": 64.8911767789, "area": 146.4657546911},
    "model_24032_d6172503_0013": {"func": model_24032_d6172503_0013, "volume": 9.0134774899, "area": 62.4026068259},
    "model_24032_d6172503_0023": {"func": model_24032_d6172503_0023, "volume": 0.6525067028, "area": 5.9128739457},
    "model_24032_d6172503_0024": {"func": model_24032_d6172503_0024, "volume": 18.6669508485, "area": 56.1127717839},
    "model_24032_d6172503_0027": {"func": model_24032_d6172503_0027, "volume": 13.4925561426, "area": 64.4154849917},
    "model_24032_d6172503_0032": {"func": model_24032_d6172503_0032, "volume": 7.8913332734, "area": 41.1131573036},
    "model_24032_d6172503_0033": {"func": model_24032_d6172503_0033, "volume": 3.2565582142, "area": 15.7975141488},
    "model_24047_9eb475f0_0007": {"func": model_24047_9eb475f0_0007, "volume": 594.1399688781, "area": 1184.3723441584},
    "model_24056_959fa476_0000": {"func": model_24056_959fa476_0000, "volume": 0.0746296526, "area": 4.2408429882},
    "model_24090_a2bf0d93_0005": {"func": model_24090_a2bf0d93_0005, "volume": 1.5548169961, "area": 17.6106328908},
    "model_24094_a5dcc4fc_0000": {"func": model_24094_a5dcc4fc_0000, "volume": 64.9266594914, "area": 156.0517693806},
    "model_24131_3ea7d5a8_0000": {"func": model_24131_3ea7d5a8_0000, "volume": 7.7446902021, "area": 112.4920957088},
    "model_24131_3ea7d5a8_0001": {"func": model_24131_3ea7d5a8_0001, "volume": 5.452031723, "area": 83.9912751535},
    "model_24131_3ea7d5a8_0009": {"func": model_24131_3ea7d5a8_0009, "volume": 1.6268107985, "area": 13.4459350493},
    "model_24131_3ea7d5a8_0013": {"func": model_24131_3ea7d5a8_0013, "volume": 0.036606399, "area": 0.9817457408},
    "model_24131_3ea7d5a8_0016": {"func": model_24131_3ea7d5a8_0016, "volume": 816.4721039243, "area": 515.3471031004},
    "model_24131_3ea7d5a8_0017": {"func": model_24131_3ea7d5a8_0017, "volume": 36.59967748, "area": 470.9891642392},
    "model_24131_3ea7d5a8_0021": {"func": model_24131_3ea7d5a8_0021, "volume": 0.0078365973, "area": 0.27235527},
    "model_24146_08d7c016_0003": {"func": model_24146_08d7c016_0003, "volume": 2.789036163, "area": 15.3555413481},
    "model_24157_49bf3a04_0001": {"func": model_24157_49bf3a04_0001, "volume": 1.0367255757, "area": 7.6026542217},
    "model_24157_49bf3a04_0006": {"func": model_24157_49bf3a04_0006, "volume": 0.3043495408, "area": 3.0107963268},
    "model_24164_bb49fff8_0000": {"func": model_24164_bb49fff8_0000, "volume": 2306.419881587, "area": 974.6791207762},
    "model_24195_9791f5d3_0002": {"func": model_24195_9791f5d3_0002, "volume": 0.606405922, "area": 7.0811498412},
    "model_24206_28ebcfe4_0002": {"func": model_24206_28ebcfe4_0002, "volume": 17.1517699835, "area": 69.9584067435},
    "model_24221_0b711dbf_0006": {"func": model_24221_0b711dbf_0006, "volume": 36.7765167365, "area": 78.1902139858},
    "model_24221_0b711dbf_0007": {"func": model_24221_0b711dbf_0007, "volume": 48.2831867973, "area": 84.8495580077},
    "model_24230_636208ab_0002": {"func": model_24230_636208ab_0002, "volume": 102.9934858589, "area": 218.1095510673},
    "model_24248_1cfc202d_0006": {"func": model_24248_1cfc202d_0006, "volume": 3.8571036019, "area": 18.0564171629},
    "model_24284_3710e946_0006": {"func": model_24284_3710e946_0006, "volume": 2.6902162124, "area": 18.4522595588},
    "model_24284_3710e946_0007": {"func": model_24284_3710e946_0007, "volume": 38.9117928687, "area": 97.011917239},
    "model_24284_3710e946_0008": {"func": model_24284_3710e946_0008, "volume": 10.1871018079, "area": 52.4153249256},
    "model_24284_3710e946_0012": {"func": model_24284_3710e946_0012, "volume": 7.5562714311, "area": 32.0533017127},
    "model_24355_99bf3f8f_0000": {"func": model_24355_99bf3f8f_0000, "volume": 45.2389342117, "area": 458.4212000118},
    "model_24412_a8e106be_0002": {"func": model_24412_a8e106be_0002, "volume": 33.64, "area": 72.4099435381},
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
