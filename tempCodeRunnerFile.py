def show_home_page(self):
        for widget in self.winfo_children():
            widget.pack_forget()