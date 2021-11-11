import numpy as np
import argparse
from ase.io import read, write


parser = argparse.ArgumentParser(description="Write ALM input file from Atoms object of ase.")

parser.add_argument("-a", "--atoms", help="Atoms object file")
parser.add_argument("-f", "--filename", help="alm filename")
parser.add_argument("-p", "--prefix", help="prefix")

args = parser.parse_args()

class elem2ind:
    def __init__(self, kd):
        self.kd = list(kd)

    def main(self, elem):
        return self.kd.index(elem)+1

def ase2alm(atoms, filename, prefix="test"):
    f = open(filename, "w")
    f.write("&general\n")

    f.write("  PREFIX = "+prefix+"\n")
    f.write("  MODE = \n")
    nat = str(atoms.get_global_number_of_atoms())
    f.write("  NAT = "+nat+"\n")
    symbols = atoms.get_chemical_symbols()
    nkd = str(len(np.unique(symbols)))
    f.write("  NKD = "+nkd+"\n")
    kd = np.unique(atoms.get_chemical_symbols())
    f.write("  KD = ")
    for k in kd:
        f.write(k)
        f.write(" ")
    f.write("\n")

    f.write("/\n\n")

    f.write("&interaction\n")
    f.write("  NORDER = 2\n")
    f.write("/\n\n")
    
    cell = np.array(atoms.get_cell())
    f.write("&cell\n")
    f.write("  1.8897261246257702\n")
    f.write("  "+str(cell[0][0])+" "+str(cell[0][1])+" "+str(cell[0][2])+"\n")
    f.write("  "+str(cell[1][0])+" "+str(cell[1][1])+" "+str(cell[1][2])+"\n")
    f.write("  "+str(cell[2][0])+" "+str(cell[2][1])+" "+str(cell[2][2])+"\n")
    f.write("/\n\n")

    f.write("&cutoff\n")
    f.write("  *-* None None\n")
    f.write("/\n\n")

    index_class = elem2ind(kd)
    index = []
    for s in symbols:
        index.append(str(index_class.main(s)))
    index = np.array(index, dtype=str)
    position = atoms.get_scaled_positions()
    position = np.around(position, decimals=3)

    f.write("&position\n")
    for i in range(atoms.get_global_number_of_atoms()):
        f.write("  "+index[i]+" "+str(position[i][0])+" "+str(position[i][1])+" "+str(position[i][2])+"\n")
    f.write("/\n")
    f.close()

if __name__=="__main__":
    atoms = read(args.atoms)
    ase2alm(atoms, args.filename, args.prefix)
