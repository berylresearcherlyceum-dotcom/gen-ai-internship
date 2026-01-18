## What information is gradually destroyed.

Forward diffusion gradually adds noise, destroying the **details and structure** of the data.  
The model then learns to recover it step by step.

## Why gradual noise addition matters.

Adding noise step by step makes learning more stable and allows the model to **recover data gradually**, leading to better generation.

## Why the model predicts noise, not data.

Predicting the noise is easier and more stable than predicting the full data,  
because the model can gradually remove the added noise to reconstruct the original input.

## Why this produces structured data.

Step-by-step denoising preserves patterns learned from real data,  
so the final output keeps the **structure and relationships** of the original inputs.

## Why diffusion gives more stable generation than GANs.

Diffusion models gradually add and remove noise in small steps,  
so each step is controlled, avoiding the instability and mode collapse common in GANs.

## Forward vs reverse diffusion

Forward diffusion gradually adds noise to destroy the data.  
-Reverse diffusion gradually removes noise to reconstruct/generate data.  

## Why noise prediction works

The model predicts the noise added at each step, which is easier than predicting full data and allows step-by-step reconstruction.  

## Diffusion vs GAN vs VAE

Diffusion is stable, iterative denoising for diverse outputs.  
GAN is adversarial, can produce sharp outputs but unstable and prone to mode collapse.  
VAE is stable, single loss, but outputs can be blurry. 

## Why diffusion is stable

Small, controlled updates in each step prevent oscillation and collapse, unlike adversarial GAN training.  

 ## One difficulty faced

 Tuning the noise schedule: too much noise destroys signal, too little reduces generation diversity.  

## How Stable Diffusion uses this idea

Stable diffusion encodes images as latent vectors and applies diffusion. It adds noise, then a trained denoiser generates new realistic images step by step.