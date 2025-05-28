
# NumPy Notes 🧠

These are my personal notes on NumPy as part of my AI/ML learning journey.

## 📌 Basics
- `np.array()` – Create arrays from lists or tuples.
- `np.arange(start, stop, step)` – Create evenly spaced values within a range.
- `np.linspace(start, stop, num)` – Create evenly spaced values between start and stop.

## 🔧 Array Creation Functions
- `np.zeros(shape)` – Create array filled with 0s.
- `np.ones(shape)` – Create array filled with 1s.
- `np.full(shape, value)` – Create array filled with a specific value.
- `np.eye(N)` – Identity matrix.
- `np.identity(n)` – Identity matrix (like `eye`).
- `np.empty(shape)` – Create empty array (uninitialized values).
- `np.zeros_like(arr)`, `np.ones_like(arr)`, `np.full_like(arr, value)` – Create arrays with same shape as `arr`.

## 🧮 Operations
- Vectorized operations (e.g., `a + b`, `a * b`) are faster and preferred over loops.
- Broadcasting: Automatically expands arrays for operations between different shapes.
- Element-wise math: `np.add()`, `np.subtract()`, `np.multiply()`, `np.divide()`

## 🧪 Indexing & Slicing
- `arr[1:5]`, `arr[:, 0]`, `arr[1:3, 2:4]`
- Boolean Indexing: `arr[arr > 5]`

## 🎲 Random Numbers
- `np.random.rand()`, `np.random.randint(low, high, size)`

## 📐 Shape & Reshape
- `.reshape(new_shape)`, `.flatten()`, `.ravel()`
- `.shape`, `.ndim`, `.size`

## 🔄 Aggregations
- `np.sum()`, `np.mean()`, `np.median()`, `np.std()`, `np.max()`, `np.min()`
- Axis-based: `arr.sum(axis=0)` (columns), `arr.sum(axis=1)` (rows)

## 🤝 Useful Utilities
- `np.where(condition, x, y)` – Vectorized if-else.
- `np.unique(arr)` – Unique values.
- `np.sort(arr)` – Sort array.

---

More coming soon as I learn! 🚀
