import gradio as gr
import tensorflow as tf
import numpy as np
import os
from tensorflow.keras.models import load_model

# ------------------------------
# Custom InstanceNormalization
# ------------------------------
class InstanceNormalization(tf.keras.layers.Layer):
    def __init__(self, epsilon=1e-5, **kwargs):
        super().__init__(**kwargs)
        self.epsilon = epsilon

    def build(self, input_shape):
        self.scale = self.add_weight(
            shape=input_shape[-1:], initializer="random_normal", trainable=True
        )
        self.offset = self.add_weight(
            shape=input_shape[-1:], initializer="zeros", trainable=True
        )

    def call(self, x):
        mean, var = tf.nn.moments(x, axes=[1, 2], keepdims=True)
        normalized = (x - mean) / tf.sqrt(var + self.epsilon)
        return self.scale * normalized + self.offset


# ------------------------------
# Load trained generator model
# ------------------------------
generator_g = load_model(
    "generator_g_epoch70.keras",
    custom_objects={"InstanceNormalization": InstanceNormalization}
)

# ------------------------------
# Preprocess & inference
# ------------------------------
def preprocess(img):
    img = tf.image.resize(img, (256, 256))
    img = (img / 127.5) - 1
    return tf.expand_dims(img, 0)

def postprocess(img):
    img = (img + 1) / 2
    return np.clip(img[0], 0, 1)

def generate_monet(image):
    if image is None:
        return None
    img = preprocess(image)
    output = generator_g(img, training=False)
    return postprocess(output)


# ------------------------------
# Gradio UI
# ------------------------------
with gr.Blocks(title="Monet Style Transfer") as demo:

    gr.Markdown(
        """
        # 🎨 Monet Style Transfer  
        Convert your **live camera** feed or uploaded images  
        into **Monet-style paintings** using CycleGAN.
        """
    )

    with gr.Row():
        input_img = gr.Image(
            label="Upload or Capture Photo",
            sources=["upload", "webcam"],
            type="numpy"   # ⚠️ IMPORTANT CHANGE
        )

        output_img = gr.Image(
            type="numpy",
            label="Monet-Style Output"
        )

    btn = gr.Button("Generate Monet Style")
    btn.click(fn=generate_monet, inputs=input_img, outputs=output_img)


# ------------------------------
# Render launch fix
# ------------------------------
port = int(os.environ.get("PORT", 10000))
demo.launch(server_name="0.0.0.0", server_port=port)
