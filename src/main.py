import os
import argparse

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
        A = f.readline().strip()
        for x in A:
            assert x in values, "Strings can only contain characters from the given alphabet"
        B = f.readline().strip()
        for x in B:
            assert x in values, "Strings can only contain characters from the given alphabet"


    DP = [[0 for _ in range(len(B)+1)] for _ in range(len(A)+1)]
    for i in range(1,len(A)+1):
        for j in range(1,len(B)+1):
            if A[i-1] == B[j-1]:
                DP[i][j] = DP[i-1][j-1] + values[A[i-1]]
            else:
                DP[i][j] = max(DP[i-1][j], DP[i][j-1])


    # BACKTRACKING HERE
    

    output = str(DP[len(A)][len(B)]) + '\n' # + reconstructed subseq

    if output_file is not None:
        with open(output_file, 'w') as f:
            f.write(output)
    else:
        print(output)