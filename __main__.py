import sys
from PyQt5.QtWidgets import QApplication
from src.vista.InterfazAutoPerfecto import App_AutoPerfecto
from src.logica.Logica_mock import Logica_mock
from src.logica.propietario import Propietario

if __name__ == '__main__':
    # Punto inicial de la aplicación

    logica = Propietario()

    app = App_AutoPerfecto(sys.argv, logica)
    sys.exit(app.exec_())