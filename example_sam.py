import tkinter as tk
from SamGuiAPI.sam_gui import DatasetViewerApp

if __name__ == "__main__":
    sam_checkpoint = '../../annotation_gui/weights/sam_vit_b_01ec64.pth'
    model_type = "vit_b"
    use_file_name=False
    use_depth = True

    root = tk.Tk()
    app = DatasetViewerApp(root,sam_checkpoint,model_type,use_file_name,use_depth)
    root.mainloop()