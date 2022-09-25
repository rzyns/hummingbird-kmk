# hummingbird-kmk
KMK implementation for hummingbird keyboard

# Setup

* Set environment variable `GIT_DIR` to where you want to keep the bare repository
* Set environment variable `GIT_WORK_TREE` to where the `CIRCUITPY` volume is mounted

## Example

```shell
CIRCUITPY_PATH="$(mount | egrep -o '/(\w+/)*CIRCUITPY')"
cd "$CIRCUITPY_PATH"
cat > .envrc <<-EOF
	export GIT_DIR="${HOME}/git/keebs/hummingbird-kmk.git"
	export GIT_WORK_TREE="${CIRCUITPY_PATH}"
EOF
direnv allow .
```
