import sys
import time
import traceback

from style import style_application

from PySide6.QtCore import QUrl, QTimeZone, QTimer, QCoreApplication, QRect, QMetaObject, Qt, QSize, Signal
from PySide6.QtGui import QIcon, QAction, QCursor, QPixmap, QMouseEvent
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
        self.tabs.tabCloseRequested.connect(lambda index: self.close_current_tab(index))
        self.tabs.tabBarClicked.connect(self.click_to_tab)

        # Properties
        self.tabs.setTabsClosable(True)
        self.tabs.setMovable(True)
        self.tabs.setDocumentMode(True)
        self.tabs.setElideMode(Qt.ElideRight)
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

    def click_to_tab(self, index):
        mouse_button = self.mouseButton()
        if mouse_button == "MidButton":
            self.close_current_tab(index)

    def mouseButton(self):
        buttons = {Qt.LeftButton: 'LeftButton', Qt.MouseButton.RightButton: 'RightButton', Qt.MouseButton.MiddleButton: 'MidButton'}
        return buttons.get(QApplication.mouseButtons(), 'Unknown')

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

    def get_page_browser(self, qurl, name_tab, icons):
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
        browser.urlChanged.connect(lambda event: self.update_url_bar(lineEdit, event, browser, name_tab))
        browser.loadFinished.connect(lambda event: self.update_url_bar(lineEdit, event, browser, name_tab))

        page = QWebEnginePage(self.profile, browser)
        page.triggerAction(QWebEnginePage.InspectElement)
        page.iconChanged.connect(lambda event: self.set_icon_page(event, icons))

        browser.setPage(page)
        browser.setUrl(qurl)

        self.start_script(browser)
        return widget, browser

    def set_icon_page(self, event, icons):
        # Get the web page icon as a QIcon
        icon_qt = QIcon(event)
        if icon_qt.isNull():
            icon_qt = QIcon("images/load.gif")

        # Set the web page icon to the label
        icons.setPixmap(icon_qt.pixmap(100, 100))

    def add_new_tab(self, qurl=None, label=None):
        if qurl is None:
            qurl = QUrl('')
        else:
            qurl = QUrl(qurl)

        if label is None:
            label = "Новая вкладка"

        widget = QWidget(self.tabs)
        widget.adjustSize()
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setWidthForHeight(widget.sizePolicy().hasWidthForHeight())
        widget.setSizePolicy(sizePolicy1)

        widget.setStyleSheet("* {"
                             "margin: 0px;"
                             "padding: 0px;"
                             "border: 0px;"
                             "}")
        widget.setObjectName(u"widget")
        horizontalLayout = QHBoxLayout(widget)
        horizontalLayout.setSpacing(5)
        horizontalLayout.setObjectName(u"horizontalLayout")

        toolButton = QPushButton(widget)
        toolButton.setText("")

        name_tab = QLabel(widget)
        name_tab.setText(str(label))
        name_tab.adjustSize()

        size = QSize(18, 18)

        icon = QIcon("images/load.gif")
        icons = QLabel(widget)
        icons.setPixmap(icon.pixmap(100, 100))
        icons.setFixedSize(size)
        icons.setScaledContents(True)
        icons.setGeometry(1, 1, 18, 18)

        horizontalLayout.addWidget(icons, 0, Qt.AlignmentFlag.AlignLeft)
        horizontalLayout.addWidget(name_tab, 1, Qt.AlignmentFlag.AlignLeft)

        browser, wid = self.get_page_browser(qurl, name_tab, icons)
        i = self.tabs.addTab(browser, "")
        self.tabs.update()
        self.tabs.setCurrentIndex(i)

        # Add close button to tab
        self.tabs.tabBar().setTabButton(i, QTabBar.ButtonPosition.LeftSide, widget)

    def close_current_tab(self, index):
        if self.tabs.count() == 1:
            self.close()
        else:
            self.tabs.removeTab(index)

    @staticmethod
    def navigate_home(browser):
        browser.setUrl(QUrl('https://www.google.com'))

    @staticmethod
    def start_script(browser):
        with open("js/autoscript.js", "r", encoding="utf-8") as file:
            script = file.read()
        browser.page().runJavaScript(script)

    @staticmethod
    def navigate_to_url(url_bar, brow):
        url = url_bar.text()
        brow.setUrl(QUrl(url))

    def update_url_bar(self, url_bar, q, brow, name_tab):
        title = brow.title()
        if not title:
            title = "Новая вкладка"

        if title == "about:blank":
            title = "Новая вкладка"

        if title.startswith("http"):
            title = "Загрузка..."

        try:
            name_tab.setText(title)
            if not isinstance(q, bool):
                url_bar.setText(q.toString())
        except:
            pass


if __name__ == '__main__':
    app = QApplication(["", '--no-sandbox'])
    app.setStyleSheet(style_application)
    browser = WebBrowser()
    browser.show()

    sys.exit(app.exec())
