#called mosn_2901aX in Season2 Episode 1 16:44
import nmap
import logger
import cameraInjector
import mainLib
import socket

def findAllCameras(localnetworksubnet, ports, logger):
    logger.log)'running nmap to find all cameras and port open on te local network')
    nmScan = nmap.Portscanner()
    infoFromScan - nmScan.scan(localnetworksubnet, ports)
    print(infoFromScan)


if __name__ == '__main__':
    print(f'PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
