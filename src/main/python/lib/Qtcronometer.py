from PySide6.QtCore import Qt, Signal, QTimer, QObject, QTime
import numpy as np
import os

if os.name == 'posix':
    import simpleaudio as sa

class Cronometro(QObject):
    tiempo_actualizado = Signal(int, bool, str)
    def __init__(self, tick:int=100, delay:int=10, tones:list=(0,40,60,90,100,340), states:list=("delay","irrigation","rest","TOROK","OFI","rest")):
        super().__init__()
        self.tick = tick
        self.delay = delay
        self.tones = tones
        self.states = states
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_cronometro)
        self.start_time = None
        self.crono_time = -10  # Iniciar en -10 segundos
        self.paused_time = 0
        self.is_paused = True
        self.show_dot = False
        self.dot_counter = 0
        self.played_tones = set()

    def start(self):
        self.start_time = QTime.currentTime().msecsSinceStartOfDay()
        self.is_paused = False
        self.timer.start(self.tick)

    def pause(self):
        self.paused_time += QTime.currentTime().msecsSinceStartOfDay() - self.start_time
        self.is_paused = True
        self.timer.stop()

    def reset(self):
        self.start_time = None
        self.crono_time = - self.delay
        self.paused_time = 0
        self.is_paused = True
        self.dot_counter = 0
        self.timer.stop()

    def update_cronometro(self):
        self.dot_counter = (self.dot_counter + 1) % 10
        self.show_dot = self.dot_counter < 5

        if not self.is_paused:
            elapsed_time = int((QTime.currentTime().msecsSinceStartOfDay() - self.start_time + self.paused_time) / 1000)
            self.crono_time = elapsed_time - self.delay

            if self.crono_time in self.tones:
                if self.crono_time not in self.played_tones:
                    self.play_tone(1000, 0.05)
                    self.played_tones.add(self.crono_time)

            if self.crono_time >= self.tones[-1]:
                self.timer.stop()

        state = self.get_current_state()
        self.tiempo_actualizado.emit(self.crono_time, self.show_dot, state)

    def get_current_state(self):
        if self.crono_time < 0:
            return self.states[0]  # "delay"
        else:
            for i in range(1, len(self.tones)):
                if self.tones[i-1] <= self.crono_time < self.tones[i]:
                    return self.states[i]
            return "Unknown state"  # O puedes retornar el último estado: return self.states[-1]


    def play_tone(self, frequency, duration):
        sample_rate = 44100
        t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
        x = np.sin(2 * np.pi * frequency * t)
        audio = (x * 32767).astype(np.int16)
        if os.name == 'posix':

            play_obj = sa.play_buffer(audio, 1, 2, sample_rate)
            play_obj.wait_done()


