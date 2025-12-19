# Day 02 — Gradient Descent from Scratch

## What does Gradient Descent do?

Gradient Descent helps a model learn by slowly adjusting weight and bias so the prediction error becomes smaller with every iteration.

---

## Why does the learning rate matter?

The learning decides how much the weight and bias change in each step. If it is chosen properly, the model learns smoothly.

---

## What happens if the learning rate is too high?

If the learning rate is too high;

    The model updates to much.

     It may miss a correct solution.

So, choosing an appropriate learning rate is necessary for stable learning.

---

## One mistake faced and how it was fixed

One issue faced during this task was that the Jupyter notebook was not producing any output because the virtual environment kernel was not activated. This was fixed by activating the `genai_env` virtual environment, installing the required packages, and selecting the correct kernel (`Python (genai_env)`) in Jupyter Notebook.
