#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 14:14:29 2022

@author: morozner
"""

objects = ['planet','WD','BH','NS','comet','RG','TZA','GCs','galaxy']
processes = ['GDF','DF','tides','kicks','RR']
environments = ['GCs','protoplanetary disk','atmospheres','AGN','GMC','field','DM halo']

APJ_keywords_Physical_Data_and_Processes = ['acceleration of particles', 'accretion, accretion disks', 'asteroseismology', 'astrobiology', 'astrochemistry', 'astroparticle physics', 'atomic data', 'atomic processes', 'black hole physics', 'chaos', 'conduction', 'convection', 'dense matter', 'diffusion', 'dynamo', 'elementary particles', 'equation of state', 'gravitation', 'gravitational lensing: strong', 'gravitational lensing: weak', 'gravitational lensing: micro', 'gravitational waves', 'hydrodynamics', 'instabilities', 'line: formation', 'line: identification', 'line: profiles', 'magnetic fields', 'magnetic reconnection', 'magnetohydrodynamics (MHD)', 'masers', 'molecular data', 'molecular processes', 'neutrinos', 'nuclear reactions, nucleosynthesis, abundances', 'opacity', 'plasmas', 'polarization', 'radiation: dynamics', 'radiation mechanisms: general', 'radiation mechanisms: non-thermal', 'radiation mechanisms: thermal', 'radiative transfer', 'relativistic processes', 'scattering', 'shock waves', 'solid state: refractory', 'solid state: volatile', 'turbulence', 'waves']
APJ_keywords_Astronomical_Instrumentation_Methods_and_Techniques = ['atmospheric effects', 'balloons', 'instrumentation: adaptive optics', 'instrumentation: detectors', 'instrumentation: high angular resolution', 'instrumentation: interferometers', 'instrumentation: miscellaneous', 'instrumentation: photometers', 'instrumentation: polarimeters', 'instrumentation: spectrographs', 'light pollution', 'methods: analytical', 'methods: data analysis', 'methods: laboratory: atomic', 'methods: laboratory: molecular', 'methods: laboratory: solid state', 'methods: miscellaneous', 'methods: numerical', 'methods: observational', 'methods: statistical', 'site testing', 'space vehicles', 'space vehicles: instruments', 'techniques: high angular resolution', 'techniques: image processing', 'techniques: imaging spectroscopy', 'techniques: interferometric', 'techniques: miscellaneous', 'techniques: photometric', 'techniques: polarimetric', 'techniques: radar astronomy', 'techniques: radial velocities', 'techniques: spectroscopic', 'telescopes']
APJ_keywords_Astronomical_Databases = ['astronomical databases: miscellaneous', 'atlases', 'catalogs', 'surveys', 'virtual observatory tools']
APJ_keywords_Astrometry_Celestial_Mechanics = ['astrometry', 'celestial mechanics', 'eclipses', 'ephemerides', 'occultations', 'parallaxes', 'proper motions', 'reference systems', 'time']
APJ_keywords_Sun = ['Sun: abundances', 'Sun: activity', 'Sun: atmosphere', 'Sun: chromosphere', 'Sun: corona', 'Sun: coronal mass ejections (CMEs)', 'Sun: evolution', 'Sun: faculae, plages', 'Sun: filaments, prominences', 'Sun: flares', 'Sun: fundamental parameters', 'Sun: general', 'Sun: granulation', 'Sun: helioseismology', 'Sun: heliosphere', 'Sun: infrared', 'Sun: interior', 'Sun: magnetic fields', 'Sun: oscillations', 'Sun: particle emission', 'Sun: photosphere', 'Sun: radio radiation', 'Sun: rotation', '(Sun:) solar–terrestrial relations', '(Sun:) solar wind', '(Sun:) sunspots', 'Sun: transition region', 'Sun: UV radiation', 'Sun: X-rays, gamma rays']
APJ_keywords_Planetary_systems = ['comets: general', 'comets: individual (…, …)', 'Earth', 'interplanetary medium', 'Kuiper belt: general', 'Kuiper belt objects: individual (…, …)', 'meteorites, meteors, meteoroids', 'minor planets, asteroids: general', 'minor planets, asteroids: individual (…, …)', 'Moon', 'Oort Cloud', 'planets and satellites: atmospheres', 'planets and satellites: aurorae', 'planets and satellites: composition', 'planets and satellites: detection', 'planets and satellites: dynamical evolution and stability', 'planets and satellites: formation', 'planets and satellites: fundamental parameters', 'planets and satellites: gaseous planets', 'planets and satellites: general', 'planets and satellites: individual (…, …)', 'planets and satellites: interiors', 'planets and satellites: magnetic fields', 'planets and satellites: oceans', 'planets and satellites: physical evolution', 'planets and satellites: rings', 'planets and satellites: surfaces', 'planets and satellites: tectonics', 'planets and satellites: terrestrial planets', 'protoplanetary disks', 'planet–disk interactions', 'planet–star interactions', 'zodiacal dust']
APJ_keywords_stars = ['stars: abundances', 'stars: activity', 'stars: AGB and post-AGB', 'stars: atmospheres', '(stars:) binaries (including multiple): close', '(stars:) binaries: eclipsing', '(stars:) binaries: general', '(stars:) binaries: spectroscopic', '(stars:) binaries: symbiotic', '(stars:) binaries: visual', 'stars: black holes', '(stars:) blue stragglers', '(stars:) brown dwarfs', 'stars: carbon', 'stars: chemically peculiar', 'stars: chromospheres', '(stars:) circumstellar matter', 'stars: coronae', 'stars: distances', 'stars: dwarf novae', 'stars: early-type', 'stars: emission-line, Be', 'stars: evolution', 'stars: flare', 'stars: formation', 'stars: fundamental parameters', 'stars: general', '(stars:) gamma-ray burst: general', '(stars:) gamma-ray burst: individual (…, …)', '(stars:) Hertzsprung–Russell and C–M diagrams', 'stars: horizontal-branch', 'stars: imaging', 'stars: individual (…, …)', 'stars: interiors', 'stars: jets', 'stars: kinematics and dynamics', 'stars: late-type', 'stars: low-mass', 'stars: luminosity function, mass function', 'stars: magnetars', 'stars: magnetic field', 'stars: massive', 'stars: mass-loss', 'stars: neutron', '(stars:) novae, cataclysmic variables', 'stars: oscillations (including pulsations)', 'stars: peculiar (except chemically peculiar)', '(stars:) planetary systems', 'stars: Population II', 'stars: Population III', 'stars: pre-main sequence', 'stars: protostars', '(stars:) pulsars: general', '(stars:) pulsars: individual (…, …)', 'stars: rotation', 'stars: solar-type', '(stars:) starspots', 'stars: statistics', '(stars:) subdwarfs', '(stars:) supergiants', '(stars:) supernovae: general', '(stars:) supernovae: individual (…, …)', 'stars: variables: Cepheids', 'stars: variables: delta Scuti', 'stars: variables: general', 'stars: variables: RR Lyrae', 'stars: variables: S Doradus', 'stars: variables: T Tauri, Herbig Ae/Be', '(stars:) white dwarfs', 'stars: winds, outflows', 'stars: Wolf–Rayet']
APJ_keywords_Interstellar_Medium_Nebulae = ['ISM: abundances', 'ISM: atoms', 'ISM: bubbles', 'ISM: clouds', '(ISM:) cosmic rays', '(ISM:) dust, extinction', '(ISM:) evolution', 'ISM: general', '(ISM:) HII regions', '(ISM:) Herbig–Haro objects', 'ISM: individual objects (…, …) (except', 'planetary nebulae)', 'ISM: jets and outflows', 'ISM: kinematics and dynamics', 'ISM: lines and bands', 'ISM: magnetic fields', 'ISM: molecules', '(ISM:) planetary nebulae: general', '(ISM:) planetary nebulae: individual (…, …)', '(ISM:) photon-dominated region (PDR)', 'ISM: structure', 'ISM: supernova remnants']
APJ_keywords_The_Galaxy = ['Galaxy: abundances', 'Galaxy: bulge', 'Galaxy: center', 'Galaxy: disk', 'Galaxy: evolution', 'Galaxy: formation', 'Galaxy: fundamental parameters', 'Galaxy: general', '(Galaxy:) globular clusters: general', '(Galaxy:) globular clusters: individual (…, …)', 'Galaxy: halo', '(Galaxy:) local interstellar matter', 'Galaxy: kinematics and dynamics', 'Galaxy: nucleus', '(Galaxy:) open clusters and associations: general', '(Galaxy:) open clusters and associations: individual (…, …)', '(Galaxy:) solar neighborhood', 'Galaxy: stellar content', 'Galaxy: structure']
APJ_keywords_galaxies = ['galaxies: abundances', 'galaxies: active', '(galaxies:) BL Lacertae objects: general', '(galaxies:) BL Lacertae objects: individual (…, …)', 'galaxies: bulges', 'galaxies: clusters: general', 'galaxies: clusters: individual (…, …)', 'galaxies: clusters: intracluster medium', 'galaxies: distances and redshifts', 'galaxies: dwarf', 'galaxies: elliptical and lenticular, cD', 'galaxies: evolution', 'galaxies: formation', 'galaxies: fundamental parameters', 'galaxies: general', 'galaxies: groups: general', 'galaxies: groups: individual (…, …)', 'galaxies: halos', 'galaxies: high-redshift', 'galaxies: individual (…, …)', 'galaxies: interactions', '(galaxies:) intergalactic medium', 'galaxies: irregular', 'galaxies: ISM', 'galaxies: jets', 'galaxies: kinematics and dynamics', '(galaxies:) Local Group', 'galaxies: luminosity function, mass function', '(galaxies:) Magellanic Clouds', 'galaxies: magnetic fields', 'galaxies: nuclei', 'galaxies: peculiar', 'galaxies: photometry', '(galaxies:) quasars: absorption lines', '(galaxies:) quasars: emission lines', '(galaxies:) quasars: general', '(galaxies:) quasars: individual (…, …)', '(galaxies:) quasars: supermassive black holes', 'galaxies: Seyfert', 'galaxies: spiral', 'galaxies: starburst', 'galaxies: star clusters: general', 'galaxies: star clusters: individual (…, …)', 'galaxies: star formation', 'galaxies: statistics', 'galaxies: stellar content', 'galaxies: structure']
APJ_keywords_cosmology = ['(cosmology:) cosmic background radiation', '(cosmology:) cosmological parameters', 'cosmology: miscellaneous', 'cosmology: observations', 'cosmology: theory', '(cosmology:) dark ages, reionization, first stars', '(cosmology:) dark matter', '(cosmology:) dark energy', '(cosmology:) diffuse radiation', '(cosmology:) distance scale', '(cosmology:) early universe', '(cosmology:) inflation', '(cosmology:) large-scale structure of universe', '(cosmology:) primordial nucleosynthesis']
APJ_keywords_Resolved_Unresolved_Sources = ['gamma rays: diffuse background', 'gamma rays: galaxies', 'gamma rays: galaxies: clusters', 'gamma rays: general', 'gamma rays: ISM', 'gamma rays: stars', 'infrared: diffuse background', 'infrared: galaxies', 'infrared: general', 'infrared: ISM', 'infrared: planetary systems', 'infrared: stars', 'radio continuum: galaxies', 'radio continuum: general', 'radio continuum: ISM', 'radio continuum: planetary systems', 'radio continuum: stars', 'radio lines: galaxies', 'radio lines: general', 'radio lines: ISM', 'radio lines: planetary systems', 'radio lines: stars', 'submillimeter: diffuse background', 'submillimeter: galaxies', 'submillimeter: general', 'submillimeter: ISM', 'submillimeter: planetary systems', 'submillimeter: stars', 'ultraviolet: galaxies', 'ultraviolet: general', 'ultraviolet: ISM', 'ultraviolet: planetary systems', 'ultraviolet: stars', 'X-rays: binaries', 'X-rays: bursts', 'X-rays: diffuse background', 'X-rays: galaxies', 'X-rays: galaxies: clusters', 'X-rays: general', 'X-rays: individual (…, …)', 'X-rays: ISM', 'X-rays: stars']

categories = [objects, processes,environments,APJ_keywords_Physical_Data_and_Processes,APJ_keywords_Astronomical_Instrumentation_Methods_and_Techniques,APJ_keywords_Astronomical_Databases,APJ_keywords_Astrometry_Celestial_Mechanics,APJ_keywords_Sun,
              APJ_keywords_Planetary_systems,APJ_keywords_stars,APJ_keywords_Interstellar_Medium_Nebulae,APJ_keywords_The_Galaxy,APJ_keywords_galaxies,APJ_keywords_cosmology,APJ_keywords_Resolved_Unresolved_Sources
              ]
categories_names = ['objects', 'processes','environments','APJ_keywords_Physical_Data_and_Processes','APJ_keywords_Astronomical_Instrumentation_Methods_and_Techniques','APJ_keywords_Astronomical_Databases','APJ_keywords_Astrometry_Celestial_Mechanics','APJ_keywords_Sun',
                    'APJ_keywords_Planetary_systems','APJ_keywords_stars','APJ_keywords_Interstellar_Medium_Nebulae','APJ_keywords_The_Galaxy','APJ_keywords_galaxies','APJ_keywords_cosmology','APJ_keywords_Resolved_Unresolved_Sources'
                    ]



from tkinter import *
import random 

class Checkbar(Frame):
   def __init__(self, parent=None, picks=[], side=TOP, anchor=W):
      Frame.__init__(self, parent)
      self.vars = []
      for pick in picks:
         var = IntVar()
         chk = Checkbutton(self, text=pick, variable=var)
         chk.pack(side=side, anchor=anchor, expand=YES)
         self.vars.append(var)
   def state(self):
      return map((lambda var: var.get()), self.vars)
if __name__ == '__main__':
   root = Tk()
   lng = Checkbar(root, categories_names)
   lng.pack(side=TOP,  fill=X)
   lng.config(relief=GROOVE, bd=2)

   def allstates(): 
      print(list(lng.state()))
   Button(root, text='Go!', command=root.quit).pack(side=TOP)
   root.mainloop()
   
   choices = list(lng.state())
   final_idea = ''
   
   for i in range(len(categories)):
       
       if choices[i] == 1:
           cat=categories[i]
           rand = random.randint(0, len(cat)-1)
           if ('APJ_keywords' in categories_names[i]) == False:
               final_idea = final_idea+str(categories_names[i])+':'+str(cat[rand])+'*'
           else:
               final_idea = final_idea+str(cat[rand])+'*'
   print(final_idea)
           
