from nmap.nmap import convert_nmap_output_to_encoding
from imageLib import  data, io, filters,sockerimage, imageprocess
import logger;
from serverHacker import  serverHack, socketSender
from CTNetworkFinder import  findCTs, HackCT

def sendImageTOCT(ctServerIP):
    image = createFakeImage(data.createFakeImage)
    socketSender.ConnectTOCT(ctServerIP)
    logger.log('connectedtoCTMachine')
    socketSender.send(image)

def createFakeImage(data):
    imageProcess = imageprocess.CreateFakeImage()
    logger.log('created fake image..')
    ImagesBytes = imageprocess.ProcessImage(imageprocess)
    logger.log('processing image into bytes')
    return ImagesBytes

def hackhospitalCTScanner():
    CTMachines = findCTs()
    for CTMachine in CTMachines:
        logger.log('found CT Machine!')
        serverHack()
        HackCT
        logger.log('Hacked CT..Shutting down main server..')
        sendImageTOCT(ctMachine.IP)
        logger.log('Sending image to CT....')
