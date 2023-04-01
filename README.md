# Minimalist Perlin Noise Implementation

This repository contains a minimalist single-file implementation of Perlin Noise in Python.

## Usage

You can use the `noise` function to generate simple Perlin Noise. The input should be the coordinates of the point you want to calculate the noise value for, and the output will be the resulting noise value.

To generate fractal Perlin Noise, use the `perlin` function, which is built on top of `noise` and takes three additional parameters to control the fractal parameters.

To obtain a grid of values, you can use the `give_grid` function, which is based on the `perlin` function. This function returns an `NxN` grid of fractal Perlin Noise values.

Dependencies: NumPy.

## Results

### Varying octaves

| octaves=1             | octaves=2             | octaves=3             |
| --------------------- | --------------------- | --------------------- |
| ![](figures/oct1.png) | ![](figures/oct2.png) | ![](figures/oct3.png) |

### Varying frequency

| frequency=1            | frequency=2            | frequency=3            |
| ---------------------- | ---------------------- | ---------------------- |
| ![](figures/freq1.png) | ![](figures/freq2.png) | ![](figures/freq3.png) |

### Varying persistence

| persistence=0.25           | persistence=0.50           | persistence=0.75           |
| -------------------------- | -------------------------- | -------------------------- |
| ![](figures/pres_0_25.png) | ![](figures/pres_0_50.png) | ![](figures/pres_0_75.png) |


## BibTeX

```
@inbook{10.1145/3571600.3571657
  author = {Jain, Aryamaan and Sharma, Avinash and Rajan, K S},
  title = {Adaptive &amp; Multi-Resolution Procedural Infinite Terrain Generation with Diffusion Models and Perlin Noise},
  year = {2022},
  isbn = {9781450398220},
  publisher = {Association for Computing Machinery},
  address = {New York, NY, USA},
  url = {https://doi.org/10.1145/3571600.3571657},
  booktitle = {Proceedings of the Thirteenth Indian Conference on Computer Vision, Graphics and Image Processing (ICVGIP'22), December 8--10, 2022, Gandhinagar, India},
  articleno = {57},
  numpages = {9}
}
```

