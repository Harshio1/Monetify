# 🎨 Monet Style Transfer (CycleGAN)

This project transforms ordinary images into **Claude Monet–style paintings** using a CycleGAN-based neural network trained on the Monet dataset.  
Think of it as an AI-powered artistic filter — upload a photo or use your **webcam** to take one, and the model reimagines it in Monet’s dreamy, impressionist style!

---

## 🚀 Live Demo

🔗 Try the model instantly on **Hugging Face Spaces**:  
👉 https://huggingface.co/spaces/Harshio/Monet-Style-Transfer

✔ Upload an image  
✔ OR take a picture using **live webcam**  
✔ Click **Submit** to get your Monet-style output  

No installation required — everything runs in your browser.

---

## 🧠 What This Project Does

✔ Converts real-world photos into **Monet-style artistic paintings**  
✔ Uses **CycleGAN** for unpaired image-to-image translation  
✔ Supports **image file upload AND live webcam input**  
✔ Runs on **TensorFlow** for inference  
✔ Served with **Gradio** and deployed on **Hugging Face Spaces**

---
## 🖼 Example Results

### Input → Output Samples

<img width="2876" height="1437" alt="input-output" src="https://github.com/user-attachments/assets/7724a4bb-d2a6-44d0-a5b2-1f0131a1efb2" />

<img width="1157" height="620" alt="side-by-side" src="https://github.com/user-attachments/assets/0a052657-458e-4e6e-80bf-4ecdb17598c6" />

---


## 🧩 CycleGAN Architecture Overview

Below is a simplified visual diagram of how CycleGAN works:
Real Photo (X) ───► Generator G ───► Monet Style (Y') ───► Monet Image (Y) ───► Generator F ───► Reconstructed X


### 🔍 Key Components

- **Generator G** — Translates Photo → Monet  
- **Generator F** — Translates Monet → Photo  
- **Discriminator Dx** — Judges real photos vs generated photos  
- **Discriminator Dy** — Judges real Monet paintings vs generated Monet-style images  

CycleGAN trains **both directions simultaneously**, enforcing cycle-consistency to preserve structure while changing artistic style.

---
## 🏗 Tech Stack

- **TensorFlow / Keras**  
- **CycleGAN Architecture**  
- **Gradio Interface** – with Upload + Webcam  
- **Hugging Face Spaces Deployment**  
- **Python 3.10+**

---

## 📌 Features

🌄 Upload any image to convert  
📸 Take a picture via **live webcam**  
⚡ Fast, real-time artistic transformation  
🌐 Works entirely in the browser — **no installation required**  
🎨 Produces soft, dream-like **Monet artworks**

---

## 🙌 Acknowledgements

- Dataset: **Monet Paintings Dataset (Kaggle)**  
- Model Architecture: **CycleGAN (Unpaired Image-to-Image Translation)**  
- UI & Hosting: **Gradio + Hugging Face Spaces**

---


