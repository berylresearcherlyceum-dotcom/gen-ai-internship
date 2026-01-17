## Why the Generator never sees real data labels.

The Generator only creates fake samples from random noise.  
It learns indirectly from the Discriminator’s feedback, not from real labels.  
This ensures it focuses on fooling the Discriminator, rather than copying real data.

## Why losses oscillate instead of converging smoothly.

GANs are a game between Generator and Discriminator.  
When one improves, the other struggles, causing losses to **go up and down** instead of converging smoothly.

## What mode collapse means.

Mode collapse happens when the Generator produces **the same output repeatedly** instead of diverse samples, ignoring most of the real data’s variety.

## Why GANs are harder to train than VAEs.

GANs have two networks competing, so small changes can destabilize training.  
VAEs have a single loss, making them more stable and easier to train.

## How GANs create sharper, more diverse samples than VAEs.

GANs use a Discriminator to push the Generator to produce **realistic and varied outputs**,  
while VAEs tend to average possibilities, resulting in **blurry or less diverse samples**.

## Generator vs Discriminator roles

Generator creates fake data from random noise.  
Discriminator tries to tell real data from fake data.  

## Why GAN loss oscillates

Generator and Discriminator compete; when one improves, the other struggles, causing losses to go up and down.  

## What mode collapse is

When the Generator produces the same output repeatedly, ignoring diversity in real data.  

## GAN vs VAE comparison

GANs produce sharper, more diverse samples because of adversarial training.  
VAEs are more stable but outputs can be blurry due to averaging.  

## One training instability faced

Using a high learning rate caused D_loss and G_loss to jump wildly instead of stabilizing. 

## How GANs relate to diffusion models

Both are generative models producing realistic data.GANs use adversarial training, diffusion models iteratively refine noise into data.



