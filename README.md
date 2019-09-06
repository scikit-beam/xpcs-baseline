# xpcs-baseline
MD Generated samples to test XPCS algorithms

## Installation and Usage

### Installation

```bash
git clone --recursive https://github.com/scikit-beam/xpcs-baseline
cd xpcs-baseline
pip install .
```

You will also need [LAMMPS](https://lammps.sandia.gov). On Ubuntu/Debian:

```bash
apt install lammps
```

On OSX:

```bash
brew install lammps
```

### Usage

Run MD simulation. This prodcues data files (ASCII text) in ``data/``

```bash
lammps -in lammps/in.melt
```

Calculate scattering

```bash
python script/calc_scattering.py
```

This produces an HDF5 file, `xpcs00512.h5`. You may use this script to generate
a PNG file with the first frame

```bash
python script/export_first_frame.py xpcs00512.h5 xpcs00512-frame0.png
```

or use any HDF5 application or library to view the output file directly. For
example, using matplotlib:

```python
import h5py
file = h5py.File('xpcs00512.h5', 'r')
frame0 = file['xpcs']['imgs'][0, :, :]
import matplotlib.pyplot as plt
plt.imshow(frame0)
```

### Developer Notes

This project's structure was based on
[the pybind11 CMake example](https://github.com/pybind/cmake_example).
