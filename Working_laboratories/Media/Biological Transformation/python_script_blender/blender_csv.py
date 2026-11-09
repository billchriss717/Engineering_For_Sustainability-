import bpy
import csv
from pathlib import Path

# Get the active movie clip
clip = next(iter(bpy.data.movieclips), None)

if clip is None:
    raise RuntimeError("No movie clip found.")

# Video dimensions
width, height = clip.size

# Frame rate
scene = bpy.context.scene
fps = scene.render.fps / scene.render.fps_base

# Output file: same folder as the .blend file
output_path = bpy.path.abspath("//tracking_data.csv")

# Get the first four tracking tracks
tracks = list(clip.tracking.tracks)[:4]

if not tracks:
    raise RuntimeError("No tracking markers found.")

# Collect marker coordinates
track_data = {}
all_frames = set()

for track in tracks:
    positions = {}

    for marker in track.markers:
        if not marker.mute:
            frame = marker.frame

            # Normalized coordinates to pixels
            x = marker.co.x * width
            y = marker.co.y * height

            positions[frame] = (x, y)
            all_frames.add(frame)

    track_data[track.name] = positions

if not all_frames:
    raise RuntimeError("No valid tracking data found.")

# Export every frame in the tracking range
first_frame = min(all_frames)
last_frame = max(all_frames)

with open(output_path, "w", newline="") as file:
    writer = csv.writer(file)

    header = ["Frame", "Time (s)"]
    for track in tracks:
        header.extend([
            f"{track.name}_X",
            f"{track.name}_Y"
        ])

    writer.writerow(header)

    for frame in range(first_frame, last_frame + 1):
        time = (frame - first_frame) / fps

        row = [frame, round(time, 6)]

        for track in tracks:
            position = track_data[track.name].get(frame)

            if position is not None:
                row.extend([
                    round(position[0], 3),
                    round(position[1], 3)
                ])
            else:
                row.extend(["", ""])

        writer.writerow(row)

# Completion popup


def show_message(message, title="CSV Export Complete"):
    def draw(self, context):
        for line in message:
            self.layout.label(text=line)

    bpy.context.window_manager.popup_menu(
        draw, title=title, icon='INFO'
    )


show_message([
    f"Exported {last_frame - first_frame + 1} frames",
    f"Tracking markers: {len(tracks)}",
    f"Frame rate: {fps:.3f} fps",
    f"File: {output_path}"
])

print(f"Tracking data exported to {output_path}")
