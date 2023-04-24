# -*- coding: utf-8 -*-

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QPushButton, QLineEdit, QFileDialog, QMessageBox
from PyQt6.QtGui import QFont


def downloader(url, save_path):
    import ffmpeg as ff

    input_source = ff.input(url)
    save_video = ff.output(input_source, save_path)
    ff.run(save_video)

    return True


def save_btn_push():
    file_path, _ = QFileDialog.getSaveFileName(None, 'Select path', './', 'All Files (*);;Video Files (*.mp4)')
    save_line_edit.setText(file_path)


def start_btn_push():
    state = downloader(url=source_line_edit.text(), save_path=save_line_edit.text())

    if state:
        QMessageBox.about(None, 'Finish', 'Please check the downloaded file.')


if __name__ == '__main__':

    app = QApplication(sys.argv)
    w = QWidget()
    layout = QGridLayout()

    w.resize(450, 300)
    w.setWindowTitle('TuTu Downloader')

    source_label = QLabel('URL')
    save_label = QLabel('Save path')

    source_label.setFont(QFont('Times New Roman', 20))
    save_label.setFont(QFont('Times New Roman', 20))

    source_line_edit = QLineEdit('')
    save_line_edit = QLineEdit('')

    source_line_edit.setFont(QFont('Times New Roman', 20))
    save_line_edit.setFont(QFont('Times New Roman', 20))
    source_line_edit.setFixedHeight(35)
    save_line_edit.setFixedHeight(35)

    start_btn = QPushButton('Start')
    save_btn = QPushButton('Select')

    start_btn.setFont(QFont('Times New Roman', 20))
    save_btn.setFont(QFont('Times New Roman', 20))

    start_btn.clicked.connect(start_btn_push)
    save_btn.clicked.connect(save_btn_push)

    layout.addWidget(source_label, 1, 0)
    layout.addWidget(source_line_edit, 1, 1, 1, 2)
    layout.addWidget(save_label, 2, 0)
    layout.addWidget(save_line_edit, 2, 1)
    layout.addWidget(save_btn, 2, 2)
    layout.addWidget(start_btn, 3, 0, 1, 3)

    w.setLayout(layout)
    w.show()

    sys.exit(app.exec())
