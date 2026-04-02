import os
import argparse

values = {}

def Val(C):
    return sum(values[c] for c in C)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=str, required=True)
    parser.add_argument("--output", type=str, required=False)
    args = parser.parse_args()

    input_file = args.input
    assert os.path.exists(input_file), "Input file does not exist"
    output_file = args.output

    with open(input_file) as f:
        assert os.stat(input_file).st_size != 0, "Error: input file is empty"
        K = int(f.readline())
        values = {}
        for _ in range(K):
            x, v = f.readline().split()
            v = int(v)
            assert v >= 0, "Values must be non-negative"
            values[x] = v
        A = f.readline()
        for x in A:
            assert x in values, ("Strings can only contain characters from "
                                 "the given alphabet")
        B = f.readline()
        for x in B:
            assert x in values, ("Strings can only contain characters from "
                                 "the given alphabet")

    

    output = ''

    if output_file is not None:
        assert os.path.exists(output_file), "Output file does not exist"
        with open(output_file, 'w') as f:
            f.write(output)
    else:
        print(output)
