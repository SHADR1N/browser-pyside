import sys
import time
import traceback

from PySide6.QtCore import QUrl, QTimeZone, QTimer, QCoreApplication, QRect, QMetaObject, Qt, QSize, Signal
from PySide6.QtGui import QIcon, QAction, QCursor
from PySide6.QtWidgets import QApplication, QMainWindow, QStatusBar, QTabWidget, QToolBar, QTabBar, QToolButton, \
    QPushButton, QStyle, QWidget, QHBoxLayout, QLabel, QLineEdit, QVBoxLayout, QSizePolicy, QSplitter
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtNetwork import QNetworkProxyFactory, QNetworkProxy
from PySide6.QtWebEngineCore import QWebEngineSettings, QWebEngineProfile, QWebEnginePage


class WebBrowser(QMainWindow):
    def __init__(self):
        super().__init__()

        self.profile = None
        self.tabs = QTabWidget(self)

        # Properties
        self.tabs.setMovable(True)
        self.tabs.setTabsClosable(True)

        self.setCentralWidget(self.tabs)

        icon = QIcon("images/add.png")
        size = QSize(20, 20)

        self.add_tab_button = QPushButton(self)
        self.add_tab_button.setIcon(icon)
        self.add_tab_button.setFixedSize(size)

        self.add_tab_button.clicked.connect(self.add_new_tab)
        self.tabs.setCornerWidget(self.add_tab_button, Qt.Corner.TopRightCorner)
        self.setGeometry(100, 100, 800, 600)
        self.connect_proxy()
        self.settings_browser()

    def settings_browser(self):
        # Create a profile with WebRTC enabled
        self.profile = QWebEngineProfile.defaultProfile()
        settings = self.profile.settings()

        settings.setAttribute(QWebEngineSettings.WebAttribute.WebRTCPublicInterfacesOnly, False)
        settings.setAttribute(QWebEngineSettings.WebAttribute.WebGLEnabled, False)
        self.add_new_tab(qurl="https://browserleaks.com/webrtc")

    def connect_proxy(self):
        # Add user proxy authentication
        self.proxy_auth = QNetworkProxy()
        self.proxy_auth.setType(QNetworkProxy.HttpProxy)
        self.proxy_auth.setHostName("138.128.91.186")
        self.proxy_auth.setPort(8000)
        self.proxy_auth.setUser("pcFjWh")
        self.proxy_auth.setPassword("6QNzMN")
        QNetworkProxy.setApplicationProxy(self.proxy_auth)

    def get_page_browser(self, qurl):
        verticalLayout_2 = QVBoxLayout(self)
        verticalLayout_2.setObjectName(u"verticalLayout_2")
        widget = QWidget(self)
        widget.setObjectName(u"widget")
        verticalLayout = QVBoxLayout(widget)
        verticalLayout.setSpacing(5)
        verticalLayout.setObjectName(u"verticalLayout")
        verticalLayout.setContentsMargins(0, 0, 0, 0)
        widget_3 = QWidget(widget)
        widget_3.setObjectName(u"widget_3")
        horizontalLayout = QHBoxLayout(widget_3)
        horizontalLayout.setSpacing(5)
        horizontalLayout.setObjectName(u"horizontalLayout")
        horizontalLayout.setContentsMargins(0, 0, 0, 0)

        back = QIcon("images/back.png")
        forward = QIcon("images/forward.png")
        refresh = QIcon("images/refresh.png")
        home = QIcon("images/home.png")
        debug = QIcon("images/debug.png")
        size = QSize(20, 20)

        toolButton = QToolButton(widget_3)
        toolButton.setIcon(back)
        toolButton.setFixedSize(size)
        toolButton.clicked.connect(lambda: browser.back())
        horizontalLayout.addWidget(toolButton)

        toolButton_2 = QToolButton(widget_3)
        toolButton_2.setIcon(forward)
        toolButton_2.setFixedSize(size)
        toolButton_2.clicked.connect(lambda: browser.forward())
        horizontalLayout.addWidget(toolButton_2)

        toolButton_3 = QToolButton(widget_3)
        toolButton_3.setIcon(refresh)
        toolButton_3.setFixedSize(size)
        toolButton_3.clicked.connect(lambda: browser.reload())
        horizontalLayout.addWidget(toolButton_3)

        toolButton_4 = QToolButton(widget_3)
        toolButton_4.setIcon(home)
        toolButton_4.setFixedSize(size)
        toolButton_4.clicked.connect(lambda: self.navigate_home(browser))
        horizontalLayout.addWidget(toolButton_4)

        toolButton_5 = QToolButton(widget_3)
        toolButton_5.setIcon(debug)
        toolButton_5.setFixedSize(size)
        toolButton_5.clicked.connect(lambda: self.start_script(browser))
        horizontalLayout.addWidget(toolButton_5)

        lineEdit = QLineEdit(widget_3)
        lineEdit.returnPressed.connect(lambda: self.navigate_to_url(lineEdit, browser))
        horizontalLayout.addWidget(lineEdit)

        verticalLayout.addWidget(widget_3, 0, Qt.AlignTop)

        widget_2 = QWidget(widget)
        widget_2.setObjectName(u"widget_2")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(widget_2.sizePolicy().hasHeightForWidth())
        widget_2.setSizePolicy(sizePolicy)
        verticalLayout_3 = QVBoxLayout(widget_2)
        verticalLayout_3.setSpacing(0)
        verticalLayout_3.setObjectName(u"verticalLayout_3")
        verticalLayout_3.setContentsMargins(0, 0, 0, 0)

        browser = QWebEngineView(widget_2)

        verticalLayout_3.addWidget(browser)

        verticalLayout.addWidget(widget_2)

        verticalLayout_2.addWidget(widget)

        verticalLayout.addWidget(widget_2)

        verticalLayout_2.addWidget(widget)
        browser.urlChanged.connect(lambda event: self.update_url_bar(lineEdit, event, browser))
        page = QWebEnginePage(self.profile, browser)
        page.triggerAction(QWebEnginePage.InspectElement)
        browser.setPage(page)
        browser.setUrl(qurl)
        self.start_script(browser)
        return widget, browser

    def add_new_tab(self, qurl=None, label="Новая вкладка"):
        if qurl is None:
            qurl = QUrl('')
        else:
            qurl = QUrl(qurl)

        browser, wid = self.get_page_browser(qurl)

        widget = QWidget(self)
        widget.setStyleSheet("* {"
                             "margin: 0px;"
                             "padding: 0px;"
                             "border: 0px;"
                             "}")
        widget.setObjectName(u"widget")
        horizontalLayout = QHBoxLayout(widget)
        horizontalLayout.setSpacing(0)
        horizontalLayout.setObjectName(u"horizontalLayout")

        toolButton = QPushButton(widget)
        toolButton.setText("")
        horizontalLayout.addWidget(toolButton, 0, Qt.AlignmentFlag.AlignCenter)

        icon = QIcon()
        icon.addFile('images/close.png', QSize(), QIcon.Normal, QIcon.Off)
        toolButton.setIcon(icon)
        size = QSize(18, 18)
        toolButton.setCursor(QCursor(Qt.PointingHandCursor))

        toolButton.setFixedSize(size)
        toolButton.setIconSize(size)

        i = self.tabs.addTab(browser, label)
        toolButton.clicked.connect(self.close_current_tab)
        self.tabs.setCurrentIndex(i)

        # Add close button to tab
        self.tabs.tabBar().setTabButton(i, QTabBar.RightSide, widget)

    def close_current_tab(self):
        if self.tabs.count() == 1:
            self.close()
        else:
            index = self.tabs.currentIndex()
            self.tabs.removeTab(index)

    @staticmethod
    def navigate_home(browser):
        browser.setUrl(QUrl('https://www.google.com'))

    @staticmethod
    def start_script(browser):
        with open("js/autoscript.js", "r", encoding="utf-8") as file:
            script = file.read()
        browser.page().runJavaScript(script)

    def navigate_to_url(self, url_bar, brow):
        url = url_bar.text()
        brow.setUrl(QUrl(url))

    def update_url_bar(self, url_bar, q, brow):
        index = self.tabs.currentIndex()
        self.tabs.setTabText(index, brow.title())
        url_bar.setText(q.toString())


if __name__ == '__main__':
    app = QApplication(sys.argv)

    browser = WebBrowser()
    browser.show()

    sys.exit(app.exec())