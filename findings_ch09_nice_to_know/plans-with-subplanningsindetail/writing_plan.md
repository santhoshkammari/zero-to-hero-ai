# Writing Plan for Ch09 Nice to Know

## Structure
1. Personal confession opening - avoided the "extras" of CV, always focused on classification/detection
2. Orientation - CV is bigger than detection and classification
3. Heads-up - prerequisite dismissal
4. Journey invitation

## Topic Flow (connected via running example: wildlife camera trap)
- Start with optical flow (something moved between frames)
- Multi-object tracking (which animal is which across frames)
- Pose estimation (what is the animal doing)
- Video understanding (understanding behavior over time)
- Visual search (finding similar animals in database)
- Image super-resolution (enhancing nighttime captures)
- NeRF / Gaussian Splatting (reconstructing the 3D habitat)
- Deformable convolutions & SE blocks (architectural building blocks that power many of the above)

## Rest Stop
After tracking + pose estimation + video understanding (the temporal stuff)
Before visual search, super-resolution, 3D reconstruction (the "other dimensions")

## Vulnerability Moments
1. Opening: confession about avoiding these topics
2. Optical flow: "I used to think optical flow was obsolete with deep learning"
3. Tracking: "identity maintenance across occlusion still trips me up conceptually"
4. NeRF: "still developing intuition for why volume rendering works so well"
5. Super-resolution: honest about hallucination problem
