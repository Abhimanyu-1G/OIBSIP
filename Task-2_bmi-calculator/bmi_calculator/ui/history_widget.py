from PyQt6.QtWidgets import QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem, QHeaderView, QLabel
from PyQt6.QtGui import QPainter, QPixmap
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.dates as mdates
import datetime
import os

class HistoryWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0) # Remove margins to better fit the new layout

        # Graph
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        layout.addWidget(self.canvas)

        # Table
        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["Date", "Weight", "Height", "BMI"])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        layout.addWidget(self.table)

        # Clear Data Button
        from PyQt6.QtWidgets import QPushButton
        self.clear_btn = QPushButton("Clear History")
        self.clear_btn.setObjectName("clear_btn") # Set object name for QSS styling
        layout.addWidget(self.clear_btn)

        self.setLayout(layout)

    def update_data(self, records):
        # Update Table
        self.table.setRowCount(len(records))
        dates = []
        bmis = []

        for i, (weight, height, bmi, date_str) in enumerate(records):
            try:
                date_obj = datetime.datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')
            except ValueError:
                date_obj = datetime.datetime.now()

            self.table.setItem(i, 0, QTableWidgetItem(date_str))
            self.table.setItem(i, 1, QTableWidgetItem(str(weight)))
            self.table.setItem(i, 2, QTableWidgetItem(str(height)))
            self.table.setItem(i, 3, QTableWidgetItem(f"{bmi:.2f}"))
            
            dates.append(date_obj)
            bmis.append(bmi)

        # Update Graph
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        
        # --- Theming for the new style ---
        self.figure.patch.set_facecolor('#1e1e1e') # Dark background
        ax.set_facecolor('#1e1e1e') # Dark axis background

        if dates:
            # Plot with the new theme colors
            line, = ax.plot(dates, bmis, marker='o', linestyle='-', linewidth=2, markersize=8)
            line.set_color('#007acc') # Blue accent for the line
            line.set_markerfacecolor('#007acc')
            line.set_markeredgecolor('#ffffff') # White edge for visibility
            
            ax.set_title("BMI Trend", color='#d4d4d4', fontsize=12, fontweight='bold')
            ax.set_xlabel("Date", color='#d4d4d4')
            ax.set_ylabel("BMI", color='#d4d4d4')
            
            # Style ticks
            ax.tick_params(axis='x', colors='#d4d4d4')
            ax.tick_params(axis='y', colors='#d4d4d4')
            
            # Style spines (the border of the graph)
            ax.spines['bottom'].set_color('#3c3c3c')
            ax.spines['top'].set_color('#3c3c3c')
            ax.spines['left'].set_color('#3c3c3c')
            ax.spines['right'].set_color('#3c3c3c')

            ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
            ax.xaxis.set_major_locator(mdates.AutoDateLocator())
            self.figure.autofmt_xdate()
            ax.grid(True, color='#3c3c3c', linestyle='--')
        
        self.canvas.draw()
