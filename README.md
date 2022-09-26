# hummingbird-kmk
KMK implementation for hummingbird keyboard

# Setup

1. Clone repository with `--bare` flag to suppress setting up the working directory
1. Set environment variable `GIT_DIR` to where you want to keep the bare repository
1. Set environment variable `GIT_WORK_TREE` to where the `CIRCUITPY` volume is mounted

## Example

```shell
BARE_REPO_PATH="path/to/clone/hummingbird-kmk.git"
CIRCUITPY_PATH="$(mount | egrep -o '/(\w+/)*CIRCUITPY')"

git clone --bare git@github.com:rzyns/hummingbird-kmk.git "${BARE_REPO_PATH}"

cd "$BARE_REPO_PATH"
git config core.bare false
git config core.worktree "$(realpath --relative-to="$PWD" "$CIRCUITPY_PATH")"

git clone --bare git@github.com:KMKfw/kmk_firmware.git modules/lib
cd modules/lib
git config core.bare false
git config core.filemode false
git config core.logallrefupdates true
git config core.sparseCheckout true
echo 'kmk' > info/sparse-checkout
git config core.worktree "$(realpath --relative-to="$PWD" "$CIRCUITPY_PATH/lib")"

cd "$CIRCUITPY_PATH"

cat > .envrc <<-EOF
	export GIT_DIR="${BARE_REPO_PATH}"
	export GIT_WORK_TREE="${CIRCUITPY_PATH}"
EOF

direnv allow .

git checkout
git submodule update --init --recursive
```
