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

MY_MAINFILE=fembemnotes

#
# These are the names of the tex sources for the document. If there is
# more than one source quotation (") marks must be used around the
# individual sources seperated by spaces

MY_TEX_SRC="titlepage.tex "\
"fem_basis_fns/fem_basis_fns.tex "\
"heat_conduction/heat_conduction.tex "\
"bem/bem.tex "\
"lin_elasticity/lin_elasticity.tex "\
"heat_conduction/heat_conduction.tex "\
"transient_heat_condn/transient_heat_condn.tex "\
"modal_analysis/modal_analysis.tex "\
"con_mechanics/con_mechanics.tex "\
"datafitting/datafitting.tex "\
"domints_in_bem/domints_in_bem.tex "\
"timedep_bem/timedep_bem.tex  "\
"derivative_bie/derivative_bie.tex  "\
"references.tex"

#	chapter8/FEM8.tex = datafitting
#	chapter9/FEM9.tex = derivative_bie
#
# The names of the eps/figs/(gnu)plot files that go into the document. 
# if there are none then leave after the ='s sign blank.

MY_EPS_SRC=
MY_FIG_SRC="fem_basis_fns/figs/*.fig bem/figs/*.fig datafitting/figs/*.fig heat_conduction/figs/*.fig lin_elasticity/figs/*.fig transient_heat_condn/figs/*.fig derivative_bie/figs/*.fig"
MY_PLOT_SRC=
MY_GNUPLOT_SRC=

#
# The name of the directory to place the html version of the document.
# Note that the actual file will be placed in the directory
# MY_HTMLUPDATE_DIR/MY_MAINFILE with filename MY_MAINFILE.html

MY_HTMLUPDATE_DIR=${OPENCMISS_ROOT}/www/help

#
# This next option should be "user" if the document is intended for
# general users or "programmer" if the document is intended for 
# cmiss programmers

MY_HTMLIDXTYPE=user

#
# The name of the bibliography database for the document

MY_BIBS=${OPENCMISS_ROOT}/documentation/notes/references/opencmiss_references.bib

#
# The name of the printer to print the document to
#MY_PRINTER=laserjet_postscript
MY_PRINTER=

#
# Below this line should not need changing
#
# Actual make command:
#

make -f ${OPENCMISS_ROOT}/documentation/notes/latex/Latex_Makefile $* \
	MAINFILE=$MY_MAINFILE \
	TEX_SRC="$MY_TEX_SRC" \
	EPS_SRC="$MY_EPS_SRC" \
	FIG_SRC="$MY_FIG_SRC" \
	PLOT_SRC="$MY_PLOT_SRC" \
	GNUPLOT_SRC="$MY_GNUPLOT_SRC" \
	HTMLUPDATE_DIR=$MY_HTMLUPDATE_DIR \
	HTMLIDXTYPE=$MY_HTMLIDXTYPE \
	BIBS="$MY_BIBS" \
	PRINTER=$MY_PRINTER

