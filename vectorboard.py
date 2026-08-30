import numpy as np
import matplotlib.pyplot as plt

def get_random_edge_coord(n, rng):
    edge = rng.integers(0, 4)
    pos = rng.integers(0, n)

    if edge == 0:
        return np.array([0, pos])
    elif edge == 1:
        return np.array([n - 1, pos])
    elif edge == 2:
        return np.array([pos, 0])
    else:
        return np.array([pos, n - 1])

n = int(input())

mogli = np.full((n, n, 2 , 2), True, dtype=bool)
mogli[0,:,0,0]= False
mogli[n-1,:,0,1]= False
mogli[:,0,1,0]= False
mogli[:,n-1,1,1]= False
rng = np.random.default_rng()
start = get_random_edge_coord(n, rng)
end = get_random_edge_coord(n, rng)
mogli[end]
while np.array_equal(start, end):
    end = get_random_edge_coord(n, rng)
print(start,end)


# --- VISUALIZATION ---

# 1. Reshape (n, n, 2, 2) array into a continuous 2D matrix (2n x 2n)
visual_grid = mogli.transpose(0, 2, 1, 3).reshape(2 * n, 2 * n)

# 2. Setup plot
fig, ax = plt.subplots(figsize=(7, 7))
ax.imshow(visual_grid, cmap="gray", origin="upper", vmin=0, vmax=1)

# 3. Add major grid lines (boundaries between main N x N cells)
ax.set_xticks(np.arange(-0.5, 2 * n, 2))
ax.set_yticks(np.arange(-0.5, 2 * n, 2))
ax.grid(color="red", linestyle="-", linewidth=2)

# 4. Highlight Start (Green) and End (Red) cells
# Convert cell coordinates (r, c) to visual matrix coordinates (2*c, 2*r)
ax.add_patch(
    plt.Rectangle(
        (start[1] * 2 - 0.5, start[0] * 2 - 0.5),
        2,
        2,
        fill=True,
        color="lime",
        alpha=0.4,
        label="Start",
    )
)
ax.add_patch(
    plt.Rectangle(
        (end[1] * 2 - 0.5, end[0] * 2 - 0.5),
        2,
        2,
        fill=True,
        color="red",
        alpha=0.4,
        label="End",
    )
)

# Hide axis tick labels
ax.set_xticklabels([])
ax.set_yticklabels([])
plt.legend(loc="upper right")
plt.title(f"{n}x{n} Maze Grid (Start: {start}, End: {end})")
plt.tight_layout()
plt.show()
