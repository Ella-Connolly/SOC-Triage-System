import os
os.system("python src/generate-logs.py")
os.system("python src/preprocessing.py")
os.system("python src/detection.py")
os.system("python src/scoring.py")
os.system("python src/visual.py")
