#!/usr/bin/env python3

if __name__ == "__main__":
    input_file = open("input", "r").read()
    w=25
    h=6
    n_pixels=w*h
    layers = [input_file[i:i+n_pixels] for i in range(0, len(input_file), n_pixels)]
    counts = [layer.count('0') for layer in layers]
    layer_n = counts.index(min(counts))
    print(layers[layer_n].count('1')*layers[layer_n].count('2'))