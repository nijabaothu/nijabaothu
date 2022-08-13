from .templates import *
from PyQt5 import QtCore,QtWidgets,QtGui
import gspread
import requests
from .modules.main_funct import MainFunction
from .modules.tool_funct import ToolFunctiton
import concurrent.futures







LIST_KU = []
LIST_THA = []

def connect_googlesheet(api_url):
	global client
	reponse = requests.get(api_url).json()
	client = gspread.service_account_from_dict(reponse)

class MainWindow(QtWidgets.QMainWindow,
	templates.UiMain,
	MainFunction,
	ToolFunctiton):

	
	"""docstring for MainWindow"""
	def __init__(self,parent=None):
		super(MainWindow, self).__init__(parent)
		self.setupUi(self)
		self.setupMain()
		self.setupButton()	
		self.auto_reload()

	def dangkychua(self):
		x=("{} *-đăng ký* chưa {} *({})*".format(self.tentaikhoan_le.text().strip(),"ạ" if self.xungho_mkt_cbb.currentText() == "em" else "nhé",self.daily_mkt_cbb.currentText()))
		self.noidungcopy_tb.setText(x)
		a = QtWidgets.QApplication.clipboard()
		a.setText(x)
	def dangkychua2(self):
		x=("{} *-đăng ký* chưa {} *({})*".format(self.tentaikhoan_t2_le.text().strip(),"ạ" if self.xungho_t2_btn.currentText() == "em" else "nhé",self.daily_t2_btn.currentText()))
		self.noidungcopy_t2_tb.setText(x)
		a = QtWidgets.QApplication.clipboard()
		a.setText(x)
	def napchua(self):
		x=("{} *-nạp lần đầu* chưa {} *({})*".format(self.tentaikhoan_le.text().strip(),"ạ" if self.xungho_mkt_cbb.currentText() == "em" else "nhé",self.daily_mkt_cbb.currentText()))
		self.noidungcopy_tb.setText(x)
		a = QtWidgets.QApplication.clipboard()
		a.setText(x)
	def napchua2(self):
		x=("{} *-nạp lần đầu* chưa {} *({})*".format(self.tentaikhoan_t2_le.text().strip(),"ạ" if self.xungho_t2_btn.currentText() == "em" else "nhé",self.daily_t2_btn.currentText()))
		self.noidungcopy_t2_tb.setText(x)
		a = QtWidgets.QApplication.clipboard()
		a.setText(x)
	def tainapchua(self):
		x=("{} *-tái nạp chưa* {} *({})*".format(self.tentaikhoan_le.text().strip(),"ạ" if self.xungho_mkt_cbb.currentText() == "em" else "nhé",self.daily_mkt_cbb.currentText()))
		self.noidungcopy_tb.setText(x)
		a = QtWidgets.QApplication.clipboard()
		a.setText(x)
	def cokhong(self):
		x=("{} *-có không* {} *({})*".format(self.tentaikhoan_le.text().strip(),"ạ" if self.xungho_mkt_cbb.currentText() == "em" else "nhé",self.daily_mkt_cbb.currentText()))
		self.noidungcopy_tb.setText(x)
		a = QtWidgets.QApplication.clipboard()
		a.setText(x)
	def cokhong2(self):
		x=("{} *-có không* {} *({})*".format(self.tentaikhoan_t2_le.text().strip(),"ạ" if self.xungho_t2_btn.currentText() == "em" else "nhé",self.daily_t2_btn.currentText()))
		self.noidungcopy_t2_tb.setText(x)
		a = QtWidgets.QApplication.clipboard()
		a.setText(x)
	def conchoikhong(self):
		x=("{} *-còn chơi* không {} *({})*".format(self.tentaikhoan_le.text().strip(),"ạ" if self.xungho_mkt_cbb.currentText() == "em" else "nhé",self.daily_mkt_cbb.currentText()))
		self.noidungcopy_tb.setText(x)
		a = QtWidgets.QApplication.clipboard()
		a.setText(x)
	def conchoikhong2(self):
		x=("{} *-còn chơi* không {} *({})*".format(self.tentaikhoan_t2_le.text().strip(),"ạ" if self.xungho_t2_btn.currentText() == "em" else "nhé",self.daily_t2_btn.currentText()))
		self.noidungcopy_t2_tb.setText(x)
		a = QtWidgets.QApplication.clipboard()
		a.setText(x)

	def trangthaitk(self):
		x=("{} *-trạng thái* như thế nào {} *({})*".format(self.tentaikhoan_le.text().strip(),"ạ" if self.xungho_mkt_cbb.currentText() == "em" else "nhé",self.daily_mkt_cbb.currentText()))
		self.noidungcopy_tb.setText(x)
		a = QtWidgets.QApplication.clipboard()
		a.setText(x)
	def trangthaitk2(self):
		x=("{} *-trạng thái* như thế nào {} *({})*".format(self.tentaikhoan_t2_le.text().strip(),"ạ" if self.xungho_t2_btn.currentText() == "em" else "nhé",self.daily_t2_btn.currentText()))
		self.noidungcopy_t2_tb.setText(x)
		a = QtWidgets.QApplication.clipboard()
		a.setText(x)

	def chuyenlinkchua(self):
		x=("{} *-chuyển về* chưa {} *({})*".format(self.tentaikhoan_le.text().strip(),"ạ" if self.xungho_mkt_cbb.currentText() == "em" else "nhé",self.daily_mkt_cbb.currentText()))
		self.noidungcopy_tb.setText(x)
		a = QtWidgets.QApplication.clipboard()
		a.setText(x)
	def napthemchua(self):
		x=("{} *-nay có nạp* không {} *({})*".format(self.tentaikhoan_le.text().strip(),"ạ" if self.xungho_mkt_cbb.currentText() == "em" else "nhé",self.daily_mkt_cbb.currentText()))
		self.noidungcopy_tb.setText(x)
		a = QtWidgets.QApplication.clipboard()
		a.setText(x)	
	def monapmail(self):
		x=("- KU: {}\n- Từ: {}\n> openbet999@gmail.com\nVui lòng kiểm tra chứng từ và xử lý MỞ NẠP giúp mình. Xin cảm ơn!".format(self.tentaikhoan_le.text().strip(),self.mail_le.text()))
		self.noidungcopy_tb.setText(x)
		a = QtWidgets.QApplication.clipboard()
		a.setText(x)
		#Code nút bấm K team
	def dangky(self):
		x=("{} {} hướng dẫn *đăng ký* giúp {} nhé. *({})*".format("Zl" if self.tlzlfb_cbb.currentText() == "Zalo" \
			else  "Fb" if self.tlzlfb_cbb.currentText() == "Facebook" else "Tl",self.tenkhach_le.text(),self.xungho_k_cbb.currentText(),self.daily_k_cbb.currentText()))
		self.noidungcopy_tb.setText(x)
		a = QtWidgets.QApplication.clipboard()
		a.setText(x)
	def taiappku(self):
		x=("{} {} hướng dẫn *tải app KU* giúp {} nhé.".format("Zl" if self.tlzlfb_cbb.currentText() == "Zalo" \
			else  "Fb" if self.tlzlfb_cbb.currentText() == "Facebook" else "Tl",self.tenkhach_le.text(),self.xungho_k_cbb.currentText()))
		self.noidungcopy_tb.setText(x)
		a = QtWidgets.QApplication.clipboard()
		a.setText(x) 
	def taiapptha(self):
		x=("{} {} hướng dẫn *tải app THA* giúp {} nhé.".format("Zl" if self.tlzlfb_cbb.currentText() == "Zalo" \
			else  "Fb" if self.tlzlfb_cbb.currentText() == "Facebook" else "Tl",self.tenkhach_le.text(),self.xungho_k_cbb.currentText()))
		self.noidungcopy_tb.setText(x)
		a = QtWidgets.QApplication.clipboard()
		a.setText(x) 
	def laylaitk(self):
		x=("{} {} hướng dẫn *lấy lại mật khẩu* giúp {} nhé. *({})*".format("Zl" if self.tlzlfb_cbb.currentText() == "Zalo" \
			else  "Fb" if self.tlzlfb_cbb.currentText() == "Facebook" else "Tl",self.tenkhach_le.text(),self.xungho_k_cbb.currentText(),self.daily_k_cbb.currentText()))
		self.noidungcopy_tb.setText(x)
		a = QtWidgets.QApplication.clipboard()
		a.setText(x) 
	def monapku(self):
		x=("{} {} hướng dẫn *mở nạp KU* giúp {} nhé.".format("Zl" if self.tlzlfb_cbb.currentText() == "Zalo" \
			else  "Fb" if self.tlzlfb_cbb.currentText() == "Facebook" else "Tl",self.tenkhach_le.text(),self.xungho_k_cbb.currentText()))
		self.noidungcopy_tb.setText(x)
		a = QtWidgets.QApplication.clipboard()
		a.setText(x)  
	def monaptha(self):
		x=("{} {} hướng dẫn *mở nạp THA* giúp {} nhé.".format("Zl" if self.tlzlfb_cbb.currentText() == "Zalo" \
			else  "Fb" if self.tlzlfb_cbb.currentText() == "Facebook" else "Tl",self.tenkhach_le.text(),self.xungho_k_cbb.currentText()))
		self.noidungcopy_tb.setText(x)
		a = QtWidgets.QApplication.clipboard()
		a.setText(x)  
	def nhandiem(self):
		x=("{} {} hướng dẫn *nhận điểm* giúp {} nhé. *({})*".format("Zl" if self.tlzlfb_cbb.currentText() == "Zalo" \
			else  "Fb" if self.tlzlfb_cbb.currentText() == "Facebook" else "Tl",self.tenkhach_le.text(),self.xungho_k_cbb.currentText(),self.daily_k_cbb.currentText()))
		self.noidungcopy_tb.setText(x)
		a = QtWidgets.QApplication.clipboard()
		a.setText(x)
	def naptien(self):
		x=("{} {} hướng dẫn *nạp tiền* giúp {} nhé. *({})*".format("Zl" if self.tlzlfb_cbb.currentText() == "Zalo" \
			else  "Fb" if self.tlzlfb_cbb.currentText() == "Facebook" else "Tl",self.tenkhach_le.text(),self.xungho_k_cbb.currentText(),self.daily_k_cbb.currentText()))
		self.noidungcopy_tb.setText(x)
		a = QtWidgets.QApplication.clipboard()
		a.setText(x)  
	def tainap(self):
		x=("{} {} hướng dẫn *tái nạp* giúp {} nhé. *({})*".format("Zl" if self.tlzlfb_cbb.currentText() == "Zalo" \
			else  "Fb" if self.tlzlfb_cbb.currentText() == "Facebook" else "Tl",self.tenkhach_le.text(),self.xungho_k_cbb.currentText(),self.daily_k_cbb.currentText()))
		self.noidungcopy_tb.setText(x)
		a = QtWidgets.QApplication.clipboard()
		a.setText(x)
	def ruttien(self):
		x=("{} {} hướng dẫn *rút tiền* giúp {} nhé. *({})*".format("Zl" if self.tlzlfb_cbb.currentText() == "Zalo" \
			else  "Fb" if self.tlzlfb_cbb.currentText() == "Facebook" else "Tl",self.tenkhach_le.text(),self.xungho_k_cbb.currentText(),self.daily_k_cbb.currentText()))
		self.noidungcopy_tb.setText(x)
		a = QtWidgets.QApplication.clipboard()
		a.setText(x)
	def chuyenlinhbd12h(self):
		x = f"*Chuyển đại lý trong 12 tiếng*\nTên TK: {self.tentaikhoan_le.text().strip()}\nBiệt danh: {self.bietdanh_le.text()}\
		\nChuyển về: *{self.daily_mkt_cbb.currentText()}* .Xin cảm ơn!"
		self.noidungcopy_tb.setText(x)
		a = QtWidgets.QApplication.clipboard()
		a.setText(x)
	def chuyenlinhsdt12h(self):
		x = f"*Chuyển đại lý trong 12 tiếng*\nTên TK: {self.tentaikhoan_le.text().strip()}\nSĐT: {self.sodienthoai_le.text()}\
		\nChuyển về: *{self.daily_mkt_cbb.currentText()}* .Xin cảm ơn!'"
		self.noidungcopy_tb.setText(x)
		a = QtWidgets.QApplication.clipboard()
		a.setText(x)	
	def doitencungbp(self):
		x = f"*Cùng bộ phận* - NẠP LẦN ĐẦU\nTK: {self.tentaikhoan_le.text().strip()} - (DV..) => {self.daily_mkt_cbb.currentText()}  - Tên TT\nNhờ anh chị *đổi tên + link* giúp {self.xungho_mkt_cbb.currentText()} nhé!"
		self.noidungcopy_tb.setText(x)
		a = QtWidgets.QApplication.clipboard()
		a.setText(x)
	def doitenkhacbp(self):
		x = f"*Khác bộ phận* - NẠP LẦN ĐẦU\nTK: {self.tentaikhoan_le.text().strip()} (DV..) => {self.daily_mkt_cbb.currentText()}  - (Tên TT)\nNhờ anh chị *đổi tên + link* giúp {self.xungho_mkt_cbb.currentText()} nhé!"
		self.noidungcopy_tb.setText(x)
		a = QtWidgets.QApplication.clipboard()
		a.setText(x)
	def doilinkcungbp(self):
		x = f"*Cùng bộ phận* - TÁI NẠP\nTK: {self.tentaikhoan_le.text().strip()} - (DV..) => {self.daily_mkt_cbb.currentText()}  - Tên TT\nNhờ anh chị *đổi tên + link* giúp {self.xungho_mkt_cbb.currentText()} nhé!"
		self.noidungcopy_tb.setText(x)
		a = QtWidgets.QApplication.clipboard()
		a.setText(x)
	def doilinkkhacbp(self):
		x = f"*Khác bộ phận* - TÁI NẠP\nTK: {self.tentaikhoan_le.text().strip()} (DV..) => {self.daily_mkt_cbb.currentText()}  - (Tên TT)\nNhờ anh chị *đổi tên + link* giúp {self.xungho_mkt_cbb.currentText()} nhé!"
		self.noidungcopy_tb.setText(x)
		a = QtWidgets.QApplication.clipboard()
		a.setText(x)
	def lienhedangky(self):
		x = f"SĐT: {self.sodienthoai_le.text()}\nVui lòng kiểm tra giúp mình khách *ĐĂNG KÝ* không nhận được mã xác nhận. Xin cảm ơn!"
		self.noidungcopy_tb.setText(x)
		a = QtWidgets.QApplication.clipboard()
		a.setText(x)
	def dangkyncngoai(self):
		x = f"Tên TK: {self.tentaikhoan_le.text().strip()}\nBiệt danh: {self.bietdanh_le.text()}\nHọ tên: \nSĐT: {self.sodienthoai_le.text()}\nMã đại lý: *{self.daily_mkt_cbb.currentText()}*\nVui lòng hỗ trợ *khách ở nước ngoài TẠO TÀI KHOẢN* giúp mình. Xin cảm ơn!"
		self.noidungcopy_tb.setText(x)
		a = QtWidgets.QApplication.clipboard()
		a.setText(x)
	def nhandiemkho(self):
		x = f"KU - Nạp lần đầu\nTên TK: {self.tentaikhoan_le.text().strip()}\n- Nạp qua: \n- Số điểm: \n- Nội dung: \n- Thời gian: \nVui lòng hỗ trợ *nhận điểm* giúp mình. Xin cảm ơn!\n\nHV đã liên hệ CSKH nhận điểm 40 phút trước, chưa thấy lên điểm."
		self.noidungcopy_tb.setText(x)
		a = QtWidgets.QApplication.clipboard()
		a.setText(x)
	def doilinkskhongfile(self):
		x=("*CHƯA LƯU FILE*\nTK: {} - *(DV)* => *(DV)*\nnhờ {} đổi link giúp {} nhé!".format(self.tentaikhoan_le.text().strip(),"anh chị" if self.xungho_mkt_cbb.currentText() == "em" else "bạn",self.xungho_mkt_cbb.currentText()))
		self.noidungcopy_tb.setText(x)
		a = QtWidgets.QApplication.clipboard()
		a.setText(x)
	def doilinksnaplandau(self):
		x=("*NẠP LẦN ĐẦU*\nTK: {} - *(DV)* => *(DV)*\nnhờ {} đổi link giúp {} nhé!".format(self.tentaikhoan_le.text().strip(),"anh chị" if self.xungho_mkt_cbb.currentText() == "em" else "bạn",self.xungho_mkt_cbb.currentText()))
		self.noidungcopy_tb.setText(x)
		a = QtWidgets.QApplication.clipboard()
		a.setText(x)


	def kiemtra(self,input_name):

		if len(LIST_KU) <=0 or \
				len(LIST_KU) <=0:
			self.label.setText('Vui lòng nạp dữ liệu')
			return False 

		self.plainTextEdit_ku.setPlainText('')
		self.plainTextEdit_tha.setPlainText('')
		self.plainTextEdit_t2_ku.setPlainText('')
		self.plainTextEdit_t2_tha.setPlainText('')
		self.sokytu.setText('0')
		self.sokytu_t2.setText('0')
		username = input_name.text().upper().strip()
		skt = len(username)
		a = False
		if username =='':
			self.label.setText('Vui lòng nhập tên tk cần tìm')
			return 
		find_ku = []
		find_tha = []
		self.sokytu.setText(str(skt))
		self.sokytu_t2.setText(str(skt))
		for khach in LIST_KU:
			if username in khach:
				find_ku.append(' | '.join(khach))
				self.plainTextEdit_ku.setPlainText('\n'.join(find_ku))
				self.plainTextEdit_t2_ku.setPlainText('\n'.join(find_ku))				
				a = True
				
				

		for khach in LIST_THA:
			if username in khach:
				find_tha.append(' | '.join(khach))
				self.plainTextEdit_tha.setPlainText('\n'.join(find_tha))
				self.plainTextEdit_t2_tha.setPlainText('\n'.join(find_tha))
				a = True

		if a == False:  
			text = 'KHÔNG CÓ NHÉ'      
			self.label.setText(text)


	def napdulieu(self):
		self.kiemtra_btn.setEnabled(False)
		self.kiemtra_t2_btn.setEnabled(False)
		self.napdulieu_btn.setEnabled(False)
		self.progressBar.setValue(0)

		self.label.setText('Đang nạp dữ liệu...')

		self.nap = DataThreadings(self)

		self.nap.signal.connect(self.setValueProgessBar)

		self.nap.start() 


	@QtCore.pyqtSlot(int,str)
	def setValueProgessBar(self,value,text):
		if value ==100:
			self.kiemtra_btn.setEnabled(True)
			self.kiemtra_t2_btn.setEnabled(True)
			self.napdulieu_btn.setEnabled(True)
		self.progressBar.setValue(value)
		self.label.setText(text)


			
class DataThreadings(QtCore.QThread):

	signal = QtCore.pyqtSignal(int,str)
	finished = QtCore.pyqtSignal()

	def __init__(self,parent=None):
		super(DataThreadings,self).__init__(parent=parent)

	def work(self,files,sheets):
		return client.open(files).worksheet(sheets).get_all_values()
	def run(self):
		global LIST_KU , LIST_THA
		files  =  ['KHÁCH_HC','KHÁCH_HC']
		sheets = ['KU','THA',]

		LIST_KU = []
		LIST_THA = []

		a = 0
		job = concurrent.futures.ThreadPoolExecutor()
		for i in range(2):
			self.signal.emit(a,f'Đang nạp khách {sheets[i]}')
			future = job.submit(self.work,files[i],sheets[i])
			return_value = future.result()
			if 'ku' in sheets[i].lower():
				LIST_KU+=return_value
			else:
				LIST_THA+=return_value

			a+=100//2
			self.signal.emit(a,f'Đã nạp xong {files[i]}')  
		self.signal.emit(100,'Đã nạp xong dữ liệu') 
		self.finished.emit()
		print(LIST_KU)

		
	def stop(self):
		self.terminate()





   
		







class Login(QtWidgets.QDialog,templates.UiLogin):
	"""docstring for Login"""
	def __init__(self):
		super(Login, self).__init__()
		self.setupUi(self)

		self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
		self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
		self.btn_close.clicked.connect(self.close)
		self.minimum.clicked.connect(self.showMinimized)
		### event dy chuyển cửa sổ 
		self.khoangtrang.mouseMoveEvent = self.moveWindow
		self.btn_login.clicked.connect(self.auth)
		self.label.setAlignment(QtCore.Qt.AlignCenter)

		self.shadow = QtWidgets.QGraphicsDropShadowEffect()
		self.shadow.setBlurRadius(15)
		self.shadow.setOffset(0, 0)
		self.shadow.setColor(QtGui.QColor(0, 0, 0, 100))
		self.container.setGraphicsEffect(self.shadow)

		reponse = requests.get('https://raw.githubusercontent.com/imat94/K_kiemkhach/main/k-kiemkhach.json').json()
		client_login = gspread.service_account_from_dict(reponse)

		mainclient = client_login.open_by_url(
			'https://docs.google.com/spreadsheets/d/1ps8MYPnMSBVT13lLVLes3xvOHk6AHUWtvIT7-i53F7o/'
		)
		self.list_tk = mainclient.worksheet('Mã').get_all_values()




	def moveWindow(self,event):       
		if event.buttons() == QtCore.Qt.LeftButton:
			self.move(self.pos() + event.globalPos() - self.dragPos)
			self.dragPos = event.globalPos()
			event.accept()
	def mousePressEvent(self,event):
		self.dragPos = event.globalPos()

	def auth(self):
		username = self.username.text()
		password = self.password.text()
		for tk in self.list_tk:
			if username == tk[1] and password ==tk[2]:
				connect_googlesheet(api_url=tk[3])
				self.label.setText('Login thành công')
				self.done(1)
			self.label.setText('Sai tên tài khoản hoặc mật khẩu')


