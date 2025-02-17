#!/bin/bash -f
#
# This shell script is used to invoke the Latex_Makefile for general 
# documents. It should be copied into the individual document directory
# as a new document is created. It is used to pass document specific 
# parameters to the makefile. NOTE that if parameters may be omitted
# by simply deleting them from the "make" command line.
#
# Usage:
#   Latex_make.sh [makefile_options] 
#
# Changable options:
#
# This is the overall name of the document

MY_MAINFILE=OpenCMISSNotes

#
# These are the names of the tex sources for the document. If there is
# more than one source quotation (") marks must be used around the
# individual sources seperated by spaces.

MY_TEX_SRC="TitlePage/TitlePage.tex "\
"Introduction/Introduction.tex "\
"BasisFunctions/BasisFunctions.tex "\
"FiniteElementMethod/FiniteElementMethod.tex "\
"DifferentialGeometry/DifferentialGeometry.tex "\
"Theory/Theory.tex "\
"Theory/SolutionMethods.tex "\
"Theory/CoordinateTransformations.tex "\
"Maths/Maths.tex "\
"Maths/Space/Space.tex "\
"Maths/Space/Sets/Sets.tex "\
"Maths/Space/Sets/Numbers/Numbers.tex "\
"Maths/Space/Topology/Topology.tex "\
"Maths/Space/AbstractSpaces/AbstractSpaces.tex "\
"Maths/Notation/Notation.tex "\
"Maths/Algebra/Algebra.tex "\
"Maths/Algebra/Groups/Groups.tex "\
"Maths/Algebra/FieldsAndRings/FieldsAndRings.tex "\
"Maths/Algebra/Modules/Modules.tex "\
"Maths/Geometry/Geometry.tex "\
"Maths/Notation/Notation.tex "\
"Maths/VectorCalculus/VectorCalculus.tex "\
"Maths/Operations/Operations.tex "\
"ClassicalField/ClassicalField.tex "\
"ClassicalField/GeneralisedLaplaceEquation.tex "\
"ClassicalField/PoissonEquation.tex "\
"ClassicalField/DiffusionEquation.tex "\
"ClassicalField/AdvectionDiffusionEquation.tex "\
"ClassicalField/ReactionDiffusionEquation.tex "\
"ClassicalField/AdvectionReactionDiffusionEquation.tex "\
"ClassicalField/WaveEquation.tex "\
"ClassicalField/BiharmonicEquation.tex "\
"ClassicalField/HelmholtzEquation.tex "\
"SolidMechanics/SolidMechanics.tex "\
"SolidMechanics/LinearElasticity.tex "\
"SolidMechanics/FiniteElasticity.tex "\
"FluidMechanics/FluidMechanics.tex "\
"FluidMechanics/NavierStokesEquation.tex "\
"FluidMechanics/BoundaryConditions.tex "\
"FluidMechanics/BurgersEquation.tex "\
"FluidMechanics/PoiseuilleFlow.tex "\
"FluidMechanics/StokesEquation.tex "\
"FluidMechanics/DarcyEquation.tex "\
"FluidMechanics/OneDimensionalFlow.tex "\
"FluidMechanics/PressurePoissonEquation.tex "\
"FluidMechanics/FiniteVolume.tex "\
"Bioelectrics/Bioelectrics.tex "\
"Bioelectrics/BidomainEquation.tex "\
"Bioelectrics/MonodomainEquation.tex "\
"Bioelectrics/ImmersedBidomain.tex "\
"MagnetoElectrics/MagnetoElectrics.tex "\
"MagnetoElectrics/ElectrostaticEquations.tex "\
"MagnetoElectrics/MagnetostaticEquations.tex "\
"MagnetoElectrics/MaxwellEquations.tex "\
"Multiphysics/Multiphysics.tex "\
"Multiphysics/Poroelasticity.tex "\
"Multiphysics/FSI.tex "\
"Fitting/Fitting.tex "\
"Fitting/LinearFitting.tex "\
"Fitting/NonlinearFitting.tex "\
"PortHamiltonian/PortHamiltonian.tex "\
"ComputationAndNumerics/ComputationAndNumerics.tex "\
"DevelopersDocument/DevelopersDoc.tex "\
"Appendices/Appendices.tex "\
"Appendices/CoordinateSystems.tex "\
"Appendices/TensorComponents.tex "\
"Appendices/ElementStiffnessMatrices.tex "\
"References/References.tex "\
"Index/Index.tex"

#
# The names of the eps/figs/(gnu)plot files that go into the document. 
# if there are none then leave after the ='s sign blank. If there is
# more than one source quotation (") marks must be used around the
# individual sources seperated by spaces.

MY_EPS_SRC=
MY_FIG_SRC="BasisFunctions/figs/*.fig"
MY_SVG_SRC="BasisFunctions/svgs/*.svg "\
"FiniteElementMethod/svgs/*.svg "\
"DifferentialGeometry/svgs/*.svg "\
"ClassicalField/svgs/*.svg "\
"SolidMechanics/svgs/*.svg "\
"FluidMechanics/svgs/*.svg "\
"Fitting/svgs/*.svg "\
"PortHamiltonian/svgs/*.svg "\
"ComputationAndNumerics/svgs/*.svg "\
"DevelopersDocument/svgs/*.svg "\
"Appendices/svgs/*.svg "
MY_PLOT_SRC="BasisFunctions/plots/*.gnu "\
"BasisFunctions/plots/*.gnu8 "\
"ComputationAndNumerics/plots/*.gnu"
MY_GNUPLOT_SRC="BasisFunctions/gnuplots/*.gnuplot "

#
# The name of the directory to place the html version of the document.
# Note that the actual file will be placed in the directory
# MY_HTMLUPDATE_DIR/MY_MAINFILE with filename index.html

MY_HTMLUPDATE_DIR=${OpenCMISS_ROOT}/www/help

#
# This next option controls the type of backlinks to add to the footer
# of the HTML file. It should be "user" if the document is intended for
# general users or "programmer" if the document is intended for 
# cmiss programmers. If no backlinks are required use "none".

MY_HTMLIDXTYPE=user

#
# The name of the bibliography database for the document

MY_BIBS=${OpenCMISS_ROOT}/documentation/notes/references/opencmiss_references.bib

#
# The name of the printer to print the document to

MY_PRINTER=laserjet_postscript

#
# Below this line should not need changing
#
# Actual make command:
#
make -f ${OpenCMISS_ROOT}/documentation/notes/latex/Latex_Makefile $* \
	MAINFILE=$MY_MAINFILE \
	TEX_SRC="$MY_TEX_SRC" \
	EPS_SRC="$MY_EPS_SRC" \
	FIG_SRC="$MY_FIG_SRC" \
	SVG_SRC="$MY_SVG_SRC" \
	PLOT_SRC="$MY_PLOT_SRC" \
	GNUPLOT_SRC="$MY_GNUPLOT_SRC" \
	HTMLUPDATE_DIR=$MY_HTMLUPDATE_DIR \
	HTMLIDXTYPE=$MY_HTMLIDXTYPE \
	BIBS=$MY_BIBS \
	PRINTER=$MY_PRINTER
