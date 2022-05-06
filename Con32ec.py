import socket


def connectToCamera(isToDeleteInfo, logger):
    logger.log('connecting to camera....')
    camerasFound = findAllCameras('127.0.0.1', '1-5001', logger)
    for camera in camerasFound():
        print('cameraName :  %s (%s)' % (host, nmScan[host].hostname()))
        print('State : %s' % nmScan[host].state())
        for cameraToAttack in camera:
            print('attacking camera by connecting to it and removing')
            print('connecting....')
            sendSocketToRemveoInfo(cameraToAttack.ip, cameraToAttack.port, logger)
def sendSocketToRemoveInfo(localnetip, port, logger):
    logger.log('sending socket to remove')
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientSocket.connect(localnetip, port)
    dataBytes = '54 68 65 20 71 75 69 63 6b 20 62 72 6f 78 20 6a 75 6d 70 73 20 6f '
    clientSocket.send(data.encode())
    dataFromServer = clientSocket.recv(1024)

