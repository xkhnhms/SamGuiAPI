import tkinter as tk
from SamGuiAPI.sam_gui import DatasetViewerApp

if __name__ == "__main__":
    # sam_checkpoint = 'weights/sam_vit_b_01ec64.pth'
    # model_type = "vit_b"

    sam_checkpoint = 'weights/sam_vit_l_0b3195.pth'
    model_type = "vit_l"
    use_file_name=False
    use_depth = False
    ask_okcancal = True

    root = tk.Tk()
    app = DatasetViewerApp(root,sam_checkpoint,model_type,use_file_name,use_depth, ask_okcancal)
    root.mainloop()
