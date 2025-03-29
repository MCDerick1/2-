import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton


class HarmonicOscillatorPlotter(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Гармоническое колебание')
        self.setGeometry(100, 100, 800, 600)

        layout = QVBoxLayout()

        # Поле ввода для амплитуды
        self.amplitude_label = QLabel('Амплитуда (в м):')
        self.amplitude_input = QLineEdit()
        layout.addWidget(self.amplitude_label)
        layout.addWidget(self.amplitude_input)

        # Поле ввода для частоты
        self.frequency_label = QLabel('Частота (в Гц):')
        self.frequency_input = QLineEdit()
        layout.addWidget(self.frequency_label)
        layout.addWidget(self.frequency_input)

        # Поле ввода для фазы
        self.phase_label = QLabel('Фаза (в градусах):')
        self.phase_input = QLineEdit()
        layout.addWidget(self.phase_label)
        layout.addWidget(self.phase_input)

        # Кнопка построить
        self.plot_button = QPushButton('Построить')
        self.plot_button.clicked.connect(self.plot_harmonic_oscillation)
        layout.addWidget(self.plot_button)

        # Виджет для отображения графика
        self.canvas = FigureCanvas(plt.Figure())
        layout.addWidget(self.canvas)

        self.setLayout(layout)

    def plot_harmonic_oscillation(self):
        # Считывание данных с полей ввода
        try:
            amplitude = float(self.amplitude_input.text())
            frequency = float(self.frequency_input.text())
            phase = float(self.phase_input.text())
        except ValueError:
            return  # Если введены некорректные данные, выходим из функции

        # Преобразование фазы из градусов в радианы
        phase_rad = np.radians(phase)

        # Генерация временной оси
        t = np.linspace(0, 5, 1000)  # время от 0 до 5 секунд

        # Вычисление смещения
        x = amplitude * np.sin(2 * np.pi * frequency * t + phase_rad)

        # Построение графика
        self.canvas.figure.clear()
        ax = self.canvas.figure.add_subplot(111)
        ax.plot(t, x)
        ax.set_xlabel('X -- время (с)')
        ax.set_ylabel('Y -- смещение (м)')
        ax.set_title('График гармонического колебания')
        ax.grid()

        self.canvas.draw()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = HarmonicOscillatorPlotter()
    window.show()
    sys.exit(app.exec_())
