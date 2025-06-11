# Image processing pipeline

Question(s):
- How do pixels get from the image sensor into the jpeg encoder?
- How are film simulations calculated and applied?

These are both hardware questions and software (IP/driver) questions.

- https://www.cs.unc.edu/~ronisen/teaching/spring_2023/web_materials/lecture4_camera.pdf

A real world example of an image signal processor: https://rockchip.fr/RK3288%20TRM/rk3288-chapter-31-image-signal-processing-(isp).pdf  
And the kernel driver: https://github.com/torvalds/linux/tree/19272b37aa4f83ca52bdf9c16d5d81bdd1354494/drivers/media/platform/rockchip/rkisp1  

## Trivia

| Name | Desc |
| --- | --- |
| LSC | Lens Shade Correction (vignetting) |
| CAC | Chromatic Aberration Correction |
| BLS | Black Level Subtraction |
| WDR | Wide Dynamic Range |
| DPF | De-noising Pre-filter |
| DPCC | Defect Pixel Cluster Correction |
| EFF | Image Effects |
