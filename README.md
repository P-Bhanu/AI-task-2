# Screen Recording Instructions

## 📹 How to Record Demo Video

### For Linux (Ubuntu/Debian)

#### Option 1: SimpleScreenRecorder (Recommended)
```bash
# Install
sudo apt update
sudo apt install simplescreenrecorder

# Record
simplescreenrecorder
```

**Settings**:
- Resolution: 1920x1080 (Full HD)
- Frame rate: 30 fps
- Format: MP4 (H.264)
- Audio: Optional (can add voice narration)

#### Option 2: OBS Studio
```bash
# Install
sudo apt install obs-studio

# Record
obs
```

#### Option 3: Kazam (Lightweight)
```bash
# Install
sudo apt install kazam

# Record
kazam
```

### For macOS

#### QuickTime Player (Built-in)
1. Open QuickTime Player
2. File → New Screen Recording
3. Click red record button
4. Click anywhere to start recording
5. Click stop button in menu bar when done
6. File → Save

#### Option 2: OBS Studio
```bash
# Install via Homebrew
brew install --cask obs

# Launch
open /Applications/OBS.app
```

### For Windows

#### Option 1: Xbox Game Bar (Built-in)
1. Press `Win + G`
2. Click the record button (or `Win + Alt + R`)
3. Stop recording with `Win + Alt + R`
4. Video saved to: `C:\Users\[YourName]\Videos\Captures`

#### Option 2: OBS Studio
1. Download from: https://obsproject.com/
2. Install and launch
3. Add Display Capture source
4. Click Start Recording

#### Option 3: Screen Recorder (Windows 11)
1. Press `Win + Shift + R`
2. Select recording area
3. Click record button

### For Raspberry Pi (ARM)

```bash
# Install ffmpeg for screen recording
sudo apt install ffmpeg

# Record screen (X11)
ffmpeg -video_size 1920x1080 -framerate 25 -f x11grab -i :0.0 output.mp4

# Stop recording: Press Ctrl+C
```

## 🎬 What to Record

### Recommended Recording Flow (5-10 minutes)

#### Part 1: Setup (2 minutes)
1. Show terminal in project directory
2. Run: `ls -la` to show project files
3. Run: `cat requirements.txt` to show dependencies
4. Run: `./setup.sh` or manual installation
5. Show virtual environment activation

#### Part 2: Generate Samples (1 minute)
1. Run: `python generate_samples.py`
2. Show console output
3. Open `sample_images/` folder
4. Display 2-3 sample images

#### Part 3: Run Inspection (2 minutes)
1. Run: `python quality_inspection.py`
2. Show console output with detections
3. Highlight:
   - Image names being processed
   - Defect counts
   - Confidence scores
   - Coordinates

#### Part 4: View Results (3 minutes)
1. Open `output/` folder
2. Show annotated images:
   - `annotated_defect_scratch_1.jpg`
   - `annotated_defect_missing_1.jpg`
   - `annotated_defect_multiple_1.jpg`
   - `annotated_good_sample_1.jpg`
3. Open `inspection_results.json`
4. Highlight JSON structure:
   - Defect type
   - Bounding boxes
   - Center coordinates
   - Confidence scores
   - Severity levels

#### Part 5: Custom Image (Optional - 2 minutes)
1. Add a custom image to `sample_images/`
2. Run inspection again
3. Show results

## 📝 Recording Tips

### Before Recording
- ✅ Close unnecessary applications
- ✅ Clear terminal history: `clear`
- ✅ Increase terminal font size for readability
- ✅ Set terminal size: 80x24 or larger
- ✅ Test audio if adding narration
- ✅ Prepare a script or outline

### During Recording
- ✅ Speak clearly if narrating
- ✅ Move mouse slowly and deliberately
- ✅ Pause briefly between steps
- ✅ Highlight important output
- ✅ Keep recording under 10 minutes

### After Recording
- ✅ Review video for clarity
- ✅ Edit out mistakes if needed
- ✅ Add title screen (optional)
- ✅ Compress if file size > 100MB

## 🎨 Video Editing (Optional)

### Linux
```bash
# Install OpenShot (free video editor)
sudo apt install openshot-qt

# Or Kdenlive
sudo apt install kdenlive
```

### macOS
- iMovie (built-in)
- Final Cut Pro (paid)

### Windows
- Windows Video Editor (built-in)
- DaVinci Resolve (free)

## 📦 Compress Video

If video file is too large:

```bash
# Install ffmpeg
sudo apt install ffmpeg  # Linux
brew install ffmpeg      # macOS

# Compress video
ffmpeg -i input.mp4 -vcodec h264 -acodec mp2 -b:v 2M output.mp4
```

## 📤 Upload to GitHub

### Option 1: Direct Upload
1. Go to your GitHub repository
2. Navigate to `demo_video/` folder
3. Click "Add file" → "Upload files"
4. Upload video file
5. Commit changes

**Note**: GitHub has a 100MB file size limit. If your video is larger, use Option 2.

### Option 2: Git LFS (Large Files)
```bash
# Install Git LFS
sudo apt install git-lfs  # Linux
brew install git-lfs      # macOS

# Initialize
git lfs install

# Track video files
git lfs track "*.mp4"
git add .gitattributes

# Add and commit
git add demo_video/quality_inspection_demo.mp4
git commit -m "Add demo video"
git push
```

### Option 3: External Hosting
If video is very large, upload to:
- YouTube (unlisted)
- Google Drive
- Dropbox

Then add link in README:
```markdown
## Demo Video
[Watch Demo Video](https://youtube.com/watch?v=YOUR_VIDEO_ID)
```

## ✅ Checklist

Before uploading your video:

- [ ] Video shows complete installation process
- [ ] Sample generation is demonstrated
- [ ] Detection script runs successfully
- [ ] Output files are shown and explained
- [ ] JSON structure is clearly visible
- [ ] Annotated images are displayed
- [ ] Video duration: 5-10 minutes
- [ ] Audio is clear (if included)
- [ ] File size < 100MB (or use Git LFS)
- [ ] Video format: MP4 (recommended)
- [ ] Resolution: 1080p or 720p minimum

## 📋 Sample Script

Use this script while recording:

```
[Part 1]
"Hello, I'll demonstrate the Automated Quality Inspection System."
"First, let's look at the project structure..."
[Show files with ls]
"Now I'll install the dependencies..."
[Run setup.sh]

[Part 2]
"Let's generate sample images for testing..."
[Run generate_samples.py]
"As you can see, we have 5 images: 1 clean and 4 with defects."
[Show sample images]

[Part 3]
"Now I'll run the inspection system..."
[Run quality_inspection.py]
"The system detects scratches, discoloration, and missing components."
"Each defect has coordinates, confidence scores, and severity levels."

[Part 4]
"Let's examine the results..."
[Show output folder]
"Here are the annotated images with defects marked..."
[Open annotated images]
"And here's the detailed JSON output..."
[Open inspection_results.json]
"Notice the bounding boxes, center coordinates, and confidence scores."

[Part 5]
"This system is production-ready and cross-platform compatible."
"Thank you for watching!"
```

## 🔗 Additional Resources

- **OBS Studio**: https://obsproject.com/
- **SimpleScreenRecorder**: https://www.maartenbaert.be/simplescreenrecorder/
- **FFmpeg**: https://ffmpeg.org/
- **Git LFS**: https://git-lfs.github.com/

## 📊 Recommended Video Specifications

| Setting | Value |
|---------|-------|
| Resolution | 1920x1080 (1080p) |
| Frame Rate | 30 fps |
| Format | MP4 (H.264) |
| Bitrate | 2-5 Mbps |
| Audio | AAC, 128 kbps (optional) |
| Duration | 5-10 minutes |
| File Size | < 100 MB (or use Git LFS) |

---

Need help? Check the main README.md or open an issue on GitHub!
