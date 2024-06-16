from pymatgen.core.structure import Structure
from pymatgen.analysis.chemenv.coordination_environments.coordination_geometry_finder import LocalGeometryFinder
from pymatgen.analysis.chemenv.coordination_environments.chemenv_strategies import SimplestChemenvStrategy, \
    MultiWeightsChemenvStrategy
from pymatgen.analysis.chemenv.coordination_environments.structure_environments import LightStructureEnvironments
from pymatgen.analysis.bond_valence import BVAnalyzer

cif_file = 'NaCl.cif'
structure = Structure.from_file(cif_file)
bva = BVAnalyzer()
valences = bva.get_valences(structure)
lgf = LocalGeometryFinder()
lgf.setup_structure(structure=structure)
se = lgf.compute_structure_environments(valences=valences)
strategy = MultiWeightsChemenvStrategy.stats_article_weights_parameters()
lse = LightStructureEnvironments.from_structure_environments(strategy=strategy, structure_environments=se)

for isite, (site,ce) in enumerate(zip(structure, lse.coordination_environments)):
    if ce is not None:
        print(site.species_string+str(isite)+': '+str(ce[0]["ce_symbol"]))