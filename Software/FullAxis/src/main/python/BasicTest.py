import qtawesome as qta
from PySide6.QtCore import Signal
from PySide6.QtWidgets import QWidget, QPushButton

from lib.basic_test_ui import Ui_Test_basic
from lib.terminal_ui import Ui_terminal
from plug_hw import FullAxisReceptor, ReceiverData
from profile_data import ActivityData
from ui_helper import helpers
from Widgets_test import WidgetSOT, WidgetTUG, WidgetVNG


class Terminal(QWidget, Ui_terminal):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)

class  BasicTest(QWidget, Ui_Test_basic):
    save_true = Signal(bool) #emite señal True al guardar la información
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.buttons_disabled = True
        self.capture = False
        self.combo_serial_complete()
        self.btns_icons()
        self.btns_tools_clicked()
        
    ### funciones Genericas
    def set_data(self, profile:str, session, test:str) -> None:
        self.profile = profile
        self.session = session
        if test == "SOT":
            self.test = "SOT"
            self.create_sot_test()
        elif test == "TUG":
            self.test = "TUG"
            self.create_tug_test()
        elif test == "VNG":
            self.test = "VNG"
            self.create_vng_test()
        self.check_delay.stateChanged.connect(self.with_delay)
            
    def new(self):
        self.btn_capture.setEnabled(True)
        self.btn_save.setEnabled(False)
        self.btn_report.setEnabled(False)
        self.reset_graph()
    
    def test_variable(self):
        if self.capture == False:
            self.capture = True
            self.btn_capture.setText("Pause")
            time_max = self.time_max.value()
            self.widget.set_time_max(time_max)
        else:
            self.capture = False
            self.btn_capture.setText("Capture")
            
    def btns_icons(self) -> None:
        terminal = qta.icon('fa5s.terminal', color='#595959')
        icon_conect = qta.icon('fa5s.plug', color='#595959')
        self.btn_view_raw.setIcon(terminal)
        self.btn_connect.setIcon(icon_conect)
        
    def btns_tools_clicked(self) -> None:
        self.btn_connect.clicked.connect(self.connect_serial)
        self.btn_capture.clicked.connect(self.test_variable)
        self.btn_save.clicked.connect(self.save_data)
        self.btn_reset.clicked.connect(self.reset_graph)
        self.btn_view_raw.clicked.connect(self.terminal_active)

    ###Funciones de Serial
    def connect_serial(self):
        port = self.combo_serial.currentText()
        connection = FullAxisReceptor()
        connection.activate_connection(port)
        #connection.reset() #este quizas es el error de porque no funciona bien la conexión
        self.receiver = ReceiverData()
        self.receiver.start()
        self.receiver.set_connection(connection)
        self.receiver.data.connect(self.receive_data_and_graph)
        self.change_state_btn_connection(True)
    
    def disconnect_serial(self):
        if "receiver" in dir(self):
            self.receiver.set_connection(None)
            self.change_state_btn_connection(False)
            self.buttons_disabled = True
            self.btn_capture.setEnabled(False)
            self.btn_reset.setEnabled(False)
            self.btn_save.setEnabled(False)
    
    def change_state_btn_connection(self, activate:bool = True) -> None:
        self.btn_connect.setDisabled(activate)
        if self.btn_connect.isEnabled():
            self.btn_connect.setText("Connect")
        else:
            self.btn_connect.setText("Conected")
        self.combo_serial.setDisabled(activate)
        self.btn_view_raw.setEnabled(activate)
    
    def change_state_btn_capture(self, activate:bool = True) -> None:
        self.btn_capture.setEnabled(activate)
        if self.btn_capture.isEnabled():
            self.btn_capture.setText("Capture")
        self.btn_reset.setEnabled(activate)


    
    def combo_serial_complete(self) -> None:
        ports = FullAxisReceptor()
        icon_signal = qta.icon('fa5s.signal',color='#595959')
        for i in ports.search_ports():
            if i[2] != 'n/a':
                self.combo_serial.addItem(icon_signal, i[0])
                self.combo_serial.setCurrentText(i[0])
            else:
                self.combo_serial.addItem(i[0])
                
    def terminal_active(self) ->None:
        term = Terminal()
        term.show() 
        
    ###Funciones de Graph
    def receive_data_and_graph(self, data):
        if self.buttons_disabled:
            self.change_state_btn_capture(True)
            self.buttons_disabled = False
        if self.capture == True:
            if not self.widget.stop:
                self.widget.update_graph_display(data)
            else:
                self.capture = False
                self.btn_capture.setText("Capture")
                self.btn_save.setEnabled(True)
                
    def reset_graph(self):
        self.widget.reset_graph()

    def with_delay(self):
        self.widget.with_delay = self.check_delay.isChecked()
                
    ###Funciones de db
    def save_data(self):
        self.create_db(self.test)
        db = ActivityData()
        unique_id = self.activity_data['unique_id']
        data = self.widget.get_data()
        db.save_data(self.profile, unique_id, data)
        self.btn_capture.setEnabled(False)
        self.btn_reset.setEnabled(False)
        self.save_true.emit(True)
    
    def data_full(self):
        return self.widget.not_empty_data()
        
    def get_unique_id(self) -> str:
        return self.activity_data['unique_id']
            
    def create_db(self, type_test):
        db = ActivityData()
        self.activity_data = db.create_activity(self.profile, self.session, type_test)    

    ### Funciones VNG
    def create_vng_test(self) -> None: 
        self.widget = WidgetVNG()
        helpers.reset_layout(self, self.layout_test)
        self.layout_test.addWidget(self.widget)
        
                  
    ### Funciones TUG
    def create_tug_test(self) -> None:
        self.widget = WidgetTUG()
        helpers.reset_layout(self, self.layout_test)
        self.layout_test.addWidget(self.widget)
        
    ### Funciones SOT
    def create_sot_test(self):
        self.widget = WidgetSOT()
        helpers.reset_layout(self, self.layout_test)
        self.layout_test.addWidget(self.widget)
        self.create_btn_sot()
    
    def create_btn_sot(self):
        btn_prev = QPushButton("<")
        btn_prox = QPushButton(">")
        self.move_cond.addWidget(btn_prev)
        self.move_cond.addWidget(btn_prox)
        btn_prev.clicked.connect(lambda: self.move_cond_sot(-1))
        btn_prox.clicked.connect(lambda:self.move_cond_sot(1))
        
    def move_cond_sot(self, btn):
        if btn == -1:
            self.widget.move_cond_sot(-1)
        if btn == 1:
            self.widget.move_cond_sot(1)
        
