#!/usr/bin/python3.1
#­*­coding: utf­8 -­*­



#JolieBulle 2.8
#Copyright (C) 2010-2013 Pierre Tavares

#This program is free software; you can redistribute it and/or
#modify it under the terms of the GNU General Public License
#as published by the Free Software Foundation; either version 3
#of the License, or (at your option) any later version.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.

#You should have received a copy of the GNU General Public License
#along with this program; if not, write to the Free Software
#Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.




import PyQt4
import sys
import logging
from PyQt4 import QtCore
import xml.etree.ElementTree as ET
from globals import *
from model.fermentable import *
from model.hop import *
from model.yeast import *
from model.misc import *
from model.mash import *
from base import *
from operator import attrgetter
import view.base

logger = logging.getLogger(__name__)

class ImportIng :
    def __init__(self):
        self.listeFermentables = list()
        self.listeHops = list()
        self.listeYeasts = list()
        self.listeMiscs = list()

    def parseFile(self, s) :
        fichierBeerXML = s
        self.arbre = ET.parse(fichierBeerXML)
        presentation=self.arbre.find('.//RECIPE')
        fermentables=self.arbre.findall('.//FERMENTABLE')
        hops = self.arbre.findall('.//HOP')
        levures = self.arbre.findall('.//YEAST')
        misc = self.arbre.findall('.//MISC')

        for element in hops:
            ImportBase.addHop( Hop.parse(element))
        for element in fermentables:
            ImportBase.addFermentable(Fermentable.parse(element))
        for element in misc:
            ImportBase.addMisc(Misc.parse(element))

        



 