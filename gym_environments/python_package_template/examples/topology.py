from gym_environments.optimizers.concrete_opt import ConcreteOptimizer, ConcreteStrategy
from gym_environments.optimizers.params_opt import ParametersOptimizer
from gym_environments.optimizers.topo_opt import TopologyOptimizer, TopologyStrategy
from gym_environments.representation.design.concrete import DConcrete
from gym_environments.representation.design.topology import DTopology
from gym_environments.representation.tools.parsers.parse import parse_library_and_seed_designs
from gym_environments.representation.tools.parsers.parsing_designs import parse_design_from_design_swri
from gym_environments.shared.paths import output_folder, ExportType

"""Loading Library and Seed Designs"""
c_library, designs = parse_library_and_seed_designs()

"""Loading optimizers at different abstraction layers"""
topo_opt = TopologyOptimizer(library=c_library)
concr_opt = ConcreteOptimizer(library=c_library)
para_opt = ParametersOptimizer(library=c_library)


def random_topology(design_name: str = "Trowel", designs_dat_file: str = "designs.dat"):

    """Generate Topology DTopology, random strategy"""
    d_topology: DTopology = topo_opt.generate_topology(
        name="RandomDesign",
        strategy=TopologyStrategy.random_strategy
    )

    print("****D_TOPOLOGY****")
    print(d_topology)

    d_topology.export(ExportType.TXT)
    d_topology.export(ExportType.DOT)

    """Refine DTopology to DConcrete, random strategy"""
    d_concrete: DConcrete = concr_opt.concretize_topology(
        d_topology=d_topology, strategy=ConcreteStrategy.random_strategy
    )
    print("\n****D_CONCRETE****")
    print(d_concrete)

    d_concrete.export(ExportType.TXT)
    d_concrete.export(ExportType.DOT)
    d_concrete.export(ExportType.JSON)
    d_concrete.export(ExportType.PDF)

if __name__ == '__main__':
    random_topology()
