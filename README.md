# Fusion 360 Gallery Dataset - build123d Reconstructions

7,683 parametric CAD models from the [Fusion 360 Gallery Reconstruction Dataset](https://github.com/AutodeskAILab/Fusion360GalleryDataset) reconstructed as executable [build123d](https://github.com/gumyr/build123d) Python scripts.

Each model was originally a Fusion 360 sketch-and-extrude sequence. These scripts reproduce the geometry programmatically using build123d's `BuildPart`, `BuildSketch`, and `BuildLine` context managers, with NURBS curves handled via OCP bindings.

**This is a Modified Set** of the Fusion 360 Gallery Dataset. It is not the original dataset. See the [original repository](https://github.com/AutodeskAILab/Fusion360GalleryDataset) for the full dataset including assembly, segmentation, and reconstruction subsets with JSON metadata.

## Structure

Models are bundled into batch files organized by complexity (timeline operation count):

```
01_2ops/       3,161 models   18 batches    2 timeline operations
02_3ops/         833 models    7 batches    3 timeline operations
03_4to5ops/    1,748 models   16 batches    4-5 timeline operations
04_6to7ops/      915 models   11 batches    6-7 timeline operations
05_8to10ops/     618 models   10 batches    8-10 timeline operations
06_11to15ops/    275 models    6 batches    11-15 timeline operations
07_16to20ops/     93 models    3 batches    16-20 timeline operations
08_21plus/        40 models    2 batches    21+ timeline operations
```

Each batch file contains up to ~200 models and stays under 5,000 lines. Every batch file is self-contained and executable.

## Batch File Format

Each batch file contains:

1. **Merged imports** from all models in the batch
2. **Model functions** (`def model_XXXXX():`) that build geometry and return a `TopoDS_Shape`
3. **`MODELS` dict** mapping function names to expected volume and area
4. **`__main__` block** that validates each model against expected measurements

```python
def model_100221_4d7b66c4_0003():
    """Model: Gause Wrap"""
    with BuildPart() as part:
        with BuildSketch(Plane.XY):
            with BuildLine():
                ...
            make_face()
        extrude(amount=7.62)
    return part.part

MODELS = {
    "model_100221_4d7b66c4_0003": {"func": model_100221_4d7b66c4_0003, "volume": 0.3386, "area": 47.8954},
    ...
}
```

## Usage

Install build123d (requires OCP/cadquery-ocp):

```bash
pip install build123d
```

Run a batch to validate all models:

```bash
python 01_2ops/batch_001.py
```

Import individual models:

```python
from importlib import import_module

batch = import_module("01_2ops.batch_001")
shape = batch.model_100221_4d7b66c4_0003()
print(f"Volume: {shape.volume:.4f}")
```

## Relationship to Source Dataset

- **Source**: [Fusion 360 Gallery Reconstruction Dataset v1.0.1](https://github.com/AutodeskAILab/Fusion360GalleryDataset)
- **Scope**: 7,683 of 8,625 reconstruction sequences (the ones that produce valid geometry)
- **Transformation**: Each JSON reconstruction sequence was converted to an equivalent build123d Python script. The JSON metadata files are not included here; refer to the original dataset for those.
- **Naming**: Function names encode the original file ID (e.g., `model_100221_4d7b66c4_0003` corresponds to `100221_4d7b66c4_0003.json` in the reconstruction dataset)
- **Validation**: Each model includes expected volume and surface area from the original Fusion 360 geometry, validated to within 1% tolerance

## Citation

If this dataset contributes to your research, please cite the Fusion 360 Gallery Dataset:

```bibtex
@inproceedings{willis2021fusion,
  title={Fusion 360 Gallery: A Dataset and Environment for Programmatic CAD Construction from Human Design Sequences},
  author={Willis, Karl DD and Pu, Yewen and Luo, Jieliang and Chu, Hang and Du, Tao and Lambourne, Joseph G and Solar-Lezama, Armando and Matusik, Wojciech},
  booktitle={ACM SIGGRAPH},
  year={2021}
}
```

## License

This Modified Set is distributed under the [Fusion 360 Gallery Dataset License](LICENSE.md) for **non-commercial research purposes only**. See [LICENSE.md](LICENSE.md) for full terms.
