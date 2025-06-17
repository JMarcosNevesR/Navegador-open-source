import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QToolBar, QAction, QLineEdit
from PyQt5.QtWebEngineWidgets import QWebEngineView

class Navegador(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Navegador Open Source")
        self.setGeometry(100, 100, 1200, 800)

        self.browser = QWebEngineView()
        self.browser.setUrl("https://www.google.com")
        self.setCentralWidget(self.browser)

        self.barra_navegacao = QToolBar()
        self.addToolBar(self.barra_navegacao)

        voltar_btn = QAction("Voltar", self)
        voltar_btn.triggered.connect(self.browser.back)
        self.barra_navegacao.addAction(voltar_btn)

        avancar_btn = QAction("Avançar", self)
        avancar_btn.triggered.connect(self.browser.forward)
        self.barra_navegacao.addAction(avancar_btn)

        recarregar_btn = QAction("Recarregar", self)
        recarregar_btn.triggered.connect(self.browser.reload)
        self.barra_navegacao.addAction(recarregar_btn)

        self.url_barra = QLineEdit()
        self.url_barra.returnPressed.connect(self.navegar_para_url)
        self.barra_navegacao.addWidget(self.url_barra)

        self.browser.urlChanged.connect(self.atualizar_url)

    def navegar_para_url(self):
        url = self.url_barra.text()
        if not url.startswith("http"):
            url = "http://" + url
        self.browser.setUrl(url)

    def atualizar_url(self, q):
        self.url_barra.setText(q.toString())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = Navegador()
    janela.show()
    sys.exit(app.exec_())
