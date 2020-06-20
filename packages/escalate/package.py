# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Escalate(BundlePackage):
    """EIC Softare Consortium environment."""

    homepage = "http://gitlab.com/eic/escalate"

    version('develop')
    # Dev
    depends_on('cmake', when='@develop')
    depends_on('boost', when='@develop')
    depends_on('python', when='@develop')
    # HENP
    depends_on('root', when='@develop')
    depends_on('geant4', when='@develop')
    depends_on('eigen', when='@develop')
    depends_on('clhep', when='@develop')
    depends_on('vgm', when='@develop')
    depends_on('genfit', when='@develop')
    depends_on('hepmc', when='@develop')
    depends_on('hepmc3', when='@develop')
    depends_on('acts', when='@develop')
    depends_on('delphes', when='@develop')
    depends_on('fastjet', when='@develop')
    # MCEG
    depends_on('lhapdf', when='@develop')
    depends_on('pythia8', when='@develop')
    depends_on('dire', when='@develop')
    # depends_on('cernlib', when='@develop')  # FIXME no package
    depends_on('lhapdf5', when='@develop')
    depends_on('pythia6', when='@develop')
    # EIC
    # depends_on('ejpm', when='@develop')  # FIXME no package
    depends_on('eic-smear', when='@develop')
    # depends_on('ejana', when='@develop')
    depends_on('g4e', when='@develop')
    depends_on('jana2', when='@develop')

    version('1.0.1')
    # gcc 9.2
    conflicts('%gcc@:9.1.0')
    conflicts('%gcc@9.3.0:')
    # Dev
    depends_on('cmake@3.17.0', when='@1.0.1')
    depends_on('boost@1.70.0', when='@1.0.1')
    depends_on('python@3.7.5', when='@1.0.1')
    # HENP
    depends_on('root@6.20.04 cxxstd=17', when='@1.0.1')
    depends_on('geant4@10.6.1 cxxstd=17', when='@1.0.1')
    depends_on('eigen@3.3.7', when='@1.0.1')
    # FIXME geant4@10.6.1 depends_on clhep@2.4.1.3
    # depends_on('clhep@2.3.2.2', when='@1.0.1')
    depends_on('vgm@4-5', when='@1.0.1')
    depends_on('genfit@2020-06-03', when='@1.0.1')
    depends_on('hepmc@2.06.09', when='@1.0.1')
    depends_on('hepmc3@3.2.1', when='@1.0.1')
    depends_on('acts@0.22.0', when='@1.0.1')
    depends_on('delphes@3.4.2', when='@1.0.1')
    depends_on('fastjet@3.3.3', when='@1.0.1')
    # MCEG
    depends_on('lhapdf@6.2.3', when='@1.0.1')
    depends_on('pythia8@8244', when='@1.0.1')
    depends_on('dire@2.004', when='@1.0.1')
    # depends_on('cernlib@2006-12-20', when='@1.0.1')  # FIXME no package
    depends_on('lhapdf5@5.9.1', when='@1.0.1')  # FIXME was version 5.9.1.6
    depends_on('pythia6@6.4.28', when='@1.0.1')  # FIXME was version RAD-CORR
    # EIC
    # depends_on('ejpm@0.3.12', when='@1.0.1')  # FIXME no package
    depends_on('eic-smear@1.0.4', when='@1.0.1')  # FIXME  was version 1.0.4f1
    # depends_on('ejana@1.2.2', when='@1.0.1')
    depends_on('g4e@1.3.4', when='@1.0.1')
    depends_on('jana2@2.0.2', when='@1.0.1')
