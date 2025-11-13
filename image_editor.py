import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from PIL import Image, ImageTk
import os
from pathlib import Path

class VerticalImageEditor:
    def __init__(self, root):
        self.root = root
        self.current_language = "ko"  # 기본 언어: 한국어
        
        # 다국어 사전
        self.languages = {
            "ko": {
                "title": "세로 이미지 편집기 - Product Image Editor",
                "merge_tab": "📄 이미지 합치기",
                "cut_tab": "✂️ 이미지 자르기",
                "merge_title": "📋 이미지 합치기",
                "add_images": "🖼️ 이미지 추가",
                "added_images": "추가된 이미지:",
                "move_up": "⬆️ 위로",
                "move_down": "⬇️ 아래로",
                "delete": "🗑️ 삭제",
                "clear_all": "🧹 전체삭제",
                "settings": "설정",
                "max_width": "최대 너비 (px):",
                "bg_color": "배경색:",
                "white": "흰색",
                "transparent": "투명",
                "merge_images": "🔗 이미지 합치기",
                "preview": "🔍 미리보기",
                "cut_title": "✂️ 이미지 자르기",
                "load_image": "📁 이미지 불러오기",
                "load_image_msg": "이미지를 불러와주세요",
                "cut_positions": "자르기 위치",
                "cut_image": "✂️ 이미지 자르기",
                "image_viewer": "🖼️ 이미지 뷰어",
                "mouse_pos": "🎯 마우스 위치:",
                "click_to_add": "클릭하여 자르기 위치 추가",
                "mouse_guide": "이미지 위로 마우스를 올려보세요",
                "out_of_range": "범위 밖",
                "select_images": "이미지 선택",
                "select_cut_image": "자를 이미지 선택",
                "save_merged": "합쳐진 이미지 저장",
                "select_save_folder": "자른 이미지들을 저장할 폴더 선택",
                "warning": "경고",
                "error": "오류",
                "complete": "완료",
                "info": "정보",
                "confirm": "확인",
                "select_item_move": "이동할 항목을 선택해주세요.",
                "select_item_delete": "삭제할 항목을 선택해주세요.",
                "no_images_to_delete": "삭제할 이미지가 없습니다.",
                "confirm_delete_all": "전체 삭제 확인",
                "delete_all_msg": "총 {}개의 이미지를 모두 삭제하시겠습니까?",
                "all_deleted": "모든 이미지가 삭제되었습니다.",
                "add_images_first": "합칠 이미지를 추가해주세요.",
                "set_image_and_position": "이미지와 자르기 위치를 설정해주세요.",
                "select_cut_position": "삭제할 자르기 위치를 선택해주세요.",
                "preview_error": "미리보기 생성 중 오류가 발생했습니다: {}",
                "merge_error": "이미지 합치기 중 오류가 발생했습니다: {}",
                "load_error": "이미지를 불러올 수 없습니다: {}",
                "cut_error": "이미지 자르기 중 오류가 발생했습니다: {}",
                "merge_success": "이미지가 성공적으로 합쳐져 저장되었습니다:\n{}",
                "cut_success": "{}개의 이미지가 저장되었습니다:\n{}",
                "file": "파일:",
                "size": "크기:",
                "cut_num": "자르기 {}",
                "language": "🌍 언어",
                "korean": "한국어",
                "chinese": "中文"
            },
            "zh": {
                "title": "竖版图片编辑器 - Product Image Editor",
                "merge_tab": "📄 图片合并",
                "cut_tab": "✂️ 图片裁剪",
                "merge_title": "📋 图片合并",
                "add_images": "🖼️ 添加图片",
                "added_images": "已添加的图片:",
                "move_up": "⬆️ 上移",
                "move_down": "⬇️ 下移",
                "delete": "🗑️ 删除",
                "clear_all": "🧹 全部删除",
                "settings": "设置",
                "max_width": "最大宽度 (px):",
                "bg_color": "背景色:",
                "white": "白色",
                "transparent": "透明",
                "merge_images": "🔗 合并图片",
                "preview": "🔍 预览",
                "cut_title": "✂️ 图片裁剪",
                "load_image": "📁 加载图片",
                "load_image_msg": "请加载图片",
                "cut_positions": "裁剪位置",
                "cut_image": "✂️ 裁剪图片",
                "image_viewer": "🖼️ 图片查看器",
                "mouse_pos": "🎯 鼠标位置:",
                "click_to_add": "点击添加裁剪位置",
                "mouse_guide": "将鼠标移至图片上方",
                "out_of_range": "超出范围",
                "select_images": "选择图片",
                "select_cut_image": "选择要裁剪的图片",
                "save_merged": "保存合并后的图片",
                "select_save_folder": "选择保存裁剪图片的文件夹",
                "warning": "警告",
                "error": "错误",
                "complete": "完成",
                "info": "信息",
                "confirm": "确认",
                "select_item_move": "请选择要移动的项目。",
                "select_item_delete": "请选择要删除的项目。",
                "no_images_to_delete": "没有要删除的图片。",
                "confirm_delete_all": "确认全部删除",
                "delete_all_msg": "是否删除全部{}张图片？",
                "all_deleted": "所有图片已删除。",
                "add_images_first": "请先添加要合并的图片。",
                "set_image_and_position": "请设置图片和裁剪位置。",
                "select_cut_position": "请选择要删除的裁剪位置。",
                "preview_error": "生成预览时发生错误: {}",
                "merge_error": "合并图片时发生错误: {}",
                "load_error": "无法加载图片: {}",
                "cut_error": "裁剪图片时发生错误: {}",
                "merge_success": "图片已成功合并并保存:\n{}",
                "cut_success": "已保存{}张图片:\n{}",
                "file": "文件:",
                "size": "大小:",
                "cut_num": "裁剪 {}",
                "language": "🌍 语言",
                "korean": "한국어",
                "chinese": "中文"
            }
        }
        
        self.setup_window()
        
        # 이미지 리스트 (합치기용)
        self.image_list = []
        self.image_paths = []
        
        # 현재 이미지 (자르기용)
        self.current_image = None
        self.current_image_path = ""
        self.cut_positions = []
        
        self.setup_ui()
    
    def setup_window(self):
        self.root.title(self.get_text("title"))
        self.root.geometry("1200x800")
    
    def get_text(self, key):
        """현재 언어에 따른 텍스트 반환"""
        return self.languages[self.current_language].get(key, key)
    
    def change_language(self, lang):
        """언어 변경 및 UI 업데이트"""
        self.current_language = lang
        self.update_all_texts()
    
    def update_all_texts(self):
        """모든 UI 텍스트 업데이트"""
        # 윈도우 제목
        self.root.title(self.get_text("title"))
        
        # 탭 제목
        self.notebook.tab(0, text=self.get_text("merge_tab"))
        self.notebook.tab(1, text=self.get_text("cut_tab"))
        
        # 합치기 탭 업데이트
        self.merge_title_label.config(text=self.get_text("merge_title"))
        self.add_images_btn.config(text=self.get_text("add_images"))
        self.images_list_label.config(text=self.get_text("added_images"))
        self.move_up_btn.config(text=self.get_text("move_up"))
        self.move_down_btn.config(text=self.get_text("move_down"))
        self.delete_btn.config(text=self.get_text("delete"))
        self.clear_all_btn.config(text=self.get_text("clear_all"))
        self.settings_frame.config(text=self.get_text("settings"))
        self.max_width_label.config(text=self.get_text("max_width"))
        self.bg_color_label.config(text=self.get_text("bg_color"))
        self.white_radio.config(text=self.get_text("white"))
        self.transparent_radio.config(text=self.get_text("transparent"))
        self.merge_btn.config(text=self.get_text("merge_images"))
        self.preview_label.config(text=self.get_text("preview"))
        
        # 자르기 탭 업데이트
        self.cut_title_label.config(text=self.get_text("cut_title"))
        self.load_image_btn.config(text=self.get_text("load_image"))
        self.cut_positions_frame.config(text=self.get_text("cut_positions"))
        self.remove_cut_btn.config(text=self.get_text("delete"))
        self.clear_cut_btn.config(text=self.get_text("clear_all"))
        self.cut_btn.config(text=self.get_text("cut_image"))
        self.viewer_label.config(text=self.get_text("image_viewer"))
        self.click_guide_label.config(text=self.get_text("click_to_add"))
        
        # 언어 버튼 업데이트
        self.lang_frame_label.config(text=self.get_text("language"))
        self.korean_btn.config(text=self.get_text("korean"))
        self.chinese_btn.config(text=self.get_text("chinese"))
        
        # 동적 텍스트 업데이트 (이미지 정보, 좌표 등)
        if hasattr(self, 'image_info_label') and self.current_image:
            filename = os.path.basename(self.current_image_path)
            info_text = f"{self.get_text('file')} {filename}\n{self.get_text('size')} {self.current_image.width} x {self.current_image.height}"
            self.image_info_label.config(text=info_text)
        elif hasattr(self, 'image_info_label'):
            self.image_info_label.config(text=self.get_text("load_image_msg"))
        
        if hasattr(self, 'coord_label'):
            if not self.current_image:
                self.coord_label.config(text=f"{self.get_text('mouse_pos')} -")
            else:
                self.coord_label.config(text=f"{self.get_text('mouse_pos')} {self.get_text('mouse_guide')}")
        
        # 자르기 위치 리스트 업데이트
        if hasattr(self, 'cut_listbox'):
            self.update_cut_listbox()
    
    
    def setup_ui(self):
        # 상단 언어 선택 패널
        top_frame = ttk.Frame(self.root)
        top_frame.pack(fill=tk.X, padx=10, pady=5)
        
        # 언어 선택 프레임
        self.lang_frame = ttk.LabelFrame(top_frame, text=self.get_text("language"))
        self.lang_frame.pack(side=tk.RIGHT)
        
        self.lang_frame_label = self.lang_frame  # 참조 저장
        
        self.korean_btn = ttk.Button(self.lang_frame, text=self.get_text("korean"), 
                                    command=lambda: self.change_language("ko"))
        self.korean_btn.pack(side=tk.LEFT, padx=5, pady=5)
        
        self.chinese_btn = ttk.Button(self.lang_frame, text=self.get_text("chinese"), 
                                     command=lambda: self.change_language("zh"))
        self.chinese_btn.pack(side=tk.LEFT, padx=5, pady=5)
        
        # 메인 탭 컨트롤
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # 탭 1: 이미지 합치기
        self.merge_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.merge_frame, text=self.get_text("merge_tab"))
        self.setup_merge_ui()
        
        # 탭 2: 이미지 자르기
        self.cut_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.cut_frame, text=self.get_text("cut_tab"))
        self.setup_cut_ui()
    
    def setup_merge_ui(self):
        # 왼쪽 패널 - 컨트롤
        left_panel = ttk.Frame(self.merge_frame)
        left_panel.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)
        
        self.merge_title_label = ttk.Label(left_panel, text=self.get_text("merge_title"), font=("Arial", 14, "bold"))
        self.merge_title_label.pack(pady=(0, 10))
        
        # 이미지 추가 버튼
        self.add_images_btn = ttk.Button(left_panel, text=self.get_text("add_images"), command=self.add_images)
        self.add_images_btn.pack(fill=tk.X, pady=5)
        
        # 이미지 리스트
        list_frame = ttk.Frame(left_panel)
        list_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
        self.images_list_label = ttk.Label(list_frame, text=self.get_text("added_images"))
        self.images_list_label.pack(anchor=tk.W)
        
        # 리스트박스와 스크롤바
        list_scroll_frame = ttk.Frame(list_frame)
        list_scroll_frame.pack(fill=tk.BOTH, expand=True)
        
        self.image_listbox = tk.Listbox(list_scroll_frame, height=10)
        scrollbar = ttk.Scrollbar(list_scroll_frame, orient=tk.VERTICAL, command=self.image_listbox.yview)
        self.image_listbox.configure(yscrollcommand=scrollbar.set)
        
        self.image_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # 순서 조정 버튼
        order_frame = ttk.Frame(left_panel)
        order_frame.pack(fill=tk.X, pady=10)
        
        self.move_up_btn = ttk.Button(order_frame, text=self.get_text("move_up"), command=self.move_up)
        self.move_up_btn.pack(side=tk.LEFT, padx=2)
        
        self.move_down_btn = ttk.Button(order_frame, text=self.get_text("move_down"), command=self.move_down)
        self.move_down_btn.pack(side=tk.LEFT, padx=2)
        
        self.delete_btn = ttk.Button(order_frame, text=self.get_text("delete"), command=self.remove_image)
        self.delete_btn.pack(side=tk.LEFT, padx=2)
        
        self.clear_all_btn = ttk.Button(order_frame, text=self.get_text("clear_all"), command=self.clear_all_images)
        self.clear_all_btn.pack(side=tk.LEFT, padx=2)
        
        # 합치기 설정
        self.settings_frame = ttk.LabelFrame(left_panel, text=self.get_text("settings"))
        self.settings_frame.pack(fill=tk.X, pady=10)
        
        # 최대 너비 설정
        self.max_width_label = ttk.Label(self.settings_frame, text=self.get_text("max_width"))
        self.max_width_label.pack(anchor=tk.W)
        self.max_width_var = tk.StringVar(value="800")
        ttk.Entry(self.settings_frame, textvariable=self.max_width_var, width=10).pack(anchor=tk.W, pady=2)
        
        # 배경색 설정
        self.bg_color_label = ttk.Label(self.settings_frame, text=self.get_text("bg_color"))
        self.bg_color_label.pack(anchor=tk.W, pady=(10, 0))
        self.bg_color_var = tk.StringVar(value="white")
        color_frame = ttk.Frame(self.settings_frame)
        color_frame.pack(anchor=tk.W)
        
        self.white_radio = ttk.Radiobutton(color_frame, text=self.get_text("white"), variable=self.bg_color_var, value="white")
        self.white_radio.pack(side=tk.LEFT)
        
        self.transparent_radio = ttk.Radiobutton(color_frame, text=self.get_text("transparent"), variable=self.bg_color_var, value="transparent")
        self.transparent_radio.pack(side=tk.LEFT)
        
        # 합치기 버튼
        self.merge_btn = ttk.Button(left_panel, text=self.get_text("merge_images"), command=self.merge_images)
        self.merge_btn.pack(fill=tk.X, pady=20)
        
        # 오른쪽 패널 - 미리보기
        right_panel = ttk.Frame(self.merge_frame)
        right_panel.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        self.preview_label = ttk.Label(right_panel, text=self.get_text("preview"), font=("Arial", 14, "bold"))
        self.preview_label.pack(pady=(0, 10))
        
        # 미리보기 캔버스
        canvas_frame = ttk.Frame(right_panel)
        canvas_frame.pack(fill=tk.BOTH, expand=True)
        
        self.merge_canvas = tk.Canvas(canvas_frame, bg="white", relief=tk.SUNKEN, borderwidth=1)
        v_scrollbar = ttk.Scrollbar(canvas_frame, orient=tk.VERTICAL, command=self.merge_canvas.yview)
        h_scrollbar = ttk.Scrollbar(canvas_frame, orient=tk.HORIZONTAL, command=self.merge_canvas.xview)
        
        self.merge_canvas.configure(yscrollcommand=v_scrollbar.set, xscrollcommand=h_scrollbar.set)
        
        self.merge_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        v_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        h_scrollbar.pack(side=tk.BOTTOM, fill=tk.X)
    
    def setup_cut_ui(self):
        # 왼쪽 패널 - 컨트롤
        left_panel = ttk.Frame(self.cut_frame)
        left_panel.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)
        
        self.cut_title_label = ttk.Label(left_panel, text=self.get_text("cut_title"), font=("Arial", 14, "bold"))
        self.cut_title_label.pack(pady=(0, 10))
        
        # 이미지 불러오기
        self.load_image_btn = ttk.Button(left_panel, text=self.get_text("load_image"), command=self.load_image_for_cut)
        self.load_image_btn.pack(fill=tk.X, pady=5)
        
        # 현재 이미지 정보
        self.image_info_label = ttk.Label(left_panel, text=self.get_text("load_image_msg"))
        self.image_info_label.pack(pady=10)
        
        # 자르기 위치 리스트
        self.cut_positions_frame = ttk.LabelFrame(left_panel, text=self.get_text("cut_positions"))
        self.cut_positions_frame.pack(fill=tk.X, pady=10)
        
        self.cut_listbox = tk.Listbox(self.cut_positions_frame, height=6)
        self.cut_listbox.pack(fill=tk.X, padx=5, pady=5)
        
        # 자르기 위치 관리 버튼
        cut_btn_frame = ttk.Frame(self.cut_positions_frame)
        cut_btn_frame.pack(fill=tk.X, padx=5, pady=5)
        
        self.remove_cut_btn = ttk.Button(cut_btn_frame, text=self.get_text("delete"), command=self.remove_cut_position)
        self.remove_cut_btn.pack(side=tk.LEFT, padx=2)
        
        self.clear_cut_btn = ttk.Button(cut_btn_frame, text=self.get_text("clear_all"), command=self.clear_cut_positions)
        self.clear_cut_btn.pack(side=tk.LEFT, padx=2)
        
        # 자르기 실행
        self.cut_btn = ttk.Button(left_panel, text=self.get_text("cut_image"), command=self.cut_image)
        self.cut_btn.pack(fill=tk.X, pady=20)
        
        # 오른쪽 패널 - 이미지 뷰어
        right_panel = ttk.Frame(self.cut_frame)
        right_panel.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        self.viewer_label = ttk.Label(right_panel, text=self.get_text("image_viewer"), font=("Arial", 14, "bold"))
        self.viewer_label.pack(pady=(0, 10))
        
        # 좌표 표시 라벨
        coord_frame = ttk.Frame(right_panel)
        coord_frame.pack(fill=tk.X, pady=5)
        
        self.coord_label = ttk.Label(coord_frame, text=f"{self.get_text('mouse_pos')} -", 
                                   font=("Arial", 10), foreground="blue")
        self.coord_label.pack(side=tk.LEFT)
        
        self.click_guide_label = ttk.Label(coord_frame, text=self.get_text("click_to_add"), 
                 font=("Arial", 9), foreground="gray")
        self.click_guide_label.pack(side=tk.RIGHT)
        
        # 이미지 캔버스
        canvas_frame = ttk.Frame(right_panel)
        canvas_frame.pack(fill=tk.BOTH, expand=True)
        
        self.cut_canvas = tk.Canvas(canvas_frame, bg="white", relief=tk.SUNKEN, borderwidth=1)
        cut_v_scrollbar = ttk.Scrollbar(canvas_frame, orient=tk.VERTICAL, command=self.cut_canvas.yview)
        cut_h_scrollbar = ttk.Scrollbar(canvas_frame, orient=tk.HORIZONTAL, command=self.cut_canvas.xview)
        
        self.cut_canvas.configure(yscrollcommand=cut_v_scrollbar.set, xscrollcommand=cut_h_scrollbar.set)
        
        self.cut_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        cut_v_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        cut_h_scrollbar.pack(side=tk.BOTTOM, fill=tk.X)
        
        # 마우스 이벤트 바인딩
        self.cut_canvas.bind("<Button-1>", self.on_canvas_click)
        self.cut_canvas.bind("<Motion>", self.on_mouse_motion)
        self.cut_canvas.bind("<Leave>", self.on_mouse_leave)
    
    def add_images(self):
        file_paths = filedialog.askopenfilenames(
            title=self.get_text("select_images"),
            filetypes=[("PNG files", "*.png"), ("JPG files", "*.jpg"), ("All images", "*.png *.jpg *.jpeg")]
        )
        
        for path in file_paths:
            if path not in self.image_paths:
                self.image_paths.append(path)
                filename = os.path.basename(path)
                self.image_listbox.insert(tk.END, filename)
        
        self.update_merge_preview()
    
    def move_up(self):
        try:
            index = self.image_listbox.curselection()[0]
            if index > 0:
                # 리스트박스에서 이동
                item = self.image_listbox.get(index)
                self.image_listbox.delete(index)
                self.image_listbox.insert(index - 1, item)
                self.image_listbox.selection_set(index - 1)
                
                # 경로 리스트에서도 이동
                self.image_paths[index], self.image_paths[index - 1] = self.image_paths[index - 1], self.image_paths[index]
                
                self.update_merge_preview()
        except:
            messagebox.showwarning(self.get_text("warning"), self.get_text("select_item_move"))
    
    def move_down(self):
        try:
            index = self.image_listbox.curselection()[0]
            if index < self.image_listbox.size() - 1:
                # 리스트박스에서 이동
                item = self.image_listbox.get(index)
                self.image_listbox.delete(index)
                self.image_listbox.insert(index + 1, item)
                self.image_listbox.selection_set(index + 1)
                
                # 경로 리스트에서도 이동
                self.image_paths[index], self.image_paths[index + 1] = self.image_paths[index + 1], self.image_paths[index]
                
                self.update_merge_preview()
        except:
            messagebox.showwarning(self.get_text("warning"), self.get_text("select_item_move"))
    
    def remove_image(self):
        try:
            index = self.image_listbox.curselection()[0]
            self.image_listbox.delete(index)
            del self.image_paths[index]
            self.update_merge_preview()
        except:
            messagebox.showwarning(self.get_text("warning"), self.get_text("select_item_delete"))
    
    def clear_all_images(self):
        """모든 이미지를 삭제하는 기능"""
        if not self.image_paths:
            messagebox.showinfo(self.get_text("info"), self.get_text("no_images_to_delete"))
            return
        
        # 확인 대화상자
        result = messagebox.askyesno(self.get_text("confirm_delete_all"), 
                                   self.get_text("delete_all_msg").format(len(self.image_paths)))
        
        if result:
            # 모든 이미지 삭제
            self.image_paths.clear()
            self.image_listbox.delete(0, tk.END)
            
            # 미리보기 캔버스 클리어
            self.merge_canvas.delete("all")
            
            messagebox.showinfo(self.get_text("complete"), self.get_text("all_deleted"))
    
    def update_merge_preview(self):
        if not self.image_paths:
            self.merge_canvas.delete("all")
            return
        
        try:
            # 이미지들을 불러와서 미리보기 생성
            images = []
            for path in self.image_paths:
                img = Image.open(path)
                images.append(img)
            
            if not images:
                return
            
            # 최대 너비 설정
            max_width = int(self.max_width_var.get())
            
            # 이미지들을 리사이즈하고 합치기
            resized_images = []
            for img in images:
                if img.width > max_width:
                    ratio = max_width / img.width
                    new_height = int(img.height * ratio)
                    img = img.resize((max_width, new_height), Image.Resampling.LANCZOS)
                resized_images.append(img)
            
            # 전체 높이 계산
            total_height = sum(img.height for img in resized_images)
            
            # 합쳐진 이미지 생성 (미리보기용으로 크기 축소)
            preview_scale = min(1.0, 400 / max_width)  # 미리보기 최대 너비 400px
            preview_width = int(max_width * preview_scale)
            preview_height = int(total_height * preview_scale)
            
            if self.bg_color_var.get() == "transparent":
                merged = Image.new('RGBA', (preview_width, preview_height), (255, 255, 255, 0))
            else:
                merged = Image.new('RGB', (preview_width, preview_height), 'white')
            
            y_offset = 0
            for img in resized_images:
                preview_img = img.resize((int(img.width * preview_scale), int(img.height * preview_scale)), Image.Resampling.LANCZOS)
                merged.paste(preview_img, (0, y_offset))
                y_offset += preview_img.height
            
            # 캔버스에 표시
            self.merge_preview_image = ImageTk.PhotoImage(merged)
            self.merge_canvas.delete("all")
            self.merge_canvas.create_image(0, 0, anchor=tk.NW, image=self.merge_preview_image)
            self.merge_canvas.configure(scrollregion=self.merge_canvas.bbox("all"))
            
        except Exception as e:
            messagebox.showerror(self.get_text("error"), self.get_text("preview_error").format(str(e)))
    
    def merge_images(self):
        if not self.image_paths:
            messagebox.showwarning(self.get_text("warning"), self.get_text("add_images_first"))
            return
        
        try:
            # 저장 경로 선택
            save_path = filedialog.asksaveasfilename(
                title=self.get_text("save_merged"),
                defaultextension=".png",
                filetypes=[("PNG files", "*.png")]
            )
            
            if not save_path:
                return
            
            # 이미지들을 불러와서 합치기
            images = []
            for path in self.image_paths:
                img = Image.open(path)
                images.append(img)
            
            # 최대 너비 설정
            max_width = int(self.max_width_var.get())
            
            # 이미지들을 리사이즈
            resized_images = []
            for img in images:
                if img.width > max_width:
                    ratio = max_width / img.width
                    new_height = int(img.height * ratio)
                    img = img.resize((max_width, new_height), Image.Resampling.LANCZOS)
                resized_images.append(img)
            
            # 전체 높이 계산
            total_height = sum(img.height for img in resized_images)
            
            # 합쳐진 이미지 생성
            if self.bg_color_var.get() == "transparent":
                merged = Image.new('RGBA', (max_width, total_height), (255, 255, 255, 0))
            else:
                merged = Image.new('RGB', (max_width, total_height), 'white')
            
            y_offset = 0
            for img in resized_images:
                merged.paste(img, (0, y_offset))
                y_offset += img.height
            
            # 저장
            merged.save(save_path)
            messagebox.showinfo(self.get_text("complete"), self.get_text("merge_success").format(save_path))
            
        except Exception as e:
            messagebox.showerror(self.get_text("error"), self.get_text("merge_error").format(str(e)))
    
    def load_image_for_cut(self):
        file_path = filedialog.askopenfilename(
            title=self.get_text("select_cut_image"),
            filetypes=[("PNG files", "*.png"), ("JPG files", "*.jpg"), ("All images", "*.png *.jpg *.jpeg")]
        )
        
        if not file_path:
            return
        
        try:
            self.current_image = Image.open(file_path)
            self.current_image_path = file_path
            self.cut_positions = []
            self.cut_listbox.delete(0, tk.END)
            
            # 좌표 라벨 초기화
            self.coord_label.config(text=f"{self.get_text('mouse_pos')} {self.get_text('mouse_guide')}")
            
            # 이미지 정보 표시
            filename = os.path.basename(file_path)
            info_text = f"{self.get_text('file')} {filename}\n{self.get_text('size')} {self.current_image.width} x {self.current_image.height}"
            self.image_info_label.config(text=info_text)
            
            # 캔버스에 이미지 표시
            self.display_image_for_cut()
            
        except Exception as e:
            messagebox.showerror(self.get_text("error"), self.get_text("load_error").format(str(e)))
    
    def display_image_for_cut(self):
        if not self.current_image:
            return
        
        # 캔버스 크기에 맞게 이미지 스케일 조정
        canvas_width = 600
        scale = min(1.0, canvas_width / self.current_image.width)
        
        display_width = int(self.current_image.width * scale)
        display_height = int(self.current_image.height * scale)
        
        display_image = self.current_image.resize((display_width, display_height), Image.Resampling.LANCZOS)
        self.cut_photo = ImageTk.PhotoImage(display_image)
        
        self.cut_canvas.delete("all")
        self.cut_canvas.create_image(0, 0, anchor=tk.NW, image=self.cut_photo)
        
        # 자르기 선 그리기
        self.draw_cut_lines()
        
        self.cut_canvas.configure(scrollregion=self.cut_canvas.bbox("all"))
        
        # 스케일 정보 저장
        self.display_scale = scale
    
    def draw_cut_lines(self):
        if not hasattr(self, 'display_scale'):
            return
        
        # 기존 자르기 선만 삭제 (가이드 라인은 유지)
        self.cut_canvas.delete("cut_line")
        
        canvas_width = int(self.current_image.width * self.display_scale)
        
        for i, pos in enumerate(self.cut_positions):
            y_pos = int(pos * self.display_scale)
            self.cut_canvas.create_line(0, y_pos, canvas_width, y_pos, 
                                      fill="red", width=2, tags="cut_line")
            
            # 자르기 번호 배경 추가 (더 잘 보이도록)
            cut_text = self.get_text('cut_num').format(i+1)
            text_width = len(cut_text) * 6 + 10  # 텍스트 길이에 따른 배경 너비 조정
            text_bg = self.cut_canvas.create_rectangle(2, y_pos - 15, text_width, y_pos - 2, 
                                                     fill="red", outline="red", tags="cut_line")
            self.cut_canvas.create_text(5, y_pos - 8, text=cut_text, 
                                      fill="white", anchor=tk.W, font=("Arial", 8, "bold"), tags="cut_line")
    
    def on_canvas_click(self, event):
        if not self.current_image:
            return
        
        # 클릭한 위치를 실제 이미지 좌표로 변환
        canvas_y = self.cut_canvas.canvasy(event.y)
        actual_y = int(canvas_y / self.display_scale)
        
        # 이미지 범위 내에서만 처리
        if 0 <= actual_y <= self.current_image.height:
            self.cut_positions.append(actual_y)
            self.cut_positions.sort()  # 정렬
            
            # 리스트박스 업데이트
            self.update_cut_listbox()
            
            # 자르기 선 다시 그리기
            self.cut_canvas.delete("cut_line")
            self.draw_cut_lines()
    
    def on_mouse_motion(self, event):
        """마우스 움직임에 따라 실시간으로 좌표 표시"""
        if not self.current_image or not hasattr(self, 'display_scale'):
            self.coord_label.config(text=f"{self.get_text('mouse_pos')} -")
            return
        
        # 현재 마우스 위치를 실제 이미지 좌표로 변환
        canvas_y = self.cut_canvas.canvasy(event.y)
        actual_y = int(canvas_y / self.display_scale)
        
        # 이미지 범위 내에 있는지 확인
        if 0 <= actual_y <= self.current_image.height:
            self.coord_label.config(text=f"{self.get_text('mouse_pos')} Y = {actual_y}px", foreground="blue")
            
            # 임시 가이드 라인 그리기 (기존 가이드 라인 삭제 후)
            self.cut_canvas.delete("guide_line")
            canvas_width = int(self.current_image.width * self.display_scale)
            guide_y = int(actual_y * self.display_scale)
            self.cut_canvas.create_line(0, guide_y, canvas_width, guide_y, 
                                      fill="gray", width=1, dash=(3, 3), tags="guide_line")
        else:
            self.coord_label.config(text=f"{self.get_text('mouse_pos')} {self.get_text('out_of_range')}", foreground="red")
            self.cut_canvas.delete("guide_line")
    
    def on_mouse_leave(self, event):
        """마우스가 캔버스를 벗어날 때 가이드 라인 삭제"""
        self.coord_label.config(text=f"{self.get_text('mouse_pos')} -")
        self.cut_canvas.delete("guide_line")
    
    def update_cut_listbox(self):
        self.cut_listbox.delete(0, tk.END)
        for i, pos in enumerate(self.cut_positions):
            self.cut_listbox.insert(tk.END, f"{self.get_text('cut_num').format(i+1)}: Y={pos}px")
    
    def remove_cut_position(self):
        try:
            index = self.cut_listbox.curselection()[0]
            del self.cut_positions[index]
            self.update_cut_listbox()
            
            # 자르기 선 다시 그리기
            self.cut_canvas.delete("cut_line")
            self.draw_cut_lines()
        except:
            messagebox.showwarning(self.get_text("warning"), self.get_text("select_cut_position"))
    
    def clear_cut_positions(self):
        self.cut_positions = []
        self.update_cut_listbox()
        self.cut_canvas.delete("cut_line")
    
    def cut_image(self):
        if not self.current_image or not self.cut_positions:
            messagebox.showwarning(self.get_text("warning"), self.get_text("set_image_and_position"))
            return
        
        try:
            # 저장할 폴더 선택
            save_dir = filedialog.askdirectory(title=self.get_text("select_save_folder"))
            if not save_dir:
                return
            
            # 원본 파일명에서 확장자 분리
            original_name = Path(self.current_image_path).stem
            
            # 자르기 위치에 0과 이미지 높이 추가
            cut_points = [0] + self.cut_positions + [self.current_image.height]
            cut_points = sorted(list(set(cut_points)))  # 중복 제거 및 정렬
            
            saved_files = []
            
            # 각 구간별로 자르기
            for i in range(len(cut_points) - 1):
                start_y = cut_points[i]
                end_y = cut_points[i + 1]
                
                if end_y - start_y > 0:  # 높이가 0보다 큰 경우만
                    # 이미지 자르기
                    cropped = self.current_image.crop((0, start_y, self.current_image.width, end_y))
                    
                    # 파일명 생성
                    filename = f"{original_name}_part_{i+1:02d}.png"
                    filepath = os.path.join(save_dir, filename)
                    
                    # 저장
                    cropped.save(filepath)
                    saved_files.append(filename)
            
            messagebox.showinfo(self.get_text("complete"), 
                              self.get_text("cut_success").format(len(saved_files), "\n".join(saved_files)))
            
        except Exception as e:
            messagebox.showerror(self.get_text("error"), self.get_text("cut_error").format(str(e)))

def main():
    root = tk.Tk()
    app = VerticalImageEditor(root)
    root.mainloop()

if __name__ == "__main__":
    main()
