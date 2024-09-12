[![INFORMS Journal on Computing Logo](https://INFORMSJoC.github.io/logos/INFORMS_Journal_on_Computing_Header.jpg)](https://pubsonline.informs.org/journal/ijoc)

# Two-Stage Estimation and Variance Modeling for Latency-Constrained Variational Quantum Algorithms

This archive is distributed in association with the [INFORMS Journal on
Computing](https://pubsonline.informs.org/journal/ijoc) under the [MIT License](LICENSE).

The software and data in this repository are a snapshot of the software and data
that were used in the research reported on in the paper 
[Two-Stage Estimation and Variance Modeling for Latency-Constrained Variational Quantum Algorithms](https://doi.org/10.1287/ijoc.2024.0575) by Yunsoo Ha, Sara Shashaani, and Matt Menickelly. 

## Cite

To cite the contents of this repository, please cite both the paper and this repo, using their respective DOIs.

https://doi.org/10.1287/ijoc.2024.0575

https://doi.org/10.1287/ijoc.2024.0575.cd

Below is the BibTex for citing this snapshot of the repository.

```
@misc{Ha2024,
  author =        {Ha, Yunsoo and Shashaani, Sara and Menickelly, Matt},
  publisher =     {INFORMS Journal on Computing},
  title =         {{Two-Stage Estimation and Variance Modeling for Latency-Constrained Variational Quantum Algorithms}},
  year =          {2024},
  doi =           {10.1287/ijoc.2024.0575.cd},
  url =           {https://github.com/INFORMSJoC/2024.0575},
  note =          {Available for download at https://github.com/INFORMSJoC/2024.0575},
}  
```

## Description

The goal of this software is to demonstrate the effect of cache optimization.

## Building

In Linux, to build the version that multiplies all elements of a vector by a
constant (used to obtain the results in [Figure 1](results/mult-test.png) in the
paper), stepping K elements at a time, execute the following commands.

```
make mult
```

Alternatively, to build the version that sums the elements of a vector (used
to obtain the results [Figure 2](results/sum-test.png) in the paper), stepping K
elements at a time, do the following.

```
make clean
make sum
```

Be sure to make clean before building a different version of the code.

## Results

All detailed results are available in [plots](experiments/plots) folder.

## Replicating

To replicate the results presented in the paper, run the code located in the [figures](figures) folder. This will generate the corresponding plots found in the [plots](experiments/plots) folder using the output .pickle files from the [outputs](experiments/outputs) folder. For example, to create Figure 12a, execute the script
'''
python figures/figure12a.py
'''


To replicate these .pickle files, execute the code in the [run](run) folder.

