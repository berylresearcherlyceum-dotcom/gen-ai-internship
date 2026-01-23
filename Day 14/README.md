## How this mirrors LLM temperature & sampling.

LLM Temperature & Sampling:

Sampling picks outputs based on probabilities.
Low temp → safe, repeated outputs.
High temp → creative, diverse outputs.

## Trade-off between creativity and correctness.

Creativity vs Correctness:

Low temperature: safe, predictable → high correctness, low creativity.
High temperature: more random → high creativity, may reduce correctness.

## How VAE, GAN, Diffusion differ conceptually

VAE: compresses & reconstructs → smooth but blurry
GAN: generator vs discriminator → sharp but unstable
Diffusion: stepwise noise & denoise → stable, high-quality

## Why diffusion is dominant today

Diffusion is dominant because it is stable and reliable. It produces high-quality, diverse outputs consistently. Also it avoids GAN problems like mode collapse and unstable training.

## Where GANs still make sense

Fast image generation when speed is more important than perfect stability. It works well for high-resolution images if training is carefully managed.

## How LLMs fit into generative modeling

Generate text/code using probabilities, temperature controls creativity vs correctness.

## One key insight gained during the internship

Learned how generative models work, when to use them, and how sampling affects outputs.
