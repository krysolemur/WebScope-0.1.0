# application.py

# Import system files
import bcrypt # type: ignore
import hashlib
import sys


from PySide6 import QtWidgets, QtCore, QtUiTools, QtGui # type: ignore
from PySide6.QtWidgets import QDialog, QLabel, QVBoxLayout, QApplication, QMessageBox, QHBoxLayout, QPushButton, QVBoxLayout, QComboBox, QLineEdit # type: ignore
from PySide6.QtCore import QTimer, QFile # type: ignore
from PySide6.QtUiTools import QUiLoader # type: ignore

# Importing program files
from libs.MainWindow.mainwindow import MainWindow
from libs.Logging.logging import Logging
from libs.Errors.errors import Error
from libs.Errors.exceptions import *
from Users.usersmanager import UsersManager
from Users.configmanager import ConfigManager

# Class for managing whole application
class Application(Logging, QApplication):
    def __init__(self) -> None:
        '''
        Set application parametres, init parents and other.
        '''
        # Init parents
        super().__init__(sys.argv)

        # Start QTimer
        self.timer = QTimer()

        # Info message
        self.printi(msg="Creating application")

        '''
        Setting all applications variables.
        '''

        # Application version
        self.version = "0.1.0"

        # User variable
        self.user = "Default"

        '''
        Inicializing all neccessary modules.
        '''

        # Users module
        self.users = UsersManager()

        # Config module
        self.config = ConfigManager()

        # Error module
        self.error = Error()

        # Window module
        self.window = MainWindow(app=self)

        '''
        Running program.
        '''

        # Setup application
        self._setup()

    '''
    Private functions.
    '''

    # Setup function
    def _setup(self) -> None:
        # Process index variable
        self.process_index = 0

        '''
        Load ui for custom restart dialog.
        '''

        # Load Ui file
        ui_file = QtCore.QFile("libs/QtGuiFiles/SetupDialog.ui")

        # Read Ui file
        ui_file.open(QtCore.QFile.ReadOnly)

        # Load to setupDialog
        self.setupDialog = QtUiTools.QUiLoader().load(ui_file)

        # Process events
        QtWidgets.QApplication.processEvents()

        # Close Ui file
        ui_file.close()

        '''
        Set window properties, title, size and more.
        '''

        # Dialog properties like title, size and more
        self.setupDialog.setWindowTitle(f"WebScope | {self.version} | Inicializing")

        # Set size
        self.setupDialog.resize(600, 75)

        # Exec setupDialog
        self.setupDialog.show()

        '''
        Set timer for loading bar.
        '''

        # Run all setup processes with pause
        self.timer.timeout.connect(self._run_next_process)

        # Small pause
        self.timer.start(500)

    # Run next proccess function
    def _run_next_process(self) -> None:
        # List of all proccesses with their labels
        all_proccess = [
            (self._checkNetworkConnection, "Checking internet connection..."),
            (self._checkForUpdates, "Checking for updates..."),
            (self._checkUserDir, "Checking user directory"),
            (self._checkConfigDir, "Checking config directory..."),
            (self._login, "Logging in...")
        ]

        '''
        Close dialog, open main window and stop timer when loop ends.
        '''
        # Check if all process was runned
        if self.process_index == len(all_proccess):
            # Stop timer
            self.timer.stop()

            # Delete timer
            del(self.timer)

            # Close loading window
            self.setupDialog.close()

            # Delete setup window
            del(self.setupDialog)

            # Show main window
            self.window.show()

            # End loop 
            return

        '''
        Run all proccess with try except block for catching errors.
        '''

        # Get one process
        process = all_proccess[self.process_index]

        # Set status label text
        self.setupDialog.statusLabel.setText("...")

        # Try-except for catching errors
        try:    
            # Check if process is call able
            if callable(process[0]):
                # Run process
                process[0]()

            '''
            Set label properties and loading bar actions.
            '''

            # Set loading label text
            self.setupDialog.loadingLabel.setText(process[1])

            # Set OK Color
            self.setupDialog.statusLabel.setStyleSheet("color: #00ff00")

            # Set OK status of function
            self.setupDialog.statusLabel.setText("OK")

            # Set progressBar value
            self.setupDialog.loadingBar.setValue(self.setupDialog.loadingBar.value() + (100 // len(all_proccess)))

            # OK message
            self.printo(msg="", function=process[0].__name__)
        except Exception as e:
            '''
            Set error look.
            '''

            # Error message
            self.printe(exception=e, msg="", function=self._run_next_process.__name__)

            # Set ERROR Color
            self.setupDialog.statusLabel.setStyleSheet("color: #ff0000")

            # Set ERROR status of function
            self.setupDialog.statusLabel.setText("ERROR")

            # Stop timer
            self.timer.stop()

        # Count + 1 process index
        self.process_index += 1

    # Checking internet connection
    def _checkNetworkConnection(self) -> None:
        None

    # Function that check for updates
    def _checkForUpdates(self) -> None:
        None

    # Check user directory
    def _checkUserDir(self) -> None:
        None

    # Checking config files
    def _checkConfigDir(self) -> None:
        None

    # Login function
    def _login(self) -> None:
        '''
        Add login forms to setup dialog.
        '''

        # Stop timer
        self.timer.stop()

        # Username layout
        self.setupDialog.usernameLayout = QHBoxLayout()

        # Password layout
        self.setupDialog.pwdLayout = QHBoxLayout()

        # Buttons layout
        self.setupDialog.buttonsLayout = QHBoxLayout()

        # Username label
        self.setupDialog.usernameLabel = QLabel("Username:")

        # Password label
        self.setupDialog.pwdLabel = QLabel("Password:")

        # Password line edit
        self.setupDialog.passwordLineEdit = QLineEdit()

        # Username combobox
        self.setupDialog.usernameComboBox = QComboBox()

        # Login button
        self.setupDialog.loginButton = QPushButton("Login")

        # Reset password button
        self.setupDialog.resetpwdButton = QPushButton("Reset password")

        # Add label to username layout
        self.setupDialog.usernameLayout.addWidget(self.setupDialog.usernameLabel)

        # Add combo box to username layout
        self.setupDialog.usernameLayout.addWidget(self.setupDialog.usernameComboBox)

        # Add label to password layout
        self.setupDialog.pwdLayout.addWidget(self.setupDialog.pwdLabel)

        # Add line edit to password layout
        self.setupDialog.pwdLayout.addWidget(self.setupDialog.passwordLineEdit)

        # Add reset password to button layout
        self.setupDialog.buttonsLayout.addWidget(self.setupDialog.resetpwdButton)

        # Add login button to button layout
        self.setupDialog.buttonsLayout.addWidget(self.setupDialog.loginButton)

        # Add username layout to login layout
        self.setupDialog.loginLayout.addLayout(self.setupDialog.usernameLayout)

        # Add username layout to login layout
        self.setupDialog.loginLayout.addLayout(self.setupDialog.pwdLayout)

        # Add username layout to login layout
        self.setupDialog.loginLayout.addLayout(self.setupDialog.buttonsLayout)

        # Set login button diabled
        self.setupDialog.loginButton.setEnabled(False)

        # Set login button diabled
        self.setupDialog.passwordLineEdit.setEnabled(True)

        '''
        Set window for another layout.
        '''

        # Resize dialog
        self.setupDialog.resize(self.setupDialog.width(), self.setupDialog.sizeHint().height())

        # Center window
        self.window._center(self.setupDialog)

        '''
        Add all users to user combo box.
        '''

        # User variable from users manager
        for user in self.users.all_users:
            # Add user to combo box
            self.setupDialog.usernameComboBox.addItem(user)

        '''
        Button actions.
        '''

        # Login button action
        self.setupDialog.loginButton.clicked.connect(self._handle_login)

        # Set enabled login buttin if there is any text 
        self.setupDialog.passwordLineEdit.textChanged.connect(self._update_login_button)

        # Set enabled login buttin if there is any text 
        self.setupDialog.usernameComboBox.currentTextChanged.connect(self._update_login_button)

        # Set disabled passwor field when is default user
        self.setupDialog.usernameComboBox.currentTextChanged.connect(lambda text: self.setupDialog.passwordLineEdit.setEnabled(text != "Default"))

    # Function that update login button set enabled True/False
    def _update_login_button(self, _=None):
        # Check password
        password_ok = bool(self.setupDialog.passwordLineEdit.text().strip())

        # Check user
        user_ok = self.setupDialog.usernameComboBox.currentText() != "Default"

        # Enable button
        if not user_ok:
            # If default user, continue without password
            self.setupDialog.loginButton.setEnabled(True)  

            # Set reset password to disabled
            self.setupDialog.resetpwdButton.setEnabled(False)
        else:
            # Else with password
            self.setupDialog.loginButton.setEnabled(bool(password_ok))  
                    
    # Handle login function
    def _handle_login(self) -> None:
        '''
        Get username, password, hashed password with salt and loing using login function from usermanager module.
        '''
        # Get user name value
        username = self.setupDialog.usernameComboBox.currentText()

        # Get password value
        password = self.setupDialog.passwordLineEdit.text()

        # Check if user is default
        if username == "Default":
            # Set password to ""
            password = ""

        # Encode password
        pwd = password.encode()

        # Generate hash with random salt
        hashed = bcrypt.hashpw(pwd, bcrypt.gensalt())

        # Login using login function from user manager
        if self.users.login(username, hashed):
            # Set ERROR Color
            self.setupDialog.statusLabel.setStyleSheet("color: #00ff00")

            # Set ERROR status of function
            self.setupDialog.statusLabel.setText("OK")

            # Start timer
            self.timer.start()
        else: 
            # Set ERROR Color
            self.setupDialog.statusLabel.setStyleSheet("color: #ff0000")

            # Set ERROR status of function
            self.setupDialog.statusLabel.setText("ERROR")

            # Raise login error
            raise LoginError(username)

    '''
    Public functions.
    '''
