#!/usr/bin/env python3
import sys

import h5py
import imageio
import numpy


def export_first_frame(in_filepath, out_filepath):
    """
    Parameters
    ----------
    in_filepath : str
        Expects path to HDF5 file with a certain structure
    out_filepath : str
        Expects writeable path to image file, e.g. 'output.png'. Format is
        inferred from file extension.
    """
    with h5py.File(in_filepath, 'r') as file:
        frame0 = file['xpcs']['imgs'][0, ...]
    # Do type conversion manually to minimize lossiness.
    frame0_uint8 = (frame0 / numpy.ptp(frame0) * 255).astype(numpy.uint8)
    imageio.imwrite(out_filepath, frame0_uint8)


if __name__ == '__main__':
    export_first_frame(sys.argv[1], sys.argv[2])
