# SAM GUI API

![](assert/001.png)

## 1 Data dir 

### 1.1 rgb sam

```
.
└── rgb
    ├── file_name1.jpg [/.png]
    ├── file_name2.jpg
    | ...
    ├── file_namen.jpg

```


### 1.2 rgbd sam

```
.
├── depth
│   ├── file_name1.png
│   ├── file_name2.png
│   ├── ...
│   └── file_namen.png
├── params.json                 # params
└── rgb
    ├── file_name1.jpg [/.png]
    ├── file_name2.jpg
    | ...
    ├── file_namen.jpg

```

#### params.json contents example

```
{
    "CameraMatrix": [
        [
            1119.9000022615076,
            0.0,
            943.07531033427
        ],
        [
            0.0,
            1119.8491268503178,
            514.4078345143769
        ],
        [
            0.0,
            0.0,
            1.0
        ]
    ]
}
```

## examples

```python
import tkinter as tk
from SamGuiAPI.sam_gui import DatasetViewerApp

if __name__ == "__main__":
    sam_checkpoint = './weights/sam_vit_b_01ec64.pth'
    model_type = "vit_b"
    use_file_name=False
    use_depth = True

    root = tk.Tk()
    app = DatasetViewerApp(root,sam_checkpoint,model_type,use_file_name,use_depth)
    root.mainloop()
```

## 3 GUI

![](assert/002.png)
