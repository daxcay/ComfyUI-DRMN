import os

def save_file(filename, output_dir, content, mode='SaveNew'):
    os.makedirs(output_dir, exist_ok=True)
    file_path = os.path.join(output_dir, filename)
    
    if mode == 'SaveNew':
        counter = 0
        while os.path.exists(file_path):
            counter += 1
            file_path = os.path.join(output_dir, f"{os.path.splitext(filename)[0]}_{counter}{os.path.splitext(filename)[1]}")
    elif mode == 'Merge' and os.path.exists(file_path):
        with open(file_path, 'a') as file:
            file.write(content)
        print(f"Content appended successfully to {file_path}")
        return
    elif mode == 'Overwrite' and os.path.exists(file_path):
        os.remove(file_path)
    elif mode == 'MergeAndSaveNew' and os.path.exists(file_path):
        with open(file_path, 'r') as file:
            existing_content = file.read()
        content = existing_content + content
        counter = 0
        while os.path.exists(file_path):
            counter += 1
            file_path = os.path.join(output_dir, f"{os.path.splitext(filename)[0]}_{counter}{os.path.splitext(filename)[1]}")
    
    with open(file_path, 'w') as file:
        file.write(content)
    print(f"File saved successfully at {file_path}")

class DATASET_TXTFileSaverBatch:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "file_names": ("STRING",{"forceInput": True}),
                "contents": ("STRING",{"forceInput": True}),
                "save_in": ("STRING", {"default": "directory path"}),
                "save_mode": (['Merge','Overwrite','SaveNew','MergeAndSaveNew'],),
            },
        }

    INPUT_IS_LIST = True
    RETURN_TYPES = ()
    FUNCTION = "SaveIT"
    OUTPUT_NODE = True

    CATEGORY = "🔶DATASET🔶"

    def SaveIT(self, file_names, contents, save_in, save_mode):
        try:

            directory = save_in[0]
            mode = save_mode[0]

            if not os.path.exists(directory):
                os.makedirs(directory)

            for i in range(0, len(contents)):
                text = contents[i]
                file_name = file_names[i]
                save_file(f"{file_name}.txt", directory, text, mode)

        except Exception as e:
            print(f"Error saving: {e}")

        return ()
    
    @classmethod
    def IS_CHANGED(s, content, file_name, directory, mode):       
       return os.urandom(16).hex()


N_CLASS_MAPPINGS = {
    "DATASET_TXTFileSaverBatch": DATASET_TXTFileSaverBatch,
}

N_DISPLAY_NAME_MAPPINGS = {
    "DATASET_TXTFileSaverBatch": "DATASET_TXTFileSaverBatch",
}
