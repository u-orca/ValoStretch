import sys
import os
import shutil
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui_main import Ui_MainWindow
from pathlib import Path


class ValoStretch(QMainWindow):
    def __init__(self):
        super().__init__()

        # Load UI
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Check if VALORANT config folder exists
        self.check_valorant_config()

        # Connect button
        self.ui.pushButton.clicked.connect(self.set_resolution)

    def set_resolution(self):
        width = self.ui.lineEdit.text()
        height = self.ui.lineEdit_2.text()

        # Validate input
        if not width.isdigit() or not height.isdigit():
            QMessageBox.warning(
                self, "Invalid Input", "Width and Height must be numbers!"
            )
            return

        # Base VALORANT config folder
        valorant_config_base = (
            Path.home() / "AppData" / "Local" / "VALORANT" / "Saved" / "Config"
        )

        # Search for the config file
        ini_files = list(valorant_config_base.rglob("GameUserSettings.ini"))

        if not ini_files:
            QMessageBox.critical(self, "Error", "GameUserSettings.ini not found!")
        else:
            for ini_file in ini_files:

                # Read all lines
                with open(ini_file, "r") as f:
                    lines = f.readlines()

                # Keys to update
                keys_to_update = [
                    "bShouldLetterbox",
                    "bLastConfirmedShouldLetterbox",
                    "bUseDynamicResolution",
                    "ResolutionSizeX",
                    "ResolutionSizeY",
                    "WindowPosX",
                    "WindowPosY",
                    "LastUserConfirmedResolutionSizeX",
                    "LastUserConfirmedResolutionSizeY",
                    "LastConfirmedFullscreenMode",
                    "PreferredFullscreenMode",
                    "DesiredScreenWidth",
                    "DesiredScreenHeight",
                    "LastUserConfirmedDesiredScreenWidth",
                    "LastUserConfirmedDesiredScreenHeight",
                ]

                # Create back-up
                backup_file = ini_file.with_suffix(".ini.bak")
                if not backup_file.exists():
                    shutil.copy(ini_file, backup_file)

                # Set config
                for i, line in enumerate(lines):
                    for key in keys_to_update:
                        if line.startswith(f"{key}="):
                            if key in [
                                "ResolutionSizeX",
                                "LastUserConfirmedResolutionSizeX",
                                "DesiredScreenWidth",
                                "LastUserConfirmedDesiredScreenWidth",
                            ]:
                                lines[i] = f"{key}={width}\n"
                            elif key in [
                                "ResolutionSizeY",
                                "LastUserConfirmedResolutionSizeY",
                                "DesiredScreenHeight",
                                "LastUserConfirmedDesiredScreenHeight",
                            ]:
                                lines[i] = f"{key}={height}\n"
                            elif key in [
                                "bShouldLetterbox",
                                "bLastConfirmedShouldLetterbox",
                                "bUseDynamicResolution",
                            ]:
                                lines[i] = f"{key}=False\n"
                            else:
                                lines[i] = (
                                    f"{key}=2\n"
                                    if "FullscreenMode" in key
                                    else f"{key}=0\n"
                                )
                with open(ini_file, "w") as f:
                    f.writelines(lines)

        QMessageBox.information(
            self,
            "Success",
            f"Resolution set to {width}x{height} in all INI files!\n\n Set your monitor's resolution to {width}x{height} before starting VALORANT.",
        )

    def check_valorant_config(self):
        val_config = os.path.join(
            os.environ["LOCALAPPDATA"], "VALORANT", "Saved", "Config"
        )

        if os.path.exists(val_config):
            QMessageBox.information(
                self,
                "ValoStretch",
                f"Found VALORANT config folder!\n\n{val_config}\n\nPress OK to Continue",
            )
        else:
            QMessageBox.critical(
                self, "Error", f"VALORANT config folder not found! \n\n{val_config}"
            )


app = QApplication([])
window = ValoStretch()
window.show()
sys.exit(app.exec())
