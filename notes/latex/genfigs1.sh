#!/bin/csh -f
#
# Shell file for generating fig files (for the first time) from
# gnu files.
#
# Usage:
#   see genfigs.sh for usage details
# Created:
#   Chris Bradley
# Updates:
#
make -f ${OpenCMISS_ROOT}/documentation/notes/latex/Makeplots $1:r.fig
