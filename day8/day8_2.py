#!/usr/bin/env python3
w=25
h=6
def print_layer(layer):
    for i in range(h):
        print(''.join(layer[i*w:i*w+w]))
    print('')

if __name__ == "__main__":
    input_file = open("input", "r").read()
    n_pixels=w*h
    layers = [input_file[i:i+n_pixels] for i in range(0, len(input_file), n_pixels)]
    final_layer = ["#"]*n_pixels
    for layer in layers:
        for i in range(n_pixels):
            if final_layer[i] == '#':
                if layer[i] == '0': final_layer[i] = " "
                if layer[i] == '1': final_layer[i] = "■"    
        print_layer(final_layer)
