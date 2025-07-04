# Arnold’s Cat Map — A Study in Chaos and Dynamical Systems

 *Algebra & Coding Project*  
 *National Higher School of Mathematics*  
 *Marouf Haider*  
 *Bahidj Nafaa*  
📅 *Academic Year: 2023–2024*

---

## 🔍 Project Overview

Arnold’s Cat Map is a discrete dynamical system known for exhibiting chaotic behavior. It transforms a unit square using a linear transformation followed by a modular reduction, resulting in image scrambling and periodicity.

This project explores:
- The mathematical foundations of the Cat Map
- Its behavior on the torus and images
- Periodicity and its connection to Fibonacci numbers
- A Python implementation for image encoding, decoding, and minimal period calculation

---

## 📄 Contents

- `report.pdf`: Full academic write-up with theory, proofs, and visuals
- `program.ipynb`: Jupyter notebook with:
  - Image encoding using Arnold's Cat Map
  - Calculation of minimal period
  - Image retrieval using reverse iterations
- `assets`: A folder with all test units used (including the one used in the report).
- `outputs`: Folder containing the results of applying the encoding to the test units.
- `README.md`: This file.

---

## 🧠 Key Concepts

- **Discrete Dynamical Systems**
- **Chaos Theory**
- **Matrix Maps on the Torus**
- **Image Scrambling and Periodicity**
- **Connections to Fibonacci and Pisano Periods**

---

## 💻 Technologies

- Python 3
- NumPy
- OpenCV (`cv2`)
- Jupyter Notebook

---

##  How to Run the Code

1. Clone this repo or download the `.ipynb` notebook.
2. Install required dependencies:
   ```bash
   pip install numpy opencv-python
   ```
---
## 🔬 Test Run

This repo includes an example input and output to demonstrate functionality.

- 📥 Input image (240*240): ![`assets/test_image.jpg`](assets/test_image.jpg) -📤 Output result (10 iterations): ![`output/result_output.jpg`](outputs/encoded_image10.jpg)
- 📤 Retrieved image: ![`output/retrieved_image.jpg`](outputs/retrieved_image.jpg)
---
## 📧 Contacts 
- [Haider Marouf]-(haider.marouf@nhsm.edu.dz)/(ensmmarouf@gmail.com).
- [Bahidj Nafaa]-(N/A).

---
Feel free to open issues for suggestions or comments. Contributions are welcome.
