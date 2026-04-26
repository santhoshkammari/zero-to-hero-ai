# Ch09 Nice to Know - Research Summary

## Topics to Cover (with deep intuition)
1. **Video Understanding** - 3D convolutions (C3D, I3D), Video Transformers (TimeSformer, ViViT), two-stream networks, VideoMAE
2. **Pose Estimation** - Top-down (detect person → keypoints) vs Bottom-up (detect all keypoints → group). OpenPose uses PAFs. HRNet maintains high-res throughout. MediaPipe for real-time.
3. **Visual Search & Retrieval** - Embedding space, metric learning, triplet loss, contrastive loss, ArcFace. Vector databases (FAISS, Milvus).
4. **Neural Radiance Fields (NeRF)** - 5D input (x,y,z,θ,φ) → color + density. Slow rendering. Gaussian Splatting is faster successor using explicit 3D Gaussians.
5. **Optical Flow** - Per-pixel motion vectors. RAFT: feature extraction → all-pairs correlation volume → iterative refinement with ConvGRU.
6. **Multi-Object Tracking (MOT)** - SORT (Kalman + Hungarian), DeepSORT (+appearance features), ByteTrack (+low confidence detections).
7. **Image Super-Resolution** - ESRGAN, Real-ESRGAN. GAN approach. Model hallucinating detail, not recovering it.
8. **Deformable Convolutions** - Learnable offsets on sampling grid. Adapts kernel shape to object geometry.
9. **Squeeze-and-Excitation Blocks** - Channel attention: squeeze (global avg pool) → excite (FC bottleneck) → scale channels.

## Running Example Idea
A wildlife camera trap system - monitoring animals in a forest reserve. Starts with detecting animals, then tracking them across frames, estimating poses, searching for similar animals, enhancing low-res nighttime images, understanding video clips, reconstructing 3D scenes.

## Key Analogies
- "Spotlight vs floodlight" - top-down vs bottom-up pose estimation
- "Fingerprint for images" - embeddings in visual search
- "Customs officer checking passports" - tracking identity across frames
