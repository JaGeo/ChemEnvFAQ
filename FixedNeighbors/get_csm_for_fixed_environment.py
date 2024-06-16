from pymatgen.analysis.chemenv.coordination_environments.coordination_geometry_finder import LocalGeometryFinder
from pymatgen.core.structure import Structure
structure=Structure.from_file("NaCl.cif")
structure
print(structure)

_neigh_coords=[structure[1].coords,structure[1].coords+[0.0,0.0,structure.lattice.c], structure[2].coords,structure[2].coords+[0.0,structure.lattice.b,0.0],structure[3].coords, structure[3].coords+[structure.lattice.a,0.0,0.0]]
print(_neigh_coords)
print(len(_neigh_coords))
lgf = LocalGeometryFinder()
lgf.setup_structure(structure=structure)
# you need to make sure to consider periodic boundary conditions
# either choose coordination environments where all atoms or in your cell
# or transform them accordingly
lgf.setup_local_geometry(isite=7, coords=_neigh_coords, optimization=2)
cncgsm = lgf.get_coordination_symmetry_measures(optimization=2)

# get all 6-fold coordination environment keys
for key in cncgsm.keys():
    print(key)

# get the csm for the octahedron:
print(cncgsm["O:6"]["csm_wcs_ctwcc"])

