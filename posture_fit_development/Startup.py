import logging
import threading
from packaging import version
from typing import NoReturn
from .Sound import SoundPlayer

def startup() -> None:
    sp = SoundPlayer()
    
    def loopSound() -> NoReturn:
        sp.sound_startup()

    loopThread = threading.Thread(target=loopSound, name='backgroundMusicThread')
    loopThread.daemon = True # shut down music thread when the rest of the program exits
    loopThread.start()

def booting(e: threading.Event, e2: threading.Event) -> None:
    sp = SoundPlayer()

    def loopSound() -> None:
        sp.sound_booting()
        e.set()  # Signal that speech is done

    loopThread = threading.Thread(target=loopSound, name='bootingThread')
    loopThread.daemon = True
    loopThread.start()

def booting2(e2: threading.Event, e: threading.Event) -> None:
    sp = SoundPlayer()

    def loopSound() -> None:
        e.wait()  # Wait for speech to finish
        sp.sound_booting_2()

    loopThread = threading.Thread(target=loopSound, name='booting2Thread')
    loopThread.daemon = True
    loopThread.start()

def update(avcv: str, avgv: str) -> bool:
    logger = logging.getLogger("PostureFIT")
    try:
        return version.parse(avcv) < version.parse(avgv)
    except version.InvalidVersion:
        logger.warn("Invalid version, please check the issue. Do a pull request or an issue request, thanks!")
        return False

