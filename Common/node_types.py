NAMED_THING = 'biolink:NamedThing'
BIOLOGICAL_ENTITY = 'biolink:BiologicalEntity'
DISEASE_OR_PHENOTYPIC_FEATURE = 'biolink:DiseaseOrPhenotypicFeature'
DISEASE = 'biolink:Disease'
PHENOTYPIC_FEATURE = 'biolink:PhenotypicFeature'
MOLECULAR_ENTITY = 'biolink:MolecularEntity'
CHEMICAL_SUBSTANCE = 'biolink:ChemicalSubstance'
DRUG = 'biolink:Drug'
METABOLITE = 'biolink:Metabolite'
ANATOMICAL_ENTITY = 'biolink:AnatomicalEntity'
GENE = 'biolink:Gene'
GENE_PRODUCT = 'biolink:GeneProduct'
GENE_OR_GENE_PRODUCT = 'biolink:GeneOrGeneProduct'
SEQUENCE_VARIANT = 'biolink:SequenceVariant'
BIOLOGICAL_PROCESS_OR_ACTIVITY = 'biolink:BiologicalProcessOrActivity'
MOLECULAR_ACTIVITY = 'biolink:MolecularActivity'
BIOLOGICAL_PROCESS = 'biolink:BiologicalProcess'
PATHWAY = 'biolink:Pathway'
CELLULAR_COMPONENT = 'biolink:CellularComponent'
CELL = 'biolink:Cell'
GROSS_ANATOMICAL_STRUCTURE = 'biolink:GrossAnatomicalStructure'
GENETIC_CONDITION = 'biolink:GeneticCondition'
UNSPECIFIED = 'biolink:Unspecified'
GENE_FAMILY = 'biolink:GeneFamily'
GENOMIC_ENTITY = 'biolink:GenomicEntity'
FOOD = 'biolink:Food'

# The root of all biolink_model entities
ROOT_ENTITY = NAMED_THING

node_types = [
    NAMED_THING,
    BIOLOGICAL_ENTITY,
    DISEASE_OR_PHENOTYPIC_FEATURE,
    DISEASE,
    PHENOTYPIC_FEATURE,
    MOLECULAR_ENTITY,
    CHEMICAL_SUBSTANCE,
    DRUG,
    METABOLITE,
    ANATOMICAL_ENTITY,
    GENE,
    SEQUENCE_VARIANT,
    BIOLOGICAL_PROCESS_OR_ACTIVITY,
    MOLECULAR_ACTIVITY,
    BIOLOGICAL_PROCESS,
    PATHWAY,
    CELLULAR_COMPONENT,
    CELL,
    GROSS_ANATOMICAL_STRUCTURE,
    GENETIC_CONDITION,
    UNSPECIFIED,
    GENE_FAMILY,
    FOOD
]


# A collection of biolink property variable names.

ORIGINAL_KNOWLEDGE_SOURCE = 'biolink:original_knowledge_source'
PRIMARY_KNOWLEDGE_SOURCE = 'biolink:primary_knowledge_source'
AGGREGATOR_KNOWLEDGE_SOURCES = 'biolink:aggregator_knowledge_source'
PUBLICATIONS = 'publications'
