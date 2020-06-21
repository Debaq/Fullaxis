
class Styles():
    btn_text = ("""
                QPushButton {
                Text-align:center;
                background: transparent;
                color:rgb(54,114,240);
                border: none;
                }
                QPushButton:hover {
                    color:rgb(54,156,240);
                }
                QPushButton:pressed {
                    color:rgb(35,187,255);
                }
                """)
    
    btn_flat = ("""
                QPushButton {
                    Text-align:center;
                    border: none;
                    color:rgb(238, 238, 236);
                    background-color: rgb(55, 144, 152);
                }
                QPushButton:hover {
                    background-color: rgb(0, 98, 106);
                }
                QPushButton:pressed {
                    text-decoration: underline;
                }
                """)
    
    btn_lateral = ("""
                QPushButton {
                    Text-align:center;
                    border: none;
                    color:rgb(238, 238, 236);
                    background-color: transparent;
                }
                QPushButton:hover {
                    background-color: rgb(244, 235, 235, 20);
                }
                QPushButton:pressed {
                    text-decoration: underline;
                    background-color: rgb(244, 235, 235, 20);
                }
                """)