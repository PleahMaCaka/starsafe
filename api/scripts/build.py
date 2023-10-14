from os import system as cli
from time import sleep

cli("docker stop starsafe-server")
print("Waiting 3 seconds for container to stop..."), sleep(3)
cli("docker rmi starsafe"), print("Old image removed!")
cli("docker build -t starsafe ."), print("Done!")
