# Missing Topics: Ch09 Cnns Computer Vision

Now I have all the information I need. Let me compile the comprehensive findings document:

Based on my thorough analysis, here's what the chapter covers and what's missing:

**Already well-covered:**
- CNN building blocks (conv, pooling, receptive field, depthwise separable, transposed conv, 1×1 conv, dilation)
- Architecture evolution (LeNet → AlexNet → VGG → GoogLeNet → ResNet → DenseNet → MobileNet → EfficientNet → ViT → Swin → ConvNeXt)
- Transfer learning (feature extraction, fine-tuning, knowledge distillation, domain adaptation)
- Image augmentation (geometric, color, Cutout, MixUp, CutMix, AutoAugment, TTA)
- Detection & Segmentation (R-CNN family, YOLO, SSD, RetinaNet, DETR, anchor-free, FCN, U-Net, DeepLab, Mask R-CNN, SAM)
- Modern vision (ViT deep dive, Swin, DeiT, ConvNeXt, CLIP, DINOv2, SAM, foundation models)
- Interpretability (Saliency, Grad-CAM, Integrated Gradients, TCAV, attention maps)
- Nice to Know (optical flow/RAFT, MOT/SORT/DeepSORT/ByteTrack, pose estimation, video understanding/C3D/I3D/VideoMAE, visual search/metric learning/ArcFace/FAISS, super-resolution/ESRGAN, NeRF/Gaussian Splatting, deformable conv, SE blocks)

**FPN is mentioned** but not given a dedicated deep-dive section. **Anchor-free detection** has its own subsection. **Receptive field calculation** is covered. **MobileNet/EfficientNet** are in architecture evolution. **CLIP/DINOv2** have deep coverage. **Metric learning/ArcFace** is in visual search section.

Here are the **truly missing topics**:

---

## Summary of Missing Topics for Chapter 9

### CRITICAL GAPS (High interview frequency, major application domains):

1. **OCR & Document Understanding** — Zero coverage. No text detection (EAST, DBNet), text recognition (CRNN, TrOCR), document layout analysis (LayoutLM, Donut), or scene text detection
2. **Face Recognition Pipeline** — Only ArcFace loss is mentioned in metric learning context. Missing: face detection (MTCNN, RetinaFace), face alignment, FaceNet architecture, face verification vs identification, anti-spoofing, face datasets (LFW, MegaFace)
3. **Depth Estimation & Stereo Vision** — Only a passing mention of "depth estimation" as a DINOv2 task. Missing: monocular depth estimation (MiDaS, DPT), stereo matching, disparity maps, structured light, time-of-flight sensors
4. **3D Vision & Point Clouds** — NeRF is covered but point cloud processing (PointNet, PointNet++), 3D object detection (VoxelNet, PointPillars), mesh reconstruction, and SLAM are completely absent
5. **Autonomous Driving Vision Pipeline** — Only brief mentions. Missing: BEV perception, multi-camera fusion, lane detection, 3D object detection from cameras, occupancy networks, sensor fusion (camera + LiDAR + radar)
6. **Image Generation in CV Context** — Style transfer mentioned only as "VGG use case." Missing: neural style transfer algorithm, image inpainting, image-to-image translation (pix2pix, CycleGAN), image harmonization
7. **Visual Anomaly Detection** — Mentioned as nav link to ch06. Missing CV-specific methods: PatchCore, knowledge distillation for anomaly detection, reconstruction-based methods, MVTec benchmark
8. **Open-Vocabulary & Grounded Detection** — No coverage of Grounding DINO, GLIP, open-set detection, or referring expression comprehension
9. **Classical CV Foundations** — SIFT/HOG mentioned only historically. Missing: image filtering, morphological operations, Hough transform, camera calibration, homography, feature matching — topics still asked in interviews
10. **Model Efficiency for Edge Deployment** — MobileNet/EfficientNet architectures covered, but missing: quantization for vision models, pruning, TensorRT/ONNX optimization, knowledge distillation pipelines for deployment, ShuffleNet, GhostNet, neural architecture search for edge

### MODERATE GAPS (Important for completeness):

11. **Medical Imaging** — U-Net mentioned, but missing: specific modality handling (CT, MRI, X-ray), attention U-Net, nnU-Net, medical image classification challenges, regulatory considerations
12. **Image Captioning & VQA** — LLaVA/GPT-4V mentioned in passing (CLIP section). Missing: BLIP/BLIP-2, Flamingo, visual grounding, image captioning architectures
13. **Satellite/Aerial/Remote Sensing** — Briefly mentioned. Missing: rotated object detection, multi-spectral imaging, change detection, geographic priors
14. **Data-Centric CV** — Missing: annotation tools/pipelines, active learning for CV, weak/semi-supervised detection, pseudo-labeling strategies, label noise handling
15. **Video Generation & Prediction** — Missing: frame prediction, video diffusion, video interpolation beyond optical flow

---

Now let me write this as a proper markdown file:

The chapter is remarkably comprehensive for a "Zero to Hero" book — it already covers receptive fields, FPN, anchor-free detection, MobileNet/EfficientNet, CLIP, DINOv2, metric learning, pose estimation, video understanding, NeRF, and super-resolution. The gaps below represent topics that are either completely absent or mentioned only in passing without dedicated explanatory coverage.

Here's the complete findings document:

---

# Chapter 9 "CNNs & Computer Vision" — Missing Topics Analysis

## Summary

Chapter 9 is already very comprehensive, covering CNN building blocks, architecture evolution (LeNet through ConvNeXt), transfer learning, augmentation, detection/segmentation (including DETR, anchor-free, SAM), modern vision (ViT, Swin, CLIP, DINOv2), interpretability, and a rich "Nice to Know" section (optical flow, tracking, pose estimation, video understanding, visual search/metric learning, super-resolution, NeRF/Gaussian Splatting). However, several important CV domains with high interview frequency and industry relevance are either completely absent or only briefly mentioned without dedicated coverage.

---

## 1. OCR & Document Understanding

**Current coverage:** Only a passing mention of "Document scanning, OCR" in an augmentation table cell.

**What's missing:**
- **Text detection**: EAST, DBNet, CRAFT — detecting text regions in natural scenes vs documents
- **Text recognition**: CRNN (CNN + BiLSTM + CTC), attention-based sequence decoders, TrOCR (transformer-based)
- **End-to-end scene text**: Reading text "in the wild" — street signs, product labels, license plates
- **Document layout analysis**: LayoutLM, LayoutLMv3, Donut (OCR-free document understanding)
- **Table extraction**: Detecting and parsing tabular data from images
- **Handwriting recognition**: Online vs offline, stroke-based approaches
- **Key-value extraction**: Invoice processing, form understanding, receipt parsing

**Why it matters:** OCR/document AI is one of the largest deployed CV application areas (banking, insurance, logistics). Common interview topic for applied ML roles. The pipeline (detect → recognize → structure) is a complete CV system design question.

**Sources:** `jbhuang0604/awesome-computer-vision` lists "Awesome Document Understanding" as a major subfield. `andrewekhalel/MLQuestions` Q#11 mentions integral images used in text detection (Viola-Jones-style).

---

## 2. Face Recognition Pipeline (End-to-End)

**Current coverage:** ArcFace loss function is explained in the "Visual Search & Retrieval" section of Nice to Know. Face verification mentioned once in a sentence.

**What's missing:**
- **Face detection**: MTCNN (multi-task cascaded), RetinaFace, BlazeFace for mobile
- **Face alignment**: Landmark detection, affine transformation to canonical pose
- **FaceNet architecture**: The embedding approach that popularized face verification
- **Face verification vs identification**: 1:1 matching vs 1:N search — different problems
- **Loss evolution**: Softmax → Center Loss → SphereFace → CosFace → ArcFace progression
- **Anti-spoofing/liveness detection**: Print attacks, replay attacks, 3D mask attacks
- **Face datasets & benchmarks**: LFW, MegaFace, WIDER FACE, IJB
- **Ethical concerns**: Bias across demographics, surveillance implications, deepfake detection
- **The complete pipeline**: Detection → Alignment → Feature Extraction → Matching/Verification

**Why it matters:** Face recognition is one of the most common CV interview system design questions. The pipeline illustrates how multiple CV components chain together. Ethical/bias discussion is increasingly expected.

**Sources:** `jbhuang0604/awesome-computer-vision` lists both "Awesome Face" and "Awesome Face Recognition" as major topics.

---

## 3. Depth Estimation & Stereo Vision

**Current coverage:** "Depth estimation" mentioned once as a DINOv2 downstream task.

**What's missing:**
- **Monocular depth estimation**: MiDaS, DPT, Depth Anything — predicting depth from a single image
- **Stereo matching**: Disparity maps, cost volumes, stereo correspondence (classical + learned)
- **Self-supervised depth**: Monodepth, using view synthesis as training signal
- **Depth sensors**: Structured light (Kinect), Time-of-Flight, LiDAR vs camera trade-offs
- **Depth completion**: Sparse-to-dense depth from sparse LiDAR + camera
- **Applications**: AR/VR, robotics, 3D photography, bokeh effects, obstacle avoidance

**Why it matters:** Depth estimation is fundamental to 3D understanding and frequently tested in robotics/autonomous driving interviews. Monocular depth (especially Depth Anything, MiDaS) has become accessible and widely deployed.

---

## 4. 3D Vision & Point Cloud Processing

**Current coverage:** NeRF and Gaussian Splatting are well covered for novel view synthesis. Point clouds mentioned only as "not a mesh or a point cloud."

**What's missing:**
- **PointNet & PointNet++**: Direct processing of unordered point sets, hierarchical feature learning
- **3D object detection**: VoxelNet, PointPillars, CenterPoint — detecting objects in 3D space
- **3D semantic segmentation**: RandLA-Net, MinkowskiNet — labeling every 3D point
- **Mesh reconstruction**: From images or point clouds to watertight meshes
- **SLAM**: Visual SLAM (ORB-SLAM), visual-inertial odometry, real-time mapping
- **Structure from Motion (SfM)**: COLMAP, multi-view reconstruction pipeline
- **Multi-view stereo (MVS)**: Dense 3D from multiple calibrated views
- **Volumetric representations**: Voxels, occupancy networks, signed distance functions (SDF)
- **3D data representations comparison**: Point clouds vs voxels vs meshes vs implicit functions

**Why it matters:** 3D vision is critical for robotics, AR/VR, autonomous driving, and manufacturing. PointNet is a classic interview question ("how do you handle unordered sets?"). 3D detection is the backbone of autonomous driving perception.

**Sources:** `jbhuang0604/awesome-computer-vision` lists "Awesome 3D Machine Learning" as a major resource. Interview Q#16 from `andrewekhalel/MLQuestions` directly asks about 3D reconstruction.

---

## 5. Autonomous Driving Vision Pipeline

**Current coverage:** Autonomous driving mentioned 3 times in passing (as an application example), never as a dedicated topic.

**What's missing:**
- **Bird's Eye View (BEV) perception**: Transforming camera features to BEV space (BEVFormer, LSS, BEVDet)
- **Multi-camera fusion**: Surrounding-view perception from 6+ cameras
- **Lane detection**: Polynomial regression, anchor-based, segmentation-based approaches
- **3D object detection from cameras**: FCOS3D, DETR3D, PETR — monocular/multi-camera 3D detection
- **Occupancy prediction**: Predicting which 3D voxels are occupied (Tesla's approach)
- **Sensor fusion**: Camera + LiDAR + Radar — early vs late fusion, cross-attention fusion
- **Temporal modeling**: Using past frames for velocity estimation and prediction
- **Map construction**: Online HD map generation, vectorized map prediction
- **End-to-end driving**: UniAD, perception-prediction-planning in one model

**Why it matters:** Autonomous driving is the largest commercial application of CV, and pipeline design is a premier system design interview question. BEV perception is one of the most active research areas (2022-2024).

---

## 6. Image Generation in CV Context (Style Transfer, Inpainting)

**Current coverage:** Style transfer mentioned only as "VGG is still used for style transfer and perceptual loss." Diffusion models noted as a separate chapter (Ch14).

**What's missing:**
- **Neural style transfer**: Gatys et al. algorithm, content vs style loss, fast style transfer (Johnson et al.)
- **Perceptual loss function**: Why VGG features make better loss functions than pixel MSE — deeply important for many CV tasks
- **Image inpainting**: Filling missing regions — partial convolutions, gated convolutions, LaMa
- **Image-to-image translation**: pix2pix (paired), CycleGAN (unpaired) — foundational ideas
- **Image harmonization**: Making composited objects blend naturally
- **Colorization**: Adding color to grayscale images
- **Image denoising**: Classical (BM3D) and learned (DnCNN, Restormer)
- **HDR imaging**: Multi-exposure fusion, tone mapping

**Why it matters:** Perceptual loss is used everywhere (super-resolution, style transfer, image synthesis) and understanding *why* feature-space losses work is an important interview concept. Inpainting/image-to-image translation demonstrate conditional generation before diffusion models.

---

## 7. Visual Anomaly Detection for CV

**Current coverage:** Anomaly detection referenced only as a chapter 6 topic (likely statistical/tabular). Industrial inspection mentioned 3 times in passing.

**What's missing:**
- **Visual anomaly detection methods**: PatchCore, SPADE, knowledge distillation (STPM, reverse distillation)
- **Reconstruction-based approaches**: Autoencoders, memory banks — detect anomalies as high reconstruction error
- **Teacher-student approaches**: Train student to mimic teacher on normal data; divergence = anomaly
- **MVTec AD benchmark**: Standard dataset, defect types (scratch, dent, contamination, structural)
- **Few-shot/zero-shot anomaly detection**: WinCLIP, AnomalyCLIP — using foundation models
- **Localization**: Not just detecting "anomalous image" but highlighting the defective region
- **Industrial deployment considerations**: False positive rates, domain-specific thresholds

**Why it matters:** Visual anomaly detection is a massive industry application (manufacturing, semiconductor inspection, food quality). It's a distinct paradigm — often one-class classification with only normal training samples — that doesn't fit neatly into standard detection/segmentation frameworks.

---

## 8. Open-Vocabulary & Grounded Detection

**Current coverage:** Zero dedicated coverage. Open-vocabulary detection mentioned once in passing in CLIP section.

**What's missing:**
- **Grounding DINO**: Detecting objects described by arbitrary text prompts
- **GLIP**: Grounded Language-Image Pre-training — unifying detection and grounding
- **Open-vocabulary segmentation**: Combining SAM + CLIP for text-guided segmentation
- **Referring expression comprehension**: "the red car on the left" → bounding box
- **OWL-ViT, OWLv2**: Open-world detection with vision-language models
- **Practical pipeline**: CLIP → filter candidates → SAM → segment — the modern zero-shot pipeline

**Why it matters:** This represents the current frontier of detection — moving beyond fixed class sets to detecting anything described in language. It's the practical convergence of CLIP + detection that many companies are deploying now (2024-2025).

---

## 9. Classical Computer Vision Foundations

**Current coverage:** SIFT/HOG mentioned as historical context for pre-deep-learning era. Canny edge detection not mentioned.

**What's missing:**
- **Image filtering**: Gaussian blur, Sobel, Laplacian — still used in preprocessing
- **Edge detection**: Canny algorithm steps (gradient, non-max suppression, hysteresis)
- **Feature descriptors**: SIFT, SURF, ORB — how they work, not just that they exist
- **Feature matching**: FLANN, brute-force matching, ratio test (Lowe's)
- **Homography & perspective transform**: RANSAC for robust estimation
- **Camera model**: Pinhole model, intrinsics/extrinsics, lens distortion
- **Camera calibration**: Checkerboard calibration, Zhang's method
- **Morphological operations**: Erosion, dilation, opening, closing — used in post-processing
- **Contour detection & analysis**: OpenCV contour hierarchy, moments
- **Color spaces**: HSV, LAB — when to use which for specific tasks

**Why it matters:** These topics are asked in CV interviews surprisingly often, especially at companies with production CV systems that combine classical + deep learning. Camera calibration is essential for any multi-view or 3D vision system. Many "quick-and-dirty" CV solutions still use classical approaches.

**Sources:** `andrewekhalel/MLQuestions` includes questions on connected components (Q#9), integral images (Q#11), RANSAC (Q#12), image registration (Q#14), and 3D reconstruction (Q#16).

---

## 10. Model Efficiency & Edge Deployment for Vision

**Current coverage:** MobileNet and EfficientNet architectures are well-explained. Knowledge distillation covered. "Edge deployment" mentioned in a table cell.

**What's missing:**
- **Quantization for vision**: INT8/INT4 quantization, quantization-aware training (QAT) vs post-training quantization (PTQ)
- **Pruning**: Structured vs unstructured pruning for CNNs, lottery ticket hypothesis
- **Neural Architecture Search (NAS)**: How EfficientNet/MobileNet were found; DARTS, once-for-all networks
- **Deployment frameworks**: TensorRT, ONNX Runtime, CoreML, TFLite — converting models for inference
- **ShuffleNet**: Channel shuffle operation for efficient group convolutions
- **GhostNet**: Generating more feature maps from cheap operations
- **RepVGG/re-parameterization**: Training with complex topology, deploying as simple conv
- **Latency vs accuracy trade-offs**: How to benchmark properly (FLOPs ≠ latency)
- **Hardware-aware design**: Designing architectures for specific hardware (GPU vs NPU vs DSP)

**Why it matters:** Deploying CV models on edge devices (phones, IoT, embedded systems) is where most production CV lives. Understanding quantization effects on detection accuracy, or why FLOPs don't predict latency, separates practitioners from academics.

---

## 11. Medical Imaging (Dedicated Section)

**Current coverage:** U-Net origin story, medical imaging mentioned several times as application context, Integrated Gradients baseline discussion mentions X-rays.

**What's missing:**
- **Modality-specific challenges**: CT (3D volumes), MRI (multi-sequence), X-ray (projection), histopathology (gigapixel), dermoscopy, fundoscopy
- **3D segmentation**: Processing volumetric data — 3D U-Net, V-Net, nnU-Net (self-configuring)
- **Attention U-Net**: Adding attention gates to skip connections
- **Medical image classification**: CheXNet, dealing with class imbalance, multi-label classification
- **Data challenges**: Limited labeled data, privacy (federated learning), domain shift across hospitals
- **Evaluation metrics specific to medical**: Hausdorff distance, surface dice, clinically relevant metrics
- **Regulatory considerations**: FDA clearance, clinical validation vs technical validation
- **Weakly supervised approaches**: Using image-level labels for localization (common in radiology)

**Why it matters:** Medical AI is one of the fastest-growing CV application areas with unique constraints (small datasets, high stakes, regulatory requirements). It's a common domain specialization asked about in interviews.

---

## 12. Image Captioning, VQA & Vision-Language Tasks

**Current coverage:** LLaVA and GPT-4V mentioned as CLIP applications. No dedicated discussion of captioning or VQA architectures.

**What's missing:**
- **Image captioning evolution**: Show-and-Tell → Show-Attend-and-Tell → BLIP → BLIP-2
- **Visual Question Answering (VQA)**: Task formulation, datasets (VQAv2), evaluation
- **BLIP/BLIP-2**: Bootstrapping vision-language pre-training, Q-Former architecture
- **Flamingo**: Few-shot visual reasoning with interleaved image-text
- **Visual grounding**: Connecting text phrases to image regions
- **Text-to-image retrieval**: Beyond CLIP — fine-grained retrieval
- **GPT-4V/Gemini capabilities**: What multimodal LLMs can and can't do for CV tasks
- **Document VQA**: Answering questions about charts, diagrams, tables

**Why it matters:** Vision-language models are the current frontier. Understanding the architecture patterns (how vision encoders connect to language models) is increasingly important. This bridges Ch9 (CV) with Ch12 (LLMs).

---

## 13. Satellite & Remote Sensing Imagery

**Current coverage:** "Satellite land-use mapping" and "counting cars in satellite photos" mentioned as examples.

**What's missing:**
- **Rotated/oriented object detection**: OBB (oriented bounding boxes) — ships, vehicles, buildings at arbitrary angles
- **Multi-spectral and hyperspectral imaging**: Beyond RGB — near-infrared, thermal bands
- **Change detection**: Comparing satellite images over time to detect construction, deforestation, disasters
- **Super-resolution for satellite**: Enhancing low-res satellite imagery
- **Geo-spatial priors**: Using geographic coordinates, elevation, season as features
- **Large-scale tiling**: Processing images too large to fit in memory — sliding window, stitching
- **Specific architectures**: HRNet for dense prediction, specialized augmentation (random rotate 360°)

**Why it matters:** Remote sensing is a significant CV market (agriculture, defense, climate monitoring, insurance). The constraints are unique: massive image sizes, unusual spectral bands, rotated objects, temporal change analysis.

---

## 14. Data-Centric Computer Vision

**Current coverage:** Augmentation is well-covered. No dedicated discussion of annotation, active learning, or semi-supervised approaches for CV.

**What's missing:**
- **Annotation tools & workflows**: Labelbox, CVAT, Label Studio — the human side of CV
- **Active learning for CV**: Selecting the most informative images to label
- **Semi-supervised detection/segmentation**: Pseudo-labeling, teacher-student for detection
- **Weak supervision for CV**: Image-level labels for segmentation (CAM-based), point/box supervision
- **Data cleaning for CV**: Detecting mislabeled images, duplicate detection
- **Synthetic data**: Domain randomization, sim-to-real transfer, using 3D rendering for training
- **Dataset bias & distribution shift**: Domain gap between training and deployment
- **Class imbalance handling**: Long-tail distributions in detection/recognition

**Why it matters:** In production CV, data quality and labeling efficiency often matter more than architecture choice. This represents the "unsexy but critical" work that dominates real-world CV engineering.

---

## 15. Few-Shot & Zero-Shot Learning for Vision

**Current coverage:** CLIP zero-shot classification well-explained. SAM zero-shot segmentation covered.

**What's missing:**
- **Few-shot classification**: Prototypical Networks, Matching Networks, MAML for vision
- **Meta-learning approaches**: Learning to learn from few examples
- **Zero-shot via attributes**: Describing classes by properties
- **Foundation model adaptation**: How to adapt CLIP/DINOv2 with minimal labeled data (linear probing, prompt tuning, adapters)
- **In-context learning for vision**: Visual prompting, providing examples as part of input

**Why it matters:** Real-world CV often has limited labeled data for new categories. Understanding how to leverage foundation models with minimal supervision is the current practical paradigm.

---

## Priority Ranking for Addition

| Priority | Topic | Justification |
|----------|-------|--------------|
| 🔴 High | OCR & Document Understanding | Major industry application, zero coverage |
| 🔴 High | Face Recognition Pipeline | Classic interview system design question |
| 🔴 High | Classical CV Foundations | Frequently asked in interviews, bridges theory to practice |
| 🔴 High | Open-Vocabulary Detection | Current frontier, rapidly becoming standard |
| 🟡 Medium | Autonomous Driving Pipeline | Largest CV market, system design interviews |
| 🟡 Medium | Depth Estimation & Stereo | Fundamental 3D understanding, growing importance |
| 🟡 Medium | 3D Vision & Point Clouds | PointNet is a classic, important for robotics |
| 🟡 Medium | Model Efficiency & Edge | Production reality, MobileNet/EfficientNet need companion deployment discussion |
| 🟡 Medium | Image Generation in CV Context | Perceptual loss is cross-cutting, style transfer is instructive |
| 🟡 Medium | Visual Anomaly Detection | Major industry application, unique paradigm |
| 🟠 Lower | Medical Imaging (dedicated) | Already touched on, could be a domain applications section |
| 🟠 Lower | Captioning & VQA | Bridges to Ch12 (LLMs), may fit better there |
| 🟠 Lower | Data-Centric CV | Cross-cutting concern, could fit in Ch3 or Ch4 |
| 🟠 Lower | Satellite/Remote Sensing | Domain-specific, lower interview frequency |
| 🟠 Lower | Few-Shot/Zero-Shot | Partially covered via CLIP/SAM, could be expanded |
