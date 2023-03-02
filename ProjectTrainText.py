from src.views.mainView import MainView
import tkinter as tk


def main():
    root = tk.Tk()
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("1600x900")
    root.mainloop()


if __name__ == "__main__":
    main()
