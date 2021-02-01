""" Game fix for Persona 4 Golden
"""
#pylint: disable=C0103

from protonfixes import util

def main():
    """ installs devenum, quartz, wmp9 and adjust pulse latency
    """

    # Fix pre-rendered cutscene playback
    util.protontricks('xactengine3_7_ge')
    util.protontricks('d3dx11_43_ge')
    util.protontricks('d3dcompiler_43_ge')
    util.protontricks('wmp9_ge')
    util.protontricks('quartz')
    util.protontricks('klite_ge')
    util.set_environment('WINEDLLOVERRIDES','mfplay=n')
