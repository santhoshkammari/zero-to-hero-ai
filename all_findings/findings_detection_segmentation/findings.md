# Detection & Segmentation — Research Findings

## Object Detection Evolution

### The Core Problem
- Classification: what's in the image (one label)
- Detection: what AND where (class + bounding box), variable number of outputs
- This variable-length output is what makes detection architecturally unique

### Shared Vocabulary
- **Bounding boxes**: (cx, cy, w, h) center format vs (x1, y1, x2, y2) corner format. YOLO=center, COCO=(x,y,w,h) top-left, Pascal VOC=corner
- **IoU**: Area of Overlap / Area of Union. Scale-invariant. Standard threshold 0.5. COCO uses 0.5:0.95 in 0.05 steps
- **Anchor boxes**: Predefined box templates. Predict offsets instead of absolute coords. Much easier optimization. 3 ratios × 3 scales = 9 anchors typical
- **NMS**: Sort by confidence, keep top, remove all with IoU > threshold. Soft-NMS decays scores instead. DETR eliminates need entirely

### R-CNN Family (Two-Stage)
- **R-CNN (2014)**: Selective Search → ~2000 proposals → each through CNN separately → SVM classification. 47 sec/image. 84 hours training
- **Fast R-CNN (2015)**: CNN once on full image → feature map → RoI Pooling extracts per-proposal features. Bottleneck now Selective Search (~2 sec CPU)
- **Faster R-CNN (2015)**: Region Proposal Network (RPN) replaces Selective Search. RPN: small sliding window over feature map, at each position predicts objectness + box offsets for k anchors. Proposals in 10ms vs 2s. End-to-end trainable
- **RoI Align** (Mask R-CNN 2017): bilinear interpolation instead of quantization. Critical for pixel-level tasks

### One-Stage Detectors (Speed Path)
- **YOLO v1 (2016)**: Image → S×S grid, each cell predicts B boxes + C classes in single pass. 45 FPS. Struggled with small objects
- **YOLOv2**: Added anchors, batch norm, multi-scale training
- **YOLOv3**: Darknet-53, predictions at 3 scales via FPN
- **YOLOv4**: CSPDarknet, Mish activation, PANet, mosaic augmentation
- **YOLOv5**: PyTorch by Ultralytics, most widely used
- **YOLOv8 (2023)**: Anchor-free, decoupled head, multi-task (detection, segmentation, pose)
- **YOLO11 (2024)**: Latest iteration, improved efficiency

### SSD (2016)
- Multi-scale feature maps: early layers detect small objects, later layers detect large objects
- This multi-scale approach became standard (FPN, YOLOv3+)

### RetinaNet & Focal Loss (2017)
- Class imbalance: ~100k candidates per image, only ~10 contain objects
- Easy negatives dominate cross-entropy loss
- Focal Loss: FL(p) = -(1-p)^γ × log(p). When p high (easy), loss crushed to near zero
- γ=2 typical: easy examples with p>0.9 get ~100× less weight
- First one-stage to match two-stage accuracy. Proved gap was training problem, not architecture

### DETR Family (Transformer-Based)
- **DETR (2020)**: Direct set prediction. N learned object queries → Transformer decoder → N predictions. Hungarian algorithm for bipartite matching → no NMS needed
- Problem: 500 epochs to converge, poor on small objects
- **Deformable DETR**: Deformable attention (sparse keypoints instead of all locations). ~50 epochs. Better small objects
- **DINO**: Denoising training + improved query design. Top-performing DETR variant
- **RT-DETR**: Real-time optimized, multi-scale features, practical deployment speed

### Anchor-Free Detectors
- **CornerNet (2018)**: Detect corners as heatmaps, group with associative embeddings
- **CenterNet (2019)**: Detect centers as heatmaps, regress w/h
- **FCOS (2019)**: Each pixel predicts distances to 4 edges + centerness score
- Modern YOLOv8+ adopted anchor-free. Field largely moved away from explicit anchors

## Segmentation

### Three Types
1. **Semantic**: Every pixel gets class label. Can't distinguish instances. Use: driving, satellite
2. **Instance**: Each object gets own mask. Can separate Cat 1 from Cat 2. Use: counting, robotics
3. **Panoptic**: Unifies both. "Stuff" (road, sky) + "things" (cars, people). Every pixel accounted for

### FCN (2015)
- Replace FC layers with 1×1 convolutions → fully convolutional, any input size
- Transposed convolutions for upsampling
- Skip connections FCN-32s → FCN-16s → FCN-8s
- Proof of concept for end-to-end pixel prediction

### U-Net (2015)
- Symmetric encoder-decoder with skip connections (concatenation, not addition)
- Encoder: conv + pool → captures "what"
- Decoder: transposed conv → recovers "where"
- Skip connections: pass fine-grained spatial info directly, spatial detail doesn't need to survive bottleneck
- Dominates medical imaging: data-efficient, precise boundaries
- Variants: U-Net++, Attention U-Net, nnU-Net (auto-configured)

### DeepLab
- Atrous/dilated convolutions: expand receptive field without downsampling. Gaps between kernel elements
- ASPP: multiple dilation rates in parallel → multi-scale context
- DeepLabv3+: ASPP + decoder + modified backbone. Top-tier for natural images

### Mask R-CNN (2017)
- Faster R-CNN + parallel mask branch
- RoI Align (bilinear interpolation, no quantization)
- Predicts K binary masks per proposal (one per class), uses predicted class's mask
- Decouples classification from segmentation

### SAM (2023)
- Foundation model: 1B+ masks, 11M images
- Promptable: point, box, mask, text → segmentation mask
- Architecture: Image Encoder (ViT-H, runs once) + Prompt Encoder + Mask Decoder (lightweight, runs per prompt)
- Zero-shot: segments anything without fine-tuning
- SAM 2 (2024): extends to video with memory mechanism

### Mask2Former
- Unified architecture for all three segmentation types
- Mask classification framework with Transformer decoder
- Outputs set of binary masks + class labels
- State-of-the-art on COCO, ADE20K, Cityscapes

### Loss Functions
- **Cross-entropy**: per-pixel, dominated by majority class unless weighted
- **Dice loss**: optimizes overlap ratio, naturally handles class imbalance
- **Combined**: CE + λ × Dice typical in practice

### Evaluation
- **IoU/Jaccard**: |P ∩ G| / |P ∪ G| per-class
- **mIoU**: mean across classes, standard metric
- **Dice score**: 2|P ∩ G| / (|P| + |G|), standard in medical imaging
- **Pixel accuracy**: misleading with class imbalance
- Dice = 2 × IoU / (1 + IoU)

## Interview Depth
- Explain R-CNN → Fast → Faster evolution and what each solved
- NMS limitations in crowded scenes, Soft-NMS, DETR as alternative
- IoU limitations: GIoU, DIoU, CIoU for better box regression
- Anchor design: k-means clustering on dataset for optimal anchors
- Focal loss: why one-stage gap was training problem not architecture
- DETR: set prediction, Hungarian matching, no hand-crafted components
- U-Net skip connections: why concatenation preserves spatial info
- SAM: paradigm shift from task-specific to foundation model
- mAP@[0.5:0.95] vs mAP@0.5, size-specific AP breakdown
